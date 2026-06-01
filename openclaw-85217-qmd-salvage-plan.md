# OpenClaw 85217 QMD Search Salvage Plan

## Goal

Fix OpenClaw issue #85217 by preserving valid QMD search JSON when the QMD subprocess exits non-zero after a macOS Metal cleanup crash.

## Scope

- Keep the generic process runner generic.
- Preserve captured stdout/stderr on non-zero subprocess exits with a typed error.
- Salvage only direct QMD search commands (`query`, `search`, `vsearch`) when stdout parses as valid QMD search JSON.
- Keep update/embed/status/maintenance failures fail-closed.
- Keep truncated output, invalid JSON, timeouts, spawn errors, and missing collection repair behavior safe.

## Implementation Steps

1. Add a typed CLI command error in `packages/memory-host-sdk/src/host/qmd-process.ts` that exposes stdout, stderr, exit code, and signal.
2. Update `runCliCommand` to reject with that typed error for non-zero exits.
3. Add focused tests for valid stdout plus non-zero exit, signal-only exit, and unchanged output limit behavior.
4. Update `extensions/memory-core/src/memory/qmd-manager.ts` to parse stdout from typed QMD search failures only in the direct search path and fallback search retry path.
5. Add regression coverage proving valid QMD search JSON is accepted after a non-zero exit and invalid stdout still fails.
6. Run focused tests and the live isolated QMD repro command if practical.
7. Commit, push, open a PR linked to issue #85217, run `codex review --base main`, address P0/P1 findings, check PR comments and CI, then post a final PR report.

## Validation Targets

- `node scripts/run-vitest.mjs packages/memory-host-sdk/src/host/qmd-process.test.ts packages/memory-host-sdk/src/host/qmd-query-parser.test.ts extensions/memory-core/src/memory/qmd-manager.test.ts extensions/memory-core/src/memory/search-manager.test.ts`
- Live QMD reproduction command on this Apple Silicon machine, if the isolated QMD cache remains usable.
- `codex review --base main`
- PR CI checks relevant to the branch.
