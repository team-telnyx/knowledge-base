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

*Part 1 of 3 — see also: [Part 2](telnyx-speech-to-text-and-text-to-speech-websocket-streaming--part-2.md), [Part 3](telnyx-speech-to-text-and-text-to-speech-websocket-streaming--part-3.md)*

Telnyx provides real-time WebSocket streaming APIs for both Speech-to-Text (STT) and Text-to-Speech (TTS), enabling low-latency audio transcription and synthesis for live voice applications. This page covers the STT and TTS WebSocket endpoints, authentication, supported engines and voices, frame formats, and complete Python examples for building bi-directional streaming clients.

## Overview

Telnyx offers two complementary WebSocket streaming APIs for real-time voice:

- **Speech-to-Text (STT) WebSocket API** — streams audio to Telnyx and receives transcription results incrementally.
- **Text-to-Speech (TTS) WebSocket API** — streams text to Telnyx and receives synthesized audio incrementally.

Both endpoints are designed for low-latency, real-time applications such as live transcription, AI voice assistants, and conversational IVR.

## Speech-to-Text WebSocket API

### Connection flow

The STT streaming process involves opening a secure WebSocket connection, streaming audio chunks, and receiving transcription events in real time:

```
Client                                   Server
   |                                        |
   |------- Connect ----------------------->|
   |<------ Connected ----------------------|
   |                                        |
   |------- Audio Frame (Binary) ---------->|
   |                                        |
   |------- Audio Frame (Binary) ---------->|
   |                                        |
   |<------ Transcript (JSON) --------------|
   |        {"transcript": "Hello"}         |
   |                                        |
   |------- Audio Frame (Binary) ---------->|
   |                                        |
   |<------ Transcript (JSON) --------------|
   |        {"transcript": "Hello world"}   |
   |                                        |
   |------- Disconnect -------------------->|
   |<------ Close --------------------------|
```

### WebSocket endpoint

The STT service uses the following WebSocket endpoint. You authenticate by passing your API key in the `Authorization` header:

```
wss://api.telnyx.com/v2/speech-to-text/transcription
```

#### Query parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `transcription_engine` | string | No | STT engine to use (e.g., `Deepgram`, `Azure`). |
| `input_format` | string | No | Audio input format (e.g., `mp3`, `wav`). |

### Supported engines

Telnyx offers several speech-to-text engines to process audio into transcription:

| Engine | Description |
| --- | --- |
| **Telnyx** | In-house Telnyx speech-to-text engine with significantly better transcription accuracy and lower latency. |
| **Google** | Google speech-to-text engine that offers additional features like interim results. |
| **Deepgram** | Deepgram speech-to-text engine with 3 models (`nova-2`, `nova-3`, and `flux`) that can be set using the `transcription_model` setting. |
| **Azure** | Azure speech-to-text engine with strong support for multiple languages and accents. |

### Authenticating and connecting

Create a class to handle the connection using the `websockets` library:

```python
import asyncio
import websockets

class STTClient:
    def __init__(self, token, engine="Deepgram", input_format="mp3"):
        self.url = f"wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine={engine}&input_format={input_format}"
        self.headers = {"Authorization": f"Bearer {token}"}
        self.ws = None

    async def connect(self):
        self.ws = await websockets.connect(self.url, additional_headers=self.headers)
        print("Connected to Telnyx STT")

    async def disconnect(self):
        if self.ws:
            await self.ws.close()
```

### Streaming audio

To transcribe audio, send binary frames to the WebSocket. The server processes these chunks in real time:

```python
    async def send_audio(self, audio_chunk):
        if self.ws:
            await self.ws.send(audio_chunk)
```

### Receiving transcripts

The server sends JSON messages back with transcription results. Add a method to listen for these messages concurrently while sending audio.

Key fields to look for in the response:

- `transcript`: The text transcription.
- `is_final`: Boolean indicating if the sentence is complete.
- `confidence`: The confidence score of the transcription.

```python
import json

    async def receive_messages(self):
        async for message in self.ws:
            data = json.loads(message)
            
            if "transcript" in data:
                print(f"Transcript: {data['transcript']} (Final: {data.get('is_final')})")
            elif "error" in data:
                print(f"Error: {data['error']}")
```

### Complete STT example

Here's how to orchestrate the bi-directional stream using `asyncio`. Use `asyncio.sleep` to simulate real-time streaming when reading from a file.

**Crucial Step:** After sending all your audio, wait for a few seconds before closing the connection. This gives the server time to send the final transcription results.

```python
async def run_transcription(api_token, audio_file_path):
    client = STTClient(api_token)
    await client.connect()

    # Task 1: Listen for transcripts
    receive_task = asyncio.create_task(client.receive_messages())

    # Task 2: Send audio chunks
    with open(audio_file_path, "rb") as f:
        while True:
            chunk = f.read(2048) # Read 2KB chunks
            if not chunk:
                break
            await client.send_audio(chunk)
            await asyncio.sleep(0.1) # Simulate delay

    # Wait for final results
    print("Audio sent. Waiting for final transcripts...")
    await asyncio.sleep(20) 
    
    await client.disconnect()
    # Cancel the listener since connection is closed
    receive_task.cancel()

# Run the async loop
# asyncio.run(run_transcription("YOUR_API_KEY", "audio.mp3"))
```
