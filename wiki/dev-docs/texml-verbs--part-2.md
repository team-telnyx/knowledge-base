---
title: TeXML Verbs
summary: A reference guide to all TeXML verbs — XML instructions used to control call
  flows on the Telnyx platform — including their attributes, child nouns, callbacks,
  and usage examples.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record
  content_hash: b1e7de22e5dfc3603f792482827743d971ca13e7c10634433b37dee4d446de5f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/redirect
  content_hash: 929bc4cfd1bdf813c8cada583ce1851ef5c4b07b102ab972ebef84b614dd7fa7
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/refer
  content_hash: 1351d94cb364fcdbffcc10835ec065d6c1246472322c0ec153d48e684ad3461f
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/reject
  content_hash: a7979c780e2824073f61f514d32e080955b25cf70126c86df66307a58de6807e
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/say
  content_hash: 5dca362eeb4073803c9cc2ce9b054fb2c12e31682444c23a4cef297cd6fd9315
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec
  content_hash: 8db4546d370cdd8c57f8dfd03ab1e6b05a3c6e6cfc915bc1d2025510cf76c3b5
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/start
  content_hash: 44cc81e2b16e50a2d475b14b27d7a8f07c99ee65abf3287513e7aba10c8bd6c5
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stop
  content_hash: 416e3d6a516e6c045a3292da6c34566d52ff8e1b6cd88f549a500339f0d4f9a1
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/stream
  content_hash: 5566b817fbdaea8050ddd33ecea17a6d5e0995b1952459d58865da0a7af44bd3
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/suppression
  content_hash: da215b7151f18c98dadb14331511e103ef60273a0f2fe66e08a7c372a445187d
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/transcription
  content_hash: 50ef432defbb70a77cc272ae72ce39a66d03878b97e74f7c443b1ee5e10800a2
- url: https://developers.telnyx.com/docs/voice/programmable-voice/tts
  content_hash: 9bbf80ec6aaf63aa519699bfc34010940806a4146e8e413aa4f5b6c58f8e3c44
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
