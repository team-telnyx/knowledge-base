---
title: Gather using AI
summary: Gather using AI is a powerful functionality that allows you to efficiently collect specific information from call participants.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
    content_hash: 06cb2329f1ad64b4efffcbc648cfc4c57e53157fd59b21853828a16172b1be3f
updated_at: 2026-04-10T00:00:00Z
---

# Gather using AI

## Introduction

Gather using AI is a powerful functionality that allows you to efficiently collect specific information from call participants. By leveraging AI, this feature can gather details such as names, addresses, or other relevant information based on a list you provided. The collected data is then sent back in a structured format. This new AI-driven feature offers a much easier user experience compared to the previous gather functionality, simplifying the process and reducing the time needed to collect information. This guide will walk you through the process of using the 'Gather Using AI' feature effectively.

## Prerequisites

The feature can be used for Voice API or TeXML calls similar to regular gather functionality. Please follow the user guides to set up your environment:

* [Voice API](https://developers.telnyx.com/docs/voice/programmable-voice/get-started)
* [TeXML](https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup)

## Voice API

Gather using AI can be enabled for any call by sending the following curl request:

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/{{call_control_id}}/actions/gather_using_ai' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ••••••' \
--data '{
    “greeting”: “Can you tell me your age and where you live?“,
    “parameters”: {
      “properties”: {
        “age”: {
          “description”: “The age of the customer.“,
          “type”: “integer”
        },
        “location”: {
          “description”: “The location of the customer.“,
          “type”: “string”
        }
      },
      “required”: [
        “age”,
        “location”
      ],
      “type”: “object”
    },
    “voice”: “Polly.Brian”
   }'
```

The `parameters` section contains all the data that you want to gather during the call. Please use the [json schema](https://json-schema.org/) to define them.
The `required` section specifies when the `gather` process should end. A webhook will be sent when all values from this list are gathered. If no values are provided, the process will end as soon as the first value is retrieved.

## Message history

It is possible to provide the history of the conversation in the `message_history` section, allowing the bot to continue the conversation without losing context

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/calls/{{call_control_id}}/actions/gather_using_ai' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ••••••' \
--data '{
    “greeting”: “Can you tell me your age and where you live?“,
    “parameters”: {
      “properties”: {
        “age”: {
          “description”: “The age of the customer.“,
          “type”: “integer”
        },
        “location”: {
          “description”: “The location of the customer.“,
          “type”: “string”
        }
      },
      “required”: [
        “age”,
        “location”
      ],
      “type”: “object”
    },
    “voice”: “Polly.Brian”,
    “message_history”: [
      {
        “role”: “assistant”,
        “content”: “Hello what’s your name?”
      },
      {
        “role”: “user”,
        “content”: “My name is Enzo.”
      }
    ]
  }'
```

## TeXML

In the similar, the gather using AI can be enabled from TeXML. There is a dedicated verb `` that can be used for that purpose:

```xml theme={null}

    <AIGather action="https://example.com/aigather">
        Hello, please provide your age and location.
        <Voice name="Polly.Joanna"/>

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

            <Message role="assistant">Hello, what's your name?
            <Message role="user">Hi, I'm Enzo.

```

## Noise suppression

The crucial part of the gathering process is to have an accurate transcription of what was said during the call.

To improve the quality of the transcription, it is recommended to enable noise suppression for the call. This can be done in the following way for Voice API calls:

```bash theme={null}
 curl --request POST \
    --url https://api.telnyx.com/v2/calls/${call_control_id}/actions/suppression_start \
    --header 'Accept: application/json' \
    --header 'Authorization: Bearer YOUR_API_KEY \
    --header 'Content-Type: application/json' \
    --data '{
        "direction": "inbound"
    }'
```

and in TeXML:

```xml theme={null}

        <Suppression direction="inbound"/>

...

```

## Need more assistance?

If you need some help, [reach out](https://telnyx.com/contact-us) to a member of our team through our form or [the portal](https://portal.telnyx.com/).
