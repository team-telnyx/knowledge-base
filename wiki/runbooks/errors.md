---
title: Errors
summary: Error codes and troubleshooting for WebSocket STT.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/errors
    content_hash: d1fb0c73b2a97b177c4252ecc1f1c370e3a489c58626a162988202ba9974a0cc
updated_at: 2026-04-10T00:00:00Z
---

# Errors

Error codes and troubleshooting for WebSocket STT.

If you send an invalid parameter (unsupported engine, format, or format/engine combination), the server responds with a JSON error and closes the connection.

## Error Response Format

```json theme={null}
{
  "errors": [{
    "code": "40001",
    "title": "Invalid Parameter",
    "detail": "Unsupported input_format 'aac'. Supported formats: mp3, wav, webm, ogg, flac, ogg_opus, webm_opus, linear16, linear32, mulaw, alaw, opus, amr_nb, amr_wb, g729, speex",
    "source": { "parameter": "input_format" }
  }]
}
```

## Error Codes

| Code    | Meaning                                                                       |
| ------- | ----------------------------------------------------------------------------- |
| `40001` | Invalid `input_format` value                                                  |
| `40002` | Format not supported by the chosen engine                                     |
| `40003` | `sample_rate` required but missing (raw encoding or Google with non-WAV/FLAC) |
| `40004` | `sample_rate` is not a valid positive integer                                 |
| `40005` | Invalid sample rate for the codec (e.g., `amr_nb` only supports 8000)         |
| `40006` | Format not supported by Flux model                                            |
| `40007` | Invalid `transcription_engine` value                                          |


## Related Pages

- [Errors](../runbooks/errors-2.md)
