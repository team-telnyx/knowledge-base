---
title: Messages
summary: WebSocket frame types — client-to-server and server-to-client.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/messages
    content_hash: 9d85c0568fab13c1ace2b0f59c908367fb29f92c21aab88b38ea363d9cb41538
updated_at: 2026-04-10T00:00:00Z
---

# Messages

WebSocket frame types — client-to-server and server-to-client.

## Client → Server

All client messages are JSON text frames.

### Text Frame

<ParamField type="string">
  Text to synthesize. `" "` (single space) for handshake. `""` (empty string) for end-of-sequence.

<ParamField type="object">
  Provider-specific voice configuration. Only used in the handshake frame (`{"text": " "}`). See [Voice Settings](https://developers.telnyx.com/docs/voice/tts/websocket-streaming/parameters/voice-settings).

<ParamField type="boolean">
  When `true`, immediately synthesizes all buffered text without waiting for a sentence boundary. Default: `false`.

<ParamField type="boolean">
  When `true`, stops the current synthesis worker and starts a new one. The original handshake is replayed automatically. Use for barge-in/interruption.

### Message Sequence

**1. Handshake** (required first message):

```json theme={null}
{"text": " "}
```

With optional voice settings:

```json theme={null}
{
  "text": " ",
  "voice_settings": {
    "voice_speed": 1.2
  }
}
```

**2. Text** (one or more):

```json theme={null}
{"text": "Hello, welcome to Telnyx."}
```

**3. Flush** (optional — force synthesis of buffered partial sentences):

```json theme={null}
{"text": "incomplete fragment", "flush": true}
```

**4. Interrupt** (optional — restart synthesis):

```json theme={null}
{"force": true}
```

**5. End of sequence**:

```json theme={null}
{"text": ""}
```

***

## Server → Client

All server messages are JSON text frames.

### Audio Chunk

Returned when synthesis produces audio for a complete sentence.

```json theme={null}
{
  "audio": "<base64-encoded-audio>",
  "text": "Hello, welcome to Telnyx.",
  "isFinal": false,
  "cached": false,
  "timeToFirstAudioFrameMs": 245
}
```

<ParamField type="string | null">
  Base64-encoded audio data. `null` when the provider uses streamed delivery — audio arrives in separate streamed chunk frames instead. See note below.

<ParamField type="string | null">
  The text segment this audio corresponds to. `null` for streamed audio chunks.

<ParamField type="boolean">
  `false` for audio chunks.

<ParamField type="boolean">
  `true` if audio was served from cache.

<ParamField type="integer">
  Time in milliseconds from speech request to first audio frame. Only present on the first chunk of each synthesis.

### Streamed Audio Chunk

For providers that stream audio incrementally (Telnyx Natural, NaturalHD, Qwen3TTS, Rime, Minimax, Resemble, Inworld), audio arrives in separate frames:

```json theme={null}
{
  "audio": "<base64-encoded-audio>",
  "text": null,
  "isFinal": false,
  "cached": false
}
```

These contain raw audio data (`text` is always `null`). The concatenated audio chunk for these providers has `audio: null` — only the streamed chunks carry audio bytes.

  For AWS Polly and Azure, audio is returned in the `audio` field of the regular audio chunk frame. For all other providers, ignore the `audio` field on the text-bearing chunk and collect audio from the streamed frames.

### Final Frame

Signals that synthesis is complete for the current text input:

```json theme={null}
{
  "audio": null,
  "text": "",
  "isFinal": true
}
```

The connection remains open after a final frame — send more text or close.

### Error Frame

```json theme={null}
{
  "error": "Provider error message"
}
```

The connection closes shortly after an error frame.


## Related Pages

- [Messages](../runbooks/messages.md)
- [Send RCS Messages](../runbooks/send-rcs-messages.md)
