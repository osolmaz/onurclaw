---
title: Provider acceptance plan
author: Onur Solmaz <2453968+osolmaz@users.noreply.github.com>
date: 2026-08-18
updated: 2026-08-21
---

# Provider acceptance plan

Some OpenClaw transports accept the shared `onResponse` option but do not call it after a successful provider request. This issue was found while reviewing [openclaw/openclaw#116551](https://github.com/openclaw/openclaw/pull/116551). It has no separate user report.

OpenClaw needs truthful acceptance data for built-in model diagnostics. It does not yet have evidence that third-party provider plugins need a new lifecycle API. This plan keeps the signal private until that need exists.

## Current evidence

On OpenClaw `main` at `7c65bbcee31bd31fa5b46c84f3a3f54c2cc522fb`, `StreamOptions.onResponse` means that a transport received a real HTTP response before consuming its body.

OpenAI Completions follows that contract. Several other built-in paths do not:

- Ollama and the bundled Google SSE transport receive real HTTP responses without calling `onResponse`.
- Mistral SDK 2.5.0 exposes each real response through its public `HTTPClient` response hook, but OpenClaw does not use it.
- Anthropic Vertex and Bedrock Mantle rebuild stream options without forwarding `onResponse`.
- Google SDK and OpenAI Responses WebSocket paths can observe provider acceptance but do not expose complete HTTP metadata.

The embedded agent runner uses response data for model-call diagnostics. A successful opaque SDK or WebSocket stream can therefore look the same as a request that failed before provider acceptance.

A deterministic reproduction confirmed the missing response calls in Mistral and the two wrappers. A live Ollama 0.24.0 run also completed successfully without calling `onResponse`.

## Requirements

The repair must satisfy these rules:

- Keep the supported Plugin SDK unchanged.
- Keep `onResponse` for real HTTP responses and never fabricate status or headers.
- Record built-in provider acceptance at the earliest reliable transport boundary.
- Keep the acceptance observer private to OpenClaw.
- Preserve the private observer when built-in wrappers copy stream options.
- Do not let diagnostics add global state or infer acceptance from tokens.
- A setup or connection failure before acceptance must record no acceptance.
- Existing `onResponse` consumers must keep their current behavior.

## Design

### Private acceptance observer

Carry one private, symbol-keyed observer on the per-call provider options object. This follows the existing private provider-context handoff pattern.

The observer receives one internal discriminated value:

```ts
type ProviderAcceptance =
  | {
      kind: "http_response";
      status: number;
      headers: Record<string, string>;
    }
  | {
      kind: "provider_stream_opened";
    };
```

The embedded runner attaches the observer when it creates the model-call options. Built-in transports call an internal helper after a successful HTTP response or after an opaque SDK or WebSocket stream opens. Object spreads preserve the symbol. Wrappers that rebuild options use one internal copy helper.

The symbol, type, and helpers stay in `@openclaw/ai/transports`. Bundled plugins receive only the needed helpers through the existing private-local `openclaw/plugin-sdk/provider-transport-runtime` seam. OpenClaw does not add a supported Plugin SDK subpath or a public `StreamOptions` field.

### HTTP compatibility

Real HTTP paths continue to call `onResponse` with observed status and headers. The shared internal helper also reports accepted 2xx responses to diagnostics. Rejected responses call only `onResponse`.

If an awaited `onResponse` callback fails, the transport cancels the unread body or stream before returning the callback error.

### Opaque streams

Google SDK and OpenAI Responses WebSocket paths report `provider_stream_opened` through the private observer. They do not call `onResponse` and do not invent HTTP metadata.

The observer is internal diagnostics plumbing. A failure in that plumbing must close an unread stream and must not leave provider resources open.

## Scope

Change the built-in Anthropic, Bedrock, Google, Mistral, Ollama, OpenAI HTTP, OpenAI WebSocket, ChatGPT/Codex, and wrapper paths already covered by [openclaw/openclaw#126028](https://github.com/openclaw/openclaw/pull/126028).

Remove these unshipped public additions from the pull request:

- `StreamOptions.onProviderAccepted`
- the public `ProviderAcceptance` export
- `openclaw/plugin-sdk/provider-lifecycle`
- public provider-plugin documentation for the lifecycle helpers

## Non-goals

This work does not add a third-party plugin lifecycle API. It does not change prompt admission, compaction, provider payloads, tool execution, retry policy, configuration, persistent data, or Gateway protocol.

A future external plugin requirement can promote the proven private contract through a separate maintainer decision.

## Acceptance criteria

The work is complete when all of these statements are true:

- The supported Plugin SDK surface has no provider-acceptance additions.
- Every affected built-in successful transport records private acceptance once.
- HTTP transports report only real status and headers.
- Opaque SDK and WebSocket transports report no fake HTTP metadata.
- Pre-acceptance failures record no acceptance.
- Built-in wrappers preserve the private observer and existing `onResponse` callback.
- Existing `onResponse` behavior remains unchanged.
- Diagnostics distinguish accepted opaque streams from requests that never reached the provider.
- Focused tests, changed checks, build, Plugin SDK checks, Pi review, and exact-head CI pass.

## Verification

Use deterministic mocked provider clients. Do not use live credentials or external network calls.

Run the focused provider and diagnostic tests, then run:

```bash
node scripts/check-changed.mjs --base upstream/main --timed
pnpm build
pnpm plugin-sdk:surface:check
node scripts/check-plugin-sdk-subpath-exports.mts
pi-reviewer --base upstream/main
```

Stop before merge. The pull request must remain open for maintainer review.
