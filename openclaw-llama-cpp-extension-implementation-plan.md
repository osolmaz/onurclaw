# OpenClaw llama.cpp extension implementation plan

## Goal

Turn OpenClaw's bundled `extensions/llama-cpp` package into the single home for llama.cpp integrations. The package will keep the existing in-process `node-llama-cpp` inference and embedding paths and add the external `llama-server` provider now maintained in `onurclaw`.

The package will register two text providers:

```text
llama-cpp/<model-id>      in-process inference through node-llama-cpp
llama-server/<model-id>   external inference through llama-server HTTP
```

The provider IDs stay separate because they have different configuration, auth, discovery, and process ownership. Users install and enable one `llama-cpp` extension for both.

This plan is maintained in `osolmaz/onurclaw`. The implementation target is `openclaw/openclaw/extensions/llama-cpp`. No OpenClaw source change is part of writing this plan.

## Current state

OpenClaw `2026.7.2` contains a bundled `extensions/llama-cpp` package. It uses `node-llama-cpp` for local GGUF text inference and embeddings. Its plugin ID and text provider ID are both `llama-cpp`.

`onurclaw/extensions/llama-server` is a separate source plugin. It connects to an operator-managed llama.cpp server through the OpenAI-compatible completions API. It has passive single-model and router discovery, endpoint-scoped auth, dynamic model resolution, setup flows, bounded caches, tool-schema handling, structured-output mapping, and 57 focused tests.

The separate `llama-server` package was created during this work and has no compatibility requirement. Its code and tests can move directly into the bundled package. The standalone package should be removed after the bundled implementation passes the required checks.

## Success criteria

The work is complete when all of these statements are true:

- OpenClaw has one bundled plugin with manifest ID `llama-cpp`.
- That plugin registers the `llama-cpp` and `llama-server` text providers.
- It also keeps the existing `node-llama-cpp` embedding provider.
- Existing `llama-cpp/*` model references and configuration behave as before.
- Existing `llama-server/*` model references, endpoint configuration, auth profiles, and discovery behavior keep their current contract.
- Both providers can be configured and used at the same time.
- Loading the external server provider does not import or initialize `node-llama-cpp`.
- The plugin never downloads, launches, stops, or reconfigures `llama-server`.
- Server discovery remains passive, SSRF-guarded, bounded, and unable to load or wake router models.
- The standalone `onurclaw/extensions/llama-server` package is removed after its implementation and tests are absorbed.
- Bob can remove the separately installed plugin and continue using `llama-server/qwen3.6-35b-a3b` without changing the model reference or provider configuration.

## Package structure

Keep the root package small. Each runtime gets its own registration module and internal files.

```text
extensions/llama-cpp/
├── index.ts
├── index.test.ts
├── openclaw.plugin.json
├── package.json
├── README.md
└── src/
    ├── node/
    │   ├── register.ts
    │   ├── defaults.ts
    │   ├── embedding-provider.ts
    │   ├── inference-provider.ts
    │   ├── inference-provider.test.ts
    │   ├── runtime.ts
    │   ├── setup.ts
    │   └── setup.test.ts
    └── server/
        ├── register.ts
        ├── auth.ts
        ├── auth.test.ts
        ├── defaults.ts
        ├── discovery.ts
        ├── discovery.test.ts
        ├── endpoint.ts
        ├── endpoint.test.ts
        ├── models.ts
        ├── models.test.ts
        ├── provider.ts
        ├── provider.test.ts
        ├── setup.ts
        ├── setup.test.ts
        ├── stream.ts
        ├── stream.test.ts
        └── live.test.ts
```

Move the existing `llama-cpp` files into `src/node/` without changing their public behavior. Move the production code and focused tests from `onurclaw/extensions/llama-server` into `src/server/`. Do not create a shared helper layer unless both implementations need the same code with the same semantics.

`src/node/register.ts` should register in-process text inference and embeddings. `src/server/register.ts` should register the external provider and live model catalog. The root entrypoint should only call those two functions:

```ts
export default definePluginEntry({
  id: "llama-cpp",
  name: "llama.cpp",
  description: "Local GGUF inference, embeddings, and llama-server connections",
  register(api) {
    registerLlamaCppNode(api);
    registerLlamaServer(api);
  },
});
```

The exact description should follow OpenClaw documentation style. Registration order must not affect provider behavior.

## Public contracts

### Plugin and provider identities

Keep one plugin identity:

```text
plugin: llama-cpp
```

Keep two provider identities:

```text
provider: llama-cpp
provider: llama-server
```

Do not merge both runtimes behind `llama-cpp` with a `mode` field. A mode switch would prevent clear simultaneous configuration and would mix unrelated auth and model discovery rules.

Keep the existing configuration namespaces:

```json5
{
  models: {
    providers: {
      "llama-cpp": {
        // node-llama-cpp model paths and runtime parameters
      },
      "llama-server": {
        baseUrl: "http://127.0.0.1:8080/v1",
      },
    },
  },
}
```

Model IDs advertised by llama-server must still preserve `/`, `:`, aliases, and quantization suffixes after the first provider separator.

### Runtime ownership

The `node` implementation owns its in-process model objects and their cleanup. It may resolve or download a configured GGUF through the existing `node-llama-cpp` setup contract.

The `server` implementation owns only HTTP communication. Operators own the server binary, models, router behavior, launch flags, slots, GPU settings, and supervision. Discovery and setup must not call router load or unload routes.

### Authentication

Keep separate synthetic auth markers and profile IDs for the two providers. Combining the package must not make credentials reusable across providers or endpoints.

The server implementation must continue to follow these rules:

- An explicit authorization value may override configured authorization.
- Ambient credentials may not override explicit provider configuration.
- Credentials are reusable only when the canonical inference endpoint remains unchanged.
- Credentialed discovery does not share cache entries across auth scopes.
- Setup cleanup removes only `llama-server:default` and preserves unrelated auth profiles and ordering.

The in-process implementation keeps its existing non-secret local marker and does not read llama-server credentials.

## Package and manifest changes

Keep the package name `@openclaw/llama-cpp-provider`. Update its description so it covers both in-process and server use.

Keep `node-llama-cpp` optional and load it only from `src/node/runtime.ts`. No import reachable during root module evaluation or `registerLlamaServer` may load the native package. A missing or unsupported native package must leave `llama-server` usable.

Update `openclaw.plugin.json` to declare both providers. The combined manifest needs:

- `providers: ["llama-cpp", "llama-server"]`
- the current `llama-cpp` provider request family
- the `llama-server` OpenAI completions request family
- refreshable model discovery for `llama-server`
- pricing declarations for both local providers
- synthetic and non-secret auth declarations for both providers
- `LLAMA_SERVER_API_KEY` setup metadata
- both setup choices under one llama.cpp group
- the current embedding provider contract

Keep `enabledByDefault: true` and the existing lazy startup behavior. Manifest contract tests should prove that every registered provider, auth choice, and catalog declaration matches runtime registration.

## Setup experience

Present one setup group named `llama.cpp` with two choices:

- `In-process GGUF` configures `llama-cpp` through `node-llama-cpp`.
- `Existing llama-server` configures `llama-server` through a URL and optional API key.

Each choice keeps its own setup implementation. The shared group changes presentation only. Detection for one choice must not initialize or probe the other runtime.

In-process setup may keep the current default model and memory checks. Server setup must remain read-only during detection and should report the normalized endpoint, discovered models, auth requirement, and build metadata when available.

The model picker should label both sources clearly. It should never present a server model as an in-process model or imply that OpenClaw manages the server process.

## Server behavior to preserve

Move the current implementation without weakening its limits:

- Endpoint normalization returns the exact server origin and `/v1` inference base URL.
- Every discovery request uses OpenClaw's SSRF guard, bounded timeouts, bounded response readers, fatal UTF-8 decoding, and body cleanup.
- Router discovery probes no more than 200 models with concurrency 8 and one total deadline.
- Discovery and dynamic-model caches remain process-local and bounded to 100 entries each.
- Optional endpoint failures remain distinct from server failure, auth rejection, malformed responses, and loading states.
- Explicit model configuration overrides discovered metadata.
- Runtime context comes from active server metadata such as `/props` `n_ctx`.
- Model capabilities come from server metadata, with conservative defaults when fields are absent.
- Direct dynamic model resolution remains synchronous and free of network access after its prepare step.
- Tool schemas use `buildProviderToolCompatFamilyHooks("llamacpp-gbnf")`.
- JSON Schema responses retain the `response_format` envelope expected by llama-server.
- `thinking: "off"` maps to `chat_template_kwargs.enable_thinking: false` without forcing thinking on for other levels.

The server provider should continue to use OpenClaw's `openai-completions` transport. Keep its stream wrapper limited to request-shape differences that the shared transport does not handle.

## Shared code policy

Both providers use llama.cpp grammar and tool conventions, but their transports differ. Call the same public Plugin SDK helpers from each registration module where appropriate. Avoid an internal abstraction that tries to hide the difference between an in-process model object and an HTTP endpoint.

Extract a shared local helper only when all of these conditions hold:

- Both implementations need it now.
- Its inputs and outputs have the same meaning in both runtimes.
- Tests can state one contract that covers both callers.
- The helper does not mix process lifecycle, auth, or discovery state.

The public Plugin SDK remains the boundary between this extension and OpenClaw core. Do not add llama-server policy tables or special cases to core model loading.

## Documentation

Rewrite `extensions/llama-cpp/README.md` as the package guide. It should open by explaining that the extension supports in-process `node-llama-cpp` and external llama-server connections.

Keep separate user sections for:

- in-process text inference
- local embeddings
- single-model llama-server
- llama-server router mode
- server authentication and remote-network safety
- model references and stable aliases
- setup and troubleshooting

Keep the provider documentation path `/providers/llama-server` if OpenClaw already exposes that route. The extension package boundary does not require both providers to share one documentation page.

Document that an unauthenticated llama-server should bind to loopback. A remote endpoint needs authentication and protected networking.

## Implementation sequence

1. Add registration tests that capture all provider, catalog, embedding, auth, setup, and wrapper hooks from the existing `llama-cpp` and standalone `llama-server` plugins.
2. Move the current `llama-cpp` implementation into `src/node/` and add `registerLlamaCppNode(api)`. Prove that existing in-process and embedding tests pass before adding server code.
3. Move the `llama-server` implementation and tests into `src/server/`. Replace the standalone default export with `registerLlamaServer(api)`.
4. Make the root entrypoint register both implementations. Add one combined test that proves each provider is registered exactly once.
5. Merge the manifest declarations and package metadata. Run manifest and package-boundary tests before changing setup presentation.
6. Put both auth choices under one llama.cpp setup group while keeping separate choice and method IDs.
7. Merge the documentation and add examples where both providers are configured at once.
8. Run focused tests, Plugin SDK checks, changed checks, and the production build.
9. Run the opt-in live llama-server suite against an official pinned runtime. Verify discovery, text generation, cancellation, structured output, tools, concurrency, and restart recovery.
10. Test in-process inference and embeddings on a supported machine with the pinned `node-llama-cpp` dependency.
11. Remove `onurclaw/extensions/llama-server` after the OpenClaw implementation contains the same production code and test coverage.
12. Update Bob only after the unified plugin has passed a real request through each enabled provider path.

Each move should preserve behavior before the next concern is added. If a step exposes an OpenClaw Plugin SDK gap, stop and document the missing public API before proposing a core change.

## Verification

### Focused tests

The combined package must cover the existing in-process suite and all 57 current server tests. Add checks for:

- both providers registering exactly once
- the embedding provider remaining available
- server registration succeeding when `node-llama-cpp` cannot be imported
- node registration avoiding server discovery or auth access
- simultaneous provider configuration
- setup choice grouping without identity changes
- manifest and runtime registration agreement
- no cache, credential, or model leakage between providers

### Repository checks

Use the commands required by the current OpenClaw contribution guide. The expected minimum is:

```bash
node scripts/run-vitest.mjs extensions/llama-cpp
pnpm test:contracts:plugins
pnpm test:extensions:package-boundary
pnpm plugin-sdk:surface:check
pnpm check:changed
pnpm build
```

Run heavier checks through the repository's required Testbox or Crabbox path. Review the final diff against the target branch and resolve every P0 or P1 finding before handoff.

### Live evidence

Record separate evidence for the two runtimes.

For `node-llama-cpp`, record the package version, model ID and revision, hardware, requested backend, observed backend, and one real text request. Exercise embeddings when the machine supports the current embedding path.

For `llama-server`, record the official runtime owner, exact version or image digest, model ID and revision, launch command, requested backend, observed backend, context size, slot count, and speculative-decoding settings. Run the existing live suite without changing or controlling an operator's unrelated server.

Do not use benchmark results as a merge requirement. This change groups integrations and preserves behavior. Any later deployment choice between in-process and server inference needs its own representative benchmark and practical-significance review.

## Bob migration

Bob currently uses `llama-server/qwen3.6-35b-a3b` with configuration under `models.providers.llama-server`. Keep both unchanged.

After Bob's OpenClaw checkout includes the unified package:

1. Stop Bob's gateway cleanly while leaving the operator-managed llama-server alone.
2. Remove the separately installed `/home/bob/.openclaw/extensions/llama-server` package and its plugin entry.
3. Confirm the bundled `llama-cpp` plugin is enabled and registers both provider IDs.
4. Validate Bob's existing configuration without rewriting the endpoint, model reference, alias, auth profile, or model parameters.
5. Start the gateway and confirm it reports `llama-server/qwen3.6-35b-a3b` as the default model.
6. Send a fresh embedded request and a real Discord request through the Looper bot identity.
7. Confirm the response metadata names `llama-server` and shows no fallback.
8. Verify the external server and gateway health endpoints after the requests finish.

Preserve Bob's unrelated files, auth profiles, sessions, and channel configuration. Do not create a service as part of this migration unless Onur asks for one.

## Work outside this plan

This work does not add server lifecycle management, model downloading for server mode, router load or unload control, automatic backend selection, a fallback between providers, or benchmarks that choose one provider for users.

It also does not redesign OpenClaw's general OpenAI-compatible provider layer. Shared SDK changes need a concrete blocker in the combined implementation and focused tests proving the missing behavior.

## Stop conditions

Stop implementation and report the evidence when any of these conditions occurs:

- The bundled extension cannot register both provider IDs through public Plugin SDK APIs.
- Importing the combined package makes `node-llama-cpp` mandatory for server-only users.
- A server test requires a core provider-specific special case.
- Passive discovery would need a router load, wake, or unload request.
- Provider identity, auth scope, or model references cannot remain separate.
- The target OpenClaw contribution rules reject this package boundary.

A blocked report should name the failing check, the relevant files, attempted paths, and the smallest maintainer decision or Plugin SDK addition needed to continue.
