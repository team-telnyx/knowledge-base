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
  content_hash: 1ae007d98f0a079c6d9fa1acec7fd9203c2af7ca66d212171ca711e3da94d0c7
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
  content_hash: d07570a4fd30575a9f261a3f4988a2208d3115a79d4b0278f337f6a791606a6b
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
  content_hash: dc746a7ef6ef062d69a462a97a0c854a29da9576afc690ef62164b2ffecfcaf8
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
  content_hash: 97d3c9a314e001171d8cdac0f6a5707f088237e0e32561470fc8a92acbfdf55c
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
  content_hash: 155c354770eb16a9fe21e6eb194f7391f2ece82729736cef4540e5a28ee21ca4
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
  content_hash: 1ea79c8dd0f948970ff36ae3e9de9dd2efaf764f85c57429bb3366a97a0eb55b
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
  content_hash: 1a351e40f03eb9e9387cc17956573eb2a3423d73dde019f2ec3879f1bcc72dd1
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
  content_hash: 69f833223aa236218e653b4f8fd0f4a0cd8aa0aecf5872dfe647ef741dca081f
updated_at: 2026-06-11T10:30:28Z
---

# Telnyx AI Assistants

*Part 2 of 4 — see also: [Part 1](telnyx-ai-assistants--part-1.md), [Part 3](telnyx-ai-assistants--part-3.md), [Part 4](telnyx-ai-assistants--part-4.md)*

Telnyx AI Assistants are configurable voice and chat agents that combine large language models, text-to-speech, speech-to-text, and real-time tools into a single no-code or API-driven platform. Assistants can handle inbound and outbound calls, multi-participant conversations, scheduled outreach, structured conversation workflows, and integrations with enterprise systems — all managed from the Mission Control Portal or the Assistants API.

## Multi-Participant Calls

Multi-participant Voice AI calls let an assistant bring another person into an active call, track who is speaking, and continue using its configured tools. Use this for scheduling meetings, connecting customers with specialists, or coordinating between multiple callers.

### How it works

The call starts like any other voice assistant call. When needed, the assistant invokes an **Invite** tool to bring another participant in. Once joined, the assistant can:

- Distinguish between the main user and invited participants.
- Respond to either participant when appropriate.
- Stay silent when participants talk to each other (via Skip Turn).
- Use all configured tools, memory, dynamic variables, and integrations.

### Invite tool

1. Open the assistant in the Portal and go to **Tools**.
2. Add an **Invite** tool.
3. Configure the target phone number or SIP URI.
4. Save.

When the assistant decides another person should join, it calls the Invite tool and receives a `Participant joined` response.

### Multi-participant instructions

Add instructions that tell the assistant how to behave with multiple people:

```
You are Amber, a voice assistant helping coordinate a multi-participant call.

The call may include the main user and one or more invited participants. Pay close attention to who is speaking and who they are addressing.

When the main user asks you to invite someone, use the Invite tool. After the participant joins, briefly confirm that they joined, then let the participants talk.

If the participants are talking to each other and are not addressing you, use the Skip Turn tool and remain silent.

If someone addresses you directly, respond normally. You can use any of your configured tools to help complete the task.
```

### Skip Turn tool

The **Skip Turn** tool lets the assistant intentionally remain silent for a turn. Add it so the assistant can:

- Stay silent while invited participants talk to the main user.
- Avoid responding to side conversations.
- Wait until someone directly addresses it.
- Let humans confirm details before the assistant takes action.

Skip Turn does not end the call or disable the assistant — it only suppresses the response for that turn.

For name-based Skip Turn rules, add participant names to **Keyterm Boost** on the **Voice** tab to improve transcription accuracy. Keyterm Boost accepts a comma-separated list (e.g. `Telnyx,Amber,Enzo`) and supports dynamic variables (e.g. `Telnyx,{{participant_names}}`).

### Using other tools during the call

After a participant joins, the assistant retains full capabilities — calling APIs, looking up information, scheduling meetings, updating records, sending messages, and more. The assistant can combine tools with turn-taking logic (e.g. check availability, propose a time, stay silent while participants confirm, then book).

### Best practices

- **Be explicit about when to speak**: Give the assistant clear turn-taking rules (e.g. "If James and Enzo are speaking directly to each other, use Skip Turn and stay silent. Only respond when someone addresses you by name or asks you to take an action.").
- **Review calls in Conversation History**: Inspect transcripts, audio, tool calls, and tool responses — especially useful for tuning Skip Turn instructions.

## Conversation Workflows

Workflows turn a single assistant into a guided, multi-step experience. Instead of one prompt handling every part of a conversation, you design a directed graph of conversation steps with conditional routing between them. Use workflows for intake, qualification, booking, verification, escalation, or support triage.

### Building blocks

- **Nodes** — Conversation steps. A **prompt node** is LLM-driven with its own instructions, model, voice, and tool settings. A **speak node** plays a fixed scripted message verbatim (no model turn) and then advances along its required default edge.
- **Edges** — Transitions between nodes (or from a node to another assistant). Each edge has a condition: **LLM** (natural-language), **variable comparison** (deterministic), or **default** (fallback).

When a conversation starts, Telnyx begins at the workflow's start node. After the assistant responds, outgoing edges are evaluated. If a condition matches, the conversation moves to the target. If no condition matches, the conversation stays on the current node (except speak nodes, which always advance).

### Node configuration

- **Name**: Short, descriptive (e.g. `Greeting & Identify Intent`, `Answer FAQ`, `Transfer Call`).
- **Instructions**: Control assistant behavior while the node is active. Choose **Append** (add to base instructions) or **Replace** (use only node instructions).
- **Tool availability**: Each node can enable or disable individual tools from the assistant's full set, or add node-specific tools. Scoping tools per node makes each step more reliable.
- **Model override**: Use a different LLM for a specific node.
- **Voice override**: Use a different voice configuration for a specific node.

Speak nodes carry a **Message** field that supports `{{variable}}` interpolation and must have exactly one outgoing default edge.

### Edge conditions

- **LLM conditions**: Best for intent, sentiment, and natural-language judgments (e.g. `The caller wants to speak with a specific person or department.`).
- **Variable comparison conditions**: Best for deterministic routing using system or custom dynamic variables (e.g. `customer_tier == "enterprise"`, `telnyx_conversation_duration_secs >= 300`).
- **Default conditions**: Fallback edges required for speak nodes. A speak node must have exactly one outgoing default edge.

### Route to another assistant

An edge can target another assistant instead of a node, keeping each assistant focused while allowing connected experiences (e.g. a general support assistant routing billing questions to a billing assistant).

### Configure via the API

Workflows are stored on the assistant as `conversation_flow`. The API accepts the full graph on create or update. Updates treat `conversation_flow` atomically: omit it to leave it unchanged, send `null` to clear it.

```json
{
  "conversation_flow": {
    "start_node_id": "n_greeting",
    "nodes": [
      {
        "id": "n_greeting",
        "name": "Greeting & Identify Intent",
        "instructions": "Quickly determine whether the caller needs a person, a department, or a general FAQ answer.",
        "instructions_mode": "append"
      },
      {
        "type": "speak",
        "id": "n_disclosure",
        "name": "Recording Disclosure",
        "message": "Thanks for calling Acme, {{first_name}}. This call may be recorded for quality and training."
      }
    ],
    "edges": [
      {
        "id": "e_disclosure_to_greeting",
        "start_node_id": "n_disclosure",
        "target": { "type": "node", "node_id": "n_greeting" },
        "condition": { "type": "default" }
      }
    ]
  }
}
```

### Example workflow patterns

- **Front desk receptionist**: Greet → route to FAQ or Transfer based on intent.
- **Appointment booking**: Collect request → Collect availability → Confirm details → Final confirmation.
- **Escalation after timeout**: Route to specialist when `telnyx_conversation_duration_secs >= 300`.
- **Multi-assistant specialization**: Main support assistant routes to billing, technical, or sales assistants.

### Workflow best practices

- Keep nodes focused on one clear job.
- Limit each node to the tools it needs.
- Prefer append mode to preserve global rules and brand voice.
- Write edge conditions as clear decisions (avoid vague terms like `billing`).
- Use variable comparisons for hard rules and deterministic routing.
- Avoid too many paths from a single node — add an intermediate triage node if needed.
- Test every path before production.
