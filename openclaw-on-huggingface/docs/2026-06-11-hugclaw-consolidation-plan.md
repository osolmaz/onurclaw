# 2026-06-11 Hugging Claw Consolidation Plan

## Goal

One place, one name, one command. Everything a user needs to create, update,
and repair their personal OpenClaw agent on Hugging Face lives in the template
Space, under the name **Hugging Claw**:

```bash
bash <(curl -fsSL https://huggingface.co/spaces/osolmaz/openclaw-huggingface/resolve/main/hugclaw.sh)
```

Existing deployments must be first-class: a previous deployment can always be
updated to the current template and repaired from config drift, without losing
agent memory. The state-sync layer makes this safe by construction: Spaces are
disposable, the bucket holds the memory, so replacing a Space never loses data.

## Naming

- Display name: **Hugging Claw** (README title, Space card).
- Command/script: `hugclaw.sh` (one short lowercase word, like `hf`).

## Consolidation

```text
spaces/osolmaz/openclaw-huggingface   (the ONE repo)
  hugclaw.sh          # launcher: bootstrap | update | doctor (was bootstrap.sh)
  Dockerfile, entrypoint.sh, openclaw.default.json, scripts/
  src/hf-state-sync/  # state sync source
  test/               # vitest suite
  docs/               # design notes (optional copies of key plans)
  README.md           # Hugging Claw: goal, one-liner, how state survives, costs

osolmaz/openclaw-bootstrap
  Tombstone README pointing at the new one-liner. No script. Never deleted
  outright: its URL has been published.
```

`hugclaw.sh` references the Space repo it is served from as the template
(self-replicating template). Duplicated user Spaces carry the script too;
that is harmless and means every copy can bootstrap further copies.

## Subcommand Contracts

Local requirements stay exactly: `hf` CLI + `hf auth login`. No Node, no
Python, no npm package. Bash remains the right tool while the work is ~15 `hf`
invocations; a TS CLI in the same repo is the graduation path, not the start.

### `hugclaw.sh bootstrap` (default when run with no args)

Today's flow, plus a version stamp:

1. Resolve agent name from Telegram bot username (existing behavior).
2. Create private bucket + private Space from the template.
3. Set variables: `OPENCLAW_HF_STATE_BUCKET`, `OPENCLAW_HF_TEMPLATE_REV`
   (template HEAD sha at copy time), port/model/agent vars. No mount, no
   `/data` path variables.
4. Set secrets: gateway token, `HF_TOKEN`, optional Telegram.
5. Restart and print Space + bucket URLs.

### `hugclaw.sh update <owner/space>`

1. Confirm the target looks like a Hugging Claw deployment
   (`OPENCLAW_HF_TEMPLATE_REV` variable present, or `--force`).
2. Force-push current template files into the target Space repo. User Spaces
   are runtime copies; customizations do not belong there. Agent memory is in
   the bucket and is never touched.
3. Re-stamp `OPENCLAW_HF_TEMPLATE_REV` to the new template sha.
4. Run the doctor checks (below) so an update always lands on a clean config.
5. Wait for rebuild; verify boot log shows `restored snapshot` or
   `fresh start` and the gateway becomes ready.

### `hugclaw.sh doctor <owner/space>`

Report-only by default; `--fix` applies repairs (mirrors `openclaw doctor`).

Checks:

- Legacy bucket volume mount present -> remove (fix).
- Stale `/data` path variables (`OPENCLAW_STATE_DIR`, `OPENCLAW_WORKSPACE_DIR`,
  `OPENCLAW_CONFIG_PATH`) -> delete (fix).
- `OPENCLAW_HF_STATE_BUCKET` missing -> set after prompting for bucket (fix).
- Required secret NAMES present (`OPENCLAW_GATEWAY_TOKEN`, `HF_TOKEN`);
  values are never read or printed.
- State bucket listable with the local token.
- `OPENCLAW_HF_TEMPLATE_REV` behind template HEAD -> report "update available".
- Runtime logs contain a state-sync outcome (`restored snapshot`/`fresh start`)
  and a recent `snapshot ... uploaded` line -> report sync health.

## Safety Rules

- `update`/`doctor` never write to the state bucket and never delete
  snapshots, manifests, or secret values.
- No secret values in output, ever; secret checks are name-only.
- Doctor `--fix` changes Space config only; destructive repo action is limited
  to the documented force-push in `update`.

## README Changes

- Title: Hugging Claw. Lead: one-command personal OpenClaw agent on Hugging
  Face that never loses its memory.
- One-liner uses the new `hugclaw.sh` URL; document `update` and `doctor`.
- Honest costs section: paid Space hardware required for an always-on agent
  (free CPU Spaces sleep and may lack Telegram egress); inference uses HF
  Inference Providers credits ($0.10/month free accounts, $2.00 PRO, then
  pay-as-you-go at provider rates).
- Bootstrap tombstone README: one paragraph, new one-liner, nothing else.

## Verification

Local: `bash -n`, shellcheck if available, vitest suite still green (sync
source unchanged but repo moves around it).

Live, in order:

1. Fresh `bootstrap` of a throwaway agent (new bucket + Space) via the new
   one-liner; confirm boot, snapshot in bucket, restart-restore.
2. `update osolmaz/onurclawtest` (a genuine previous deployment); confirm
   rebuild, restore from existing snapshots, Telegram still configured.
3. `doctor osolmaz/onurclawtest` -> clean report.
4. Induce drift (re-add a stale `/data` variable), `doctor` reports it,
   `doctor --fix` repairs it.
5. Remove throwaway resources created in step 1.

## Out of Scope

- npm/pip-distributed CLI.
- Self-updating Spaces (a Space rewriting its own repo via HF_TOKEN): updates
  stay user-initiated.
- Multi-agent / multi-Space management beyond one target per invocation.
