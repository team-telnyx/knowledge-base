---
title: Agent Handoff
summary: Agent handoff lets one Telnyx AI Assistant transfer control to other specialized
  assistants while preserving full conversation context. Use it to route by domain
  or task, choose a seamless single‑voice experience (Unified) or a conference‑style
  experience (Distinct), and scale a team of expert agents that collaborate in one
  conversation.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
updated_at: 2026-05-20T08:28:33Z
---

# Agent Handoff

*Part 2 of 2 — see also: [Part 1](agent-handoff--part-1.md)*

Agent handoff lets one Telnyx AI Assistant transfer control to other specialized assistants while preserving full conversation context. Use it to route by domain or task, choose a seamless single‑voice experience (Unified) or a conference‑style experience (Distinct), and scale a team of expert agents that collaborate in one conversation.

## Best‑practice checklist
- Define crisp domains and escalation rules per assistant.
- Keep Unified mode for brand continuity; use Distinct mode to highlight expert voices.
- Pass structured context via dynamic variables and persist conversation state via memory.
- Combine async tools with message injection to keep conversations flowing.
- Turn on observability and test new versions behind targeted routing before broad rollout.

## References
- Assistants API (create/update): public API reference on developers.telnyx.com.
- Add Messages API (inject results): public API reference.
- Transfer Call API (programmatic PSTN/SIP transfer): public API reference.
- Related wiki pages: [Workflow](workflow.md), [Dynamic Variables](dynamic-variables.md), [Memory](memory.md), [Transcription Settings](transcription-settings.md), [Async Tools & Deferred Context](async-tools-deferred-context.md), [Tools Library](tools-library.md), [Observability](observability.md), [Testing and Traffic Distribution for AI Assistants](testing-and-traffic-distribution-for-ai-assistants.md), [Scheduled Events](scheduled-events.md), [Voicemail Detection on Transfer](voicemail-detection-on-transfer.md), [Configure custom LLM providers for AI assistants](configure-custom-llm-providers-for-ai-assistants.md), [Voice Assistant Quickstart](voice-assistant-quickstart.md), [Multi-Participant Voice AI Calls](multi-participant-voice-ai-calls.md), [Importing Assistants from another Provider](importing-assistants-from-another-provider.md).
