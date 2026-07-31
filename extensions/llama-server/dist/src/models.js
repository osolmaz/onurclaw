import { SELF_HOSTED_DEFAULT_CONTEXT_WINDOW, SELF_HOSTED_DEFAULT_COST, SELF_HOSTED_DEFAULT_MAX_TOKENS, } from "openclaw/plugin-sdk/provider-setup";
import { asPositiveSafeInteger } from "openclaw/plugin-sdk/string-coerce-runtime";
import { resolveLlamaServerEndpoint } from "./endpoint.js";
function readBoolean(record, key) {
    const value = record?.[key];
    return typeof value === "boolean" ? value : undefined;
}
function normalizeStatus(value) {
    switch (value) {
        case "unloaded":
        case "loading":
        case "loaded":
        case "sleeping":
        case "downloading":
            return value;
        default:
            return "unknown";
    }
}
function resolveContextWindow(props) {
    return (asPositiveSafeInteger(props?.default_generation_settings?.n_ctx) ??
        asPositiveSafeInteger(props?.n_ctx) ??
        SELF_HOSTED_DEFAULT_CONTEXT_WINDOW);
}
function resolveMaxTokens(props, contextWindow) {
    const params = props?.default_generation_settings?.params;
    const advertised = asPositiveSafeInteger(params?.max_tokens) ?? asPositiveSafeInteger(params?.n_predict);
    return Math.min(advertised ?? SELF_HOSTED_DEFAULT_MAX_TOKENS, contextWindow);
}
function resolveInput(row, props) {
    const advertised = row.architecture?.input_modalities;
    const supportsImage = (Array.isArray(advertised) && advertised.includes("image")) ||
        props?.modalities?.vision === true;
    return supportsImage ? ["text", "image"] : ["text"];
}
function buildCompat(props) {
    const caps = props?.chat_template_caps;
    const supportsTools = readBoolean(caps, "supports_tools") === true &&
        readBoolean(caps, "supports_tool_calls") === true;
    const supportsTypedContent = readBoolean(caps, "supports_typed_content") === true;
    return {
        supportsStore: false,
        supportsDeveloperRole: false,
        supportsReasoningEffort: false,
        supportsTemperature: true,
        supportsUsageInStreaming: true,
        supportsTools,
        supportsStrictMode: false,
        supportsJsonSchemaResponseFormat: true,
        requiresStringContent: !supportsTypedContent,
        maxTokensField: "max_tokens",
    };
}
/** Maps one llama-server model row plus optional runtime properties into OpenClaw config. */
export function mapLlamaServerModel(row, props) {
    const id = typeof row.id === "string" ? row.id.trim() : "";
    if (!id || (row.object !== undefined && row.object !== "model")) {
        return null;
    }
    const contextWindow = resolveContextWindow(props);
    const buildInfo = typeof props?.build_info === "string" ? props.build_info.trim() : "";
    const exitCode = asPositiveSafeInteger(row.status?.exit_code);
    return {
        config: {
            id,
            name: id,
            reasoning: false,
            input: resolveInput(row, props),
            cost: { ...SELF_HOSTED_DEFAULT_COST },
            contextWindow,
            contextTokens: contextWindow,
            maxTokens: resolveMaxTokens(props, contextWindow),
            compat: buildCompat(props),
        },
        status: normalizeStatus(row.status?.value),
        failed: row.status?.failed === true,
        ...(exitCode !== undefined ? { exitCode } : {}),
        ...(buildInfo ? { buildInfo } : {}),
        ...(asPositiveSafeInteger(props?.total_slots) !== undefined
            ? { totalSlots: asPositiveSafeInteger(props?.total_slots) }
            : {}),
    };
}
/** Keeps explicit rows first and appends models discovered from the server. */
export function mergeLlamaServerModels(params) {
    const explicit = Array.isArray(params.explicitModels) ? params.explicitModels : [];
    const merged = [...explicit];
    const seen = new Set(explicit.map((model) => model.id));
    for (const discovered of params.discoveredModels) {
        if (seen.has(discovered.config.id)) {
            continue;
        }
        seen.add(discovered.config.id);
        merged.push(discovered.config);
    }
    return merged;
}
export function buildLlamaServerProviderConfig(params) {
    const endpoint = resolveLlamaServerEndpoint(params.configured?.baseUrl);
    const request = params.configured?.request ?? {};
    return {
        ...params.configured,
        baseUrl: endpoint.inferenceBaseUrl,
        api: "openai-completions",
        request: typeof request.allowPrivateNetwork === "boolean"
            ? request
            : { ...request, allowPrivateNetwork: true },
        models: mergeLlamaServerModels({
            explicitModels: params.configured?.models,
            discoveredModels: params.discoveredModels,
        }),
    };
}
