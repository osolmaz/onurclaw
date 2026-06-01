# OpenClaw 80379 Implementation Plan

## Goal

Fix tool-result redaction so harmless shell env placeholders stay byte-stable in persisted session history, without allowing plaintext credentials to be saved or shown.

## Scope

- Keep persisted transcript/tool redaction enabled.
- Preserve same-key shell env references such as `DISCORD_BOT_TOKEN="${DISCORD_BOT_TOKEN:-}"`.
- Redact mismatched shell references, literal secret values, and literal fallback defaults.
- Cover raw text redaction, structured tool args, tool-result sanitization, and transcript persistence.
- Update the existing PR `#86928`.

## Validation

- Run focused Vitest files through `node scripts/run-vitest.mjs`.
- Run formatting and `git diff --check`.
- Push the current branch.
- Run `codex review --base main` until no P0/P1 findings remain.
- Check PR comments and inline review comments.
- Wait for CI and report any unrelated failures.
