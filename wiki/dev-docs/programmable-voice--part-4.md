---
title: Programmable Voice
summary: The Telnyx Programmable Voice API enables you to integrate voice calling
  capabilities into your applications, providing flexible inbound and outbound call
  control, real-time webhooks, and advanced features such as Conversation Relay, Deepfake
  Detection, Dialogflow ES integration, and AI-driven gather flows.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conversation-relay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/deepfake-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
- url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/get-started/index
updated_at: 2026-08-05T14:03:33Z
---

# Programmable Voice

*Part 4 of 4 — see also: [Part 1](programmable-voice--part-1.md), [Part 2](programmable-voice--part-2.md), [Part 3](programmable-voice--part-3.md)*

The Telnyx Programmable Voice API enables you to integrate voice calling capabilities into your applications, providing flexible inbound and outbound call control, real-time webhooks, and advanced features such as Conversation Relay, Deepfake Detection, Dialogflow ES integration, and AI-driven gather flows.

## Gather Using AI

Gather using AI is a powerful functionality that allows you to efficiently collect specific information from call participants. By leveraging AI, this feature can gather details such as names, addresses, or other relevant information based on a list you provide. The collected data is then sent back in a structured format. This AI-driven feature offers a much easier user experience compared to the previous gather functionality, simplifying the process and reducing the time needed to collect information.

The feature can be used for Voice API or TeXML calls similar to regular gather functionality. See the [Voice API Fundamentals](voice-api-fundamentals.md) and [TeXML Setup](texml-setup.md) guides to set up your environment.

### Voice API

Gather using AI can be enabled for any call by sending the following request:

```
curl --location 'https://api.telnyx.com/v2/calls/{{call_control_id}}/actions/gather_using_ai' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ••••••' \
--data '{
    "greeting": "Can you tell me your age and where you live?",
    "parameters": {
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
    },
    "voice": "Polly.Brian"
   }'
```

The `parameters` section contains all the data that you want to gather during the call. Use [JSON Schema](https://json-schema.org/) to define them. The `required` section specifies when the `gather` process should end. A webhook is sent when all values from this list are gathered. If no values are provided, the process ends as soon as the first value is retrieved.

### Message History

You can provide the history of the conversation in the `message_history` section, allowing the bot to continue the conversation without losing context:

```
curl --location 'https://api.telnyx.com/v2/calls/{{call_control_id}}/actions/gather_using_ai' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ••••••' \
--data '{
    "greeting": "Can you tell me your age and where you live?",
    "parameters": {
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
    },
    "voice": "Polly.Brian",
    "message_history": [
      {
        "role": "assistant",
        "content": "Hello what's your name?"
      },
      {
        "role": "user",
        "content": "My name is Enzo."
      }
    ]
  }'
```

### TeXML

In TeXML, there is a dedicated `<AIGather>` verb that can be used for that purpose:

```
<Response>
    <AIGather action="https://example.com/aigather">
        <Greeting>Hello, please provide your age and location.</Greeting>
        <Voice name="Polly.Joanna"/>
        <Parameters>
            <![CDATA[
                {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The location of the user"
                        },
                        "age": {
                            "type": "number",
                            "description": "The age of the user"
                        }
                    },
                    "required": ["location", "age"]
                }
            ]]>
        </Parameters>
        <MessageHistory>
            <Message role="assistant">Hello, what's your name?</Message>
            <Message role="user">Hi, I'm Enzo.</Message>
        </MessageHistory>
    </AIGather>
</Response>
```

### Noise Suppression

To improve transcription quality, it is recommended to enable noise suppression for the call. For Voice API calls:

```
 curl --request POST \
    --url https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_start \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer YOUR_API_KEY \
    --header 'Content-Type: application/json' \
    --data '{
        "direction": "inbound"
    }'
```

And in TeXML:

```
<Response>
    <Start>
        <Suppression direction="inbound"/>
    </Start>
...
    <Stop>
        <Suppression/>
    </Stop>
</Response>
```

## Next Steps

- Start with `prompt` frames to react to caller speech in Conversation Relay.
- Send `text` frames to stream LLM responses back to the caller.
- Use `dtmf` and `sendDigits` frames to integrate keypad-driven flows.
- Use `language` frames for multilingual conversations.
- Use `end` when your application is ready to leave Conversation Relay.
- Explore the Resources and Tutorials sections in the navigation for deeper coverage of the Programmable Voice API.

## Additional Resources

- [Telnyx API documentation](/api-reference/call-commands/dial)
- [What is voice API? Unlocking advanced calling](https://telnyx.com/resources/what-is-voice-api)
- [Telnyx Launches Programmable Voice API: Call Control](https://telnyx.com/resources/telnyx-launches-programmable-voice-api-call-control)
- [Telnyx vs. Twilio for Programmable Voice](https://telnyx.com/resources/telnyx-twilio-programmable-voice)
- [Voice API Fundamentals](/docs/voice/programmable-voice/voice-api-fundamentals)
- [Receiving Webhooks](/docs/voice/programmable-voice/receiving-webhooks)
- [Answering Machine Detection](/docs/voice/programmable-voice/answering-machine-detection)
- [Dial API Reference](/api-reference/call-commands/dial)
- [Answer API Reference](/api-reference/call-commands/answer-call)
- [Start Conversation Relay API Reference](/api-reference/call-commands/start-conversation-relay)

For help, [reach out](https://telnyx.com/contact-us) to the Telnyx team, visit the [support portal](https://support.telnyx.com/), or join the [Slack community](https://joinslack.telnyx.com/).
