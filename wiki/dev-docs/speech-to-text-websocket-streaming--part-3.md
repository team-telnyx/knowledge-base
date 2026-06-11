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

*Part 3 of 3 — see also: [Part 1](speech-to-text-websocket-streaming--part-1.md), [Part 2](speech-to-text-websocket-streaming--part-2.md)*

Real-time speech-to-text over a persistent WebSocket connection. Send audio as binary frames, receive JSON transcription results — all configuration is set at connect time via query parameters and cannot be changed mid-session.

## Errors

Invalid parameters return a JSON error and the connection closes.

```json
{
  "errors": [{
    "code": "40001",
    "title": "Invalid Parameter",
    "detail": "Unsupported input_format 'aac'. Supported formats: mp3, wav, webm, ogg, flac, ogg_opus, webm_opus, linear16, linear32, mulaw, alaw, opus, amr_nb, amr_wb, g729, speex",
    "source": { "parameter": "input_format" }
  }]
}
```

| Code | Meaning |
|---|---|
| `40001` | Invalid `input_format` value |
| `40002` | Format not supported by the chosen engine |
| `40003` | `sample_rate` required but missing (raw encoding or Google with non-WAV/FLAC) |
| `40004` | `sample_rate` is not a valid positive integer |
| `40005` | Invalid sample rate for the codec (e.g., `amr_nb` only supports 8000) |
| `40006` | Format not supported by Flux model |
| `40007` | Invalid `transcription_engine` value |

## Production Patterns

### Connection Recovery

Treat the WebSocket session as disposable. Reconnect on network failure, server close, idle timeout, and process restart.

| Event | Action |
|---|---|
| Connection fails before `open` | Retry with backoff. Do not send audio until the connection is open. |
| Connection closes unexpectedly | Stop sending audio, preserve buffered audio, reconnect, then resume streaming. |
| Error message received | Log `errors[].code`, `errors[].title`, and `errors[].source.parameter`. Reconnect only after fixing parameter errors. |
| Graceful shutdown | Send `{"type": "CloseStream"}` and wait for final transcripts before closing the socket. |

Set all query parameters on every reconnect — configuration cannot be changed mid-session.

### Backoff

Use bounded exponential backoff with jitter.

| Attempt | Base delay |
|---|---|
| 1 | 250 ms |
| 2 | 500 ms |
| 3 | 1 s |
| 4 | 2 s |
| 5+ | 5 s max |

Add random jitter of 0–500 ms per attempt. Reset the attempt counter after a stable connection. Do not retry immediately on authentication or validation errors — fix the API key, query parameters, engine, model, or format first.

### Handling Partials

Enable `interim_results=true` when the application needs live captions or low-latency UI updates.

- `is_final: false` — Display as temporary text. Replace when a newer partial arrives. Do not persist as final transcript.
- `is_final: true` — Commit to the transcript. Do not replace with later partials.
- `utterance_end: true` — Treat as a segment boundary. Do not render an empty transcript as text.

Store final transcript segments separately from the current partial to prevent duplicate text.

### Audio Buffering

Buffer audio at the producer boundary, not inside the WebSocket send loop.

| Control | Recommendation |
|---|---|
| Chunk size | Send 2048–8192 byte binary frames |
| Queue size | Set a maximum buffered duration such as 5–10 seconds |
| Backpressure | Pause or drop low-priority audio when the queue is full |
| Reconnect | Keep a short rolling buffer only if retranscription after reconnect is required |

Avoid unbounded queues. For live audio, prefer dropping stale buffered audio over sending it late.

### Keepalive

For Deepgram sessions, send `{"type": "KeepAlive"}` during long silence periods. Keep sending audio as binary frames when audio is available. For other engines, use the WebSocket client's ping/pong support and reconnect on missed heartbeats.

### Monitoring

| Metric | Purpose |
|---|---|
| Connection attempts | Detect retry loops and regional network issues |
| Connection duration | Detect unstable sessions and idle timeout patterns |
| Close code and reason | Separate expected closes from failures |
| Error codes | Identify invalid parameters and engine compatibility issues |
| Audio queue depth | Detect send-loop backpressure |
| Partial-to-final latency | Measure caption freshness |
| Final transcript count | Detect stalled recognition |
| Empty final count | Detect silence segmentation behavior |

Log `transcription_engine`, `model`, `input_format`, `sample_rate`, and `interim_results` with each session. Redact API keys and user audio.

### Graceful Shutdown

1. Drain the audio queue.
2. Send `{"type": "CloseStream"}`.
3. Wait for final transcript messages.
4. Close the WebSocket.

Set a shutdown timeout. If final messages do not arrive before the timeout, close the socket and mark the transcript as incomplete.

## Code Example

Stream a WAV file and print transcripts (Python):

```python
import asyncio
import json
import websockets

API_KEY = "YOUR_API_KEY"
AUDIO_FILE = "audio.wav"

async def transcribe():
    url = (
        "wss://api.telnyx.com/v2/speech-to-text/transcription"
        "?transcription_engine=Deepgram"
        "&model=nova-3"
        "&input_format=wav"
        "&interim_results=true"
    )
    headers = {"Authorization": f"Bearer {API_KEY}"}

    async with websockets.connect(url, extra_headers=headers) as ws:
        async def listen():
            async for message in ws:
                data = json.loads(message)
                prefix = "FINAL" if data.get("is_final") else "partial"
                print(f"[{prefix}] {data.get('transcript', '')}")

        listener = asyncio.create_task(listen())

        with open(AUDIO_FILE, "rb") as f:
            while chunk := f.read(4096):
                await ws.send(chunk)
                await asyncio.sleep(0.05)

        await asyncio.sleep(3)
        await ws.send(json.dumps({"type": "CloseStream"}))
        listener.cancel()

asyncio.run(transcribe())
```

## Pricing

Pricing varies by engine and model. Contact [Telnyx sales](https://telnyx.com/contact-us) or check the [pricing page](https://telnyx.com/pricing/speech-to-text) for current rates.
