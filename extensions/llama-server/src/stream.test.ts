import type { AssistantMessage, Context, Model } from "openclaw/plugin-sdk/llm";
import { createAssistantMessageEventStream } from "openclaw/plugin-sdk/llm";
import { describe, expect, it, vi } from "vitest";
import { resolveLlamaServerLoopRecoveryConfig } from "./loop-recovery.js";
import {
  normalizeLlamaServerPayload,
  normalizeLlamaServerThinking,
  wrapLlamaServerStream,
} from "./stream.js";

describe("llama-server stream payload", () => {
  it("maps thinking off to llama-server chat-template kwargs", () => {
    expect(
      normalizeLlamaServerThinking(
        {
          model: "model",
          chat_template_kwargs: { preserve_thinking: true, enable_thinking: true },
        },
        "off",
      ),
    ).toEqual({
      model: "model",
      chat_template_kwargs: { preserve_thinking: true, enable_thinking: false },
    });
  });

  it("does not force thinking on when OpenClaw selected another level", () => {
    const payload = { model: "model" };
    expect(normalizeLlamaServerThinking(payload, "high")).toBe(payload);
  });

  it("maps OpenAI nested JSON Schema to llama-server's direct schema field", () => {
    expect(
      normalizeLlamaServerPayload({
        model: "model",
        response_format: {
          type: "json_schema",
          json_schema: {
            name: "openclaw_response",
            schema: {
              type: "object",
              properties: { ok: { type: "boolean" } },
              required: ["ok"],
            },
          },
        },
      }),
    ).toEqual({
      model: "model",
      response_format: {
        type: "json_object",
        schema: {
          type: "object",
          properties: { ok: { type: "boolean" } },
          required: ["ok"],
        },
      },
    });
  });

  it("maps llama-server's direct response-format schema to json_object", () => {
    expect(
      normalizeLlamaServerPayload({
        response_format: {
          type: "json_schema",
          schema: { type: "object", properties: { ok: { type: "boolean" } } },
        },
      }),
    ).toEqual({
      response_format: {
        type: "json_object",
        schema: { type: "object", properties: { ok: { type: "boolean" } } },
      },
    });
  });

  it("injects a requested schema when the shared transport omits it", () => {
    expect(
      normalizeLlamaServerPayload(
        { model: "model" },
        {
          type: "object",
          properties: { ok: { type: "boolean" } },
          required: ["ok"],
        },
      ),
    ).toEqual({
      model: "model",
      response_format: {
        type: "json_object",
        schema: {
          type: "object",
          properties: { ok: { type: "boolean" } },
          required: ["ok"],
        },
      },
    });
  });

  it("keeps non-schema response formats unchanged", () => {
    const payload = { response_format: { type: "json_object" } };
    expect(normalizeLlamaServerPayload(payload)).toEqual(payload);
  });

  it("sends one tool-free recovery request through the shared stream", async () => {
    const model: Model = {
      id: "qwen3.6-35b-a3b",
      name: "Qwen",
      api: "openai-completions",
      provider: "llama-server",
      baseUrl: "http://127.0.0.1:8080/v1",
      reasoning: false,
      input: ["text"],
      cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },
      contextWindow: 65_536,
      maxTokens: 8192,
    };
    const usage: AssistantMessage["usage"] = {
      input: 1,
      output: 1,
      cacheRead: 0,
      cacheWrite: 0,
      totalTokens: 2,
      cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, total: 0 },
    };
    const toolCycle = (id: string) => [
      {
        role: "assistant" as const,
        content: [
          {
            type: "toolCall" as const,
            id,
            name: "exec",
            arguments: { command: "find /private 2>/dev/null" },
          },
        ],
        api: "openai-completions" as const,
        provider: "llama-server",
        model: model.id,
        usage,
        stopReason: "toolUse" as const,
        timestamp: 1,
      },
      {
        role: "toolResult" as const,
        toolCallId: id,
        toolName: "exec",
        content: [{ type: "text" as const, text: "(no output)" }],
        isError: false,
        timestamp: 2,
      },
    ];
    const context: Context = {
      messages: [
        { role: "user", content: "concurrency", timestamp: 0 },
        ...toolCycle("call-1"),
        ...toolCycle("call-2"),
      ],
      tools: [{ name: "exec", description: "run", parameters: { type: "object" } }],
    };
    const observedContexts: Context[] = [];
    const final: AssistantMessage = {
      role: "assistant",
      content: [{ type: "text", text: "I need access to continue." }],
      api: "openai-completions",
      provider: "llama-server",
      model: model.id,
      usage,
      stopReason: "stop",
      timestamp: 3,
    };
    const underlying = vi.fn((_model: Model, submitted: Context) => {
      observedContexts.push(submitted);
      const stream = createAssistantMessageEventStream();
      stream.push({ type: "start", partial: final });
      stream.push({ type: "done", reason: "stop", message: final });
      return stream;
    });
    const onLoopRecovery = vi.fn();
    const wrapped = wrapLlamaServerStream({ streamFn: underlying, thinkingLevel: "off" } as never, {
      loopRecovery: resolveLlamaServerLoopRecoveryConfig({
        loopRecovery: {
          enabled: true,
          models: ["llama-server/qwen3.6-35b-a3b"],
        },
      }),
      onLoopRecovery,
    });

    await expect((await wrapped(model, context)).result()).resolves.toEqual(final);
    expect(underlying).toHaveBeenCalledOnce();
    expect(observedContexts[0]?.tools).toEqual([]);
    expect(observedContexts[0]?.messages).toHaveLength(4);
    expect(onLoopRecovery).toHaveBeenCalledWith({
      model: "llama-server/qwen3.6-35b-a3b",
      toolName: "exec",
      repeatCount: 2,
      collapsedCycles: 1,
    });
  });
});
