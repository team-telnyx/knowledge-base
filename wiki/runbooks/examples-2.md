---
title: Examples
summary: Complete code examples for WebSocket STT streaming.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/examples
    content_hash: d3ea75a684452a4ea933eec1468245b982d75ea9ba2282cc4f9b57b7f95ddf58
updated_at: 2026-04-10T00:00:00Z
---

# Examples

Complete code examples for WebSocket STT streaming.

Stream a WAV file and print transcripts.

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


## Related Pages

- [Examples](../runbooks/examples.md)
- [Examples](../runbooks/examples-3.md)
- [Examples](../runbooks/examples-4.md)
