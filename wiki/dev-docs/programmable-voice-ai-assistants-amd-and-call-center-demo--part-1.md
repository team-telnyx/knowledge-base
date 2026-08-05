---
title: 'Programmable Voice: AI Assistants, AMD, and Call Center Demo'
summary: 'This page covers three Programmable Voice capabilities on Telnyx: attaching
  a pre-configured AI assistant to an active call (including adding participants and
  stopping the assistant), configuring Answering Machine Detection (AMD) for outbound
  calls with standard and Premium modes plus iOS Call Screening support, and building
  a TeXML-based call center demo that forwards calls to multiple SIP-connected agents
  with optional voicemail and custom audio.'
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ai-assistant-start
- url: https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-center
updated_at: 2026-08-05T14:03:06Z
---

# Programmable Voice: AI Assistants, AMD, and Call Center Demo

*Part 1 of 3 — see also: [Part 2](programmable-voice-ai-assistants-amd-and-call-center-demo--part-2.md), [Part 3](programmable-voice-ai-assistants-amd-and-call-center-demo--part-3.md)*

This page covers three Programmable Voice capabilities on Telnyx: attaching a pre-configured AI assistant to an active call (including adding participants and stopping the assistant), configuring Answering Machine Detection (AMD) for outbound calls with standard and Premium modes plus iOS Call Screening support, and building a TeXML-based call center demo that forwards calls to multiple SIP-connected agents with optional voicemail and custom audio.

## Attach an AI Assistant to a Call

The `ai_assistant_start` command lets you attach a pre-configured AI assistant to an active call. The assistant takes over the conversation, handles speech recognition, and responds using a voice of your choice — no additional infrastructure required. This is different from [Gather using AI](gather-using-ai.md), which is purpose-built for collecting structured data. `ai_assistant_start` is for open-ended, conversational AI experiences.

### Prerequisites

- A Telnyx account with an active call in progress. Follow the [Voice API getting started guide](voice-api-getting-started-guide.md) if you haven't set that up.
- An AI assistant. You can create one:
  - **No-code** via the Portal: [AI Assistants guide](ai-assistants-guide.md)
  - **Via the API**: [Create an assistant](https://developers.telnyx.com/api-reference/assistants/create-an-assistant)

Once you have an assistant, note its `id` (format: `assistant-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).

### Start an AI Assistant on a Call

Send a `POST` request to `ai_assistant_start` with the `call_control_id` of the active call:

```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_start \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "assistant": {
      "id": "assistant-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    }
  }'
```

That's it. The assistant is now live on the call.

### Webhooks

Once started, the assistant emits the following webhooks:

| Event | Description |
| --- | --- |
| `call.conversation.ended` | The AI conversation has ended |
| `call.conversation_insights.generated` | Conversation summary and insights are available |

### Stop the Assistant

To stop the assistant and return control to your application:

```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_stop \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Add a Participant to an Existing Conversation

Once an AI assistant conversation is running, you can bring additional call legs into it using `ai_assistant_join`. For example, you can dial out to a new destination, wait for the person to answer, then add them to the ongoing conversation.

#### Prerequisites

- An active AI assistant conversation with a known `conversation_id`. The `conversation_id` is returned in the `200` response of `ai_assistant_start`.

#### Example: Dial a new participant and add them to the conversation

**Step 1 — Dial the new destination:**

```
curl -X POST https://api.telnyx.com/v2/calls \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "connection_id": "your-connection-id",
    "to": "+15555550100",
    "from": "+15555550199"
  }'
```

This returns a new `call_control_id` for the outbound leg.

**Step 2 — Wait for the `call.answered` webhook:**
When Telnyx sends a `call.answered` event for the new call leg, extract its `call_control_id`.

**Step 3 — Add the participant to the conversation:**

#### Join the Conversation

Once you have the new `call_control_id`:

```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_join \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "participant": {
      "id": "{call_control_id}",
      "role": "user"
    }
  }'
```

The participant's `id` must be the `call_control_id` of the call being added. The only supported `role` is `"user"`.

#### Optional Participant Fields

| Field | Type | Description |
| --- | --- | --- |
| `name` | string | Display name for the participant |
| `on_hangup` | string | What happens when this participant hangs up: `"continue_conversation"` (default) or `"end_conversation"` |

### Next Steps

- Explore the full [AI Assistant API reference](https://developers.telnyx.com/api-reference/assistants/create-an-assistant)
- Configure your assistant in the [Portal](https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index)
- Collect structured data mid-call with [Gather using AI](gather-using-ai.md)
