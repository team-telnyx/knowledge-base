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

*Part 3 of 4 — see also: [Part 1](telnyx-voice-platform--part-1.md), [Part 2](telnyx-voice-platform--part-2.md), [Part 4](telnyx-voice-platform--part-4.md)*

Covers two major Telnyx Voice capabilities: STIR/SHAKEN call authentication (attestation levels, certificate hosting, SIP header verification) and Speech-to-Text transcription (WebSocket streaming, REST file upload, in-call transcription, multi-engine model selection, and provider migration).

## STT REST API

Synchronous file transcription at `POST /v2/ai/audio/transcriptions`. Upload audio or pass a URL, get text back. The endpoint is **OpenAI SDK compatible** — swap `base_url` and `api_key` and existing code works.

### Feature Support

| Feature | Status |
|---|---|
| OpenAI SDK compatible | Yes |
| Multi-engine selection | Yes — 3 models behind one endpoint |
| File upload | Yes |
| URL transcription | Yes (`file_url`) |
| Timestamps (segment) | Yes (`verbose_json`) |
| Timestamps (word-level) | Deepgram only (via `model_config`) |
| Diarization | Deepgram only (via `model_config`) |
| Smart formatting | Deepgram only (via `model_config`) |
| Multilingual | Model-dependent |
| Async / webhooks | No |
| Multichannel | No (forced mono) |
| Export formats (SRT/VTT) | No |
| Audio event tagging | No |
| YouTube/TikTok URL | No |
| Transcript retrieval | No |
| File size limit | 100 MB |

### Quick Start (Python)

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_TELNYX_API_KEY",
    base_url="https://api.telnyx.com/v2",
)

result = client.audio.transcriptions.create(
    model="openai/whisper-large-v3-turbo",
    file=open("audio.mp3", "rb"),
)
```

### REST API Parameters

All parameters are sent as `multipart/form-data`.

| Parameter | Type | Description |
|---|---|---|
| `model` | string (required) | `openai/whisper-large-v3-turbo` (default), `openai/whisper-tiny`, or `deepgram/nova-3` |
| `file` | file | Audio file to transcribe. Mutually exclusive with `file_url` |
| `file_url` | string | Publicly accessible URL to an audio file. Mutually exclusive with `file` |
| `language` | string | Language hint. Behavior varies by model |
| `response_format` | string | `json` (default) or `verbose_json` |
| `timestamp_granularities[]` | string | Only valid with `verbose_json`. Values: `segment` |
| `model_config` | object | Deepgram-specific options. Only valid with `deepgram/nova-3`; returns 400 for other models |

### Model Capabilities (REST)

| | `openai/whisper-large-v3-turbo` | `openai/whisper-tiny` | `deepgram/nova-3` |
|---|---|---|---|
| Default | Yes | | |
| Audio formats | All 10 | All 10 | mp3, wav only |
| Language | 80+ languages, auto-detected | 50+ languages, auto-detected | English variants only (`en`, `en-US`, `en-GB`, `en-AU`, `en-NZ`, `en-IN`) |
| Timestamps | No | No | Word-level (via `model_config`) |
| Diarization | No | No | Yes (via `model_config`) |
| Smart formatting | No | No | Yes (via `model_config`) |
| `model_config` | Returns 400 | Returns 400 | Deepgram pass-through |

### Audio Formats

Applies to both `file` (multipart upload) and `file_url` (URL download).

- **Max size:** 100 MB
- **Processing:** All audio is decoded, resampled to 16 kHz, and mixed to mono via ffmpeg before transcription. Container format doesn't matter as long as ffmpeg can decode it.

| Format | `whisper-turbo` | `whisper-tiny` | `deepgram/nova-3` |
|---|---|---|---|
| flac | Yes | Yes | No |
| m4a | Yes | Yes | No |
| mp3 | Yes | Yes | Yes |
| mp4 | Yes | Yes | No |
| mpeg | Yes | Yes | No |
| mpga | Yes | Yes | No |
| oga | Yes | Yes | No |
| ogg | Yes | Yes | No |
| wav | Yes | Yes | Yes |
| webm | Yes | Yes | No |

#### `file` vs `file_url`

| | `file` | `file_url` |
|---|---|---|
| Delivery | Multipart upload in request body | Server downloads from URL before transcription |
| Timeout | Request timeout | 15 s download timeout |
| Auth | N/A | URL must be publicly accessible (no auth headers forwarded) |

One of `file` or `file_url` is required. Sending both returns 400.

### Model Config (Deepgram Only)

Pass-through to Deepgram's pre-recorded API query parameters. Every key-value pair in `model_config` is forwarded directly — Telnyx does not validate individual options. Invalid keys are forwarded and may cause Deepgram to return an error. Returns 400 if used with non-Deepgram models.

Commonly used options:

| Option | Type | Description |
|---|---|---|
| `smart_format` | boolean | Capitalization, punctuation, dates, numbers, currency |
| `punctuate` | boolean | Add punctuation |
| `diarize` | boolean | Speaker identification. Adds `speakers` array to `verbose_json` segments |
| `utterance` | boolean | Segment transcript into utterances |
| `numerals` | boolean | Convert spoken numbers to digits |
| `language` | string | Override language. Top-level `language` param takes precedence |

Example:

```
curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -F "file=@call-recording.mp3" \
  -F "model=deepgram/nova-3" \
  -F "response_format=verbose_json" \
  -F 'model_config={"smart_format": true, "diarize": true, "punctuate": true}'
```

`model_config` can be sent as a JSON string in the multipart form field.

### Response Format

#### `json` (Default)

Text only:

```json
{ "text": "The quick brown fox jumps over the lazy dog." }
```

#### `verbose_json`

Adds `duration` (seconds) and timestamped `segments` — **only when using `deepgram/nova-3`**. The Whisper models return text only regardless of `response_format`.

Set `timestamp_granularities[]=segment` alongside `response_format=verbose_json`. Using `timestamp_granularities` without `verbose_json` returns 400.

Example with `model=deepgram/nova-3`:

```json
{
  "text": "The quick brown fox jumps over the lazy dog.",
  "duration": 3.42,
  "segments": [
    {
      "id": 0,
      "text": "The quick brown fox jumps over the lazy dog.",
      "start": 0.0,
      "end": 3.42
    }
  ]
}
```

Segment fields:

| Field | Type | Description |
|---|---|---|
| `id` | integer | Zero-indexed segment number |
| `text` | string | Segment transcript |
| `start` | float | Start time in seconds |
| `end` | float | End time in seconds |
| `words` | array | Word-level timestamps (Deepgram only) |
| `speakers` | array | Speaker labels (when `diarize=true` in `model_config` — Deepgram only) |

Timestamp availability:

| Model | `verbose_json` timestamps |
|---|---|
| `openai/whisper-large-v3-turbo` | No timestamps |
| `openai/whisper-tiny` | No timestamps |
| `deepgram/nova-3` | Segment-level + word-level |

#### Streaming Response (Undocumented)

Sending `Accept: application/stream+json` returns newline-delimited JSON chunks as segments are transcribed. Each line: `{"text": "segment text", "start": 0.0, "end": 3.42}`. This is used internally but not in the public OAS spec.
