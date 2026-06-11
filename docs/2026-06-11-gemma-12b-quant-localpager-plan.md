---
title: Gemma 4 12B Quant Localpager Agent Test Plan
author: Bob <dutifulbob@gmail.com>
date: 2026-06-11
---

# Gemma 4 12B Quant Localpager Agent Test Plan

Plan for rerunning the Gemma 4 12B quantization smoke test through the maintained
batch Localpager Agent path.

## Goal

Compare reasoning-enabled Gemma 4 12B quantizations on the same small OpenClaw
classification sample while ensuring every classification call goes through
Localpager Agent.

This rerun replaces the earlier direct recorder path. Do not use the archived
direct OpenAI-compatible recorder for classification runs.

## Repos

- dataset repo: `/home/bob/oc/openclaw-classification-dataset`
- runner: `scripts/batch_localpager_agent_prompt.mjs`
- prompt: `prompts/localpager-openclaw-routing-v8-production.hbs`
- dataset: `ds4.jsonl`
- output root: `scratch/gemma-12b-quant-smoke-localpager-reasoning/`

## Runtime Rules

- Run one quantization at a time.
- Before each command, confirm LM Studio has the matching model loaded.
- Keep DS4 stopped during the test to reduce memory pressure.
- Use Localpager Agent batch runner only.
- Use `--sample stratified --limit 5` to match the earlier quant smoke shape.
- Use high context and high output caps so the test is not distorted by
  truncation:
  - `--context-window 262144` when LM Studio loaded the model at 262k context.
  - `--context-window 131072` only if that is the actual loaded context.
  - `--max-tokens 16384` for reasoning-enabled runs.

## Preflight

```bash
cd /home/bob/oc/openclaw-classification-dataset

systemctl --user stop ds4-server.service || true
systemctl --user start lm-studio.service

node --check scripts/batch_localpager_agent_prompt.mjs
curl -fsS http://127.0.0.1:1234/v1/models | jq .
```

Confirm the model id returned by LM Studio matches the command being run.

## Commands

Run each command only after loading the matching reasoning-enabled quant in
LM Studio.

```bash
node scripts/batch_localpager_agent_prompt.mjs \
  --model gemma-12b-q4km-reason \
  --model-key gemma-12b-q4km-reason \
  --model-quantization "Q4_K_M (4-bit)" \
  --base-url http://127.0.0.1:1234/v1 \
  --prompt-id localpager-openclaw-routing-v8-production \
  --prompt-template prompts/localpager-openclaw-routing-v8-production.hbs \
  --sample stratified \
  --limit 5 \
  --context-window 262144 \
  --max-tokens 16384 \
  --temperature 0 \
  --top-p 1 \
  --seed 1234 \
  --presence-penalty 0 \
  --frequency-penalty 0 \
  --thinking on \
  --run-dir scratch/gemma-12b-quant-smoke-localpager-reasoning/q4-k-m \
  --quiet
```

Repeat the same command shape for:

| Quant | Model | Model key | Run dir |
| --- | --- | --- | --- |
| QAT-Q4_0 | `gemma-12b-qat-q4-reason` | `gemma-12b-qat-q4-reason` | `scratch/gemma-12b-quant-smoke-localpager-reasoning/qat-q4-0` |
| Q6_K | `gemma-12b-q6k-reason` | `gemma-12b-q6k-reason` | `scratch/gemma-12b-quant-smoke-localpager-reasoning/q6-k` |
| Q8_0 | `gemma-12b-q8-reason` | `gemma-12b-q8-reason` | `scratch/gemma-12b-quant-smoke-localpager-reasoning/q8-0` |

## Review Checklist

- [ ] Every run has `errors=0` or each error is explained.
- [ ] Every run has `schema_errors=0` or each schema error is inspected.
- [ ] Compare rows/min, average latency, p95 latency, and completion behavior.
- [ ] Compare label quality manually on the five sampled rows.
- [ ] Do not commit raw `raw/` Localpager Agent artifacts unless there is a
      specific provenance reason.
- [ ] If results are useful, commit compact summaries or derived writeups only.
