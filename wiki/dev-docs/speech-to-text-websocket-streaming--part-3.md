---
title: Speech-to-Text WebSocket Streaming
summary: Real-time speech-to-text over a persistent WebSocket connection. Send audio
  as binary frames, receive JSON transcription results — all configuration is set
  at connect time via query parameters and cannot be changed mid-session.
sources:
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/errors
  content_hash: 24bdbc8f31b24bb9025cd06e0720f19213e535dc8d870523544af7fa81582adc
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/examples
  content_hash: 4294b110b6684122c3d220b57e8aa132d7bd5aa58ed18701cf2b778384aefe5b
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/index
  content_hash: ce2a470f6e6022a5b6f829b7dfa76ea4087a4926fea0ae45c99dae8679235128
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/audio-formats
  content_hash: 16cf6d4a4b1a8ff2a3c495bc4ab7607d5d75ebf24b681921aeae66315ec4ef19
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/end-of-turn
  content_hash: 159958b703db53e6b7c52a3e07a7b9862add8bdfe847fd467a00ee988a79e002
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/endpointing
  content_hash: eed2b58435f9cc915eaa4310946f0e0cd99e19b16dd208a2a654913c1fa0c045
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/engines-and-models
  content_hash: ffca0d0738cb6f6e6c6a4739ed808032d31b0d81263ce6f7ac29a8a46cdb6afa
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/index
  content_hash: 7ab90b8dbaeeb0f025121ef2b36aade371eef3ee937e5cc8b69751b0d53dea3b
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/interim-results
  content_hash: f3a5dfb61fc2ac35321d8de21b31d417ab94cc2de458034e200eacc5ee20180a
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/keyword-boosting
  content_hash: bdfd68fcd4e84a24eff4c9c912d6ab82bef8b41afe1f00d01925779bf331e75d
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/language
  content_hash: 8bb115e5fcbef787883a74db2a8784f3d6243f3689170ec23866cab65d958fad
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/redaction
  content_hash: 3526be7f342f9303fdefe0ec28ac900ccb0c0c3ce8aabcd4c4e1d25c81f76125
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/pricing
  content_hash: 3b2ed3368ec525b8a13216049e0cc01e57d27701bbcbd21a22b09567ce426568
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/production-patterns
  content_hash: c97293533540b0438a91cc6390ab76366220f19152513ba3e9a3f356fcddd35b
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/responses
  content_hash: e1268df1998d11a2023fcee2c972f9d32c81bafa5c0f70d80bb5dd505c6da612
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
