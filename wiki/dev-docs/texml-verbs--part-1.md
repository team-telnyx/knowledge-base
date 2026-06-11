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

*Part 1 of 3 — see also: [Part 2](texml-verbs--part-2.md), [Part 3](texml-verbs--part-3.md)*

A reference guide to all TeXML verbs — XML instructions used to control call flows on the Telnyx platform — including their attributes, child nouns, callbacks, and usage examples.

## Record

The `<Record>` verb creates an audio file with the call audio. If a `recordingStatusCallback` is provided, Telnyx delivers the recording URL to that address once the call has ended. Recording URLs are valid for 10 minutes after the call ends. All recordings are also available via the [Telnyx Mission Control Portal](https://portal.telnyx.com/).

The `<Record>` verb also supports automatic transcription by setting `transcription="true"` and providing a `transcriptionCallback` URL. The transcription result is sent via webhook.

| Attribute | Description | Options | Default |
|---|---|---|---|
| `action` | Optional URL where TeXML will make a request when `<Record>` ends, to retrieve a new set of TeXML instructions. | | - |
| `method` | HTTP request type used to retrieve the next set of instructions. | `GET`, `POST` | `POST` |
| `finishOnKey` | Set of digits, any one of which will end the recording. | Any digit, `#`, `*` | `1234567890*#` |
| `timeout` | Seconds to wait before stopping the recording if silence is detected (timer starts when speech is detected). Uses transcription for silence detection, so a related charge applies. Set `0` for infinite. | | `0` |
| `maxLength` | Maximum recording length in seconds. `0` for infinite. | `0`–`14400` | `3600` |
| `playBeep` | Whether a sound is played before recording starts. | | `true` |
| `trim` | Removes silence from beginning and end of recording when set to `trim-silence`. | `trim-silence` | - |
| `channels` | Dual-channel produces stereo audio: first leg on channel A, the rest on channel B. | `single`, `dual` | `dual` |
| `recordingStatusCallback` | URL where Telnyx sends its request when the recording is available. | | - |
| `recordingStatusCallbackMethod` | HTTP request type for `recordingStatusCallback`. | `GET`, `POST` | `POST` |
| `transcription` | Enables automatic transcription of the recorded audio. | `true`, `false` | `false` |
| `transcriptionCallback` | URL where Telnyx sends the transcription result. | | - |
| `transcriptionEngine` | Engine to use for transcription. | `A`, `B` | `A` |
| `transcriptionLanguage` | Language for transcription when enabled. | | `en-US` |
| `format` | Format of the recording file. | `mp3`, `wav` | `mp3` |
| `recordingStatusCallbackEvent` | Recording events for which Telnyx should send a webhook. Multiple events separated by a space. | `in-progress`, `completed` | `completed` |

Example — simple recording:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Record action="https://example.com/recording-complete"
            maxLength="30"
            playBeep="true"/>
</Response>
```

Example — recording with transcription:

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

If `action` or `recordingStatusCallback` is set, callbacks are sent for `in-progress` and `completed` events. If transcription is enabled, a transcription callback is sent to `transcriptionCallback`.

## Redirect

The `<Redirect>` verb transfers control of a call to a TeXML document hosted at another URL. This is useful for creating a tree structure of TeXML files across different applications. No nouns can be nested within `<Redirect>`.

| Attribute | Description | Options | Default |
|---|---|---|---|
| `method` | HTTP request type for the `<Redirect>` URL. | `GET`, `POST` | `POST` |

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Redirect method="POST">https://example.com/next-instructions</Redirect>
</Response>
```

## Refer

The `<Refer>` verb transfers a phone call to another SIP infrastructure during a TeXML call. When invoked, Telnyx replaces the original call with a new call to the specified external system.

| Attribute | Description | Options | Default |
|---|---|---|---|
| `action` | Optional URL where TeXML will make a request when `<Refer>` ends, to retrieve a new set of TeXML instructions. | | - |
| `method` | HTTP request type used to retrieve the next set of instructions. | `GET`, `POST` | `POST` |

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Refer>
        <Sip>sip:john@example.com</Sip>
    </Refer>
</Response>
```

If `action` is set, a callback is sent when `<Refer>` finishes.

## Reject

The `<Reject>` verb rejects a call to your Telnyx number. It acts as an exit statement — there is no way to return to instructions listed after `<Reject>`. If placed as the very first verb on an incoming call, it prevents the call from being answered and incurs no cost. If placed elsewhere, the call hangs up but is charged up to that point. No verbs can be nested within `<Reject>` and `<Reject>` cannot be nested in any other verb.

| Attribute | Description | Options | Default |
|---|---|---|---|
| `reason` | The tone to play indicating why the call was rejected. | `rejected`, `busy` | `rejected` |

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Reject reason="busy"/>
</Response>
```

## Say

The `<Say>` verb speaks the specified text back to the caller using text-to-speech. See the [Text-to-Speech Providers](text-to-speech-providers.md) section below for details on available TTS engines and voice formats.

| Attribute | Description | Options | Default |
|---|---|---|---|
| `voice` | TTS voice type. Basic: `man`, `woman` (en-US only). Premium: `alice`, `Polly.VoiceId`, `Polly.VoiceId-Neural`, `AWS.Polly.VoiceId`, `Azure.VoiceId`, `ElevenLabs.ModelId.VoiceId`, `Telnyx.ModelId.VoiceId`, `Resemble.ModelId.VoiceId`, `Minimax.ModelId.VoiceId`, `Rime.ModelId.VoiceId`, `Inworld.ModelId.VoiceId`. | | `man` |
| `language` | ISO language type for `alice` voice. Ignored when a specific Amazon Polly voice is used. | | - |
| `loop` | Number of times to repeat the text. `0` means infinite. | `0`–`10` | `1` |
| `gender` | Voice gender (Azure only). | `Male`, `Female` | - |
| `effect` | Audio effect applied to spoken text (Azure only). | `eq_telecomhp8k`, `eq_car` | - |
| `voiceSpeed` | Speech rate. | `0.1`–`2.0` | `1` |
| `api_key_ref` | Reference to an API key stored via the [integration secrets API](https://developers.telnyx.com/api-reference/integration-secrets/create-a-secret). Used with ElevenLabs and Azure voices. | | - |
| `region` | Cloud region for the TTS provider. Required for Azure voices when using a custom API key. | | - |
| `pronunciationDictId` | UUID of a pronunciation dictionary to apply. | | - |
| `languageBoost` | Language hint for Telnyx Qwen3TTS voices. Full names (`Auto`, `English`, `German`, `Chinese`, `French`, `Italian`, `Japanese`, `Korean`, `Portuguese`, `Russian`, `Spanish`) or ISO 639-1 codes (`en`, `de`, `zh`, `fr`, `it`, `ja`, `ko`, `pt`, `ru`, `es`). | | - |

Example:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="alice">This is a premium Amazon Polly text-to-speech message!</Say>
</Response>
```
