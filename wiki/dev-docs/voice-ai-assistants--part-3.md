---
title: Voice AI Assistants
summary: Telnyx Voice AI Assistants let you build, configure, and operate conversational
  voice agents entirely from the Mission Control Portal or via API. This page covers
  the no-code quickstart, supported language and transcription models, voice and noise-suppression
  settings, built-in and library tools, integrations, scheduled outbound events with
  retries, and programmatic voice control.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
updated_at: 2026-08-05T13:45:11Z
---

# Voice AI Assistants

*Part 3 of 6 — see also: [Part 1](voice-ai-assistants--part-1.md), [Part 2](voice-ai-assistants--part-2.md), [Part 4](voice-ai-assistants--part-4.md), [Part 5](voice-ai-assistants--part-5.md), [Part 6](voice-ai-assistants--part-6.md)*

Telnyx Voice AI Assistants let you build, configure, and operate conversational voice agents entirely from the Mission Control Portal or via API. This page covers the no-code quickstart, supported language and transcription models, voice and noise-suppression settings, built-in and library tools, integrations, scheduled outbound events with retries, and programmatic voice control.

## MMS Integration During Voice Calls

Your AI Assistant can receive and process MMS messages during live voice calls, enabling visual context and real-time image analysis.

### How it works

When a user sends an MMS message during an ongoing voice call, the agent can:

- Automatically detect incoming MMS messages.
- Access and analyze attached images using vision-capable Language Models (VLMs).
- Provide real-time responses based on visual content.
- Continue the voice conversation with enhanced context.

### Use cases

| Category | Use Case | Description |
| --- | --- | --- |
| **Visual Support** | Customer Service | Analyze product photos sent by customers |
|  | Technical Support | Review error screenshots or equipment photos |
|  | Healthcare | Examine medical documents or symptoms |
| **Document Verification** | Insurance Claims | Process claims with photo evidence |
|  | Identity Verification | Verify identity with document images |
|  | Compliance | Conduct compliance checks with visual documentation |
| **Real-time Analysis** | Quality Control | Perform inspections with photo submissions |
|  | Inventory Management | Manage inventory with visual confirmation |
|  | Damage Assessment | Assess damage with real-time photo analysis |

### Configuration

MMS integration requires:

1. **Messaging must be enabled** for your Voice AI Agent to receive MMS during calls.
2. **Vision-capable models required** — use one of the two supported vision models: `Groq/llama-4-maverick-17b-128e-instruct` or `OpenAI/gpt-4o` for image processing.
3. **Image processing** — the assistant can handle common image formats (JPEG, PNG, etc.).

### Best practices

- **Model selection:** Choose one of the two supported vision models when configuring your assistant.
- **Response timing:** The assistant will process images and respond within the voice call flow.
- **Image quality:** Higher resolution images provide better analysis results.
- **Context integration:** The assistant seamlessly combines visual and conversational context.

For detailed information about vision Language Models, see [Available Models](/docs/inference/models).

## Built-in Tools

Beyond the default Hangup tool, Telnyx provides several built-in tools that let the agent take real-world actions.

**Webhook.** The webhook tool lets the agent make API requests. You can configure headers (with integration secrets), along with path, query, and body parameters, and reference dynamic variables in the webhook path or parameter descriptions. After saving a webhook tool on your assistant, you can test it with sample data by clicking the play button icon on the tool.

**Handoff.** The handoff tool enables multiple assistants to support a user in a single conversation. By default, handoff is transparent to the user: assistants share the same context and voice, allowing a unified experience where a variety of tasks can be handled by a team of specialists. You can also toggle to distinct voice mode, where all assistants retain their voice configuration, providing the experience of a conference call with a team of assistants. See the [Agent Handoff guide](/docs/inference/ai-assistants/agent-handoff) for best practices and advanced configuration.

**Transfer and SIP Refer.** The transfer and SIP Refer tools let the agent transfer or refer a call to a list of named targets.

**Send DTMF.** The Send DTMF tool lets the agent interact with legacy IVR systems.

**Client-Side Tools.** Client-side tools let the assistant call functions that run directly in the browser during a WebRTC voice or chat conversation. This is useful for reading data the page already has, triggering UI actions, or calling APIs authenticated with the user's browser session. See the [Client-Side Tools guide](/docs/inference/ai-assistants/client-side-tools) for setup and implementation details.

## Tools Library

The Tools Library lets you create tools in a shared library and assign them to any assistant. Previously, tools were tied to individual assistants — if multiple assistants needed the same tool, you had to recreate it each time.

### Capabilities

- **Shared tools** — Create tools in a central library and assign them to any assistant.
- **Reduced duplication** — Eliminates recreating identical tools across assistants with similar workflows.
- **Centralized configuration** — Update a tool in one place and maintain consistency across assistants.
- **Faster deployment** — Speed up assistant creation using prebuilt tools from the library.

All tool types are supported in the library, including [webhook tools](/docs/inference/ai-assistants/async-tools), [client-side tools](/docs/inference/ai-assistants/client-side-tools), handoff, transfer, and hangup tools.

### Getting started

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Navigate to **AI, Storage and Compute** > **[AI Tools](https://portal.telnyx.com/#/ai/tools)**.
3. Click **Create New Tool** to add a new tool to the library.
4. When building or editing an assistant, assign tools from the library instead of creating them inline.

You can also assign library tools directly from the assistant builder.

### Migrating existing tools

Existing assistants with legacy (inline) tools continue to work. You can migrate legacy tools to the library at your own pace. Migration is optional — legacy tools remain functional, and you can migrate tools one at a time as needed.

## Model Context Protocol (MCP) Servers

You can [configure an MCP Server with Telnyx](https://portal.telnyx.com/#/ai/mcp-servers) and then add it to an assistant. If the URL for the server must be kept secret (because the server is not otherwise authenticated), you may store it securely as an integration secret with Telnyx.

When setting up MCP servers with Telnyx AI Assistants, Telnyx automatically includes a `telnyx_conversation_id` with each MCP tool call. If you are managing your own MCP Server, the `telnyx_conversation_id` can be used for tracking and controlling the flow of conversations within your applications. This is sent on the `_meta` field of MCP.

To receive the conversation ID at the start of a voice conversation, you have two options:

- For call control applications, the conversation ID is returned by the [Start AI Assistant command](/api-reference/call-commands/start-ai-assistant#start-ai-assistant).
- If you have configured a [dynamic variables webhook URL](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables), the conversation ID will be sent in this request payload at the start of a voice conversation.

The `telnyx_conversation_id` is set by the Telnyx platform, not by the AI agent, and as such is not susceptible to prompt injection attacks.

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "some_mcp_method",
  "params": {
    "_meta": {
      "progressToken": null,
      "telnyx_conversation_id": "123"
    }
  }
}
```

## Knowledge Bases

You can use the **Knowledge Bases** tab to enable your assistant to retrieve your custom context. Provide a name, then upload files or provide a URL.

## Insights

You can automatically run structured and unstructured analysis on every assistant conversation using the **Insights** tab. You can assign an **Insight Group** to your assistant, which can have one or more Insights. Insights can be reused across Groups, and Groups can be reused across Assistants. You can also configure a webhook URL to receive conversation insights after they are generated. See the [AI Insights documentation](https://developers.telnyx.com/docs/inference/ai-insights) for comprehensive guides on creating insights, using structured data schemas, organizing insight groups, configuring webhooks, and industry-specific use cases.

## Embeddable Widget

You can easily embed a customizable voice and chat widget on your frontend in the **Widget** tab.
