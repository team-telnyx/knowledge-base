---
title: Examples
summary: Python and JavaScript WebSocket TTS examples.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/examples
    content_hash: a7653e4896c36a7dd72b4dd174f45f012a31d178a904e8de5dabca7972d1157c
updated_at: 2026-04-10T00:00:00Z
---

# Examples

Python and JavaScript WebSocket TTS examples.

## Basic Streaming

  ```python
  import asyncio
  import json
  import base64
  import websockets

  async def tts_stream():
      url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
      headers = {"Authorization": "Bearer YOUR_API_KEY"}

      async with websockets.connect(url, extra_headers=headers) as ws:
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

## Conversational (Barge-In)

Send multiple text segments and interrupt mid-synthesis:

```python theme={null}
import asyncio
import json
import base64
import websockets

async def conversational_tts():
    url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    async with websockets.connect(url, extra_headers=headers) as ws:
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

## LLM Token Streaming

Stream tokens from an LLM directly to TTS. The server buffers text and synthesizes at sentence boundaries:

```python theme={null}
import asyncio
import json
import websockets

async def llm_to_tts(llm_token_stream):
    url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    async with websockets.connect(url, extra_headers=headers) as ws:
        await ws.send(json.dumps({"text": " "}))

        # Stream LLM tokens directly — TTS handles sentence buffering
        for token in llm_token_stream:
            await ws.send(json.dumps({"text": token}))

        # Done — flush remaining
        await ws.send(json.dumps({"text": ""}))
```

  Markdown in LLM output is automatically stripped before synthesis — headers, bold, italics, code blocks, and links are converted to plain text.


## Related Pages

- [Examples](../runbooks/examples.md)
- [Examples](../runbooks/examples-2.md)
- [Examples](../runbooks/examples-3.md)
