---
title: TeXML Verbs Reference
summary: A comprehensive reference for all TeXML verbs supported by Telnyx, including
  attributes, child elements, examples, and expected callbacks for building programmable
  voice applications.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conversationrelay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/gather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/httprequest
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/leave
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play
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
