---
title: TeXML Programmable Voice
summary: TeXML is Telnyx's XML-based markup language for controlling Programmable
  Voice calls, designed for drop-in compatibility with Twilio's TwiML. This page covers
  the TeXML quickstart, verb and noun compatibility with TwiML, REST API endpoint
  parity, and detailed reference for the core verbs including Dial, Conference, Enqueue,
  Connect, AIAssistant, AIGather, and ConversationRelay.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conversationrelay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue
updated_at: 2026-08-05T14:04:49Z
---

# TeXML Programmable Voice

*Part 5 of 6 — see also: [Part 1](texml-programmable-voice--part-1.md), [Part 2](texml-programmable-voice--part-2.md), [Part 3](texml-programmable-voice--part-3.md), [Part 4](texml-programmable-voice--part-4.md), [Part 6](texml-programmable-voice--part-6.md)*

TeXML is Telnyx's XML-based markup language for controlling Programmable Voice calls, designed for drop-in compatibility with Twilio's TwiML. This page covers the TeXML quickstart, verb and noun compatibility with TwiML, REST API endpoint parity, and detailed reference for the core verbs including Dial, Conference, Enqueue, Connect, AIAssistant, AIGather, and ConversationRelay.

## AIAssistant

The `<AIAssistant>` verb starts a voice assistant on the call.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `id` | The identifier of the AI assistant. The AI assistant can be created using the [AI Assistant API](https://developers.telnyx.com/api-reference/assistants/create-an-assistant). | — | — |
| `join` | The ID of an existing AI assistant conversation to join. When set, the call leg is added as a participant to the specified conversation instead of starting a new one. Use `participantName` and `participantRole` to configure the joining participant. | — | — |
| `participantName` | The display name of the participant joining the conversation. Only used when `join` is set. | — | — |
| `participantRole` | The role of the participant joining the conversation. Only used when `join` is set. | `user`, `assistant` | `user` |

### Examples

```xml
<Response>
    <Connect>
        <AIAssistant id="assistant-776d0d6f-716d-4d8f-b6da-b95181636838">
        </AIAssistant>
    </Connect>
</Response>
```

```xml
<!-- Join an existing AI assistant conversation -->
<Response>
    <Connect>
        <AIAssistant join="v3:abc123def456" participantName="John" participantRole="user">
        </AIAssistant>
    </Connect>
</Response>
```

```xml
<!-- Transfer to an agent when the assistant conversation ends with an error -->
<Response>
    <Connect action="https://example.com/after-assistant" method="POST">
        <AIAssistant id="assistant-776d0d6f-716d-4d8f-b6da-b95181636838">
        </AIAssistant>
    </Connect>
</Response>
```

When the `action` attribute is set on `<Connect>`, TeXML makes a request to that URL when the assistant conversation ends and executes the TeXML instructions returned in the response. The request payload includes a `Reason` field describing why the conversation ended (for example `service_error`), so the action endpoint can branch on it — such as returning a `<Dial>` to a human agent on error:

```xml
<!-- Example response returned by the action URL on a server-error reason -->
<Response>
    <Dial>+15551234567</Dial>
</Response>
```

## AIGather

The `<AIGather>` verb collects specific information from call participants leveraging AI. It requires the child node `<Parameters>` to be provided with a JSON Schema object that describes the parameters to be gathered.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `action` | URL where TeXML sends the gathered speech input. The same method (GET/POST) as set for the TeXML application is used. Transfers control of the current call to the TeXML file returned. | — | — |
| `method` | HTTP request type used to retrieve the next set of instructions. | `GET`, `POST` | `POST` |

### Child verbs/nouns

- **`<Greeting>`** — Reads supplied text back to the caller when the gathering starts. If none, nothing is played.
- **`<Voice>`** — The voice to be used by the voice assistant.
- **`<Parameters>`** — The parameters described as a JSON Schema object to be gathered by the voice assistant. Must be provided within CDATA tags.
- **`<MessageHistory>`** — The message history the voice assistant should be aware of. Provided as a list of `<Message>` nodes, each with a `role` attribute (`user` or `assistant`).
- **`<Tools>`** — The list of tools to be used by the AI assistant. Each `<Tool>` should contain a tool definition in JSON format. See the [Voice API Gather using AI documentation](https://developers.telnyx.com/api-reference/call-commands/gather-using-ai) for available tools.

### Voice attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `name` | The voice to be used by the voice assistant. Supports ElevenLabs (`ElevenLabs.model_id.voice_id`), Telnyx (`Telnyx.model_id.voice_id`), and AWS Polly (`AWS.Polly.voice_id` or `Polly.voice_id`) voices. | — | `Telnyx.NaturalHD.Astra` |
| `api_key_ref` | Reference to the ElevenLabs API key to be used for the voice assistant. The API key must be added to the account text-to-speech secrets. Only used with ElevenLabs voices. | — | — |
| `voice_speed` | The voice speed. Must be between 0.1 and 2.0. Only used with Telnyx voices. | `0.1`–`2.0` | `1` |

### Example

```xml
<Response>
     <AIGather action="/after_ai_gather">
    <Greeting></Greeting>
    <Parameters>
    <![CDATA[
    {
      "properties": {
        "age": {
          "description": "The age of the customer.",
          "type": "integer"
        },
        "location": {
          "description": "The location of the customer.",
          "type": "string"
        }
      },
      "required": [
        "age",
        "location"
      ],
      "type": "object"
    }
    ]]>
    </Parameters>
    <Voice name="Telnyx.NaturalHD.Astra" voice_speed="1.0"/>
    <MessageHistory>
      <Message role="user">Hello my name is Enzo.</Message>
    </MessageHistory>
    <InterruptionSettings enable="true"/>
    <Transcription model="some_model"/>
    <Assistant model="openai/gpt-4" api_key_ref="my_key_ref" instructions="You are a helpful assistant that can help the customer with their questions.">
      <Tools>
        <Tool>
          <![CDATA[
          {
            "type": "hangup",
            "hangup": {
              "description": "Hang up the call."
            }
          }
          ]]>
        </Tool>
        <Tool>
          <![CDATA[
          {
            "type": "transfer",
            "transfer": [
              {
                "name": "support",
                "to": "+1234567890"
              }
            ]
          }
          ]]>
        </Tool>
      </Tools>
    </Assistant>
  </AIGather>
</Response>
```

### Expected callbacks

If `action` is set, a callback is sent when the AI gather completes with the collected result and message history. See the [AI Gather Callback](https://developers.telnyx.com/api-reference/callbacks/texml-ai-gather) reference.
