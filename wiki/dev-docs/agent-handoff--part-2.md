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

*Part 2 of 2 — see also: [Part 1](agent-handoff--part-1.md)*

Agent handoff lets you route a live conversation from one AI assistant to another while preserving full context. Use it to orchestrate a team of specialized agents behind one seamless voice (Unified mode) or as distinct specialists (Distinct mode), with shared memory, tools, integrations, observability, and fine‑grained testing and rollout controls.

## Industry patterns (templates)
- Healthcare: Triage agent collects symptoms, then specialist (e.g., Cardiology) reviews and advises; insurance and appointment steps hand off as needed.
- E‑commerce: Browse/Recommend → Purchase/Checkout → Post‑sale Support; each agent optimized for its step.
- Financial services: Authentication → Account → Fraud; escalate based on risk signals.
- Customer support tiers: Tier 1 troubleshooting → Tier 2 advanced config → Tier 3 engineering; preserve full case history and actions tried.

## Related links
- See and edit tools and flows: [Workflow](workflow.md), [Tools Library](tools-library.md)
- Personalize and persist context: [Dynamic Variables](dynamic-variables.md), [Memory](memory.md)
- Handle transfers to people: [Voicemail Detection on Transfer](voicemail-detection-on-transfer.md)
- Make long calls proactive: [Scheduled Events](scheduled-events.md)
- Connect CRMs/ITSMs/dev tools/QA: [AI assistant integrations](ai-assistant-integrations.md)
- Choose and customize models: [Configure custom LLM providers for AI assistants](configure-custom-llm-providers-for-ai-assistants.md)
- Trace and manage prompts: [Observability](observability.md)
- QA and rollout safely: [Testing and Traffic Distribution for AI Assistants](testing-and-traffic-distribution-for-ai-assistants.md)
