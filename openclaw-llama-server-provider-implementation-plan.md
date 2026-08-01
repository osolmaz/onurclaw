# OpenClaw llama-server provider implementation plan

> This standalone-package plan is superseded by the [llama.cpp extension implementation plan](openclaw-llama-cpp-extension-implementation-plan.md). This file records the design and verification contract of the implementation being absorbed.

## Goal

Maintain an independent `llama-server` provider in this repository. The provider connects OpenClaw to an existing llama.cpp `llama-server` process through its OpenAI-compatible HTTP API.

The result works for a single loaded model and for llama-server router mode. It discovers models and runtime capabilities without making operators maintain duplicate model metadata in `openclaw.json`.

The implementation lives at `extensions/llama-server/` in `osolmaz/onurclaw` and targets the OpenClaw `2026.7.2` Plugin SDK. It is not an OpenClaw core or bundled-plugin change.

## Design decision

Keep the provider as an independently installed source plugin under `onurclaw/extensions/llama-server`. Keep OpenClaw's bundled `extensions/llama-cpp` plugin focused on in-process `node-llama-cpp` inference.

The provider names describe different runtime boundaries:

```text
llama-cpp/<model>      in-process node-llama-cpp
llama-server/<model>   external llama-server over HTTP
```

The plugin uses OpenClaw's existing `openai-completions` transport. It owns llama-server discovery, capability mapping, setup, auth, and tool-schema compatibility without changing OpenClaw core.

The implementation connects to a server that the operator already runs. It does not download, build, update, or implicitly start llama-server. Operators who want OpenClaw to start a known local binary can use the existing `models.providers.<id>.localService` contract with an explicit absolute command.

## Current status

The implementation is now maintained in this repository. The local suite has 55 passing tests plus a clean standalone type check against the OpenClaw `2026.7.2` Plugin SDK. Earlier live checks covered passive discovery, concurrent generation, cancellation, and a tool-call round trip. The mapped structured-output path still needs another live run when a guarded llama-server is ready.

## Success criteria

The implementation is complete when all of these statements are true:

- `llama-server/<model-id>` resolves and streams through the existing OpenAI completions transport.
- Setup can connect to an unauthenticated loopback server or a server protected by an API key or SecretRef.
- OpenClaw discovers model IDs from both single-model and router-mode servers.
- Discovery is passive. Listing models never loads, wakes, or unloads one.
- Runtime context and chat-template capabilities come from server metadata when the server reports them.
- Tool schemas use OpenClaw's `llamacpp-gbnf` compatibility family.
- A missing or stopped server does not block gateway startup. Requests and setup return a specific, redacted diagnostic.
- Existing custom OpenAI-compatible providers and the in-process `llama-cpp` plugin keep their current behavior.
- Tests cover streaming, cancellation, tool calls, structured output, router discovery, and server restart recovery.

No performance claim is part of this change. A later benchmark can compare in-process inference with llama-server when an operational decision depends on the result.

## Public contract

### Provider identity

Use `llama-server` as the provider and plugin ID. Do not add aliases for arbitrary existing provider IDs such as `local-qwen`; OpenClaw cannot prove that those endpoints are llama-server instances.

Model references preserve the server's advertised ID exactly after the first provider separator. IDs containing `/`, `:`, or quantization suffixes remain valid:

```text
llama-server/ggml-org/gemma-3-4b-it-GGUF:Q4_K_M
```

For a single-model server, documentation should recommend a stable `llama-server --alias` value instead of a model path.

### Configuration

The normal configuration should contain endpoint and auth information only:

```json5
{
  models: {
    providers: {
      "llama-server": {
        baseUrl: "http://127.0.0.1:8080/v1",
      },
    },
  },
  agents: {
    defaults: {
      model: {
        primary: "llama-server/my-model",
      },
    },
  },
}
```

An explicit `models` array remains available for operator overrides or a server that cannot expose discovery. Explicit values take precedence over discovered values. The provider should not introduce new provider-specific configuration keys unless the existing provider config and `localService` fields cannot express a required behavior.

Authentication should use `LLAMA_SERVER_API_KEY` and normal SecretRef support when a key is required. An unauthenticated local server should use a declared non-secret auth marker internally, without writing a fake API key into user configuration.

### Process ownership

The plugin owns the HTTP connection. The operator owns the llama-server executable, model files, launch flags, slots, batching, GPU settings, router policy, and process supervisor.

The plugin must not invoke router load or unload endpoints during setup, discovery, or normal model resolution. A request may cause loading only when the operator has enabled llama-server's own router autoload behavior.

## Implementation

### Plugin package

Add these initial files:

```text
extensions/llama-server/
├── index.ts
├── openclaw.plugin.json
├── package.json
├── README.md
└── src/
    ├── auth.ts
    ├── defaults.ts
    ├── discovery.ts
    ├── endpoint.ts
    ├── models.ts
    ├── setup.ts
    └── *.test.ts
```

Keep production imports inside `openclaw/plugin-sdk/*` and the plugin package. Add a small `api.ts` or `runtime-api.ts` barrel only if a real cross-boundary caller needs one.

The manifest declares the provider, refreshable model discovery, non-secret local auth, self-hosted pricing, setup metadata, and OpenAI completions streaming usage. Package metadata declares the compatible OpenClaw Plugin SDK and gateway versions.

### Endpoint handling

Create one endpoint resolver that accepts either an origin or a `/v1` base URL and returns both values:

```text
origin:         http://127.0.0.1:8080
openaiBaseUrl:  http://127.0.0.1:8080/v1
```

All inference uses `openaiBaseUrl`. Health, router, and property requests use `origin`. Normalize trailing slashes once and reject URLs with credentials embedded in them.

Every discovery request must use `fetchWithSsrFGuard`, a bounded timeout, bounded JSON readers, fatal UTF-8 decoding, and response-body cleanup. Trust only the exact configured origin under the existing provider SSRF policy. Do not add a broad private-network exception.

### Discovery

Implement one discovery service shared by setup, runtime model resolution, and catalog display. It should probe in this order:

1. Check `/health` to distinguish an unreachable server from a loading server.
2. Read `/v1/models` for OpenAI-compatible model IDs.
3. Read `/models` when the response identifies router mode or contains router model state.
4. Read `/props` for the active model when available.

Do not treat one optional endpoint returning `404` as a failed server. Authentication failures, malformed responses, loading states, and transport failures should remain distinct outcomes.

Use closed result types for server reachability and model state. Keep successful discovery in a short process-local cache keyed by normalized origin. Do not cache auth failures or malformed responses. An unavailable server should leave explicit configured model rows intact. It must not replace the catalog with an empty provider.

Router discovery must preserve loaded, loading, sleeping, and unavailable state when llama-server reports it. These states belong in catalog diagnostics; model discovery must not change them.

### Catalog and model resolution

Register the modern control-plane catalog through `api.registerModelCatalogProvider` with kind `text` and a live catalog callback. The provider also needs the legacy `registerProvider().catalog` hook because that hook remains the text runtime source until OpenClaw's unified loader replaces it. Both hooks must map the same discovery result through one implementation.

Add `prepareDynamicModel` and `resolveDynamicModel` so a direct `llama-server/<id>` reference can refresh discovery asynchronously and then resolve from the same cache. Keep synchronous resolution deterministic and free of network access.

Use `normalizeConfig` to set `api: "openai-completions"`, normalize the base URL, merge explicit model overrides, and apply safe self-hosted defaults. Use `resolveSyntheticAuth` for an unauthenticated local endpoint. Avoid a custom stream implementation.

Metadata precedence is:

1. Explicit model configuration
2. Live llama-server metadata
3. OpenClaw self-hosted defaults

The runtime context window should come from the active server context, such as `/props` `n_ctx`. The GGUF training context does not describe the server's current allocation. The output token limit remains an OpenClaw default or explicit override unless llama-server advertises a separate output limit.

### Capabilities and tool schemas

Map capabilities from documented server fields. Do not infer vision, tools, or reasoning from a model name.

Use `/props` chat-template capabilities when available:

- `supports_tools`
- `supports_tool_calls`
- `supports_parallel_tool_calls`
- `supports_system_role`
- `supports_string_content`
- `supports_typed_content`
- `supports_preserve_reasoning`

Unknown capabilities default to the conservative setting. Explicit operator configuration can override discovered compatibility values.

Register `buildProviderToolCompatFamilyHooks("llamacpp-gbnf")` from `openclaw/plugin-sdk/provider-tools`. This keeps llama.cpp JSON-schema projection at the provider boundary and covers the parser restrictions already handled for the in-process llama.cpp, LM Studio, and Ollama paths.

Structured output and multimodal support should be enabled only after a live request proves the intended llama-server endpoint accepts the payload produced by OpenClaw. Capability discovery alone is insufficient proof for these paths.

### Setup and diagnostics

Add interactive, non-interactive, and app-guided setup following the LM Studio provider pattern. Detection must be read-only. It should report the normalized endpoint, discovered model count, server build information when available, and whether authentication is required.

Setup should fail with clear messages for these cases:

- Endpoint unreachable
- Server still loading
- Authentication required or rejected
- No text-generation model available
- Requested model absent
- Malformed or unsupported discovery response

Keep secrets out of logs and cache keys. Server diagnostics may include the normalized origin, HTTP status, model ID, router state, and llama.cpp build metadata.

The plugin should classify known llama-server errors such as context overflow, slot exhaustion, schema rejection, and model loading through existing generic error hooks where possible. Add a thin `wrapStreamFn` only if the generic transport cannot preserve a typed error. The wrapper must decorate the shared transport and keep its request and stream handling.

### Documentation

Keep the user guide at `extensions/llama-server/PROVIDER.md`. Document single-model and router examples, stable aliases, authentication, loopback deployment, optional `localService`, tool-template requirements, and troubleshooting.

Keep development and installation instructions in `extensions/llama-server/README.md`.

The docs should state that a remote endpoint needs authentication and protected networking. An unauthenticated server should bind to loopback.

## Verification

### Unit and contract tests

Use fixture HTTP responses to cover:

- Origin and `/v1` URL normalization
- Single-model `/v1/models` discovery
- Router `/models` discovery without autoload
- `/props` context and chat-template capability mapping
- Explicit-over-discovered metadata precedence
- Optional auth and rejected auth
- Bounded malformed and oversized responses
- Model IDs containing `/` and `:`
- Dynamic model refresh and cache invalidation
- Gateway startup while the server is unavailable
- Tool-schema projection through `llamacpp-gbnf`

Add provider registration and manifest contract coverage. Prove that the plugin uses public SDK imports and does not add a llama-server ID or policy table to core.

### Live integration proof

Create an opt-in live test that uses an official pinned llama.cpp release binary and a small, redistributable GGUF fixture. Do not build llama.cpp from source as part of the test. Record the exact release, server build metadata, model revision, launch command, requested backend, and observed backend in the evidence.

The live test should exercise:

- Health and catalog discovery
- A streamed text completion with usage
- Cancellation during generation
- One tool call and its result turn
- One JSON-schema response
- Two concurrent requests when two slots are configured
- Server termination followed by restart and a successful new request
- Router discovery where an unloaded model remains unloaded

The test must use an isolated state directory and free ports. It must not touch an operator's gateway, config, service, model cache, or running llama-server process.

### Repository checks

At minimum, run the focused extension tests, plugin contract tests, formatting, changed checks, and a production build because the change adds a bundled package and lazy setup imports. Expected commands include:

```bash
node scripts/run-vitest.mjs extensions/llama-server
pnpm test:contracts:plugins
pnpm test:extensions:package-boundary
pnpm plugin-sdk:surface:check
pnpm check:changed
pnpm build
```

Use the repository's required Testbox or Crabbox path for the heavy checks. Complete a fresh autoreview before landing code. Open a feature issue before implementation, link the implementation PR, and obtain owner review for the new provider and setup surface.

## Bob migration

Bob can keep the current custom OpenAI-compatible configuration while the plugin is being built. Rename the provider to `llama-server` only when the server advertises a stable alias and the matching OpenClaw model reference has been tested.

After the plugin is available:

1. Start the existing official llama-server runtime with a stable `--alias` and the intended context and tool-template flags.
2. Enable or configure the `llama-server` provider at its current endpoint.
3. Confirm discovery reports the expected model ID, runtime context, and tool capability.
4. Run text, tool-calling, cancellation, and restart-recovery smoke tests.
5. Change the default model from `local-qwen/...` to `llama-server/<alias>`.
6. Remove the duplicate explicit model metadata after live discovery has proven equivalent values.

Do not automatically migrate arbitrary `local-*` providers. Bob's configuration can be changed directly because its endpoint and model ownership are known.

## Deferred work

Keep these items out of the first provider change:

- Downloading or compiling llama-server
- Choosing GPU, quantization, batching, or speculative-decoding settings
- Automatic router load and unload control
- A provider-specific process supervisor
- Embeddings and reranking
- Benchmark-based preference between `llama-cpp` and `llama-server`
- A generic redesign of all OpenAI-compatible provider helpers

Embeddings can be added later through the same plugin if a real llama-server embedding deployment proves the lifecycle and model-selection contract. Shared provider helpers should be extracted only after the new provider exposes duplicated behavior in at least two maintained plugins.
