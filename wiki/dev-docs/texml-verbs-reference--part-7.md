---
title: TeXML Verbs Reference
summary: A consolidated reference for the TeXML verbs available in Telnyx Programmable
  Voice, covering call control, media playback, recording, transcription, conferencing,
  payments, and SIPREC. Each verb section lists attributes, child nouns, examples,
  and the callbacks that the platform emits.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/recording
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/redirect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/refer
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/reject
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/say
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/start
updated_at: 2026-08-05T14:05:15Z
---

# TeXML Verbs Reference

*Part 7 of 7 — see also: [Part 1](texml-verbs-reference--part-1.md), [Part 2](texml-verbs-reference--part-2.md), [Part 3](texml-verbs-reference--part-3.md), [Part 4](texml-verbs-reference--part-4.md), [Part 5](texml-verbs-reference--part-5.md), [Part 6](texml-verbs-reference--part-6.md)*

A consolidated reference for the TeXML verbs available in Telnyx Programmable Voice, covering call control, media playback, recording, transcription, conferencing, payments, and SIPREC. Each verb section lists attributes, child nouns, examples, and the callbacks that the platform emits.

## Say

The `<Say>` verb speaks the text specified back to the caller, enabling text-to-speech for any application.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `voice` | Optional text-to-speech voice type. For basic text-to-speech use `man` or `woman` (en-US only). For premium text-to-speech use `alice` or one of the following provider-prefixed formats: `Polly.VoiceId` / `Polly.VoiceId-Neural` for Amazon Polly, `AWS.Polly.VoiceId` for direct AWS Polly notation, `Azure.VoiceId` for Azure TTS (supports `gender` and `effect` attributes), `ElevenLabs.ModelId.VoiceId` for ElevenLabs (requires `api_key_ref`), `Telnyx.ModelId.VoiceId` for Telnyx native TTS, `Resemble.ModelId.VoiceId` for Resemble AI, `Minimax.ModelId.VoiceId` for Minimax, `Rime.ModelId.VoiceId` for Rime, `Inworld.ModelId.VoiceId` for Inworld, and `FishAudio.ModelId.VoiceId` for Fish Audio (ModelId is one of `s2.1-pro`, `s2-pro`, or `s1`). | `man`, `woman`, `alice`, `Polly.VoiceId`, `Polly.VoiceId-Neural`, `AWS.Polly.VoiceId`, `Azure.VoiceId`, `ElevenLabs.ModelId.VoiceId`, `Telnyx.ModelId.VoiceId`, `Resemble.ModelId.VoiceId`, `Minimax.ModelId.VoiceId`, `Rime.ModelId.VoiceId`, `Inworld.ModelId.VoiceId`, `FishAudio.ModelId.VoiceId` | `man` |
| `language` | ISO language type to be used if voice type `alice` is selected. If `man` or `woman` is selected, the language accent will always be en-US. This parameter is ignored when a specific Amazon Polly voice is used. | — | — |
| `loop` | The number of times to repeat the text. `0` means infinite. | `0`–`10` | `1` |
| `gender` | Specifies the gender of the voice. Only applicable when using Azure voices (`Azure.*`). | `Male`, `Female` | — |
| `effect` | Applies an audio effect to the spoken text. Only applicable when using Azure voices (`Azure.*`). | `eq_telecomhp8k`, `eq_car` | — |
| `voiceSpeed` | Speech rate for the voice. Must be a decimal between `0.1` and `2.0`. | `0.1`–`2.0` | `1` |
| `api_key_ref` | Reference to the API key for authentication with the TTS provider. The key must be stored via the [integration secrets API](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret). Used with ElevenLabs and Azure voices. | — | — |
| `region` | Cloud region to use with the TTS provider. Required for Azure voices when using a custom API key. | — | — |
| `pronunciationDictId` | UUID of a pronunciation dictionary to apply to the spoken text. | — | — |
| `languageBoost` | Language hint for Telnyx Qwen3TTS voices. Accepted as full names (`Auto`, `English`, `German`, `Chinese`, `French`, `Italian`, `Japanese`, `Korean`, `Portuguese`, `Russian`, `Spanish`) or ISO 639-1 codes (`en`, `de`, `zh`, `fr`, `it`, `ja`, `ko`, `pt`, `ru`, `es`). | — | — |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="alice">This is a premium Amazon Polly text-to-speech message!</Say>
</Response>
```

## Siprec

The `<Siprec>` instruction starts the SIPREC session on the given call.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `connectorName` | Specifies which pre-configured external connector shall be used for this request. | — | — |
| `statusCallback` | A URL for Telnyx to send webhook requests to on each event related to the SIPREC session. | — | — |
| `statusCallbackMethod` | HTTP request type used for `statusCallback`. | `GET`, `POST` | `POST` |
| `track` | Specifies which track should be forwarded to the SRS. | `inbound_track`, `outbound_track`, `both_tracks` | `both_tracks` |
| `name` | Name of the SIPREC session. It can be used to stop the session. | — | — |
| `includeMetadataCustomHeaders` | Controls whether custom parameters are added as metadata; if `false`, they are added to SIP headers. | — | `false` |
| `secure` | Controls whether to encrypt media sent to your SRS using SRTP and TLS. When set, you need to configure the SRS port in your connector to `5061`. | — | `false` |
| `sessionTimeoutSecs` | Sets the `Session-Expires` header on the INVITE. A re-INVITE is sent every half the value set. Useful for session keep-alive. Minimum value is `90`; set to `0` to disable. | `90`–`14440` | `1800` |

### Examples

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Siprec name="siprec_session" track="both_tracks" connectorName="my-connector" statusCallback="https://example.com/siprec_callback" />
  </Start>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Stop>
    <Siprec name="siprec_session" />
  </Stop>
</Response>
```

### Expected callbacks

If `statusCallback` is set, SIPREC status callbacks are sent for the following events:

- `siprec-started` — SIPREC session has started
- `siprec-stopped` — SIPREC session has stopped
- `siprec-failed` — SIPREC session failed to start

See the [SIPREC Callback](https://developers.telnyx.com/api-reference/callbacks/texml-siprec) for the full payload reference.

## Start

The `<Start>` verb starts the service defined in the nested noun. As soon as the service is started, the next TeXML instructions will be executed from the provided instructions.

### Child verbs/nouns

- `Suppression` — start noise suppression. See the [Suppression documentation](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/suppression) for more information.
- `Transcription` — start transcription. See the [Transcription documentation](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription) for more information.
- `Stream` — start media stream over websocket. See the [Stream documentation](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream) for more information.
- `Recording` — start recording the call. See the [Recording](recording.md) documentation for more information.
