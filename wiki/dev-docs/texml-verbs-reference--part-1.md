---
title: TeXML Verbs Reference
summary: A comprehensive reference for all TeXML verbs supported by Telnyx, including
  attributes, child elements, examples, and expected callbacks for building programmable
  voice applications.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant
  content_hash: af198eef7639e391f8c8f060405b7b04bad9b1c02f5eb3d0771068267a71caec
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather
  content_hash: afbc1d87d0606d433f6e5f456da75392521725ceebeec0a015e41479b6925ca6
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
  content_hash: f6246336ddcc26e377ef5a351ff895009cfab433929d181fa375ef09312ca49d
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect
  content_hash: dc8d6bbc5592d61ad053cc65f12f14d46cd45c42fce7c9c888e080bd775c0e37
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conversationrelay
  content_hash: d63d26ac52566cb49f4398eb06e0be92ce5093c2726eeec62887b4259770e650
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
  content_hash: 5fae52a988962b1da6c202ea94e3a1c3f03e5a91d33715480c226586ecd7f94a
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue
  content_hash: 802557ce95d90b7cad4499133baf861a0378c2c4d25f7948466065fd06917085
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather
  content_hash: 598265ec490514334437faa8896ebb239db96bb5c07e2423a8e0b275874c33c0
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index
  content_hash: 1a98d136a32499275e01c6a23d47697b2f6ed227eb045c7aff6e8e559cb92454
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest
  content_hash: aff57efbd08370a28153150b16a57ae8a59fc7be4fdcd7c5eb9f5f1e00ebcc0d
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave
  content_hash: e2785d6fb22979fb9d219336aa2266f819a04d494710e3a5c063312a0202179e
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause
  content_hash: 7d0c629edbe69236ddf3169e86442136d8063a9b534b148164cc3c4fa1e23e7c
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play
  content_hash: dfbb4e7ed40f0ebdbb5969ad0de1a97c96b87edbf0b3e886c3bd01d676b17130
updated_at: 2026-06-11T10:44:08Z
---

# TeXML Verbs Reference

*Part 1 of 5 — see also: [Part 2](texml-verbs-reference--part-2.md), [Part 3](texml-verbs-reference--part-3.md), [Part 4](texml-verbs-reference--part-4.md), [Part 5](texml-verbs-reference--part-5.md)*

A comprehensive reference for all TeXML verbs supported by Telnyx, including attributes, child elements, examples, and expected callbacks for building programmable voice applications.

TeXML (Telnyx Markup Language) verbs control call flows in Telnyx programmable voice applications. Each verb is an XML element nested within a `<Response>` root. This page documents every available verb, its attributes, child nouns/verbs, examples, and callbacks.

## AIAssistant

The `<AIAssistant>` verb starts a voice assistant on the call. It must be nested within a `<Connect>` verb.

### Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `id` | Identifier of the AI assistant, created via the [AI Assistant API](https://developers.telnyx.com/api-reference/assistants/create-an-assistant). | — | — |
| `join` | ID of an existing AI assistant conversation to join. When set, the call leg becomes a participant in that conversation instead of starting a new one. | — | — |
| `participantName` | Display name of the participant joining the conversation. Only used when `join` is set. | — | — |
| `participantRole` | Role of the participant joining the conversation. Only used when `join` is set. | `user`, `assistant` | `user` |

### Example

Start a new assistant:

```xml
<Response>
    <Connect>
        <AIAssistant id="assistant-776d0d6f-716d-4d8f-b6da-b95181636838">
        </AIAssistant>
    </Connect>
</Response>
```

Join an existing conversation:

```xml
<Response>
    <Connect>
        <AIAssistant join="v3:abc123def456" participantName="John" participantRole="user">
        </AIAssistant>
    </Connect>
</Response>
```

## AIGather

The `<AIGather>` verb collects specific information from call participants using AI. It requires a `<Parameters>` child node containing a JSON Schema object describing the parameters to gather.

### Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `action` | URL where TeXML sends the gathered speech input. Transfers control to the TeXML file returned. | — | — |
| `method` | HTTP request type used to retrieve the next set of instructions. | `GET`, `POST` | `POST` |

### Child Verbs/Nouns

| Noun/Verb | Description |
|---|---|
| `Greeting` | Text read back to the caller when gathering starts. If omitted, nothing is played. |
| `Voice` | The voice to be used by the voice assistant. |
| `Parameters` | Parameters described as a JSON Schema object to be gathered. Must be wrapped in CDATA tags. |
| `MessageHistory` | Message history for context, provided as a list of `<Message>` nodes. Each `<Message>` must have a `role` attribute (`user` or `assistant`). |
| `Tools` | List of `<Tool>` nodes for the AI assistant. Each `<Tool>` contains a tool definition in JSON format. Available tools are defined in the [Voice API Gather using AI documentation](https://developers.telnyx.com/api-reference/call-commands/gather-using-ai). |

### Voice Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `name` | Voice to use. Supports ElevenLabs (`ElevenLabs.model_id.voice_id`), Telnyx (`Telnyx.model_id.voice_id`), and AWS Polly (`AWS.Polly.voice_id` or `Polly.voice_id`). | — | `Telnyx.NaturalHD.Astra` |
| `api_key_ref` | Reference to the ElevenLabs API key added via `/v2/text-to-speech/secret`. Only used with ElevenLabs voices. | — | — |
| `voice_speed` | Voice speed, between 0.1 and 2.0. Only used with Telnyx voices. | `0.1`–`2.0` | `1` |

### Example

```xml
<Response>
  <AIGather action="/after_ai_gather">
    <Greeting></Greeting>
    <Parameters>
    <![CDATA[
    {
      "properties": {
        "age": { "description": "The age of the customer.", "type": "integer" },
        "location": { "description": "The location of the customer.", "type": "string" }
      },
      "required": ["age", "location"],
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
          <![CDATA[{ "type": "hangup", "hangup": { "description": "Hang up the call." } }]]>
        </Tool>
        <Tool>
          <![CDATA[{ "type": "transfer", "transfer": [{ "name": "support", "to": "+1234567890" }] }]]>
        </Tool>
      </Tools>
    </Assistant>
  </AIGather>
</Response>
```

### Expected Callbacks

If `action` is set, a callback is sent when the AI gather completes with the collected result and message history. See [AI Gather Callback](https://developers.telnyx.com/api-reference/callbacks/texml-ai-gather) for the full payload.
