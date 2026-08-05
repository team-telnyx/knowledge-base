---
title: Speech-to-Text
summary: 'Telnyx Speech-to-Text (STT) transcribes audio to text via three integration
  paths: WebSocket streaming for real-time partial and final transcripts, a REST API
  for synchronous file-based transcription, and in-call transcription for live voice
  calls. The platform supports multiple engines (Deepgram, Telnyx-hosted Whisper,
  Google, Azure, xAI, AssemblyAI, Speechmatics, Soniox, Parakeet, Reson8) selectable
  per request, with a single global endpoint and Bearer-token authentication.'
sources:
- url: https://developers.telnyx.com/docs/voice/stt/getting-started
- url: https://developers.telnyx.com/docs/voice/stt/in-call-transcription/index
- url: https://developers.telnyx.com/docs/voice/stt/migration
- url: https://developers.telnyx.com/docs/voice/stt/models
- url: https://developers.telnyx.com/docs/voice/stt/overview
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/audio-formats
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/index
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/model-config
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/models
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/parameters/response
- url: https://developers.telnyx.com/docs/voice/stt/rest-api/pricing
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/index
updated_at: 2026-08-05T14:06:51Z
---

# Speech-to-Text

*Part 3 of 7 — see also: [Part 1](speech-to-text--part-1.md), [Part 2](speech-to-text--part-2.md), [Part 4](speech-to-text--part-4.md), [Part 5](speech-to-text--part-5.md), [Part 6](speech-to-text--part-6.md), [Part 7](speech-to-text--part-7.md)*

Telnyx Speech-to-Text (STT) transcribes audio to text via three integration paths: WebSocket streaming for real-time partial and final transcripts, a REST API for synchronous file-based transcription, and in-call transcription for live voice calls. The platform supports multiple engines (Deepgram, Telnyx-hosted Whisper, Google, Azure, xAI, AssemblyAI, Speechmatics, Soniox, Parakeet, Reson8) selectable per request, with a single global endpoint and Bearer-token authentication.

## WebSocket Streaming

Real-time speech-to-text over a persistent WebSocket connection. Send audio, receive transcripts.

### Endpoint

```
wss://api.telnyx.com/v2/speech-to-text/transcription
```

You can also connect directly to the WebSocket endpoint without an HTTP upgrade:

```
wss://transcription.telnyx.com/public/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&input_format=wav
```

The same query parameters apply. Once connected, the message protocol is identical.

### Connection Lifecycle

**1. Handshake** — The connection starts as an HTTP GET with `Upgrade: websocket`. The server responds with `101 Switching Protocols`, then the connection upgrades to WebSocket frames.

```
GET /v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&input_format=wav HTTP/1.1
Host: api.telnyx.com
Upgrade: websocket
Connection: Upgrade
Authorization: Bearer YOUR_API_KEY
Sec-WebSocket-Version: 13
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
```

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

All configuration is set at connect time via query parameters — engine, model, format, language, options. Cannot be changed mid-session. Invalid parameters return a JSON error and the connection closes.

**2. Streaming** — Once connected, audio and transcription flow concurrently — no request/response pairing.

**Client → Server**

| Frame type | Content |
| --- | --- |
| binary | Audio data — raw bytes, chunked. No base64 or JSON wrapping. |
| text | `{"type": "Finalize"}` — flush buffer, force final transcript (Deepgram only) |
| text | `{"type": "CloseStream"}` — flush remaining transcription and close the stream gracefully (Deepgram, Speechmatics, Soniox) |
| text | `{"type": "KeepAlive"}` — reset idle timeout (Deepgram only) |

**Server → Client**

| Message | Description |
| --- | --- |
| Transcription result | `{"transcript": "...", "is_final": true, "confidence": 0.98}` |
| Utterance end | `{"transcript": "", "is_final": true, "utterance_end": true}` (Deepgram) |
| Error | `{"errors": [...]}` — connection closes after |

Example flow:

```
Client → Server  binary: audio chunk
Client → Server  binary: audio chunk
Client ← Server  {"transcript":"Hello","is_final":false}
Client → Server  binary: audio chunk
Client ← Server  {"transcript":"Hello, how are you?","is_final":true}
```

**3. Teardown** — Send `{"type": "CloseStream"}` (Deepgram, Speechmatics, and Soniox) to flush remaining audio and close gracefully. The server finishes processing, sends any remaining transcripts, then closes the WebSocket.

```
Client → Server  {"type":"CloseStream"}
Client ← Server  final transcript
Client ← Server  [connection closed]
```

For other engines, close the WebSocket connection directly. Dropping the connection without `CloseStream` works but may lose buffered audio on Deepgram, Speechmatics, and Soniox.

### Quickstart: Streaming a Live Audio Source

**Python**

Install:

```
pip install "websockets>=14"
```

`main.py`:

```python
import asyncio
import json
import urllib.request
import websockets

API_KEY = "YOUR_TELNYX_API_KEY"
STREAM_URL = "https://kexp-mp3-128.streamguys1.com/kexp128.mp3"

async def transcribe():
    url = (
        "wss://api.telnyx.com/v2/speech-to-text/transcription"
        "?transcription_engine=Deepgram"
        "&model=nova-3"
        "&input_format=mp3"
        "&interim_results=true"
    )
    headers = {"Authorization": f"Bearer {API_KEY}"}

    async with websockets.connect(
        url, additional_headers=headers
    ) as ws:
        # Listen for transcripts
        async def listen():
            async for message in ws:
                data = json.loads(message)
                transcript = data.get("transcript", "")
                if not transcript:
                    continue
                prefix = "FINAL" if data.get("is_final") else "partial"
                print(f"[{prefix}] {transcript}")

        listener = asyncio.create_task(listen())

        # Stream audio from KEXP Radio
        req = urllib.request.urlopen(STREAM_URL)
        try:
            while chunk := req.read(4096):
                await ws.send(chunk)
                await asyncio.sleep(0.05)
        except KeyboardInterrupt:
            pass

        await ws.send(json.dumps({"type": "CloseStream"}))
        listener.cancel()

asyncio.run(transcribe())
```

Run it:

```
python main.py
```

**Node.js**

Install:

```
npm install ws
```

`index.js`:

```javascript
const WebSocket = require("ws");
const https = require("https");

const API_KEY = "YOUR_TELNYX_API_KEY";
const STREAM_URL = "https://kexp-mp3-128.streamguys1.com/kexp128.mp3";

const url = new URL("wss://api.telnyx.com/v2/speech-to-text/transcription");
url.searchParams.set("transcription_engine", "Deepgram");
url.searchParams.set("model", "nova-3");
url.searchParams.set("input_format", "mp3");
url.searchParams.set("interim_results", "true");

const ws = new WebSocket(url.toString(), {
  headers: { Authorization: `Bearer ${API_KEY}` },
});

ws.on("open", () => {
  console.log("Connected. Streaming KEXP Radio...\n");

  https.get(STREAM_URL, (stream) => {
    stream.on("data", (chunk) => {
      if (ws.readyState === WebSocket.OPEN) {
        ws.send(chunk);
      }
    });
  });
});

ws.on("message", (data) => {
  const msg = JSON.parse(data);
  const transcript = msg.transcript || "";
  if (!transcript) return;
  const prefix = msg.is_final ? "FINAL" : "partial";
  console.log(`[${prefix}] ${transcript}`);
});

ws.on("error", (err) => console.error("Error:", err.message));
```

Run it:

```
node index.js
```

Example output:

```
Connected. Streaming KEXP Radio...

[partial] the latest news from
[partial] the latest news from the BBC
[FINAL] The latest news from the KEXP Radio.
[partial] tensions continue
[partial] tensions continue to rise in the
[FINAL] Tensions continue to rise in the region as diplomatic talks stall.
```

### Example: Streaming a WAV File

**Python**

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

    async with websockets.connect(url, additional_headers=headers) as ws:
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

**JavaScript**

```javascript
const WebSocket = require("ws");
const fs = require("fs");

const API_KEY = "YOUR_API_KEY";
const AUDIO_FILE = "audio.wav";

const url = new URL("wss://api.telnyx.com/v2/speech-to-text/transcription");
url.searchParams.set("transcription_engine", "Deepgram");
url.searchParams.set("model", "nova-3");
url.searchParams.set("input_format", "wav");
url.searchParams.set("interim_results", "true");

const ws = new WebSocket(url.toString(), {
  headers: { Authorization: `Bearer ${API_KEY}` },
});

ws.on("open", () => {
  const audio = fs.readFileSync(AUDIO_FILE);
  for (let i = 0; i < audio.length; i += 4096) {
    ws.send(audio.slice(i, i + 4096));
  }
  setTimeout(() => {
    ws.send(JSON.stringify({ type: "CloseStream" }));
    ws.close();
  }, 3000);
});

ws.on("message", (data) => {
  const msg = JSON.parse(data);
  const prefix = msg.is_final ? "FINAL" : "partial";
  console.log(`[${prefix}] ${msg.transcript || ""}`);
});

ws.on("error", (err) => console.error("Error:", err.message));
```

### WebSocket Errors

If you send an invalid parameter (unsupported engine, format, or format/engine combination), the server responds with a JSON error and closes the connection.

Error response format:

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

Error codes:

| Code | Meaning |
| --- | --- |
| `40001` | Invalid `input_format` value |
| `40002` | Format not supported by the chosen engine |
| `40003` | `sample_rate` required but missing (raw encoding or Google with non-WAV/FLAC) |
| `40004` | `sample_rate` is not a valid positive integer |
| `40005` | Invalid sample rate for the codec (e.g., `amr_nb` only supports 8000) |
| `40006` | Format not supported by Flux model |
| `40007` | Invalid `transcription_engine` value |
