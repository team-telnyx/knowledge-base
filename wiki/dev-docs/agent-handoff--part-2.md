---
title: Agent Handoff
summary: Agent handoff lets one Telnyx AI Assistant transfer control to other specialized
  assistants while preserving full conversation context. Use it to route by domain
  or task, choose a seamless single‑voice experience (Unified) or a conference‑style
  experience (Distinct), and scale a team of expert agents that collaborate in one
  conversation.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
  content_hash: e0189c3115b2b0ec8739b1ba3b782ea483de7a1205ddf866eaa083720296cb8c
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
  content_hash: 2c912fe20139394c5ab264f87da4acbca62e09fddc4a85f5e6875085d54ae351
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools/index
  content_hash: 736401f329fc4cb4c746ff8fd5d756c00fd3a780410ce9084deeeeb5f6531aef
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
  content_hash: 6431659cfc1080b05fae3580b16b26fe3b6f7b5202645fba44f5e79be2cd854a
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
  content_hash: 54ced37ff96d25d884594291a9b2182447838e85369a8d510fbb3b23c14c4680
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
  content_hash: c2cd727b5e21acc75cb8258b170d8409ca6cc11ac83c54f1e0ae8ddbb4c428f3
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
  content_hash: d95fae886becd4d35ad12b53c88e99212098bdbb49dc9b7d58794d25ec44d2da
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
  content_hash: 12dbefea69b6d1bf42a1127a6196161d990988bef7f3d2d9f76dbe17b9f37965
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
  content_hash: e32a9adc892a0661d42b14ffb4ac44c8d27673ed44659a0ed8b4b0cde6a43a8b
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
  content_hash: 092e6a9c0e06ea66330623a246ed29bafe161aee37d5fe70ac30e438f59b0843
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
  content_hash: 64ef9736186a641ad56c46a2b877e3213acdd746097cc5b16a68f96cd948f852
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
  content_hash: fdb8a55e2ef84acf968b46cb1f3050a2a2f38f85a26cf00e2962197f656855a1
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
  content_hash: ca821eba88d1eac534203355be68363e22a3aebbd50b291e3dc76c00a3911401
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
  content_hash: f6ca453d878e12ba5456d3869fdccb68f6c8dbfd59cc90f645354a9fd3c0f56f
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
  content_hash: 7c4a61c73ea31848ed9fee51d634e781b570a94428b81ac911ec4bb571d43c31
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
