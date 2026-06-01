## Summary
- harden bound ACP reset and recovery flows so Discord ACP bindings can recreate cleanly after partial resets or stale runtime state
- make Discord ACP reply lifecycle startup non-blocking so delivery can continue even when lifecycle startup or typing setup misbehaves
- add focused regressions around ACP session recovery, stateful target lifecycle, Discord typing, and ACP delivery visibility

## Root cause
Bound ACP sessions could retain half-cleared local or runtime state across reset and recovery paths, which left some Discord-bound ACP channels stuck instead of lazily recreating a healthy session. Separately, the Discord reply lifecycle could block delivery when startup or typing setup hung, so even healthy ACP replies could appear wedged.

## Validation
- `pnpm test src/acp/control-plane/manager.test.ts src/acp/persistent-bindings.lifecycle.test.ts src/acp/persistent-bindings.test.ts src/channels/plugins/acp-stateful-target-driver.test.ts`
- `node scripts/run-vitest.mjs run --config vitest.auto-reply.config.ts src/auto-reply/reply/dispatch-acp-delivery.test.ts`
- `pnpm test src/auto-reply/reply/dispatch-acp-delivery.test.ts -t "does not block delivery when reply lifecycle startup hangs"`
- `pnpm test extensions/discord/src/monitor/message-handler.process.test.ts extensions/discord/src/monitor/typing.test.ts`
- `pnpm build`

## Notes
- The repo-wide pre-commit `pnpm check` path is currently blocked by unrelated existing `extensions/xai/*` lint errors on this base; this PR was validated with the focused commands above plus a full build.
