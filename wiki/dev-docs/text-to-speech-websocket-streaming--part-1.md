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

*Part 1 of 2 — see also: [Part 2](text-to-speech-websocket-streaming--part-2.md)*

Real-time text-to-speech over a persistent WebSocket connection. Send text, receive audio. This page covers the connection lifecycle, message protocol, voice settings, and code examples for streaming synthesis with barge-in and LLM token support.

## Overview

Telnyx Text-to-Speech WebSocket streaming provides real-time synthesis over a persistent WebSocket connection. Text and audio flow concurrently — there is no request/response pairing. Text is buffered on the server and synthesized at sentence boundaries, with audio streamed back as it is produced.

The endpoint is:

```
wss://api.telnyx.com/v2/text-to-speech/speech
```

## Connection Lifecycle

### Handshake

There are two ways to establish a connection:

- **Direct WebSocket connection** — pass all configuration as query parameters in the `wss://` URL. Most WebSocket clients and libraries support this natively; no separate HTTP request is needed.
- **HTTP upgrade** — initiate the connection as an HTTP GET request that upgrades to a WebSocket via the standard `101 Switching Protocols` handshake. This is what happens under the hood when a WebSocket client connects, and may be relevant if you need fine-grained control over the upgrade (e.g., setting custom headers in environments where the WebSocket library doesn't expose them directly).

Regardless of how the connection is established, send an initialization frame before any text:

```json
{"text": " "}
```

The initialization frame may include `voice_settings` to configure provider-specific parameters:

```json
{
  "text": " ",
  "voice_settings": {
    "voice_speed": 1.2
  }
}
```

All configuration — query parameters and voice settings — is locked before synthesis begins. See [Voice Settings](voice-settings.md) for both surfaces and the full parameter reference.

### Streaming

Once initialized, text and audio flow concurrently. Text accumulates until the server detects a sentence boundary (period, question mark, exclamation). Short fragments without punctuation wait for more text. Send `"flush": true` to force synthesis of buffered partials.

**Text preprocessing:** Markdown formatting is automatically stripped before synthesis (headers, bold, italics, code blocks, links, lists, emoji). This is useful when synthesizing LLM output. Pronunciation dictionary replacements are applied if `pronunciation_dict_id` is set.

**Streamed vs. concatenated delivery:** Most providers (Telnyx Natural/NaturalHD/Qwen3TTS, Rime, Minimax, Resemble, Inworld) stream audio in separate frames where `text` is `null`. AWS Polly and Azure return audio in the text-bearing chunk instead. See [Messages](messages.md) for details.

A typical exchange looks like:

```
Client → Server  {"text":" "}                          (handshake)
Client → Server  {"text":"Hello, welcome."}
Client → Server  {"text":" How are you?"}
                                          (sentence boundary detected)
Client ← Server  {"audio":"<b64>","isFinal":false}     (streamed chunks)
Client ← Server  {"audio":"<b64>","isFinal":false}
Client ← Server  {"audio":null,"isFinal":true}         (synthesis complete)
Client → Server  {"text":""}                            (end of sequence)
Client ← Server  remaining audio + final frame
                                          connection closes
```

### Teardown

Send `{"text": ""}` (empty string) to flush remaining buffered text and close gracefully. The server finishes synthesis, sends any remaining audio and a final frame, then closes the WebSocket.

```
Client → Server  {"text":""}
Client ← Server  final audio chunks
Client ← Server  {"audio":null,"text":"","isFinal":true}
Client ← Server  [connection closed]
```

Dropping the connection without the empty-text frame works but may lose buffered text. The connection also closes on server error or inactivity timeout.

## Messages

### Client → Server

All client messages are JSON text frames.

| Field | Type | Description |
| --- | --- | --- |
| `text` | string (required) | Text to synthesize. `" "` (single space) for handshake. `""` (empty string) for end-of-sequence. |
| `voice_settings` | object | Provider-specific voice configuration. Only used in the handshake frame (`{"text": " "}`). See [Voice Settings](voice-settings.md). |
| `flush` | boolean | When `true`, immediately synthesizes all buffered text without waiting for a sentence boundary. Default: `false`. |
| `force` | boolean | When `true`, stops the current synthesis worker and starts a new one. The original handshake is replayed automatically. Use for barge-in/interruption. |

**Message sequence:**

1. **Handshake** (required first message):

   ```json
   {"text": " "}
   ```

   With optional voice settings:

   ```json
   {
     "text": " ",
     "voice_settings": {
       "voice_speed": 1.2
     }
   }
   ```

2. **Text** (one or more):

   ```json
   {"text": "Hello, welcome to Telnyx."}
   ```

3. **Flush** (optional — force synthesis of buffered partial sentences):

   ```json
   {"text": "incomplete fragment", "flush": true}
   ```

4. **Interrupt** (optional — restart synthesis):

   ```json
   {"force": true}
   ```

5. **End of sequence**:

   ```json
   {"text": ""}
   ```

### Server → Client

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

| Field | Type | Description |
| --- | --- | --- |
| `audio` | string \| null | Base64-encoded audio data. `null` when the provider uses streamed delivery — audio arrives in separate streamed chunk frames instead. |
| `text` | string \| null | The text segment this audio corresponds to. `null` for streamed audio chunks. |
| `isFinal` | boolean | `false` for audio chunks. |
| `cached` | boolean | `true` if audio was served from cache. |
| `timeToFirstAudioFrameMs` | integer | Time in milliseconds from speech request to first audio frame. Only present on the first chunk of each synthesis. |

**Streamed audio chunk** — for providers that stream audio incrementally (Telnyx Natural, NaturalHD, Qwen3TTS, Rime, Minimax, Resemble, Inworld), audio arrives in separate frames:

```json
{
  "audio": "<base64-encoded-audio>",
  "text": null,
  "isFinal": false,
  "cached": false
}
```

These contain raw audio data (`text` is always `null`). The concatenated audio chunk for these providers has `audio: null` — only the streamed chunks carry audio bytes.

For AWS Polly and Azure, audio is returned in the `audio` field of the regular audio chunk frame. For all other providers, ignore the `audio` field on the text-bearing chunk and collect audio from the streamed frames.

**Final frame** — signals that synthesis is complete for the current text input:

```json
{
  "audio": null,
  "text": "",
  "isFinal": true
}
```

The connection remains open after a final frame — send more text or close.

**Error frame:**

```json
{
  "error": "Provider error message"
}
```

The connection closes shortly after an error frame.
