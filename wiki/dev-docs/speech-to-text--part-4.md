---
title: Speech-to-Text
summary: 'Telnyx Speech-to-Text (STT) transcribes audio to text via three integration
  paths: WebSocket streaming for real-time partial and final transcripts, a REST API
  for synchronous file-based transcription, and in-call transcription for live voice
  calls. The platform supports multiple engines (Deepgram, Telnyx-hosted Whisper,
  Google, Azure, xAI, AssemblyAI, Speechmatics, Soniox, Parakeet, Reson8) selectable
  per request, with a single global endpoint and Bearer-token authentication.'
sources:
- url: https://developers.telnyx.com/docs/voice/stt/getting-started
- url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
- url: https://developers.telnyx.com/docs/voice/stt/migration
- url: https://developers.telnyx.com/docs/voice/stt/models
- url: https://developers.telnyx.com/docs/voice/stt/overview
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/pricing
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/index
updated_at: 2026-08-05T14:06:51Z
---

# Speech-to-Text

*Part 4 of 7 — see also: [Part 1](speech-to-text--part-1.md), [Part 2](speech-to-text--part-2.md), [Part 3](speech-to-text--part-3.md), [Part 5](speech-to-text--part-5.md), [Part 6](speech-to-text--part-6.md), [Part 7](speech-to-text--part-7.md)*

Telnyx Speech-to-Text (STT) transcribes audio to text via three integration paths: WebSocket streaming for real-time partial and final transcripts, a REST API for synchronous file-based transcription, and in-call transcription for live voice calls. The platform supports multiple engines (Deepgram, Telnyx-hosted Whisper, Google, Azure, xAI, AssemblyAI, Speechmatics, Soniox, Parakeet, Reson8) selectable per request, with a single global endpoint and Bearer-token authentication.

## REST API

`POST /v2/ai/audio/transcriptions` — Synchronous file transcription. Upload audio or pass a URL, get text back.

The endpoint is OpenAI SDK compatible — swap `base_url` and `api_key` and your existing code works.

### Feature Support

| Feature | Status |
| --- | --- |
| OpenAI SDK compatible | **Yes** — swap `base_url` and `api_key`, existing code works |
| Multi-engine selection | **Yes** — 3 models behind one endpoint |
| File upload | **Yes** |
| URL transcription | **Yes** (`file_url`) |
| Timestamps (segment) | **Yes** (`verbose_json`) |
| Timestamps (word-level) | **Deepgram only** (via `model_config`) |
| Diarization | **Deepgram only** (via `model_config`) |
| Smart formatting | **Deepgram only** (via `model_config`) |
| Multilingual | **Model-dependent** — whisper-turbo: 80+ languages, whisper-tiny: 50+ languages, Deepgram models support language coverage based on the selected model |
| Async / webhooks | No |
| Multichannel | No (forced mono) |
| Export formats (SRT/VTT) | No |
| Audio event tagging | No |
| YouTube/TikTok URL | No |
| Transcript retrieval | No |
| File size limit | 100 MB |

### Quick Start

**Python**

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

**JavaScript**

```javascript
import OpenAI from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: "YOUR_TELNYX_API_KEY",
  baseURL: "https://api.telnyx.com/v2",
});

const result = await client.audio.transcriptions.create({
  model: "openai/whisper-large-v3-turbo",
  file: fs.createReadStream("audio.mp3"),
});
```

**cURL**

```
curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
  -H "Authorization: Bearer YOUR_TELNYX_API_KEY" \
  -F model="openai/whisper-large-v3-turbo" \
  -F file=@audio.mp3
```

Or transcribe from a URL (no file upload needed):

```
curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
  -H "Authorization: Bearer YOUR_TELNYX_API_KEY" \
  -F model="openai/whisper-large-v3-turbo" \
  -F file_url="https://example.com/audio.mp3"
```

Example response:

```json
{
  "text": "The latest news from the KEXP Radio. Tensions continue to rise in the region as diplomatic talks stall."
}
```

For segment- or word-level timestamps, use `model="deepgram/nova-3"` with `response_format=verbose_json`. The Whisper models (`openai/whisper-large-v3-turbo`, `openai/whisper-tiny`) return text only.

### REST Parameters

All parameters are sent as `multipart/form-data`.

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `model` | string | Yes | Model to use for transcription. Values: `openai/whisper-large-v3-turbo` (default), `openai/whisper-tiny`, `deepgram/nova-3` |
| `file` | file | One of `file`/`file_url` | Audio file to transcribe. Mutually exclusive with `file_url`. |
| `file_url` | string | One of `file`/`file_url` | Publicly accessible URL to an audio file. Mutually exclusive with `file`. |
| `language` | string | No | Language hint. Behavior varies by model. |
| `response_format` | string | No | Output shape. Values: `json` (default), `verbose_json` |
| `timestamp_granularities[]` | string | No | Timestamp detail level. Only valid with `response_format=verbose_json` — returns 400 otherwise. Values: `segment` |
| `model_config` | object | No | Deepgram-specific options. Only valid with `deepgram/nova-3` — returns 400 for other models. |

### REST Models

Your choice of `model` determines which audio formats are accepted, what `language` values are valid, and what response fields are available.

|  | `openai/whisper-large-v3-turbo` | `openai/whisper-tiny` | `deepgram/nova-3` |
| --- | --- | --- | --- |
| **Default** | Yes |  |  |
| **Audio formats** | All 10 | All 10 | mp3, wav only |
| **Language** | 80+ languages, auto-detected | 50+ languages, auto-detected | English variants only (`en`, `en-US`, `en-GB`, `en-AU`, `en-NZ`, `en-IN`) |
| **Timestamps** | No | No | Word-level (via `model_config`) |
| **Diarization** | No | No | Yes (via `model_config`) |
| **Smart formatting** | No | No | Yes (via `model_config`) |
| **`model_config`** | Returns 400 | Returns 400 | Deepgram pass-through |

**`openai/whisper-large-v3-turbo`** — Default model. Multilingual. Auto-detected if `language` omitted. Returns text only — no timestamps regardless of `response_format`.

**`openai/whisper-tiny`** — Lightweight, lowest resource usage. Multilingual (50+ languages, auto-detected). Returns text only — no timestamps.

**`deepgram/nova-3`** — Highest accuracy for English. Advanced features (diarization, word timestamps, smart formatting, numerals, punctuation) available via `model_config`. Defaults `language` to `en` if omitted. Can also set `language` inside `model_config` — top-level field takes precedence.

### Audio Formats

Applies to both `file` (multipart upload) and `file_url` (URL download).

- **Max size:** 100 MB
- **Processing:** All audio is decoded, resampled to 16kHz, and mixed to mono via ffmpeg before transcription. Container format doesn't matter as long as ffmpeg can decode it — the validated extension list is the actual restriction.

| Format | `whisper-turbo` | `whisper-tiny` | `deepgram/nova-3` |
| --- | --- | --- | --- |
| flac | Yes | Yes | No |
| m4a | Yes | Yes | No |
| mp3 | Yes | Yes | **Yes** |
| mp4 | Yes | Yes | No |
| mpeg | Yes | Yes | No |
| mpga | Yes | Yes | No |
| oga | Yes | Yes | No |
| ogg | Yes | Yes | No |
| wav | Yes | Yes | **Yes** |
| webm | Yes | Yes | No |

`file` vs `file_url`:

|  | `file` | `file_url` |
| --- | --- | --- |
| Delivery | Multipart upload in request body | Server downloads from URL before transcription |
| Timeout | Request timeout | 15s download timeout |
| Auth | N/A | URL must be publicly accessible (no auth headers forwarded) |
| Validation | Same format and size checks | Same format and size checks |

One of `file` or `file_url` is required. Sending both returns 400.

### Model Config

Deepgram only. Returns 400 if used with other models.

Pass-through to [Deepgram's pre-recorded API](https://developers.deepgram.com/docs/pre-recorded-audio) query parameters. Every key-value pair in `model_config` is forwarded directly — Telnyx does not validate individual options.

Commonly used options:

| Option | Type | Description |
| --- | --- | --- |
| `smart_format` | boolean | Capitalization, punctuation, dates, numbers, currency |
| `punctuate` | boolean | Add punctuation |
| `diarize` | boolean | Speaker identification. Adds `speakers` array to `verbose_json` segments. |
| `utterance` | boolean | Segment transcript into utterances |
| `numerals` | boolean | Convert spoken numbers to digits |
| `language` | string | Override language. Top-level `language` param takes precedence. |

Example:

```
curl -X POST https://api.telnyx.com/v2/ai/audio/transcriptions \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -F "file=@call-recording.mp3" \
  -F "model=deepgram/nova-3" \
  -F "response_format=verbose_json" \
  -F 'model_config={"smart_format": true, "diarize": true, "punctuate": true}'
```

`model_config` can be sent as a JSON string in the multipart form field. The server parses it before forwarding.

Any Deepgram query parameter can be passed. If Deepgram adds new options, they work immediately without a Telnyx API update. Conversely, invalid keys are forwarded and may cause Deepgram to return an error. Refer to [Deepgram's API reference](https://developers.deepgram.com/reference/listen-file) for the full list of supported parameters.

### Response Format

Controlled by the `response_format` parameter.

**`json` (Default)** — Text only:

```json
{
  "text": "The quick brown fox jumps over the lazy dog."
}
```

**`verbose_json`** — Adds `duration` (seconds) and timestamped `segments` — **only when using `deepgram/nova-3`**. The Whisper models (`openai/whisper-large-v3-turbo`, `openai/whisper-tiny`) return text only regardless of `response_format`.

Example response with `model=deepgram/nova-3`:

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

Set `timestamp_granularities[]=segment` alongside `response_format=verbose_json`. Using `timestamp_granularities` without `verbose_json` returns 400.

Segment fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | integer | Zero-indexed segment number |
| `text` | string | Segment transcript |
| `start` | float | Start time in seconds |
| `end` | float | End time in seconds |
| `words` | array | Word-level timestamps (present when the backend provides them — Deepgram only) |
| `speakers` | array | Speaker labels (present when `diarize=true` in `model_config` — Deepgram only) |

Timestamp availability by model:

| Model | `verbose_json` timestamps |
| --- | --- |
| `openai/whisper-large-v3-turbo` | **No timestamps** — backend returns text only |
| `openai/whisper-tiny` | **No timestamps** — backend returns text only |
| `deepgram/nova-3` | Segment-level + word-level (from Deepgram response) |

Sending `Accept: application/stream+json` returns newline-delimited JSON chunks as segments are transcribed. Each line:

```
{"text": "segment text", "start": 0.0, "end": 3.42}
```

This is used internally but not in the public OAS spec.

### Pricing

Pricing for REST API STT varies by engine and model. Contact [sales](https://telnyx.com/contact-us) or check the [pricing page](https://telnyx.com/pricing/speech-to-text) for current rates.
