# Silent-transport fallback patches (PR #116551)

These two patches preserve the full silent-transport fallback that abarsegov trimmed from PR #116551 in commit `3470f323523` ("fix-agents-require-payload-dispatch"). The branch history still contains the original commits; these patches exist so the work is restorable without digging through the PR.

## What is here

- `af3506f2ae0-dispatch-commit.patch` — "fix(agents): commit admitted prompt state at provider dispatch". Moves projection state, the provider call counter, and the user-turn-sent record from the admission callback to a dispatch hook that fires when the payload chain completes. Includes the first fallback layer: a transport that never fires `onPayload` has its pending commit adopted when the next provider call begins.
- `8b2d2429547-silent-settle.patch` — "fix(agents): settle silent transport prompt state at submission end". The second fallback layer: a still-unobserved pending commit settles when the submission completes, so the final provider call of a silent transport is not dropped. Includes its regression test.

## When to revive

Revive if a real third-party transport that never calls `onPayload` appears and loses sent-marking or mid-turn precheck gating. Apply in order with `git am` on top of a branch that already has the dispatch-commit mechanism, then reconcile with `3470f323523`'s removal of the same code.

## Status

Accepted tradeoff, not an oversight: as of `3470f323523` the strict rule is "nothing observed, nothing committed", and silent transports lose the feature deliberately. Documented on the PR.
