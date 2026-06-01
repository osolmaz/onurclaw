# OpenClaw Dense Stream Production Fix Plan

## Goal

Fix dense local-provider stream processing so the gateway remains responsive while large streamed answers are processed.

## Scope

- Keep the live gateway dense-stream repro in the PR.
- Retain the narrow Ollama cooperative-yield guard for dense NDJSON parsing.
- Add the broader production shape: stream consumers should process incremental deltas instead of repeatedly scanning or copying full growing assistant messages.
- Preserve compatibility where current consumers still require full snapshots.
- Keep tests focused and fast.

## Implementation Shape

- Add a shared assistant stream accumulator that can emit lightweight delta partials or full snapshot partials.
- Use lightweight delta partials for Ollama text and thinking deltas.
- Keep full content on boundary/final events.
- Migrate proxy reconstruction to the shared accumulator in snapshot mode.
- Update gateway subscribers and BTW streaming to consume deltas first and handle replacement deltas.
- Add focused unit tests plus an opt-in live gateway repro harness.

## Proof Required

- Focused Vitest coverage for the accumulator, Ollama stream path, proxy compatibility, subscriber delta path, BTW replacement handling, diagnostics accounting, and gateway coalescing.
- Lint/type/build checks for touched surfaces.
- Live local gateway repro with `--assert-responsive`.
- Codex review against `origin/main` until no P0/P1 findings remain.
- PR comments and CI checked before handoff.

## Known Proof Gaps

- Windows and WSL2 live repro.
- Real Ollama daemon naturally producing dense output.
- Cross-OS Crabbox/Testbox proof.
