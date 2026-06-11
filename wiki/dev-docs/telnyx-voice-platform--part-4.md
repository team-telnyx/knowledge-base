---
title: Telnyx Voice Platform
summary: 'Covers two major Telnyx Voice capabilities: STIR/SHAKEN call authentication
  (attestation levels, certificate hosting, SIP header verification) and Speech-to-Text
  transcription (WebSocket streaming, REST file upload, in-call transcription, multi-engine
  model selection, and provider migration).'
sources:
- url: https://developers.telnyx.com/docs/voice/stir-shaken/attestation-behavior/index
- url: https://developers.telnyx.com/docs/voice/stir-shaken/hosted-cert
- url: https://developers.telnyx.com/docs/voice/stir-shaken/sip-header-parameters
- url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
- url: https://developers.telnyx.com/docs/voice/stt/migration
- url: https://developers.telnyx.com/docs/voice/stt/models
- url: https://developers.telnyx.com/docs/voice/stt/overview/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/pricing
updated_at: 2026-06-11T10:47:02Z
---

# Telnyx Voice Platform

*Part 4 of 4 — see also: [Part 1](telnyx-voice-platform--part-1.md), [Part 2](telnyx-voice-platform--part-2.md), [Part 3](telnyx-voice-platform--part-3.md)*

Covers two major Telnyx Voice capabilities: STIR/SHAKEN call authentication (attestation levels, certificate hosting, SIP header verification) and Speech-to-Text transcription (WebSocket streaming, REST file upload, in-call transcription, multi-engine model selection, and provider migration).

## Migrate to Telnyx STT

Most migrations require changing 2–3 lines of code.

### From Deepgram

**WebSocket** — Same wire protocol (binary audio in, JSON transcripts out):

```
- wss://api.deepgram.com/v1/listen?model=nova-2&language=en
- Authorization: Token DEEPGRAM_KEY
+ wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-2&language=en
+ Authorization: Bearer TELNYX_KEY
```

| | Deepgram | Telnyx |
|---|---|---|
| Auth scheme | `Token` | `Bearer` |
| Engine | implicit | `transcription_engine=Deepgram` |
| Model name | `nova-2`, `nova-3`, `flux` | Same names |

Response mapping: `results.channels[0].alternatives[0].transcript` → `transcript`; `is_final` → `is_final`; `speech_final` → `is_final`.

**REST** — Change auth, body format, and model prefix:

```
- curl -X POST https://api.deepgram.com/v1/listen?model=nova-2 \
-   -H "Authorization: Token DEEPGRAM_KEY" -H "Content-Type: audio/wav" --data-binary @audio.wav
+ curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
+   -H "Authorization: Bearer TELNYX_KEY" -F model="deepgram/nova-3" -F file=@audio.wav
```

| | Deepgram | Telnyx |
|---|---|---|
| Auth | `Token` | `Bearer` |
| Body | raw binary | `multipart/form-data` |
| Model | `nova-2` | `deepgram/nova-3` |

Response mapping: `results.channels[0].alternatives[0].transcript` → `text`; words available via `model_config.diarize` / `model_config.smart_format`.

### From ElevenLabs

**WebSocket** — Same wire protocol:

```
- wss://api.elevenlabs.io/v1/speech-to-text/realtime?model_id=scribe_v1&language_code=en
- xi-api-key: ELEVENLABS_KEY
+ wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&language=en
+ Authorization: Bearer TELNYX_KEY
```

Config mapping: `model_id` → `transcription_engine` + `model`; `language_code` → `language`; `keywords` → `keyterm` (Nova-3/Flux).

Response mapping: `text` → `transcript`; `is_final` → `is_final`.

**REST** — Response shape is identical (`{"text": "..."}`), no parsing changes:

```
- curl -X POST https://api.elevenlabs.io/v1/speech-to-text -H "xi-api-key: ELEVENLABS_KEY" -F "audio=@audio.mp3" -F "model_id=scribe_v1"
+ curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions -H "Authorization: Bearer TELNYX_KEY" -F model="openai/whisper-large-v3-turbo" -F file=@audio.mp3
```

| | ElevenLabs | Telnyx |
|---|---|---|
| Auth header | `xi-api-key` | `Authorization: Bearer` |
| File field | `audio` | `file` |
| Model field | `model_id` | `model` |

### From OpenAI

**REST** — Telnyx is OpenAI SDK compatible. Change the API key and base URL:

```python
from openai import OpenAI

client = OpenAI(
-   api_key="sk-OPENAI_KEY",
+   api_key="YOUR_TELNYX_API_KEY",
+   base_url="https://api.telnyx.com/v2",
)

result = client.audio.transcriptions.create(
    model="openai/whisper-large-v3-turbo",
    file=open("audio.mp3", "rb"),
)
```

Response shape is identical — `result.text` works unchanged. Note: OpenAI's `verbose_json` returns segments with timestamps, but Telnyx's Whisper models return text only. If you need timestamps, switch to `model="deepgram/nova-3"` with `model_config`.

### From Google Cloud

Google uses gRPC with protobuf; Telnyx uses WebSocket with JSON — no protobuf compilation, no service account credentials.

```
+ wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Google&language=en-US&interim_results=true&input_format=linear16&sample_rate=16000
+ Authorization: Bearer TELNYX_KEY
```

Config mapping: `language_code` → `language`; `encoding` → `input_format`; `sample_rate_hertz` → `sample_rate`; `interim_results` → `interim_results`; `enable_automatic_punctuation` → enabled by default.

Response mapping: `results[0].alternatives[0].transcript` → `transcript`; `results[0].is_final` → `is_final`.

### From AWS Transcribe

AWS uses HTTP/2 with event streams via the `amazon-transcribe-streaming-sdk`. Telnyx uses a plain WebSocket — no AWS SDK, no SigV4 signing, no IAM credentials.

```
+ wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&language=en-US&input_format=linear16&sample_rate=16000
+ Authorization: Bearer TELNYX_KEY
```

Config mapping: `language_code` → `language`; `media_encoding` → `input_format`; `media_sample_rate_hz` → `sample_rate`; `enable_partial_results_stabilization` → `interim_results`; `vocabulary_name` → `keyterm` (Nova-3/Flux).

Response mapping: `transcript.results[].alternatives[].transcript` → `transcript`; `transcript.results[].is_partial` → `is_final` (inverted).

### From Azure

The Azure Speech SDK wraps a region-specific WebSocket. Telnyx uses a plain WebSocket — no SDK install, no region routing.

```
+ wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Azure&language=en-US&interim_results=true
+ Authorization: Bearer TELNYX_KEY
```

Config mapping: `speech_recognition_language` → `language`; `recognizing` event → `is_final: false`; `recognized` event → `is_final: true`; `region` → not needed (single global endpoint).

Response mapping: `evt.result.text` → `transcript`.

**REST** migration:

```
- curl -X POST "https://eastus.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language=en-US" -H "Ocp-Apim-Subscription-Key: AZURE_KEY" -H "Content-Type: audio/wav" --data-binary @audio.wav
+ curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions -H "Authorization: Bearer TELNYX_KEY" -F model="openai/whisper-large-v3-turbo" -F file=@audio.wav
```

| | Azure | Telnyx |
|---|---|---|
| Auth | `Ocp-Apim-Subscription-Key` | `Authorization: Bearer` |
| URL | Region-specific | Single global endpoint |
| Body | Raw binary | `multipart/form-data` |
| Language | Required query param | Auto-detected or optional |

Response mapping: `DisplayText` → `text`; `NBest[0].Lexical` → `text`.

## STT Pricing

REST API pricing varies by engine and model. Contact [Telnyx sales](https://telnyx.com/contact-us) or check the [pricing page](https://telnyx.com/pricing/speech-to-text) for current rates.
