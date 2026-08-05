---
title: AI Assistant Configuration
summary: Telnyx AI assistants can be extended with enterprise integrations, tuned
  interruption behavior, persistent memory across conversations, and multi-participant
  call capabilities. This page covers the available integration catalog and connection
  workflow, interruption settings for turn-taking and non turn-taking transcription
  models, memory configuration via the dynamic variables webhook, and the Invite and
  Skip Turn tools used to coordinate multi-participant voice calls.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
- url: https://developers.telnyx.com/docs/inference/ai-assistants/interruption-settings
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
updated_at: 2026-08-05T13:44:48Z
---

# AI Assistant Configuration

*Part 4 of 6 — see also: [Part 1](ai-assistant-configuration--part-1.md), [Part 2](ai-assistant-configuration--part-2.md), [Part 3](ai-assistant-configuration--part-3.md), [Part 5](ai-assistant-configuration--part-5.md), [Part 6](ai-assistant-configuration--part-6.md)*

Telnyx AI assistants can be extended with enterprise integrations, tuned interruption behavior, persistent memory across conversations, and multi-participant call capabilities. This page covers the available integration catalog and connection workflow, interruption settings for turn-taking and non turn-taking transcription models, memory configuration via the dynamic variables webhook, and the Invite and Skip Turn tools used to coordinate multi-participant voice calls.

## Memory

Memory enables your AI assistant to recall essential details from past conversations. Instead of starting each phone call or text exchange from scratch, your AI assistant naturally continues previous discussions. Telnyx Assistants natively support Voice and Messaging APIs, meaning the same assistant can seamlessly remember conversations across channels.

### Identifying the conversations to include

There is no one-size-fits-all answer for which previous conversations an AI Assistant should remember during a specific conversation. You may want an AI Assistant to have memory access to:

- Every conversation it had with any user
- Every conversation it had with **this specific user**
- Every conversation it had with **users in a specific group** in **the past 10 days**
- Or something else entirely

To support this, Telnyx exposes a flexible query language to give customers full control over their assistant's memory. Any query you can build with the [List Conversations endpoint](/api-reference/conversations/list-conversations), you can use to configure memory access.

### Configuring memory with the dynamic variables webhook

If the `dynamic_variables_webhook_url` is set for the assistant, Telnyx sends the following payload at the start of the conversation:

```
{
  "data" :{
   "record_type": "event",
   "id": "event_id",
   "event_type": "assistant.initialization",
   "occurred_at": "2025-04-07T10:00:00Z",
   "payload": {
    "telnyx_conversation_channel": "phone_call",
    "telnyx_agent_target": "+1234567890",
    "telnyx_end_user_target": "+1234567890",
    "telnyx_end_user_target_verified": false
   }
  }
}
```

For inbound phone calls to an assistant, the `telnyx_end_user_target_verified` field will be set to `true` if the call has Full (A) [STIR/SHAKEN attestation](https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx) and Telnyx was able to verify the authenticity of the PASSporT token.

Telnyx expects a JSON response with the following structure. If a response is not received within a 1-second timeout, the call will proceed "best effort":

```
{
  "dynamic_variables": {
    "full_name": "Rachel Thomas",
    "facility_name": "UCHealth",
    "facility_department": "Cardiology"
  },
  "memory": {
    "conversation_query": "metadata->telnyx_end_user_target=eq.+13128675309&limit=5&order=last_message_at.desc"
  }
}
```

In this example, the optional `memory` field provides the AI assistant with memory access to the last 5 conversations with the current user's phone number. You can read more about the optional `dynamic_variables` field in the [Dynamic Variables](dynamic-variables.md) tutorial.

![AI Assistant Variable Config](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/configure-dynamic.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=2868ce1f60c770a3d22a10d080163cce)

In addition to controlling which conversations are remembered, you can customize which information from a conversation is remembered. Specify a comma-delimited list of insight IDs in the memory field. Insight IDs can be retrieved in the Insights tab for your assistant. Only the results from the insights you specify will be included in the assistant's memory.

```
{
  "dynamic_variables": {
    "full_name": "Rachel Thomas",
    "facility_name": "UCHealth",
    "facility_department": "Cardiology"
  },
  "memory": {
    "conversation_query": "metadata->telnyx_end_user_target=eq.+13128675309&limit=5&order=last_message_at.desc",
    "insight_query": "insight_ids=123,456""
  }
}
```

![AI Assistant Insight Copy](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/copy-insight-id.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=14ad03b9d6a1010e3ef9977931cb32c2)

### Custom metadata

You may want to create your own memory access system based on custom metadata for conversations. To do this, add metadata to conversations in the dynamic variable webhook response:

```
{
  "dynamic_variables": {
    "full_name": "Rachel Thomas",
    "facility_name": "UCHealth",
    "facility_department": "Cardiology"
  },
  "memory": {
    "conversation_query": "metadata->telnyx_end_user_target=eq.+13128675309&limit=5&order=last_message_at.desc"
  },
  "conversation": {
    "metadata": {
      "your_custom_metadata": "your_custom_value"
    }
  }
}
```

In future conversations, you can filter that metadata in the `memory` field using the syntax `metadata->your_custom_metadata=eq.your_custom_value`.
