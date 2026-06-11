# 2026-06-11 hclaw Consolidation Plan

## Goal

One place, one name, one command, one language. Everything a user needs to
create, update, and repair their personal OpenClaw agent on Hugging Face lives
in the template Space, in TypeScript, under the display name **Hugging Claw**
with the CLI command **`hclaw`**.

Existing deployments are first-class: a previous deployment can always be
updated to the current template and repaired from config drift, without losing
agent memory. The state-sync layer makes this safe by construction: Spaces are
disposable, the bucket holds the memory, so replacing a Space never loses data.

## Naming

- Display name: **Hugging Claw** (README title, Space card).
- CLI command/script: **`hclaw`**.

## Language Decision (revised 2026-06-11)

Everything is TypeScript: the state-syncer (already TS), the `hclaw` CLI, and
a new **TS bucket client** that both consume. The earlier bash/Python launcher
ideas are dropped.

The bucket client is implemented in this repo using the Python client
(`huggingface_hub`) as the protocol reference:

- Reference clones: `~/hf/huggingface_hub` (canonical bucket client,
  `_buckets.py`, `hf_api.py` bucket methods) and `~/hf/huggingface.js`
  (Xet upload machinery in `packages/hub/src/utils/`).
- Wire protocol (from `hf_api.py:_batch_bucket_files`):
  1. Fetch a Xet write token for `repo_type=bucket`.
  2. Upload bytes via the Xet protocol (chunking/dedup).
  3. `POST /api/buckets/{id}/batch` with NDJSON
     `addFile {path, xetHash, mtime}` / `deleteFile {path}` lines.
  4. List/metadata via `/api/buckets/{id}/tree` and `/paths-info`;
     downloads via resolve URLs (plain HTTP GET works for non-xet-aware
     reads).
- Xet upload in TS: `@huggingface/hub` contains the full implementation
  (`uploadShards.ts` 440 L, `createXorbs.ts` 779 L, `xetWriteToken.ts`,
  `shardParser.ts`, helpers) but does NOT export it. We vendor those files
  (MIT, with attribution header) into `src/vendor/hfjs-xet/` and depend on the
  published WASM packages (`@huggingface/xetchunk-wasm`,
  `@huggingface/splitmix64-wasm`, both on npm). The write-token fetch is
  adapted for `repo_type=bucket` per the Python reference.
- Follow-up (separate track, not blocking): upstream bucket support to
  `huggingface/huggingface.js` so the vendor dir can be deleted.

Consequence for the Docker image: the state-syncer switches from shelling out
to the `hf` CLI to the shared TS bucket client, and Python + the `hf` CLI are
REMOVED from the image. One canonical path; the CLI-shelling path is deleted
in the same change.

## Consolidation

```text
spaces/osolmaz/openclaw-huggingface   (the ONE repo)
  hclaw.sh            # thin shim: checks node >= 20, fetches dist/hclaw.mjs, runs it
  dist/hclaw.mjs      # committed bundled CLI (drift-guarded by a test)
  src/hclaw/          # CLI source: bootstrap | update | doctor
  src/hf-bucket-client/  # shared TS bucket client (REST + xet upload)
  src/vendor/hfjs-xet/   # vendored upload machinery from huggingface.js (MIT)
  src/hf-state-sync/  # state syncer (switches to hf-bucket-client)
  test/               # vitest suite
  Dockerfile, entrypoint.sh, openclaw.default.json, scripts/
  docs/               # design notes
  README.md           # Hugging Claw: goal, one-liner, how state survives, costs

osolmaz/openclaw-bootstrap
  Tombstone README pointing at the new one-liner. No script. Kept because its
  URL has been published.
```

One-liner stays bash-friendly via the shim:

```bash
bash <(curl -fsSL https://huggingface.co/spaces/osolmaz/openclaw-huggingface/resolve/main/hclaw.sh)
```

Local requirement: Node >= 20. The `hf` CLI is no longer needed locally; auth
comes from `HF_TOKEN` env or the standard token cache at
`~/.cache/huggingface/token`, the same locations the Python client reads.

`dist/hclaw.mjs` is a committed build artifact because Space repos have no CI;
a vitest guard rebuilds and compares so source and bundle cannot drift.

## Subcommand Contracts

### `hclaw bootstrap` (default when run with no args)

1. Resolve agent name from Telegram bot username (existing behavior).
2. Create private bucket + private Space from the template.
3. Set variables: `OPENCLAW_HF_STATE_BUCKET`, `OPENCLAW_HF_TEMPLATE_REV`
   (template HEAD sha at copy time), port/model/agent vars. No mount, no
   `/data` path variables.
4. Set secrets: gateway token, `HF_TOKEN`, optional Telegram.
5. Restart and print Space + bucket URLs.

### `hclaw update <owner/space>`

1. Confirm the target looks like a Hugging Claw deployment
   (`OPENCLAW_HF_TEMPLATE_REV` variable present, or `--force`).
2. Force-push current template files into the target Space repo. User Spaces
   are runtime copies; customizations do not belong there. Agent memory is in
   the bucket and is never touched.
3. Re-stamp `OPENCLAW_HF_TEMPLATE_REV`.
4. Run the doctor checks so an update always lands on a clean config.
5. Wait for rebuild; verify boot log shows `restored snapshot` or
   `fresh start` and the gateway becomes ready.

### `hclaw doctor <owner/space>`

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

Space management calls (variables, secrets, restart, logs, repo push) are
plain Hub REST; implement what `@huggingface/hub` lacks directly against the
endpoints, with the Python client as reference.

## Safety Rules

- `update`/`doctor` never write to the state bucket and never delete
  snapshots, manifests, or secret values.
- No secret values in output, ever; secret checks are name-only.
- Doctor `--fix` changes Space config only; destructive repo action is limited
  to the documented force-push in `update`.

## README Changes

- Title: Hugging Claw. Lead: one-command personal OpenClaw agent on Hugging
  Face that never loses its memory.
- One-liner uses `hclaw.sh`; document `update` and `doctor`.
- Honest costs section: paid Space hardware required for an always-on agent
  (free CPU Spaces sleep and may lack Telegram egress); inference uses HF
  Inference Providers credits ($0.10/month free accounts, $2.00 PRO, then
  pay-as-you-go at provider rates).
- Bootstrap tombstone README: one paragraph, new one-liner, nothing else.

## Verification

Local:

- vitest: bucket client round-trip against a fake transport; bundle drift
  guard; existing state-sync suite stays green on the new client seam.
- Live bucket client parity test against a real test bucket: upload bytes +
  file, list, metadata, download, delete; compare results with the `hf` CLI
  doing the same operations.

Live, in order:

1. Fresh `bootstrap` of a throwaway agent (new bucket + Space) via the new
   one-liner; confirm boot, snapshot in bucket (written by the TS client from
   inside the container), restart-restore.
2. `update osolmaz/onurclawtest`; confirm rebuild, restore from existing
   snapshots, Telegram still configured.
3. `doctor osolmaz/onurclawtest` -> clean report.
4. Induce drift (re-add a stale `/data` variable), `doctor` reports it,
   `doctor --fix` repairs it.
5. Remove throwaway resources created in step 1.

## Out of Scope

- npm/pip-distributed CLI (the shim + committed bundle is the distribution).
- Self-updating Spaces; updates stay user-initiated.
- Multi-agent / multi-Space management beyond one target per invocation.
- Upstreaming bucket support to huggingface.js (tracked as follow-up; deletes
  `src/vendor/hfjs-xet/` when it lands).
