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

*Part 5 of 7 — see also: [Part 1](texml-verbs-reference--part-1.md), [Part 2](texml-verbs-reference--part-2.md), [Part 3](texml-verbs-reference--part-3.md), [Part 4](texml-verbs-reference--part-4.md), [Part 6](texml-verbs-reference--part-6.md), [Part 7](texml-verbs-reference--part-7.md)*

A consolidated reference for the TeXML verbs available in Telnyx Programmable Voice, covering call control, media playback, recording, transcription, conferencing, payments, and SIPREC. Each verb section lists attributes, child nouns, examples, and the callbacks that the platform emits.

## Record

The `<Record>` verb creates an audio file with the call audio. If a `recordingStatusCallback` is set, Telnyx will deliver the URL for the recording to that address once the call has ended. Recording URLs are valid for 10 minutes after the call has ended. All recordings are also available via the [Telnyx Mission Control Portal](https://portal.telnyx.com/).

In addition to recording, `<Record>` supports automatic transcription by setting `transcription="true"` and providing a `transcriptionCallback` URL. The transcription result will be sent via webhook.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `action` | Optional URL where TeXML will make a request when `<Record>` ends to retrieve a new set of TeXML instructions to continue the call flow, sent with additional request parameters. | — | — |
| `method` | HTTP request type used to retrieve the next set of instructions. | `GET`, `POST` | `POST` |
| `finishOnKey` | Set of digits specified together, any one of which will end the recording. Supported characters: any digit, `#`, `*`. | — | `1234567890*#` |
| `timeout` | The number of seconds that Telnyx will wait for the recording to be stopped if silence is detected. The timer only starts when speech is detected. Transcription is used to detect silence and the related charge will be applied. `0` for infinite. | — | `0` |
| `maxLength` | Defines the maximum length for the recording in seconds. `0` for infinite. | `0`–`14400` | `3600` |
| `playBeep` | Whether or not a sound is played before the start of a recording. | — | `true` |
| `trim` | Will remove silence from the beginning and end of the recording when set to `trim-silence`. | `trim-silence` | — |
| `channels` | When using dual channels, the final audio file will be stereo recorded with the first leg on channel A, and the rest on channel B. | `single`, `dual` | `dual` |
| `recordingStatusCallback` | Optional URL that tells Telnyx where to make its `GET` or `POST` request when the recording is available. | — | — |
| `recordingStatusCallbackMethod` | HTTP request type used for `recordingStatusCallback`. | `GET`, `POST` | `POST` |
| `transcription` | Enables automatic transcription of the recorded audio. When set to `true`, a transcription will be generated and delivered to the `transcriptionCallback` URL. | `true`, `false` | `false` |
| `transcriptionCallback` | The URL where Telnyx will send the transcription result once available. | — | — |
| `transcriptionEngine` | Specifies the engine to use for transcription. `A` uses Google (default) and `B` uses Telnyx. Set to `Deepgram` to transcribe the recording with Deepgram, optionally pairing it with `transcriptionModel` to choose a specific Deepgram model. | `A`, `B`, `Deepgram`, `deepgram` | `A` |
| `transcriptionModel` | Optional model to use with the specified `transcriptionEngine`. Format is `vendor/model-name` — e.g. `deepgram/nova-2` or `deepgram/nova-3`. The vendor must match `transcriptionEngine`. If not specified, the engine's default model will be used. On Deepgram, defaults to `deepgram/nova-3`. See transcription models in [transcription_engine_config](https://developers.telnyx.com/api-reference/call-commands/transcription-start). | — | — |
| `transcriptionLanguage` | Language to use for transcription when transcription is enabled. Use a BCP-47 language tag such as `en-US`. The set of supported languages depends on the `transcriptionEngine` and `transcriptionModel` — see languages in [transcription_engine_config](https://developers.telnyx.com/api-reference/call-commands/transcription-start). | — | `en-US` |
| `format` | The format of the recording file. | `mp3`, `wav` | `mp3` |
| `recordingStatusCallbackEvent` | The recording events for which Telnyx should send a webhook to the `recordingStatusCallback` URL. Multiple events are separated by a space. | `in-progress`, `completed` | `completed` |

### Examples

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Record action="https://example.com/recording-complete" 
            maxLength="30" 
            playBeep="true"/>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="Telnyx.KokoroTTS.af">This call will be recorded and transcribed for quality purposes.</Say>
  <Record 
    action="https://example.com/recording-complete" 
    method="POST"
    maxLength="60"
    timeout="5"
    transcription="true"
    transcriptionEngine="A"
    transcriptionCallback="https://example.com/transcription-result" />
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="Telnyx.KokoroTTS.af">This call will be recorded and transcribed for quality purposes.</Say>
  <Record 
    action="https://example.com/recording-complete" 
    method="POST"
    maxLength="60"
    transcription="true"
    transcriptionEngine="Deepgram"
    transcriptionModel="deepgram/nova-3"
    transcriptionLanguage="en-US"
    transcriptionCallback="https://example.com/transcription-result" />
</Response>
```

### Expected callbacks

If `action` or `statusCallback` is set, recording status callbacks are sent:

| Event | Callback Reference |
| --- | --- |
| `in-progress` | [Recording In Progress](https://developers.telnyx.com/api-reference/callbacks/texml-recording-in-progress) |
| `completed` | [Recording Completed](https://developers.telnyx.com/api-reference/callbacks/texml-recording-completed) |

If `transcribe` is enabled, a transcription callback is sent to `transcribeCallback`. See the [Transcription Callback](https://developers.telnyx.com/api-reference/callbacks/texml-transcription) for the full payload reference.
