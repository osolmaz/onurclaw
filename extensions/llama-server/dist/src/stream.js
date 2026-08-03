import { streamSimple } from "openclaw/plugin-sdk/llm";
import { LLAMA_SERVER_PROVIDER_ID } from "./defaults.js";
import { guardToollessRecoveryStream, recoverRepeatedToolLoop, } from "./loop-recovery.js";
function isRecord(value) {
    return Boolean(value) && typeof value === "object" && !Array.isArray(value);
}
/** Disables chat-template reasoning when OpenClaw selected thinking off. */
export function normalizeLlamaServerThinking(payload, thinkingLevel) {
    if (!isRecord(payload) || thinkingLevel !== "off") {
        return payload;
    }
    const existing = isRecord(payload.chat_template_kwargs) ? payload.chat_template_kwargs : {};
    return {
        ...payload,
        chat_template_kwargs: {
            ...existing,
            enable_thinking: false,
        },
    };
}
/** Maps the requested response format to the shape llama-server accepts. */
export function normalizeLlamaServerPayload(payload, requestedResponseFormat) {
    if (!isRecord(payload)) {
        return payload;
    }
    const responseFormat = isRecord(payload.response_format)
        ? payload.response_format
        : requestedResponseFormat;
    if (!responseFormat) {
        return payload;
    }
    if (responseFormat.type === "text") {
        return { ...payload, response_format: responseFormat };
    }
    const schema = responseFormat.type === "json_schema"
        ? isRecord(responseFormat.json_schema)
            ? responseFormat.json_schema.schema
            : responseFormat.schema
        : responseFormat.type === "json_object"
            ? responseFormat.schema
            : responseFormat;
    if (!isRecord(schema)) {
        return payload;
    }
    return {
        ...payload,
        response_format: {
            type: "json_object",
            schema,
        },
    };
}
/** Keeps the shared OpenAI transport and adjusts only llama-server request quirks. */
export function wrapLlamaServerStream(ctx, wrapperOptions = {}) {
    const underlying = ctx.streamFn ?? streamSimple;
    return (model, context, options) => {
        if (model.provider !== LLAMA_SERVER_PROVIDER_ID) {
            return underlying(model, context, options);
        }
        const recovery = wrapperOptions.loopRecovery
            ? recoverRepeatedToolLoop({
                context,
                model,
                config: wrapperOptions.loopRecovery,
            })
            : {
                context,
                recovered: false,
                collapsedCycles: 0,
                repeatCount: 0,
            };
        if (recovery.recovered && recovery.toolName) {
            wrapperOptions.onLoopRecovery?.({
                model: `${model.provider}/${model.id}`,
                toolName: recovery.toolName,
                repeatCount: recovery.repeatCount,
                collapsedCycles: recovery.collapsedCycles,
            });
        }
        const onPayload = options?.onPayload;
        const source = underlying(model, recovery.context, {
            ...options,
            onPayload: async (payload, requestModel) => {
                const customized = (await onPayload?.(payload, requestModel)) ?? payload;
                const thinkingNormalized = normalizeLlamaServerThinking(customized, ctx.thinkingLevel);
                return normalizeLlamaServerPayload(thinkingNormalized, options?.responseFormat);
            },
        });
        return recovery.recovered ? guardToollessRecoveryStream({ model, source }) : source;
    };
}
