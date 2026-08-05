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

*Part 3 of 4 — see also: [Part 1](speech-to-text-websocket-streaming--part-1.md), [Part 2](speech-to-text-websocket-streaming--part-2.md), [Part 4](speech-to-text-websocket-streaming--part-4.md)*

The Telnyx Speech-to-Text WebSocket streaming endpoint accepts real-time audio over a single WebSocket connection and returns transcription results as JSON text frames. All session configuration is passed as query parameters on the connection URL and locked at connect time; audio is sent as binary frames and control messages as JSON. The endpoint supports multiple transcription engines and models, a wide range of audio formats, language selection, interim results, endpointing, keyword boosting, redaction, and Deepgram Flux end-of-turn detection, with production guidance for connection recovery, buffering, keepalive, and graceful shutdown.

## End-of-Turn Detection

Deepgram Flux only. These parameters return a 400 error on non-Flux models. Flux uses a confidence-based system to decide when a speaker has finished their turn.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `eot_threshold` | float | `0.7` | Confidence threshold (`0.5`–`0.9`) for triggering an `EndOfTurn` event. Higher values require more certainty the speaker is done — fewer false positives but slightly more latency. Lower values respond faster but may cut speakers off mid-thought. |
| `eager_eot_threshold` | float | — | Confidence threshold (`0.3`–`0.9`) for triggering an early `EagerEndOfTurn` event. Not set by default — setting it enables eager mode. When fired, your agent can start generating a response speculatively. If the speaker resumes, a `TurnResumed` event cancels it. Must be ≤ `eot_threshold`. Lower values = earlier triggers, more false starts. Typical range: `0.3`–`0.5` for ~150–250 ms latency savings at the cost of ~50–70% more LLM calls. |
| `eot_timeout_ms` | integer | `5000` | Maximum silence in ms (`500`–`10000`) before forcing `EndOfTurn` regardless of confidence. Resets when speech resumes. Increase for speakers who pause frequently; decrease for rapid-fire Q&A. |

### Event Flow

Without eager mode (`eot_threshold` only):

```
Speech → silence → confidence ≥ eot_threshold → EndOfTurn
Speech → silence → timeout (eot_timeout_ms) → EndOfTurn
```

With eager mode (`eager_eot_threshold` set):

```
Speech → silence → confidence ≥ eager_eot_threshold → EagerEndOfTurn
  → speaker stays silent → confidence ≥ eot_threshold → EndOfTurn
  → speaker resumes → TurnResumed (cancel speculative work)
```

### Configuration Profiles

**Default** — balanced for general use:

```
?eot_threshold=0.7&eot_timeout_ms=5000
```

**Low-latency** — fast response, more false starts:

```
?eager_eot_threshold=0.4&eot_threshold=0.7&eot_timeout_ms=6000
```

**High-reliability** — fewer interruptions, more latency:

```
?eot_threshold=0.85&eot_timeout_ms=8000
```

## Keyword Boosting

Deepgram only. Other engines ignore these parameters. Two parameters control keyword boosting, targeting different Deepgram model generations.

### `keyterm` — Nova-3 and Flux

Comma-separated list of terms to boost. Simple — no intensifiers.

```
?keyterm=Telnyx,WebRTC,SIP
```

Deepgram Nova-3 and Flux only. Ignored on older models.

### `keywords` — Nova (Legacy)

Terms with optional intensity scores. Format: `keyword:intensifier`.

```
?keywords=Telnyx:2
```

Deepgram Nova only. Not supported on Flux (silently ignored).

### Which To Use

| Model | Parameter |
| --- | --- |
| Flux | `keyterm` |
| Nova-3 | `keyterm` |
| Nova | `keywords` |
| Nova-2 | `keywords` |

### Examples

Boost multiple terms on Nova-3:

```
?transcription_engine=Deepgram&model=nova-3&keyterm=Telnyx,SIP,RTP,WebRTC
```

Boost with intensifiers on legacy Nova:

```
?transcription_engine=Deepgram&model=nova&keywords=Telnyx:2&keywords=telephony:1
```

## Redaction

Deepgram only. Other engines ignore this parameter. Replaces sensitive data in transcripts with placeholder text.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?redact=pci
```

| Value | Redacts |
| --- | --- |
| `pci` | Credit card numbers |
| `ssn` | Social Security numbers |
| `numbers` | All numeric sequences |

Multiple values can be passed as comma-separated:

```
?redact=pci,ssn
```

Redacted content is replaced in the transcript text. The exact replacement format depends on the Deepgram model:

```
{"transcript": "My card number is [REDACTED]", "is_final": true}
```

Redaction applies to final and interim results. There is no way to get the un-redacted version once redaction is enabled for a session.

## Messages

The WebSocket carries two frame types: binary frames (audio) from client to server, and JSON text frames in both directions.

### Client → Server

**Audio Data** — Binary WebSocket frames containing raw audio bytes. No base64, no JSON wrapping. Recommended chunk size: 2048–8192 bytes. Smaller chunks reduce latency; larger chunks reduce round trips.

```
[binary frame: audio bytes]
```

**Control Messages** — JSON text frames with a `type` field.

```
{"type": "Finalize"}
{"type": "CloseStream"}
{"type": "KeepAlive"}
```

| Type | Effect | Engine support |
| --- | --- | --- |
| `Finalize` | Flush audio buffer, force a final transcript | Deepgram only |
| `CloseStream` | End session, close connection gracefully | Deepgram, Speechmatics, Soniox |
| `KeepAlive` | Reset idle timeout | Deepgram only |

Unknown text frames are silently ignored.

### Server → Client

All server messages are JSON text frames.

**Transcription Result** — Emitted for each recognized speech segment (partial or final):

```
{
  "transcript": "Hello, how are you today?",
  "is_final": true,
  "speech_final": true,
  "confidence": 0.98
}
```

| Field | Type | Present | Description |
| --- | --- | --- | --- |
| `transcript` | string | Always | Transcribed text |
| `is_final` | boolean | Always | `true` = finalized segment. `false` = interim (may revise). |
| `speech_final` | boolean | Deepgram | `true` = speaker stopped talking |
| `confidence` | float | When available | 0.0–1.0 confidence score |
| `utterance_end` | boolean | Deepgram | `true` = silence-triggered utterance boundary |

**Utterance End** — Emitted on speaker pause (Deepgram). Empty transcript, `is_final: true`:

```
{
  "transcript": "",
  "is_final": true,
  "utterance_end": true
}
```

**Error** — Emitted on validation or connection errors. Connection closes shortly after:

```
{
  "errors": [
    {
      "code": "40002",
      "title": "Unsupported format",
      "detail": "Format 'flac' is not supported by engine 'Azure'",
      "source": {"parameter": "input_format"}
    }
  ]
}
```

| Field | Type | Description |
| --- | --- | --- |
| `errors` | array | One or more error objects |
| `errors[].code` | string | Error code |
| `errors[].title` | string | Short description |
| `errors[].detail` | string | Human-readable explanation |
| `errors[].source.parameter` | string | Query parameter that caused the error |

### Message Flow

With `interim_results=false` (default), the server sends only final transcripts:

```
Client:  [binary audio frames]
Server:  {"transcript": "Hello, how are you today?", "is_final": true, "speech_final": true, "confidence": 0.98}
Client:  [binary audio frames]
Server:  {"transcript": "I'm doing well.", "is_final": true, "speech_final": true, "confidence": 0.95}
Client:  {"type": "CloseStream"}
         [connection closed]
```

With `interim_results=true`, the server sends partials, then final:

```
Client:  [binary audio frames]
Server:  {"transcript": "Hello", "is_final": false, "speech_final": false}
Server:  {"transcript": "Hello, how are", "is_final": false, "speech_final": false}
Server:  {"transcript": "Hello, how are you today?", "is_final": true, "speech_final": true, "confidence": 0.98}
```

Partials are best-effort and may revise. Only `is_final: true` results are stable.
