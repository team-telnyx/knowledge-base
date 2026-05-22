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

*Part 1 of 2 — see also: [Part 2](agent-handoff--part-2.md)*

Agent handoff lets one Telnyx AI Assistant transfer control to other specialized assistants while preserving full conversation context. Use it to route by domain or task, choose a seamless single‑voice experience (Unified) or a conference‑style experience (Distinct), and scale a team of expert agents that collaborate in one conversation.

## What agent handoff enables
Build a team of focused assistants that collaborate in a single conversation. The current assistant detects when a specialist is better suited, selects a target, transfers full context, and the target continues with awareness of prior turns. Handoff is model‑agnostic: each assistant can run on a different LLM, including native, third‑party, or a [custom LLM](configure-custom-llm-providers-for-ai-assistants.md).

## Lifecycle at a glance
- Detection: identify intent, domain, task, or criteria for handoff.
- Selection: choose the best target assistant from your configured list.
- Context transfer: send conversation history, user data, and intent.
- Transition: switch assistants in Unified (seamless) or Distinct (explicit) mode.
- Continuation: the target responds with full context.

## Unified vs Distinct voice modes
- Unified (default): one consistent voice and identity; transitions are transparent; best for a single brand persona.
- Distinct: each assistant uses its own voice; the handoff is announced (for example: “I’m transferring you to Sarah from billing”); similar to a conference handover where specialists introduce themselves.

## When to split into multiple assistants
Split when domains, tools, or response styles differ; when you need independent deployment, testing, and maintenance; or when expertise boundaries reduce prompt complexity. Keep as one assistant when tasks are tightly related, context switching would hurt quality, or the domain is narrow.

## Common patterns and use cases
- Multi‑domain support: triage → billing → technical support.
- Workflow segmentation: information gathering → processing → confirmation.
- Triage and routing: assess, then route to a specialist.
- Language switching: detect language and handoff to localized assistants.
- Escalation tiers: L1 → L2 → L3 engineering.
- Task segmentation: research/browse → purchase → post‑sale support.

## Designing reliable handoff triggers
- Triggers: intent phrases (e.g., “refund”), keywords, task completion, capability gaps, or sentiment thresholds (escalate when frustration is detected).
- Avoid loops: define clear ownership per assistant, track prior handoffs, set max handoffs per conversation, and route to a human after N transfers.
- Transitions: in Unified mode, continue without announcements; in Distinct mode, announce the transfer and let the specialist greet the user.
- Programmatic transfers: for PSTN/SIP call transfers outside AI‑to‑AI handoff, use the Transfer tool or the Telnyx Transfer Call API (see the public API reference).

## Preserving and passing context
- What to pass: user info (name, account/tier), conversation history, current intent/goals, collected data (order IDs, issue details), prior actions, and sentiment.
- Dynamic variables: standardize structured context across agents with placeholders such as {{customer_name}}, {{account_id}}, {{issue_type}}, {{previous_agent}}, {{handoff_reason}}. See [Dynamic Variables](dynamic-variables.md).
- Memory: enable conversation memory for all assistants, use consistent query logic (for example, “last 5 conversations for this phone number”), and reuse memory keys across agents. See [Memory](memory.md).

## Voice and multi‑participant considerations
- Distinct mode sounds like a conference with multiple voices; specialists may introduce themselves.
- In conversations that include multiple humans, add a Skip Turn tool so the assistant stays silent while people talk to each other, then resumes when addressed. See [Multi-Participant Voice AI Calls](multi-participant-voice-ai-calls.md).
- Improve name‑based turn‑taking with Keyterm Boost in transcription settings (e.g., add participant names, optionally via dynamic variables). See [Transcription Settings](transcription-settings.md).

## Configure handoff in the Portal
- Open your assistant in the Telnyx Portal and add a Handoff tool.
- Choose voice mode: Unified (seamless) or Distinct (conference‑style).
- Add one or more target assistants (name + assistant ID) and optional display names.
- Save; repeat to add additional specialists.
- Visualize end‑to‑end routing and tools in [Workflow](workflow.md).

## Configure handoff via API (what to send)
Use the Assistants API create/update endpoints (see the public API reference). In the assistant payload:
- Add a tool with type `handoff`.
- Under `handoff`, set `voice_mode` to `unified` or `distinct`.
- Provide `ai_assistants`: an array of targets with `id` and optional `name`.
- Update later by sending a new tools array containing the updated handoff configuration.

## Models and custom LLMs per assistant
- Each assistant in a handoff chain can use a different model (OpenAI, Anthropic, Meta, etc.).
- To use your own OpenAI‑compatible endpoint, configure an external LLM and, if needed, enable `forward_metadata` so dynamic variables are forwarded as `extra_metadata` for routing, logging, or personalization. See [Configure custom LLM providers for AI assistants](configure-custom-llm-providers-for-ai-assistants.md).

## Observability, testing, and rollout
- Enable Langfuse‑based tracing on each assistant to see LLM calls, tool executions, latency, tokens, and costs grouped by conversation. See [Observability](observability.md).
- Create versions, write tests, and route a percentage of traffic to new versions (target specific end‑user numbers/SIP URIs, canary by percentage, keep a main fallback). See [Testing and Traffic Distribution for AI Assistants](testing-and-traffic-distribution-for-ai-assistants.md).

## Working with async backends during handoff
- Don’t block the call while slow operations run. Mark webhook tools as async so the assistant keeps talking, and inject results later with the Add Messages API; the next agent in the chain inherits the updated context. See [Async Tools & Deferred Context](async-tools-deferred-context.md).

## Operational tips and adjacent features
- Tools Library: define webhook/transfer/handoff tools once and reuse across assistants to keep behavior consistent across your specialist team. See [Tools Library](tools-library.md).
- Scheduled callbacks: queue timed follow‑ups (calls or SMS) from any assistant; useful when a specialist isn’t immediately available. See [Scheduled Events](scheduled-events.md).
- Human transfers: when routing to people instead of AI, enable voicemail detection on transfer to avoid dead air and either stop the transfer or leave a message automatically. See [Voicemail Detection on Transfer](voicemail-detection-on-transfer.md).
- Quickstart and voice setup: create, test, and tune speaking/turn‑taking, TTS/STT providers, noise suppression, and background audio. See [Voice Assistant Quickstart](voice-assistant-quickstart.md) and [Transcription Settings](transcription-settings.md).
- Importing: migrate assistants from Vapi/ElevenLabs/Retell; tools and dynamic variables carry over. See [Importing Assistants from another Provider](importing-assistants-from-another-provider.md).

## Troubleshooting handoff
- Repeated loops: narrow ownership per assistant, add explicit “handle if in scope” instructions, track handoff history, and set a max handoff cap before escalating.
- Context loss: ensure every assistant has the dynamic variables webhook (if used), consistent memory queries, and shared conversation metadata; verify variables resolve (watch Portal logs) and that targets exist and are correct.
- Wrong specialist selection: refine triage instructions with examples, add a confirmation step (“Do you need billing help?”), and review transcripts to tune keywords/intent rules.
- Handoff not triggering: verify the Handoff tool exists on the source assistant, target IDs are valid, and triggers are explicitly spelled out in instructions; test with direct phrases.
