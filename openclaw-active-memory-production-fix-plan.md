# OpenClaw Active Memory Production Fix Plan

## Goal

Make Active Memory useful without letting it block normal replies.

Today, a reply can hold the `main` lane while waiting for Active Memory recall. The recall run can also default to `main`, so it waits behind the reply that is waiting for it. Crabbox reproduced this with the real OpenClaw queue code:

- AWS Crabbox lease: `cbx_9a2c0c874ecf`
- Run: `run_f2e6ba5d2b84`
- Result: omitted recall lane resolved to `main`, timed out while the reply held `main`; dedicated `active-memory` lane finished before timeout.

## Target Behavior

1. A user reply never waits behind Active Memory work on the same lane.
2. Active Memory recall has a small reply-time budget.
3. If recall finishes fast, inject the memory.
4. If recall is slow, skip memory and let the reply continue.
5. Slow recall cannot flood the gateway or block unrelated sessions.

## Implementation Steps

1. Add an Active Memory recall lane constant in `extensions/active-memory/index.ts`.
2. Pass that lane to the embedded recall run.
3. Add a focused regression test proving recall uses the dedicated lane.
4. Add a second behavior test that simulates a parent reply holding `main` and proves recall on the dedicated lane can still run.
5. Keep the hook timeout based on resolved config, not a fixed default, so custom budgets still work.
6. Add a short reply-time deadline mode for Active Memory:
   - recall ready before deadline: inject memory
   - recall misses deadline: return no memory and continue the reply
7. Decide whether missed recall should be cancelled or allowed to finish and populate cache for the next turn.
8. Add bounded concurrency:
   - at least one cap per agent
   - preferably one cap per session or per agent/session key
   - avoid one global recall lane becoming a new bottleneck
9. Make risky defaults visible:
   - warn when Active Memory inherits a slow main model
   - warn when timeout is high
   - warn when recall mostly returns timeout or empty results

## Production Shape

The clean long-term flow should be:

```text
reply starts on main
recall starts on active-memory:<agent-or-session>
reply waits briefly
memory ready -> inject it
memory slow -> skip it and reply anyway
```

## Validation

1. Focused unit tests for lane selection and hook deadline behavior.
2. A synthetic queue repro like the Crabbox proof, checked into tests if it fits cleanly.
3. One real gateway proof with Active Memory enabled:
   - direct session
   - recall logs show the dedicated lane
   - no `before_prompt_build` timeout
   - reply completes
   - gateway queue/liveness stays healthy
4. A concurrency proof with two sessions, to ensure one slow recall does not block another reply.
5. Relevant `check:changed` or Testbox proof before merge.

## PR Strategy

Ship this in two PRs if needed:

1. Narrow safety PR:
   - dedicated recall lane
   - regression tests
   - live/synthetic proof

2. Production hardening PR:
   - short deadline mode
   - bounded concurrency
   - cache/cancel policy
   - status or doctor warnings

Do not revive PR #73667 as-is. It is stale and changes QMD startup/default timeout behavior without fixing the lane bug.
