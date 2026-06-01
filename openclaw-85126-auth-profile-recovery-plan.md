# OpenClaw #85126 Auth Profile Recovery Plan

Status: proposed.

Goal: fix sessions that get stuck on an auto-selected fallback provider/auth profile, such as a MiniMax agent remaining pinned to DeepSeek after fallback.

## Problem

The current failure mode is a self-confirming loop:

1. Agent primary is `minimax/MiniMax-M2.7`.
2. A transient failure falls back to `deepseek/deepseek-v4-flash`.
3. Session state stores DeepSeek model/auth fields with `source: "auto"`.
4. The next turn reads the saved DeepSeek state.
5. Auth resolution validates `deepseek:default` against DeepSeek.
6. The session keeps DeepSeek instead of recovering to MiniMax.

The bug is not that DeepSeek fallback exists. The bug is treating auto fallback state like a durable user choice.

## Design Rule

Provider, model, and auth profile must move as one decision.

- User-selected provider/model/auth state should stick.
- Auto-selected fallback state is temporary recovery state.
- Auth selection should follow the selected provider/model.
- The auth resolver must stay provider-scoped; it should not mix MiniMax and DeepSeek profile orders.
- Do not add a new config value for this bug.
- Do not change the plugin SDK or plugin runtime interface for this bug.

This is an internal core session-state repair. Plugins should keep receiving the
same provider/model/auth inputs they receive today, only with those inputs made
coherent before dispatch.

## Implementation Shape

1. Add or extend a shared core session selection step before agent dispatch.
   - Inputs: configured primary model, stored provider/model fields, stored auth profile fields, source fields, fallback provenance, session key, agent id.
   - Output: one effective selection: provider, model, auth profile, and whether persisted session state should be repaired.
   - This step must be internal to core. It should not expose a new public config knob, plugin manifest field, plugin SDK method, or channel API.

2. Route all major run entry points through the same repaired selection.
   - WebChat/TUI `chat.send`
   - Telegram/Discord/normal auto-reply
   - cron and isolated agent runs
   - queued/follow-up runs
   - live model switch retry paths
   - compaction paths that forward runtime/auth context

3. Preserve explicit user choices.
   - If `modelOverrideSource === "user"` or `authProfileOverrideSource === "user"`, keep the user-owned state unless it is invalid for the selected runtime.
   - Do not clear user auth while repairing auto model fallback state.

4. Treat auto fallback state as temporary.
   - If auto model fallback provenance exists, use the existing primary-probe path.
   - If an auto auth/profile/runtime field points to a provider different from the configured primary and lacks usable provenance, clear it or route it into the primary-probe path.
   - Do not validate an auto fallback profile only against the fallback provider when deciding whether the session has recovered.

5. Repair stale fields together.
   - When the primary is selected again, clear fallback-owned `providerOverride`, `modelOverride`, `modelOverrideSource`, fallback-origin fields, `authProfileOverride`, `authProfileOverrideSource`, `authProfileOverrideCompactionCount`, and stale runtime `modelProvider` / `model` fields as one persisted update.
   - When fallback remains active, persist enough fallback-origin metadata for future primary probes.

6. Keep `resolveSessionAuthProfileOverride` narrow.
   - It should answer: "which auth profile is valid for this provider/runtime?"
   - It should not prepend profiles from another provider to escape stale session state.

7. Keep the public behavior contract unchanged.
   - No new `openclaw.json` config field.
   - No migration for user config.
   - No plugin SDK type or method change.
   - No new plugin manifest field.
   - No change to provider plugin auth contracts.
   - Existing sessions may be repaired in place, but only by clearing or updating already-existing session fields.

## Likely Code Areas

- `src/auto-reply/reply/model-selection.ts`
- `src/agents/agent-command.ts`
- `src/auto-reply/reply/get-reply-run.ts`
- `src/cron/isolated-agent/run.ts`
- `src/gateway/server-methods/chat.ts`
- `src/gateway/session-utils.ts`
- `src/agents/auth-profiles/session-override.ts`

## Tests

Add focused regression coverage for:

1. WebChat/TUI fresh or reused session with:
   - agent primary `minimax/MiniMax-M2.7`
   - stored auto `authProfileOverride: "deepseek:default"`
   - stored runtime `modelProvider: "deepseek"`
   - expected recovery to MiniMax plus `minimax:global`, or clearing DeepSeek state before dispatch.

2. Normal auto fallback with provenance:
   - fallback remains active when primary probe fails.
   - fallback clears when primary probe succeeds.

3. Legacy auto-like state without fallback-origin metadata:
   - stale auto provider/model/auth fields do not remain self-confirming forever.

4. User overrides:
   - user-selected model stays selected.
   - user-selected auth profile is preserved when valid for the selected runtime.

5. Provider boundary:
   - no test may pass by pairing a MiniMax auth profile with an active DeepSeek run.

6. Entry-point parity:
   - WebChat/TUI and normal auto-reply resolve the same stale auto fallback session shape the same way.
   - Cron/isolated runs either use the same helper or have a test proving equivalent behavior.
   - Queued/follow-up paths do not reintroduce stale fallback auth after the primary has recovered.

7. Public surface guard:
   - no config schema snapshot, plugin SDK export, plugin manifest schema, or provider contract changes are needed for the fix.

## Proof Required

- `node scripts/run-vitest.mjs src/agents/auth-profiles/session-override.test.ts`
- `node scripts/run-vitest.mjs src/auto-reply/reply/model-selection.test.ts`
- `node scripts/run-vitest.mjs src/agents/agent-scope.test.ts`
- Focused WebChat/TUI or gateway session test proving the reported session shape.
- `node scripts/run-vitest.mjs src/auto-reply/reply/agent-runner-execution.test.ts -t "auto fallback"`
- Focused cron/isolated or queued/follow-up proof if the shared helper is not mechanically used by those paths.
- Diff review confirming no config schema, plugin SDK, plugin manifest, or provider contract surface changed.
- Changed check or Testbox proof before PR handoff.

Live MiniMax/DeepSeek proof is useful but not the first gate. A high-fidelity synthetic gateway/WebChat test is enough to prove the invariant without real credentials or forced provider failure.

## PR Guidance

Do not land PR #85311 as-is. It changes auth ordering without changing provider/model selection and can create cross-provider auth mismatches.

Preferred PR shape:

1. Add failing regression for the stale auto DeepSeek session shape.
2. Implement shared internal selection repair.
3. Route major run entry points through the repaired selection or prove equivalent behavior.
4. Keep auth resolution provider-scoped.
5. Add source/provenance tests for auto vs user state.
6. Confirm no new config value and no plugin SDK/interface change.
7. Include a real behavior proof section with exact commands and observed before/after session state.
