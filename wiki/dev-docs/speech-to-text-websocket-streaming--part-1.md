---
title: Speech-to-Text WebSocket Streaming
summary: The Telnyx Speech-to-Text WebSocket streaming endpoint accepts real-time
  audio over a single WebSocket connection and returns transcription results as JSON
  text frames. All session configuration is passed as query parameters on the connection
  URL and locked at connect time; audio is sent as binary frames and control messages
  as JSON. The endpoint supports multiple transcription engines and models, a wide
  range of audio formats, language selection, interim results, endpointing, keyword
  boosting, redaction, and Deepgram Flux end-of-turn detection, with production guidance
  for connection recovery, buffering, keepalive, and graceful shutdown.
sources:
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/audio-formats
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/end-of-turn
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/endpointing
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/engines-and-models
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/index
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/interim-results
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/keyword-boosting
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/language
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/redaction
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/pricing
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/production-patterns
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/responses
updated_at: 2026-08-05T14:06:24Z
---

# Speech-to-Text WebSocket Streaming

*Part 1 of 4 — see also: [Part 2](speech-to-text-websocket-streaming--part-2.md), [Part 3](speech-to-text-websocket-streaming--part-3.md), [Part 4](speech-to-text-websocket-streaming--part-4.md)*

The Telnyx Speech-to-Text WebSocket streaming endpoint accepts real-time audio over a single WebSocket connection and returns transcription results as JSON text frames. All session configuration is passed as query parameters on the connection URL and locked at connect time; audio is sent as binary frames and control messages as JSON. The endpoint supports multiple transcription engines and models, a wide range of audio formats, language selection, interim results, endpointing, keyword boosting, redaction, and Deepgram Flux end-of-turn detection, with production guidance for connection recovery, buffering, keepalive, and graceful shutdown.

## Overview

The standalone WebSocket STT endpoint is exposed at `wss://api.telnyx.com/v2/speech-to-text/transcription`. All session configuration is passed as query string parameters on the URL and is locked at connection time — parameters cannot be changed mid-session. Audio is sent from client to server as binary WebSocket frames (chunked bytes, no base64, no JSON wrapping), and JSON text frames are used for control messages and server responses in both directions.

A typical connection looks like:

```
wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&input_format=wav&language=en-US&interim_results=true
```

## Engines and Models

The `transcription_engine` and `model` query parameters select the underlying speech recognition provider. Deepgram is the default engine and offers the broadest format support.

| Engine | Default model | Other models | Notes |
| --- | --- | --- | --- |
| **Deepgram** | `nova-3` | `nova-2`, `flux`, `flux-multi` | Default engine. Broadest format support. |
| **Telnyx** | `openai/whisper-tiny` | — | On-network, lightweight |
| **Google** | `latest_long` | — | Multilingual, long-form |
| **Azure** | `azure/fast` | — | Broad language/accent coverage |
| **xAI** | `xai/grok-stt` | — | Grok STT for real-time transcription |
| **AssemblyAI** | `assemblyai/universal-streaming` | — | Universal-Streaming (backed by Universal-3.5 Pro Realtime) for low-latency voice agents |
| **Speechmatics** | `speechmatics/standard` | — | High-accuracy real-time transcription with multilingual and bilingual packs |
| **Soniox** | `soniox/stt-rt-v4` | — | Real-time transcription with automatic language detection |
| **Parakeet** | `nvidia/parakeet-v3` | — | Self-hosted multilingual transcription with automatic language detection. Final results only. |
| **Reson8** | `reson8/turns` | — | Turn-based transcription of 10 European languages with automatic language detection. |

Deepgram's Flux model is its lowest-latency option with built-in [End-of-Turn Detection](end-of-turn-detection.md). `flux` is English-only; `flux-multi` adds code-switching across English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, and Dutch (plus `auto`). See [Audio Formats](audio-formats.md) for the formats Flux supports.

## Audio Formats

The `input_format` query parameter selects the audio encoding. Container formats (mp3, webm, etc.) are self-describing — the server demuxes the byte stream and extracts encoding and sample rate from headers. Raw formats have no metadata, so `sample_rate` must be set explicitly. Invalid sample rates return error 40005.

### Browser Capture

Output from `MediaRecorder` or similar browser APIs. Container headers carry sample rate.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?input_format=webm_opus
```

| Format | Sample rate | Notes |
| --- | --- | --- |
| `webm` | from header | WebM container |
| `webm_opus` | from header | WebM + Opus. Valid: 8000–48000. Alias: `webm-opus` |
| `ogg_opus` | from header | Ogg + Opus. Valid: 8000–48000. Alias: `ogg-opus` |
| `ogg` | from header | Ogg container (Vorbis or other) |

### Telephony

Codecs from voice networks. Raw frames, `sample_rate` required.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?input_format=mulaw&sample_rate=8000
```

| Format | Sample rate | Notes |
| --- | --- | --- |
| `mulaw` | any | G.711 µ-law. North America. Default: 8000 Hz. |
| `alaw` | any | G.711 A-law. EU/international. Default: 8000 Hz. |
| `g729` | 8000 | G.729. Fixed. |
| `amr_nb` | 8000 | AMR narrowband. Fixed. Alias: `amr-nb` |
| `amr_wb` | 16000 | AMR wideband. Fixed. Alias: `amr-wb` |
| `speex` | 8000, 16000, 32000 | Google: 16000 only. |

### Raw PCM

Uncompressed audio from microphones, processing pipelines, or SDKs. `sample_rate` required.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?input_format=linear16&sample_rate=16000
```

| Format | Sample rate | Notes |
| --- | --- | --- |
| `linear16` | any | 16-bit signed PCM, little-endian (s16le). Default: 16000 Hz. |
| `linear32` | any | 32-bit float PCM, little-endian (f32le). Default: 16000 Hz. |
| `opus` | 8000, 12000, 16000, 24000, 48000 | Raw Opus frames, no container. Deepgram also: 44100. |

### Recorded File

Pre-recorded files read in chunks and streamed through the socket. Container headers carry sample rate.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?input_format=mp3
```

| Format | Sample rate | Notes |
| --- | --- | --- |
| `mp3` | from header | Default for most engines |
| `wav` | from header | Uncompressed. Default for Flux model. |
| `flac` | from header | Lossless compression |

### Engine Compatibility

Unsupported format/engine combinations return error 40002. Unsupported Flux formats return error 40006. Flux is the most restrictive of Deepgram's models — it drops `mp3`, `flac`, `webm_opus`, `amr_nb`, `amr_wb`, `g729`, and `speex` compared to Nova.

| Format | Deepgram Nova | Deepgram Flux | Telnyx | Google | Azure | Speechmatics | Soniox | Parakeet | Reson8 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| mp3 | ✓ |  | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| wav | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |  |
| webm | ✓ | ✓ |  |  |  |  | ✓ |  |  |
| ogg | ✓ | ✓ |  |  |  | ✓ | ✓ |  |  |
| flac | ✓ |  |  | ✓ |  | ✓ | ✓ |  |  |
| ogg_opus | ✓ | ✓ |  | ✓ |  |  |  |  |  |
| webm_opus | ✓ |  |  | ✓ |  |  |  |  |  |
| linear16 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| linear32 | ✓ | ✓ | ✓ |  |  | ✓ | ✓ | ✓ | ✓ |
| mulaw | ✓ | ✓ |  | ✓ |  | ✓ | ✓ |  | ✓ |
| alaw | ✓ | ✓ |  |  |  |  | ✓ |  | ✓ |
| opus | ✓ | ✓ |  |  |  |  |  |  |  |
| amr_nb | ✓ |  |  | ✓ |  |  |  |  |  |
| amr_wb | ✓ |  |  | ✓ |  |  |  |  |  |
| g729 | ✓ |  |  |  |  |  |  |  |  |
| speex | ✓ |  |  | ✓ |  |  |  |  |  |

Reson8 accepts raw formats only (`linear16`, `linear32`, `mulaw`, `alaw`) at any sample rate — container formats are not supported. `linear16` is the only format supported by every engine and model.
