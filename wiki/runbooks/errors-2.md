---
title: Errors
summary: WebSocket error codes and troubleshooting.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/websocket-streaming/errors
    content_hash: 07d435b36abd866ccddd91c1fb3a80e3840fc036bca58670981dbe0d421de038
updated_at: 2026-04-10T00:00:00Z
---

# Errors

WebSocket error codes and troubleshooting.

## HTTP Errors (Handshake)

These occur during the WebSocket upgrade request, before the connection is established.

| Code | Cause                                                                                                              |
| ---- | ------------------------------------------------------------------------------------------------------------------ |
| 400  | Invalid parameters — unsupported provider, missing required fields, or invalid voice format                        |
| 401  | Missing or invalid API key                                                                                         |
| 403  | Ultra model restricted on public WebSocket endpoint. Use [REST API](rest-api.md) for Ultra.           |
| 403  | Cloned voice restricted — organization requires identity verification for cloned voices (Qwen3TTS, Minimax clones) |

## WebSocket Errors (Runtime)

After the connection is established, errors arrive as JSON frames:

```json theme={null}
{
  "error": "Error in audio response"
}
```

The connection closes shortly after an error frame.

### Error Messages

| Error                                 | Cause                                                                   |
| ------------------------------------- | ----------------------------------------------------------------------- |
| `"Error in audio response"`           | The TTS provider returned an error during synthesis                     |
| `"Error in remaining audio response"` | Provider error while synthesizing buffered text during connection close |

## Troubleshooting

| Symptom                        | Cause                          | Fix                                                                                                          |
| ------------------------------ | ------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| Connection rejected (400)      | Invalid voice format           | Use `Provider.Model.VoiceId` format (e.g., `Telnyx.NaturalHD.astra`)                                         |
| Connection rejected (401)      | Missing auth                   | Pass `Authorization: Bearer <key>` header during WebSocket upgrade                                           |
| No audio after connecting      | Missing handshake              | Send `{"text": " "}` as first frame                                                                          |
| `audio` field is `null`        | Expected behavior              | For streamed providers (Telnyx, Rime, Minimax, Resemble, Inworld), audio arrives in separate streamed frames |
| Text sent but no response      | Sentence buffering             | Text is buffered until a sentence boundary. Send more text, use `flush: true`, or end with punctuation       |
| Ultra not working on WebSocket | Intentional restriction        | Ultra is REST-only. Use `POST /v2/text-to-speech/speech`                                                     |
| Cloned voice rejected          | Identity verification required | Complete L2 verification in the [Telnyx Portal](https://portal.telnyx.com)                                   |


## Related Pages

- [Errors](../runbooks/errors.md)
