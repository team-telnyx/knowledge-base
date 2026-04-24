---
title: Gather
summary: The `` verb collects DTMF tones during a call.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather/index
    content_hash: 578c12024fd35edd8feb8c9ebe143e417a49b0d08e0beaddac91d98be4baf4b0
updated_at: 2026-04-10T00:00:00Z
---

# Gather

The `` verb collects DTMF tones during a call. `` can be nested within `` to create an interactive IVR with text-to-speech.

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
      <td> URL where TeXML will send the gathered result and message history. Same method (<code>GET</code>/<code>POST</code>) as set for the TexML application is used. Transfers control of the current call to the TeXML file returned. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>timeout</code></td>
      <td> Time in seconds between digits before the `` digits are sent to your action URL. Telnyx will wait until all nested verbs have been executed before beginning the timeout period. </td>
      <td><code>1</code> - <code>120</code></td>
      <td><code>5</code></td>
    </tr>

    <tr>
      <td><code>input</code></td>
      <td> The input type for the gather action. </td>
      <td><code>dtmf</code>, <code>speech</code>, <code>dtmf speech</code></td>
      <td><code>dtmf</code></td>
    </tr>

    <tr>
      <td><code>speechTimeout</code></td>
      <td> Time in seconds to wait after speech ends before timing out. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>partialResultCallback</code></td>
      <td> URL for sending partial gather results. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>partialResultCallbackMethod</code></td>
      <td> HTTP request type used for partialResultCallback. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>profanityFilter</code></td>
      <td> Whether to filter profanity from speech recognition results (camelCase format). </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>useEnhanced</code></td>
      <td> Enables enhanced transcription, this works for models phone\_call and video (camelCase format). </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>hints</code></td>
      <td> Hints to improve transcription accuracy. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>transcriptionEngine</code></td>
      <td> Engine to use for speech recognition:  Google, Telnyx </td>
      <td><code>Google</code>, <code>Telnyx</code>, <code>Azure</code>, <code>Deepgram</code></td>
      <td>-</td>
    </tr>

    <tr>
      <td><code>apiKeyRef</code></td>
      <td> Reference to the API key for authentication. See [integration secrets documentation](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret) for details. The parameter is optional as defaults are available for some regions. Used with Azure transcriptionEngine. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>region</code></td>
      <td> Region to use with the specified transcription engine. Required for Azure. See regions in [transcription\_engine\_config](https://developers.telnyx.com/api-reference/call-commands/transcription-start). </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>finishOnKey</code></td>
      <td> The set of digits, (0-9, \*, #), that indicates the end of the gather. </td>

      <td />

      <td><code>#</code></td>
    </tr>

    <tr>
      <td><code>numDigits</code></td>
      <td> The number of digits to be gathered. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>language</code></td>
      <td> The language used. See <a href="/api-reference/call-commands/speak-text">RESTful API documentation</a> for supported values. By default en-US. </td>

      <td />

      <td><code>en-US</code></td>
    </tr>

    <tr>
      <td><code>validDigits</code></td>
      <td> The set of valid digits for the gather action. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>invalidDigitsAction</code></td>
      <td> URL where TeXML will send the invalid gathered digits. The same method (GET/POST) as set for the TeXML application is used. Transfers control of the current call to the TeXML file returned. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>minDigits</code></td>
      <td> Minimum number of digits to be gathered. </td>
      <td><code>1</code> - <code>128</code></td>
      <td><code>1</code></td>
    </tr>

    <tr>
      <td><code>maxDigits</code></td>
      <td> Maximum number of digits to be gathered. </td>
      <td><code>1</code> - <code>128</code></td>
      <td><code>128</code></td>
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
      <td><code>Say</code></td>

      <td />
    </tr>

    <tr>
      <td><code>Play</code></td>

      <td />
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Gather timeout="5" numDigits="1" finishOnKey="#">
        Press 1 for sales, press 2 for support.

```

## Expected callbacks

If `action` is set, a callback is sent when gather completes with the collected digits or speech.

See [Gather Callback](https://developers.telnyx.com/api-reference/callbacks/texml-gather) for the full payload reference.
