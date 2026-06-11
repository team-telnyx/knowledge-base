---
title: AI Assistants
summary: Telnyx AI Assistants are configurable voice and text agents that support
  multi-agent handoff, dynamic variables, persistent memory, async tool execution,
  enterprise integrations, custom LLM providers, Langfuse observability, and migration
  from other providers — all orchestrated through the Mission Control Portal or API.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
  content_hash: 70a4981634a6392849db64eb9505dc98ed11f2c816e1a5a90809b02d509e14b1
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
  content_hash: fef9a26ab4abb9421515d4444216948ad9d6348ed5eebc66c50729e9ab27e71a
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools/index
  content_hash: 4305d6ceba22801446c835423e7dad2029e48c5d186c3358bde90d33d9cf2d90
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
  content_hash: 26757cd4f78fd56c2320d158d13becea98fbb06936445b505a2075cdd609a686
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
  content_hash: 3d2eeb67ed78ad9cf2e5fd0a52e0b6b017bf273d08335395bf9df845a2f4bacf
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
  content_hash: c1af4766c041fd4740d0e4a329bb36fb52a550bc0e8b28684ba40e1aa0274ac4
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
  content_hash: 4441f80ea6c53c4f58838df0f99b66bd3cc4779b2c8415f970c5a4d17dab9d77
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
  content_hash: c7ecb160d4f9b143af3c70bcb729def8e69d59ff8b3f872b15654bf3b3971030
updated_at: 2026-06-11T10:29:30Z
---

# AI Assistants

*Part 2 of 4 — see also: [Part 1](ai-assistants--part-1.md), [Part 3](ai-assistants--part-3.md), [Part 4](ai-assistants--part-4.md)*

Telnyx AI Assistants are configurable voice and text agents that support multi-agent handoff, dynamic variables, persistent memory, async tool execution, enterprise integrations, custom LLM providers, Langfuse observability, and migration from other providers — all orchestrated through the Mission Control Portal or API.

## Dynamic Variables

Dynamic variables let you template your assistant's behaviour using `{{variable_name}}` placeholders that are resolved at conversation start. This enables a single assistant configuration to handle personalised conversations for different users and contexts.

### Resolution precedence

Variables are resolved in this order (highest to lowest):

1. **Outbound API call** — Pass values via `AIAssistantDynamicVariables` in the dial request.
2. **Custom SIP headers** — Headers using the `X-` prefix are mapped to variables (`X-Full-Name` → `{{full_name}}`). The `telnyx_` namespace is reserved and ignored.
3. **Dynamic variables webhook** — If `dynamic_variables_webhook_url` is set, Telnyx sends an `assistant.initialization` event at conversation start. The webhook must respond within 1 second.
4. **Default values** — Set in the Assistant builder as fallbacks.
5. **Unset** — Variables not resolved by any method remain as raw `{{variable_name}}` text.

### System variables

Telnyx provides built-in variables:

| Variable | Description |
|---|---|
| `{{telnyx_current_time}}` | Current date and time (UTC) |
| `{{telnyx_conversation_channel}}` | `phone_call`, `web_call`, or `sms_chat` |
| `{{telnyx_agent_target}}` | Phone number or SIP URI of the agent |
| `{{telnyx_end_user_target}}` | Phone number or SIP URI of the end user |
| `{{telnyx_shaken_stir_attestation}}` | SHAKEN/STIR attestation level (`a`, `b`, or `c`) |
| `{{call_control_id}}` | Call control ID |

A family of date/time variables and timezone variants is also available (e.g., `{{telnyx_current_time_America/New_York}}`, `{{telnyx_current_date}}`, `{{telnyx_current_weekday}}`). For custom formatting, pipe through the `date` filter with `strftime` codes:

- `{{ telnyx_current_time | date: "%A, %B %d, %Y" }}`
- `{{ telnyx_current_time | date: "%I:%M %p", "America/New_York" }}`

### Webhook payload and response

When the dynamic variables webhook fires, it receives a signed payload containing conversation context (`telnyx_conversation_channel`, `telnyx_agent_target`, `telnyx_end_user_target`, `call_control_id`, `assistant_id`). The expected response shape is:

```json
{
  "dynamic_variables": {
    "full_name": "Rachel Thomas",
    "facility_name": "UCHealth"
  },
  "memory": {
    "conversation_query": "metadata->telnyx_end_user_target=eq.+13128675309&limit=5&order=last_message_at.desc"
  },
  "conversation": {
    "metadata": {
      "customer_tier": "premium"
    }
  }
}
```

All three top-level fields (`dynamic_variables`, `memory`, `conversation`) are optional. For inbound phone calls, `telnyx_end_user_target_verified` is `true` when the call has Full (A) STIR/SHAKEN attestation.

### Variable naming best practices

- Use descriptive, `snake_case` names (e.g., `customer_name`, `account_number`).
- Group related variables (`facility_name`, `facility_department`).
- Never use the reserved `telnyx_` prefix.
- Set default values for testing and as fallbacks.
- Keep webhook responses under the 1-second timeout.

## Memory

Memory enables an assistant to recall details from past conversations. Rather than a fixed memory scope, Telnyx exposes a flexible query language — any query supported by the [List Conversations endpoint](https://developers.telnyx.com/api-reference/conversations/list-conversations) can be used to define which previous conversations the assistant remembers.

### Configuring memory

Memory is configured via the `memory` field in the dynamic variables webhook response. Specify a `conversation_query` to control which conversations are included:

```json
{
  "memory": {
    "conversation_query": "metadata->telnyx_end_user_target=eq.+13128675309&limit=5&order=last_message_at.desc"
  }
}
```

This example gives the assistant access to the last 5 conversations with the current user's phone number.

### Insight filtering

To control which information *within* a conversation is remembered, specify a comma-delimited list of insight IDs via `insight_query`:

```json
{
  "memory": {
    "conversation_query": "metadata->telnyx_end_user_target=eq.+13128675309&limit=5",
    "insight_query": "insight_ids=123,456"
  }
}
```

Insight IDs can be found in the **Insights** tab for your assistant.

### Custom metadata

You can build your own memory access system using custom metadata on conversations. Add metadata in the webhook response:

```json
{
  "conversation": {
    "metadata": {
      "your_custom_metadata": "your_custom_value"
    }
  }
}
```

In future conversations, filter on this metadata in the `conversation_query` using the syntax `metadata->your_custom_metadata=eq.your_custom_value`.

## Async Tools

Async tools let an assistant trigger long-running operations without blocking the conversation. Combined with the [Add Messages API](https://developers.telnyx.com/api-reference/call-commands/add-messages-to-ai-assistant), results can be injected back into the conversation whenever they are ready.

### The two building blocks

| Feature | What it does | Standalone use |
|---|---|---|
| **Async webhook flag** (`async: true`) | Assistant continues talking while the webhook executes | Fire-and-forget operations (logging, notifications) |
| **Add Messages API** | Injects new context into an active conversation | Supervisor interventions, scheduled reminders, external triggers |

### Combined workflow

1. Assistant triggers an async webhook (e.g., order lookup).
2. Assistant continues chatting with the customer.
3. Backend processes the request (5–30+ seconds).
4. Backend calls the Add Messages API to inject results.
5. Assistant naturally incorporates the new information.

### Configuring an async webhook

Set `async: true` in the webhook tool configuration:

```json
{
  "type": "webhook",
  "webhook": {
    "name": "lookup_order_status",
    "description": "Triggers an async order status lookup.",
    "url": "https://your-backend.com/order-lookup",
    "method": "POST",
    "async": true,
    "body_parameters": {
      "type": "object",
      "properties": {
        "order_id": { "type": "string", "description": "The customer's order ID" }
      },
      "required": ["order_id"]
    }
  }
}
```

When the webhook fires, your backend receives the configured body parameters plus the `x-telnyx-call-control-id` header, which is needed to inject results back via the Add Messages API.

### Add Messages API

```
POST /v2/calls/{call_control_id}/actions/ai_assistant_add_messages
```

```bash
curl -X POST "https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_add_messages" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "system",
        "content": "Order ORD-12345 status: SHIPPED. Share this with the customer now."
      }
    ]
  }'
```

Supported message roles:

| Role | Use case |
|---|---|
| `system` | Instructions or context for the assistant (recommended for async results) |
| `user` | Simulate user input |
| `assistant` | Inject assistant responses |

### Multiple parallel lookups

You can trigger multiple async webhooks simultaneously. Each completes independently and injects results as they become available. Instruct the assistant to call all relevant tools at once rather than sequentially.

### Best practices

- When injecting results, format messages clearly with identifiers so the assistant knows which query the results belong to.
- Your backend should return a 200 response quickly to acknowledge receipt, then process asynchronously.
- There is no timeout constraint on async webhooks — your backend can take as long as needed before calling the Add Messages API.
- If a call has already ended when you try to inject a message, the API returns a 404.
