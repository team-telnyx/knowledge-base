---
title: TeXML Verbs Reference
summary: A comprehensive reference for all TeXML verbs supported by Telnyx, including
  attributes, child elements, examples, and expected callbacks for building programmable
  voice applications.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant
  content_hash: af198eef7639e391f8c8f060405b7b04bad9b1c02f5eb3d0771068267a71caec
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather
  content_hash: afbc1d87d0606d433f6e5f456da75392521725ceebeec0a015e41479b6925ca6
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
  content_hash: f6246336ddcc26e377ef5a351ff895009cfab433929d181fa375ef09312ca49d
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect
  content_hash: dc8d6bbc5592d61ad053cc65f12f14d46cd45c42fce7c9c888e080bd775c0e37
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conversationrelay
  content_hash: d63d26ac52566cb49f4398eb06e0be92ce5093c2726eeec62887b4259770e650
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
  content_hash: 5fae52a988962b1da6c202ea94e3a1c3f03e5a91d33715480c226586ecd7f94a
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue
  content_hash: 802557ce95d90b7cad4499133baf861a0378c2c4d25f7948466065fd06917085
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather
  content_hash: 598265ec490514334437faa8896ebb239db96bb5c07e2423a8e0b275874c33c0
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index
  content_hash: 1a98d136a32499275e01c6a23d47697b2f6ed227eb045c7aff6e8e559cb92454
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest
  content_hash: aff57efbd08370a28153150b16a57ae8a59fc7be4fdcd7c5eb9f5f1e00ebcc0d
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave
  content_hash: e2785d6fb22979fb9d219336aa2266f819a04d494710e3a5c063312a0202179e
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause
  content_hash: 7d0c629edbe69236ddf3169e86442136d8063a9b534b148164cc3c4fa1e23e7c
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play
  content_hash: dfbb4e7ed40f0ebdbb5969ad0de1a97c96b87edbf0b3e886c3bd01d676b17130
updated_at: 2026-06-11T10:44:08Z
---

# TeXML Verbs Reference

*Part 5 of 5 — see also: [Part 1](texml-verbs-reference--part-1.md), [Part 2](texml-verbs-reference--part-2.md), [Part 3](texml-verbs-reference--part-3.md), [Part 4](texml-verbs-reference--part-4.md)*

A comprehensive reference for all TeXML verbs supported by Telnyx, including attributes, child elements, examples, and expected callbacks for building programmable voice applications.

## Play

The `<Play>` verb plays an MP3 or WAV audio file fetched from a URL. It can also play DTMF tones via the `digits` attribute, or fetch a file from Telnyx media storage when `mediaStorage="true"` is set (expects a `media_name` instead of a URL). `<Play>` can be used independently or nested within `<Gather>` to play audio while waiting for DTMF tones.

### Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `loop` | Times to repeat the audio. | — | `1` |
| `mediaStorage` | When `true`, fetches the file from Telnyx media storage using a media name instead of a URL. | `true`, `false` | `false` |
| `digits` | DTMF tones to play. Supports 0–9, `*`, `#`, and `w` (0.5s pause). When specified, plays DTMF tones instead of an audio file. | — | — |
| `failoverUrl` | Backup audio source when the primary URL fails. The `mediaStorage` flag also applies. Only one retry attempt is made. | — | — |
| `continueOnError` | When `true`, a playback failure does not abort the script. The error is logged and execution continues. | — | `false` |
| `ringTone` | Plays a country-specific ringback tone instead of an audio file. Cannot be combined with an audio body. Not supported inside `<Conference>`. | Country codes (e.g., `us`, `uk`, `de`, `jp`, etc.) | — |

### Examples

Play an audio file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play>https://example.com/welcome.mp3</Play>
</Response>
```

Play a ringback tone:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play ringTone="us" loop="3"/>
</Response>
```

Continue on error:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play continueOnError="true">https://example.com/might-404.mp3</Play>
    <Say>Sorry, we could not play the message.</Say>
</Response>
```

Failover URL:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play failoverUrl="https://cdn-backup.example.com/welcome.mp3">https://cdn.example.com/welcome.mp3</Play>
</Response>
```
