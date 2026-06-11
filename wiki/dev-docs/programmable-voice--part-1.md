---
title: Programmable Voice
summary: A comprehensive guide to Telnyx Programmable Voice features including AI
  assistants, conversational AI, answering machine detection, deepfake detection,
  conferencing, call center and call tracking applications, and command reliability
  patterns.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ai-assistant-start
- url: https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-center
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking
- url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conversation-relay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/deepfake-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
- url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
updated_at: 2026-06-11T10:41:58Z
---

# Programmable Voice

*Part 1 of 4 — see also: [Part 2](programmable-voice--part-2.md), [Part 3](programmable-voice--part-3.md), [Part 4](programmable-voice--part-4.md)*

A comprehensive guide to Telnyx Programmable Voice features including AI assistants, conversational AI, answering machine detection, deepfake detection, conferencing, call center and call tracking applications, and command reliability patterns.

## AI Assistant on Calls

The `ai_assistant_start` command attaches a pre-configured AI assistant to an active call. The assistant takes over the conversation, handles speech recognition, and responds using a chosen voice — no additional infrastructure required. This is distinct from [Gather Using AI](gather-using-ai.md), which is purpose-built for collecting structured data; `ai_assistant_start` is for open-ended, conversational AI experiences.

### Prerequisites

- A Telnyx account with an active call in progress.
- An AI assistant, created either no-code via the Portal or via the API. Note the assistant's `id` (format: `assistant-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`).

### Starting an AI Assistant

Send a `POST` request with the `call_control_id` of the active call:

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

The `200` response returns a `conversation_id` that identifies the running conversation.

### Stopping an AI Assistant

```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/ai_assistant_stop \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Adding a Participant to a Conversation

Use `ai_assistant_join` to bring additional call legs into a running AI assistant conversation. First dial the new destination, wait for the `call.answered` webhook, then join:

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

The participant's `id` must be the `call_control_id` of the call being added. The only supported `role` is `"user"`. Optional participant fields include `name` (display name) and `on_hangup` (either `continue_conversation` — the default — or `end_conversation`).

### AI Assistant Webhooks

| Event | Description |
| --- | --- |
| `call.conversation.ended` | The AI conversation has ended |
| `call.conversation_insights.generated` | Conversation summary and insights are available |

## Gather Using AI

Gather using AI collects specific structured information from call participants — names, addresses, or other data defined by a JSON Schema. It offers a simpler user experience than the traditional gather functionality.

### Voice API

Send a `gather_using_ai` command on an active call:

```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/gather_using_ai \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "greeting": "Can you tell me your age and where you live?",
    "parameters": {
      "properties": {
        "age": { "description": "The age of the customer.", "type": "integer" },
        "location": { "description": "The location of the customer.", "type": "string" }
      },
      "required": ["age", "location"],
      "type": "object"
    },
    "voice": "Polly.Brian"
  }'
```

The `parameters` section uses [JSON Schema](https://json-schema.org/) to define the data to collect. The `required` array specifies which values must be gathered before the process ends. If no required values are provided, the process ends after the first value is retrieved.

### Message History

Provide conversation context via `message_history` so the bot can continue without losing context:

```json
"message_history": [
  { "role": "assistant", "content": "Hello what's your name?" },
  { "role": "user", "content": "My name is Enzo." }
]
```

### TeXML

Use the `<AIGather>` verb in TeXML:

```xml
<Response>
  <AIGather action="https://example.com/aigather">
    <Greeting>Hello, please provide your age and location.</Greeting>
    <Voice name="Polly.Joanna"/>
    <Parameters><![CDATA[
      {
        "type": "object",
        "properties": {
          "location": { "type": "string", "description": "The location of the user" },
          "age": { "type": "number", "description": "The age of the user" }
        },
        "required": ["location", "age"]
      }
    ]]></Parameters>
    <MessageHistory>
      <Message role="assistant">Hello, what's your name?</Message>
      <Message role="user">Hi, I'm Enzo.</Message>
    </MessageHistory>
  </AIGather>
</Response>
```

### Noise Suppression for Gathering

Accurate transcription is critical for gathering. Enable noise suppression to improve quality:

**Voice API:**

```
curl -X POST https://api.telnyx.com/v2/calls/{call_control_id}/actions/suppression_start \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{ "direction": "inbound" }'
```

**TeXML:**

```xml
<Response>
  <Start><Suppression direction="inbound"/></Start>
  <!-- ... -->
  <Stop><Suppression/></Stop>
</Response>
```
