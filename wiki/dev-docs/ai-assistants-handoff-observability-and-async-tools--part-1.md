---
title: 'AI Assistants: Handoff, Observability, and Async Tools'
summary: Telnyx AI assistants support advanced conversation patterns including agent
  handoff between specialized assistants, Langfuse-based observability for tracing
  LLM calls and tool executions, and async webhook tools combined with the Add Messages
  API for long-running operations that inject results back into active conversations
  without blocking the user.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools/index
updated_at: 2026-08-05T13:43:49Z
---

# AI Assistants: Handoff, Observability, and Async Tools

*Part 1 of 4 — see also: [Part 2](ai-assistants-handoff-observability-and-async-tools--part-2.md), [Part 3](ai-assistants-handoff-observability-and-async-tools--part-3.md), [Part 4](ai-assistants-handoff-observability-and-async-tools--part-4.md)*

Telnyx AI assistants support advanced conversation patterns including agent handoff between specialized assistants, Langfuse-based observability for tracing LLM calls and tool executions, and async webhook tools combined with the Add Messages API for long-running operations that inject results back into active conversations without blocking the user.

## Overview

Telnyx AI assistants can be composed into sophisticated multi-agent systems and instrumented for production observability. Three capabilities work together to support real-world conversational AI:

- **Agent handoff** lets one assistant transfer a conversation to another specialized assistant while preserving full context, with either a seamless (Unified) or conference-call-style (Distinct) voice experience.
- **Observability** connects an assistant to [Langfuse](https://langfuse.com) so every LLM call, tool execution, and conversation turn is traced for debugging, cost tracking, and quality evaluation.
- **Async tools and deferred context** let webhook tools run in the background while the assistant keeps talking, with results injected back into the active conversation via the Add Messages API.

## Agent Handoff

Agent handoff enables an AI assistant to transfer conversations to other specialized AI assistants while preserving full context. This allows you to build a team of expert agents, each focused on specific domains or tasks, working together in a single conversation. Handoff is model-agnostic and works with any AI model supported by Telnyx (OpenAI GPT, Meta Llama, Anthropic Claude, Qwen, etc.); each agent in the chain can use a different model.

### How handoff works

The handoff lifecycle follows these steps:

1. **Detection** — the current agent identifies that another agent would be better suited to the user's request.
2. **Agent selection** — the system determines which specialist should receive the handoff.
3. **Context transfer** — full conversation history, user data, and relevant context are transferred to the target agent.
4. **Transition** — the handoff occurs, either seamlessly (Unified) or explicitly (Distinct).
5. **Continuation** — the target agent continues the conversation with full context awareness.

### Unified vs Distinct modes

**Unified mode (default)** — assistants share the same context and voice, creating a seamless experience where specialists work behind the scenes. The user experiences one consistent agent.

- Same voice across all agents
- Transparent transition (user doesn't notice the handoff)
- Shared context (full conversation history available to all agents)
- Best when you want a unified brand experience

**Distinct mode** — each assistant retains its own voice configuration, creating a conference-call experience with multiple distinct voices.

- Individual voices per agent
- Explicit transition (user hears "I'm transferring you to [specialist name]")
- Shared context (full conversation history available to all agents)
- Best when you want to highlight specialist expertise

### Common use cases

- Multi-domain support (technical, billing, sales) with full context
- Workflow automation (information gathering → processing → confirmation)
- Triage and routing (assessment agent routes to the right specialist)
- Language switching (detection agent hands off to a language-specific agent)
- Escalation tiers (Level 1 → Level 2 → Level 3)
- Task segmentation (browse → purchase → post-sale support)

### Best practices

**Agent architecture design** — split into multiple agents when domains require significantly different knowledge bases, agents need different tools, response patterns differ substantially, or you want to independently update capabilities. Keep as one agent when tasks are closely related, context switching would reduce quality, the user benefits from continuity, or the domain is narrow and well-defined.

Specialization patterns include by domain, by task, by customer segment, by complexity, and by channel.

**Handoff trigger design** — define explicit triggers (intent-based, keyword-based, task completion, capability-based, sentiment-based) and prevent handoff loops by defining clear responsibility boundaries, tracking handoff history, setting maximum handoff limits, and designing a failsafe that routes to a human after N handoffs.

**Context preservation** — pass user information, conversation history, user intent, collected data, agent actions, and sentiment. Use [Dynamic Variables](dynamic-variables.md) such as `{{customer_name}}`, `{{account_id}}`, `{{customer_tier}}`, `{{issue_type}}`, `{{priority_level}}`, `{{previous_agent}}`, and `{{handoff_reason}}`. Configure [Memory](memory.md) consistently across all agents in the handoff chain.

### Portal configuration

1. Navigate to AI Assistants in the [Telnyx Portal](https://portal.telnyx.com/#/ai/assistants).
2. In the Tools section, add a Handoff tool.
3. Choose your voice mode: Unified (seamless) or Distinct (conference-call style).
4. Enter a display name for the target assistant.
5. Select the target assistant from the dropdown menu.
6. Click the plus (+) button to add additional target assistants if needed.
7. Save your configuration.

### API implementation

Create an assistant with a Handoff tool by including target assistant IDs in the `tools` array:

```
curl -L 'https://api.telnyx.com/v2/ai/assistants' \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -H 'Authorization: Bearer <TOKEN>' \
  --data-raw '{
    "name": "Customer Support Triage Agent",
    "instructions": "You are a triage agent for customer support. Listen to customer needs and determine if they need technical support, billing help, or sales assistance. Handoff to the appropriate specialist when needed.",
    "model": "moonshotai/Kimi-K2.5",
    "tools": [
      {
        "type": "handoff",
        "handoff": {
          "voice_mode": "unified",
          "ai_assistants": [
            {"name": "Technical Support", "id": "asst_tech_abc123"},
            {"name": "Billing Support", "id": "asst_billing_def456"},
            {"name": "Sales", "id": "asst_sales_ghi789"}
          ]
        }
      }
    ]
  }'
```

To enable Distinct mode, set `"voice_mode": "distinct"` in the handoff configuration. To update handoff settings on an existing assistant, send a `PATCH` request to `/v2/ai/assistants/{assistant_id}` with the new `tools` array.

### Troubleshooting

- **Handoff loops** — define clear, mutually exclusive responsibility boundaries; document what each agent handles; add explicit instructions like "Only handoff if the request is truly outside your domain".
- **Context loss after handoff** — configure the dynamic variables webhook for all agents in the chain, ensure all agents use the same conversation query logic, use consistent conversation metadata, and verify dynamic variables are passed to target agents.
- **Incorrect agent selection** — refine triage agent instructions with specific examples, add a confirmation step, and review conversation logs for misrouting patterns.
- **Handoff doesn't trigger** — verify the handoff tool is added, check target assistant IDs are valid, add explicit handoff triggers in instructions, and test with direct requests.
