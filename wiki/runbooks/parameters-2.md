---
title: Parameters
summary: Query parameters for the WebSocket STT endpoint.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/index
    content_hash: 54e06df722b3670507f5dc8729172bfbe9ea849b576b86c472f11a72366375c3
updated_at: 2026-04-10T00:00:00Z
---

# Parameters

Query parameters for the WebSocket STT endpoint.

All parameters are passed as query string values on the WebSocket URL. Locked at connection time — cannot be changed mid-session.

<ParamField type="string">
  `Deepgram`, `Telnyx`, `Google`, `Azure`

<ParamField type="string">
  See [Engines & Models](engines-models.md)

<ParamField type="string">
  See [Audio Formats](audio-formats-2.md)

<ParamField type="integer">
  Hz. Required for raw encodings (`linear16`, `mulaw`, `alaw`). Ignored for container formats. Invalid value returns [error 40005](errors.md).

<ParamField type="string">
  BCP-47 code. `multi` for auto-detect. See [Language](language.md) for details.

<ParamField type="string">
  `"true"` for partial transcripts. See [Interim Results](interim-results.md) for details.

<ParamField type="string">
  Deepgram silence detection in ms. `"false"` to disable. See [Endpointing](endpointing.md) for details.

<ParamField type="string">
  PII redaction. Deepgram only. See [Redaction](redaction.md) for details.

<ParamField type="string">
  Comma-separated boost terms. Deepgram Nova-3/Flux. See [Keyword Boosting](keyword-boosting.md) for details.

<ParamField type="string">
  Legacy keyword boosting with intensifiers. Deepgram Nova. See [Keyword Boosting](keyword-boosting.md) for details.

<ParamField type="string">
  Azure Speech Services region.

<ParamField type="float">
  Flux only. Confidence threshold for `EndOfTurn` events. See [End-of-Turn Detection](end-of-turn-detection.md) for details.

<ParamField type="integer">
  Flux only. Max silence before forcing `EndOfTurn`. See [End-of-Turn Detection](end-of-turn-detection.md) for details.

<ParamField type="float">
  Flux only. Speculative `EagerEndOfTurn` threshold. Disabled by default. See [End-of-Turn Detection](end-of-turn-detection.md) for details.

## Example

```
wss://api.telnyx.com/v2/speech-to-text/transcription?transcription_engine=Deepgram&model=nova-3&input_format=wav&language=en-US&interim_results=true
```


## Related Pages

- [Parameters](../runbooks/parameters.md)
