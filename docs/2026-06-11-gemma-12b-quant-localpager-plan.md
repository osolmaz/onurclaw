---
title: Gemma 4 12B Quant Localpager Agent Test Plan
author: Bob <dutifulbob@gmail.com>
date: 2026-06-11
---

# Gemma 4 12B Quant Localpager Agent Test Plan

Plan for rerunning the Gemma 4 12B quantization smoke test through the maintained
batch Localpager Agent path.

## Goal

Compare reasoning-enabled Gemma 4 12B quantizations on the same single OpenClaw
classification row while ensuring every classification call goes through
Localpager Agent. Also determine the highest safe Localpager Agent concurrency
for each loaded quantization.

This rerun replaces the earlier direct recorder path. Do not use the archived
direct OpenAI-compatible recorder for classification runs.

## Repos

- dataset repo: `/home/bob/oc/openclaw-classification-dataset`
- runner: `scripts/batch_localpager_agent_prompt.mjs`
- Localpager Agent bin: `localpager-agent`
- prompt: `prompts/2026-06-09-ds4-topic-inventory.hbs`
- dataset: `ds4.jsonl`
- output root: `scratch/gemma-12b-quant-smoke-localpager-reasoning/`
- concurrency output root:
  `scratch/gemma-12b-quant-concurrency-localpager-reasoning/`

## Runtime Rules

- Run one quantization at a time.
- Before each command, confirm LM Studio has the matching model loaded.
- Keep DS4 stopped during the test to reduce memory pressure.
- Use Localpager Agent batch runner only.
- Use the installed `localpager-agent` command. Do not pass the
  `/home/bob/repos/localpager/localpager-agent` source directory as an
  executable.
- Use one row per quantization for the quality/speed smoke.
- Use a small multi-row sample only for concurrency probing.
- Use high context and high output caps so the test is not distorted by
  truncation:
  - `--context-window 262144` when LM Studio loaded the model at 262k context.
  - `--context-window 131072` only if that is the actual loaded context.
  - `--max-tokens 16384` for reasoning-enabled runs.
- Gemma 4 12B reasoning can take a long time, but this smoke test must not let
  a single row occupy the machine indefinitely. Use a 4-minute per-row task cap:
  `--timeout-ms 240000`.
- Treat a 4-minute timeout as the result for that quantization/settings pair:
  record it as too slow or failed, then move on. Do not raise the timeout to
  wait for a slow reasoning trace.
- Use a valid Localpager/Pi thinking level. Valid levels are `off`, `minimal`,
  `low`, `medium`, `high`, and `xhigh`; do not use `on`.
- Start concurrency at `1`.
- Raise concurrency gradually only after the previous level completed without
  OOM, server crash, schema failures caused by truncation, or request timeouts.

## Preflight

```bash
cd /home/bob/oc/openclaw-classification-dataset

systemctl --user stop ds4-server.service || true
systemctl --user start lm-studio.service

cd /home/bob/repos/localpager/localpager-agent
npm run build
npm link

cd /home/bob/oc/openclaw-classification-dataset
command -v localpager-agent
node --check scripts/batch_localpager_agent_prompt.mjs
curl -fsS http://127.0.0.1:1234/v1/models | jq .
localpager-agent --status
```

Confirm the model id returned by LM Studio matches the command being run.
`localpager-agent --status` must report a loaded model before starting a smoke
run. If it reports no models, load the target reasoning quant in LM Studio
first.

## Current Finding

The first Q4_K_M trial was run with invalid `--thinking on`; Pi recorded the
effective thinking level as `off`, and the row still took 245.7 seconds. A
second trial with valid `--thinking high` reached the old one-hour timeout
without a final structured output. LM Studio logs showed prompt processing took
only seconds; the time was spent generating a very long reasoning stream. A
third trial with `--thinking medium` was still generating after many minutes and
was killed manually.

Use `--thinking low` plus the 4-minute timeout for the next smoke. If `low`
times out, record that result and either test a lower reasoning level or reject
the quant/settings pair for this task.

## Commands

Run each command only after loading the matching reasoning-enabled quant in
LM Studio. The quality/speed smoke is one row per quantization.

```bash
node scripts/batch_localpager_agent_prompt.mjs \
  --model gemma-12b-q4km-reason \
  --model-key gemma-12b-q4km-reason \
  --model-quantization "Q4_K_M (4-bit)" \
  --base-url http://127.0.0.1:1234/v1 \
  --prompt-id ds4-topic-inventory \
  --prompt-template prompts/2026-06-09-ds4-topic-inventory.hbs \
  --sample head \
  --limit 1 \
  --context-window 262144 \
  --max-tokens 16384 \
  --temperature 0 \
  --top-p 1 \
  --seed 1234 \
  --presence-penalty 0 \
  --frequency-penalty 0 \
  --thinking low \
  --timeout-ms 240000 \
  --run-dir scratch/gemma-12b-quant-smoke-localpager-reasoning/q4-k-m \
  --quiet
```

Repeat the same command shape for:

| Quant | Model | Model key | Run dir |
| --- | --- | --- | --- |
| QAT-Q4_0 | `gemma-12b-qat-q4-reason` | `gemma-12b-qat-q4-reason` | `scratch/gemma-12b-quant-smoke-localpager-reasoning/qat-q4-0` |
| Q6_K | `gemma-12b-q6k-reason` | `gemma-12b-q6k-reason` | `scratch/gemma-12b-quant-smoke-localpager-reasoning/q6-k` |
| Q8_0 | `gemma-12b-q8-reason` | `gemma-12b-q8-reason` | `scratch/gemma-12b-quant-smoke-localpager-reasoning/q8-0` |

## Concurrency Probe

After the one-row smoke passes for a quantization, probe the highest safe
concurrency for that same loaded quant.

The batch runner should expose a concurrency setting before this probe is run.
Use Localpager Agent for every row; do not switch back to a direct recorder.

Probe order:

1. `--concurrency 1`
2. `--concurrency 2`
3. `--concurrency 3`
4. Stop at the first OOM, server restart, timeout burst, or materially worse
   schema/output failure rate.

Use a small enough sample to avoid wasting machine time while still exercising
parallelism:

```bash
node scripts/batch_localpager_agent_prompt.mjs \
  --model gemma-12b-q4km-reason \
  --model-key gemma-12b-q4km-reason-c2 \
  --model-quantization "Q4_K_M (4-bit)" \
  --base-url http://127.0.0.1:1234/v1 \
  --prompt-id ds4-topic-inventory \
  --prompt-template prompts/2026-06-09-ds4-topic-inventory.hbs \
  --sample stratified \
  --limit 6 \
  --context-window 262144 \
  --max-tokens 16384 \
  --temperature 0 \
  --top-p 1 \
  --seed 1234 \
  --presence-penalty 0 \
  --frequency-penalty 0 \
  --thinking low \
  --timeout-ms 240000 \
  --concurrency 2 \
  --run-dir scratch/gemma-12b-quant-concurrency-localpager-reasoning/q4-k-m-c2 \
  --quiet
```

Repeat the command shape for each quant and each concurrency level. Name run
dirs with the quant and concurrency, for example `q6-k-c1`, `q6-k-c2`, and
`q6-k-c3`.

Record the chosen safe concurrency per quant:

| Quant | Safe concurrency | Reason |
| --- | ---: | --- |
| Q4_K_M | TBD | TBD |
| QAT-Q4_0 | TBD | TBD |
| Q6_K | TBD | TBD |
| Q8_0 | TBD | TBD |

## Metrics To Extract

Each smoke and concurrency run must produce a compact metrics record. Do not
rely only on the Markdown summary.

Record these fields for each run:

- quantization
- model id
- loaded context length
- requested `--context-window`
- requested `--max-tokens`
- requested `--thinking`
- requested concurrency
- sample mode and row count
- total wall time
- per-row elapsed seconds
- average latency seconds
- p95 latency seconds
- rows/min
- prompt tokens
- completion tokens
- total tokens
- reasoning tokens, when exposed
- completion tokens/sec
- total tokens/sec
- error count
- schema error count
- output topics for the one-row smoke

Expected sources:

- `*.outputs.jsonl`: per-row outputs, per-row elapsed seconds, parsed usage when
  Localpager Agent exposes it.
- `*.run-stats.json`: aggregate elapsed time, latency, rows/min, errors, and
  schema errors.
- `summary.md`: human-readable cross-check only.
- raw Localpager Agent session artifacts: fallback source for usage fields when
  the compact output has `usage: null`.
- LM Studio logs: fallback source for prompt/completion/reasoning token counts
  and tokens/sec if Localpager artifacts do not expose them.

If any token or speed field cannot be extracted, mark it as `missing` and write
the reason. Do not treat missing usage as zero.

## Review Checklist

- [ ] Every one-row smoke has `errors=0` or each error is explained.
- [ ] Every concurrency probe has `errors=0` or each error is explained.
- [ ] Every run has `schema_errors=0` or each schema error is inspected.
- [ ] Extract total duration, tokens/sec, token counts, latency, rows/min, and
      reasoning-token values where available.
- [ ] Compare rows/min, average latency, p95 latency, token speed, and
      completion behavior.
- [ ] Compare label quality manually on the one-row smoke outputs.
- [ ] Record the highest safe concurrency for each quantization.
- [ ] Do not commit raw `raw/` Localpager Agent artifacts unless there is a
      specific provenance reason.
- [ ] If results are useful, commit compact summaries or derived writeups only.
