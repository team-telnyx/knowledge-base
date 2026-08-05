---
title: Telnyx Programmable Voice
summary: A consolidated reference for Telnyx Programmable Voice covering the Voice
  API fundamentals, available commands and resources, TeXML verbs (Stop, Stream, Suppression,
  Transcription), Text-to-Speech providers, and the European regional endpoint.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stop
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/suppression
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription
- url: https://developers.telnyx.com/docs/voice/programmable-voice/tts
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-commands-and-resources
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-fundamentals
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-services-in-europe/index
updated_at: 2026-08-05T14:05:29Z
---

# Telnyx Programmable Voice

*Part 3 of 5 — see also: [Part 1](telnyx-programmable-voice--part-1.md), [Part 2](telnyx-programmable-voice--part-2.md), [Part 4](telnyx-programmable-voice--part-4.md), [Part 5](telnyx-programmable-voice--part-5.md)*

A consolidated reference for Telnyx Programmable Voice covering the Voice API fundamentals, available commands and resources, TeXML verbs (Stop, Stream, Suppression, Transcription), Text-to-Speech providers, and the European regional endpoint.

## TeXML Verbs

TeXML is an XML-based scripting layer that mirrors the Voice API command set. The verbs below are commonly used inside `<Start>` and `<Stop>` containers.

### Stop

The `<Stop>` verb stops the instruction specified by its child noun on a call.

| Noun/Verb | Description |
| --- | --- |
| `Suppression` | Stops current suppression, no attributes need to be provided. |
| `Transcription` | Stops current transcription, no attributes need to be provided. |
| `Stream` | Stops current media stream, no attributes need to be provided. |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Stop>
    <Stream />
  </Stop>
</Response>
```

### Stream

The `<Stream>` instruction starts streaming the media from a call to a specific WebSocket address in near-real-time. Audio is delivered as base64-encoded RTP payloads (no headers), wrapped in JSON payloads.

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `url` | The destination WebSocket address where the stream is going to be delivered. | — | — |
| `track` | Specifies which track should be streamed. | `inbound_track`, `outbound_track`, `both_tracks` | `inbound_track` |
| `name` | Specifies custom name for the stream instance. | — | — |
| `codec` | Specifies the codec to be used for the streamed audio. When set to `default` or when transcoding is not possible, the codec from the call will be used. Currently, transcoding is only supported between PCMU and PCMA codecs. | `PCMU`, `PCMA`, `G722`, `OPUS`, `AMR-WB`, `default` | `default` |
| `bidirectionalMode` | Bidirectional streaming mode. | `mp3`, `rtp` | `mp3` |
| `bidirectionalCodec` | Bidirectional streaming codec, used only with `bidirectionalMode=rtp`. | `PCMU`, `PCMA`, `G722`, `OPUS`, `AMR-WB` | `PCMU` |
| `bidirectionalSamplingRate` | Bidirectional streaming sampling rate in Hz. | `8000`, `16000`, `24000` | `8000` |
| `statusCallback` | A URL for Telnyx to send webhook requests to on stream status events (e.g. stream started, stopped, or failed). | — | — |
| `statusCallbackMethod` | HTTP request type used for `statusCallback`. | `GET`, `POST` | `POST` |
| `enableReconnect` | Whether the platform should automatically attempt to reconnect the WebSocket stream if disconnected. | — | `true` |

The `<Parameter>` child noun passes custom key-value parameters to the WebSocket server. Parameters are included in the `start` message sent over the WebSocket connection.

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `name` | The name of the custom parameter. | — | — |
| `value` | The value of the custom parameter. | — | — |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Stream url="wss://yourdomain.com/stream" track="both_tracks" />
  </Start>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Stream url="wss://yourdomain.com/stream" statusCallback="https://example.com/stream-events">
      <Parameter name="customer_id" value="12345" />
      <Parameter name="call_type" value="support" />
    </Stream>
  </Start>
</Response>
```

By default, `enableReconnect` is `"true"`, and the platform will automatically attempt to reconnect the WebSocket stream if it is disconnected. Set `enableReconnect="false"` to disable this behavior, for example when a disconnection should immediately end the stream.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Stream url="wss://yourdomain.com/stream" enableReconnect="false" />
  </Start>
</Response>
```

If `statusCallback` is set, stream status callbacks are sent for the following events:

- `stream-started` — Stream has started
- `stream-stopped` — Stream has stopped
- `stream-failed` — Stream failed to start or was interrupted

### Suppression

The `<Suppression>` noun is used inside `<Start>` and `<Stop>` verbs to control noise suppression on the call to improve audio quality.

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `direction` | Specifies which side of the audio shall be denoised. | `inbound`, `outbound`, `both` | `inbound` |
| `noiseSuppressionEngine` | The noise suppression engine to use. | `Denoiser`, `DeepFilterNet`, `Krisp`, `AiCoustics` | `Denoiser` |
| `model` | The Krisp model to use. Only applicable when `noiseSuppressionEngine` is `Krisp`. Available models: `krisp-viva-tel-v2.kef`, `krisp-viva-tel-lite-v1.kef`, `krisp-viva-pro-v1.kef`, `krisp-viva-ss-v1.kef`. | — | — |
| `suppressionLevel` | Suppression intensity (0.0–100.0). Only applicable when `noiseSuppressionEngine` is `Krisp`. | — | — |
| `family` | The AiCoustics model family. Only applicable when `noiseSuppressionEngine` is `AiCoustics`. Valid values: `sparrow` (default), `quail`. | — | — |
| `size` | The AiCoustics model size. Only applicable when `noiseSuppressionEngine` is `AiCoustics`. Valid values: `s` (default), `l`, `vf` (`vf` requires `family` to be `quail`). CCA-supported size aliases are also accepted and normalized. | — | — |
| `enhancementLevel` | Enhancement intensity (0.0–1.0). Only applicable when `noiseSuppressionEngine` is `AiCoustics`. | — | `0.8` |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Suppression direction="both" />
  </Start>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Suppression
      direction="inbound"
      noiseSuppressionEngine="Krisp"
      model="krisp-viva-tel-v2.kef"
      suppressionLevel="75" />
  </Start>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Stop>
    <Suppression />
  </Stop>
</Response>
```

### Transcription

The `<Transcription>` verb enables real-time speech-to-text transcription for the call.

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `language` | Language to use for speech recognition. | — | `en` |
| `interimResults` | Whether to send also interim results. If set to false, only final results will be sent. Applies to transcriptionEngine A only. | — | `false` |
| `transcriptionEngine` | Engine to use for speech recognition. Available engines: Google (default), Telnyx, Deepgram, Azure, xAI, AssemblyAI, Soniox, Speechmatics, Parakeet, Humain, Reson8, Cohere. Legacy values `A` (maps to Google) and `B` (maps to Telnyx) are supported for backward compatibility. | `Google`, `Telnyx`, `Deepgram`, `Azure`, `xAI`, `AssemblyAI`, `Soniox`, `Speechmatics`, `Parakeet`, `Humain`, `Reson8`, `Cohere`, `A`, `B` | `Google` |
| `transcriptionTracks` | Indicates which leg of the call will be transcribed. Use `inbound` for the leg that requested the transcription, `outbound` for the other leg, and `both` for both legs of the call. | `inbound`, `outbound`, `both` | `inbound` |
| `transcriptionCallback` | URL that tells Telnyx where to make its GET or POST requests with transcription data. | — | — |
| `transcriptionCallbackMethod` | HTTP request type used for `transcriptionCallback`. | `GET`, `POST` | `POST` |
| `model` | Optional model to use with the specified transcription engine. Format is `vendor/model-name` — e.g. `deepgram/nova-2`, `deepgram/nova-3`, `azure/fast`, `assemblyai/universal-streaming`, `soniox/stt-rt-v4`, `speechmatics/standard`, `nvidia/parakeet-v3`, `xai/grok-stt`, `humain/realtime`, `reson8/turns`, `cohere/ar-stt`. The vendor must match `transcriptionEngine`. If not specified, the engine's default model will be used. On Deepgram, defaults to `deepgram/nova-3`. | — | — |
| `hints` | Hints to improve transcription accuracy. On Deepgram, this maps to the Nova-2 keyword biasing feature and is supported only on `model="deepgram/nova-2"`; it is silently dropped on Nova-3 (use `keyterms` instead). Accepts a comma-separated string. | — | — |
| `keyterms` | Deepgram Nova-3 keyterm prompting. Biases recognition toward domain-specific terms or brand names. Supported only on `model="deepgram/nova-3"`; silently dropped on Nova-2 (use `hints` instead). Accepts a comma-separated string. | — | — |
| `smartFormat` | Disable Deepgram's smart formatting so the transcript stays lowercase with no punctuation. Deepgram-only; silently dropped on other engines. | — | `true` |
| `apiKeyRef` | Reference to the API key for authentication. Optional as defaults are available for some regions. | — | — |
| `region` | Region to use with the specified transcription engine. Required for Azure. | — | — |

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Transcription language="en" interimResults="true" transcriptionCallback="/transcription" />
  </Start>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Transcription
      transcriptionEngine="Google"
      model="phone_call"
      language="en-US"
      interimResults="true"
      transcriptionCallback="/transcription" />
  </Start>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Transcription
      transcriptionEngine="Telnyx"
      model="openai/whisper-large-v3-turbo"
      language="es"
      transcriptionCallback="/transcription" />
  </Start>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Transcription
      transcriptionEngine="Deepgram"
      model="deepgram/nova-3"
      language="fr"
      transcriptionCallback="/transcription" />
  </Start>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Transcription
      transcriptionEngine="Azure"
      model="azure/fast"
      language="en-US"
      apiKeyRef="your-azure-api-key-ref"
      region="eastus"
      transcriptionCallback="/transcription" />
  </Start>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Transcription
      transcriptionEngine="Azure"
      model="azure/realtime"
      language="en-US"
      region="westus"
      transcriptionCallback="/transcription" />
  </Start>
</Response>
```

If `transcriptionCallback` is set, transcription results are sent as they become available.
