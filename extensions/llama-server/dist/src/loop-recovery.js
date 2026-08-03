import { createAssistantMessageEventStream } from "openclaw/plugin-sdk/llm";
const DEFAULT_REPEAT_THRESHOLD = 2;
const MIN_REPEAT_THRESHOLD = 2;
const MAX_REPEAT_THRESHOLD = 10;
const MAX_TAIL_MESSAGES = 40;
const MAX_BUFFERED_RECOVERY_EVENTS = 100_000;
export const LOOP_RECOVERY_TERMINAL_TEXT = "I couldn't safely continue after the same tool call produced no new evidence. Please provide the missing access or clarify how you want me to proceed.";
export const DEFAULT_LOOP_RECOVERY_INSTRUCTION = "OpenClaw stopped a repeated tool call because the same action produced no new evidence. Do not call tools in this response. Use the evidence already available, explain what access or information is missing, or ask one concise clarifying question.";
function isRecord(value) {
    return Boolean(value) && typeof value === "object" && !Array.isArray(value);
}
function stringArray(value) {
    if (!Array.isArray(value)) {
        return [];
    }
    return [
        ...new Set(value
            .filter((entry) => typeof entry === "string" && entry.trim().length > 0)
            .map((entry) => entry.trim())),
    ];
}
export function resolveLlamaServerLoopRecoveryConfig(pluginConfig) {
    const raw = isRecord(pluginConfig) && isRecord(pluginConfig.loopRecovery)
        ? pluginConfig.loopRecovery
        : {};
    const repeatThreshold = typeof raw.repeatThreshold === "number" &&
        Number.isInteger(raw.repeatThreshold) &&
        raw.repeatThreshold >= MIN_REPEAT_THRESHOLD &&
        raw.repeatThreshold <= MAX_REPEAT_THRESHOLD
        ? raw.repeatThreshold
        : DEFAULT_REPEAT_THRESHOLD;
    return {
        enabled: raw.enabled === true,
        models: new Set(stringArray(raw.models)),
        repeatThreshold,
        tools: new Set(stringArray(raw.tools).length > 0 ? stringArray(raw.tools) : ["exec"]),
    };
}
function stableJson(value) {
    if (value === null || typeof value !== "object") {
        return JSON.stringify(value);
    }
    if (Array.isArray(value)) {
        return `[${value.map((entry) => stableJson(entry)).join(",")}]`;
    }
    const record = value;
    return `{${Object.keys(record)
        .sort()
        .map((key) => `${JSON.stringify(key)}:${stableJson(record[key])}`)
        .join(",")}}`;
}
function textOutcome(result) {
    const parts = [];
    for (const content of result.content) {
        if (content.type !== "text") {
            return undefined;
        }
        parts.push(content.text);
    }
    return parts.join("\n").replaceAll("\r\n", "\n").trim();
}
function extractCycle(messages, end) {
    const result = messages[end];
    const assistant = messages[end - 1];
    if (result?.role !== "toolResult" || assistant?.role !== "assistant") {
        return undefined;
    }
    const calls = assistant.content.filter((entry) => entry.type === "toolCall");
    if (calls.length !== 1) {
        return undefined;
    }
    const call = calls[0];
    if (call.id !== result.toolCallId || call.name !== result.toolName) {
        return undefined;
    }
    const outcome = textOutcome(result);
    if (outcome === undefined) {
        return undefined;
    }
    return {
        start: end - 1,
        end,
        assistant,
        result,
        call,
        signature: stableJson({
            toolName: call.name,
            arguments: call.arguments,
            outcome,
            isError: result.isError,
        }),
    };
}
function findRepeatedTail(messages, config) {
    if (messages.length < config.repeatThreshold * 2) {
        return [];
    }
    const floor = Math.max(1, messages.length - MAX_TAIL_MESSAGES);
    const latest = extractCycle(messages, messages.length - 1);
    if (!latest || !config.tools.has(latest.call.name)) {
        return [];
    }
    const cycles = [latest];
    let cursor = latest.start - 1;
    while (cursor >= floor) {
        const previous = extractCycle(messages, cursor);
        if (!previous || previous.signature !== latest.signature) {
            break;
        }
        cycles.push(previous);
        cursor = previous.start - 1;
    }
    if (cycles.length < config.repeatThreshold) {
        return [];
    }
    return cycles.reverse();
}
function annotateRetainedResult(result, repeatCount) {
    const note = {
        type: "text",
        text: `OpenClaw observed this same action and outcome ${repeatCount} times and stopped the repeated loop.`,
    };
    return {
        ...result,
        content: [...result.content, note],
    };
}
export function recoverRepeatedToolLoop(params) {
    const canonicalModel = `${params.model.provider}/${params.model.id}`;
    if (!params.config.enabled || !params.config.models.has(canonicalModel)) {
        return {
            context: params.context,
            recovered: false,
            collapsedCycles: 0,
            repeatCount: 0,
        };
    }
    const cycles = findRepeatedTail(params.context.messages, params.config);
    if (cycles.length === 0) {
        return {
            context: params.context,
            recovered: false,
            collapsedCycles: 0,
            repeatCount: 0,
        };
    }
    const retained = cycles[0];
    const messages = [
        ...params.context.messages.slice(0, retained.start),
        retained.assistant,
        annotateRetainedResult(retained.result, cycles.length),
        {
            role: "user",
            content: params.instruction ?? DEFAULT_LOOP_RECOVERY_INSTRUCTION,
            timestamp: params.now ?? Date.now(),
        },
    ];
    return {
        context: {
            ...params.context,
            messages,
            tools: [],
        },
        recovered: true,
        collapsedCycles: cycles.length - 1,
        repeatCount: cycles.length,
        toolName: retained.call.name,
    };
}
function hasToolCall(message) {
    return message.content.some((entry) => entry.type === "toolCall");
}
function zeroUsage() {
    return {
        input: 0,
        output: 0,
        cacheRead: 0,
        cacheWrite: 0,
        totalTokens: 0,
        cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0, total: 0 },
    };
}
function terminalMessage(model, source, errorMessage) {
    return {
        role: "assistant",
        content: [{ type: "text", text: LOOP_RECOVERY_TERMINAL_TEXT }],
        api: source?.api ?? model.api,
        provider: source?.provider ?? model.provider,
        model: source?.model ?? model.id,
        usage: source?.usage ?? zeroUsage(),
        stopReason: "stop",
        timestamp: Date.now(),
        ...(errorMessage ? { errorMessage } : {}),
    };
}
function pushTextResponse(output, message) {
    const partial = { ...message, content: [] };
    output.push({ type: "start", partial });
    output.push({ type: "text_start", contentIndex: 0, partial });
    output.push({
        type: "text_delta",
        contentIndex: 0,
        delta: LOOP_RECOVERY_TERMINAL_TEXT,
        partial: message,
    });
    output.push({
        type: "text_end",
        contentIndex: 0,
        content: LOOP_RECOVERY_TERMINAL_TEXT,
        partial: message,
    });
    output.push({ type: "done", reason: "stop", message });
}
/**
 * Buffers the single recovery response so a provider cannot smuggle a tool call
 * through an empty submitted tool surface. Normal model calls remain streaming.
 */
export function guardToollessRecoveryStream(params) {
    const output = createAssistantMessageEventStream();
    void (async () => {
        try {
            const source = await params.source;
            const events = [];
            for await (const event of source) {
                if (events.length >= MAX_BUFFERED_RECOVERY_EVENTS) {
                    throw new Error("tool-loop recovery response exceeded the event limit");
                }
                events.push(event);
            }
            const final = await source.result();
            if (hasToolCall(final)) {
                pushTextResponse(output, terminalMessage(params.model, final));
                return;
            }
            for (const event of events) {
                output.push(event);
            }
        }
        catch (error) {
            const message = terminalMessage(params.model, undefined, error instanceof Error ? error.message : String(error));
            pushTextResponse(output, message);
        }
    })();
    return output;
}
