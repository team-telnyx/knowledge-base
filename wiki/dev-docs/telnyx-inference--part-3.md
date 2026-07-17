---
title: Telnyx Inference
summary: Telnyx Inference is a developer platform for building AI-powered applications,
  centered on an OpenAI-compatible chat completions API and a managed Voice AI Assistant
  product. It offers open-source LLMs hosted on Telnyx GPU infrastructure, embeddings
  and RAG, fine-tuning, audio language models, function calling, structured output,
  and integrations with enterprise platforms. The Voice AI Assistant product supports
  dynamic variables, memory, agent handoff, conversation workflows, multi-participant
  calls, scheduled events, observability via Langfuse, and AI Insights for conversation
  analysis.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/client-side-tools
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights/index
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
- url: https://developers.telnyx.com/docs/inference/ai-insights/telnyx-managed-insights
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
- url: https://developers.telnyx.com/docs/inference/anthropic
- url: https://developers.telnyx.com/docs/inference/audio-language-models
- url: https://developers.telnyx.com/docs/inference/clusters
- url: https://developers.telnyx.com/docs/inference/crewai
- url: https://developers.telnyx.com/docs/inference/data-residency/index
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/feature-coverage
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/index
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/pricing
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/retention
- url: https://developers.telnyx.com/docs/inference/embedding-rag/conversation-history/searching
- url: https://developers.telnyx.com/docs/inference/embedding-rag/index
- url: https://developers.telnyx.com/docs/inference/embeddings/index
- url: https://developers.telnyx.com/docs/inference/fine-tuning
- url: https://developers.telnyx.com/docs/inference/functions
- url: https://developers.telnyx.com/docs/inference/getting-started/index
- url: https://developers.telnyx.com/docs/inference/integrations/index
- url: https://developers.telnyx.com/docs/inference/json-mode
- url: https://developers.telnyx.com/docs/inference/langchain-integration
- url: https://developers.telnyx.com/docs/inference/livekit
- url: https://developers.telnyx.com/docs/inference/llama-index
- url: https://developers.telnyx.com/docs/inference/missions/index
- url: https://developers.telnyx.com/docs/inference/models/index
- url: https://developers.telnyx.com/docs/inference/models/pricing
- url: https://developers.telnyx.com/docs/inference/models/regions
- url: https://developers.telnyx.com/docs/inference/openai
- url: https://developers.telnyx.com/docs/inference/pr-reviewer
- url: https://developers.telnyx.com/docs/inference/streaming-functions
updated_at: 2026-07-17T09:14:08Z
---

# Telnyx Inference

*Part 3 of 5 — see also: [Part 1](telnyx-inference--part-1.md), [Part 2](telnyx-inference--part-2.md), [Part 4](telnyx-inference--part-4.md), [Part 5](telnyx-inference--part-5.md)*

Telnyx Inference is a developer platform for building AI-powered applications, centered on an OpenAI-compatible chat completions API and a managed Voice AI Assistant product. It offers open-source LLMs hosted on Telnyx GPU infrastructure, embeddings and RAG, fine-tuning, audio language models, function calling, structured output, and integrations with enterprise platforms. The Voice AI Assistant product supports dynamic variables, memory, agent handoff, conversation workflows, multi-participant calls, scheduled events, observability via Langfuse, and AI Insights for conversation analysis.

## Memory

Memory enables your AI assistant to recall essential details from past conversations. Configure which conversations the assistant has memory access to via the `memory.conversation_query` field in the dynamic variables webhook response, using the same query language as the [List Conversations endpoint](https://developers.telnyx.com/api-reference/conversations/list-conversations). Optionally specify which insights to include via `memory.insight_query` (comma-delimited insight IDs).

Add custom metadata to conversations via the `conversation.metadata` field in the webhook response, then filter on it in future conversations using `metadata->your_custom_metadata=eq.your_custom_value`.

## Agent Handoff

Agent handoff enables your AI assistant to seamlessly transfer conversations to other specialized AI assistants while preserving full context. It is model-agnostic and works with any AI model supported by Telnyx.

### Unified vs Distinct Modes

- **Unified Mode (Default)**: All agents share the same context and voice. The user experiences one consistent agent. Use for a unified brand experience.
- **Distinct Mode**: Each assistant retains its voice configuration, creating a conference call experience. The user hears different voices as they're transferred. Use to highlight specialist expertise.

### Configuration

Add a Handoff tool in the Tools section, choose voice mode (Unified or Distinct), enter a display name, and select target assistants. Via API, include a `handoff` tool with `voice_mode` and `ai_assistants` array in the tools array.

### Best Practices

- Define clear, mutually exclusive responsibility boundaries to avoid handoff loops.
- Set maximum handoff limits per conversation with a failsafe to a human agent.
- Pass full conversation history, user information, collected data, and sentiment to the target agent.
- Use dynamic variables like `{{customer_name}}`, `{{account_id}}`, `{{previous_agent}}`, `{{handoff_reason}}`.
- Enable conversation memory for all agents in the handoff chain with consistent memory keys.

## Conversation Workflows

Conversation workflows let you turn a single AI Assistant into a guided, multi-step experience. A workflow is a directed graph stored on the AI Assistant as `conversation_flow` with two building blocks:

- **Nodes**: Conversation steps. A **prompt node** is an LLM-driven step with its own instructions, model override, and voice override. A **speak node** is a deterministic step that plays a fixed scripted message with no LLM turn.
- **Edges**: Transitions between nodes. Each edge has a condition: **LLM** (natural-language decision), **variable comparison** (deterministic), or **default** (fallback, required for speak nodes).

Node instructions can **append to** or **replace** the assistant's base instructions. Each node controls which of the assistant's tools the model can call. An edge can target another workflow node or another assistant entirely.

## Tools

### Built-in Tools

- **Hangup** — end the call at an appropriate time.
- **Handoff** — transfer to another specialized assistant.
- **Transfer** and **SIP Refer** — transfer or refer a call to named targets.
- **Send DTMF** — interact with legacy IVR systems.
- **Invite** — bring another participant into a multi-participant call.
- **Skip Turn** — stay silent for a turn in a multi-participant call.

### Webhook Tools

Webhook tools let your agent make API requests. Configure headers (with integration secrets), path, query, and body parameters. Reference dynamic variables in the webhook path or parameter descriptions.

### Async Webhooks and Add Messages API

Set `async: true` on a webhook tool so the assistant continues without waiting for a response. Your backend receives the `x-telnyx-call-control-id` header and can process the request asynchronously, then inject results back into the conversation via the [Add Messages API](https://developers.telnyx.com/api-reference/call-commands/add-messages-to-ai-assistant) (`POST /v2/calls/{call_control_id}/actions/ai_assistant_add_messages`). Message roles: `system` (instructions/context, recommended for async results), `user` (simulate user input), `assistant` (inject assistant responses).

Multiple async webhooks can run in parallel, with results arriving independently as each completes.

### Client-Side Tools

Client-side tools let your AI assistant invoke functions that run directly in the browser during WebRTC voice or chat conversations. They are available via the `@telnyx/ai-agent-lib` JavaScript/React library (version 0.5.0+). They are not available for SIP/phone-call-based conversations. Register tools at construction time or runtime via `agent.registerClientTool()` and `agent.unregisterClientTool()`. Each tool has a configurable Timeout in the Portal (default 5000 ms).

### Tools Library

The Tools Library lets you create tools in a shared library and assign them to any assistant. Navigate to **AI, Storage and Compute** > [AI Tools](https://portal.telnyx.com/#/ai/tools) to create shared tools. All tool types are supported, including webhook tools, client-side tools, handoff, transfer, and hangup tools.

## Integrations

Telnyx AI assistants integrate with leading enterprise platforms. The Integrations tab in the assistant builder offers a growing catalog organized by category:

- **Sales & CRM**: Salesforce, HubSpot, Pipedrive, Zoho CRM, Gong
- **Customer Support**: Zendesk, Intercom, ServiceNow, Jira, Jira Service Management
- **Engineering & Product**: GitHub, Jira, Linear
- **IT Operations**: ServiceNow, Jira Service Management, Microsoft Teams
- **Work Management**: Asana, Airtable, Notion
- **Knowledge & Documentation**: Confluence, Notion, SharePoint, GitHub
- **Communication & Collaboration**: Microsoft Teams, Outlook
- **File Storage & Productivity**: OneDrive, Outlook, SharePoint
- **HR & Recruiting**: Greenhouse, SAP SuccessFactors
- **Scheduling**: Calendly
- **Design & UX**: Figma
- **Accounting & Finance**: QuickBooks Online
- **E-commerce & Payments**: Shopify, Stripe
- **Testing & Evaluation**: Coval

To connect: open the assistant, go to the Integrations tab, add a platform, enter credentials, and enable the tools you need.

### MCP Servers

Configure an MCP Server with Telnyx and add it to an assistant. Telnyx automatically includes a `telnyx_conversation_id` with each MCP tool call in the `_meta` field. If the MCP server URL must be kept secret, store it as an integration secret.

### Importing Assistants

Import voice assistants from Vapi, ElevenLabs, or Retell via the portal or [API](https://developers.telnyx.com/api-reference/assistants/import-assistants-from-external-provider#import-assistants-from-external-provider). Instructions, greeting, LLM, voice, dynamic variables, tools, MCP servers, insights, and data retention settings are imported as-is. Knowledge bases are not imported by default. Telnyx creates placeholder integration secrets that you must resupply.

## Custom LLM Providers

Power your AI Assistant with any public OpenAI-compatible chat completions endpoint, including models hosted using AWS Bedrock, Azure OpenAI, Baseten, or open-source inference engines like vLLM and SGLang. In the Agent tab, check **Use Custom LLM**, input the endpoint URL as the Base URL (append `/openai/v1`), and create an Integration Secret with your API key.

Set `forward_metadata: true` on `external_llm` to include dynamic variables in requests as a top-level `extra_metadata` object.
