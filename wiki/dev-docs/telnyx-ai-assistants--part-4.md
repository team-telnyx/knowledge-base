---
title: Telnyx AI Assistants
summary: Telnyx AI Assistants are configurable voice and chat agents that combine
  large language models, text-to-speech, speech-to-text, and real-time tools into
  a single no-code or API-driven platform. Assistants can handle inbound and outbound
  calls, multi-participant conversations, scheduled outreach, structured conversation
  workflows, and integrations with enterprise systems — all managed from the Mission
  Control Portal or the Assistants API.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
updated_at: 2026-06-11T10:30:28Z
---

# Telnyx AI Assistants

*Part 4 of 4 — see also: [Part 1](telnyx-ai-assistants--part-1.md), [Part 2](telnyx-ai-assistants--part-2.md), [Part 3](telnyx-ai-assistants--part-3.md)*

Telnyx AI Assistants are configurable voice and chat agents that combine large language models, text-to-speech, speech-to-text, and real-time tools into a single no-code or API-driven platform. Assistants can handle inbound and outbound calls, multi-participant conversations, scheduled outreach, structured conversation workflows, and integrations with enterprise systems — all managed from the Mission Control Portal or the Assistants API.

## Version Testing and Traffic Distribution

### AI Tests

Create tests in the Portal under the [AI Tests page](https://portal.telnyx.com/#/ai/tests) to validate assistant behavior before going live. Define test names, select the assistant, set success criteria, and run tests. Review detailed results including conversation history.

### Assistant versions

Create new versions of an assistant with modified configurations (instructions, tools, voice, widget theme, etc.). Click **Save as New Version** and provide a descriptive name and notes.

### Traffic distribution

Control which live calls receive each version using ordered routing rules:

- **Target rules**: Match on end user target (phone number, SIP URI, or identifier) with operators `is one of`, `is not one of`, or `starts with`. Conditions in the same rule are AND-joined. The first matching rule wins.
- **Percentage splits**: Split matching traffic across versions for gradual rollouts. Percentages must add up to less than 100; remaining traffic goes to the main version as a built-in safety fallback.
- **Default rule**: Handles calls that match no target rule. Defaults to the main version; configure a custom default or percentage split as needed.

Use **Rollback** to clear all routing rules and return traffic to the main version.

### Automated evaluation with Coval

For automated evaluation at scale, Telnyx integrates with [Coval](https://www.coval.dev/) — a simulation and evaluation platform for voice and chat agents. Coval adds scenario simulation, CI/CD evaluations, production monitoring, and built-in metrics. Set up the integration on the assistant's Integrations tab.

## Embeddable Widget

Embed a customizable voice and chat widget on your frontend from the **Widget** tab. The widget supports appearance customization (dark/light theme) and can be enabled per assistant version for A/B testing.

## Programmatic Voice

Start an assistant as part of a programmatic voice application using the [Start AI Assistant](https://developers.telnyx.com/api-reference/call-commands/start-ai-assistant) call command.

## Importing Assistants

Assistants configured in Vapi or ElevenLabs can be [imported](https://developers.telnyx.com/docs/inference/ai-assistants/importing) as Telnyx AI Assistants in a single click.
