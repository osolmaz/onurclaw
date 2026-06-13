# OpenClaw Onur Inventory Job

This repo carries the public, non-secret half of the periodic OpenClaw Onur
inventory automation. Deployment-specific paths, credentials, message
destinations, and host security details intentionally live outside this public
repo.

## Security Contract

Run the job as an isolated automation agent with a narrow execution surface:

- The working repo is mounted read/write as `/workspace`.
- Gitcrawl-derived data is mounted read-only as `/gitcrawl`.
- Job state is mounted read/write as `/state`.
- Network egress is disabled for the job sandbox.
- No host credential directories, shell history, SSH keys, GitHub tokens, or
  OpenClaw runtime secrets are mounted into the sandbox.
- The cron payload allows only sandbox `exec`/`process` tools.
- Broad command execution is allowed only inside the locked sandbox. The sandbox
  still has no network, host credentials, host secrets, or host workspace
  mounts.

The prompt is not a security boundary. Treat GitHub issue text, Discord text,
model output, inventory rows, and database contents as untrusted input. A prompt
injection can ask for more tools, more files, or network access, but the runtime
must not provide those capabilities.

## Data Inputs

The job expects these files to be provided by the private deployment:

- `/gitcrawl/gitcrawl.db`: read-only Gitcrawl archive data.
- `/gitcrawl/notifier.sqlite`: read-only notifier classification data.
- `/state/inventory-notifier-compare-state.json`: persistent compare state. The
  file is created on first run if missing.

The public script validates that the read-only data files exist before doing
anything useful. Data export, snapshot freshness, and GitHub publication are
private deployment responsibilities.

## Skill Copy

The job reads the checked-in local skill at
`/workspace/.agents/skills/openclaw-onur-inventory/SKILL.md`. It must be a real file,
not a symlink or remote link, because the sandbox has no network or host repo
access.

That file is synced from the tools repo source:
`agents/skills/openclaw-onur-inventory/sandbox/SKILL.md`.

When both repos are checked out locally, verify the copy with:

```bash
python3 scripts/check_synced_skill.py
```

Use `ONURCLAW_TOOLS_REPO=/path/to/tools` or `--tools-repo /path/to/tools` when
the tools checkout is not a sibling directory. In environments without the tools
repo, the check skips cleanly unless `--require-source` is passed.

## Job Flow

The cron message should make the curation step explicit:

```text
Read /workspace/.agents/skills/openclaw-onur-inventory/SKILL.md and follow it to
refresh /workspace/OPENCLAW_ONUR_INVENTORY.md from /gitcrawl/gitcrawl.db.
First run: git checkout main
Use scripts/list_inventory_review_candidates.py with --format jsonl --output
/state/inventory-candidates.jsonl, review candidates from that file in small
chunks without printing the whole file, update the inventory and watermark only
for ranges fully reviewed, then run exactly:
/workspace/scripts/finalize_inventory_job.sh
If the command output is exactly NO_CHANGES, reply exactly NO_REPLY.
Otherwise reply with the command output only.
```

The model does the curation before the finalizer. The helper
`scripts/list_inventory_review_candidates.py` builds a broad review pool from
the exported Gitcrawl database. It should write that pool to
`/state/inventory-candidates.jsonl` and print only the summary line. The model
must still decide each item against the skill criteria.

The sandbox does not provide Codex's `apply_patch` helper. Mechanical file
edits should use checked-in scripts or simple shell/Python commands that pass
the sandbox command preflight, followed by the sorter/finalizer.

`scripts/finalize_inventory_job.sh` then:

1. Verifies that it is running from the expected mounted repo.
2. Verifies the read-only Gitcrawl/notifier inputs and writable state directory.
3. Sorts `OPENCLAW_ONUR_INVENTORY.md` without live GitHub activity refresh,
   regenerating the newest-open view and collapsed full open table.
4. Exports and validates `OPENCLAW_ONUR_INVENTORY.json`, the machine-readable
   mirror used by automation.
5. Compares the JSON inventory against notifier state. The compare path must
   not parse Markdown tables.
6. Commits `OPENCLAW_ONUR_INVENTORY.md` and
   `OPENCLAW_ONUR_INVENTORY.json` if either file changed.
7. Prints either `NO_CHANGES` or the concise mismatch report. The cron prompt
   maps `NO_CHANGES` to the final `NO_REPLY` sentinel so delivery can stay
   quiet.

It deliberately does not push. Publication should be a deterministic host-side
step that only has access to the onurclaw repo, not to the sandbox prompt or
model context.

`scripts/run_inventory_job.sh` is kept as a compatibility alias for the
finalizer. The cron prompt should call `finalize_inventory_job.sh` only after
the curation work is done.

## Local Smoke Checks

From this repo:

```bash
bash -n scripts/run_inventory_job.sh scripts/finalize_inventory_job.sh
python3 scripts/check_synced_skill.py
python3 -m py_compile scripts/inventory_data.py scripts/export_inventory_json.py scripts/validate_inventory_json.py scripts/sort_openclaw_onur_inventory.py scripts/inventory_notifier_compare.py scripts/list_inventory_review_candidates.py scripts/check_synced_skill.py
OPENCLAW_ONUR_INVENTORY_SKIP_ACTIVITY=1 python3 scripts/sort_openclaw_onur_inventory.py --no-activity
python3 scripts/export_inventory_json.py
python3 scripts/validate_inventory_json.py
python3 scripts/inventory_notifier_compare.py --inventory-json OPENCLAW_ONUR_INVENTORY.json --notifier-db .inventory-job-state/gitcrawl/notifier.sqlite --no-state --limit 3
```
