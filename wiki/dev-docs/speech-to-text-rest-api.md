---
title: Speech-to-Text REST API
summary: Synchronous file or URL transcription via POST /v2/ai/audio/transcriptions,
  with multi‑engine support (Whisper and Deepgram), OpenAI SDK compatibility, and
  optional Deepgram-only features like diarization and word timestamps. Upload audio
  or provide a public URL (≤100 MB) and receive text immediately; timestamps and formatting
  enhancements are available when using Deepgram with model_config.
sources:
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/pricing
updated_at: 2026-05-20T10:00:56Z
---

# Speech-to-Text REST API

Synchronous file or URL transcription via POST /v2/ai/audio/transcriptions, with multi‑engine support (Whisper and Deepgram), OpenAI SDK compatibility, and optional Deepgram-only features like diarization and word timestamps. Upload audio or provide a public URL (≤100 MB) and receive text immediately; timestamps and formatting enhancements are available when using Deepgram with model_config.

## Endpoint and compatibility
- Endpoint: POST /v2/ai/audio/transcriptions
- Authentication: Authorization: Bearer <TELNYX_API_KEY>
- OpenAI SDK compatible: point your client’s base_url to https://api.telnyx.com/v2 and use your Telnyx API key; existing OpenAI transcription code works with only those swaps.
- Synchronous only: no async jobs or webhooks; responses return in the same HTTP request.

## Request format and parameters
All inputs are sent as multipart/form-data. Exactly one of file or file_url is required.

- model (string, required)
  - Values: openai/whisper-large-v3-turbo (default), openai/whisper-tiny, deepgram/nova-3
- file (file upload)
  - Mutually exclusive with file_url
- file_url (string)
  - Publicly accessible URL; server fetches before transcription; 15s download timeout; no auth headers forwarded
- language (string)
  - Language hint; behavior depends on model (see Models and features)
- response_format (string)
  - json (default) or verbose_json
- timestamp_granularities[] (string array)
  - Only valid with response_format=verbose_json; allowed value: segment
- model_config (object)
  - Deepgram-only pass-through options; using it with non-Deepgram models returns 400

## Supported audio and limits
- Maximum file size: 100 MB
- Preprocessing: audio is decoded, resampled to 16 kHz, and mixed to mono (multichannel is not supported)
- Accepted containers/codecs depend on the model and ffmpeg decode support
- Formats by model:
  - Whisper (turbo, tiny): flac, m4a, mp3, mp4, mpeg, mpga, oga, ogg, wav, webm
  - Deepgram (nova-3): mp3, wav only
- file vs file_url
  - Same validation and size checks; sending both returns 400

## Models and features
- openai/whisper-large-v3-turbo (default)
  - Multilingual (80+), auto-detects if language omitted
  - Returns text only; no timestamps (even with verbose_json)
- openai/whisper-tiny
  - Lightweight, multilingual (~50+), auto-detects if language omitted
  - Returns text only; no timestamps
- deepgram/nova-3
  - Highest accuracy for English; defaults language to en if omitted
  - English variants only (e.g., en, en-US, en-GB, en-AU, en-NZ, en-IN)
  - Advanced features via model_config: diarization, word-level timestamps, smart formatting, numerals, punctuation, utterance segmentation

## Response shapes
- response_format=json (default)
  - Returns: text
- response_format=verbose_json
  - Deepgram only: adds duration (seconds) and segments[]
  - Whisper models still return text only (no timestamps) regardless of response_format
- Segments (Deepgram when verbose_json)
  - id: zero-based segment index
  - text: segment transcript
  - start, end: seconds
  - words: array of word-level timestamps (when provided by Deepgram)
  - speakers: array of speaker labels (present when diarize=true in model_config)
- Timestamp availability by model
  - Whisper (turbo, tiny): no timestamps
  - Deepgram: segment- and word-level timestamps

## Deepgram model_config pass-through
- Only valid with model=deepgram/nova-3; otherwise returns 400
- Every key/value is forwarded directly to Deepgram’s pre-recorded API; Telnyx does not validate options
- Common options:
  - smart_format (boolean): capitalization, punctuation, dates, numbers, currency
  - punctuate (boolean): add punctuation
  - diarize (boolean): speaker identification; adds speakers to segments
  - utterance (boolean): utterance-based segmentation
  - numerals (boolean): convert spoken numbers to digits
  - language (string): override language (top-level language takes precedence)
- model_config may be sent as a JSON string in the multipart field
- See Deepgram docs for full parameter list: https://developers.deepgram.com/reference/listen-file

## Feature support summary
- Works with OpenAI SDKs (swap base_url and api_key)
- Multiple engines behind one endpoint (Whisper turbo, Whisper tiny, Deepgram nova-3)
- File upload and URL transcription
- Timestamps
  - Segment-level: with Deepgram via verbose_json
  - Word-level: Deepgram only (in segments.words)
- Diarization: Deepgram only (via model_config)
- Smart formatting: Deepgram only (via model_config)
- Multilingual
  - Whisper turbo: 80+ languages; Whisper tiny: ~50+; Deepgram: English variants only
- Not supported: async/webhooks, multichannel (audio is mixed to mono), SRT/VTT export, audio event tagging, YouTube/TikTok URLs, transcript retrieval
- File size limit: 100 MB

## Errors and validation notes
- 400 Bad Request when:
  - file and file_url are both provided or both missing
  - timestamp_granularities is used without response_format=verbose_json
  - model_config is provided with non-Deepgram models
  - Audio exceeds 100 MB or fails format validation
  - deepgram/nova-3 is used with unsupported formats (anything other than mp3, wav)
- file_url must be public and fetchable within 15s; private/authenticated URLs are not supported

## Streaming variant (experimental)
- If the request includes Accept: application/stream+json, the server can return newline-delimited JSON chunks as segments are produced (each line includes text plus start/end times)
- This behavior is not part of the public OpenAPI spec and may change

## Pricing
Pricing varies by engine and model. See https://telnyx.com/pricing/speech-to-text or contact sales at https://telnyx.com/contact-us for current rates.

## See also
- [Speech-to-Text WebSocket Streaming](speech-to-text-websocket-streaming--part-1.md) for low-latency, real-time transcription
- [In-Call Transcription](in-call-transcription.md) for transcription during live voice calls
