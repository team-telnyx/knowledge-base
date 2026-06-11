---
title: TeXML Verbs
summary: A reference guide to all TeXML verbs — XML instructions used to control call
  flows on the Telnyx platform — including their attributes, child nouns, callbacks,
  and usage examples.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/redirect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/refer
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/reject
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/say
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/start
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stop
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/suppression
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription
- url: https://developers.telnyx.com/docs/voice/programmable-voice/tts
updated_at: 2026-06-11T10:44:32Z
---

# TeXML Verbs

*Part 3 of 3 — see also: [Part 1](texml-verbs--part-1.md), [Part 2](texml-verbs--part-2.md)*

A reference guide to all TeXML verbs — XML instructions used to control call flows on the Telnyx platform — including their attributes, child nouns, callbacks, and usage examples.

## Transcription

The `<Transcription>` verb enables real-time speech-to-text transcription for the call. Use within `<Start>` or `<Stop>`.

| Attribute | Description | Options | Default |
|---|---|---|---|
| `language` | Language for speech recognition. | | `en` |
| `interimResults` | Whether to send interim results (applies to transcriptionEngine A only). | | `false` |
| `transcriptionEngine` | Engine for speech recognition. Legacy values `A` (Google) and `B` (Telnyx) supported for backward compatibility. | `Google`, `Telnyx`, `Deepgram`, `Azure`, `xAI`, `AssemblyAI`, `Soniox`, `Speechmatics`, `A`, `B` | `Google` |
| `transcriptionTracks` | Which call leg to transcribe. | `inbound`, `outbound`, `both` | `inbound` |
| `transcriptionCallback` | URL for transcription data requests. | | - |
| `transcriptionCallbackMethod` | HTTP request type for `transcriptionCallback`. | `GET`, `POST` | `POST` |
| `model` | Optional model in `vendor/model-name` format (e.g. `deepgram/nova-2`, `azure/fast`). The vendor must match `transcriptionEngine`. Deepgram defaults to `deepgram/nova-3`. | | - |
| `hints` | Hints to improve accuracy. On Deepgram, maps to Nova-2 keyword biasing; silently dropped on Nova-3. Comma-separated string. | | - |
| `keyterms` | Deepgram Nova-3 keyterm prompting for domain-specific terms or brand names. Silently dropped on Nova-2. Comma-separated string. | | - |
| `smartFormat` | Disable Deepgram's smart formatting (lowercase, no punctuation). Deepgram-only; silently dropped on other engines. | | `true` |
| `apiKeyRef` | Reference to an API key for authentication. Optional if defaults are available for the region. | | - |
| `region` | Region for the transcription engine. Required for Azure. | | - |

Example — Google (default):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Transcription language="en" interimResults="true" transcriptionCallback="/transcription" />
  </Start>
</Response>
```

Example — Deepgram with Nova-3:

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

Example — Azure with credentials:

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

If `transcriptionCallback` is set, transcription results are sent as they become available.

## Text-to-Speech Providers

The `<Say>` verb supports multiple TTS providers through the `voice` attribute. Below is a summary of each provider and its voice format.

### Telnyx Ultra

Telnyx Ultra delivers ultra-quality voice synthesis with low latency and support for 44 languages. Voice format: `Telnyx.Ultra.<VoiceId>`.

```xml
<Response>
    <Say voice="Telnyx.Ultra.3e1ed423-17e5-4773-b87c-25b031106e41">The text that should be said on the call!</Say>
</Response>
```

### Telnyx Internal TTS

Telnyx provides a high-quality, low-latency TTS engine. Voice format: `Telnyx.KokoroTTS.<VoiceId>`.

```xml
<Response>
    <Say voice="Telnyx.KokoroTTS.af">The text that should be said on the call!</Say>
</Response>
```

### Telnyx Natural

Enhanced speech quality with improved naturalness and clarity. Voice format: `Telnyx.Natural.<VoiceId>`.

```xml
<Response>
    <Say voice="Telnyx.Natural.abbie">The text that should be said on the call!</Say>
</Response>
```

### Telnyx NaturalHD

Premium-quality speech synthesis with exceptional clarity and richness, ideal for critical audio quality scenarios. Voice format: `Telnyx.NaturalHD.<VoiceId>`.

```xml
<Response>
    <Say voice="Telnyx.NaturalHD.andersen_johan">The text that should be said on the call!</Say>
</Response>
```

### AWS Polly

Supports both neural and standard quality levels. Neural voices use the prefix `Polly.*-Neural`. See the [available voices list](https://docs.aws.amazon.com/polly/latest/dg/available-voices.html). Voice format: `Polly.<VoiceId>` or `Polly.<VoiceId>-Neural`.

```xml
<Response>
    <Say voice="Polly.Amy-Neural">The text that should be said on the call!</Say>
</Response>
```

See the [pricing page](https://telnyx.com/pricing/call-control) for cost details.

### Azure AI Speech

Supports Neural and Neural HD (High Definition) service levels. Neural voices use deep neural networks for natural, expressive speech. HD voices deliver enhanced clarity with finer prosody control. Voice format: `Azure.<VoiceId>` (e.g. `Azure.en-CA-ClaraNeural`). See the [voice gallery](https://speech.microsoft.com/portal/voicegallery) for supported voices.

```xml
<Response>
    <Say voice="Azure.en-CA-ClaraNeural">The text that should be said on the call!</Say>
</Response>
```

When using Azure with a custom API key, provide `api_key_ref` and `region` attributes on `<Say>`.

### ElevenLabs

Offers many voice options but may have higher latency than AWS Polly or Azure. Requires a premium ElevenLabs account (freemium is not supported). You must provide an API key stored via the [integration secrets API](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret). Voice format: `ElevenLabs.<ModelId>.<VoiceId>`.

```xml
<Response>
    <Say voice="ElevenLabs.Default.cgSgspJ2msm6clMCkdW9" api_key_ref="your_api_key_ref">The text that should be said on the call!</Say>
</Response>
```

### MiniMax

High-quality TTS with expressive voices across multiple languages and accents. Voice format: `Minimax.<ModelId>.<VoiceId>`.

```xml
<Response>
    <Say voice="Minimax.speech-2.6-turbo.English_expressive_narrator">The text that should be said on the call!</Say>
</Response>
```

### Resemble AI

Built on the Chatterbox model, delivering AI voices that preserve emotion, style, and accent. Voice format: `Resemble.<ModelId>.<VoiceId>`.

```xml
<Response>
    <Say voice="Resemble.Pro.Aaron_en-US">The text that should be said on the call!</Say>
</Response>
```

### Inworld

Expressive multilingual AI voices with Mini and Max model tiers. Voice format: `Inworld.<ModelId>.<VoiceId>`.

```xml
<Response>
    <Say voice="Inworld.Mini.Loretta">The text that should be said on the call!</Say>
</Response>
```

### Rime

Offers two TTS models through Telnyx:

- **Coda** (recommended) — Rime's flagship model with LLM backbone, sub-100ms latency, 184 voices, and support for English, Spanish, French, Portuguese, German, and Japanese. Voice format: `Rime.Coda.<VoiceId>`.
- **ArcanaV3** — Previous flagship with multilingual codeswitching across 10 languages (Arabic, English, French, German, Hebrew, Hindi, Japanese, Portuguese, Spanish, Tamil). Voice format: `Rime.ArcanaV3.<VoiceId>`.

```xml
<Response>
    <Say voice="Rime.Coda.cove">The text that should be said on the call!</Say>
</Response>
```
