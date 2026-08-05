# Provider request egress design

This document proposes a long-term architecture for the provider-prompt boundary in OpenClaw. In short, build the real request first, then measure and decide on that exact object, and stop keeping separate records of things that might happen. PR #116551 ships as the bridge, and its scaffolding gets deleted at the end.

## The plain version

OpenClaw decides whether to shorten the conversation by measuring one version of the prompt, then sends a different version to the model. Wrappers change the request after it gets measured, so the measurement can be wrong in both directions. The model loses detail it could have kept, or the provider rejects a request we thought would fit.

The same thing happens with bookkeeping. OpenClaw writes down "this turn was sent" before the request provably goes out. When the request dies on the way, the record is wrong, and other behavior built on that record goes wrong with it.

The fix has two parts. Build the actual request first and measure that, so the measured thing and the sent thing are the same object. Then replace every "we think it happened" record with a record made by the one piece of code that truly sent it.

## Problem

OpenClaw decides whether to compact or send by estimating the token pressure of an agent-level `Context`. The bytes that actually leave are produced later, inside each transport, and then rewritten by an open chain of `onPayload` hooks.

The Codex web-search wrapper swaps a 498-token managed tool for a 23-token native one after the estimate is taken. Code mode filters the tool list in the same hook. `createOpenAICompletionsExtraBodyWrapper` (src/agents/embedded-agent-runner/extra-params.ts:789) lets user config overwrite `messages` and `tools` wholesale. Each of these is a place where the measured object and the sent object diverge, and each review round of PR #116551 has found another one.

Alongside the estimate, the runner keeps records of things it predicts will happen. `sentUserTurnIds` in session-prompt-state.ts, the tool-result projection adoption, and the `providerCalls` counter in attempt-prompt-submit.ts are all written by code that has not yet observed a request leaving the process.

PR #116551 dragged those writes to a dispatch-commit hook that fires after the final pre-send check. That is later than before, but it is still a prediction. The patches are individually correct and collectively non-convergent, because the architecture keeps producing new divergence points faster than they can be guarded.

## Root cause

The request does not exist when the decision is made. Each transport builds its wire body at the last possible moment (`buildParams` at packages/ai/src/providers/openai-completions.ts:173, openai-responses-shared.ts:575, google-shared.ts:433, anthropic.ts:388).

The only seam before dispatch is the `onPayload` callback, which exists for patching. It was never meant for observation. Because patching was the only seam, fifteen-odd wrappers in extra-params.ts and src/llm/providers/stream-wrappers/openai.ts stacked onto it. Anything upstream that wants to know what will be sent must simulate the whole stack.

The accounting context in provider-prompt-accounting.ts is exactly that simulation. It is a hidden-symbol side channel that every payload-mutating wrapper must mirror by hand, and extensions/openai/native-web-search.ts already carries a hand-written duplicate of its own payload patch just so admission measures the right tool surface. A design that requires every future wrapper author to remember a parallel bookkeeping call does not converge.

The second cause is that "this request was sent" has no owner. Nothing records dispatch as a fact, so each consumer invented its own marker: `markSentToProvider`, `sentUserTurnIds`, the projection adoption, the `providerCalls` counter. All of them commit at points chosen because they were probably safe, without being observed. When the point turns out to be wrong, the records lie, and the fix so far has been to move the commit point again.

## Design

The target architecture makes the request a first-class object. Two registry-level operations exist per provider family, and one ordered transform plan runs between building and measuring.

### Request materialization

Each provider module in packages/ai splits its lifecycle function at the point where `buildParams` returns. The build half becomes an exported `materializeProviderRequest(model, context, options)` that produces the exact wire body for that family. The send half becomes `dispatchProviderRequest(materialized, options)`, which takes the materialized object and streams the response.

The existing `StreamFn` contract survives as the composition of the two halves, so callers that never cared about the boundary keep working unchanged. Payload shapes stay family-specific. The runtime registry in src/llm/stream.ts gains the two operations next to `stream`, and a family that has not been split yet falls through to the composed path.

### The egress plan

Every transform that changes what the model sees moves out of `onPayload` closures into a `requestTransforms` array on the stream options. The transport applies the plan immediately after the body is built and before anything measures it.

The runner composes the plan once per run from the same sources that build the wrapper onion today. Config-driven transforms come from extra-params.ts (`extra_body`, `chat_template_kwargs`, `parallel_tool_calls`, store stripping). Provider-family transforms come from stream-wrappers/openai.ts (service tier, text verbosity, reasoning effort, Responses payload policy, code-mode filtering, the Codex web-search swap). Plugin transforms arrive through a new plugin SDK seam that replaces `streamWithPayloadPatch` for request mutation. Order within the plan reproduces today's onion order so materialized bytes do not drift during migration.

Stream wrappers do not disappear. Wrappers that normalize the response side, such as DeepSeek `reasoning_content` handling and MiMo thinking-as-text, keep the `StreamFn` shape because they never touch prompt size. The plan enforces one narrow rule that is easy to check. After `requestTransforms` runs, nothing may change the request. `onPayload` stays temporarily as a deprecated observation-only hook and is removed at the end of the migration.

### Admission on the real object

The runner's outermost streamFn wrapper, today installed through `installProviderPromptContextAdmission`, becomes straight-line code that projects the context, materializes the request, measures it, decides, then dispatches.

provider-prompt-admission.ts survives with its projection loop intact, because tool-result truncation legitimately operates on messages before the request exists. Its measurement input changes from `context.messages` plus the accounting context to the exact materialized request. The overflow loop becomes project, materialize, measure, then on overflow reproject tighter and rematerialize, which costs one extra build only on the overflow path.

`MidTurnPrecheckSignal` and its re-raise dance in attempt-prompt-submit.ts stay for now. They are AgentCore control flow, and they can be revisited once AgentCore grows a typed pre-dispatch rejection channel.

### Disposition of current mechanisms

provider-prompt-state.ts is deleted at the end of the migration. The identical-replay guard is genuinely useful and moves into the runner's attempt state as a plain object passed explicitly, computed on the materialized request. The global singleton keyed by runId and its `clearProviderPromptState` lifecycle go away.

The final-payload overflow guard becomes a development-build assertion that measured digest equals dispatched digest. It stays through the migration as the canary that proves nothing downstream mutates the request, then gets deleted once the transform plan is the only mutation path.

The `contextAdmission` and `promptDispatch` hook installation is replaced by the straight-line materialize/dispatch code. The `attemptPayloadObserved` settling fields exist only to cope with transports that silently skip `onPayload`, and materialization is not skippable, so they are deleted.

provider-prompt-accounting.ts is deleted entirely, along with its propagation code in stream-wrappers/openai.ts and extensions/openai/native-web-search.ts. Measuring after the transform plan makes the side channel's job structural.

## Truth from proof

The doctrine here is single-owner recording rather than zero recording. A dispatch is a real event, and the code that performs it is the only code allowed to record it.

The dispatcher emits one event, `provider.request.dispatched`, carrying the run id, the request digest, the ids of user turns contained in the request, and the projection candidate identity. The event lands in the run's event stream, the same path that already carries `provider.prompt.observed`. Everything the extra records answered is derived from that event plus the append-only transcript.

For `sentUserTurnIds`, the question consumers actually ask is whether the bytes of a user turn crossed the LLM boundary, because that decides whether late-resolved media appends as a new turn or rewrites the original (the #99495 fix). A turn counts as sent if any dispatch event in this session includes its idempotency key. Across process restarts, where the in-memory event stream is gone, it counts as sent if the transcript contains an assistant message after it.

An aborted request still counts as sent, because dispatch happened and the provider may have cached the prefix. The event is emitted when the transport hands the body to the HTTP client, so an abort between dispatch and first token retains it. A turn dispatched in a process that crashed before any response persisted is treated as unsent after restart. That can rewrite one prompt-cache slot, and it trades that rare cache miss for never lying in the durable record.

For projection adoption, the candidate projection travels inside the materialized request. Adoption becomes the line after `dispatchProviderRequest` is called, in the same function, with no `pendingDispatchCommit` closure trampolined through a hook. Mid-turn tool loops need no special casing. Each iteration is one materialize/dispatch pair emitting one event, and sent turns accumulate monotonically.

For `providerCalls`, the counter's only job is gating the mid-turn precheck to calls after the first. It is replaced by counting dispatch events for the run, and probably by nothing, because once admission measures the real request cheaply on every call, gating the precheck to later calls loses its reason to exist. That last simplification is decided in the step that lands it.

## Migration

Each step lands independently and names what it deletes.

**Step 1, shipped.** PR #116551 is the bridge, carrying admission at the provider boundary, the accounting context, the final-payload guard, and dispatch-boundary commits. Everything below removes it piece by piece.

**Step 2, transport split.** Split each provider lifecycle in packages/ai at the `buildParams` return into exported materialize and dispatch halves, with the existing stream entry becoming their composition. One PR per family, or two families per PR: openai-completions, openai-responses-shared plus openai-chatgpt-responses, google-shared, anthropic, mistral. Pure refactor, proven by existing suites plus new materialization snapshot tests. Nothing deleted yet.

**Step 3, transform plan.** Add `requestTransforms` to the stream options in @openclaw/ai and apply it in each transport after build. Convert the payload-mutating wrappers in extra-params.ts and stream-wrappers/openai.ts, and the two web-search wrappers, into registered transforms. Each converted wrapper is deleted in the same PR, and its `onPayload` closure with it. The delete criterion per PR is that the converted path no longer appears in an `onPayload` grep of the touched files and the materialized-bytes snapshot for that family is unchanged.

**Step 4, exact admission.** Rewire the runner's streamFn wrapper to materialize, measure, decide, dispatch. Point provider-prompt-admission.ts at the materialized request. Delete provider-prompt-accounting.ts, its propagation in stream-wrappers/openai.ts and extensions/openai/native-web-search.ts, and the accounting parameter threading in provider-prompt-state.ts. Demote the final-payload guard to a dev-build digest assertion. The delete criterion is that `readProviderPromptAccountingContext` has no callers.

**Step 5, dispatch events.** Emit `provider.request.dispatched` from the dispatch call site and derive turn-sent state from it. Migrate the recorder's `markSentToProvider` callers to the derivation. Delete `sentUserTurnIds`, `markSessionUserTurnsSent`, `hasSessionUserTurnBeenSent`, the `pendingDispatchCommit` closure, the `promptDispatch` hook, and the `providerCalls` counter. The delete criterion is that session-prompt-state.ts contains only the projection types and the event-derived accessors.

**Step 6, state teardown.** Move the replay guard into attempt-owned state and delete provider-prompt-state.ts, including the global singleton, `clearProviderPromptState`, the observation-settling fields, and the dev-build digest assertion once it has run clean through a release cycle. The delete criterion is that the file is gone and no `Symbol.for("openclaw.providerPromptStates")` remains.

**Step 7, SDK deprecation.** Deprecate request mutation through `onPayload` and `streamWithPayloadPatch` in the plugin SDK under the shipped-contract exception. The transform seam is the new API, bundled callers are already migrated in step 3, and external plugins get a deprecation window and a documented migration before the mutating form is removed.

**Step 8, calibration.** Optional and last, this step adds observed-usage margin calibration and edge-zone count-tokens consultation.

## Risks and bounds

Late-media prompt-cache behavior (#99495) depends on the sent marker firing at the right moment. The dispatch event fires at the same boundary the current `promptDispatch` hook does, so behavior is preserved. The existing late-media regression test plus one new fault-injection case, media resolving after dispatch and appending instead of rewriting, bound it.

Third-party transports that implement neither the split nor `onPayload` are today's silent divergence case. In the new design the registry knows whether a family provides materialize, and a family that does not falls back to context-level estimation with the `pressureSource` recorded as an estimate, surfaced in the context-budget status instead of silently trusted. That is strictly better than today, and the plugin SDK surface makes the capability explicit for plugin-provided transports.

Context-engine compaction ownership does not move. Admission still returns a recovery route and the runner still compacts through the context engine; only the measurement input changed. Compaction sees agent messages while admission measures wire bytes, so the recovery request keeps reporting both the overflow tokens and the reducible chars, as it does now.

Performance of building before deciding is bounded by what already happens. The current code walks every message in the estimator and then `stableStringify`s the full payload for the replay digest on every call, so materializing once and reusing the serialization for measurement and digest is roughly net neutral. A benchmark on a long transcript of 200 or more messages, before and after step 4, is the gate.

Byte drift during migration is the quiet risk, since reordering transforms could change materialized bytes and invalidate provider prompt caches for live sessions. The bound is the per-family snapshot suite introduced in step 2, asserting byte-identical output between the wrapper onion and the transform plan for representative contexts before each conversion PR lands.

## Verification

The invariant the design exists to establish is that the measured request and the dispatched request are the same object. Development builds check it on every call through the digest assertion. A property-style suite runs representative transform plans, including `extra_body` replacing `messages`, the code-mode filter, and both web-search swaps, and asserts measured digest equals dispatched digest for every family. The historical incidents become named regression tests. The web-search case asserts the measured tool surface is the native 23-token tool instead of the 498-token managed one, and the extra-body case asserts admission sees the replacement messages.

Record removal is proven by fault injection at the boundary, per the repo's testing doctrine. Kill the transport before dispatch and assert no turn is marked sent, no projection is adopted, and the retry materializes fresh. Abort after dispatch and assert the turn is sent and late media appends. Restart mid-turn and assert the transcript-derived fallback gives the conservative answer. A mock-gateway harness run covering a full tool loop with one induced overflow provides the channel-visible proof for the landing PR.

Live proof closes the loop on measurement with one session per provider family logging estimated tokens against `usage.input`, the delta expected inside the calibrated margin, and the context-budget status showing `pressureSource` as the materialized request. The old failure modes are demonstrated gone when the PR #116551 regression suite passes with provider-prompt-accounting.ts, the final-payload guard, and the dispatch-commit hook deleted, because those tests encoded each historical divergence and now hold without the scaffolding that patched them.
