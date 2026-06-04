# onurclaw

Public OpenClaw maintainer workbench for Onur.

This repo contains curated maintainer artifacts that are useful to share openly:

- `OPENCLAW_ONUR_INVENTORY.md`: curated local-model and open-weight OpenClaw issue/PR inventory.
- `OPENCLAW_ONUR_INVENTORY.json`: machine-readable mirror used by automation.
- `schemas/openclaw-onur-inventory.schema.json`: JSON schema for the machine-readable mirror.
- `scripts/sort_openclaw_onur_inventory.py`: sorter/activity refresher for the inventory.
- `scripts/export_inventory_json.py`: exports the Markdown inventory to JSON.
- `scripts/run_inventory_job.sh`: constrained cron entrypoint for the inventory automation.
- `docs/inventory-job.md`: public security contract for the sandboxed inventory job.
- `openclaw-*.md` and `active-memory-issue.md`: public OpenClaw implementation plans, repro notes, and findings.
- `notes/openclaw/`: older public OpenClaw root-cause notes and PR writeups.

Private scratch notes, raw prompt captures, personal workspace state, and unrelated project artifacts should stay out of this repo.
