---
title: 'AI Assistants: Handoff, Observability, and Async Tools'
summary: Telnyx AI assistants support advanced conversation patterns including agent
  handoff between specialized assistants, Langfuse-based observability for tracing
  LLM calls and tool executions, and async webhook tools combined with the Add Messages
  API for long-running operations that inject results back into active conversations
  without blocking the user.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools/index
updated_at: 2026-08-05T13:43:49Z
---

# AI Assistants: Handoff, Observability, and Async Tools

*Part 2 of 4 — see also: [Part 1](ai-assistants-handoff-observability-and-async-tools--part-1.md), [Part 3](ai-assistants-handoff-observability-and-async-tools--part-3.md), [Part 4](ai-assistants-handoff-observability-and-async-tools--part-4.md)*

Telnyx AI assistants support advanced conversation patterns including agent handoff between specialized assistants, Langfuse-based observability for tracing LLM calls and tool executions, and async webhook tools combined with the Add Messages API for long-running operations that inject results back into active conversations without blocking the user.

## Observability

Observability gives full visibility into an AI assistant's behavior by connecting it to [Langfuse](https://langfuse.com). Every LLM call, tool execution, and conversation turn is traced, including input messages, output responses, token usage, latency, and cost.

### What is traced

| What is traced | Where it happens | Details captured |
| --- | --- | --- |
| LLM generations | AI Conversations | Input messages, output response, model, token usage |
| Tool calls | AI Assistants | Tool name, input arguments, output result |

Traces are grouped by conversation using a deterministic trace ID derived from the `conversation_id`, so all LLM calls and tool executions within the same conversation appear together in the Langfuse dashboard.

### Key benefits

- **Debugging** — inspect the exact messages sent to the LLM and the responses received.
- **Cost tracking** — monitor token usage per conversation, assistant, or model.
- **Quality evaluation** — review LLM outputs and tool call results to identify issues.
- **Latency analysis** — measure response times for LLM calls and tool executions.
- **Multi-tenant** — each assistant can connect to a different Langfuse project with its own credentials.

### Requirements

1. A [Langfuse](https://langfuse.com) account (cloud or self-hosted)
2. A Langfuse project with a public key and secret key
3. A Telnyx AI Assistant

### Configuration

**Step 1 — Create Langfuse credentials.** In the Langfuse dashboard, navigate to **Settings > API Keys** and create a new API key pair. You will need a Public Key (e.g., `pk-lf-abc123...`), a Secret Key (e.g., `sk-lf-xyz789...`), and the Host URL (e.g., `https://cloud.langfuse.com`).

**Step 2 — Store credentials as integration secrets.** Navigate to [Integration Secrets](https://portal.telnyx.com/#/integration-secrets) in the portal and create two secrets: one for the Langfuse secret key (e.g., `langfuse-secret-key`) and one for the public key (e.g., `langfuse-public-key`). The secret value cannot be retrieved after it is stored.

**Step 3 — Enable observability on your assistant.** Set `observability_settings` when creating or updating an assistant:

```
curl --request POST \
  --url https://api.telnyx.com/v2/ai/assistants \
  --header "Authorization: Bearer $TELNYX_API_KEY" \
  --header 'Content-Type: application/json' \
  --data '{
    "name": "My Observable Assistant",
    "model": "anthropic/claude-haiku-4-5",
    "instructions": "You are a helpful assistant.",
    "observability_settings": {
      "status": "enabled",
      "secret_key_ref": "langfuse-secret-key",
      "public_key_ref": "langfuse-public-key",
      "host": "https://cloud.langfuse.com"
    }
  }'
```

To disable observability, update the status to `"disabled"`.

### Linking a Langfuse-managed prompt

In addition to tracing, an assistant can be linked to a [prompt managed in Langfuse](https://langfuse.com/docs/prompts/get-started). This lets you iterate on the assistant's instructions in Langfuse and reference them by version or label, and optionally have Telnyx publish the assistant's instructions back to Langfuse on every save.

**Pin to a prompt version or label.** Set `prompt_name` together with either `prompt_version` (an integer pinning to an exact version) or `prompt_label` (e.g., `"production"`, pinning to whichever version currently carries that label). The two are mutually exclusive.

**Auto-publish the assistant's instructions.** Set `prompt_sync` to `"enabled"` to automatically publish the assistant's `instructions` back to Langfuse as a prompt on every create or update. Telnyx calls Langfuse's create-prompt API and stores the returned version in `prompt_version`, so the assistant continues to run on the exact instructions just saved. `prompt_sync` requires `prompt_name` and is independent of `prompt_version` / `prompt_label` pinning.

### Observability settings reference

| Field | Type | Required when enabled | Description |
| --- | --- | --- | --- |
| `status` | string | Yes | `enabled` or `disabled` |
| `secret_key_ref` | string | Yes | Integration secret identifier for your Langfuse secret key |
| `public_key_ref` | string | Yes | Integration secret identifier for your Langfuse public key |
| `host` | string | Yes | Your Langfuse instance URL |
| `prompt_name` | string | No | Name of a Langfuse-managed prompt to link. Required when `prompt_version`, `prompt_label`, or `prompt_sync` is set |
| `prompt_version` | integer | No | Pin the assistant to an exact prompt version (≥ 1). Mutually exclusive with `prompt_label` |
| `prompt_label` | string | No | Pin the assistant to a labeled prompt (e.g., `"production"`). Mutually exclusive with `prompt_version` |
| `prompt_sync` | string | No | `enabled` or `disabled` (default `disabled`). When `enabled`, publishes the assistant's instructions to Langfuse on every save and stores the returned version in `prompt_version`. Requires `prompt_name` |

When status is `enabled`, all three credential fields are required. The API returns an error if any are missing, and the secret references are validated to ensure they exist in your integration secrets.

### What you will see in Langfuse

- **Traces** — each conversation turn generates a trace. Traces from the same conversation share a deterministic ID derived from the `conversation_id`. Each trace includes a name (the conversation name if set, otherwise `chat`) and metadata (`conversation_id`, `assistant_id`).
- **Generations** — each LLM call appears as a generation observation with the model, input (full message array), output, and token usage (non-streaming only).
- **Tool calls** — webhook tool executions appear as events named `tool-call-{tool_name}` with input arguments and output result.

### Best practices

- **Security** — never share Langfuse keys directly; always store them as Telnyx integration secrets. Use separate Langfuse projects for development and production. Rotate keys periodically.
- **Performance** — observability adds minimal overhead; traces are sent asynchronously and do not block conversation flow. If self-hosting Langfuse, ensure the instance is reachable from Telnyx infrastructure.
- **Organization** — use conversation names to make traces easier to find, and filter by metadata in Langfuse to find traces for a specific `conversation_id` or `assistant_id`.

### Troubleshooting

- **Traces not appearing** — verify `observability_settings.status` is `"enabled"`, credentials point to valid integration secrets, the `host` matches your Langfuse instance, and you are looking at the correct project.
- **Missing output or token usage** — token usage is captured for non-streaming LLM calls; streaming calls may not include token counts depending on the model provider. Output is captured after the LLM response completes; if a call fails mid-stream, the output may be empty.
- **Secret reference errors** — ensure the integration secret exists, the identifier exactly matches the secret name, and the secret belongs to the same organization as the assistant.
- **Observability not working after key rotation** — update the integration secret values in the portal; the assistant will automatically use the new values on the next conversation.
