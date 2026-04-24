---
title: AIGather
summary: The `` verb collects specific information from call participants leveraging AI.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather/index
    content_hash: 2b17f34d8959ddf715f86fc6a40f7c66fcf0d3030832ef91f0ee32cb882aaf05
updated_at: 2026-04-10T00:00:00Z
---

# AIGather

The `` verb collects specific information from call participants leveraging AI. It requires the child node `` to be provided with a JSON Schema object that describes the parameters to be gathered.

## Attributes

<table>
  <thead>
    <tr>
      <th>ATTRIBUTE</th>
      <th>DESCRIPTION</th>
      <th>OPTIONS</th>
      <th>DEFAULT</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>action</code></td>
      <td> URL where TeXML will send the gathered speech input. The same method (GET/POST) as set for the TeXML application is used. Transfers control of the current call to the TeXML file returned. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>method</code></td>
      <td> HTTP request type used to retrieve the next set of instructions. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>
  </tbody>
</table>

## Child verbs/nouns

<table>
  <thead>
    <tr>
      <th>NOUN/VERB</th>
      <th>DESCRIPTION</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>Greeting</code></td>
      <td> Reads supplied text back to the caller when the gathering starts, if none then nothing will be played when the gathering starts. </td>
    </tr>

    <tr>
      <td><code>Voice</code></td>
      <td> The voice to be used by the voice assistant. </td>
    </tr>

    <tr>
      <td><code>Parameters</code></td>
      <td> The parameters are described as a JSON Schema object that needs to be gathered by the voice assistant. It needs to be provided within CDATA tags (see the example below). </td>
    </tr>

    <tr>
      <td><code>MessageHistory</code></td>
      <td> The message history you want the voice assistant to be aware of, this can be useful to keep the context of the conversation, or to pass additional information to the voice assistant. They can be provided as a list of `` nodes. Each `` node must contain a role attribute that can be either user or assistant. The role attribute is used to determine if the message is from the user or the assistant. The text of the message is provided in the `` node (see the example below). </td>
    </tr>

    <tr>
      <td><code>Tools</code></td>
      <td> The list of `` to be used by the AI assistant. The `` should contain at tool definition in json format. All of the available tools are defined in the [Voice API Gather using AI documentation](https://developers.telnyx.com/api-reference/call-commands/gather-using-ai). </td>
    </tr>
  </tbody>
</table>

## Voice Attributes

<table>
  <thead>
    <tr>
      <th>ATTRIBUTE</th>
      <th>DESCRIPTION</th>
      <th>OPTIONS</th>
      <th>DEFAULT</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>name</code></td>
      <td> The voice to be used by the voice assistant. Currently, we support ElevenLabs, Telnyx and AWS voices only, for ElevenLabs voices you can pass the voice as <code>ElevenLabs.model\_id.voice\_id</code>, for Telnyx voices you can pass the voice as <code>Telnyx.model\_id.voice\_id</code>, for AWS Polly voices you can pass the voice as <code>AWS.Polly.voice\_id</code>, we also support this notation for AWS Polly voices: <code>Polly.voice\_id</code> </td>

      <td />

      <td><code>Telnyx.NaturalHD.Astra</code></td>
    </tr>

    <tr>
      <td><code>api\_key\_ref</code></td>
      <td> The reference to the ElevenLabs API key to be used for the voice assistant. The API key must be added to the account text-to-speech secrets /v2/text-to-speech/secret. Note: this is only used when using an ElevenLabs voice. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>voice\_speed</code></td>
      <td> The voice speed to be used for the voice. The voice speed must be between 0.1 and 2.0. Note: this is only used when using a Telnyx voice </td>
      <td><code>0.1</code> - <code>2.0</code></td>
      <td><code>1</code></td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}

     <AIGather action="/after_ai_gather">

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

    <Voice name="Telnyx.NaturalHD.Astra" voice_speed="1.0"/>

      <Message role="user">Hello my name is Enzo.

    <InterruptionSettings enable="true"/>
    <Transcription model="some_model"/>
    <Assistant model="openai/gpt-4" api_key_ref="my_key_ref" instructions="You are a helpful assistant that can help the customer with their questions.">

          <![CDATA[
          {
            "type": "hangup",
            "hangup": {
              "description": "Hang up the call."
            }
          }
          ]]>

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

```

## Expected callbacks

If `action` is set, a callback is sent when the AI gather completes with the collected result and message history.

See [AI Gather Callback](https://developers.telnyx.com/api-reference/callbacks/texml-ai-gather) for the full payload reference.
