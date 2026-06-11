---
title: Speech-to-Text WebSocket Streaming
summary: Real-time speech-to-text over a persistent WebSocket connection. Send audio
  as binary frames, receive JSON transcription results — all configuration is set
  at connect time via query parameters and cannot be changed mid-session.
sources:
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/index
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
updated_at: 2026-06-11T10:46:55Z
---

# Speech-to-Text WebSocket Streaming

*Part 1 of 3 — see also: [Part 2](speech-to-text-websocket-streaming--part-2.md), [Part 3](speech-to-text-websocket-streaming--part-3.md)*

Real-time speech-to-text over a persistent WebSocket connection. Send audio as binary frames, receive JSON transcription results — all configuration is set at connect time via query parameters and cannot be changed mid-session.

## Endpoint

```
wss://api.telnyx.com/v2/speech-to-text/transcription
```

An alternative direct WebSocket endpoint is also available:

```
wss://transcription.telnyx.com/public/speech-to-text/transcription
```

Both accept the same query parameters and use the same message protocol after connection.

## Connection Lifecycle

### Handshake

The connection starts as an HTTP GET with `Upgrade: websocket`. The server responds with `101 Switching Protocols`, then the connection upgrades to WebSocket frames. Authentication is via the `Authorization: Bearer YOUR_API_KEY` header. Invalid parameters return a JSON error and the connection closes.

### Streaming

Once connected, audio and transcription flow concurrently — there is no request/response pairing. All configuration is set at connect time via query parameters and cannot be changed mid-session.

### Teardown

Send `{"type": "CloseStream"}` (Deepgram, Speechmatics, and Soniox) to flush remaining audio and close gracefully. The server finishes processing, sends any remaining transcripts, then closes the WebSocket. For other engines, close the WebSocket connection directly. Dropping the connection without `CloseStream` works but may lose buffered audio on Deepgram, Speechmatics, and Soniox.

## Parameters

All parameters are passed as query string values on the WebSocket URL.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `transcription_engine` | string | `Deepgram` | Engine: `Deepgram`, `Telnyx`, `Google`, `Azure`, `xAI`, `AssemblyAI`, `Speechmatics`, `Soniox` |
| `model` | string | per engine | See [Speech-to-Text WebSocket Streaming#Engines & Models](speech-to-text-websocket-streaming-engines-models.md) |
| `input_format` | string | `mp3` | See [Speech-to-Text WebSocket Streaming#Audio Formats](speech-to-text-websocket-streaming-audio-formats.md) |
| `sample_rate` | integer | `16000` | Hz. Required for raw encodings (`linear16`, `mulaw`, `alaw`). Ignored for container formats. |
| `language` | string | `en-US` | BCP-47 code. `multi`/`auto`/`auto_detect` for auto-detection. See [Speech-to-Text WebSocket Streaming#Language](speech-to-text-websocket-streaming-language.md) |
| `interim_results` | string | `false` | `"true"` for partial transcripts. See [Speech-to-Text WebSocket Streaming#Interim Results](speech-to-text-websocket-streaming-interim-results.md) |
| `endpointing` | string | `100` | Silence detection in ms. `"false"` to disable. See [Speech-to-Text WebSocket Streaming#Endpointing](speech-to-text-websocket-streaming-endpointing.md) |
| `redact` | string | — | PII redaction (Deepgram only). `pci`, `ssn`, `numbers`, or comma-separated combo |
| `keyterm` | string | — | Comma-separated boost terms (Deepgram Nova-3/Flux) |
| `keywords` | string | — | Legacy keyword boosting with intensifiers (Deepgram Nova/Nova-2) |
| `region` | string | `eastus` | Azure Speech Services region |
| `eot_threshold` | float | `0.7` | Flux only. End-of-turn confidence threshold |
| `eot_timeout_ms` | integer | `5000` | Flux only. Max silence before forcing EndOfTurn |
| `eager_eot_threshold` | float | — | Flux only. Speculative EagerEndOfTurn threshold. Disabled by default |

Example:

```
wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&input_format=wav&language=en-US&interim_results=true
```

## Audio Formats

Set via the `input_format` query parameter. Audio is sent as binary WebSocket frames — chunked bytes, no base64, no JSON wrapping.

Container formats (mp3, webm, ogg, wav, flac) are self-describing: the server demuxes the byte stream and extracts encoding/sample rate from headers. Raw formats have no metadata, so you must set `sample_rate` explicitly.

### Browser Capture

| Format | Sample rate | Notes |
|---|---|---|
| `webm` | from header | WebM container |
| `webm_opus` | from header | WebM + Opus. Valid: 8000–48000. Alias: `webm-opus` |
| `ogg_opus` | from header | Ogg + Opus. Valid: 8000–48000. Alias: `ogg-opus` |
| `ogg` | from header | Ogg container (Vorbis or other) |

### Telephony

Raw frames; `sample_rate` required.

| Format | Sample rate | Notes |
|---|---|---|
| `mulaw` | any | G.711 µ-law. North America. Default: 8000 Hz. |
| `alaw` | any | G.711 A-law. EU/international. Default: 8000 Hz. |
| `g729` | 8000 | G.729. Fixed. |
| `amr_nb` | 8000 | AMR narrowband. Fixed. Alias: `amr-nb` |
| `amr_wb` | 16000 | AMR wideband. Fixed. Alias: `amr-wb` |
| `speex` | 8000, 16000, 32000 | Google: 16000 only. |

### Raw PCM

Uncompressed audio. `sample_rate` required.

| Format | Sample rate | Notes |
|---|---|---|
| `linear16` | any | 16-bit signed PCM, little-endian (s16le). Default: 16000 Hz. |
| `linear32` | any | 32-bit float PCM, little-endian (f32le). Default: 16000 Hz. |
| `opus` | 8000, 12000, 16000, 24000, 48000 | Raw Opus frames, no container. Deepgram also: 44100. |

### Recorded File

Pre-recorded files read in chunks. Container headers carry sample rate.

| Format | Sample rate | Notes |
|---|---|---|
| `mp3` | from header | Default for most engines |
| `wav` | from header | Uncompressed. Default for Flux model. |
| `flac` | from header | Lossless compression |

### Engine Compatibility

Unsupported format/engine combinations return error `40002`. Unsupported Flux formats return error `40006`.

| Format | Deepgram Nova | Deepgram Flux | Telnyx | Google | Azure | Speechmatics | Soniox |
|---|---|---|---|---|---|---|---|
| mp3 | ✓ | | ✓ | ✓ | ✓ | ✓ | ✓ |
| wav | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| webm | ✓ | ✓ | | | | | ✓ |
| ogg | ✓ | ✓ | | | | ✓ | ✓ |
| flac | ✓ | | | ✓ | | ✓ | ✓ |
| ogg_opus | ✓ | ✓ | | ✓ | | | |
| webm_opus | ✓ | | | ✓ | | | |
| linear16 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| linear32 | ✓ | ✓ | ✓ | | | ✓ | ✓ |
| mulaw | ✓ | ✓ | | ✓ | | ✓ | ✓ |
| alaw | ✓ | ✓ | | | | | ✓ |
| opus | ✓ | ✓ | | | | | |
| amr_nb | ✓ | | | ✓ | | | |
| amr_wb | ✓ | | | ✓ | | | |
| g729 | ✓ | | | | | | |
| speex | ✓ | | | ✓ | | | |

Universal formats (all engines and models): `wav`, `linear16`.

## Engines & Models

| Engine | Default model | Other models | Notes |
|---|---|---|---|
| **Deepgram** | `nova-3` | `nova-2`, `flux` | Default engine. Broadest format support. |
| **Telnyx** | `openai/whisper-tiny` | — | On-network, lightweight |
| **Google** | `latest_long` | — | Multilingual, long-form |
| **Azure** | `azure/fast` | — | Broad language/accent coverage |
| **xAI** | `xai/grok-stt` | — | Grok STT for real-time transcription |
| **AssemblyAI** | `assemblyai/universal-streaming` | — | Universal-Streaming for low-latency voice agents |
| **Speechmatics** | `speechmatics/standard` | — | High-accuracy real-time transcription with multilingual and bilingual packs |
| **Soniox** | `soniox/stt-rt-v4` | — | Real-time transcription with automatic language detection |

Deepgram Flux is the lowest-latency model with built-in end-of-turn detection, designed for real-time voice agents. It is the most restrictive format-wise — it drops `mp3`, `flac`, `webm_opus`, `amr_nb`, `amr_wb`, `g729`, and `speex` compared to Nova.
