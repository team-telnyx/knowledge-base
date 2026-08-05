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

*Part 3 of 4 — see also: [Part 1](ai-assistants-handoff-observability-and-async-tools--part-1.md), [Part 2](ai-assistants-handoff-observability-and-async-tools--part-2.md), [Part 4](ai-assistants-handoff-observability-and-async-tools--part-4.md)*

Telnyx AI assistants support advanced conversation patterns including agent handoff between specialized assistants, Langfuse-based observability for tracing LLM calls and tool executions, and async webhook tools combined with the Add Messages API for long-running operations that inject results back into active conversations without blocking the user.

## Async Tools and Deferred Context

Async tools allow an AI assistant to trigger long-running operations without blocking the conversation. Combined with the [Add Messages API](https://developers.telnyx.com/api-reference/call-commands/add-messages-to-ai-assistant), results can be injected back into the conversation whenever they are ready — whether that is 5 seconds or 5 minutes later.

Traditional webhook tools block the conversation until they complete, which works for fast operations but creates awkward pauses for slow backend queries. Async tools let the assistant continue the conversation while operations run in the background. If a backend responds within a few seconds and you prefer to keep using sync webhooks, [Filler Messages](filler-messages.md) offer a simpler alternative — scripted phrases that play at timed intervals to fill silence while the webhook executes.

### The two building blocks

These features are orthogonal — each is useful on its own, but they become especially powerful when combined.

| Feature | What it does | Use alone |
| --- | --- | --- |
| Async webhook flag | Lets the assistant continue talking while the webhook executes | Fire-and-forget operations (logging, notifications) |
| [Add Messages API](https://developers.telnyx.com/api-reference/call-commands/add-messages-to-ai-assistant) | Injects new context into an active conversation | External triggers, scheduled reminders, supervisor interventions |

When combined, the workflow is: the assistant triggers an async webhook (e.g., order lookup), continues chatting with the customer, the backend processes the request (5–30 seconds later), the backend calls the Add Messages API to inject the results, and the assistant naturally incorporates the new information.

### Async webhooks

The `async` flag on webhook tools tells the assistant not to wait for the response. The webhook fires, and the assistant immediately continues the conversation.

**Configuring an async webhook** — set `async: true` in the webhook tool configuration:

```
{
  "type": "webhook",
  "webhook": {
    "name": "lookup_order_status",
    "description": "Triggers an async order status lookup. Results will be delivered automatically when ready.",
    "url": "https://your-backend.com/order-lookup",
    "method": "POST",
    "async": true,
    "headers": [
      {"name": "Content-Type", "value": "application/json"}
    ],
    "body_parameters": {
      "type": "object",
      "properties": {
        "order_id": {
          "type": "string",
          "description": "The customer's order ID"
        }
      },
      "required": ["order_id"]
    }
  }
}
```

Key configuration options:

| Field | Description |
| --- | --- |
| `async` | When `true`, the assistant continues without waiting for a response |
| `url` | Your backend endpoint that will process the request |
| `method` | HTTP method (typically `POST`) |
| `body_parameters` | JSON schema defining the parameters the assistant should provide |

**What your backend receives** — the configured body parameters (e.g., `order_id`) and the `x-telnyx-call-control-id` header identifying the active call. The `x-telnyx-call-control-id` header is critical — it is needed to inject results back into the conversation using the Add Messages API.

### Add Messages API

The [Add Messages API](https://developers.telnyx.com/api-reference/call-commands/add-messages-to-ai-assistant) lets you inject new messages into an active conversation from outside the call flow. This is useful for delivering async results, supervisor interventions, or external triggers.

**Endpoint:** `POST /v2/calls/{call_control_id}/actions/ai_assistant_add_messages`

```
curl -X POST "https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_add_messages" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "system",
        "content": "Order ORD-12345 status: SHIPPED. Tracking: 1Z999AA10123456784. Estimated delivery: Tomorrow. Share this with the customer now."
      }
    ]
  }'
```

**Message roles:**

| Role | Use case |
| --- | --- |
| `system` | Instructions or context for the assistant (recommended for async results) |
| `user` | Simulate user input |
| `assistant` | Inject assistant responses |

**Standalone use cases** — supervisor intervention (a human supervisor injects guidance during a difficult call), scheduled reminders (external system reminds the assistant about time-sensitive information), cross-system triggers (CRM or ticketing system pushes updates to an active call), and escalation prompts (monitoring system detects frustration and injects de-escalation guidance).

### Combining async webhooks with Add Messages

A complete async order lookup system works as follows:

1. **Configure the assistant** with async webhook tools. Instructions should tell the assistant to continue engaging while waiting (mention promotions, ask about experience, offer to help with anything else) and to naturally incorporate results when they arrive.
2. **Build the backend service** that receives the webhook, processes the request, and calls the Add Messages API when done. The backend should return a 200 response quickly to acknowledge receipt and process the actual work asynchronously (background workers, Celery, AWS Lambda, etc.). There is no timeout constraint on async webhooks — the backend can take as long as needed before calling the Add Messages API.
3. **Test the flow** by calling the assistant, asking about an order, and verifying that the assistant triggers the async lookup, continues chatting, and seamlessly shares the order details once results arrive.

### Multiple parallel lookups

Multiple async webhooks can be triggered simultaneously. Each completes independently and injects results as they become available. For example, an assistant can trigger `check_loyalty_points` (~10 seconds) and `lookup_order_status` (~20 seconds) at once, with results dripping into the conversation naturally as each lookup completes.

For parallel lookups to work well, instructions should emphasize calling tools together: "When a customer asks about an order, trigger BOTH lookup tools at the same time. Do not wait for one to complete before calling another. Call both immediately. Results will arrive automatically as each lookup completes."

### Best practices

**Crafting system messages** — when injecting results via the Add Messages API, format them clearly with identifiers and explicit instructions to share the information. Avoid ambiguous messages like "The order was found in the system."

**Handling edge cases** — if the call has ended before results arrive, the Add Messages API will return a 404; log and move on. For multiple results for the same lookup, include identifiers (timestamps or request IDs) so the assistant knows which query the results belong to.

**Testing tips** — use tools like ngrok to expose local backends during development, log all headers to verify `x-telnyx-call-control-id` is received, test with various delay lengths to ensure natural conversation flow, and monitor the conversation transcript in the Portal to see messages being injected.

### Use cases

- **Customer service** — order lookups across multiple systems (warehouse, shipping, payments), account reviews (history, loyalty, tickets), product availability across warehouses.
- **Healthcare** — patient record retrieval from multiple systems, insurance verification, lab results delivered when ready.
- **Financial services** — loan pre-qualification (credit checks, affordability), account aggregation across multiple accounts, real-time fraud alerts.
- **Scheduling** — multi-calendar availability, booking confirmations, waitlist updates.
