---
title: Memory
summary: Memory enables your AI assistant to recall essential details from past conversations.
sources:
  - url: https://developers.telnyx.com/docs/inference/ai-assistants/memory/index
    content_hash: bcf421ba2b665f365053cbad5fbb166f2cfa7e3a68e8a2d25bbf2946a9e48cd8
updated_at: 2026-04-10T00:00:00Z
---

# Memory

Memory enables your AI assistant to recall essential details from past conversations. Instead of starting each phone call or text exchange from scratch, your AI assistant naturally continues previous discussions.

In this tutorial, you will learn how to:

* Specify which conversations your AI Assistant has memory access to
* Configure this dynamically at the start of every conversation

> **Note:** *Telnyx Assistants natively support our Voice and Messaging APIs, meaning the same assistant can seamlessly remember conversations across channels.*

***

## Identifying the conversations to include

There is no one-size-fits-all answer for which previous conversations an AI Assistant should remember during a specific conversation.

You may want an AI Assistant to have memory access to:

* Every conversation it had with any user
* Every conversation it had with **this specific user**
* Every conversation it had with **users in a specific group** in **the past 10 days**
* Or something else entirely...

To support this, we have exposed a flexible query language to give customers full control over their assistant's memory. Any query you can build with our [List Conversations endpoint](https://developers.telnyx.com/api-reference/conversations/list-conversations), you can use to configure memory access.

## Configuring memory with the Dynamic Variables Webhook

If the `dynamic_variables_webhook_url` is set for the assistant, we will send the following payload at the start of the conversation.

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

> **Note:** *For inbound phone calls to an assistant, the `telnyx_end_user_target_verified` field will be set to `true` if the call has Full (A) [STIR/SHAKEN attestation](https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx) and Telnyx was able to verify the authenticity of the PASSporT token.*

We expect a JSON response with the following structure. If we do not receive this response within a 1-second timeout, the call will proceed "best effort".

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

In this example, the optional `memory` field provides your AI assistant with memory access to the last 5 conversations with the current user's phone number.

You can read more about the optional `dynamic_variables` field in our [tutorial on Dynamic Variables](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables).

<img alt="AI Assistant Variable Config" />

In addition to controlling which conversations are remembered, you can customize which information from a conversation is remembered.

To do this, specify a comma-delimited list of insight IDs in the memory field. Insight IDs can be retrieved in the Insights tab for your assistant, as shown below. Only the results from the insights you specify will be included in the assistant's memory.

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

<img alt="AI Assistant Insight Copy" />

## Custom Metadata

You may want to create your own memory access system based on custom metadata for conversations. To do this, you can add metadata to conversations in the dynamic variable webhook response:

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

In future conversations, you can filter that metadata in the `memory` field using the following syntax `metadata->your_custom_metadata=eq.your_custom_value`.
