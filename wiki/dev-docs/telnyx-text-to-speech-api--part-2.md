---
title: Telnyx Text-to-Speech API
summary: Telnyx Text-to-Speech provides REST and WebSocket interfaces for synthesizing
  audio from text, supporting real-time streaming playback, multiple TTS providers,
  OpenAI SDK compatibility, and conversational barge-in patterns.
sources:
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/api-reference
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/examples
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/index
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/pricing
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/request
- url: https://developers.telnyx.com/docs/voice/tts/rest-api/response
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/configuration
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/errors
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/examples
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/index
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/messages
- url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/parameters/voice-settings
- url: https://developers.telnyx.com/docs/voice/uac-connections/index
updated_at: 2026-06-11T10:48:38Z
---

# Telnyx Text-to-Speech API

*Part 2 of 3 — see also: [Part 1](telnyx-text-to-speech-api--part-1.md), [Part 3](telnyx-text-to-speech-api--part-3.md)*

Telnyx Text-to-Speech provides REST and WebSocket interfaces for synthesizing audio from text, supporting real-time streaming playback, multiple TTS providers, OpenAI SDK compatibility, and conversational barge-in patterns.

## WebSocket Streaming

Real-time text-to-speech over a persistent WebSocket connection. Send text, receive audio — no request/response pairing, no polling, no callbacks. Text and audio flow concurrently.

### Endpoint

```
wss://api.telnyx.com/v2/text-to-speech/speech
```

Connect directly by passing configuration as query parameters, or use a standard HTTP upgrade (`101 Switching Protocols`). Pass the API key via the `Authorization: Bearer <key>` header during the WebSocket upgrade.

### Connection Lifecycle

**1. Handshake** — Send an initialization frame as the first message: `{"text": " "}` (a single space). This frame may include `voice_settings` for provider-specific tuning. All configuration is locked before synthesis begins and cannot be changed mid-session.

**2. Streaming** — Send text frames; the server buffers text and synthesizes at sentence boundaries. Audio chunks arrive as they are produced. When done, send `{"text": ""}` to flush remaining buffer and close.

**3. Teardown** — Send `{"text": ""}` (empty string) to flush remaining buffered text and close gracefully. The server finishes synthesis, sends remaining audio and a final frame, then closes the WebSocket. Dropping the connection without the empty-text frame works but may lose buffered text.

### Configuration

Configuration is set in two places, both immutable once synthesis starts:

| Surface | When | What |
|---|---|---|
| Query parameters | WebSocket URL | Voice, audio format, sample rate, connection options |
| `voice_settings` | Init frame | Provider-specific tuning (speed, pitch, etc.) |

#### Query Parameters

| Parameter | Type | Default | Description |
|---|---|---|---|
| `voice` | string | — | Voice identifier in `Provider.Model.VoiceId` format. |
| `language` | string | — | BCP-47 language code. Only used by providers that accept it (AWS Polly, Azure, ElevenLabs, Inworld). |
| `text_type` | string | `text` | `text` or `ssml`. Only AWS Polly and Azure use this. |
| `audio_format` | string | `mp3` | Output format: `mp3`, `linear16`, `wav`, `mulaw`, `alaw`, `ogg_vorbis`. Not all formats supported by every provider. |
| `sample_rate` | integer | provider default | Output sample rate in Hz. Accepted values vary by provider. |
| `disable_cache` | boolean | `false` | Bypass the audio cache. |

Example URL:

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra&audio_format=linear16&disable_cache=true
```

#### Voice Settings (Init Frame)

Provider-specific tuning is passed once in `voice_settings` on the handshake frame. There are no common fields — every field is provider-specific and unrecognized fields are silently ignored.

```
{
  "text": " ",
  "voice_settings": {
    "voice_speed": 1.2
  }
}
```

See the Voice Settings reference below for per-provider fields.

### Messages

#### Client → Server

All client messages are JSON text frames.

| Frame | Content | Purpose |
|---|---|---|
| Handshake | `{"text": " "}` | Required first message. May include `voice_settings`. |
| Text | `{"text": "Hello."}` | Text to synthesize. |
| Flush | `{"text": "...", "flush": true}` | Force immediate synthesis of buffered text without waiting for a sentence boundary. |
| Interrupt | `{"force": true}` | Stop current synthesis (barge-in), restart the worker. The original handshake is replayed automatically. |
| End | `{"text": ""}` | Flush remaining buffer and close. |

#### Server → Client

All server messages are JSON text frames.

**Audio chunk** — returned when synthesis produces audio for a complete sentence:

```json
{
  "audio": "<base64-encoded-audio>",
  "text": "Hello, welcome to Telnyx.",
  "isFinal": false,
  "cached": false,
  "timeToFirstAudioFrameMs": 245
}
```

- `audio`: Base64-encoded audio data, or `null` for streamed providers (see below).
- `text`: The text segment this audio corresponds to, or `null` for streamed audio chunks.
- `isFinal`: `false` for audio chunks.
- `cached`: `true` if audio was served from cache.
- `timeToFirstAudioFrameMs`: Milliseconds from speech request to first audio frame. Only present on the first chunk of each synthesis.

**Streamed audio chunk** — For providers that stream audio incrementally (Telnyx Natural, NaturalHD, Qwen3TTS, Rime, Minimax, Resemble, Inworld), audio arrives in separate frames where `text` is `null`. The concatenated audio chunk for these providers has `audio: null` — only the streamed chunks carry audio bytes. For AWS Polly and Azure, audio is returned in the `audio` field of the regular audio chunk frame.

**Final frame** — Signals synthesis is complete for the current input:

```json
{"audio": null, "text": "", "isFinal": true}
```

The connection remains open after a final frame — send more text or close.

**Error frame** — `{"error": "Provider error message"}`. The connection closes shortly after.

### Errors and Troubleshooting

**HTTP errors (handshake):**

| Code | Cause |
|---|---|
| 400 | Invalid parameters — unsupported provider, missing required fields, or invalid voice format |
| 401 | Missing or invalid API key |
| 403 | Ultra model restricted on WebSocket (REST only), or cloned voice restricted (organization requires identity verification) |

**WebSocket errors (runtime):**

| Error | Cause |
|---|---|
| `"Error in audio response"` | The TTS provider returned an error during synthesis |
| `"Error in remaining audio response"` | Provider error while synthesizing buffered text during connection close |

**Troubleshooting:**

| Symptom | Cause | Fix |
|---|---|---|
| Connection rejected (400) | Invalid voice format | Use `Provider.Model.VoiceId` format |
| Connection rejected (401) | Missing auth | Pass `Authorization: Bearer <key>` header |
| No audio after connecting | Missing handshake | Send `{"text": " "}` as first frame |
| `audio` field is `null` | Expected behavior | For streamed providers, audio arrives in separate streamed frames |
| Text sent but no response | Sentence buffering | Send more text, use `flush: true`, or end with punctuation |
| Ultra not working on WebSocket | Intentional restriction | Ultra is REST-only |
| Cloned voice rejected | Identity verification required | Complete L2 verification in the Telnyx Portal |

### WebSocket Examples

**Basic streaming:**

```python
import asyncio, json, base64, websockets

async def tts_stream():
    url = "wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra"
    headers = {"Authorization": "Bearer YOUR_API_KEY"}

    async with websockets.connect(url, extra_headers=headers) as ws:
        await ws.send(json.dumps({"text": " "}))
        await ws.send(json.dumps({"text": "Hello from Telnyx text-to-speech."}))
        await ws.send(json.dumps({"text": ""}))

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

    with open("output.mp3", "wb") as f:
        for chunk in audio_chunks:
            f.write(chunk)

asyncio.run(tts_stream())
```

**Conversational with barge-in:** Send multiple text segments and interrupt mid-synthesis using `{"force": true}`.

**LLM token streaming:** Stream tokens from an LLM directly to TTS. The server buffers text and synthesizes at sentence boundaries. Markdown in LLM output is automatically stripped.

---
