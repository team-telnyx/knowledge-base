---
title: Telnyx Speech-to-Text and Text-to-Speech WebSocket Streaming
summary: Telnyx provides real-time WebSocket streaming APIs for both Speech-to-Text
  (STT) and Text-to-Speech (TTS), enabling low-latency audio transcription and synthesis
  for live voice applications. This page covers the STT and TTS WebSocket endpoints,
  authentication, supported engines and voices, frame formats, and complete Python
  examples for building bi-directional streaming clients.
sources:
- url: https://developers.telnyx.com/docs/tts-stt/stt-websocket-streaming
- url: https://developers.telnyx.com/docs/tts-stt/telnyx-ultra-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-available-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-websocket-streaming
updated_at: 2026-08-05T14:01:43Z
---

# Telnyx Speech-to-Text and Text-to-Speech WebSocket Streaming

*Part 2 of 3 — see also: [Part 1](telnyx-speech-to-text-and-text-to-speech-websocket-streaming--part-1.md), [Part 3](telnyx-speech-to-text-and-text-to-speech-websocket-streaming--part-3.md)*

Telnyx provides real-time WebSocket streaming APIs for both Speech-to-Text (STT) and Text-to-Speech (TTS), enabling low-latency audio transcription and synthesis for live voice applications. This page covers the STT and TTS WebSocket endpoints, authentication, supported engines and voices, frame formats, and complete Python examples for building bi-directional streaming clients.

## Text-to-Speech WebSocket API

### WebSocket endpoint

#### Connection URL

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice={voice_id}
```

#### Query parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `voice` | string | Yes | Voice identifier (e.g., `Telnyx.NaturalHD.astra`) |
| `inactivity_timeout` | integer | No | Time without message to keep the WebSocket open (default: 20 seconds) |

#### Authentication

Include your Telnyx API key as an `Authorization` header in the connection request:

```
Authorization: Bearer YOUR_API_KEY
```

#### Example connection

```python
import websockets

url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
headers = {
    "Authorization": "Bearer YOUR_API_KEY"
}

websocket = await websockets.connect(url, additional_headers=headers)
```

### Connection flow

The TTS WebSocket follows this lifecycle:

1. **Connect** — Establish WebSocket connection with authentication.
2. **Initialize** — Send initialization frame with a space character.
3. **Send Text** — Send one or more text frames to synthesize.
4. **Receive Audio** — Receive audio frames with base64-encoded mp3 data.
5. **Stop** — Send empty text frame to signal completion.
6. **Close** — Connection closes after processing completes.

```
Client                          Server
  |                               |
  |------- Connect -------------->|
  |<------ Connected -------------|
  |                               |
  |------- Init Frame ----------->|
  |       {"text": " "}           |
  |                               |
  |------- Text Frame ----------->|
  |       {"text": "Hello"}       |
  |                               |
  |<------ Audio Frame -----------|
  |       {"audio": "base64..."}  |
  |<------ Audio Frame -----------|
  |       {"audio": "base64..."}  |
  |                               |
  |------- Stop Frame ----------->|
  |       {"text": ""}            |
  |                               |
  |<------ Close -----------------|
```

### Frame types

#### Outbound frames (Client → Server)

All outbound frames are JSON text messages.

**1. Initialization frame** — Initialize the TTS session:

```json
{
  "text": " "
}
```

```python
import json

init_frame = {"text": " "}
await websocket.send(json.dumps(init_frame))
```

Notes:
- Must be sent first after connection.
- Contains a single space character.
- Required to begin the session.

**2. Text frame** — Send text content to be synthesized into speech:

```json
{
  "text": "Your text content here"
}
```

```python
text_frame = {"text": "Hello, this is a test of the Telnyx TTS service."}
await websocket.send(json.dumps(text_frame))
```

Multiple text frames can be sent sequentially:

```python
frames = [
    {"text": "First sentence."},
    {"text": "Second sentence."},
    {"text": "Third sentence."}
]

for frame in frames:
    await websocket.send(json.dumps(frame))
    await asyncio.sleep(0.5)
```

Notes:
- Can send multiple text frames in one session.
- Each frame is processed and synthesized separately.
- Audio is returned incrementally for each text frame.

**3. Stop frame** — Signal completion of text input and end the session:

```json
{
  "text": ""
}
```

```python
stop_frame = {"text": ""}
await websocket.send(json.dumps(stop_frame))
```

Notes:
- Contains an empty string.
- Signals the server to finish processing.
- Should be sent after all text frames.

#### Inbound frames (Server → Client)

The server sends JSON text messages containing synthesized audio data.

**Audio frame** — Deliver synthesized audio data:

```json
{
  "audio": "UklGRiQAAABXQVZFZm10IBAAAAABAAEAQB8AAAB9AAACABAAZGF0YQAAAAA="
}
```

```python
import base64

async for message in websocket:
    data = json.loads(message)

    if "audio" in data:
        # Decode base64 audio
        audio_bytes = base64.b64decode(data["audio"])

        # Save or process audio
        with open("output.mp3", "ab") as f:
            f.write(audio_bytes)
```

Audio specifications:

| Property | Value |
| --- | --- |
| Format | mp3 |
| Sample Rate | 16 kHz |
| Bit Depth | 16-bit |
| Channels | Mono (1) |
| Encoding | Base64 |

Notes:
- Multiple audio frames may be received for a single text input.
- Each audio chunk is a complete mp3 file with headers.
- Chunks should be concatenated in the order received.
- Use append mode when saving to file to preserve all audio.

### Complete TTS example

```python
import asyncio
import json
import base64
import websockets

async def tts_example():
    # 1. Connect to WebSocket
    url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
    headers = {
        "Authorization": "Bearer YOUR_API_KEY"
    }

    async with websockets.connect(url, additional_headers=headers) as ws:
        print("Connected to TTS WebSocket")

        # 2. Send initialization frame
        init_frame = {"text": " "}
        await ws.send(json.dumps(init_frame))
        print("Sent: Initialization frame")

        # 3. Send text frame
        text_frame = {"text": "Hello, welcome to Telnyx Text-to-Speech streaming."}
        await ws.send(json.dumps(text_frame))
        print("Sent: Text frame")

        # 4. Receive audio frames
        audio_count = 0
        async for message in ws:
            data = json.loads(message)

            if "audio" in data:
                audio_count += 1
                audio_bytes = base64.b64decode(data["audio"])

                # Append audio chunks to file
                with open("output.mp3", "ab") as f:
                    f.write(audio_bytes)

                print(f"Received: Audio frame #{audio_count} ({len(audio_bytes)} bytes)")

                # After receiving audio, send stop frame
                if audio_count >= 10:  # Adjust based on your needs
                    # 5. Send stop frame
                    stop_frame = {"text": ""}
                    await ws.send(json.dumps(stop_frame))
                    print("Sent: Stop frame")

        print("Connection closed")

asyncio.run(tts_example())
```

Expected output:

```
Connected to TTS WebSocket
Sent: Initialization frame
Sent: Text frame
Received: Audio frame #1 (8192 bytes)
Received: Audio frame #2 (6144 bytes)
Received: Audio frame #3 (4096 bytes)
Sent: Stop frame
Connection closed
```

### TTS configuration summary

Required configuration:

```python
# WebSocket URL
ENDPOINT = "wss://api.telnyx.com/v2/text-to-speech/speech"
VOICE_ID = "Telnyx.NaturalHD.astra"
URL = f"{ENDPOINT}?voice={VOICE_ID}"

# Authentication Header
HEADERS = {
    "Authorization": "Bearer YOUR_API_KEY"
}
```

Message sequence:

```python
# 1. Initialization
{"text": " "}

# 2. Text to synthesize (can send multiple)
{"text": "Your text here"}

# 3. Stop signal
{"text": ""}
```

### TTS troubleshooting

| Issue | Solution |
| --- | --- |
| Connection fails | Verify token format: `Bearer YOUR_API_KEY` |
| No audio received | Ensure initialization frame sent first |
| Audio is garbled | Check base64 decoding and file append mode |
| Empty audio file | Confirm text frame contains valid content |

## Available TTS voices

Telnyx gives you access to a wide range of voices through one API. Choose from Telnyx's own voice tiers — Natural, NaturalHD, and [Ultra](telnyx-ultra-voices.md) — as well as third-party providers like xAI Grok, AWS Polly, Azure, ElevenLabs, Inworld, MiniMax, ResembleAI, and Rime. Mix and match providers and models to balance quality, tone, and cost for every interaction.

For configuration details on third-party providers, see the [Text-to-Speech guide](text-to-speech-guide.md). You can also create your own custom voices using [Voice Design](voice-design.md).
