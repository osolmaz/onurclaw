# ShellBench Public Task Run Results

Date: 2026-07-01

Status: baseline local run complete.

This report records ShellBench public Harbor task results for OpenClaw runtime and local open-weight model experiments. It intentionally excludes task prompts, fixture contents, workspace packets, generated artifacts, verifier rationales, and raw trajectories.

## Non-Sensitive Scope

Included:

- Aggregate pass counts and mean reward.
- Runtime and model identifiers.
- High-level harness notes needed to reproduce the benchmark setup.
- An anonymized per-task score matrix using stable labels and SHA-256 prefixes of task slugs.

Excluded:

- Task text, task instructions, and scenario descriptions.
- Input data files from task workspaces.
- Agent outputs and generated task artifacts.
- Judge prompts, judge responses, and free-text verdict reasons.
- Raw Harbor job directories.

Raw Harbor outputs remain local under `/Users/onur/repos/shellbench-local/harbor-jobs/` and are not copied into this public repo.

## Benchmark Setup

- Public task checkout: `ShellBench/public-tasks`
- Public task revision: `30d6135`
- Task set: 20 Harbor public tasks under `tasks/harbor`
- Harness: Harbor running OpenClaw
- Scoring: local OpenAI-compatible Codex judge proxy backed by `codex exec -m gpt-5.5`
- Local Docker workaround: temporary task copies rewrote deprecated `allow_internet = false` to `allow_internet = true` because this Harbor Docker backend rejected the corresponding no-network mode. The source public-task checkout was not modified.
- Fairness rule for model comparison: no extra model-specific task instructions were used in the scored runs.

## Aggregate Results

| Runtime / model | Completed | Passed | Mean reward | Exceptions |
| --- | ---: | ---: | ---: | --- |
| OpenClaw Codex runtime + `openai/gpt-5.5` | `20/20` | `4/20` | `0.200` | `1` timeout |
| OpenClaw embedded + vLLM Qwen A3B, `openai/qwen-vllm` | `20/20` | `1/20` | `0.050` | `1` timeout |
| OpenClaw embedded + vLLM Qwen dense 27B, `openai/qwen-dense-vllm` | `20/20` | `1/20` | `0.050` | `2` timeouts |
| OpenClaw embedded + vLLM Gemma A4B, `openai/gemma-vllm` | `20/20` | `1/20` | `0.050` | `0` |
| OpenClaw embedded + vLLM Gemma dense 31B QAT, `openai/gemma-dense-vllm` | `20/20` | `1/20` | `0.050` | `0` |

## Model Artifacts

| Run label | Model artifact | Serving notes |
| --- | --- | --- |
| Codex | `openai/gpt-5.5` | OpenClaw Gateway-backed Codex runtime; not `--local` embedded runtime |
| Qwen A3B | `lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit` | vLLM Metal, 65,536-token context |
| Qwen dense | `lmstudio-community/Qwen3.6-27B-MLX-4bit` | vLLM Metal, 65,536-token context |
| Gemma A4B | `lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit` | vLLM Metal, 65,536-token context |
| Gemma dense | `mlx-community/gemma-4-31B-it-qat-4bit` | vLLM Metal, 22,528-token context due to KV-cache capacity |

## Per-Task Score Matrix

Task labels are anonymized. `Task hash` is the first 12 hex characters of `sha256(public_task_slug)`, included only to make this matrix stable across internal reruns without publishing task content here.

| Task | Task hash | Codex | Qwen A3B | Qwen dense | Gemma A4B | Gemma dense |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `T01` | `a72d5aa40cb2` | `0` | `0` | `0` | `0` | `0` |
| `T02` | `83602c9ceefd` | `1` | `0` | `0` | `0` | `0` |
| `T03` | `e0f32729303f` | `1` | `1` | `1` | `1` | `1` |
| `T04` | `147197956235` | `0` | `0` | `0` | `0` | `0` |
| `T05` | `7507222d7cdf` | `0` | `0` | `0` | `0` | `0` |
| `T06` | `758ebecb63b6` | `0` | `0` | `0` | `0` | `0` |
| `T07` | `5daaf98f0001` | `0` | `0` | `0` | `0` | `0` |
| `T08` | `d2c1f21c8434` | `0` | `0` | `0` | `0` | `0` |
| `T09` | `555b37e39846` | `0` | `0` | `0` | `0` | `0` |
| `T10` | `ee7d175b23a3` | `0` | `0` | `0` | `0` | `0` |
| `T11` | `0cad87c7900c` | `1` | `0` | `0` | `0` | `0` |
| `T12` | `8ea6ed034af2` | `1` | `0` | `0` | `0` | `0` |
| `T13` | `1da635f5a536` | `0` | `0` | `0` | `0` | `0` |
| `T14` | `83a641021ed7` | `0` | `0` | `0` | `0` | `0` |
| `T15` | `88818d15af82` | `0` | `0` | `0` | `0` | `0` |
| `T16` | `40d7109adacc` | `0` | `0` | `0` | `0` | `0` |
| `T17` | `0bd2a7eb8702` | `0` | `0` | `0` | `0` | `0` |
| `T18` | `971682e7f209` | `0` | `0` | `0` | `0` | `0` |
| `T19` | `2008671ec8bd` | `0` | `0` | `0` | `0` | `0` |
| `T20` | `6cfba286b28d` | `0` | `0` | `0` | `0` | `0` |

## Interpretation

- Codex runtime was the strongest baseline in this run: `4/20`, mean reward `0.200`.
- Every tested vLLM open-weight run passed the same single task and scored `1/20`, mean reward `0.050`.
- No Qwen or Gemma vLLM run passed a task that Codex failed.
- Dense variants did not improve aggregate score over the smaller/sparser variants in this harness setup.
- The Gemma dense run is not a perfect context-equivalent comparison because the 31B QAT model could not fit a 65k KV cache locally; it ran at 22,528 tokens.

## Reproducibility Pointers

Canonical local notes with raw job paths and command details:

```text
/Users/onur/repos/shellbench-local/reports/openclaw-local-runtime-benchmark.md
```

Those local notes may reference raw task names and job directories. They should remain outside this public repo unless redacted.
