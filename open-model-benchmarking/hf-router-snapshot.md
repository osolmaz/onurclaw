# Hugging Face Router Snapshot

Captured from:

```text
https://router.huggingface.co/v1/models
```

Capture timestamp:

```text
2026-06-19T11:23:39Z
```

This endpoint lists OpenAI-compatible chat-completion models currently served by Hugging Face Inference Providers. It is a good first source for models that can be benchmarked without setting up our own serving infrastructure.

## Serving Providers

The snapshot includes these providers:

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

Provider counts in the router snapshot:

| Provider | Model entries |
| --- | ---: |
| `featherless-ai` | 74 |
| `novita` | 66 |
| `deepinfra` | 30 |
| `together` | 24 |
| `nscale` | 16 |
| `zai-org` | 16 |
| `fireworks-ai` | 13 |
| `cohere` | 11 |
| `scaleway` | 10 |
| `ovhcloud` | 8 |
| `groq` | 6 |
| `publicai` | 6 |
| `cerebras` | 2 |
| `hyperbolic` | 1 |
| `sambanova` | 1 |

## Model Creators / Owners

The snapshot includes these model creators / owners:

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

Creator counts in the router snapshot:

| Creator | Model entries |
| --- | ---: |
| `Qwen` | 31 |
| `zai-org` | 19 |
| `deepseek-ai` | 14 |
| `CohereLabs` | 11 |
| `meta-llama` | 8 |
| `MiniMaxAI` | 6 |
| `google` | 6 |
| `moonshotai` | 6 |
| `openai` | 3 |
| `Sao10K` | 2 |
| `aisingapore` | 2 |
| `deepcogito` | 2 |
| `nvidia` | 2 |
| `stepfun-ai` | 2 |
| `swiss-ai` | 2 |
| `EssentialAI` | 1 |
| `allenai` | 1 |
| `alpindale` | 1 |
| `baidu` | 1 |
| `inclusionAI` | 1 |
| `pearl-ai` | 1 |
| `utter-project` | 1 |

## SEA-LION Note

`aisingapore` appears because the router currently serves:

- `aisingapore/Gemma-SEA-LION-v4-27B-IT`
- `aisingapore/Qwen-SEA-LION-v4-32B-IT`

Both are text-in/text-out SEA-LION models served by `featherless-ai` and `publicai` in the captured snapshot.

## Data Files

- `data/hf-router-models-20260619T112339Z.json`
- `data/hf-router-models-20260619T112339Z.tsv`
- `data/hf-router-models-20260619T112339Z.ids.txt`

## Research Caution

The router snapshot is not the same thing as "all open-weight models worth benchmarking."

It is a served-model inventory. The next pass must verify:

- open-weight status
- license
- gated access
- exact Hugging Face model or artifact identity
- artifact availability, such as safetensors, GGUF, MLX, or Ollama
- whether a model is a base model, instruction model, coding model, vision-language model, guard model, or benchmark-specialized model
- whether ShellBench should benchmark a family once or multiple artifacts separately
