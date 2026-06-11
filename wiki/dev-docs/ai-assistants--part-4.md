---
title: AI Assistants
summary: Telnyx AI Assistants are configurable voice and text agents that support
  multi-agent handoff, dynamic variables, persistent memory, async tool execution,
  enterprise integrations, custom LLM providers, Langfuse observability, and migration
  from other providers — all orchestrated through the Mission Control Portal or API.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
updated_at: 2026-06-11T10:29:30Z
---

# AI Assistants

*Part 4 of 4 — see also: [Part 1](ai-assistants--part-1.md), [Part 2](ai-assistants--part-2.md), [Part 3](ai-assistants--part-3.md)*

Telnyx AI Assistants are configurable voice and text agents that support multi-agent handoff, dynamic variables, persistent memory, async tool execution, enterprise integrations, custom LLM providers, Langfuse observability, and migration from other providers — all orchestrated through the Mission Control Portal or API.

## Observability

Observability gives you full visibility into your assistant's behaviour by connecting it to [Langfuse](https://langfuse.com). Every interaction is automatically traced — including input messages, output responses, token usage, latency, and cost.

### What is traced

| What | Where | Details captured |
|---|---|---|
| LLM generations | AI Conversations | Input messages, output response, model, token usage |
| Tool calls | AI Assistants | Tool name, input arguments, output result |

Traces are grouped by conversation using a deterministic trace ID derived from the `conversation_id`.

### Configuration

1. **Create Langfuse credentials** — Obtain a public key, secret key, and host URL from your Langfuse project.
2. **Store as integration secrets** — In the [Integration Secrets](https://portal.telnyx.com/#/integration-secrets) tab, create secrets for the Langfuse secret key and public key.
3. **Enable on your assistant** — Set `observability_settings` via API:

```bash
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

To disable, set `"status": "disabled"`.

### Observability settings reference

| Field | Required when enabled | Description |
|---|---|---|
| `status` | Yes | `enabled` or `disabled` |
| `secret_key_ref` | Yes | Integration secret identifier for Langfuse secret key |
| `public_key_ref` | Yes | Integration secret identifier for Langfuse public key |
| `host` | Yes | Langfuse instance URL |
| `prompt_name` | No | Name of a Langfuse-managed prompt to link |
| `prompt_version` | No | Pin to an exact prompt version (mutually exclusive with `prompt_label`) |
| `prompt_label` | No | Pin to a labelled prompt, e.g. `"production"` (mutually exclusive with `prompt_version`) |
| `prompt_sync` | No | When `enabled`, publishes the assistant's instructions to Langfuse on every save. Requires `prompt_name` |

### Langfuse-managed prompts

You can link an assistant to a prompt managed in Langfuse. Pin to a specific version with `prompt_version` or to a label with `prompt_label` (the two are mutually exclusive). Enable `prompt_sync` to auto-publish the assistant's instructions back to Langfuse on every save; Telnyx stores the returned version in `prompt_version`.

### What you see in Langfuse

- **Traces** — One per conversation turn, grouped by `conversation_id`. Includes name and metadata (`conversation_id`, `assistant_id`).
- **Generations** — Each LLM call. Includes model, full input/output, and token usage (non-streaming only).
- **Tool call events** — Name (`tool-call-{tool_name}`), input arguments, output result.

### Security and performance

- Never share Langfuse keys directly — always store them as integration secrets.
- Use separate Langfuse projects for development and production.
- Observability adds minimal overhead; traces are sent asynchronously and do not block conversation flow.
- If self-hosting Langfuse, ensure the instance is reachable from Telnyx infrastructure.

## Importing Assistants

If you have voice assistants with another provider, you can import them to Telnyx via the Portal or [API](https://developers.telnyx.com/api-reference/assistants/import-assistants-from-external-provider).

### Supported providers

- **Vapi** — Import voice assistants with all configurations.
- **ElevenLabs** — Import conversational AI agents.
- **Retell** — Import single- and multi-prompt agents.

### Import workflow

1. Navigate to [AI Assistants](https://portal.telnyx.com/#/ai/assistants) and click **Import Assistants**.
2. Select the provider and securely store your API key.
3. Choose which assistants to import.
4. Test the imported assistants using the pencil or telephone icons.

Any previously imported assistant will be overwritten with its latest version from the source provider. Trial accounts are limited to 1 AI Assistant.

### Supported import functionality

| Feature | Import behaviour |
|---|---|
| Instructions | Imported as-is |
| Greeting (first message) | Imported as-is |
| LLM | Defaults to Telnyx on-prem LLM; BYO with third-party providers by storing an API key |
| Voice | Vapi/ElevenLabs voices imported as-is; otherwise defaults to Telnyx on-prem TTS |
| Dynamic variables | References and defaults imported as-is |
| Tools | Hangup, transfer, and webhook tools imported as-is |
| MCP Servers | Imported as-is |
| Insights | Structured and unstructured analysis configuration imported as-is |
| Data retention | Disabled data retention setting imported as-is |
| Knowledge bases | **Not imported** — drag and drop files or import website content manually |
| Secrets | Placeholder integration secrets are created with the same names; you must resupply the values on the [Integration Secrets](https://portal.telnyx.com/#/integration-secrets) page |

## Troubleshooting

### Handoff issues

- **Handoff loops** — Define clear, mutually exclusive responsibility boundaries. Add instructions like "Only handoff if the request is truly outside your domain." Set maximum handoff limits and implement failsafe routing to human agents.
- **Context loss after handoff** — Ensure the dynamic variables webhook is configured for all agents in the chain. Verify consistent conversation metadata and memory query logic across agents.
- **Incorrect agent selection** — Refine triage instructions with specific examples. Add confirmation steps ("It sounds like you need billing help, is that correct?"). Review conversation logs for misrouting patterns.
- **Handoff doesn't trigger** — Verify the handoff tool is added and target assistant IDs are valid. Add explicit handoff triggers in agent instructions.

### Dynamic variable issues

- **Variables not resolving** — Check webhook timeout (must respond within 1 second), variable name mismatches, and resolution precedence order.
- **Incorrect formatting** — Validate JSON syntax, data types, and mustache template usage (`{{variable}}`, not `{variable}`).
- **Webhook debugging** — Use the Portal's per-conversation webhook logs alongside transcripts. Test endpoints independently with the exact payload Telnyx sends.

### Integration issues

- **Connection failures** — Verify credentials, API access, security tokens, and instance URL format (no `https://` or trailing `/`).
- **Tools not appearing** — Refresh the page, verify integration account permissions, and check platform subscriptions.
- **Authentication errors during calls** — Regenerate tokens, update stored credentials, and check for account locks.
- **Rate limiting** — Reduce call frequency, implement caching, or distribute calls across service accounts.

### Observability issues

- **Traces not appearing** — Verify `status` is `enabled`, credentials reference valid integration secrets, and the `host` URL matches your Langfuse instance.
- **Missing output or token usage** — Token counts are captured for non-streaming calls only. Output may be empty if a call fails mid-stream.
- **Secret reference errors** — Ensure the identifier exactly matches the secret name and the secret belongs to the same organisation as the assistant.
- **Key rotation** — Update integration secret values in the Portal; the assistant automatically uses new values on the next conversation.

### Async tool issues

- **Call ended before results arrive** — The Add Messages API returns a 404; log and move on.
- **Multiple results for the same lookup** — Include identifiers in injected messages so the assistant can distinguish them.
