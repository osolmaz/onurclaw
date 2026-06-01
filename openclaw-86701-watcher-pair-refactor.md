# OpenClaw PR 86701 Watcher Pair Refactor Plan

## Goal

Make the native memory watcher lifecycle easier to reason about by storing each
main recursive watcher and its optional parent watcher as one pair.

## Steps

1. Replace separate native watcher arrays with a pair structure.
2. Update error, replacement, fallback, and close paths to operate on pairs.
3. Keep behavior unchanged: macOS/Windows native recursive watch, Linux chokidar,
   chokidar fallback on native failure, parent watcher replacement detection.
4. Run focused tests and formatting/lint checks.
5. Commit and push to PR 86701.
6. Run `codex review --base main` and address P0/P1 findings.
7. Check PR comments and CI, then report.
