---
title: Lifecycle
summary: WebSocket endpoint for real-time text-to-speech streaming.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/index
    content_hash: d96ad959111ae0a251acb7712fbbcfac35d810f8897bec22ce9bd189077ebcc4
updated_at: 2026-04-10T00:00:00Z
---

# Lifecycle

WebSocket endpoint for real-time text-to-speech streaming.

Real-time text-to-speech over a persistent WebSocket connection. Send text, receive audio.

## Endpoint

```
wss://api.telnyx.com/v2/text-to-speech/speech
```

## Connection Lifecycle

### 1. Handshake

There are two ways to establish a connection:

#### Direct WebSocket connection

You can connect directly to the WebSocket endpoint by passing all configuration as query parameters in the `wss://` URL:

```
wss://api.telnyx.com/v2/text-to-speech/speech?voice=Telnyx.NaturalHD.astra
```

Most WebSocket clients and libraries support this natively — simply open a WebSocket connection to the URL and begin the message flow. No separate HTTP request is needed.

#### HTTP upgrade

Alternatively, initiate the connection as an HTTP GET request that upgrades to a WebSocket via the standard `101 Switching Protocols` handshake. This is what happens under the hood when a WebSocket client connects, and may be relevant if you need fine-grained control over the upgrade (e.g., setting custom headers in environments where the WebSocket library doesn't expose them directly).

#### Initialization frame

Regardless of how the connection is established, send an initialization frame before any text:

```json theme={null}
{"text": " "}
```

The initialization frame may include `voice_settings` to configure provider-specific parameters:

```json theme={null}
{
  "text": " ",
  "voice_settings": {
    "voice_speed": 1.2
  }
}
```

All configuration — query parameters and voice settings — is locked before synthesis begins. See [Configuration](configuration-3.md) for both surfaces and the full parameter reference.

### 2. Streaming

Once initialized, text and audio flow concurrently — no request/response pairing. Text is buffered and synthesized at sentence boundaries.

**Client → Server**

| Frame type | Content                                                                       |
| ---------- | ----------------------------------------------------------------------------- |
| text       | `{"text": "Hello."}` — text to synthesize                                     |
| text       | `{"text": "...", "flush": true}` — force immediate synthesis of buffered text |
| text       | `{"force": true}` — interrupt current synthesis (barge-in), restart worker    |
| text       | `{"text": ""}` — end of sequence, flush remaining buffer and close            |

**Server → Client**

| Message        | Description                                                      |
| -------------- | ---------------------------------------------------------------- |
| Audio chunk    | `{"audio":"<b64>","text":"Hello.","isFinal":false}`              |
| Streamed chunk | `{"audio":"<b64>","text":null,"isFinal":false}` (most providers) |
| Final frame    | `{"audio":null,"text":"","isFinal":true}` — synthesis complete   |
| Error          | `{"error":"..."}` — connection closes after                      |

See [Messages](messages-2.md) for the complete wire protocol reference.

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

**Text buffering:** Text accumulates until the server detects a sentence boundary (period, question mark, exclamation). Short fragments without punctuation wait for more text. Send `"flush": true` to force synthesis of buffered partials.

**Text preprocessing:** Markdown formatting is automatically stripped before synthesis (headers, bold, italics, code blocks, links, lists, emoji). Useful when synthesizing LLM output. Pronunciation dictionary replacements are applied if `pronunciation_dict_id` is set.

**Streamed vs. concatenated delivery:** Most providers (Telnyx Natural/NaturalHD/Qwen3TTS, Rime, Minimax, Resemble, Inworld) stream audio in separate frames where `text` is `null`. AWS Polly and Azure return audio in the text-bearing chunk instead. See [Messages](messages-2.md) for details.

### 3. Teardown

Send `{"text": ""}` (empty string) to flush remaining buffered text and close gracefully. The server finishes synthesis, sends any remaining audio and a final frame, then closes the WebSocket.

```
Client → Server  {"text":""}
Client ← Server  final audio chunks
Client ← Server  {"audio":null,"text":"","isFinal":true}
Client ← Server  [connection closed]
```

Dropping the connection without the empty-text frame works but may lose buffered text.

The connection also closes on server error or inactivity timeout.

See [Examples](examples-4.md) for complete code samples.


## Related Pages

- [Lifecycle](../runbooks/lifecycle.md)
- [SIM Lifecycle](../runbooks/sim-lifecycle.md)
