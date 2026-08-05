---
title: AI Assistant Configuration
summary: Telnyx AI assistants can be extended with enterprise integrations, tuned
  interruption behavior, persistent memory across conversations, and multi-participant
  call capabilities. This page covers the available integration catalog and connection
  workflow, interruption settings for turn-taking and non turn-taking transcription
  models, memory configuration via the dynamic variables webhook, and the Invite and
  Skip Turn tools used to coordinate multi-participant voice calls.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
- url: https://developers.telnyx.com/docs/inference/ai-assistants/interruption-settings
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
updated_at: 2026-08-05T13:44:48Z
---

# AI Assistant Configuration

*Part 6 of 6 — see also: [Part 1](ai-assistant-configuration--part-1.md), [Part 2](ai-assistant-configuration--part-2.md), [Part 3](ai-assistant-configuration--part-3.md), [Part 4](ai-assistant-configuration--part-4.md), [Part 5](ai-assistant-configuration--part-5.md)*

Telnyx AI assistants can be extended with enterprise integrations, tuned interruption behavior, persistent memory across conversations, and multi-participant call capabilities. This page covers the available integration catalog and connection workflow, interruption settings for turn-taking and non turn-taking transcription models, memory configuration via the dynamic variables webhook, and the Invite and Skip Turn tools used to coordinate multi-participant voice calls.

## Related resources

- [Voice Assistant Quickstart](voice-assistant-quickstart.md) — Learn how to create and configure AI assistants.
- [Workflow](workflow.md) — Visualize how your integrations and tools connect in your assistant's conversation flow.
- [Agent Handoff](https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff) — Enable multiple specialized assistants with integrations.
- [Dynamic Variables](dynamic-variables.md) — Pass integration-specific context to your assistant.
- [Assistants API Reference](/api-reference/assistants/list-assistants) — Programmatic assistant management.
- [Transcription Settings](transcription-settings.md) — Configure STT models and end-of-turn detection for turn-taking models like `deepgram/flux`.
- [Create an Assistant API Reference](/api-reference/assistants/create-an-assistant) — Full assistant configuration options including `interruption_settings`.
- [End-of-Turn Detection](/docs/voice/stt/websocket-streaming/parameters/end-of-turn) — Lower-level end-of-turn parameters for WebSocket STT streaming.
- [Integration Secrets](https://portal.telnyx.com/#/integration-secrets) — Securely store API keys and tokens.
- [AI Assistants Portal](https://portal.telnyx.com/#/ai/assistants) — Configure assistants and integrations.
- [Tools Library](tools-library.md) — Add reusable tools to your assistant.
- [Agent Observability](/docs/inference/ai-assistants/agent-observability) — Review production calls.
