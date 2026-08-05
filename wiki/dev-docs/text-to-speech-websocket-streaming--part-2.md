---
title: Text-to-Speech WebSocket Streaming
summary: Real-time text-to-speech over a persistent WebSocket connection. Send text,
  receive audio. This page covers the connection lifecycle, message protocol, voice
  settings, and code examples for streaming synthesis with barge-in and LLM token
  support.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/index
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/messages
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/parameters/voice-settings
updated_at: 2026-08-05T14:06:55Z
---

# Text-to-Speech WebSocket Streaming

*Part 2 of 2 — see also: [Part 1](text-to-speech-websocket-streaming--part-1.md)*

Real-time text-to-speech over a persistent WebSocket connection. Send text, receive audio. This page covers the connection lifecycle, message protocol, voice settings, and code examples for streaming synthesis with barge-in and LLM token support.

## Voice Settings

`voice_settings` is an object sent in the handshake frame to configure provider-specific parameters:

```json
{
  "text": " ",
  "voice_settings": {
    "voice_speed": 1.2
  }
}
```

### Telnyx Natural

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_speed` | float | 1.0 | Speech rate. Values > 1 are faster. |

### Telnyx NaturalHD

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_speed` | float | 1.0 | Speech rate. Values > 1 are faster. |

### Telnyx Ultra

Telnyx Ultra is **REST-only** — not available over WebSocket. These settings apply to the REST API.

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_speed` | float | 1.0 | Speech rate. Values > 1 are faster. |
| `language_boost` | string | — | Target language |
| `volume` | float | — | Volume level |
| `emotion` | string | — | Emotion: `neutral`, `happy`, `sad`, `angry`, `fearful`, `disgusted`, `surprised` |

### Telnyx Qwen3TTS

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `language_boost` | string | `"Auto"` | Target language. Accepted: `Auto`, `English`, `Chinese`, `French`, `German`, `Italian`, `Japanese`, `Korean`, `Portuguese`, `Russian`, `Spanish`, or ISO codes (`en`, `zh`, etc.) |

### Azure Speech

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `language_code` | string | `"en-US"` | Language code |
| `text_type` | string | `"text"` | Input type: `text` or `ssml` |
| `effect` | string | — | Audio effect: `eq_car` or `eq_telecomhp8k` |
| `gender` | string | — | Voice gender filter: `Male` or `Female` |

### AWS Polly

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `language_code` | string | — | BCP-47 language code |
| `output_format` | string | — | Audio format override |
| `engine` | string | `"standard"` | Polly engine: `standard`, `neural`, `generative`, `long-form` |
| `text_type` | string | `"text"` | Input type: `text` or `ssml` |
| `lexicon_names` | array | — | Pronunciation lexicon names |

### Minimax

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `speed` | float | — | Speech rate |
| `vol` | float | — | Volume |
| `pitch` | integer | — | Pitch adjustment |
| `language_boost` | string | — | Language emphasis |

### Rime

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `voice_speed` | float | 1.0 | Speech rate. Above 1.0 = faster, below 1.0 = slower. |
| `sampling_rate` | integer | 24000 | Output sample rate in Hz. |
| `response_format` | string | `"mp3"` | Output format: `mp3`, `pcm`, or `wav`. |

### Inworld

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `language_code` | string | — | Language code |
| `delivery_mode` | string | — | `STABLE`, `BALANCED`, or `CREATIVE`. Only supported by `inworld-tts-2`. |

### Fish Audio

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `format` | string | `"pcm"` | `mp3`, `wav`, `pcm`, `opus` |
| `sample_rate` | integer | `24000` | Valid values depend on format: pcm/wav — 8000, 16000, 24000, 32000, 44100; mp3 — 32000, 44100; opus — 48000 |

## Examples

### Basic Streaming

**Python:**

```python
import asyncio
import json
import base64
import websockets

async def tts_stream():
    url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    async with websockets.connect(url, additional_headers=headers) as ws:
        # 1. Handshake
        await ws.send(json.dumps({"text": " "}))

        # 2. Send text
        await ws.send(json.dumps({"text": "Hello from Telnyx text-to-speech."}))

        # 3. Signal end of input
        await ws.send(json.dumps({"text": ""}))

        # 4. Collect audio
        audio_chunks = []
        async for message in ws:
            data = json.loads(message)

            if data.get("error"):
                print(f"Error: {data['error']}")
                break

            if data.get("audio"):
                audio_chunks.append(base64.b64decode(data["audio"]))

            if data.get("isFinal"):
                break

    # Save audio
    with open("output.mp3", "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)

asyncio.run(tts_stream())
```

**JavaScript:**

```javascript
const WebSocket = require('ws');
const fs = require('fs');

const url = 'wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra';
const ws = new WebSocket(url, {
  headers: { 'Authorization': 'Bearer YOUR_API_KEY' }
});

const audioChunks = [];

ws.on('open', () => {
  // 1. Handshake
  ws.send(JSON.stringify({ text: ' ' }));

  // 2. Send text
  ws.send(JSON.stringify({ text: 'Hello from Telnyx text-to-speech.' }));

  // 3. Signal end of input
  ws.send(JSON.stringify({ text: '' }));
});

ws.on('message', (raw) => {
  const data = JSON.parse(raw);

  if (data.error) {
    console.error('Error:', data.error);
    ws.close();
    return;
  }

  if (data.audio) {
    audioChunks.push(Buffer.from(data.audio, 'base64'));
  }

  if (data.isFinal) {
    fs.writeFileSync('output.mp3', Buffer.concat(audioChunks));
    ws.close();
  }
});
```

### Conversational (Barge-In)

Send multiple text segments and interrupt mid-synthesis:

```python
import asyncio
import json
import base64
import websockets

async def conversational_tts():
    url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    async with websockets.connect(url, additional_headers=headers) as ws:
        # Handshake with voice settings
        await ws.send(json.dumps({
            "text": " ",
            "voice_settings": {"voice_speed": 1.1}
        }))

        # Send first sentence
        await ws.send(json.dumps({"text": "Welcome to the demo."}))

        # Wait for first audio, then interrupt
        async for message in ws:
            data = json.loads(message)
            if data.get("isFinal"):
                break

        # Interrupt and send new text
        await ws.send(json.dumps({"force": true}))
        await ws.send(json.dumps({"text": "Actually, let me start over."}))

        # Collect remaining audio...
        await ws.send(json.dumps({"text": ""}))

        async for message in ws:
            data = json.loads(message)
            if data.get("isFinal"):
                break

asyncio.run(conversational_tts())
```

### LLM Token Streaming

Stream tokens from an LLM directly to TTS. The server buffers text and synthesizes at sentence boundaries:

```python
import asyncio
import json
import websockets

async def llm_to_tts(llm_token_stream):
    url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    async with websockets.connect(url, additional_headers=headers) as ws:
        await ws.send(json.dumps({"text": " "}))

        # Stream LLM tokens directly — TTS handles sentence buffering
        for token in llm_token_stream:
            await ws.send(json.dumps({"text": token}))

        # Done — flush remaining
        await ws.send(json.dumps({"text": ""}))
```

Markdown in LLM output is automatically stripped before synthesis — headers, bold, italics, code blocks, and links are converted to plain text.
