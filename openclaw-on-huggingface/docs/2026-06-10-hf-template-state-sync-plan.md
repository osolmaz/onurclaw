# 2026-06-10 HF Template State Sync Plan

## Goal

The product goal: anyone can create their own persistent OpenClaw agent on
Hugging Face with one command. The Space runs the agent and is disposable;
the user's private bucket is the agent's durable memory.

This plan secures the one missing property: state must move between Space and
bucket without loss or corruption. Running live SQLite directly on the bucket
mount corrupts the database (see `tracking/`), so the runtime keeps live state
on local disk and the bucket stores verified snapshots. Every section below
serves that property; anything that does not is cuttable.

## Decision

The long-term Hugging Face deployment should use:

```text
local live state + bucket snapshots
```

not:

```text
live SQLite directly on the HF bucket mount
```

The bucket remains the durable source of truth. The Space container restores a
verified state snapshot from the bucket on boot, runs OpenClaw against local
disk, and writes verified snapshots back to the bucket.

## Repository Ownership

This tracking repo is not the final runtime source of truth.

Target ownership (everything hosted on Hugging Face):

```text
huggingface.co/spaces/osolmaz/openclaw-huggingface
  Source of truth AND deployable Space template:
  - TypeScript state sync implementation
  - tests
  - Dockerfile
  - entrypoint
  - template config

huggingface.co/osolmaz/openclaw-bootstrap
  Minimal bootstrap launcher.
  It creates the user's private bucket and private Space, copies the template,
  and sets secrets/env vars. It should not contain runtime state logic.

user private bucket
  Durable state snapshots and recovery manifests, written via the Hub API.

user private Space
  Runtime copy of the template.
```

## Why This Is The Right Split

- Everything stays under Hugging Face; no external hosting dependency.
- The Space repo is a normal git repo: source, tests, and the deployable are
  one artifact, like the hermes-agent template.
- The bootstrap repo stays small and security-sensitive: no users paste HF
  credentials into another Space.
- Users do not need Python locally.
- The Space runtime uses Node, which OpenClaw already requires.
- HF-specific storage behavior stays outside OpenClaw core until the pattern is
  proven.

## Runtime Layout

The bucket is NOT mounted into the Space. All bucket reads and writes go
through the Hub HTTP API; the unreliable mount that corrupted live SQLite is
out of the trust path entirely.

Bucket repo contents:

```text
manifest.json
snapshots/
  state-2026-06-10T12-00-00Z.tar.zst
  state-2026-06-10T12-05-00Z.tar.zst
```

Inside the Space container:

```text
/tmp/openclaw-live/
  .openclaw/
    openclaw.json
    state/openclaw.sqlite
    agents/
    credentials/   # materialized from Space secrets at boot, never snapshotted
    ...
```

OpenClaw should run with:

```text
OPENCLAW_STATE_DIR=/tmp/openclaw-live/.openclaw
OPENCLAW_CONFIG_PATH=/tmp/openclaw-live/.openclaw/openclaw.json
OPENCLAW_WORKSPACE_DIR=/tmp/openclaw-live/workspace
```

The bucket stores snapshots and manifests only, never the active SQLite
database or its WAL/SHM sidecars.

## TypeScript Components

In the Space repo (`huggingface.co/spaces/osolmaz/openclaw-huggingface`):

```text
src/hf-state-sync/
  cli.ts
  restore.ts
  snapshot.ts
  manifest.ts
  hub.ts        # bucket API upload/download (tarball upload + manifest overwrite)
  sqlite.ts
  paths.ts
  archive.ts
  retention.ts

test/
  hf-state-sync.restore.test.ts
  hf-state-sync.snapshot.test.ts
  hf-state-sync.manifest.test.ts
  hf-state-sync.sqlite.test.ts

Dockerfile
entrypoint.sh
openclaw.default.json
scripts/
  configure-telegram.mjs
```

There is no `lock.ts`: with atomic manifest overwrite there is nothing for a
lock to protect, and a lock protocol over an eventually-consistent remote is
more dangerous than the race it prevents. Spike before implementing: confirm
the bucket batch API (`batch_bucket_files`/`sync_bucket` in Python
`huggingface_hub`) is reachable from Node via `@huggingface/hub`; if not, shell
out to the `hf buckets` CLI inside the image for the same operations.

Built artifact inside the image:

```text
/app/hf-state-sync.js
```

Entrypoint shape:

```bash
node /app/hf-state-sync.js restore
node /app/hf-state-sync.js supervise -- openclaw gateway
```

`supervise` starts OpenClaw, runs the snapshot loop, forwards signals, and takes
a best-effort final snapshot on shutdown.

## Snapshot Contract

Manifest:

```json
{
  "version": 1,
  "current": {
    "id": "2026-06-10T12-00-00Z",
    "path": "snapshots/state-2026-06-10T12-00-00Z.tar.zst",
    "createdAt": "2026-06-10T12:00:00.000Z",
    "sha256": "...",
    "sizeBytes": 123456,
    "openclawVersion": "...",
    "verified": true
  },
  "previous": []
}
```

Rules:

- Never overwrite the only known-good snapshot.
- Stage and verify locally first: build the archive in a local temp dir, verify
  its checksum, and run `PRAGMA integrity_check` on every staged SQLite DB.
- Promote in two steps over the bucket API: (1) upload the snapshot tarball to
  its final `snapshots/` path, (2) only after upload succeeds, overwrite
  `manifest.json` in a single object write. Object writes are atomic at the
  object level, so readers see the old or the new manifest, never a partial
  one, and the manifest never points at an archive that is not fully uploaded.
- Buckets are non-versioned (no commits, no history), so the manifest's
  `previous` list plus retained snapshot files are the ONLY rollback path.
  Never delete a snapshot that the manifest still references.
- Record the container run id and boot time in the manifest for observability.
- No locking. Overlapping containers (e.g. during a rebuild) produce serialized
  object writes; the last verified writer wins.
- Keep the last N verified snapshots.
- On boot, if the latest snapshot fails verification, walk back through
  `previous` entries until one passes.

## SQLite Handling

Snapshotting must not copy live SQLite files directly.

For each live SQLite DB:

```text
*.sqlite
*.sqlite-wal
*.sqlite-shm
```

Use SQLite backup semantics:

1. Open the live DB read-only or read-write as required by the backup method.
2. Produce a consistent standalone DB file in a staging directory.
3. Run `PRAGMA integrity_check` on the staged DB.
4. Put the staged DB into the archive.

Acceptable implementation options:

- Prefer SQLite backup API if available cleanly from Node.
- Otherwise use `VACUUM INTO` against the live DB into staging.
- Avoid raw copying of `sqlite`, `sqlite-wal`, and `sqlite-shm` as the durable
  snapshot format.

## Files To Include

Snapshot the whole OpenClaw state directory, not only `state/openclaw.sqlite`.

Include:

```text
openclaw.json
agent-name.txt
agents/
state/*.sqlite as consistent standalone DB copies
workspace metadata if stored under state
```

Exclude:

```text
credentials/          # secrets live in HF Space Secrets, never in snapshots
.env                  # same
state/*.sqlite-wal
state/*.sqlite-shm
logs that do not need durability
tmp/
cache/
large transient downloads
```

Secrets rule: provider/bot tokens live in HF Space Secrets only; the entrypoint
materializes them into the live state dir at boot. Anything that must survive a
rebuild must live in state, not in `credentials/`.

The exclude list should be explicit and tested.

## Bootstrap Behavior

`osolmaz/openclaw-bootstrap` should:

1. Resolve the bot name and target resource names.
2. Create a private bucket.
3. Create/copy a private Space from `osolmaz/openclaw-huggingface`.
4. Set Space secrets and variables.
5. Start/restart the Space.
6. Print the Space URL and bucket URL.

It should not implement snapshot/restore logic.

## Verification

Required tests in the GitHub source repo:

- fresh boot with empty bucket creates initial local state
- snapshot writes manifest only after verification
- restore chooses latest verified snapshot
- restore falls back when latest snapshot fails integrity
- SQLite snapshot does not include WAL/SHM sidecars
- corrupted SQLite archive is rejected
- retention keeps last N snapshots
- signal handling runs best-effort final snapshot
- bootstrap-created Space uses `/tmp/openclaw-live`, not `/data/.openclaw`, as
  `OPENCLAW_STATE_DIR`

Required live HF verification:

1. Deploy template to a private test Space.
2. Confirm OpenClaw state DB lives under `/tmp/openclaw-live`.
3. Confirm bucket contains snapshots and manifest, not active WAL sidecars.
4. Send Telegram messages and verify replies.
5. Restart/rebuild the Space.
6. Confirm state restores from bucket snapshot.
7. Run read-only integrity checks against restored local DB and latest bucket
   snapshot.

## Migration From Current Test Space

The current test bucket contains a corrupted live DB. Do not use it as a trusted
snapshot.

For migration testing:

1. Start with a fresh bucket, or
2. recover non-SQLite state from the old bucket manually, and
3. create a fresh SQLite state DB locally.

The new template should refuse to promote a snapshot if SQLite integrity fails.

## Resolved Decisions (2026-06-11)

- Bucket I/O goes through the bucket HTTP API; the bucket is never mounted.
  This matches the documented bucket access guidance: mounts are "not for"
  multi-writer or lock-dependent workloads (hf-mount README), while CLI/API
  sync is the documented path for backups (hub docs, "Rolling backups").
- Promotion: upload tarball, then atomically overwrite `manifest.json`; no
  lock protocol. Buckets are non-versioned, so manifest history + retained
  snapshots are the only rollback.
- Secrets are excluded from snapshots; HF Space Secrets are the only secret
  store, materialized at boot.
- Snapshot interval default: 60 seconds. Worst case, one interval of state is
  lost on an unclean kill; SIGTERM takes a best-effort final snapshot.
- Archive format: `tar.zst` (we control the Dockerfile; install `zstd`).
- Snapshot-after-important-writes remains an OpenClaw-core concern; not
  required for the first version.

## First Implementation Target

Implement directly in the Space repo:

```text
huggingface.co/spaces/osolmaz/openclaw-huggingface
```

Order:

1. Spike: upload/download to a Storage Bucket from Node via `@huggingface/hub`
   (fallback: `hf` CLI in the image). This decides `hub.ts`.
2. `hf-state-sync` module + tests.
3. Dockerfile/entrypoint: live state under `/tmp/openclaw-live`, no bucket
   mount.
4. Live verification per the checklist above.
5. Only after live verification: update `osolmaz/openclaw-bootstrap` to stop
   creating the bucket mount, and fix its README persistence wording.
