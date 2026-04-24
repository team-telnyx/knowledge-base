---
title: Messages
summary: All message types sent and received over the WebSocket connection.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/responses
    content_hash: 093bbf713c78a5977fff033c77d6e5dcadb075a1c17c4f6d0a69eb6f7bde6a1c
updated_at: 2026-04-10T00:00:00Z
---

# Messages

All message types sent and received over the WebSocket connection.

The WebSocket carries two frame types: binary frames (audio) from client to server, and JSON text frames in both directions.

## Client → Server

### Audio Data

Binary WebSocket frames containing raw audio bytes. No base64, no JSON wrapping.

Recommended chunk size: 2048–8192 bytes. Smaller chunks reduce latency; larger chunks reduce round trips.

```
[binary frame: audio bytes]
```

### Control Messages

JSON text frames with a `type` field.

  ```json
  {"type": "Finalize"}
  ```

  ```json
  {"type": "CloseStream"}
  ```

  ```json
  {"type": "KeepAlive"}
  ```

| Type          | Effect                                       | Engine support |
| ------------- | -------------------------------------------- | -------------- |
| `Finalize`    | Flush audio buffer, force a final transcript | Deepgram only  |
| `CloseStream` | End session, close connection gracefully     | All            |
| `KeepAlive`   | Reset idle timeout                           | Deepgram only  |

Unknown text frames are silently ignored.

***

## Server → Client

All server messages are JSON text frames.

### Transcription Result

Emitted for each recognized speech segment (partial or final).

```json theme={null}
{
  "transcript": "Hello, how are you today?",
  "is_final": true,
  "speech_final": true,
  "confidence": 0.98
}
```

| Field           | Type    | Present        | Description                                                 |
| --------------- | ------- | -------------- | ----------------------------------------------------------- |
| `transcript`    | string  | Always         | Transcribed text                                            |
| `is_final`      | boolean | Always         | `true` = finalized segment. `false` = interim (may revise). |
| `speech_final`  | boolean | Deepgram       | `true` = speaker stopped talking                            |
| `confidence`    | float   | When available | 0.0–1.0 confidence score                                    |
| `utterance_end` | boolean | Deepgram       | `true` = silence-triggered utterance boundary               |

### Utterance End

Emitted on speaker pause (Deepgram). Empty transcript, `is_final: true`.

```json theme={null}
{
  "transcript": "",
  "is_final": true,
  "utterance_end": true
}
```

### Error

Emitted on validation or connection errors. Connection closes shortly after.

```json theme={null}
{
  "errors": [
    {
      "code": "40002",
      "title": "Unsupported format",
      "detail": "Format 'flac' is not supported by engine 'Azure'",
      "source": {"parameter": "input_format"}
    }
  ]
}
```

| Field                       | Type   | Description                                                           |
| --------------------------- | ------ | --------------------------------------------------------------------- |
| `errors`                    | array  | One or more error objects                                             |
| `errors[].code`             | string | Error code (see [Errors](errors.md)) |
| `errors[].title`            | string | Short description                                                     |
| `errors[].detail`           | string | Human-readable explanation                                            |
| `errors[].source.parameter` | string | Query parameter that caused the error                                 |

***

## Message Flow

**`interim_results=false`** (default) — server sends only final transcripts:

```
Client:  [binary audio frames]
Server:  {"transcript": "Hello, how are you today?", "is_final": true, "speech_final": true, "confidence": 0.98}
Client:  [binary audio frames]
Server:  {"transcript": "I'm doing well.", "is_final": true, "speech_final": true, "confidence": 0.95}
Client:  {"type": "CloseStream"}
         [connection closed]
```

**`interim_results=true`** — server sends partials, then final:

```
Client:  [binary audio frames]
Server:  {"transcript": "Hello", "is_final": false, "speech_final": false}
Server:  {"transcript": "Hello, how are", "is_final": false, "speech_final": false}
Server:  {"transcript": "Hello, how are you today?", "is_final": true, "speech_final": true, "confidence": 0.98}
```

Partials are best-effort and may revise. Only `is_final: true` results are stable.


## Related Pages

- [Messages](../runbooks/messages-2.md)
- [Send RCS Messages](../runbooks/send-rcs-messages.md)
