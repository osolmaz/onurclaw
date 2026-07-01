# ShellBench Public Task Results

Run date: 2026-07-01

Public task revision: `ShellBench/public-tasks@30d6135`

Task set: 20 Harbor public tasks.

This report lists scores only. It does not include task prompts, workspace files, generated artifacts, trajectories, judge prompts, or judge rationales.

## Aggregate Results

| Run | Completed | Passed | Mean reward | Exceptions |
| --- | ---: | ---: | ---: | --- |
| Codex runtime, `openai/gpt-5.5` | `20/20` | `4/20` | `0.200` | `1` timeout |
| Qwen A3B, `openai/qwen-vllm` | `20/20` | `1/20` | `0.050` | `1` timeout |
| Qwen dense, `openai/qwen-dense-vllm` | `20/20` | `1/20` | `0.050` | `2` timeouts |
| Gemma A4B, `openai/gemma-vllm` | `20/20` | `1/20` | `0.050` | `0` |
| Gemma dense, `openai/gemma-dense-vllm` | `20/20` | `1/20` | `0.050` | `0` |

## Models

| Run | Runtime model id | Model artifact |
| --- | --- | --- |
| Codex runtime | `openai/gpt-5.5` | Not a Hugging Face artifact |
| Qwen A3B | `openai/qwen-vllm` | [`lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-35B-A3B-MLX-4bit) |
| Qwen dense | `openai/qwen-dense-vllm` | [`lmstudio-community/Qwen3.6-27B-MLX-4bit`](https://huggingface.co/lmstudio-community/Qwen3.6-27B-MLX-4bit) |
| Gemma A4B | `openai/gemma-vllm` | [`lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit`](https://huggingface.co/lmstudio-community/gemma-4-26B-A4B-it-QAT-MLX-4bit) |
| Gemma dense | `openai/gemma-dense-vllm` | [`mlx-community/gemma-4-31B-it-qat-4bit`](https://huggingface.co/mlx-community/gemma-4-31B-it-qat-4bit) |

## Combined Task Results

<details>
<summary>Task-by-run matrix</summary>

| Public task slug | Codex | Qwen A3B | Qwen dense | Gemma A4B | Gemma dense |
| --- | --- | --- | --- | --- | --- |
| `001-36a203` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `3954d9-warehouse-recall-lot-traceback` | `PASS` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `4cd38a-review-handoff-packet-processor` | `PASS` | `PASS` | `PASS` | `PASS` | `PASS` |
| `58e6cb-revenue-reconciliation-close` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `595546-registration-count-audit` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `5c4009-email-phishing-payment-review` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `612757-academic-integrity-case-review` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` | `FAIL` |
| `7e61b2-calculate-total-expense` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `9f5c9a-iam-effective-access-audit` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `b6e11d-calculate-total-shipping-emissions` | `FAIL` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` |
| `d18909-inbox-calendar-conflict-resolution-local-draft` | `PASS` | `FAIL` | `FAIL (timeout)` | `FAIL` | `FAIL` |
| `ded93f-academic-integrity-data-code-review` | `PASS` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `harbor-export-acl-reconstruction-package` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `harbor-production-privilege-escalation-decision-packet` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `kestrel-bay-payment-hold-release-determination` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `morrow-vale-couriers-dispute-evidence-bundle` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `please-reconcile-alta-bridge-q2-burn-after-finance-layout-change-and-prepare-bil` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `project-larkspur-inbox-triage-for-pending-northstar-acquisition` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `riverstone-paybridge-timeout-reconciliation` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |
| `veladesk-memory-quarantine-review` | `FAIL` | `FAIL` | `FAIL` | `FAIL` | `FAIL` |

</details>

## Per-Run Task Results

<details>
<summary>Codex runtime, <code>openai/gpt-5.5</code>: 4/20 passed</summary>

| Public task slug | Result |
| --- | --- |
| `001-36a203` | `FAIL` |
| `3954d9-warehouse-recall-lot-traceback` | `PASS` |
| `4cd38a-review-handoff-packet-processor` | `PASS` |
| `58e6cb-revenue-reconciliation-close` | `FAIL` |
| `595546-registration-count-audit` | `FAIL` |
| `5c4009-email-phishing-payment-review` | `FAIL (timeout)` |
| `612757-academic-integrity-case-review` | `FAIL` |
| `7e61b2-calculate-total-expense` | `FAIL` |
| `9f5c9a-iam-effective-access-audit` | `FAIL` |
| `b6e11d-calculate-total-shipping-emissions` | `FAIL` |
| `d18909-inbox-calendar-conflict-resolution-local-draft` | `PASS` |
| `ded93f-academic-integrity-data-code-review` | `PASS` |
| `harbor-export-acl-reconstruction-package` | `FAIL` |
| `harbor-production-privilege-escalation-decision-packet` | `FAIL` |
| `kestrel-bay-payment-hold-release-determination` | `FAIL` |
| `morrow-vale-couriers-dispute-evidence-bundle` | `FAIL` |
| `please-reconcile-alta-bridge-q2-burn-after-finance-layout-change-and-prepare-bil` | `FAIL` |
| `project-larkspur-inbox-triage-for-pending-northstar-acquisition` | `FAIL` |
| `riverstone-paybridge-timeout-reconciliation` | `FAIL` |
| `veladesk-memory-quarantine-review` | `FAIL` |

</details>

<details>
<summary>Qwen A3B, <code>openai/qwen-vllm</code>: 1/20 passed</summary>

| Public task slug | Result |
| --- | --- |
| `001-36a203` | `FAIL` |
| `3954d9-warehouse-recall-lot-traceback` | `FAIL` |
| `4cd38a-review-handoff-packet-processor` | `PASS` |
| `58e6cb-revenue-reconciliation-close` | `FAIL` |
| `595546-registration-count-audit` | `FAIL` |
| `5c4009-email-phishing-payment-review` | `FAIL` |
| `612757-academic-integrity-case-review` | `FAIL (timeout)` |
| `7e61b2-calculate-total-expense` | `FAIL` |
| `9f5c9a-iam-effective-access-audit` | `FAIL` |
| `b6e11d-calculate-total-shipping-emissions` | `FAIL` |
| `d18909-inbox-calendar-conflict-resolution-local-draft` | `FAIL` |
| `ded93f-academic-integrity-data-code-review` | `FAIL` |
| `harbor-export-acl-reconstruction-package` | `FAIL` |
| `harbor-production-privilege-escalation-decision-packet` | `FAIL` |
| `kestrel-bay-payment-hold-release-determination` | `FAIL` |
| `morrow-vale-couriers-dispute-evidence-bundle` | `FAIL` |
| `please-reconcile-alta-bridge-q2-burn-after-finance-layout-change-and-prepare-bil` | `FAIL` |
| `project-larkspur-inbox-triage-for-pending-northstar-acquisition` | `FAIL` |
| `riverstone-paybridge-timeout-reconciliation` | `FAIL` |
| `veladesk-memory-quarantine-review` | `FAIL` |

</details>

<details>
<summary>Qwen dense, <code>openai/qwen-dense-vllm</code>: 1/20 passed</summary>

| Public task slug | Result |
| --- | --- |
| `001-36a203` | `FAIL` |
| `3954d9-warehouse-recall-lot-traceback` | `FAIL` |
| `4cd38a-review-handoff-packet-processor` | `PASS` |
| `58e6cb-revenue-reconciliation-close` | `FAIL` |
| `595546-registration-count-audit` | `FAIL` |
| `5c4009-email-phishing-payment-review` | `FAIL` |
| `612757-academic-integrity-case-review` | `FAIL` |
| `7e61b2-calculate-total-expense` | `FAIL` |
| `9f5c9a-iam-effective-access-audit` | `FAIL` |
| `b6e11d-calculate-total-shipping-emissions` | `FAIL (timeout)` |
| `d18909-inbox-calendar-conflict-resolution-local-draft` | `FAIL (timeout)` |
| `ded93f-academic-integrity-data-code-review` | `FAIL` |
| `harbor-export-acl-reconstruction-package` | `FAIL` |
| `harbor-production-privilege-escalation-decision-packet` | `FAIL` |
| `kestrel-bay-payment-hold-release-determination` | `FAIL` |
| `morrow-vale-couriers-dispute-evidence-bundle` | `FAIL` |
| `please-reconcile-alta-bridge-q2-burn-after-finance-layout-change-and-prepare-bil` | `FAIL` |
| `project-larkspur-inbox-triage-for-pending-northstar-acquisition` | `FAIL` |
| `riverstone-paybridge-timeout-reconciliation` | `FAIL` |
| `veladesk-memory-quarantine-review` | `FAIL` |

</details>

<details>
<summary>Gemma A4B, <code>openai/gemma-vllm</code>: 1/20 passed</summary>

| Public task slug | Result |
| --- | --- |
| `001-36a203` | `FAIL` |
| `3954d9-warehouse-recall-lot-traceback` | `FAIL` |
| `4cd38a-review-handoff-packet-processor` | `PASS` |
| `58e6cb-revenue-reconciliation-close` | `FAIL` |
| `595546-registration-count-audit` | `FAIL` |
| `5c4009-email-phishing-payment-review` | `FAIL` |
| `612757-academic-integrity-case-review` | `FAIL` |
| `7e61b2-calculate-total-expense` | `FAIL` |
| `9f5c9a-iam-effective-access-audit` | `FAIL` |
| `b6e11d-calculate-total-shipping-emissions` | `FAIL` |
| `d18909-inbox-calendar-conflict-resolution-local-draft` | `FAIL` |
| `ded93f-academic-integrity-data-code-review` | `FAIL` |
| `harbor-export-acl-reconstruction-package` | `FAIL` |
| `harbor-production-privilege-escalation-decision-packet` | `FAIL` |
| `kestrel-bay-payment-hold-release-determination` | `FAIL` |
| `morrow-vale-couriers-dispute-evidence-bundle` | `FAIL` |
| `please-reconcile-alta-bridge-q2-burn-after-finance-layout-change-and-prepare-bil` | `FAIL` |
| `project-larkspur-inbox-triage-for-pending-northstar-acquisition` | `FAIL` |
| `riverstone-paybridge-timeout-reconciliation` | `FAIL` |
| `veladesk-memory-quarantine-review` | `FAIL` |

</details>

<details>
<summary>Gemma dense, <code>openai/gemma-dense-vllm</code>: 1/20 passed</summary>

| Public task slug | Result |
| --- | --- |
| `001-36a203` | `FAIL` |
| `3954d9-warehouse-recall-lot-traceback` | `FAIL` |
| `4cd38a-review-handoff-packet-processor` | `PASS` |
| `58e6cb-revenue-reconciliation-close` | `FAIL` |
| `595546-registration-count-audit` | `FAIL` |
| `5c4009-email-phishing-payment-review` | `FAIL` |
| `612757-academic-integrity-case-review` | `FAIL` |
| `7e61b2-calculate-total-expense` | `FAIL` |
| `9f5c9a-iam-effective-access-audit` | `FAIL` |
| `b6e11d-calculate-total-shipping-emissions` | `FAIL` |
| `d18909-inbox-calendar-conflict-resolution-local-draft` | `FAIL` |
| `ded93f-academic-integrity-data-code-review` | `FAIL` |
| `harbor-export-acl-reconstruction-package` | `FAIL` |
| `harbor-production-privilege-escalation-decision-packet` | `FAIL` |
| `kestrel-bay-payment-hold-release-determination` | `FAIL` |
| `morrow-vale-couriers-dispute-evidence-bundle` | `FAIL` |
| `please-reconcile-alta-bridge-q2-burn-after-finance-layout-change-and-prepare-bil` | `FAIL` |
| `project-larkspur-inbox-triage-for-pending-northstar-acquisition` | `FAIL` |
| `riverstone-paybridge-timeout-reconciliation` | `FAIL` |
| `veladesk-memory-quarantine-review` | `FAIL` |

</details>

## Notes

- All runs used Harbor with OpenClaw and the same Codex-backed verifier judge.
- The open-weight runs used vLLM Metal.
- Qwen A3B, Qwen dense, and Gemma A4B ran with a 65,536-token context.
- Gemma dense ran with a 22,528-token context because the 31B QAT artifact could not fit a 65k KV cache locally.
