import type {
  AssistantMessage,
  Context,
  Model,
  ToolCall,
  ToolResultMessage,
} from "openclaw/plugin-sdk/llm";
import { createAssistantMessageEventStream } from "openclaw/plugin-sdk/llm";
import { describe, expect, it } from "vitest";
import {
  DEFAULT_LOOP_RECOVERY_INSTRUCTION,
  LOOP_RECOVERY_TERMINAL_TEXT,
  guardToollessRecoveryStream,
  recoverRepeatedToolLoop,
  resolveLlamaServerLoopRecoveryConfig,
} from "./loop-recovery.js";

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

function assistant(
  id: string,
  args: Record<string, unknown>,
  text = "checking\n",
): AssistantMessage {
  return {
    role: "assistant",
    content: [
      { type: "text", text },
      { type: "toolCall", id, name: "exec", arguments: args },
    ],
    api: "openai-completions",
    provider: "llama-server",
    model: model.id,
    usage,
    stopReason: "toolUse",
    timestamp: 1,
  };
}

function result(id: string, text = "(no output)"): ToolResultMessage {
  return {
    role: "toolResult",
    toolCallId: id,
    toolName: "exec",
    content: [{ type: "text", text }],
    isError: false,
    timestamp: 2,
  };
}

function enabledConfig() {
  return resolveLlamaServerLoopRecoveryConfig({
    loopRecovery: {
      enabled: true,
      models: ["llama-server/qwen3.6-35b-a3b"],
    },
  });
}

function repeatedContext(): Context {
  return {
    systemPrompt: "system",
    messages: [
      { role: "user", content: "concurrency", timestamp: 0 },
      assistant("call-1", { command: "find /private 2>/dev/null" }),
      result("call-1"),
      assistant("call-2", { command: "find /private 2>/dev/null" }),
      result("call-2"),
    ],
    tools: [{ name: "exec", description: "run", parameters: { type: "object" } }],
  };
}

describe("llama-server loop recovery", () => {
  it("is disabled unless explicitly configured for a canonical model", () => {
    expect(resolveLlamaServerLoopRecoveryConfig({})).toMatchObject({
      enabled: false,
      repeatThreshold: 2,
    });
    expect(
      recoverRepeatedToolLoop({
        context: repeatedContext(),
        model,
        config: resolveLlamaServerLoopRecoveryConfig({}),
      }),
    ).toMatchObject({ recovered: false });
  });

  it("collapses an identical tail and submits a text-only recovery context", () => {
    const source = repeatedContext();
    const recovered = recoverRepeatedToolLoop({
      context: source,
      model,
      config: enabledConfig(),
      now: 3,
    });

    expect(recovered).toMatchObject({
      recovered: true,
      collapsedCycles: 1,
      repeatCount: 2,
      toolName: "exec",
    });
    expect(recovered.context.tools).toEqual([]);
    expect(recovered.context.messages).toHaveLength(4);
    expect(recovered.context.messages[0]).toBe(source.messages[0]);
    expect(recovered.context.messages[1]).toBe(source.messages[1]);
    expect(recovered.context.messages[2]).toMatchObject({
      role: "toolResult",
      toolCallId: "call-1",
      content: [
        { type: "text", text: "(no output)" },
        { type: "text", text: expect.stringContaining("2 times") },
      ],
    });
    expect(recovered.context.messages[3]).toEqual({
      role: "user",
      content: DEFAULT_LOOP_RECOVERY_INSTRUCTION,
      timestamp: 3,
    });
    expect(source.messages).toHaveLength(5);
    expect((source.messages[2] as ToolResultMessage).content).toEqual([
      { type: "text", text: "(no output)" },
    ]);
  });

  it("canonicalizes argument key order", () => {
    const context = repeatedContext();
    context.messages[1] = assistant("call-1", { timeout: 5, command: "same" });
    context.messages[3] = assistant("call-2", { command: "same", timeout: 5 });
    expect(recoverRepeatedToolLoop({ context, model, config: enabledConfig() })).toMatchObject({
      recovered: true,
    });
  });

  it.each([
    {
      name: "changed arguments",
      mutate(context: Context) {
        context.messages[3] = assistant("call-2", { command: "different" });
      },
    },
    {
      name: "changed outcomes",
      mutate(context: Context) {
        context.messages[4] = result("call-2", "permission denied");
      },
    },
    {
      name: "a non-matching model",
      mutate(_context: Context) {},
      otherModel: { ...model, id: "other" },
    },
  ])("does not recover $name", ({ mutate, otherModel }) => {
    const context = repeatedContext();
    mutate(context);
    expect(
      recoverRepeatedToolLoop({ context, model: otherModel ?? model, config: enabledConfig() }),
    ).toMatchObject({ recovered: false });
  });

  it("requires one tool call per assistant message", () => {
    const context = repeatedContext();
    (context.messages[3] as AssistantMessage).content.push({
      type: "toolCall",
      id: "call-extra",
      name: "read",
      arguments: { path: "/tmp/file" },
    });
    expect(recoverRepeatedToolLoop({ context, model, config: enabledConfig() })).toMatchObject({
      recovered: false,
    });
  });

  it("does not apply the exec-only default to polling tools", () => {
    const context = repeatedContext();
    for (const index of [1, 3]) {
      const message = context.messages[index] as AssistantMessage;
      const call = message.content.find((entry): entry is ToolCall => entry.type === "toolCall");
      if (!call) {
        throw new Error("expected tool call");
      }
      call.name = "process";
    }
    for (const index of [2, 4]) {
      (context.messages[index] as ToolResultMessage).toolName = "process";
    }
    expect(recoverRepeatedToolLoop({ context, model, config: enabledConfig() })).toMatchObject({
      recovered: false,
    });
  });

  it("replaces a recovery response that still contains a tool call", async () => {
    const source = createAssistantMessageEventStream();
    const repeated = assistant("call-3", { command: "same" });
    const guarded = guardToollessRecoveryStream({ model, source });
    source.push({ type: "start", partial: repeated });
    source.push({ type: "done", reason: "toolUse", message: repeated });

    const final = await guarded.result();
    expect(final.stopReason).toBe("stop");
    expect(final.content).toEqual([{ type: "text", text: LOOP_RECOVERY_TERMINAL_TEXT }]);
  });

  it("preserves a text recovery response", async () => {
    const source = createAssistantMessageEventStream();
    const message: AssistantMessage = {
      ...assistant("unused", {}),
      content: [{ type: "text", text: "I need access to that path." }],
      stopReason: "stop",
    };
    const guarded = guardToollessRecoveryStream({ model, source });
    source.push({ type: "start", partial: message });
    source.push({ type: "done", reason: "stop", message });

    await expect(guarded.result()).resolves.toEqual(message);
  });
});
