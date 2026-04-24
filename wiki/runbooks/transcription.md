---
title: Transcription
summary: The `` verb enables real-time speech-to-text transcription for the call.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription/index
    content_hash: 917753f7c70c91e3d16c590f387549a4ff4f42b7732538b9d1b02caa26ec75e4
updated_at: 2026-04-10T00:00:00Z
---

# Transcription

The `` verb enables real-time speech-to-text transcription for the call.

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
      <td><code>language</code></td>
      <td> Language to use for speech recognition. See languages in [transcription\_engine\_config](https://developers.telnyx.com/api-reference/call-commands/transcription-start). </td>

      <td />

      <td><code>en</code></td>
    </tr>

    <tr>
      <td><code>interimResults</code></td>
      <td> Whether to send also interim results. If set to false, only final results will be sent. Applies to transcriptionEngine A only. </td>

      <td />

      <td><code>false</code></td>
    </tr>

    <tr>
      <td><code>transcriptionEngine</code></td>
      <td> Engine to use for speech recognition. Available engines: Google (default), Telnyx, Deepgram. Each engine supports different models and languages - see model attribute and examples below. Legacy values "A" (maps to Google) and "B" (maps to Telnyx) are supported for backward compatibility. </td>
      <td><code>Google</code>, <code>Telnyx</code>, <code>Deepgram</code>, <code>Azure</code>, <code>A</code>, <code>B</code></td>
      <td><code>Google</code></td>
    </tr>

    <tr>
      <td><code>transcriptionTracks</code></td>
      <td> Indicates which leg of the call will be transcribed. Use inbound for the leg that requested the transcription, outbound for the other leg, and both for both legs of the call. </td>
      <td><code>inbound</code>, <code>outbound</code>, <code>both</code></td>
      <td><code>inbound</code></td>
    </tr>

    <tr>
      <td><code>transcriptionCallback</code></td>
      <td> URL that tells Telnyx where to make its GET or POST requests with transcription data. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>transcriptionCallbackMethod</code></td>
      <td> HTTP request type used for transcriptionCallback. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>model</code></td>
      <td> Optional model to use with the specified transcription engine. If not specified, the engine's default model will be used. See transcription models in [transcription\_engine\_config](https://developers.telnyx.com/api-reference/call-commands/transcription-start). </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>apiKeyRef</code></td>
      <td> Reference to the API key for authentication. See [integration secrets documentation](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret) for details. The parameter is optional as defaults are available for some regions. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>region</code></td>
      <td> Region to use with the specified transcription engine. Required for Azure. See regions in [transcription\_engine\_config](https://developers.telnyx.com/api-reference/call-commands/transcription-start). </td>

      <td />

      <td>-</td>
    </tr>
  </tbody>
</table>

## Examples

**Example 1: Basic transcription using Google (default)**

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Transcription language="en" interimResults="true" transcriptionCallback="/transcription" />

```

**Example 2: Google with phone call optimized model**

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Transcription
      transcriptionEngine="Google"
      model="phone_call"
      language="en-US"
      interimResults="true"
      transcriptionCallback="/transcription" />

```

**Example 3: Telnyx engine with Whisper model**

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Transcription
      transcriptionEngine="Telnyx"
      model="openai/whisper-large-v3-turbo"
      language="es"
      transcriptionCallback="/transcription" />

```

**Example 4: Deepgram with Nova-3 model**

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Transcription
      transcriptionEngine="Deepgram"
      model="deepgram/nova-3"
      language="fr"
      transcriptionCallback="/transcription" />

```

**Example 5: Azure with Fast model and credentials**

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Transcription
      transcriptionEngine="Azure"
      model="azure/fast"
      language="en-US"
      apiKeyRef="your-azure-api-key-ref"
      region="eastus"
      transcriptionCallback="/transcription" />

```

**Example 6: Azure with Realtime model**

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Transcription
      transcriptionEngine="Azure"
      model="azure/realtime"
      language="en-US"
      region="westus"
      transcriptionCallback="/transcription" />

```

## Expected callbacks

If `transcriptionCallback` is set, transcription results are sent as they become available.

See [Transcription Callback](https://developers.telnyx.com/api-reference/callbacks/texml-transcription) for the full payload reference.


## Related Pages

- [In-Call Transcription](../runbooks/in-call-transcription.md)
- [Transcription Settings](../runbooks/transcription-settings.md)
