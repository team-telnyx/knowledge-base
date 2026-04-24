---
title: Interim Results
summary: Partial transcription behavior and message flow differences.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/interim-results
    content_hash: f64d8d336d1695e44a637cf3e3926146e2845edf2f50f475ad0f11ce006226e2
updated_at: 2026-04-10T00:00:00Z
---

# Interim Results

Partial transcription behavior and message flow differences.

**Deepgram only.** Other engines ignore this parameter.

Controls whether the server sends partial (non-final) transcripts as speech is processed.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?interim_results=true
```

Default: `false`. Pass `"true"` as a string.

**`interim_results=false`** (default) — Server sends only final transcripts. Each message has `is_final: true`. Lower message volume, higher latency per result.

```json theme={null}
{"transcript": "Hello, how are you?", "is_final": true, "confidence": 0.98}
```

**`interim_results=true`** — Server sends evolving partial transcripts as audio is processed, followed by a final. Partials have `is_final: false` and are replaced by the next message.

```json theme={null}
{"transcript": "Hello", "is_final": false, "confidence": 0.0}
{"transcript": "Hello, how", "is_final": false, "confidence": 0.0}
{"transcript": "Hello, how are you?", "is_final": true, "confidence": 0.98}
```

> **Note:** Partial transcripts have `confidence: 0.0` — confidence is only meaningful on final results.
