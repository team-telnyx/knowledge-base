---
title: TeXML Verbs
summary: A reference guide to all TeXML verbs — XML instructions used to control call
  flows on the Telnyx platform — including their attributes, child nouns, callbacks,
  and usage examples.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/redirect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/refer
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/reject
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/say
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/start
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stop
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/suppression
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription
- url: https://developers.telnyx.com/docs/voice/programmable-voice/tts
updated_at: 2026-06-11T10:44:32Z
---

# TeXML Verbs

*Part 2 of 3 — see also: [Part 1](texml-verbs--part-1.md), [Part 3](texml-verbs--part-3.md)*

A reference guide to all TeXML verbs — XML instructions used to control call flows on the Telnyx platform — including their attributes, child nouns, callbacks, and usage examples.

## Siprec

The `<Siprec>` instruction starts a SIPREC session on the call. It is used within `<Start>` or `<Stop>` verbs.

| Attribute | Description | Options | Default |
|---|---|---|---|
| `connectorName` | Pre-configured external connector to use. | | - |
| `statusCallback` | URL for webhook requests on SIPREC session events. | | - |
| `statusCallbackMethod` | HTTP request type for `statusCallback`. | `GET`, `POST` | `POST` |
| `track` | Which track to forward to the SRS. | `inbound_track`, `outbound_track`, `both_tracks` | `both_tracks` |
| `name` | Name of the SIPREC session (used to stop it later). | | - |
| `includeMetadataCustomHeaders` | Whether custom parameters are added as metadata (`true`) or SIP headers (`false`). | | `false` |
| `secure` | Whether to encrypt media using SRTP and TLS. When set, configure SRS port to 5061. | | `false` |
| `sessionTimeoutSecs` | Sets `Session-Expires` header on the INVITE. A re-INVITE is sent every half the value. Minimum 90; set `0` to disable. | `90`–`14440` | `1800` |

Example — starting a SIPREC session:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Siprec name="siprec_session" track="both_tracks" connectorName="my-connector" statusCallback="https://example.com/siprec_callback" />
  </Start>
</Response>
```

Example — stopping a SIPREC session:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Stop>
    <Siprec name="siprec_session" />
  </Stop>
</Response>
```

If `statusCallback` is set, callbacks are sent for `siprec-started`, `siprec-stopped`, and `siprec-failed` events.

## Start and Stop

### Start

The `<Start>` verb starts the service defined in the nested noun. As soon as the service is started, the next TeXML instructions are executed.

| Child Noun/Verb | Description |
|---|---|
| `Suppression` | Start noise suppression |
| `Transcription` | Start real-time transcription |
| `Stream` | Start media stream over WebSocket |

### Stop

The `<Stop>` verb stops the instruction specified by the nested noun on a call.

| Child Noun/Verb | Description |
|---|---|
| `Suppression` | Stops current suppression (no attributes needed) |
| `Transcription` | Stops current transcription (no attributes needed) |
| `Stream` | Stops current media stream (no attributes needed) |

Example — stopping a stream:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Stop>
    <Stream />
  </Stop>
</Response>
```

## Stream

The `<Stream>` instruction streams call media to a WebSocket address in near-real-time. Audio is delivered as base64-encoded RTP payloads (no headers), wrapped in JSON payloads. Use within `<Start>` or `<Stop>`.

| Attribute | Description | Options | Default |
|---|---|---|---|
| `url` | Destination WebSocket address. | | - |
| `track` | Which track to stream. | `inbound_track`, `outbound_track`, `both_tracks` | `inbound_track` |
| `name` | Custom name for the stream instance. | | - |
| `codec` | Codec for streamed audio. Transcoding only supported between PCMU and PCMA. | `PCMU`, `PCMA`, `G722`, `OPUS`, `AMR-WB`, `default` | `default` |
| `bidirectionalMode` | Bidirectional streaming mode. | `mp3`, `rtp` | `mp3` |
| `bidirectionalCodec` | Bidirectional streaming codec (only with `bidirectionalMode=rtp`). | `PCMU`, `PCMA`, `G722`, `OPUS`, `AMR-WB` | `PCMU` |
| `bidirectionalSamplingRate` | Bidirectional streaming sampling rate in Hz. | `8000`, `16000`, `24000` | `8000` |
| `statusCallback` | URL for stream status webhook events. | | - |
| `statusCallbackMethod` | HTTP request type for `statusCallback`. | `GET`, `POST` | `POST` |
| `enableReconnect` | Whether the platform automatically attempts to reconnect the WebSocket if disconnected. | | `true` |

### Parameter child noun

The `<Parameter>` noun passes custom key-value pairs to the WebSocket server. Parameters are included in the `start` message sent over the WebSocket connection.

| Attribute | Description | Options | Default |
|---|---|---|---|
| `name` | Name of the custom parameter. | | - |
| `value` | Value of the custom parameter. | | - |

Example — basic stream:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Stream url="wss://yourdomain.com/stream" track="both_tracks" />
  </Start>
</Response>
```

Example — stream with custom parameters:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Stream url="wss://yourdomain.com/stream" statusCallback="https://example.com/stream-events">
      <Parameter name="customer_id" value="12345" />
      <Parameter name="call_type" value="support" />
    </Stream>
  </Start>
</Response>
```

To disable automatic reconnection (which is enabled by default), set `enableReconnect="false"`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Stream url="wss://yourdomain.com/stream" enableReconnect="false" />
  </Start>
</Response>
```

If `statusCallback` is set, callbacks are sent for `stream-started`, `stream-stopped`, and `stream-failed` events.

## Suppression

The `<Suppression>` instruction starts noise suppression on the call to improve audio quality. Use within `<Start>` or `<Stop>`.

| Attribute | Description | Options | Default |
|---|---|---|---|
| `direction` | Which side of the audio to denoise. | `inbound`, `outbound`, `both` | `inbound` |

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Suppression direction="both" />
  </Start>
</Response>
```
