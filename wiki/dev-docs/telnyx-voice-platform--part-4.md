---
title: Telnyx Voice Platform
summary: 'Covers two major Telnyx Voice capabilities: STIR/SHAKEN call authentication
  (attestation levels, certificate hosting, SIP header verification) and Speech-to-Text
  transcription (WebSocket streaming, REST file upload, in-call transcription, multi-engine
  model selection, and provider migration).'
sources:
- url: https://developers.telnyx.com/docs/voice/stir-shaken/attestation-behavior/index
  content_hash: e71721006805ece97317b6a2ce287bded0ee694d74cd96070f8efb6ec4546534
- url: https://developers.telnyx.com/docs/voice/stir-shaken/hosted-cert
  content_hash: 8a1cedc407a7eeed8a1f689a60c15c545dc6394a4ce0d4d664a31846b54b856b
- url: https://developers.telnyx.com/docs/voice/stir-shaken/sip-header-parameters
  content_hash: ddcbe69b5d283081160304794571d8ad56e52cca94e1f55ac224d31fe3f9ac5f
- url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
  content_hash: a17bf544d2f5411cb7a1e10bd8204fae4fb499a8debccef66cb9d596da2c280c
- url: https://developers.telnyx.com/docs/voice/stt/migration
  content_hash: 8273de02389d2c31f810a359f89523eeb2a64aa43286be196c610a805e479cdc
- url: https://developers.telnyx.com/docs/voice/stt/models
  content_hash: 637078dde1176884102bdc0e61dcc482b32bdee3552c24cbf5158b865a6a1426
- url: https://developers.telnyx.com/docs/voice/stt/overview/index
  content_hash: 3cd2887c1a24d01ca417a1e3a2f2e7e7db6cd92449fb5a77027b8cadb348015f
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
  content_hash: 277f6f5e42acfabb557c1b22f1293ce8235db0e343e8af493560f9071b12fa36
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
  content_hash: c75d57b2ceae2c7f6f780f4385e6a545f6dcc11d41a7cca25441d1add888572f
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
  content_hash: 3856e7e0bf451af19678e8ba5f19deb2fffe5ebab69aa15c93f0ee331521f964
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
  content_hash: afd719ffe51051e3855f74439d0eba8bde4e617f527163f25e99321d501562d6
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
  content_hash: 262aa6764992fbe5d612843b7bfe1044f0ddfb4a118cb7cb7038d64fb2ae28aa
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
  content_hash: 56bd4f643fc6734d46569c545513342da1a4a2e611b863a525edb13ea879d8dc
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/pricing
  content_hash: d6959b095ff36f9266a76bb3ba3f39c0cd75fd2f49e2b4bb7e1d3a7b480f23d6
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
