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

*Part 4 of 4 — see also: [Part 1](speech-to-text-websocket-streaming--part-1.md), [Part 2](speech-to-text-websocket-streaming--part-2.md), [Part 3](speech-to-text-websocket-streaming--part-3.md)*

The Telnyx Speech-to-Text WebSocket streaming endpoint accepts real-time audio over a single WebSocket connection and returns transcription results as JSON text frames. All session configuration is passed as query parameters on the connection URL and locked at connect time; audio is sent as binary frames and control messages as JSON. The endpoint supports multiple transcription engines and models, a wide range of audio formats, language selection, interim results, endpointing, keyword boosting, redaction, and Deepgram Flux end-of-turn detection, with production guidance for connection recovery, buffering, keepalive, and graceful shutdown.

## Production Patterns

Use these patterns when running the standalone WebSocket STT endpoint in production.

### Connection Recovery

Treat the WebSocket session as disposable. Reconnect on network failure, server close, idle timeout, and process restart.

| Event | Action |
| --- | --- |
| Connection fails before `open` | Retry with backoff. Do not send audio until the connection is open. |
| Connection closes unexpectedly | Stop sending audio, preserve buffered audio, reconnect, then resume streaming. |
| Error message received | Log `errors[].code`, `errors[].title`, and `errors[].source.parameter`. Reconnect only after fixing parameter errors. |
| Graceful shutdown | Send `{"type": "CloseStream"}` and wait for final transcripts before closing the socket. |

Set all query parameters on every reconnect. STT configuration cannot be changed mid-session.

### Backoff

Use bounded exponential backoff with jitter.

| Attempt | Base delay |
| --- | --- |
| 1 | 250 ms |
| 2 | 500 ms |
| 3 | 1 s |
| 4 | 2 s |
| 5+ | 5 s max |

Add random jitter of 0–500 ms per attempt. Reset the attempt counter after a stable connection. Do not retry immediately on authentication or validation errors. Fix the API key, query parameters, engine, model, or format first.

### Partials

Enable `interim_results=true` when the application needs live captions or low-latency UI updates.

| Message | Handling |
| --- | --- |
| `is_final: false` | Display as temporary text. Replace it when a newer partial arrives. Do not persist it as final transcript. |
| `is_final: true` | Commit to the transcript. Do not replace it with later partials. |
| `utterance_end: true` | Treat as a segment boundary. Do not render an empty transcript as text. |

Store final transcript segments separately from the current partial. This prevents duplicate text when a final result arrives after one or more interim results.

### Audio Buffering

Buffer audio at the producer boundary, not inside the WebSocket send loop.

| Control | Recommendation |
| --- | --- |
| Chunk size | Send 2048–8192 byte binary frames. |
| Queue size | Set a maximum buffered duration, such as 5–10 seconds. |
| Backpressure | Pause or drop low-priority audio when the queue is full. |
| Reconnect | Keep a short rolling buffer only if retranscription after reconnect is required. |

Avoid unbounded queues. A slow or disconnected socket should not grow memory usage indefinitely. For live audio, prefer dropping stale buffered audio over sending it late. Late audio increases transcript delay and can make captions appear out of sync.

### Keepalive

For Deepgram sessions, send `{"type": "KeepAlive"}` during long silence periods. Keep sending audio as binary frames when audio is available. For other engines, use the WebSocket client's ping/pong support when available and reconnect on missed heartbeats.

### Monitoring

Track connection, latency, transcript, and buffer metrics.

| Metric | Purpose |
| --- | --- |
| Connection attempts | Detect retry loops and regional network issues. |
| Connection duration | Detect unstable sessions and idle timeout patterns. |
| Close code and reason | Separate expected closes from failures. |
| Error codes | Identify invalid parameters and engine compatibility issues. |
| Audio queue depth | Detect send-loop backpressure. |
| Partial-to-final latency | Measure caption freshness. |
| Final transcript count | Detect stalled recognition. |
| Empty final count | Detect silence segmentation behavior. |

Log the selected `transcription_engine`, `model`, `input_format`, `sample_rate`, and `interim_results` value with each session. Redact API keys and user audio.

### Shutdown

Use graceful shutdown for planned stops:

1. Drain the audio queue.
2. Send `{"type": "CloseStream"}`.
3. Wait for final transcript messages.
4. Close the WebSocket.

Set a shutdown timeout. If final messages do not arrive before the timeout, close the socket and mark the transcript as incomplete.

## Pricing

Pricing for WebSocket STT varies by engine and model. Contact [sales](https://telnyx.com/contact-us) or check the [pricing page](https://telnyx.com/pricing/speech-to-text) for current rates.
