---
title: Speech-to-Text WebSocket Streaming
summary: 'Real-time speech-to-text over a persistent WebSocket: send binary audio
  frames, receive interim and final transcripts. Configure engine, model, format,
  language, and options via query parameters at connect time. This page covers endpoints,
  lifecycle, parameters, audio formats, wire protocol, errors, production guidance,
  pricing, and an end-to-end example.'
sources:
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/index
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/index
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/audio-formats
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/end-of-turn
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/endpointing
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/engines-and-models
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/interim-results
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/keyword-boosting
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/language
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/redaction
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/pricing
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/production-patterns
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/responses
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/examples
updated_at: 2026-05-20T10:05:31Z
---

# Speech-to-Text WebSocket Streaming

*Part 2 of 2 — see also: [Part 1](speech-to-text-websocket-streaming--part-1.md)*

Real-time speech-to-text over a persistent WebSocket: send binary audio frames, receive interim and final transcripts. Configure engine, model, format, language, and options via query parameters at connect time. This page covers endpoints, lifecycle, parameters, audio formats, wire protocol, errors, production guidance, pricing, and an end-to-end example.

## Endpointing (Deepgram)

- Controls how long Deepgram waits after silence before finalizing an utterance.
- Values:
  - Integer milliseconds (e.g., 100, 300, 1000): lower = faster but more splits; higher = more complete sentences but higher latency.
  - "false": disable automatic endpointing; you can manually segment with Finalize or rely on CloseStream for a single final transcript.
- Interaction: when endpointing triggers, Deepgram typically sends a final transcript, then an utterance_end marker (empty transcript with is_final true) signaling the turn boundary.

## Language Selection and Auto-Detection

- Use BCP-47 language codes (e.g., en-US, es, fr). Default is en-US.
- Auto detection: pass multi (Deepgram). Aliases auto and auto_detect are mapped to multi. Telnyx Whisper-based engine treats auto_detect as disabling the language hint entirely.
- Engine notes:
  - Deepgram: BCP-47 codes; multi for multi-language mode; Flux is English-only.
  - Telnyx (Whisper): 50+ languages; auto_detect disables the hint.
  - Google and Azure: BCP-47 codes.
  - xAI: short codes such as en, fr, de, ja.
  - AssemblyAI: automatic multilingual detection and code switching across supported languages.
  - Speechmatics: standard codes (e.g., en, es) plus Telnyx shorthand for bilingual/multilingual packs (e.g., ar_en); Telnyx maps shorthand internally; no auto; defaults to en if unrecognized.
- Common codes include en or en-US, en-GB, es, fr, de, pt-BR, it, ja, zh, hi, ar, ko, and multi (Deepgram auto).

## Keyword Boosting (Deepgram)

- keyterm (Nova-3 and Flux): comma-separated boosted terms, e.g., keyterm=Telnyx,SIP,WebRTC
- keywords (Nova/Nova-2 legacy): terms with optional intensifiers, e.g., keywords=Telnyx:2&keywords=telephony:1
- Which to use: Flux and Nova-3 → keyterm; Nova/Nova-2 → keywords.

## Redaction (Deepgram)

- Enable with redact parameter; values: pci (credit cards), ssn (US Social Security numbers), numbers (all numeric sequences). Multiple values are comma-separated.
- Redaction is applied to interim and final results; redacted content is replaced in the transcript text. There is no way to retrieve un-redacted text within that session.

## Errors and Close Behavior

- Invalid parameters produce an error message and the server closes the connection.
- Error payload structure includes:
  - errors[].code (string): see list below
  - errors[].title (short description)
  - errors[].detail (human-readable explanation)
  - errors[].source.parameter (the offending query parameter)
- Common error codes:
  - 40001 — invalid input_format value
  - 40002 — format not supported by the chosen engine
  - 40003 — sample_rate required but missing (raw encodings or Google with non-WAV/FLAC)
  - 40004 — sample_rate is not a valid positive integer
  - 40005 — invalid sample rate for the codec (e.g., amr_nb must be 8000)
  - 40006 — format not supported by Flux
  - 40007 — invalid transcription_engine value

## Production Patterns and Operational Guidance

Connection recovery
- Treat sessions as disposable; reconnect on network failure, server close, idle timeout, and process restart.
- On unexpected close: stop sending audio, preserve buffered audio as needed, reconnect, then resume streaming.
- On parameter errors: log the code/title/detail/parameter and fix configuration before retrying.
- For graceful shutdown: send CloseStream and wait for final transcripts before closing the socket.

Backoff strategy
- Use bounded exponential backoff with jitter (e.g., 250 ms, 500 ms, 1 s, 2 s, then max ~5 s) and add 0–500 ms random jitter. Reset the counter after a stable connection.

Handling partials
- When interim_results=true: render is_final=false text as temporary; replace it as newer partials arrive; only commit is_final=true to storage. Treat utterance_end=true as a segment boundary and do not render the empty transcript.

Audio buffering and flow control
- Send binary frames of ~2–8 KB. Maintain a bounded queue (e.g., 5–10 seconds). Apply backpressure: pause or drop low-priority audio when full. Prefer dropping stale live audio over sending it late.
- Keep a short rolling buffer only if you need retranscription after reconnect.

Keepalive and heartbeats
- Deepgram: send {"type":"KeepAlive"} during long silences.
- Other engines: rely on client ping/pong when available and reconnect on missed heartbeats.

Monitoring
- Track connection attempts, duration, close code/reason, error codes, audio queue depth, partial-to-final latency, final transcript count, and empty final count. Log chosen engine/model/format/sample_rate/interim_results; never log API keys or user audio.

Shutdown
- Drain audio queue, send CloseStream, wait for finals, then close the WebSocket. Use a timeout and mark the transcript incomplete if finals do not arrive in time.

## Pricing

- Pricing varies by engine and model. Contact Telnyx sales or see the public pricing page for current rates.

## Example: Stream a WAV File in Python

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
