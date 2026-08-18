---
date: 2026-08-18
author: Onur Solmaz <2453968+osolmaz@users.noreply.github.com>
title: Add external llama-server support to the llama.cpp extension
tags: [openclaw, llama-cpp, llama-server, provider]
---

## Goal

OpenClaw must support a `llama-server` process that the user already runs. The
support belongs in the existing `llama-cpp` extension because that extension
already uses `llama-server` for its managed local runtime.

The extension will expose two provider IDs:

```text
llama-cpp/<model-id>      OpenClaw installs and manages llama-server
llama-server/<model-id>   the user supplies and manages llama-server
```

The plugin ID and package stay `llama-cpp` and `@openclaw/llama-cpp-provider`.
The implementation adds no second extension or package.

## Current state

OpenClaw `main` has one `llama-cpp` extension and one `llama-cpp` text provider.
The extension downloads a pinned official `llama-server`, downloads verified
GGUF files after consent, writes a router preset, starts the process through
`localService`, and uses it for chat and local embeddings.

OpenClaw can reach a user-managed `llama-server` through manual custom
OpenAI-compatible configuration. That route requires the user to enter model
IDs, context limits, tool compatibility, and other model data by hand. It does
not own llama.cpp model discovery, router state, chat-template capabilities, or
guided authentication.

The tested external implementation is in
[`extensions/llama-server/`](../extensions/llama-server/). It has 57 focused
tests and has passed its test, type-check, and build scripts against OpenClaw
`2026.7.2` and `2026.8.1`. Earlier live checks covered discovery, concurrent
generation, cancellation, and a tool call. A fresh live structured-output check
is still required.

This plan was prepared against:

- OpenClaw `9564b9fc006c38b3022c90fb5572e24dca30473e` from 2026-08-18.
- The managed llama.cpp build `b10357`, source revision
  [`689e227db485c6b33d061555e74034c93a867649`](https://github.com/ggml-org/llama.cpp/commit/689e227db485c6b33d061555e74034c93a867649).
- llama.cpp upstream revision
  [`27e345b574dd8c8838e2c06e47699a3135f16ec9`](https://github.com/ggml-org/llama.cpp/commit/27e345b574dd8c8838e2c06e47699a3135f16ec9).
- OpenClaw issue [#116765](https://github.com/openclaw/openclaw/issues/116765)
  and the closed proof-of-concept PR
  [#116808](https://github.com/openclaw/openclaw/pull/116808).

The implementation must re-read current `main` and current repository
instructions before making changes.

## User requirements

- Keep one llama.cpp extension.
- Keep the current managed llama.cpp behavior.
- Add first-class support for an existing external `llama-server`.
- Let managed and external servers work at the same time.
- Keep setup and model names clear to users.
- Make discovery passive. Discovery must not load, wake, unload, download,
  launch, stop, or reconfigure a model or server.
- Use OpenClaw's public Plugin SDK and shared transport.
- Preserve secrets, auth profiles, unrelated configuration, sessions, and
  running services.

## Design

### One plugin, two providers

The package will register two text providers and the existing embedding
provider:

| Plugin      | Provider       | Owner    | Purpose                     |
| ----------- | -------------- | -------- | --------------------------- |
| `llama-cpp` | `llama-cpp`    | OpenClaw | Managed chat and embeddings |
| `llama-cpp` | `llama-server` | User     | External chat               |

Provider IDs stay separate because they are configuration and runtime
identities. They have different authentication, setup, discovery, and process
ownership. Separate IDs also let one OpenClaw installation use both paths at
once.

The UI names will make ownership explicit:

- **llama.cpp (managed)**
- **llama-server (external)**

Both choices will appear in one setup group named **llama.cpp**.

### Managed provider boundary

The existing `llama-cpp` provider remains the managed path. It keeps:

- The current model references and configuration namespace.
- Verified llama.cpp and GGUF downloads.
- The managed router preset.
- `localService` lifecycle management.
- Local embedding support.
- Existing cache and index identities.
- Current model and embedding setup behavior.
- Current diagnostics and compatibility repair.

The external provider must never run managed setup code. Selecting or calling
`llama-server/*` must not import or call the installer, downloader, preset
writer, managed server preparation, or local embedding code.

### External provider boundary

The new `llama-server` provider owns only the connection from OpenClaw to a
configured HTTP endpoint. It owns:

- Endpoint parsing and normalization.
- Optional API-key and header authentication.
- Passive server and model discovery.
- Router status and model capability mapping.
- Dynamic model resolution.
- llama.cpp tool-schema compatibility.
- The small request changes that current llama.cpp requires and the shared
  transport does not provide.
- Guided and non-interactive setup.
- User-facing diagnostics for the configured endpoint.

The user owns:

- The server binary and version.
- Model files and aliases.
- Host, port, TLS, reverse proxy, and access controls.
- Context, slots, batching, GPU, speculative decoding, and chat-template flags.
- Router load and unload policy.
- Process supervision and restarts.

`models.providers.llama-server.localService` is outside this contract. The
provider must reject it with a clear message instead of starting a process.
Users who want OpenClaw to own the process must use `llama-cpp`.

### Source layout

Keep `index.ts` small and make registration boundaries visible:

```text
extensions/llama-cpp/
  index.ts
  src/
    managed-provider.ts
    managed-server.ts
    managed-provider-config.ts
    setup.ts
    embedding-provider.ts
    external-server/
      register.ts
      defaults.ts
      endpoint.ts
      auth.ts
      discovery.ts
      models.ts
      provider.ts
      setup.ts
      request.ts
```

`managed-provider.ts` will contain the current `llama-cpp` text-provider
registration. Existing managed implementation files should otherwise keep their
paths unless a move is required for a real dependency boundary. Avoid a broad
file shuffle.

`external-server/register.ts` will register `llama-server`. The remaining
external files will move from the tested standalone implementation. Do not copy
built `dist/` files into OpenClaw.

The root registration will have this shape:

```ts
register(api) {
  api.registerEmbeddingProvider(llamaCppEmbeddingProviderAdapter);
  registerManagedLlamaCppProvider(api);
  registerExternalLlamaServerProvider(api);
}
```

### Shared code

Reuse these current OpenClaw contracts:

- `openai-completions` for chat and streaming.
- `buildProviderToolCompatFamilyHooks("llamacpp-gbnf")` for tool schemas.
- Provider auth and SecretRef helpers.
- Guarded provider HTTP readers.
- SSRF policies that pin the configured origin.
- Unified model-catalog and dynamic-model hooks.
- Current self-hosted setup helpers where they preserve all llama.cpp-specific
  behavior.

Do not add a generic abstraction only to make the two registrations look
symmetrical. Endpoint discovery, router state, and external auth have no managed
equivalent. Managed process setup and embeddings have no external equivalent.

If both providers need the same llama-server request patch, add one named helper
such as `src/llama-server-request.ts` and test both callers. Keep the managed
lifecycle wrapper and the protocol request patch as separate functions so they
can be composed without mixing ownership.

## Provider contracts

### Provider and model identity

Keep these permanent namespaces:

```text
models.providers.llama-cpp
models.providers.llama-server

llama-cpp/<model-id>
llama-server/<model-id>
```

Model IDs from the server may contain `/`, `:`, dots, aliases, and quantization
suffixes. Split the OpenClaw model reference only at the first `/` and preserve
the remaining model ID exactly.

Do not add a `mode` field to `llama-cpp`. A mode switch would prevent
simultaneous use and would mix unrelated auth and lifecycle rules.

### Endpoint normalization

The default external endpoint is:

```text
http://127.0.0.1:8080/v1
```

Normalization must:

- Accept a host and port with or without an explicit scheme.
- Accept an origin or a base URL ending in `/v1`.
- Produce one exact origin for server endpoints and one `/v1` base URL for
  inference.
- Accept only HTTP and HTTPS.
- Reject usernames and passwords in the URL.
- Remove query strings and fragments.
- Preserve non-root path prefixes if llama-server is behind a reverse proxy.
- Never copy credentials into logs, errors, cache keys, or model metadata.

Add table-driven tests for IPv4, IPv6, DNS names, path prefixes, trailing
slashes, uppercase `/V1`, invalid schemes, URL credentials, queries, and
fragments.

### Authentication

Support these external-server cases:

- Unauthenticated loopback server.
- `LLAMA_SERVER_API_KEY`.
- An OpenClaw auth profile.
- SecretRef values in provider auth and configured headers.
- An explicit `Authorization` header for a reverse proxy.

Use a separate non-secret marker and auth-profile namespace for `llama-server`.
Never reuse `llama-cpp-local` or managed credentials.

Auth resolution must follow this order:

1. Explicit request or configured authorization header.
2. The selected `llama-server` auth profile.
3. The configured provider API key or SecretRef.
4. `LLAMA_SERVER_API_KEY`.
5. The non-secret local marker for an unauthenticated endpoint.

An explicit authorization header must prevent a second bearer header. Changing
the canonical endpoint must not silently reuse endpoint-scoped credentials.
Setup cleanup may remove only the profile it owns and must preserve profile
order and unrelated entries.

Tests must prove that no secret appears in snapshots, errors, logs, discovery
cache keys, or generated model rows.

### Network security

The endpoint is user supplied and can point at a private network. Treat it as
untrusted input even when it is local.

Discovery requests must:

- Use OpenClaw's guarded fetch path.
- Pin redirects and DNS resolution to the configured origin policy.
- Allow the explicitly configured loopback or private origin.
- Continue to block cloud metadata and link-local targets.
- Use bounded response readers.
- Cancel unread bodies and release dispatchers.
- Use one total deadline rather than a fresh unbounded timeout for every router
  model.

Setup-generated configuration may set the private-network opt-in after the user
confirms the endpoint. `normalizeConfig` must preserve an explicit deny and must
not silently broaden manually written request policy.

Inference must continue through OpenClaw's provider transport so timeout, TLS,
proxy, auth, SSRF, local-service, retry, error, and SSE rules stay centralized.
The external provider must not create a separate inference HTTP client.

Security tests must cover loopback, a private host, a public host, a metadata
host, redirects away from the configured origin, DNS rebinding, oversized JSON,
malformed UTF-8, slow responses, aborted requests, and unread-body cleanup.

### Passive discovery

Use the llama.cpp routes that the server already exposes:

1. `GET /health`
2. `GET /models`, with `GET /v1/models` only as a compatibility fallback
3. `GET /props` for a single model
4. `GET /props?model=<id>&autoload=false` in router mode

Discovery must not send `reload=1`. It must not call router `POST`, `PUT`, or
`DELETE` routes.

The managed b10357 server and current upstream both support `autoload=false`.
Keep a direct source-contract test or fixture that proves the query is present
for router property probes.

Apply these bounds:

- Default total deadline: 5 seconds unless the caller gives a smaller deadline.
- Maximum router models probed for properties: 200.
- Property-probe concurrency: 8.
- Successful unauthenticated discovery cache TTL: 30 seconds.
- Discovery cache maximum: 100 endpoint entries.
- Dynamic-model cache maximum: 100 runtime, profile, and endpoint scopes.
- Credentialed discovery: no shared cache.

A health or discovery failure must not block Gateway startup. Setup and explicit
catalog refresh should show the error. Normal startup should keep the configured
static rows and continue.

### Model mapping

Map server data conservatively:

- `id` and display name from the advertised model ID.
- Active context from `default_generation_settings.n_ctx`, then `n_ctx`.
- Training context only as a fallback when active context is unavailable.
- Maximum output tokens from advertised generation settings, capped by active
  context.
- Text input by default.
- Image input only when server properties report vision support.
- Tool support only when both `supports_tools` and `supports_tool_calls` are
  true.
- Typed message content only when the server reports it.
- Zero local usage cost.
- Router status, failure state, exit code, build information, and slot count as
  catalog capabilities or warnings.

Explicit user model entries win over discovered rows with the same ID. Discovery
may fill missing models but must not overwrite explicit limits, compatibility
flags, names, or parameters.

Automatic setup selection must prefer a healthy loaded model. It may then choose
sleeping or unloaded router models that can be loaded by the user's router
policy. It must never prefer a model marked failed when a healthy model exists.
Keep failed rows visible with a warning so the user can diagnose the server.

Do not infer tool, image, or context capabilities from the model name. Keep
discovered reasoning disabled unless the server or an explicit model entry
provides a reliable signal.

### Request behavior

Use the shared OpenAI completions transport.

The managed b10357 server accepts both OpenAI `json_schema` and llama.cpp
`json_object` response formats. An external b9204 server ignored the nested
OpenAI shape during live testing and returned fenced JSON instead of constrained
JSON. Map structured-output requests to llama.cpp's direct `json_object` schema
shape. This shape works on b9204, b10357, and current upstream.

Keep the narrow thinking-off patch if live tests still show that a reasoning
chat template continues thinking when OpenClaw selects `off`:

```json
{
  "chat_template_kwargs": {
    "enable_thinking": false
  }
}
```

Apply that patch only to `llama-server` requests and only when the selected
thinking level is `off`. Preserve existing `chat_template_kwargs` fields. Leave
enabled and unspecified thinking behavior to the user's model and server
configuration.

Do not add provider-specific repeated-tool-loop recovery. Loop handling belongs
in the shared agent or transport layer.

### Setup

The llama.cpp setup group will contain two choices:

| Choice                | Provider       | Result               |
| --------------------- | -------------- | -------------------- |
| Managed local server  | `llama-cpp`    | Prepare local models |
| Existing llama-server | `llama-server` | Connect to endpoint  |

External setup will:

1. Ask for the endpoint, defaulting to `http://127.0.0.1:8080/v1`.
2. Ask whether authentication is required.
3. Resolve the API key or configured header without displaying it.
4. Run bounded passive discovery.
5. Show endpoint, health, build, model IDs, status, context, slots, and tool
   support.
6. Let the user select a healthy advertised model.
7. Save `models.providers.llama-server` and `llama-server/<id>`.
8. Save only the auth profile and provider fields that this choice owns.

External setup must never call managed setup, install a binary, download a
model, write a preset, reserve a port, or create a service.

Non-interactive setup must require the endpoint and explicit risk acceptance
under the repository's current CLI contract. It may accept an optional model ID
and API-key option. It must fail with a useful message when the requested model
is absent or the endpoint cannot be verified.

### Runtime and startup

Keep plugin activation lazy. Loading the plugin may register both providers, but
it must not probe an external endpoint or prepare the managed runtime.

Only these actions may trigger external discovery:

- External guided setup.
- An explicit model catalog request.
- Dynamic resolution of a selected `llama-server/*` model.
- A future explicit diagnostics command.

A `llama-cpp/*` request must use the current managed lifecycle wrapper. A
`llama-server/*` request must use the configured endpoint directly and must
never acquire a managed local-service lease.

### Manifest and package

Update the existing `extensions/llama-cpp/openclaw.plugin.json` in place:

- Keep plugin ID `llama-cpp`.
- Set `providers` to `['llama-cpp', 'llama-server']`.
- Declare request families for both provider IDs.
- Declare refreshable discovery for `llama-server`.
- Declare local zero-cost pricing for both.
- Keep the managed synthetic marker and add the external marker.
- Add `LLAMA_SERVER_API_KEY` setup metadata.
- Add both auth choices under one llama.cpp group.
- Keep the local embedding contract unchanged.
- Auto-enable the plugin when either provider is configured if current manifest
  rules require it.

Update the existing package description. Do not add a package, dependency,
workspace importer, or second lockfile entry. The expected `pnpm-lock.yaml`
change is none.

### Documentation

Update `docs/plugins/llama-cpp.md` so it starts with the two supported ownership
modes. Keep managed installation, downloads, embeddings, and diagnostics on that
page.

Add or update `docs/providers/llama-server.md` for the external provider.
Include:

- The ownership difference.
- Quick start with an official `llama-server` and stable `--alias`.
- Guided and non-interactive setup.
- Authentication and reverse proxies.
- Single-model and router discovery.
- Context and capability mapping.
- The rule that OpenClaw never manages the external process.
- Troubleshooting for health, auth, tools, structured output, and router state.

Generate plugin inventory and reference pages with repository scripts. Do not
edit generated plugin reference files by hand.

## Implementation sequence

### Baseline

1. Create a new branch and worktree from current OpenClaw `main`.
2. Read the current root, extension, and docs instructions.
3. Record the current managed provider registration, setup, chat, embedding,
   doctor, and package tests.
4. Run the focused managed suite before edits.
5. Confirm the standalone external suite still passes against the target
   checkout.

### Registration split

1. Move only the current managed text-provider registration from `index.ts` to
   `src/managed-provider.ts`.
2. Keep embedding registration at the plugin root.
3. Prove that the extraction causes no behavior, manifest, or generated-output
   change.
4. Commit this working slice before adding the external provider.

### External source move

1. Move the standalone source and tests into `src/external-server/`.
2. Replace the standalone default plugin export with
   `registerExternalLlamaServerProvider(api)`.
3. Remove standalone package, build, and `dist/` assumptions.
4. Update imports to current public Plugin SDK paths.
5. Reuse current shared provider helpers where they preserve the
   llama.cpp-specific contract.
6. Re-derive the request patch from live external-server behavior, b10357, and
   current upstream. Keep the direct `json_object` mapping required by b9204 and
   accepted by newer builds.
7. Commit the provider with focused unit tests passing.

### Manifest and setup

1. Add the second provider to the existing manifest.
2. Group managed and external setup choices under llama.cpp.
3. Add external auth, endpoint, discovery, model selection, and non-interactive
   setup.
4. Add contract tests that compare manifest declarations with runtime
   registration.
5. Commit after setup and contract tests pass.

### Integration hardening

1. Add simultaneous-provider tests.
2. Add lifecycle isolation tests.
3. Add auth-scope and cache-isolation tests.
4. Add SSRF, body-bound, timeout, cancellation, and redirect tests.
5. Add router failure-selection and warning tests.
6. Add current-upstream response-format and thinking-off tests.
7. Run a real external-server request before changing documentation claims.
8. Commit each coherent, passing hardening slice.

### Documentation and cleanup

1. Update the user docs and generated plugin inventory.
2. Run docs checks.
3. Review the final diff against current `main`.
4. Run the full required repository checks.
5. Open a PR linked to issue #116765.
6. After the OpenClaw implementation merges, remove the standalone provider from
   `onurclaw` and keep this plan as the historical design record.

## Verification

### Focused tests

The combined package must include the current managed suite and all useful
standalone external tests. It must prove:

- The plugin registers exactly two text providers and one embedding provider.
- Managed setup, chat, embeddings, downloads, and lifecycle behavior stay
  unchanged.
- External registration and setup do not import or call managed runtime code.
- Both providers can be configured and called in one process.
- Provider, auth, model, cache, and endpoint identities do not leak across
  paths.
- Explicit external models override discovered rows.
- Router discovery never autoloads or reloads a model.
- Failed router models are not preferred automatically.
- External unavailability does not block startup.
- Dynamic model caches are bounded and scoped.
- SecretRef, API-key, custom-header, and unauthenticated paths work.
- SSRF guards, deadlines, body limits, cancellation, and cleanup work.
- Tool schemas use the shared llama.cpp profile.
- Structured output uses the current upstream request shape.
- Thinking off sends the tested llama.cpp template option only when required.
- `llama-server.localService` is rejected.
- Manifest and runtime registration agree.

### Repository checks

Use the commands required by current OpenClaw instructions. The expected minimum
is:

```bash
node scripts/run-vitest.mjs extensions/llama-cpp
pnpm test:contracts:plugins
pnpm test:extensions:package-boundary
pnpm plugin-sdk:surface:check
pnpm plugins:inventory:gen
pnpm docs:map:gen
pnpm check:docs
pnpm check:changed
pnpm build
```

Run independent Vitest commands sequentially in one worktree. Use the
repository's required Testbox or Crabbox path for heavy checks. Run a fresh
self-review against current `main` and resolve every P0 or P1 finding before
handoff.

### Live external-server proof

Use an existing canonical runtime or an official llama.cpp release. Do not build
from source for this test without separate approval.

Record:

- Full llama.cpp owner, version, build number, and immutable revision.
- Model repository, model revision, GGUF filename, and model alias.
- Runtime command with secrets removed.
- Requested and observed backend.
- Context size, slot count, batching, and speculative-decoding settings.
- OpenClaw commit and plugin package version.

Run these checks:

1. Passive health and single-model discovery.
2. Router discovery with loaded, sleeping, unloaded, and failed rows when
   available.
3. One normal streamed text response.
4. Two concurrent responses.
5. Cancellation during generation.
6. One tool-call round trip.
7. One JSON-schema structured response.
8. Thinking off on a template that otherwise reasons.
9. Endpoint authentication.
10. Gateway restart while the external server remains untouched.

Verify from logs and response metadata that the selected provider is
`llama-server` and that no fallback or managed local-service start occurred.

### Managed regression proof

Use the existing pinned managed runtime and current default model. Prove:

1. Guided managed setup still prepares the verified runtime.
2. A `llama-cpp/*` chat request starts and reuses the managed server.
3. Local embeddings still use the managed router.
4. Idle shutdown still occurs.
5. External configuration does not change managed paths, ports, presets, caches,
   or auth.

Do not redownload large artifacts when verified current artifacts can be reused.

## Acceptance criteria

The change is ready when:

- One installed `llama-cpp` extension provides both `llama-cpp/*` and
  `llama-server/*`.
- Existing managed users need no configuration change.
- A user can configure an existing server without writing model metadata by
  hand.
- Managed and external providers work at the same time.
- External requests never start, stop, install, download, or reconfigure a
  server.
- Discovery is passive, bounded, cancellable, and safe for private endpoints.
- Auth and cache state stay scoped to the external endpoint and profile.
- Tool calls and structured output pass against the official server.
- Managed chat and embeddings pass their regression checks.
- Manifest, generated docs, type checks, tests, build, and required CI are
  green.
- The PR has current maintainer review for the new first-party provider surface.

## Non-goals

This work does not add:

- External-server embeddings or reranking.
- Automatic server installation for `llama-server`.
- Router load, unload, sleep, wake, download, or delete controls.
- Automatic model or backend selection.
- Automatic fallback between managed and external providers.
- Provider-specific tool-loop recovery.
- New GPU, quantization, batching, or speculative-decoding defaults.
- A redesign of every self-hosted OpenAI-compatible provider.
- Benchmarks that choose managed or external mode for the user.

## Stop conditions

Stop and report evidence if:

- Current public Plugin SDK APIs cannot register both providers in one plugin.
- External registration causes managed installer or embedding code to load or
  run.
- Safe inference to an explicitly configured private origin requires weakening
  shared SSRF policy.
- Passive router discovery requires loading, waking, unloading, or reloading a
  model.
- Provider identity, auth profile, model reference, or cache scope cannot remain
  separate.
- Structured output needs a provider-specific format rewrite that conflicts with
  the managed b10357 contract.
- The current contribution rules reject the combined package boundary.

A blocked report must name the failing test or contract, files checked, exact
source revisions, attempted alternatives, and the smallest Plugin SDK or
maintainer decision needed to continue.
