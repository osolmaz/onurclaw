---
title: Provider acceptance hooks plan
author: Onur Solmaz <2453968+osolmaz@users.noreply.github.com>
date: 2026-08-18
---

# Provider acceptance hooks plan

Some OpenClaw transports accept the shared `onResponse` option but never call it after a successful provider request. This issue was found while reviewing [openclaw/openclaw#116551](https://github.com/openclaw/openclaw/pull/116551). It has no separate user report.

This plan defines a truthful provider-acceptance signal. It supports the request lifecycle in the [provider request egress plan](2026-08-05-provider-request-egress-design-plan.md) without copying the broad hook patches from #116551.

## Current evidence

On OpenClaw `main` at `7c65bbcee31bd31fa5b46c84f3a3f54c2cc522fb`, `StreamOptions` documents `onResponse` as a callback that runs after an HTTP response arrives and before its body stream is consumed.

OpenAI Completions follows that contract. It obtains the real `Response`, records its status and headers, and invokes the hook before stream events are consumed.

The following built-in paths do not provide equivalent behavior:

- Google and Mistral open successful SDK streams without calling `onResponse`.
- The bundled Google transport opens a successful SSE stream without calling it.
- Anthropic Vertex and Bedrock Mantle do not forward `onResponse` to their underlying transport.
- Ollama receives a real HTTP `Response` but does not call the hook.

The embedded agent runner installs `onResponse` for model-call diagnostics. Missing calls leave the response status unknown even after generation starts. Other consumers also cannot tell whether request setup failed or the provider accepted the request.

A deterministic runtime reproduction on the same revision confirmed the issue. A direct Mistral request made one mocked fetch, completed with `stop`, and returned `mistral-ok`, while `onResponse` ran zero times. Anthropic Vertex and Bedrock Mantle both completed with `stop`, but neither forwarded the callback. The OpenAI Completions control made one mocked fetch, called `onResponse` once with the real status and headers, and invoked it before the first stream event. No external network or credentials were used.

Further inspection found two related SDK-backed paths. The canonical Anthropic Messages transport and the OpenAI Responses WebSocket transport can observe an accepted provider stream but do not own HTTP metadata. The bundled Google SSE transport and Ollama own real HTTP responses and can report their exact metadata. Bedrock exposes real status and request metadata through its SDK response.

## Implementation status

[openclaw/openclaw#125807](https://github.com/openclaw/openclaw/pull/125807) implements this plan. It remains open and unmerged. The implementation also prevents rejected ChatGPT Responses attempts from being marked accepted and cancels unread HTTP response bodies when an acceptance callback fails.

## Problem

A manual patch in each provider is easy to miss when a transport is added or rewritten. It also encourages fake values such as status `200` and empty headers when an SDK hides the HTTP response. Fake metadata makes diagnostics look complete when the transport did not observe those facts.

Provider acceptance and HTTP response metadata are related but different facts. Some transports own a raw HTTP response. Other transports only know that an SDK returned an open provider stream. OpenClaw needs one contract that represents both cases honestly.

## Requirements

The fix must satisfy these rules:

- Every built-in text transport reports provider acceptance at the earliest reliable point.
- A raw HTTP transport reports the real status and headers.
- An SDK-backed transport says that HTTP metadata is unavailable.
- No transport invents a status, headers, retries, or request identifier.
- A setup or connection failure before acceptance emits no acceptance event.
- Wrappers forward the acceptance contract without provider-specific glue.
- Retry behavior reports only attempts that the transport can observe.
- Existing `onResponse` consumers keep their current behavior for real HTTP responses.

## Design

### Provider acceptance receipt

Add one typed receipt for the fact that a provider accepted or opened a request:

```ts
type ProviderAcceptance =
  | {
      kind: "http_response";
      status: number;
      headers: Record<string, string>;
    }
  | {
      kind: "provider_stream_opened";
      httpMetadata: "unavailable";
    };
```

Expose it through a request-lifecycle callback. The caller keeps request correlation through the existing `requestId` option, so the receipt does not copy or invent an identifier. `provider_accepted` is the lifecycle stage; the receipt is its evidence.

Keep `onResponse` as a compatibility callback for transports that hold a real HTTP response. Do not call it with synthetic metadata. Internal diagnostics move to the acceptance receipt and record HTTP status only for the `http_response` case.

### Shared transport boundary

Put acceptance dispatch in one shared transport helper. A transport calls the helper after the HTTP response passes status checks or after an SDK returns an open stream, and before the first model event is exposed.

The helper emits the canonical acceptance receipt and then adapts a real HTTP receipt to the existing `onResponse` callback. Wrappers pass the lifecycle callback through unchanged. They do not reconstruct receipts.

An observed retry can emit one receipt per accepted attempt. An SDK that hides its internal retries emits only the final stream-opened receipt that OpenClaw can observe.

### Provider conversion

Convert the affected providers in small groups:

1. Fix Ollama, Bedrock, and the bundled Google SSE transport as cases with real status and headers.
2. Fix Google, Mistral, canonical Anthropic Messages, and OpenAI Responses WebSocket as SDK-backed cases with unavailable HTTP metadata.
3. Fix Anthropic Vertex and Bedrock Mantle forwarding.
4. Move model-call diagnostics to the canonical receipt.

Each conversion removes its local omission. No provider can advertise the new lifecycle capability and then skip the shared helper.

## Non-goals

This work does not change prompt admission, compaction, provider payloads, tool execution, or retry policy. It does not fabricate HTTP metadata for SDK-backed providers. It does not copy the provider-prompt state system from #116551.

## Acceptance criteria

The work is complete when all of these statements are true:

- The current-main failure is reproduced before implementation, with Mistral and two forwarding wrappers failing while the OpenAI control passes.
- Every affected successful transport emits one observable acceptance receipt.
- Ollama supplies its real HTTP status and headers.
- SDK-backed providers explicitly report unavailable HTTP metadata.
- A pre-response network or setup failure emits no receipt.
- Forwarding wrappers preserve the callback and caller-owned request identity.
- Existing OpenAI `onResponse` behavior remains unchanged.
- Diagnostics distinguish accepted-without-metadata from no accepted request.
- Focused tests, type checks, plugin SDK checks, and repository gates pass.

## Verification

Add contract tests that run a successful stream, a setup failure, and a callback failure through the shared helper. Add focused tests for OpenAI Completions, Ollama, Google, Mistral, the Google extension transport, Anthropic Vertex, and Bedrock Mantle.

For the reproduction, use spies with deterministic mocked provider clients. Consume each stream to completion and record the hook count and receipt. Do not use live credentials or external network calls.

Run the focused tests and then the repository gates:

```bash
pnpm tsgo:prod
pnpm tsgo:test
pnpm check
pnpm test
```

The implementation must stop if a provider cannot expose either a real HTTP response or a reliable stream-opened point. Record that provider as blocked instead of inventing acceptance evidence.
