# OpenClaw tool-loop recovery implementation plan

## Goal

Build a production tool-loop recovery path in `onurclaw` and use that implementation to prepare a provider-neutral OpenClaw contribution.

The current delivery target is the existing `extensions/llama-server` provider. Its public `wrapStreamFn` boundary runs before every model request and receives OpenClaw's normalized context. The extension will detect a repeated no-progress tail there, submit one text-only recovery request, and reject any tool call returned from that request.

The long-term OpenClaw design moves detection and run control into the agent harness, along with persistence. The provider extension then keeps only model matching and Qwen-specific wording.

```text
current
  osolmaz/onurclaw/extensions/llama-server
    normalized-context recovery and output guard

future
  openclaw/openclaw
    provider-neutral recovery controller and persistence

  bundled or external llama.cpp provider
    Qwen recovery profile
```

The current implementation must use public Plugin SDK imports and OpenClaw's shared transport. It must not patch an OpenClaw checkout or register another provider identity.

## Evidence behind the design

Bob ran OpenClaw `2026.7.2` with `llama-server/qwen3.6-35b-a3b`. After an `exec` command returned the same `(no output)` result, Qwen repeated the same explanation and command until the user aborted the turn.

The investigation established these facts:

- OpenClaw sent valid OpenAI-compatible assistant tool calls and matching tool-role results.
- The final tool result told Qwen that the call had been blocked as a critical loop.
- A direct replay against the same llama-server with `cache_prompt: false` produced the same 172-token explanation and identical command.
- Prompt caching and compaction did not cause the repeated generation. Tool-role ordering was valid.
- OpenClaw kept calling the model after its detector blocked the tool. This allowed Qwen's repeated generation to become a runaway run.

OpenClaw PR [#110633](https://github.com/openclaw/openclaw/pull/110633) adds a typed critical-loop signal and a single terminal owner. This plan builds on that direction. It must not add a competing termination path.

## Current success criteria

The OnurClaw work is complete when all of the following are true:

- Recovery is disabled by default and enabled only for exact canonical model references.
- Two contiguous calls with the same tool, normalized arguments, and model-visible outcome trigger recovery before another model request can generate the same call.
- The provider-bound recovery context retains one tool cycle, summarizes the repeat, and exposes an empty tool list.
- The model receives a short runtime-authored explanation of the loop and its allowed choices.
- A text response completes the turn normally.
- The extension buffers the recovery response and replaces any returned tool call with one terminal explanation.
- Normal model calls keep their existing streaming behavior.
- The stored OpenClaw transcript remains unchanged.
- Detection is bounded and scoped to configured tool names. The default scope contains only `exec`.
- The extension uses only public Plugin SDK imports.
- A backed-up copy of Bob's problematic session reproduces the repeated tail in an isolated test.
- A live request built from that tail returns text, contains no tool call, and sends one provider request.
- Bob's original Discord session keeps the same session ID, event count, compaction count, and killed status during testing.

## Upstream success criteria

The later OpenClaw contribution is complete when core owns the signal, one-attempt run state, deterministic replay projection, persistence, and terminal handling. The later criteria in this plan describe that target. They do not authorize changes to an OpenClaw checkout during the OnurClaw implementation.

## Design rules

### One owner for each concern

The detector decides that a loop exists. The run controller decides whether to recover or stop. The context projector decides what the model sees. The provider sends the resulting snapshot. The extension contributes policy but cannot execute retries or terminate runs.

### Side effects stop before recovery

Recovery begins when the model proposes the next repeated call. OpenClaw blocks that call before tool execution. The previous completed outcomes provide the evidence for recovery.

### One recovery attempt

The first version fixes the recovery limit at one. Configuration must not raise it. A later increase would need new evidence that multiple recovery calls improve completion without creating another loop or spending path.

### Text-only recovery

The recovery request has an empty tool surface. If a provider still emits a tool call, OpenClaw rejects it and ends the run. The call never reaches the tool registry.

### Exact detection first

The first implementation compares normalized tool identities, effective arguments, and model-visible outcomes. It does not use fuzzy command similarity or an LLM judge. Tool-specific progress classifiers can be added later behind the same contract.

### Immutable raw history

Recovery does not delete or rewrite raw transcript events. OpenClaw stores a recovery record that tells prompt construction which repeated span to summarize. This keeps audit history and deterministic replay.

## Current extension flow

The OnurClaw extension handles the loop at the normalized stream boundary:

```text
two completed identical no-progress cycles
  |
  | next provider call enters wrapStreamFn
  v
collapse repeated tail and remove submitted tools
  |
  | one buffered recovery request
  v
text response -> complete
  |
  | provider still emits a tool call
  v
replace with one terminal text response
```

This path prevents another tool call from reaching OpenClaw. It leaves the raw transcript intact. OpenClaw's built-in loop detector remains the final run-level circuit breaker.

## Future core flow

The upstream run controller should follow this state machine:

```text
running
  |
  | model proposes another identical no-progress call
  v
recovery pending
  |
  | block before execution and emit a typed signal
  v
recovering
  |\
  | \ tool call, provider error, cancellation, or invalid state
  |  \
  |   v
  |  blocked
  |
  | text response
  v
complete
```

Only the outer run controller changes state. Tool wrappers report observations and signals but do not start model calls themselves.

## Detection contract

OpenClaw already records tool calls and outcomes for loop detection. Extend that path with a recoverable signal before the critical terminal signal.

A draft normalized execution record is:

```ts
type ToolLoopExecutionRecord = {
  runId: string;
  ordinal: number;
  toolCallId: string;
  toolName: string;
  toolKind?: string;
  effectiveArgumentsHash: string;
  modelVisibleOutcomeHash: string;
  outcome: "success" | "error" | "blocked";
};
```

The hashes must be derived from the same values used by the actual execution and provider replay paths:

- Tool name and kind come from the host tool registry.
- Arguments are captured after trusted policy and plugin rewrites.
- Execution target information is included when it changes the meaning of a call.
- Outcome text is captured after model-visible result middleware and before provider-specific serialization.
- Volatile IDs, timestamps, progress counters, and UI-only details are excluded.

The detector emits structured facts. It does not own the user-facing warning string:

```ts
type ToolLoopInterventionSignal = {
  detector: ToolLoopDetectorKind;
  count: number;
  toolName: string;
  toolKind?: string;
  coveredToolCallIds: string[];
  retainedToolCallId: string;
  outcomeClass: "empty" | "error" | "blocked" | "identical";
  severity: "recoverable" | "critical";
};
```

The exact field names should follow the merged form of PR #110633. The implementation should extend that signal and avoid a parallel observer.

### Trigger order

The detector should support this order:

1. A warning may be emitted at the existing warning threshold.
2. A recoverable signal is emitted when the next repeated call can be blocked before execution.
3. A critical signal ends the run when recovery is unavailable, already used, or unsuccessful.
4. The global circuit breaker remains the last fallback for loop forms that the focused detectors miss.

For Bob's first deployment, explicit thresholds can be lower than the current 10/20/30 defaults. Upstream defaults should remain unchanged and recovery should start disabled until the live test set has enough evidence.

## Recovery controller

Add a `ToolLoopRecoveryController` owned by the embedded run loop. It should have no provider-specific branches.

The controller receives the signal, current run state, cancellation state, active model, and the exact normalized context that would otherwise continue to the provider. It returns one of three decisions:

```ts
type ToolLoopRecoveryDecision =
  | { action: "recover"; plan: ToolLoopRecoveryPlan }
  | { action: "block"; reason: string }
  | { action: "ignore" };
```

`ignore` is valid only for a warning-level observation. A critical signal cannot be ignored.

A recovery plan contains structured data that the shared prompt path can serialize:

```ts
type ToolLoopRecoveryPlan = {
  recoveryId: string;
  signal: ToolLoopInterventionSignal;
  instruction: string;
  tools: "none";
  maxAttempts: 1;
};
```

The controller must enforce these invariants:

- At most one plan is accepted for a run.
- Existing user or plugin cancellation wins over recovery.
- Recovery never resets the critical-loop history.
- Provider failover, overflow handling, and compaction cannot create a second logical recovery attempt.
- Recovery completion releases the session lane.
- Failure produces one visible terminal message and one blocked run result.

## Recovery context

The model should not receive twenty copies of the behavior it must stop. OpenClaw should build a recovery projection from normalized messages before provider serialization.

The projection should:

1. Preserve all messages before the detected loop span.
2. Keep the first valid assistant tool-call and tool-result pair.
3. Remove later pairs covered by the recovery record.
4. Add a short note to the retained tool result stating how many times the same action produced the same outcome.
5. Append a runtime-authored recovery instruction after the retained result.
6. Set the submitted tool list to an empty array.

The instruction should say what happened and what the model may do. The generic form is:

> OpenClaw stopped a repeated tool call because the same action produced no new evidence. Do not call tools in this response. Use the evidence already available, explain what access or information is missing, or ask one concise clarifying question.

Provider or model policy may replace this wording, but it cannot add tools or request another retry.

### Snapshot identity

Build one `RecoveryPromptSnapshot` after projection. The preflight estimator, mid-turn pressure checks, context diagnostics, cache trace, and stream function must all receive that snapshot. No later hook may rebuild the message list from the unprojected session branch.

The projector should preserve object content and ordering before the first affected pair. This keeps the prompt-cache prefix reusable. The loop tail is recent, so invalidation begins near the end of the prompt.

## Persistence and replay

Persist a first-class recovery record in the session transcript or session event store:

```ts
type ToolLoopRecoveryRecord = {
  version: 1;
  recoveryId: string;
  runId: string;
  detector: ToolLoopDetectorKind;
  coveredToolCallIds: string[];
  retainedToolCallId: string;
  toolNames: string[];
  repeatCount: number;
  outcomeClass: "empty" | "error" | "blocked" | "identical";
  createdAt: number;
};
```

The record must not copy raw arguments or tool output. Those values already exist in the transcript and may contain sensitive data.

Prompt construction uses the record to reproduce the same collapsed history after reload. Compaction may absorb the record once its summary includes the stopped loop. Until then, compaction and branch operations must retain the record with the active path.

A crash between recording the plan and finishing recovery must not run the blocked tool after restart. The next load may either resume the text-only recovery once or expose the blocked terminal result. It must never return to ordinary tool execution without an explicit new user turn.

## Public Plugin SDK contract

A plugin needs a narrow way to contribute recovery policy without gaining control of the run loop. Add a registration surface such as:

```ts
api.registerToolLoopRecoveryProfile({
  id: "qwen-local",
  match: {
    providers: ["llama-server"],
    modelIds: ["qwen3.6-35b-a3b"],
  },
  buildInstruction(event) {
    return "...";
  },
});
```

The final API may instead be a provider hook if OpenClaw maintainers want recovery profiles owned by provider plugins. Both forms must keep these constraints:

- Matching uses exact canonical provider and model IDs.
- The event contains detector facts and omits raw conversation history.
- The result may supply an instruction and safe label only.
- The result cannot alter thresholds, tools, retries, persistence, or termination.
- OpenClaw has a generic fallback when no profile matches.
- Multiple matches fail closed with a clear diagnostic. Plugin load order cannot choose the winner.

The SDK addition needs package-surface tests, manifest contract coverage, trust documentation, and an example extension.

## OnurClaw extension

Add the current implementation to the existing provider:

```text
extensions/llama-server/
├── index.ts
├── openclaw.plugin.json
├── PROVIDER.md
└── src/
    ├── loop-recovery.ts
    ├── loop-recovery.test.ts
    ├── stream.ts
    └── stream.test.ts
```

`loop-recovery.ts` is a pure normalized-context transformer plus a buffered output guard. `stream.ts` calls it before invoking OpenClaw's shared `streamSimple` transport. The implementation must not inspect serialized HTTP JSON, maintain a private session database, or install another provider.

Initial configuration is explicit and small:

```json5
{
  plugins: {
    entries: {
      "llama-server": {
        config: {
          loopRecovery: {
            enabled: true,
            models: ["llama-server/qwen3.6-35b-a3b"],
            repeatThreshold: 2,
            tools: ["exec"]
          }
        }
      }
    }
  }
}
```

Keep the model list required. Do not infer every model whose name contains `qwen`. Reject unknown fields and malformed canonical model references. The provider guide must state that this is a provider-bound recovery projection and that OpenClaw's core detector remains enabled.

## Core configuration

Recovery policy belongs under the existing loop detector:

```json5
{
  tools: {
    loopDetection: {
      enabled: true,
      warningThreshold: 2,
      recovery: {
        enabled: true,
        threshold: 3
      },
      criticalThreshold: 4,
      globalCircuitBreakerThreshold: 5
    }
  }
}
```

These values are an example for Bob's bounded evaluation. Upstream defaults remain unchanged. Validation must require:

```text
warningThreshold < recovery.threshold < criticalThreshold
criticalThreshold < globalCircuitBreakerThreshold
historySize >= globalCircuitBreakerThreshold
```

The first schema exposes only `enabled` and `threshold` under `recovery`. The one-attempt limit and text-only tool policy remain fixed behavior.

## Implementation sequence

### OnurClaw delivery

1. Back up Bob's authoritative SQLite session database with `sqlite3 .backup`, record the session identity and event count, and verify the backup with `PRAGMA quick_check` plus SHA-256.
2. Add strict `loopRecovery` plugin configuration with exact model references, a bounded repeat threshold, and an explicit tool allowlist.
3. Implement exact contiguous-tail detection over normalized `Message[]` values.
4. Keep the first tool cycle, annotate its repeated outcome, append the recovery instruction, and pass an empty tool list to the shared transport.
5. Buffer only recovery responses. Replace a returned tool call or recovery-stream failure with one terminal text response.
6. Add unit tests for matching, non-matching, argument canonicalization, changed outcomes, multi-tool calls, default polling exclusions, output guarding, and stream integration.
7. Reconstruct the repeated tail from the backed-up session without adding raw session data to Git.
8. Run one live request through the official pinned llama.cpp runtime with prompt caching disabled or clearly reported. Verify one request, text output, and zero tool calls.
9. Install the tested extension for Bob, enable it only for the exact Qwen model, restart the foreground gateway, and run an isolated session fork.
10. Delete the diagnostic fork after verification and prove that the original session remained unchanged.

### Future critical termination foundation

1. Track PR #110633 and confirm its final signal, cancellation, and terminal-owner contracts.
2. Rebase later core work onto the merged implementation or coordinate directly with that PR if upstream recovery development starts earlier.
3. Add a regression test showing that critical handling makes no provider request after the blocked tool call.
4. Keep critical termination independently useful when recovery is disabled.

### Recoverable signal

5. Add `recovery` configuration and validation beside the current loop detector settings.
6. Extend the detector result with a recoverable severity and the tool-call IDs needed for projection.
7. Emit the recoverable signal before executing the triggering duplicate call.
8. Preserve outcome ordering for sequential and parallel tool calls.
9. Add matching relay behavior for Codex and Copilot without letting those harnesses invent their own recovery rules.

### Run controller

10. Add the recovery state machine to the single run-terminal owner.
11. Make cancellation, critical termination, overflow recovery, and recovery attempts share one attempt budget and one lane owner.
12. Reject a second recovery plan in the same run.
13. Enforce a text-only result and convert any recovery tool call into a terminal blocked result.
14. Emit structured diagnostics without logging raw arguments or results.

### Context and persistence

15. Add the recovery record to session storage and active-path readers.
16. Implement the deterministic normalized-message projector.
17. Build one recovery snapshot and use it through estimation and provider submission.
18. Preserve recovery records across reload, branch operations, and compaction until they are absorbed into a summary.
19. Add crash-recovery tests for interruption before and during the recovery provider call.

### Plugin SDK and extension

20. Add the smallest public profile registration or provider hook accepted by OpenClaw maintainers.
21. Add Plugin SDK surface, trust, conflict, and compatibility tests.
22. Create `onurclaw/extensions/tool-loop-recovery` against that public contract.
23. Register only explicitly configured canonical Qwen model references.
24. Add the Qwen instruction and focused extension tests.
25. Document installation, configuration, recovery behavior, and removal.

### Live validation

26. Reconstruct the sanitized Bob loop fixture from persisted transcript evidence.
27. Prove that the third duplicate `exec` call is not executed.
28. Prove that exactly one text-only request reaches llama-server.
29. Run the same test with `cache_prompt: false` and with guarded prompt caching enabled.
30. Confirm that the recovery response is persisted and that the next user turn reuses the session normally.
31. Confirm gateway and llama-server health and inspect logs for fallback, CUDA, OOM, and stream errors.

## Test plan

### Detector tests

Cover exact repeat, changed arguments, changed outcomes, ping-pong calls, known polling tools, plugin vetoes, approval denials, parallel outcomes, run boundaries, and volatile result metadata. The new recovery threshold must not weaken existing warning or critical behavior.

### Controller tests

Prove one recovery attempt, cancellation precedence, terminal ownership, provider failure, output containing a tool call, overflow during recovery, compaction pressure, failover behavior, and lane release. Count provider submissions and tool executions directly.

### Projection tests

Use full normalized `Message[]` fixtures. Assert valid tool-call/result pairing, exact covered IDs, unchanged prefix content, bounded annotations, deterministic replay after reload, and no mutation of source messages.

### Storage tests

Exercise SQLite and any compatibility transcript backend supported by the target OpenClaw release. Cover branch switching, rewind/fork rules, compaction, reset, deletion, and crash recovery.

### Plugin tests

Check strict configuration, exact canonical model matching, no match for similarly named models, generic fallback behavior, duplicate profile conflicts, and public-import compliance.

### End-to-end tests

Run embedded, Codex, and Copilot harness scenarios with a deterministic model stub. Each scenario must record the number of model calls, tool calls, stored messages, recovery records, terminal replies, and later same-session turns.

### Live Qwen test

Use the pinned official llama.cpp runtime already registered under `~/runtimes/llama-cpp`. Record the exact runtime revision, model revision, launch command, requested and observed backend, prompt-cache state, context size, and sampling settings.

The live test passes only when:

- two identical no-progress calls may complete,
- the next duplicate is blocked before execution,
- one text-only recovery request is sent,
- Qwen returns text or OpenClaw emits one terminal blocked reply,
- no later provider or tool request occurs,
- the session accepts a new user turn.

## Prompt-cache behavior

Recovery changes only the recent loop span and appends one instruction. The prefix before the retained tool pair must remain byte-equivalent after provider conversion. Cache traces should report the first changed message and show that earlier prompt tokens remain reusable.

Do not make cache hits a correctness dependency. Run every live correctness case once with prompt caching disabled.

## Security and privacy

Tool arguments and results may contain credentials, private paths, URLs, or user data. Recovery records, logs, metrics, and plugin events must use hashes, tool names, counts, and bounded reason codes. The model-visible recovery projection may include the original retained result because it was already part of model context, but it must not copy that content into diagnostics.

A recovery profile is trusted prompt input. Installed plugins must require normal prompt-injection trust. Profile conflicts stop recovery; OpenClaw must never concatenate instructions from several plugins.

The recovery request cannot restore tools through provider payload hooks or later prompt hooks. Tool removal must occur after optional-tool resolution and before the exact provider snapshot is frozen.

## Upstream strategy

Split upstream work so maintainers can review one ownership change at a time:

1. Critical-loop terminal handling, preferably through PR #110633.
2. Recoverable signal and bounded controller with a generic instruction.
3. Persistence and deterministic recovery projection.
4. Public recovery-profile SDK contract.
5. Bundled Qwen profile after live evidence supports it.

The generic controller must work without the OnurClaw extension. This lets OpenClaw merge the safety mechanism before deciding whether Qwen-specific wording belongs in core, the bundled `llama-cpp` extension, or an external package.

Once upstream contains the accepted policy, remove the external OnurClaw extension instead of keeping a compatibility shim. Existing recovery records remain readable through the core schema.

## Bob rollout

Bob remains on the current model and provider identity:

```text
llama-server/qwen3.6-35b-a3b
```

Use an isolated cloned session for the first test. Do not run the proof in the live Discord channel. After deterministic and live tests pass:

1. Stop the gateway cleanly without stopping the operator-managed llama-server.
2. Install the extension build that matches Bob's OpenClaw revision.
3. Enable recovery only for the exact Qwen model reference.
4. Use conservative explicit thresholds from the tested configuration.
5. Start the gateway and run a fresh isolated no-progress fixture.
6. Confirm model-call count, tool-call count, persistence, delivery, and lane release.
7. Run one normal tool turn to check that the detector does not alter successful work.
8. Keep core critical termination enabled as the final guard.

Preserve Bob's sessions, auth profiles, cron jobs, provider endpoint, model parameters, prompt-cache settings, and unrelated files.

## Work outside this plan

This work does not add semantic command equivalence, an LLM loop judge, automatic sampler changes, arbitrary retry counts, or model fine-tuning. It does not treat every repeated polling call as a failure. It does not replace provider overflow handling, compaction, or prompt-cache policy.

The extension does not own llama-server lifecycle, configuration, or health monitoring. It does not change the `llama-server/*` provider namespace.

## Stop conditions

Stop implementation and report the evidence when any of these conditions occurs:

- PR #110633 or its replacement has no stable single-owner terminal signal to extend.
- Recovery requires returning another ordinary blocked tool result to the model.
- The triggering duplicate cannot be stopped before tool execution.
- The current provider implementation would require private OpenClaw imports or serialized HTTP payload rewriting.
- Prompt estimation and provider submission cannot use the same projected snapshot.
- Persistence requires deleting raw transcript evidence.
- Codex or Copilot needs a separate recovery state machine.
- A recovery tool call can reach the tool registry.
- Live Qwen testing needs an unapproved runtime build, model change, or paid compute launch.

A blocked report should name the failed invariant, relevant files and commits, the smallest core or SDK decision needed, and the evidence collected before stopping.
