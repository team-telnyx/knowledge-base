---
title: Telnyx TTS & STT WebSocket Streaming
summary: Reference for Telnyx's real-time Speech-to-Text (STT) and Text-to-Speech
  (TTS) WebSocket streaming APIs, including connection flows, frame formats, Python
  client examples, supported STT engines, the Telnyx Ultra voice tier with expressive
  mode and SSML emotion tags, and the broader voice catalog.
sources:
- url: https://developers.telnyx.com/docs/tts-stt/stt-websocket-streaming
- url: https://developers.telnyx.com/docs/tts-stt/telnyx-ultra-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-available-voices
- url: https://developers.telnyx.com/docs/tts-stt/tts-websocket-streaming
updated_at: 2026-07-17T09:17:04Z
---

# Telnyx TTS & STT WebSocket Streaming

*Part 1 of 3 — see also: [Part 2](telnyx-tts-stt-websocket-streaming--part-2.md), [Part 3](telnyx-tts-stt-websocket-streaming--part-3.md)*

Reference for Telnyx's real-time Speech-to-Text (STT) and Text-to-Speech (TTS) WebSocket streaming APIs, including connection flows, frame formats, Python client examples, supported STT engines, the Telnyx Ultra voice tier with expressive mode and SSML emotion tags, and the broader voice catalog.

## Overview

The Telnyx Speech-to-Text (STT) WebSocket API provides real-time audio transcription. This streaming endpoint allows you to send audio and receive transcription results incrementally, enabling low-latency voice transcription for real-time applications.

The Telnyx Text-to-Speech (TTS) WebSocket API provides real-time audio synthesis from text input. This streaming endpoint allows you to send text and receive synthesized audio incrementally, enabling low-latency voice generation for real-time applications.

This guide shows how to build a Python client to stream audio to Telnyx's Speech-to-Text (STT) engine and synthesize speech via the TTS engine using WebSocket and `asyncio`.

## Prerequisites

- **Python 3.8+**.
- A **Telnyx API key**.
- `websockets` library: `pip install websockets`.

## Speech-to-Text WebSocket

### Connection flow

The Speech-to-Text streaming process involves opening a secure WebSocket connection, streaming audio chunks, and receiving transcription events in real time.

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

The Telnyx STT service uses a WebSocket endpoint. You authenticate by passing your API key in the `Authorization` header.

The connection URL follows this format:

`wss://api.telnyx.com/v2/speech-to-text/transcription`

#### Query parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `transcription_engine` | string | No | STT engine to use (e.g., `Deepgram`, `Azure`). |
| `input_format` | string | No | Audio input format (e.g., `mp3`, `wav`). |

#### Supported engines

Telnyx offers several speech-to-text engines to process audio into transcription:

| Engine | Description |
| --- | --- |
| **Telnyx** | In-house Telnyx speech-to-text engine with significantly better transcription accuracy and lower latency. |
| **Google** | Google speech-to-text engine that offers additional features like interim results. |
| **Deepgram** | Deepgram speech-to-text engine with 3 models (`nova-2`, `nova-3`, and `flux`) that can be set using the `transcription_model` setting. |
| **Azure** | Azure speech-to-text engine with strong support for multiple languages and accents. |

### Authenticating and connecting

Create a class to handle the connection using the `websockets` library.

```python
import asyncio
import websockets

class STTClient:
    def __init__(self, token, engine="Deepgram", input_format="mp3"):
        self.url = f"wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine={engine}&input_format={input_format}"
        self.headers = {"Authorization": f"Bearer {token}"}
        self.ws = None

    async def connect(self):
        self.ws = await websockets.connect(self.url, extra_headers=self.headers)
        print("Connected to Telnyx STT")

    async def disconnect(self):
        if self.ws:
            await self.ws.close()
```

### Streaming audio

To transcribe audio, send binary frames to the WebSocket. The server processes these chunks in real time.

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

### Complete example

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
