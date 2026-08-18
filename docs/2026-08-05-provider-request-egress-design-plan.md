---
title: Provider request egress plan
author: Onur Solmaz <2453968+osolmaz@users.noreply.github.com>
date: 2026-08-05
updated: 2026-08-18
---

# Provider request egress plan

OpenClaw must base prompt reduction on the request that it will send. This plan starts from current `main`. PR [#116551](https://github.com/openclaw/openclaw/pull/116551) remains useful test and design evidence. New work starts from a fresh branch.

## Current status

Current `main` includes [#124267](https://github.com/openclaw/openclaw/pull/124267), which anchors prompt pressure to provider-reported usage when that usage is available in the expected form. This helps, but it does not establish that OpenClaw measures the final provider request.

A deterministic local OpenAI Responses test on `f99a0c638ac555d82093779c13403d123fe17961` reproduced the remaining failure. The test requested 30 sequential tool calls with a 50,000-character result from each call. OpenClaw stopped after six calls.

The provider reported 81,684 input tokens for the last accepted request. The prompt budget was 180,000 tokens, leaving 98,316 tokens of headroom. The mid-turn precheck estimated 189,879 tokens and raised a context-overflow error. Its estimate exceeded the provider value by 108,195 tokens, or 2.325 times the provider value.

The earlier live comparison in [#116551](https://github.com/openclaw/openclaw/pull/116551#issuecomment-5241430029) showed the same class of failure against a real provider. The base revision stopped after 16 of 30 tool calls and compacted twice. The PR revision completed all 30 calls without compaction. The sanitized evidence is also available in the linked [test record](https://gist.github.com/abarsegov/56363c22b4d5359bbb3b523d22037be4).

These results justify a structural fix. A small patch that copies OpenAI usage into another field can delay the failure, but it remains one request behind and cannot see later payload changes.

## Problem

OpenClaw estimates prompt pressure from an agent-level context. Provider code later builds the wire request, and payload wrappers can then change messages, tools, media, and request options. Admission can therefore measure one prompt and send another.

The Codex web-search wrapper can replace a large managed tool with a small native tool. Code mode can filter the tool list. Configured `extra_body` values can replace `messages` or `tools`. Future plugins can add more payload changes through the same hook chain.

The runner also records predicted events in several places. Sent-turn state, projection adoption, and provider-call counters are committed at convenient points instead of being derived from an observed request lifecycle. Moving those commit points does not give the events one clear owner.

## Requirements

The implementation must satisfy these rules:

- Admission measures the final provider-visible request.
- Dispatch sends the same prepared request that admission measured.
- An uncertain estimate does not cause destructive compaction.
- Completed tool calls are never replayed during context recovery.
- Tool-result reduction happens before conversation compaction.
- Every built-in transport reports the same request lifecycle stages.
- Provider and plugin compatibility changes follow a bounded migration.
- Logs and metrics do not contain prompt text, tool output, media, or credentials.

## Scope

The first behavior change covers OpenAI Responses, including the ChatGPT and Codex variants that share its request family. It includes request construction, payload transforms, prompt measurement, tool-result reduction, dispatch, and lifecycle records for that family.

Later changes apply the same contract to OpenAI Completions, Anthropic, Google, Mistral, Bedrock, Ollama, and bundled extension transports. Each provider family moves in a separate reviewable change.

## Non-goals

This work does not require an exact tokenizer for every model. It does not change summary quality, summary format, or the normal tool execution contract. It does not rewrite response-only stream wrappers. It does not merge or rebase the old #116551 branch.

## Design

### Prepared provider request

Each provider family splits request construction from dispatch:

```ts
interface ProviderEgress<Body> {
  prepare(context: Context, options: StreamOptions): Promise<PreparedProviderRequest<Body>>;
  dispatch(request: PreparedProviderRequest<Body>, options: DispatchOptions): AssistantMessageEventStream;
}

interface PreparedProviderRequest<Body> {
  requestId: string;
  family: string;
  body: Body;
  digest: string;
  measurement: PromptMeasurement;
  projectionReceipt: ProjectionReceipt;
}
```

The current `StreamFn` API remains available as `prepare()` followed by `dispatch()`. Callers that do not need admission continue to use `stream()` without a behavior change.

A prepared request is immutable by contract. Production code sends its stored body without rebuilding it. Development builds compute a digest before admission and assert that dispatch receives the same digest.

### Ordered request transforms

Every change that affects model-visible input moves into an ordered `requestTransforms` plan. The provider builds its base body, applies the plan once, and then creates the prepared request.

The plan includes config changes such as `extra_body`, provider-family changes such as service tier and reasoning options, code-mode filtering, native web-search conversion, and plugin request transforms. The migration preserves the current wrapper order so the provider-visible request and prompt-cache prefix do not change by accident.

Response-only wrappers remain stream wrappers. No code can change the request after the transform plan completes.

### Prompt measurement

The request body is exact, but its token count is not always exact. The measurement records both the value and the evidence behind it:

```ts
type PromptMeasurement = {
  tokens: number;
  source: "provider_usage" | "provider_tokenizer" | "bounded_estimate" | "local_estimate";
  certainty: "authoritative" | "bounded" | "uncertain";
  outputReserveTokens: number;
};
```

Provider usage is authoritative only for the request digest that produced it. A later request can use that value as an anchor, but it must account for changes in the newly prepared body.

Admission has three outcomes:

- `fits` means reliable evidence places the request below the budget.
- `too_large` means reliable evidence places it above the budget.
- `uncertain` means the estimate crosses the boundary without enough evidence for a destructive change.

An uncertain request is sent. If the provider returns a typed context-limit error, OpenClaw reduces the context and retries once. This follows the safer part of Pi's behavior while still measuring the final OpenClaw request.

### Bounded admission loop

Admission runs immediately before each provider call, including calls inside a tool loop:

1. Project the current context.
2. Prepare and measure the provider request.
3. Dispatch when it fits or remains uncertain.
4. If it is too large, reduce old tool results toward an explicit target.
5. Prepare and measure again.
6. Compact only when reduction cannot reach the target.

The loop has a fixed iteration limit. Every reduction step must produce a smaller prepared request. Context recovery changes only the next provider projection, so completed tools remain completed.

### Request lifecycle

One lifecycle record replaces the current collection of predictive flags:

```text
prepared
admitted
dispatch_started
provider_accepted
completed | failed | outcome_unknown
```

Different consumers use different facts. Prompt-cache accounting can use `dispatch_started`. Accepted-call metrics use `provider_accepted`. Retry policy treats a connection loss after dispatch but before acknowledgement as `outcome_unknown`.

Sent-turn state is derived from these records instead of a separate mutable set. Projection adoption is tied to the prepared request and committed at its defined lifecycle stage. Provider-call counts come directly from lifecycle records.

### Legacy provider capability

The provider registry advertises whether a family supports prepared requests. Converted built-in providers use prepared admission. Unconverted providers keep the current stream path during migration and report that they lack this capability.

A provider that advertises prepared-request support must never fall back silently. Missing preparation, measurement, or lifecycle data is an error in development and test builds. Production diagnostics identify the provider family and failed stage without recording request content.

The public plugin mutation hook gets a documented transform replacement and a bounded deprecation period. Observation hooks can remain, but observation cannot change a prepared request.

## Implementation sequence

Each pull request starts from current `main` and leaves the repository in a working state.

### OpenAI Responses transport split

Split OpenAI Responses request construction from dispatch. Keep `stream()` as their composition and make no admission change. Add snapshots that compare the old wire body with the prepared body for text, tools, media, reasoning, web search, and configured payload overrides.

The gate is byte-equivalent provider input for the test matrix and no change to public stream behavior.

### OpenAI transform plan and admission

Convert every OpenAI Responses payload mutation to the ordered transform plan. Add prepared-request measurement and the bounded admission loop. Add the deterministic 30-call regression and a true-overflow case.

Remove the hard mid-turn estimate for this capable path. Do not add the accounting side channel, global provider-prompt state, or hook propagation from #116551.

The gate is 30 completed calls, no compaction while the prepared request fits, and successful reduction or compaction when authoritative evidence shows a real overflow.

### Lifecycle records

Emit request lifecycle records from the prepared-request path. Move sent-turn decisions, projection adoption, and provider-call accounting to these records. Add fault injection before dispatch, after dispatch, after provider acknowledgement, during streaming, and during process termination.

Delete each superseded flag or counter in the same pull request that moves its last consumer.

### Remaining provider families

Convert one provider family at a time. Each conversion includes body-equivalence snapshots, measurement tests, lifecycle fault tests, and a provider-specific live check when credentials and a safe test route are available.

Response-only wrappers remain unchanged. Provider-specific request transforms move into the common ordered plan.

### Plugin migration and cleanup

Publish the transform API through the plugin SDK. Convert bundled plugins first, document the external migration, and keep the old mutation hook only for the announced compatibility period.

After every built-in provider uses prepared requests, remove the legacy mid-turn precheck, wrapper-side request accounting, temporary digest assertions, and any remaining predictive sent-state code.

### Optional measurement calibration

Compare each prepared-request estimate with the provider usage returned for the same digest. Use this evidence to improve conservative bounds for provider and model families. Calibration must not turn uncertain evidence into an authoritative overflow decision.

## Risks and controls

### Provider request drift

Reordering transforms can change messages, tools, headers, or prompt-cache prefixes. Per-family snapshots compare old and new provider bodies before each conversion lands. The first transport split is a pure refactor so request drift is separate from admission behavior.

### False reduction

A weak estimate can remove useful context. Only authoritative or bounded evidence can produce `too_large`. Uncertain requests are sent and can recover from a typed provider overflow.

### Duplicate work

A failed request can leave dispatch outcome unknown. Lifecycle records keep this state explicit. Context recovery never reruns completed tools, and provider retries follow idempotency support when the provider offers it.

### Performance and memory

Materialization must happen once on the normal path. Dispatch reuses the prepared body and serialization. A benchmark with at least 200 messages, large tool schemas, media, and large tool results compares build time, peak memory, and time to first provider byte before behavior changes are enabled.

### Plugin compatibility

The existing `StreamFn` contract remains. External request mutation moves through a documented deprecation period because OpenClaw has a shipped plugin contract. Converted providers cannot silently use the legacy path.

## Acceptance criteria

The work is complete when all of these statements are true:

- The admitted request digest equals the dispatched request digest.
- The 30-call regression completes all 30 calls without unnecessary compaction.
- A request with at least 98,316 tokens of measured headroom is not rejected by the old local estimate.
- A truly oversized request reduces tool results first and compacts only when needed.
- An uncertain estimate does not trigger compaction.
- No recovery path repeats a completed tool call.
- Failures at each lifecycle stage produce the expected durable and in-memory state.
- Built-in providers use the prepared-request contract or report an explicit legacy capability.
- Plugin SDK API checks and protocol baselines pass.
- No diagnostic output contains provider request content or credentials.
- Performance stays within the limits agreed before the behavior-changing pull request starts.

## Verification

Each provider conversion runs focused provider and agent tests, followed by the repository gates:

```bash
pnpm tsgo:prod
pnpm tsgo:test
pnpm check
pnpm test
```

The focused suite must include payload snapshots, transform ordering, digest identity, measurement certainty, reduction monotonicity, true overflow, uncertain overflow, and lifecycle fault injection.

The OpenAI behavior change also runs the deterministic 30-call local test against an isolated OpenAI-compatible server. A live test then uses the same 30-call shape with a fixed context budget and records request count, provider input usage, admission decisions, compaction count, context-limit errors, and final completion. Live artifacts store only digests and counts.

A provider family is complete only after its focused tests, type checks, repository checks, local behavior proof, and applicable live proof all pass on the exact reviewed revision.

## Open questions

The first transport-split review must settle three details before behavior changes land:

- The stable plugin type for request transforms and provider-family bodies.
- The lifecycle stage used by each existing sent-turn consumer.
- The performance limits for request build time and peak memory.

These questions do not change the main rule. OpenClaw must measure and dispatch the same prepared request, and uncertain measurements must preserve context.
