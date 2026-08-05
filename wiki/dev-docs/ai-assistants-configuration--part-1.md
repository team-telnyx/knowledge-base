---
title: AI Assistants Configuration
summary: Covers advanced configuration options for Telnyx AI assistants, including
  client-side tools, custom LLM providers, dynamic variables, webhook filler messages,
  and importing assistants from third-party providers.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/client-side-tools
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
- url: https://developers.telnyx.com/docs/inference/ai-assistants/filler-messages
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
updated_at: 2026-08-05T13:45:16Z
---

# AI Assistants Configuration

*Part 1 of 5 — see also: [Part 2](ai-assistants-configuration--part-2.md), [Part 3](ai-assistants-configuration--part-3.md), [Part 4](ai-assistants-configuration--part-4.md), [Part 5](ai-assistants-configuration--part-5.md)*

Covers advanced configuration options for Telnyx AI assistants, including client-side tools, custom LLM providers, dynamic variables, webhook filler messages, and importing assistants from third-party providers.

## Client-Side Tools

Client-side tools let your AI assistant invoke functions that run directly in the browser or client application during a voice or chat conversation. Unlike [webhook tools](async-tools-deferred-context.md) — which make HTTP requests to your backend — client-side tools execute JavaScript code on the client, with direct access to browser state, local data, and any API the page is authenticated to call.

### How they work

1. **You define a tool** in the [Portal](https://portal.telnyx.com/#/ai/assistants) with a name, description, and JSON Schema for parameters — the same way you configure other tool types.
2. **The assistant decides when to call it** based on the conversation context and the tool's description.
3. **Your client-side handler runs** in the browser, receiving the parsed arguments from the assistant.
4. **The return value is sent back** to the assistant so it can continue the conversation naturally.

This flow uses the Voice SDK Proxy WebSocket to relay tool invocations and results between the assistant and your client code — no HTTP webhook required.

Client-side tools are available for WebRTC-based conversations (voice and chat) using the `@telnyx/ai-agent-lib` JavaScript/React library. They are not available for SIP/phone-call-based conversations.

### When to use client-side tools

| Scenario | Client-side tool | Webhook tool |
| --- | --- | --- |
| Read data the page already has (shopping cart, user session) | ✅ |  |
| Trigger a UI action (open a modal, navigate, play media) | ✅ |  |
| Call an API authenticated with the user's browser session | ✅ |  |
| Query a backend database or internal service |  | ✅ |
| Send a notification to an external system |  | ✅ |
| Needs to work for phone/SIP calls |  | ✅ |

### Configure a client-side tool in the Portal

1. Open **AI Assistants** in the [Telnyx Portal](https://portal.telnyx.com/#/ai/assistants).
2. Select an assistant and scroll to the **Tools** section.
3. Click **Add Tool** and select **Client-Side Tool**.
4. Fill in the fields:

| Field | Description |
| --- | --- |
| **Name** | The tool name the assistant uses to call it. Must match the name you register in your client code. Only letters, numbers, underscores, and hyphens. |
| **Description** | Tell the assistant what the tool does and when to use it. The clearer the description, the better the assistant is at deciding when to invoke it. |
| **Parameters** | A JSON Schema object defining the tool's input parameters. Use the visual editor for simple schemas (strings, numbers, booleans, enums, arrays) or switch to **Advanced mode** for complex schemas with nested objects or custom keywords. |
| **Timeout (ms)** | How long the client has to execute the tool before a timeout error is returned to the assistant. Default: 5000 ms. This per-tool value is sent to the client and applied automatically — you do not need to configure it in code. |

5. Click **Create & Add to Assistant**.

You can also create client-side tools in the [Tools Library](tools-library.md) and share them across multiple assistants.

The **Parameters** schema uses the same JSON Schema format as webhook tool body parameters. The visual editor supports `string`, `number`, `integer`, `boolean`, `enum`, and array types. If your schema uses keywords the visual editor doesn't support (like `minimum`, `pattern`, or `default`), it will be displayed in **Advanced mode** as raw JSON to preserve those keywords.

### Implement client-side tool handlers

Install the Telnyx AI Agent library:

```
npm install @telnyx/ai-agent-lib
```

Client-side tools require `@telnyx/ai-agent-lib` version **0.5.0** or later.

#### Register tools at construction time

```
import { TelnyxAIAgent } from '@telnyx/ai-agent-lib';

const agent = new TelnyxAIAgent({
  agentId: 'your-agent-id',
  clientTools: {
    // The key must match the tool name configured in the Portal
    lookup_order: async (args) => {
      // args is typed as `unknown` — cast to your expected shape
      const { orderId } = args as { orderId: string };
      const response = await fetch(`/api/orders/${orderId}`);
      const order = await response.json();
      return { status: 'found', orderId: order.id, total: order.total };
    },

    get_cart: () => {
      // No parameters needed — return data the page already has
      return { itemCount: cart.items.length, items: cart.items };
    },

    open_chat_panel: () => {
      // Trigger a UI action
      setChatOpen(true);
      return { success: true };
    },
  },
  // Optional client-wide fallback timeout, used only for tools that have no
  // Timeout configured in the Portal. Each tool's Portal Timeout takes
  // precedence and is applied automatically. Default: 30000 ms.
  clientToolTimeoutMs: 15000,
});
```

#### Register tools at runtime

```
// Add a tool after construction
agent.registerClientTool('get_user_profile', () => {
  return { name: currentUser.name, email: currentUser.email };
});

// Remove a tool
agent.unregisterClientTool('get_user_profile');

// List registered tools
agent.getClientTools(); // ['lookup_order', 'get_cart']
```

#### Use with React

```
import { useClient } from '@telnyx/ai-agent-lib';

function ToolRegistration() {
  const client = useClient();

  useEffect(() => {
    client.registerClientTool('lookup_order', async (args) => {
      const { orderId } = args as { orderId: string };
      const response = await fetch(`/api/orders/${orderId}`);
      const order = await response.json();
      return { status: 'found', orderId: order.id, total: order.total };
    });

    return () => client.unregisterClientTool('lookup_order');
  }, [client]);

  return null;
}
```

#### Handler contract

```
type ClientSideToolHandler = (
  args: unknown,                  // parsed JSON arguments (or undefined if empty)
  context: ClientSideToolContext, // { callId, toolName, rawArguments }
) => unknown | Promise<unknown>;
```

- The return value is serialized and sent back as the tool output. Strings are sent verbatim; anything else is JSON-stringified.
- Handlers may be async. Each runs with its tool's **Timeout** configured in the Portal, falling back to `clientToolTimeoutMs` for tools that have none. If the handler exceeds it, a `{ "error": "timeout" }` output is returned to the assistant.
- The library handles the `call_id` round-trip — you don't need to manage that yourself.

### Error handling

The library always returns a result to the assistant so the conversation never hangs:

| Scenario | What happens |
| --- | --- |
| Unknown tool name | Safe error output `{ "error": "unknown_tool" }` |
| Invalid JSON arguments | Safe error output `{ "error": "invalid_arguments" }` |
| Handler throws or rejects | Safe error output `{ "error": "handler_error" }` |
| Handler exceeds timeout | Safe error output `{ "error": "timeout" }` |
| Disconnected before output sent | Output dropped, error event emitted |
| Duplicate `call_id` (re-delivery) | Ignored — tool is not executed twice |

Your handler should handle its own errors gracefully. If you want the assistant to know about a failure (e.g., an API returned 404), return an error object rather than throwing:

```
lookup_order: async (args) => {
  const { orderId } = args as { orderId: string };
  const response = await fetch(`/api/orders/${orderId}`);
  if (!response.ok) {
    return { error: 'order_not_found', orderId };
  }
  const order = await response.json();
  return { status: 'found', orderId: order.id, total: order.total };
},
```

### Observe tool lifecycle events

```
agent.on('client.tool.invoked', ({ callId, toolName }) => {
  console.log(`Tool ${toolName} invoked (${callId})`);
});

agent.on('client.tool.completed', ({ callId, toolName, isError }) => {
  console.log(`Tool ${toolName} completed, error=${isError}`);
});

agent.on('client.tool.error', ({ callId, toolName, reason }) => {
  console.warn(`Tool ${toolName} failed: ${reason}`);
});
```

Tool arguments and outputs are **never logged** — they may contain customer data. Only safe correlation fields (`callId`, tool name) appear in debug logs.

### Client-side tools vs. webhook tools

| Feature | Client-side tools | Webhook tools |
| --- | --- | --- |
| Execution location | Browser/client | Your backend server |
| Requires public endpoint | No | Yes |
| Works with phone/SIP calls | No | Yes |
| Works with WebRTC (voice/chat) | Yes | Yes |
| Can access browser state | Yes | No |
| Latency | Minimal (no HTTP round-trip) | Network-dependent |
| Can be tested in the Portal | No | Yes (test button) |

### Use cases

- **E-commerce**: Look up cart contents, check order status from the browser session, apply a promo code
- **Scheduling**: Read the user's calendar from the page, open a booking modal
- **Customer support**: Fetch user details from the client session, trigger a screen share
- **IoT dashboards**: Read device state from the dashboard, toggle a device on/off
