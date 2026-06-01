## OpenClaw Visible Output Normalizer Plan

1. Reproduce the current failure with regression tests that cover repeated visible suffixes whose full repeated output is explicitly named in the model preamble.
2. Fix the shared visible-output normalizer so it preserves intentional repeated outputs while still collapsing leaked internal scaffolding and repeated visible suffix bugs.
3. Re-run targeted tests and a build.
4. Smoke test the branch on the watched local gateway with a live Discord probe.
5. Push the branch, run `codex review --base main`, address any P0/P1 issues, update the PR title/body if needed, and verify CI is green.
