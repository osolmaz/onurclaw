# Open Model Benchmarking

Research folder for open-weight and open-model candidates that should be benchmarked with ShellBench and later optimized with GEPA-style profile or prompt search.

The goal is to move from "models that happen to be available" to a ranked set of model families and artifacts that are worth evaluating for OpenClaw model profiles.

## Current Inputs

The first hydrated data source is the live Hugging Face Inference Providers router snapshot captured on 2026-06-19.

- Public model browser: https://huggingface.co/inference/models
- Raw router endpoint: https://router.huggingface.co/v1/models
- API docs: https://huggingface.co/docs/inference-providers/hub-api

Snapshot files:

- `data/hf-router-models-20260619T112339Z.json`: raw router response.
- `data/hf-router-models-20260619T112339Z.tsv`: compact table with model id, creator, modalities, provider list, tool support, structured-output support, and max context.
- `data/hf-router-models-20260619T112339Z.ids.txt`: plain model ids.

## Programmatic Metadata Snapshots

`scripts/snapshot_hf_models.py` takes Hugging Face creator slugs and writes a timestamped metadata snapshot under `snapshots/`.

Default input:

- `creators.txt`: creator / owner slugs from the current HF router snapshot.

Default command:

```bash
python3 open-model-benchmarking/scripts/snapshot_hf_models.py
```

Useful development command:

```bash
python3 open-model-benchmarking/scripts/snapshot_hf_models.py --limit-per-creator 2 --output-dir /tmp/hf-model-snapshot-smoke
```

Generated files:

- `summary.json`: machine-readable aggregate counts.
- `creators.txt`: exact creator input used for the run.
- `models.raw.jsonl`: one raw Hugging Face Hub API metadata record per line.
- `models.normalized.jsonl`: one normalized model record per line.
- `models.normalized.csv`: sortable normalized table.
- `models.by-downloads.csv`: normalized table sorted by current download count.
- `models.over-100k-downloads.csv`: normalized table filtered only to records with more than 100,000 current downloads.
- `models.over-100k-downloads.ids.txt`: plain model ids from the same unfiltered-by-router over-100k download set.
- `models.by-likes.csv`: normalized table sorted by likes.
- `models.by-params.csv`: normalized table sorted by discovered parameter count.
- `creators.summary.csv`: creator-level aggregate table.

The script uses Hugging Face JSON metadata endpoints only. It does not download model weights, tokenizer files, configs through `/resolve`, or other model blobs.

By default it requests metadata fields that matter for ranking and benchmark selection:

- downloads and all-time downloads
- likes and trending score
- creator / owner
- pipeline tag and library
- license and gated/private status
- tags and base model metadata
- safetensors / GGUF metadata when exposed by the Hub
- file-name inventory from `siblings`
- parameter count when exposed by safetensors/GGUF metadata
- inference provider mapping
- router-served status from the local router snapshot
- tool and structured-output support when exposed by provider metadata

## Manual Curation

`MODEL_MANUAL_CURATION.jsonl` is the single hand-curated decision file for popular models.

Each line has exactly:

```json
{"id":"Qwen/Qwen3-8B","include":true}
```

The file intentionally stores only the include/exclude decision. Report fields such as Hugging Face links, downloads, likes, parameter count, license, router status, and tool/structured-output signals are joined from the generated snapshot.

Regenerate the report:

```bash
python3 open-model-benchmarking/scripts/generate_report.py
```

## Current Snapshot

- Router models: 123
- Serving providers: 15
- Model creators / owners: 22
- Models with tool support through at least one provider: 92
- Models with structured-output support through at least one provider: 57
- Models with image input: 36

Latest Hub metadata snapshot:

- `snapshots/hf-model-metadata-20260619T114556Z/`
- Creator namespaces requested: 22
- Normalized model records: 4,301
- Router-served records matched back to the HF router snapshot: 123
- Records with more than 100,000 current downloads: 430
- Records with discovered parameter count: 2,427
- Records with license metadata: 3,781
- Errors: 0

Manual curation status:

- Popular models curated: 430
- Included OpenClaw candidates: 254
- Excluded popular models: 176

This Hub snapshot is intentionally creator-wide. It includes all model records under the selected creator namespaces, not only chat/instruct/open-weight LLMs. The final ShellBench queue should filter this broad snapshot by task, license, gating, artifact type, model family, and OpenClaw relevance.

## Intended Workflow

1. Collect candidates from Hugging Face router and Hugging Face Hub.
2. Normalize by model family, creator, artifact, and exact revision.
3. Verify open-weight status, license, gated access, and artifact availability.
4. Deduplicate variants and group by family before benchmarking.
5. Select representative model families and artifacts for ShellBench.
6. Use benchmark results as the objective for GEPA-style prompt/profile optimization.
7. Produce `REPORT.md` with the final recommended benchmark queue and rationale.

## What This Is Not Yet

This is not yet the final list of all open-weight models worth benchmarking.

The HF router list includes models currently served through Hugging Face Inference Providers. Some are excellent benchmark candidates, but the open-weight/license status still needs to be verified against the model repos and artifacts.

## Related OpenClaw Context

- `openclaw-model-profile-registry-proposal.md` in this repo proposes ClawHub-hosted model profiles, benchmark-informed recommendations, and GEPA-style automatic profile generation.
- OpenClaw RFC `0009-model-harness-profiles.md` formalizes the safer implementation path: model harness profiles, deterministic registry resolution, exact `localModelLean` migration, and future benchmark-informed ClawHub profile packs.
