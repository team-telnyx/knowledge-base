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

*Part 4 of 7 — see also: [Part 1](texml-verbs-reference--part-1.md), [Part 2](texml-verbs-reference--part-2.md), [Part 3](texml-verbs-reference--part-3.md), [Part 5](texml-verbs-reference--part-5.md), [Part 6](texml-verbs-reference--part-6.md), [Part 7](texml-verbs-reference--part-7.md)*

A consolidated reference for the TeXML verbs available in Telnyx Programmable Voice, covering call control, media playback, recording, transcription, conferencing, payments, and SIPREC. Each verb section lists attributes, child nouns, examples, and the callbacks that the platform emits.

## Play

The `<Play>` verb plays an MP3 or WAV audio file, which Telnyx fetches back to the caller from the URL you configure. Alternatively, specify `mediaStorage="true"` to fetch a file you previously uploaded to Telnyx using media storage APIs. When `mediaStorage="true"` is used the verb expects a `media_name` instead of a URL. You can also use the `digits` attribute to play DTMF tones instead of an audio file. The `ringTone` attribute generates a country-specific ringback tone instead of fetching an audio file; it cannot be combined with an audio body and is not supported inside `<Conference>`. By default, a playback failure (e.g. the audio URL returns 404) aborts the TeXML script. Set `continueOnError="true"` to log the failure and proceed with the next verb instead. Set `failoverUrl` to retry once with a backup audio source before the failure path is taken; `continueOnError` still applies if the failover also fails. `<Play>` can be used independently as a verb or nested within `<Gather]]` as a noun to play an audio file while waiting for DTMF tones.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `loop` | Times to repeat the audio. When used with `ringTone`, forwarded to FreeSWITCH as the `tone_stream` `loops` parameter; `loop="0"` plays the tone indefinitely until interrupted by a subsequent verb or hangup. | — | `1` |
| `mediaStorage` | When true, fetches the file from Telnyx media storage using the provided media name. | `true`, `false` | `false` |
| `digits` | DTMF tones to play. The value can include digits `0`–`9`, `*`, `#`, and `w` (for a 0.5 second pause). When specified, the verb plays DTMF tones instead of an audio file. | — | — |
| `failoverUrl` | Backup audio source played when the primary URL fails. The `mediaStorage` flag also applies to this URL. Only one retry attempt is made. | — | — |
| `continueOnError` | When true, a playback failure does not abort the script. Telnyx still logs the error and continues with the next verb. | `true`, `false` | `false` |
| `ringTone` | Plays a country-specific ringback tone instead of an audio file. Cannot be combined with an audio body. Not supported inside `<Conference>`. | `at`, `au`, `bg`, `br`, `be`, `ch`, `cl`, `cn`, `cz`, `de`, `dk`, `ee`, `es`, `fi`, `fr`, `gr`, `hu`, `il`, `in`, `it`, `lt`, `jp`, `mx`, `my`, `nl`, `no`, `nz`, `ph`, `pl`, `pt`, `ru`, `se`, `sg`, `th`, `tw`, `ve`, `za`, `us`, `us-old`, `uk` | — |

### Examples

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play>https://example.com/welcome.mp3</Play>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play ringTone="us" loop="3"/>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play continueOnError="true">https://example.com/might-404.mp3</Play>
    <Say>Sorry, we could not play the message.</Say>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Play failoverUrl="https://cdn-backup.example.com/welcome.mp3">https://cdn.example.com/welcome.mp3</Play>
</Response>
```
