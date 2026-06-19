# onurclaw

Public OpenClaw maintainer workbench for Onur.

This repo contains curated maintainer artifacts that are useful to share openly:

- `OPENCLAW_ONUR_INVENTORY.md`: curated local-model and open-weight OpenClaw issue/PR inventory.
- `OPENCLAW_ONUR_INVENTORY.json`: machine-readable mirror used by automation.
- `schemas/openclaw-onur-inventory.schema.json`: JSON schema for the machine-readable mirror.
- `scripts/sort_openclaw_onur_inventory.py`: sorter/activity refresher for the inventory.
- `scripts/export_inventory_json.py`: exports the Markdown inventory to JSON.
- `scripts/check_synced_skill.py`: verifies that the sandbox inventory skill copy matches the tools source when that checkout is available.
- `scripts/run_inventory_job.sh`: constrained cron entrypoint for the inventory automation.
- `docs/inventory-job.md`: public security contract for the sandboxed inventory job.
- `docs/2026-06-11-gemma-12b-quant-localpager-plan.md`: plan for rerunning the Gemma 4 12B quantization smoke through Localpager Agent.
- `open-model-benchmarking/`: research packet for open models to benchmark with ShellBench and optimize with GEPA-style profile/prompt search.
- `.agents/skills/openclaw-onur-inventory/SKILL.md`: local sandbox skill copy read by the no-network inventory job.
- `openclaw-model-configuration-registry-proposal.md`: proposal for moving beyond `localModelLean` toward benchmark-informed model configuration management.
- `openclaw-*.md` and `active-memory-issue.md`: public OpenClaw implementation plans, repro notes, and findings.
- `notes/openclaw/`: older public OpenClaw root-cause notes and PR writeups.

Private scratch notes, raw prompt captures, personal workspace state, and unrelated project artifacts should stay out of this repo.
