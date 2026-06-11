---
title: AI Assistants
summary: Telnyx AI Assistants are configurable voice and text agents that support
  multi-agent handoff, dynamic variables, persistent memory, async tool execution,
  enterprise integrations, custom LLM providers, Langfuse observability, and migration
  from other providers — all orchestrated through the Mission Control Portal or API.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
  content_hash: 70a4981634a6392849db64eb9505dc98ed11f2c816e1a5a90809b02d509e14b1
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
  content_hash: fef9a26ab4abb9421515d4444216948ad9d6348ed5eebc66c50729e9ab27e71a
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools/index
  content_hash: 4305d6ceba22801446c835423e7dad2029e48c5d186c3358bde90d33d9cf2d90
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
  content_hash: 26757cd4f78fd56c2320d158d13becea98fbb06936445b505a2075cdd609a686
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
  content_hash: 3d2eeb67ed78ad9cf2e5fd0a52e0b6b017bf273d08335395bf9df845a2f4bacf
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
  content_hash: c1af4766c041fd4740d0e4a329bb36fb52a550bc0e8b28684ba40e1aa0274ac4
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
  content_hash: 4441f80ea6c53c4f58838df0f99b66bd3cc4779b2c8415f970c5a4d17dab9d77
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
  content_hash: c7ecb160d4f9b143af3c70bcb729def8e69d59ff8b3f872b15654bf3b3971030
updated_at: 2026-06-11T10:29:30Z
---

# AI Assistants

*Part 1 of 4 — see also: [Part 2](ai-assistants--part-2.md), [Part 3](ai-assistants--part-3.md), [Part 4](ai-assistants--part-4.md)*

Telnyx AI Assistants are configurable voice and text agents that support multi-agent handoff, dynamic variables, persistent memory, async tool execution, enterprise integrations, custom LLM providers, Langfuse observability, and migration from other providers — all orchestrated through the Mission Control Portal or API.

## Core Concepts

Telnyx AI Assistants power conversational AI over voice and messaging channels. Each assistant is defined by instructions, a model, a voice, tools, and optional integrations. Assistants natively support Telnyx Voice and Messaging APIs, meaning the same assistant can operate seamlessly across phone calls, web calls, and SMS.

Key capabilities include:

- **Agent handoff** — Transfer conversations between specialised agents while preserving full context.
- **Dynamic variables** — Template placeholders (`{{variable_name}}`) resolved at conversation start for personalisation.
- **Memory** — Recall details from past conversations using flexible query configuration.
- **Async tools** — Trigger long-running operations without blocking the conversation, then inject results when ready.
- **Integrations** — Connect assistants to enterprise platforms (Salesforce, Jira, Zendesk, etc.).
- **Custom LLM providers** — Use any OpenAI-compatible chat completions endpoint (Azure, Baseten, vLLM, etc.).
- **Observability** — Trace every LLM call and tool execution through Langfuse.
- **Importing** — Migrate existing assistants from Vapi, ElevenLabs, or Retell.

## Agent Handoff

Agent handoff enables an AI assistant to seamlessly transfer conversations to other specialised assistants while preserving full context. This lets you build a team of expert agents — each focused on a specific domain — that collaborate within a single conversation. Handoff is model-agnostic and works with any supported model (OpenAI, Llama, Claude, Qwen, etc.); each agent in the chain can use a different model.

### Handoff lifecycle

1. **Detection** — The current agent identifies that another agent would be better suited.
2. **Agent selection** — The system determines the target specialist.
3. **Context transfer** — Full conversation history, user data, and relevant context are transferred.
4. **Transition** — The handoff occurs (seamlessly or explicitly, depending on mode).
5. **Continuation** — The target agent continues with full context awareness.

### Unified vs. Distinct modes

| Mode | Voice | Transition | Use case |
|---|---|---|---|
| **Unified** (default) | All agents share the same voice | Transparent — user notices nothing | Unified brand experience |
| **Distinct** | Each agent retains its own voice | Explicit — "I'm transferring you to…" | Highlighting specialist expertise |

Both modes share full conversation history across agents.

### Common handoff patterns

- **Multi-domain support** — Transfer between technical support, billing, and sales.
- **Workflow automation** — Information gathering → processing → confirmation.
- **Triage and routing** — Assessment agent evaluates needs, then routes to a specialist.
- **Escalation tiers** — Level 1 → Level 2 → Level 3 support.
- **Language switching** — Detection agent identifies language, hands off to language-specific agent.
- **Task segmentation** — Browse → Purchase → Post-sale support.

### Designing handoff triggers

Define explicit triggers to control when handoffs occur:

- **Intent-based** — "I need to talk to billing" → Billing agent.
- **Keyword-based** — User mentions "refund" → Billing agent.
- **Task completion** — Information gathered → Processing agent.
- **Capability-based** — Technical question beyond triage scope → Specialist.
- **Sentiment-based** — Frustrated customer → Senior support agent.

To avoid handoff loops (agents endlessly transferring to each other):

- Define clear, mutually exclusive responsibility boundaries.
- Implement handoff history tracking.
- Set maximum handoff limits per conversation.
- Design a failsafe that routes to a human agent after N handoffs.

### Portal configuration

1. Navigate to your AI Assistants in the [Telnyx Portal](https://portal.telnyx.com/#/ai/assistants).
2. In the **Tools** section, add a **Handoff** tool.
3. Choose voice mode: **Unified** or **Distinct**.
4. Enter a display name and select the target assistant from the dropdown.
5. Click the plus (+) button to add additional targets.
6. Save.

### API configuration

Include the Handoff tool in the `tools` array when creating or updating an assistant:

```bash
curl -L 'https://api.telnyx.com/v2/ai/assistants' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer <TOKEN>' \
  --data-raw '{
    "name": "Customer Support Triage Agent",
    "instructions": "You are a triage agent. Hand off to the appropriate specialist.",
    "model": "moonshotai/Kimi-K2.5",
    "tools": [
      {
        "type": "handoff",
        "handoff": {
          "voice_mode": "unified",
          "ai_assistants": [
            { "name": "Technical Support", "id": "asst_tech_abc123" },
            { "name": "Billing Support", "id": "asst_billing_def456" },
            { "name": "Sales", "id": "asst_sales_ghi789" }
          ]
        }
      }
    ]
  }'
```

For **Distinct** mode, set `"voice_mode": "distinct"`. To update handoff settings on an existing assistant, send a `PATCH` request to `/v2/ai/assistants/{assistant_id}` with the updated `tools` array.
