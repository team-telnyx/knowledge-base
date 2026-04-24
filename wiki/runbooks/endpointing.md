---
title: Endpointing
summary: Silence detection for utterance boundary detection.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/endpointing
    content_hash: 21dd694a3e41844b71ed3cbf845b5a023d1bc597a87637d23b608fd378a9fa00
updated_at: 2026-04-10T00:00:00Z
---

# Endpointing

Silence detection for utterance boundary detection.

**Deepgram only.** Other engines ignore this parameter.

Controls how long Deepgram waits after silence before finalizing an utterance.

```
wss://api.telnyx.com/v2/speech-to-text/transcription?endpointing=300
```

Default: `100` ms.

## Values

| Value        | Behavior                                                                |
| ------------ | ----------------------------------------------------------------------- |
| Integer (ms) | Finalize after this many ms of silence. Lower = faster but more splits. |
| `"false"`    | Disable endpointing entirely. No automatic utterance boundaries.        |

## Trade-offs

**Low values (50–100 ms)** — Fast response. Utterances may split mid-sentence on short pauses.

**High values (300–1000 ms)** — More complete sentences. Higher latency before finalization.

**Disabled (`"false"`)** — No automatic splits. Use `Finalize` control messages to manually trigger boundaries, or rely on `CloseStream` for a single final transcript.

## Interaction With Utterance End

When endpointing triggers, Deepgram sends the final transcript followed by an utterance end event (if `utterance_end_ms` is configured server-side — currently 1000 ms).

```json theme={null}
{"transcript": "Hello, how are you?", "is_final": true}
{"transcript": "", "is_final": true, "utterance_end": true}
```

The utterance end marker signals "this speaker turn is done." See [Messages](messages.md) for details.
