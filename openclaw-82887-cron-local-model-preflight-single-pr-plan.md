# OpenClaw #82887 Cron Local-Model Preflight Single-PR Plan

Status: implemented in PR #82887.

Goal: fix scheduled isolated cron runs that skip before a real model turn when a local primary provider is unavailable even though configured fallback models exist.

Plan:

1. Reuse the shared model fallback candidate builder for cron preflight.
2. Preflight candidates in runtime fallback order: primary first, then configured fallbacks.
3. Preserve strict behavior for `fallbacks: []`.
4. If preflight selects a fallback, pass only remaining candidates into execution so the dead primary is not retried in the same run.
5. Add focused tests for fallback handoff, strict empty fallbacks, and post-preflight fallback narrowing.
6. Update cron docs to describe local-provider preflight fallback behavior.
7. Prove with focused unit tests, build/type/lint checks, codex review, CI, and a scheduled cron run using a dead local primary plus synthetic OpenAI-compatible fallback.

Implemented PR:

https://github.com/openclaw/openclaw/pull/82887

