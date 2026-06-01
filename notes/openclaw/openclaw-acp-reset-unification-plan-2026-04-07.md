# OpenClaw ACP Reset Unification Plan

Date: 2026-04-07

## Problem

OpenClaw currently has two different reset implementations for ACP-bound sessions:

1. The gateway/session reset path in `src/gateway/session-reset-service.ts`
2. The ACP-specific bound reset path behind:
   - `src/channels/plugins/stateful-target-drivers.ts`
   - `src/channels/plugins/binding-targets.ts`
   - `src/channels/plugins/acp-stateful-target-driver.ts`
   - `src/acp/persistent-bindings.lifecycle.ts`

That split caused real behavior drift:

- gateway reset became the stronger, correct path
- Discord `/new` and `/reset` were still hitting the weaker ACP-only path
- bugs got fixed in one path but not the other

## Current conclusion

The public SDK contract should stay intact.

Specifically, we should keep:

- `StatefulBindingTargetDriver`
- `resetInPlace`
- `resetConfiguredBindingTargetInPlace`

Those are part of the Plugin SDK surface, so deleting or casually changing them would be the wrong move.

## Desired end state

There should be one real reset authority for OpenClaw sessions.

That authority should own the full reset lifecycle:

- runtime cleanup
- ACP close with persistent-state discard
- stale identity rewrite to fresh/pending state when needed
- local session rotation and related reset bookkeeping

The natural place for that authority is the existing gateway reset implementation:

- `src/gateway/session-reset-service.ts`

## Compatibility-preserving design

Do not remove the public stateful-target reset contract.

Instead:

1. Keep the SDK surface unchanged.
2. Make ACP's `resetInPlace` implementation delegate to the single real reset authority.
3. Remove duplicated ACP-only reset logic underneath that adapter once the delegation is in place.

In plain language:

- callers can still use the same reset abstraction
- ACP no longer owns separate reset semantics
- gateway reset and command/slash reset all converge on the same real implementation

## What “elegant” means here

The clean solution is not “delete abstractions.”

The clean solution is:

- one reset implementation
- multiple entrypoints
- one public contract
- thin adapters at the boundaries

That avoids:

- SDK breakage
- behavior drift
- duplicate fixes
- ACP-specific reset behavior for what is really a generic OpenClaw session reset

## Optional refinement

If needed, extract a smaller internal reset primitive under `src/gateway/session-reset-service.ts` and let both:

- gateway session reset
- ACP `resetInPlace`

call that same primitive.

That would be a structural cleanup only. It does not change the core design decision.

## Recommendation

Treat this as a compatibility-preserving unification:

- public Plugin SDK contract stays
- ACP reset implementation becomes a thin adapter
- the gateway/session reset path becomes the single source of truth

## Pinned decisions

These points are now considered the intended design:

1. `src/gateway/session-reset-service.ts` is the single reset authority for OpenClaw sessions.
2. ACP-bound `/new` and `/reset` must have the same reset semantics as gateway session reset.
3. The public SDK surface stays intact:
   - `StatefulBindingTargetDriver`
   - `resetInPlace`
   - `resetConfiguredBindingTargetInPlace`
4. ACP's `resetInPlace` implementation should be a thin adapter over the single reset authority, not a separate reset implementation.
5. Any remaining ACP-specific reset logic below that adapter is technical debt and should be removed only after delegation is complete.

## Non-goals

These are explicitly not part of the cleanup:

- removing the public Plugin SDK reset contract
- changing third-party plugin-facing reset APIs as part of this unification
- keeping two different reset semantics for "reset the same conversation"
