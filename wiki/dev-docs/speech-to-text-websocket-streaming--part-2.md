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

*Part 2 of 3 — see also: [Part 1](speech-to-text-websocket-streaming--part-1.md), [Part 3](speech-to-text-websocket-streaming--part-3.md)*

Real-time speech-to-text over a persistent WebSocket connection. Send audio as binary frames, receive JSON transcription results — all configuration is set at connect time via query parameters and cannot be changed mid-session.

## Language

BCP-47 language code. Default: `en-US`. Pass `multi` (or aliases `auto`/`auto_detect`) to enable automatic language detection.

| Engine | Behavior |
|---|---|
| Deepgram | BCP-47 codes. `multi` for multi-language mode. Nova-3 supports `multi` (10 languages in code-switching). Flux supports English, Spanish, French, German, Hindi, Russian, Portuguese, Japanese, Italian, Dutch. |
| Telnyx | Whisper-based. `auto_detect` disables language hint entirely. |
| Google | BCP-47 codes. 125+ languages/locales. |
| Azure | BCP-47 codes. 100+ languages/locales. |
| xAI | Language codes such as `en`, `fr`, `de`, `ja`. 25 languages. |
| AssemblyAI | Automatic multilingual detection and code switching across 6 languages. |
| Speechmatics | Language codes such as `en`, `es`. Bilingual packs use Telnyx shorthand (e.g. `ar_en`, `cmn_en`, `en_ms`, `en_ta`, `cmn_en_ms_ta`) — mapped internally. Does not support `auto`; defaults to `en` if unrecognized. |
| Soniox | Automatic language detection. The `language` parameter is ignored. |

## Interim Results

**Deepgram, Speechmatics, and Soniox only.** Other engines ignore this parameter.

Controls whether the server sends partial (non-final) transcripts as speech is processed. Default: `false`.

- **`interim_results=false`** (default) — Server sends only final transcripts. Each message has `is_final: true`.
- **`interim_results=true`** — Server sends evolving partial transcripts, followed by a final. Partials have `is_final: false` and are replaced by the next message. Partial transcripts have `confidence: 0.0` — confidence is only meaningful on final results.

```
{"transcript": "Hello", "is_final": false, "confidence": 0.0}
{"transcript": "Hello, how", "is_final": false, "confidence": 0.0}
{"transcript": "Hello, how are you?", "is_final": true, "confidence": 0.98}
```

## Endpointing

**Deepgram, xAI, Google, Speechmatics, and Soniox.** Other engines ignore this parameter.

Controls how long the engine waits after silence before finalizing an utterance. Default: `100` ms.

- **Integer (ms)** — Finalize after this many ms of silence. Lower = faster but more splits.
- **`"false"`** — Disable endpointing entirely. No automatic utterance boundaries.

**Soniox has a different valid range**: when `transcription_engine=Soniox`, this parameter maps to `max_endpoint_delay_ms` and must be between 500 and 3000 ms. Values outside that range are rejected. Soniox endpointing is disabled unless a value in the 500–3000 ms range is provided.

**Trade-offs:**
- Low values (50–100 ms) — Fast response. Utterances may split mid-sentence on short pauses. (Deepgram, xAI, Google, Speechmatics only — below Soniox minimum.)
- High values (300–1000 ms) — More complete sentences. Higher latency before finalization.
- Soniox range (500–3000 ms) — Minimum 500 ms.
- Disabled (`"false"`) — No automatic splits. Use `Finalize` control messages to manually trigger boundaries, or rely on `CloseStream` for a single final transcript.

When endpointing triggers, Deepgram sends the final transcript followed by an utterance end event:

```
{"transcript": "Hello, how are you?", "is_final": true}
{"transcript": "", "is_final": true, "utterance_end": true}
```

## End-of-Turn Detection

**Deepgram Flux only.** These parameters return a 400 error on non-Flux models.

Flux uses a confidence-based system to decide when a speaker has finished their turn.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `eot_threshold` | float | `0.7` | Confidence threshold (0.5–0.9) for triggering `EndOfTurn`. Higher = fewer false positives, more latency. |
| `eager_eot_threshold` | float | — | Confidence threshold (0.3–0.9) for early `EagerEndOfTurn`. Not set by default — setting it enables eager mode. Must be ≤ `eot_threshold`. |
| `eot_timeout_ms` | integer | `5000` | Maximum silence in ms (500–10000) before forcing `EndOfTurn` regardless of confidence. |

**Event flow without eager mode:**

```
Speech → silence → confidence ≥ eot_threshold → EndOfTurn
Speech → silence → timeout (eot_timeout_ms) → EndOfTurn
```

**Event flow with eager mode:**

```
Speech → silence → confidence ≥ eager_eot_threshold → EagerEndOfTurn
  → speaker stays silent → confidence ≥ eot_threshold → EndOfTurn
  → speaker resumes → TurnResumed (cancel speculative work)
```

**Configuration profiles:**

- **Default** — balanced for general use: `?eot_threshold=0.7&eot_timeout_ms=5000`
- **Low-latency** — fast response, more false starts: `?eager_eot_threshold=0.4&eot_threshold=0.7&eot_timeout_ms=6000`
- **High-reliability** — fewer interruptions, more latency: `?eot_threshold=0.85&eot_timeout_ms=8000`

Typical `eager_eot_threshold` range: 0.3–0.5 for ~150–250 ms latency savings at the cost of ~50–70% more LLM calls.

## Keyword Boosting

**Deepgram only.** Other engines ignore these parameters.

| Model | Parameter | Format |
|---|---|---|
| Flux | `keyterm` | Comma-separated terms, no intensifiers |
| Nova-3 | `keyterm` | Comma-separated terms, no intensifiers |
| Nova-2 | `keywords` | `keyword:intensifier` format |
| Nova | `keywords` | `keyword:intensifier` format |

Examples:

```
?keyterm=Telnyx,WebRTC,SIP
?keywords=Telnyx:2&keywords=telephony:1
```

## Redaction

**Deepgram only.** Other engines ignore this parameter.

Replaces sensitive data in transcripts with placeholder text. Multiple values can be comma-separated.

| Value | Redacts |
|---|---|
| `pci` | Credit card numbers |
| `ssn` | Social Security numbers |
| `numbers` | All numeric sequences |

Redacted content is replaced in the transcript text. There is no way to get the un-redacted version once redaction is enabled for a session.

```
{"transcript": "My card number is [REDACTED]", "is_final": true}
```

## Wire Protocol

### Client → Server

**Audio data** — Binary WebSocket frames containing raw audio bytes. No base64, no JSON wrapping. Recommended chunk size: 2048–8192 bytes.

**Control messages** — JSON text frames with a `type` field:

| Type | Effect | Engine support |
|---|---|---|
| `Finalize` | Flush audio buffer, force a final transcript | Deepgram only |
| `CloseStream` | End session, close connection gracefully | Deepgram, Speechmatics, Soniox |
| `KeepAlive` | Reset idle timeout | Deepgram only |

Unknown text frames are silently ignored.

### Server → Client

All server messages are JSON text frames.

**Transcription result** — Emitted for each recognized speech segment (partial or final):

| Field | Type | Present | Description |
|---|---|---|---|
| `transcript` | string | Always | Transcribed text |
| `is_final` | boolean | Always | `true` = finalized segment. `false` = interim (may revise). |
| `speech_final` | boolean | Deepgram | `true` = speaker stopped talking |
| `confidence` | float | When available | 0.0–1.0 confidence score |
| `utterance_end` | boolean | Deepgram | `true` = silence-triggered utterance boundary |

**Utterance end** — Emitted on speaker pause (Deepgram). Empty transcript, `is_final: true`.

**Error** — Emitted on validation or connection errors. Connection closes shortly after.

### Message Flow Examples

**`interim_results=false`** (default):

```
Client:  [binary audio frames]
Server:  {"transcript": "Hello, how are you today?", "is_final": true, "speech_final": true, "confidence": 0.98}
Client:  [binary audio frames]
Server:  {"transcript": "I'm doing well.", "is_final": true, "speech_final": true, "confidence": 0.95}
Client:  {"type": "CloseStream"}
         [connection closed]
```

**`interim_results=true`**:

```
Client:  [binary audio frames]
Server:  {"transcript": "Hello", "is_final": false, "speech_final": false}
Server:  {"transcript": "Hello, how are", "is_final": false, "speech_final": false}
Server:  {"transcript": "Hello, how are you today?", "is_final": true, "speech_final": true, "confidence": 0.98}
```

Partials are best-effort and may revise. Only `is_final: true` results are stable.
