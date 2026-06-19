# Open Model Benchmarking Report

Status: draft scaffold.

This report will identify open-weight and open-model candidates that should be benchmarked in ShellBench and optimized with GEPA-style profile or prompt search.

## Objective

Find the model families and artifacts that matter most for OpenClaw model profiles.

The final report should answer:

- Which open-weight models are worth benchmarking first?
- Which served models are already available through Hugging Face Inference Providers?
- Which model families need separate profiles because their harness behavior differs?
- Which artifacts or quantizations need separate evaluation?
- Which profile dimensions should GEPA optimize first: system prompt, tool exposure, Tool Search, reasoning defaults, memory, or context posture?

## Current Data Source

Initial source:

```text
https://router.huggingface.co/v1/models
```

This produced:

- 123 router-served chat models
- 15 serving providers
- 22 model creators / owners

The raw and normalized data are in `data/`.

The next source is the Hugging Face Hub model metadata API, driven by creator slugs in `creators.txt` and implemented in `scripts/snapshot_hf_models.py`.

That snapshotter captures model metadata needed for later ranking:

- downloads
- all-time downloads where exposed
- likes
- trending score
- parameter count where exposed
- license
- gated/private status
- task / pipeline tag
- model files by filename only
- safetensors / GGUF metadata
- inference provider mapping
- router-served status
- tool and structured-output support

The first full Hub metadata snapshot is in `snapshots/hf-model-metadata-20260619T114556Z/`.

It contains:

- 4,301 normalized model records
- 22 creator namespaces
- 123 records matched back to the router-served model list
- 430 records with more than 100,000 current downloads
- 2,427 records with discovered parameter count
- 3,781 records with license metadata
- 98 records with tool support through either Hub provider metadata or the router snapshot
- 62 records with structured-output support through either Hub provider metadata or the router snapshot
- 0 collection errors

This is a broad creator-wide snapshot. It is not yet the final ShellBench benchmark queue. The next step is to filter it down to chat/instruct/coding/tool-capable open-weight model families and exact artifacts.

## Known Serving Providers

- `cerebras`
- `cohere`
- `deepinfra`
- `featherless-ai`
- `fireworks-ai`
- `groq`
- `hyperbolic`
- `novita`
- `nscale`
- `ovhcloud`
- `publicai`
- `sambanova`
- `scaleway`
- `together`
- `zai-org`

## Known Model Creators / Owners

- `CohereLabs`
- `EssentialAI`
- `MiniMaxAI`
- `Qwen`
- `Sao10K`
- `aisingapore`
- `allenai`
- `alpindale`
- `baidu`
- `deepcogito`
- `deepseek-ai`
- `google`
- `inclusionAI`
- `meta-llama`
- `moonshotai`
- `nvidia`
- `openai`
- `pearl-ai`
- `stepfun-ai`
- `swiss-ai`
- `utter-project`
- `zai-org`

## Early Candidate Families

These are not final benchmark recommendations yet. They are high-signal families present in the first HF router snapshot:

- Qwen
- Gemma
- Llama
- DeepSeek
- Kimi
- GLM
- MiniMax
- Nemotron
- GPT-OSS
- Cohere Command / Aya
- OLMo
- Apertus
- SEA-LION
- EuroLLM

## Selection Criteria To Fill In

Candidate priority should consider:

- Open-weight/license status.
- Whether the model is instruct/chat/coding/tool-capable.
- Adoption signal: router availability, provider count, downloads, likes, community usage.
- OpenClaw relevance: tools, ShellBench tasks, code editing, messaging, long workflows.
- Size and capacity class.
- Artifact formats: safetensors, GGUF, MLX, Ollama.
- Whether the benchmark target should be family-level or artifact-level.
- Whether GEPA can realistically optimize a stable profile for the target.

## Open Questions

- Should the first benchmark queue include only router-served models, or combine router-served models with locally served GGUF/Ollama models?
- Which ShellBench subset should be the initial objective?
- Should GEPA optimize only system prompt first, or also tool exposure and Tool Search defaults?
- Should vision-language models enter the first queue, or should text-only models come first?
- Should guard/safety models be excluded from the first ShellBench queue?
- Should community fine-tunes like `Sao10K/*` and `alpindale/*` be benchmarked early, or only after publisher families are covered?

## Next Steps

1. Enrich the HF router snapshot with Hugging Face Hub metadata.
2. Mark each model as open-weight, gated open-weight, hosted-only, unclear, or out of scope.
3. Group model ids into canonical families.
4. Add license, parameter count, base model, and artifact availability.
5. Build a first ShellBench queue with size and family coverage.
6. Run baseline ShellBench.
7. Use GEPA-style optimization to propose profile changes.
8. Compare optimized profiles against baseline profiles.
9. Promote stable results into the model profile registry proposal.
