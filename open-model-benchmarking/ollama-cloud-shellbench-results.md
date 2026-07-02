# Ollama Cloud ShellBench Results

Run date: 2026-07-02

Public task revision: `ShellBench/public-tasks@30d6135`

Task set: 20 Harbor public tasks.

This report lists scores only. It does not include task prompts, workspace files, generated artifacts, trajectories, judge prompts, or judge rationales.

## Run Setup

- Harness: Harbor with stock OpenClaw embedded runtime.
- Agent endpoint: Ollama Cloud OpenAI-compatible API at `https://ollama.com/v1`.
- Judge endpoint: local Codex-backed OpenAI-compatible verifier proxy.
- Judge model: `gpt-5.5`.
- Runner: `shellbench-local/scripts/run_openclaw_ollama_cloud_public.sh`.
- Jobs root: `shellbench-local/harbor-jobs/openclaw-ollama-cloud-public-clean-20260702`.
- Parallelism: 3 concurrent Harbor task containers.
- Prompting: same public task instructions for all models; no extra model-specific instructions.

## Summary

| Model | Provider family | Completed | Passed | Mean reward | Exceptions |
| --- | --- | ---: | ---: | ---: | --- |
| [`glm-5.2:cloud`](https://ollama.com/library/glm-5.2) | Z.ai GLM | `20/20` | `3/20` | `0.150` | `0` |
| [`kimi-k2.7-code:cloud`](https://ollama.com/library/kimi-k2.7-code) | Moonshot Kimi | `20/20` | `2/20` | `0.100` | `0` |
| [`minimax-m3:cloud`](https://ollama.com/library/minimax-m3) | MiniMax | `20/20` | `3/20` | `0.150` | `1` timeout |
| [`deepseek-v4-flash:cloud`](https://ollama.com/library/deepseek-v4-flash) | DeepSeek | `20/20` | `4/20` | `0.200` | `0` |
| [`deepseek-v4-pro:cloud`](https://ollama.com/library/deepseek-v4-pro) | DeepSeek | `20/20` | `5/20` | `0.250` | `1` agent exit |
| [`qwen3.5:397b-cloud`](https://ollama.com/library/qwen3.5/tags) | Qwen | `20/20` | `2/20` | `0.100` | `0` |
| [`gemma4:cloud`](https://ollama.com/library/gemma4/tags) | Google Gemma | `20/20` | `1/20` | `0.050` | `1` timeout |

## Task Matrix

<details open>
<summary>Task-by-model results</summary>

| Public task slug | [`glm-5.2:cloud`](https://ollama.com/library/glm-5.2) | [`kimi-k2.7-code:cloud`](https://ollama.com/library/kimi-k2.7-code) | [`minimax-m3:cloud`](https://ollama.com/library/minimax-m3) | [`deepseek-v4-flash:cloud`](https://ollama.com/library/deepseek-v4-flash) | [`deepseek-v4-pro:cloud`](https://ollama.com/library/deepseek-v4-pro) | [`qwen3.5:397b-cloud`](https://ollama.com/library/qwen3.5/tags) | [`gemma4:cloud`](https://ollama.com/library/gemma4/tags) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `001-36a203` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `3954d9-warehouse-recall-lot-traceback` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `FAIL` | `FAIL` |
| `4cd38a-review-handoff-packet-processor` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` |
| `58e6cb-revenue-reconciliation-close` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL (agent exit)` | `FAIL` | `FAIL (timeout)` |
| `595546-registration-count-audit` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `5c4009-email-phishing-payment-review` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `FAIL` | `FAIL` | `FAIL` |
| `612757-academic-integrity-case-review` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `7e61b2-calculate-total-expense` | `FAIL` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `9f5c9a-iam-effective-access-audit` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `b6e11d-calculate-total-shipping-emissions` | `PASS` | `FAIL` | `PASS` | `PASS` | `PASS` | `FAIL` | `FAIL` |
| `d18909-inbox-calendar-conflict-resolution-local-draft` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `PASS` | `FAIL` |
| `ded93f-academic-integrity-data-code-review` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `PASS` | `FAIL` | `FAIL` |
| `harbor-export-acl-reconstruction-package` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `harbor-production-privilege-escalation-decision-packet` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `kestrel-bay-payment-hold-release-determination` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `morrow-vale-couriers-dispute-evidence-bundle` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `please-reconcile-alta-bridge-q2-burn-after-finance-layout-change-and-prepare-bil` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `project-larkspur-inbox-triage-for-pending-northstar-acquisition` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `riverstone-paybridge-timeout-reconciliation` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `veladesk-memory-quarantine-review` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |

</details>

## Per-Model Results

<details>
<summary><code>glm-5.2:cloud</code>: 3/20 passed</summary>

Passed:

- `3954d9-warehouse-recall-lot-traceback`
- `4cd38a-review-handoff-packet-processor`
- `b6e11d-calculate-total-shipping-emissions`

Exceptions: none.

</details>

<details>
<summary><code>kimi-k2.7-code:cloud</code>: 2/20 passed</summary>

Passed:

- `3954d9-warehouse-recall-lot-traceback`
- `4cd38a-review-handoff-packet-processor`

Exceptions: none.

</details>

<details>
<summary><code>minimax-m3:cloud</code>: 3/20 passed</summary>

Passed:

- `3954d9-warehouse-recall-lot-traceback`
- `4cd38a-review-handoff-packet-processor`
- `b6e11d-calculate-total-shipping-emissions`

Exceptions:

- `7e61b2-calculate-total-expense`: `AgentTimeoutError`

</details>

<details>
<summary><code>deepseek-v4-flash:cloud</code>: 4/20 passed</summary>

Passed:

- `3954d9-warehouse-recall-lot-traceback`
- `4cd38a-review-handoff-packet-processor`
- `5c4009-email-phishing-payment-review`
- `b6e11d-calculate-total-shipping-emissions`

Exceptions: none.

</details>

<details>
<summary><code>deepseek-v4-pro:cloud</code>: 5/20 passed</summary>

Passed:

- `3954d9-warehouse-recall-lot-traceback`
- `4cd38a-review-handoff-packet-processor`
- `b6e11d-calculate-total-shipping-emissions`
- `d18909-inbox-calendar-conflict-resolution-local-draft`
- `ded93f-academic-integrity-data-code-review`

Exceptions:

- `58e6cb-revenue-reconciliation-close`: `NonZeroAgentExitCodeError`

</details>

<details>
<summary><code>qwen3.5:397b-cloud</code>: 2/20 passed</summary>

Passed:

- `4cd38a-review-handoff-packet-processor`
- `d18909-inbox-calendar-conflict-resolution-local-draft`

Exceptions: none.

</details>

<details>
<summary><code>gemma4:cloud</code>: 1/20 passed</summary>

Passed:

- `4cd38a-review-handoff-packet-processor`

Exceptions:

- `58e6cb-revenue-reconciliation-close`: `AgentTimeoutError`

</details>
