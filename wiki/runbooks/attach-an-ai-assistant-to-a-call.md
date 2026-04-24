---
title: Attach an AI Assistant to a Call
summary: Learn how to attach a pre-configured AI assistant to a live call using the ai_assistant_start command.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/ai-assistant-start/index
    content_hash: a00b405fd621f82e8f80dbde700a7a78dfe17d8fa1ca664b2e29c60ec488a660
updated_at: 2026-04-10T00:00:00Z
---

# Attach an AI Assistant to a Call

Learn how to attach a pre-configured AI assistant to a live call using the ai_assistant_start command.

## Overview

The `ai_assistant_start` command lets you attach a pre-configured AI assistant to an active call. The assistant takes over the conversation, handles speech recognition, and responds using a voice of your choice — no additional infrastructure required.

This is different from [Gather using AI](gather-using-ai.md), which is purpose-built for collecting structured data. `ai_assistant_start` is for open-ended, conversational AI experiences.

## Prerequisites

* A Telnyx account with an active call in progress. Follow the [Voice API getting started guide](https://developers.telnyx.com/docs/voice/programmable-voice/get-started/index) if you haven't set that up.
* An AI assistant. You can create one:
  * **No-code** via the Portal: [AI Assistants guide](voice-assistant-quickstart.md)
  * **Via the API**: [Create an assistant](https://developers.telnyx.com/api-reference/assistants/create-an-assistant)

Once you have an assistant, note its `id` (format: `assistant-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).

## Start an AI Assistant on a Call

Send a `POST` request to `ai_assistant_start` with the `call_control_id` of the active call:

```bash theme={null}
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

## Webhooks

Once started, the assistant emits the following webhooks:

| Event                                  | Description                                     |
| -------------------------------------- | ----------------------------------------------- |
| `call.conversation.ended`              | The AI conversation has ended                   |
| `call.conversation_insights.generated` | Conversation summary and insights are available |

## Stop the Assistant

To stop the assistant and return control to your application:

```bash theme={null}
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_stop \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

## Add a Participant to an Existing Conversation

Once an AI assistant conversation is running, you can bring additional call legs into it using `ai_assistant_join`. For example, you can dial out to a new destination, wait for the person to answer, then add them to the ongoing conversation.

### Prerequisites

* An active AI assistant conversation with a known `conversation_id`. The `conversation_id` is returned in the `200` response of `ai_assistant_start`.

### Example: Dial a new participant and add them to the conversation

**Step 1 — Dial the new destination:**

```bash theme={null}
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

### Join the Conversation

Once you have the new `call_control_id`:

```bash theme={null}
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

### Optional Participant Fields

| Field       | Type   | Description                                                                                              |
| ----------- | ------ | -------------------------------------------------------------------------------------------------------- |
| `name`      | string | Display name for the participant                                                                         |
| `on_hangup` | string | What happens when this participant hangs up: `"continue_conversation"` (default) or `"end_conversation"` |

## Next Steps

* Explore the full [AI Assistant API reference](https://developers.telnyx.com/api-reference/assistants/create-an-assistant)
* Configure your assistant in the [Portal](voice-assistant-quickstart.md)
* Collect structured data mid-call with [Gather using AI](gather-using-ai.md)
