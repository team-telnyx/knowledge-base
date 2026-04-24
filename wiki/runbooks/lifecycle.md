---
title: Lifecycle
summary: WebSocket endpoint for real-time speech-to-text streaming.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/index
    content_hash: d53b0f71af858dfa616b8fa728af72c2664e8beefbd184096ece521c3e2053cf
updated_at: 2026-04-10T00:00:00Z
---

# Lifecycle

WebSocket endpoint for real-time speech-to-text streaming.

Real-time speech-to-text over a persistent WebSocket connection. Send audio, receive transcripts.

## Endpoint

```
wss://api.telnyx.com/v2/speech-to-text/transcription
```

## Connection Lifecycle

### 1. Handshake

The connection starts as an HTTP GET with `Upgrade: websocket`. The server responds with `101 Switching Protocols`, then the connection upgrades to WebSocket frames.

```
GET /v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&input_format=wav HTTP/1.1
Host: api.telnyx.com
Upgrade: websocket
Connection: Upgrade
Authorization: Bearer YOUR_API_KEY
Sec-WebSocket-Version: 13
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
```

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

You can also connect directly to the WebSocket endpoint without an HTTP upgrade:

```
wss://transcription.telnyx.com/public/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&input_format=wav
```

The same query parameters apply. Once connected, the message protocol is identical.

All configuration is set at connect time via query parameters — engine, model, format, language, options. Cannot be changed mid-session. See [Parameters](parameters-2.md) for the full list.

Invalid parameters return a JSON error and the connection closes.

### 2. Streaming

Once connected, audio and transcription flow concurrently — no request/response pairing.

**Client → Server**

| Frame type | Content                                                                                                   |
| ---------- | --------------------------------------------------------------------------------------------------------- |
| binary     | Audio data — raw bytes, chunked. No base64 or JSON wrapping.                                              |
| text       | `{"type": "Finalize"}` — flush buffer, force final transcript (Deepgram only)                             |
| text       | `{"type": "CloseStream"}` — flush remaining transcription and close the stream gracefully (Deepgram only) |
| text       | `{"type": "KeepAlive"}` — reset idle timeout (Deepgram only)                                              |

**Server → Client**

| Message              | Description                                                              |
| -------------------- | ------------------------------------------------------------------------ |
| Transcription result | `{"transcript": "...", "is_final": true, "confidence": 0.98}`            |
| Utterance end        | `{"transcript": "", "is_final": true, "utterance_end": true}` (Deepgram) |
| Error                | `{"errors": [...]}` — connection closes after                            |

See [Messages](messages.md) for the complete wire protocol reference.

```
Client → Server  binary: audio chunk
Client → Server  binary: audio chunk
Client ← Server  {"transcript":"Hello","is_final":false}
Client → Server  binary: audio chunk
Client ← Server  {"transcript":"Hello, how are you?","is_final":true}
```

### 3. Teardown

Send `{"type": "CloseStream"}` (Deepgram only) to flush remaining audio and close gracefully. The server finishes processing, sends any remaining transcripts, then closes the WebSocket.

```
Client → Server  {"type":"CloseStream"}
Client ← Server  final transcript
Client ← Server  [connection closed]
```

For other engines, close the WebSocket connection directly. Dropping the connection without `CloseStream` works but may lose buffered audio on Deepgram.

See [Examples](examples-2.md) for complete code samples.


## Related Pages

- [Lifecycle](../runbooks/lifecycle-2.md)
- [SIM Lifecycle](../runbooks/sim-lifecycle.md)
