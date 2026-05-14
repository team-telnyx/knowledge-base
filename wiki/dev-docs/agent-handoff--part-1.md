---
title: Agent Handoff
summary: Agent handoff lets you route a live conversation from one AI assistant to
  another while preserving full context. Use it to orchestrate a team of specialized
  agents behind one seamless voice (Unified mode) or as distinct specialists (Distinct
  mode), with shared memory, tools, integrations, observability, and fine‑grained
  testing and rollout controls.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
- url: https://developers.telnyx.com/docs/inference/ai-insights/creating-insights
- url: https://developers.telnyx.com/docs/inference/ai-insights/insight-groups
- url: https://developers.telnyx.com/docs/inference/ai-insights/structured-insights
- url: https://developers.telnyx.com/docs/inference/ai-insights/use-cases
- url: https://developers.telnyx.com/docs/inference/ai-outfit-recommender
- url: https://developers.telnyx.com/docs/inference/clusters
- url: https://developers.telnyx.com/docs/inference/crewai
- url: https://developers.telnyx.com/docs/inference/embeddings
- url: https://developers.telnyx.com/docs/inference/functions
- url: https://developers.telnyx.com/docs/inference/getting-started
- url: https://developers.telnyx.com/docs/inference/integrations
- url: https://developers.telnyx.com/docs/inference/langchain-integration
- url: https://developers.telnyx.com/docs/inference/livekit
- url: https://developers.telnyx.com/docs/inference/llama-index
- url: https://developers.telnyx.com/docs/inference/missions
- url: https://developers.telnyx.com/docs/inference/models
- url: https://developers.telnyx.com/docs/inference/models/pricing
- url: https://developers.telnyx.com/docs/inference/models/regions
- url: https://developers.telnyx.com/docs/inference/openai
- url: https://developers.telnyx.com/docs/inference/pr-reviewer
- url: https://developers.telnyx.com/docs/inference/streaming-functions
updated_at: 2026-05-14T09:52:01Z
---

# Agent Handoff

*Part 1 of 2 — see also: [Part 2](agent-handoff--part-2.md)*

Agent handoff lets you route a live conversation from one AI assistant to another while preserving full context. Use it to orchestrate a team of specialized agents behind one seamless voice (Unified mode) or as distinct specialists (Distinct mode), with shared memory, tools, integrations, observability, and fine‑grained testing and rollout controls.

## What agent handoff enables
Agent handoff is a model‑agnostic capability that works with any LLM supported by Telnyx (OpenAI, Anthropic, Meta Llama, Qwen, Moonshot, and more). Instead of one mega‑agent, you compose a team of focused assistants and route to the best specialist at each step. Benefits:
- Specialist routing with higher accuracy per domain
- Preserved context across agents (no repetition)
- Lower complexity and easier maintenance
- Scalable architecture — add specialists over time

## How the lifecycle works
1) Detection: the active assistant recognizes another agent is better suited for the task. 2) Agent selection: pick the target specialist. 3) Context transfer: pass full history, user data, variables, and metadata. 4) Transition: Unified (seamless) or Distinct (explicit) modes. 5) Continuation: the target agent responds with full context.

## Unified vs Distinct handoff modes
- Unified (default): shared voice configuration; transitions are transparent to the user. Use for one brand voice across specialists.
- Distinct: each assistant keeps its own voice; users hear, e.g., “I’m transferring you to Sarah from billing.” Use to highlight expert roles.
Both modes share full conversation context.

## When to split assistants vs keep one
Split into multiple assistants when domains, tools, or response patterns differ, or you need independent versioning. Keep one when tasks are tightly related, context switching would hurt quality, or the domain is narrow.

## Handoff trigger design
- Triggers: intent keywords (e.g., “refund”), capability limits (beyond triage scope), task completion (handoff to processing), sentiment (frustration → senior support), or language detection.
- Avoid loops: define clear ownership, track handoff history, cap handoffs per conversation, and fall back to a human.
- Phrase transitions: Unified — continue naturally; Distinct — announce the transfer and introduce the specialist.

## Passing context reliably
Include: user identifiers/tier, intent and goals, prior actions tried, collected data (order IDs, symptoms), conversation history, and sentiment.
- Dynamic variables: template instructions/greetings/tools with {{variable_name}}; set via outbound API, custom SIP headers (X‑Header → {{header_name}}), a dynamic variables webhook, or assistant‑level defaults. See [Dynamic Variables](dynamic-variables.md).
- Memory: configure which past conversations and which insight results are accessible at start (via webhook response: conversation_query, optional insight_query). Use consistent metadata keys across agents. See [Memory](memory.md).
- External LLMs: if using a custom OpenAI‑compatible gateway, enable forward_metadata so Telnyx includes extra_metadata (e.g., customer_name, telnyx_agent_target, telnyx_end_user_target) in the request. See [Configure custom LLM providers for AI assistants](configure-custom-llm-providers-for-ai-assistants.md).

## Voice, telephony, and user experience
- Unified mode keeps one voice across specialists; Distinct creates a conference‑style handoff with unique voices per agent.
- For handoffs to people (not AI), use Transfer or SIP Refer tools and optionally enable voicemail handling to avoid dead air. See [Voicemail Detection on Transfer](voicemail-detection-on-transfer.md).
- For calls with multiple humans, design turn‑taking; add Skip Turn rules and Keyterm Boost for names. See [Multi-Participant Voice AI Calls](multi-participant-voice-ai-calls.md) and [Transcription Settings](transcription-settings.md).

## Configure in the Portal
In the assistant’s Tools section, add a Handoff tool, choose voice_mode (unified or distinct), give each target assistant a display name, pick target assistants from the dropdown, and save. You can add multiple targets for one source assistant.

## Configure via API (fields to set)
Create or update an assistant with a tools[] item:
- type: "handoff"
- handoff.voice_mode: "unified" or "distinct"
- handoff.ai_assistants: list of { name, id } for each target
Each linked assistant can use a different LLM or voice.

## Working with tools, async ops, and mid‑call updates
- Combine handoff with webhooks, Transfer, SIP Refer, Send DTMF, and more — reuse shared tools via [Tools Library](tools-library.md).
- Long‑running backends: mark webhook tools async so the agent keeps talking while work runs, then inject results mid‑conversation with Add Messages (POST /v2/calls/{call_control_id}/actions/ai_assistant_add_messages). Your webhook receives x‑telnyx-call-control-id to target the active call. See [Async Tools & Deferred Context](async-tools-deferred-context.md).
- Visualize and tune flows in [Workflow](workflow.md).

## Using enterprise integrations and knowledge
- Connect Salesforce, ServiceNow, Jira, HubSpot, Zendesk, Intercom, GitHub, Greenhouse, and Coval per assistant. Each specialist can have its own connected tools. See [AI assistant integrations](ai-assistant-integrations.md).
- Add knowledge bases for retrieval; or ground LLMs with embeddings and clusters for analysis where relevant (see Embeddings/Clusters docs in the analytics section of the wiki).

## Models and custom LLMs
Agent handoff is model‑agnostic; each assistant can use a different model suited to its task. You can also BYO OpenAI‑compatible endpoint (e.g., Azure, Baseten), store credentials as integration secrets, and optionally forward_metadata for routing/personalization. See [Configure custom LLM providers for AI assistants](configure-custom-llm-providers-for-ai-assistants.md).

## Observability and prompt ops
Enable Langfuse tracing per assistant via observability_settings (status enabled, host, secret_key_ref, public_key_ref stored as Integration Secrets). Traces are grouped by conversation_id, capturing generations and tool calls. You can link a Langfuse‑managed prompt by name + version or label, and optionally sync assistant instructions back to Langfuse (prompt_sync). See [Observability](observability.md).

## Testing, versions, and traffic routing
- Build tests and success criteria; iterate safely before production.
- Create assistant versions and route live calls by ordered rules using the end user target (phone/SIP) — send all traffic to a version or split by percentage for canarying; keep main as fallback. See [Testing and Traffic Distribution for AI Assistants](testing-and-traffic-distribution-for-ai-assistants.md).

## Troubleshooting
- Handoff loops: clarify ownership, add explicit “only handoff if outside domain,” cap handoffs, and add human fallback.
- Context loss: ensure dynamic variables webhook is configured across agents; use consistent memory queries/metadata; verify variables resolve within 1s timeout; confirm default fallbacks.
- Wrong specialist selected: refine triage instructions with examples; add a confirmation step (“Do you need billing help?”); analyze transcripts and retune triggers.
- Handoff won’t trigger: verify a Handoff tool exists with correct target assistant IDs; make triggers explicit in instructions; test direct intents.
- Observability not logging: check status enabled, secret refs exist, and host matches Langfuse project.

## Security, performance, and reliability notes
- Store API keys and Langfuse creds in Integration Secrets; rotate regularly.
- Limit integration scopes and use sandbox orgs for testing.
- Observability is async; minimal overhead. Ensure any self‑hosted endpoints are reachable.
- Async webhooks should ACK fast and do work out‑of‑band; there is no enforced backend timeout before you inject results.
