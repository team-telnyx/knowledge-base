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

*Part 6 of 7 — see also: [Part 1](texml-verbs-reference--part-1.md), [Part 2](texml-verbs-reference--part-2.md), [Part 3](texml-verbs-reference--part-3.md), [Part 4](texml-verbs-reference--part-4.md), [Part 5](texml-verbs-reference--part-5.md), [Part 7](texml-verbs-reference--part-7.md)*

A consolidated reference for the TeXML verbs available in Telnyx Programmable Voice, covering call control, media playback, recording, transcription, conferencing, payments, and SIPREC. Each verb section lists attributes, child nouns, examples, and the callbacks that the platform emits.

## Recording

The `<Recording>` instruction starts a non-blocking call recording when nested inside `<Start>`. After recording starts, Telnyx immediately continues executing the next TeXML instruction. The recording stops when the call ends or when it is stopped with the Stop Recording command.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `recordingStatusCallback` | Optional URL that tells Telnyx where to make its `GET` or `POST` request when recording status events occur. Relative URLs are resolved against the current TeXML document URL. | — | — |
| `recordingStatusCallbackMethod` | HTTP request type used for `recordingStatusCallback`. | `GET`, `POST` | `POST` |
| `recordingStatusCallbackEvent` | The recording events for which Telnyx should send a webhook to the `recordingStatusCallback` URL. Multiple events are separated by a space. | `in-progress`, `completed`, `absent` | `completed` |
| `channels` | Specifies whether the final audio file should be recorded as one channel or two channels. Use `mono` or `single` for a single-channel recording. | `mono`, `single`, `dual` | `dual` |
| `track` | Specifies which track should be recorded. | `inbound`, `outbound`, `both` | `both` |
| `trim` | Removes silence from the beginning and end of the recording when set to `trim-silence`. | `trim-silence` | — |
| `format` | The format of the recording file. | `mp3`, `wav` | `mp3` |

### Examples

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Recording />
  </Start>
  <Say>Recording has started.</Say>
</Response>
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Start>
    <Recording
      channels="dual"
      track="both"
      format="mp3"
      trim="trim-silence"
      recordingStatusCallback="https://example.com/recording-status"
      recordingStatusCallbackMethod="POST"
      recordingStatusCallbackEvent="in-progress completed absent" />
  </Start>
  <Say>This call may be recorded for quality assurance.</Say>
</Response>
```

### Expected callbacks

If `recordingStatusCallback` is set, recording status callbacks are sent for the events listed in `recordingStatusCallbackEvent`:

| Event | Callback Reference |
| --- | --- |
| `in-progress` | [Recording In Progress](https://developers.telnyx.com/api-reference/callbacks/texml-recording-in-progress) |
| `completed` | [Recording Completed](https://developers.telnyx.com/api-reference/callbacks/texml-recording-completed) |
| `absent` | Recording failed or was not created |

When `recordingStatusCallbackEvent` is not provided, Telnyx sends the `completed` callback by default.

## Redirect

The `<Redirect>` verb transfers control of a call to the TeXML document at another TeXML application. This is useful to create a tree structure of TeXML files for different applications. No nouns can be nested within `<Redirect>`.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `method` | The type of request used for the `<Redirect>` URL. | `GET`, `POST` | `POST` |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Redirect method="POST">https://example.com/next-instructions</Redirect>
</Response>
```

## Refer

The `<Refer>` verb in Telnyx allows you to transfer a phone call to another SIP infrastructure during a TeXML call. You can initiate it at any point during the call. When you use `<Refer>`, Telnyx will replace the original call with a new call to the external system you specify, effectively transferring the call to that system.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `action` | Optional URL where TeXML will make a request when the `<Refer>` verb ends, to retrieve a new set of TeXML instructions to continue the call flow. | — | — |
| `method` | HTTP request type used to retrieve the next set of instructions. | `GET`, `POST` | `POST` |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Refer>
        <Sip>sip:john@example.com</Sip>
    </Refer>
</Response>
```

### Expected callbacks

If `action` is set, a callback is sent when the `<Refer>` verb finishes. See the [Refer Status Callback](https://developers.telnyx.com/api-reference/callbacks/texml-refer-status) for the full payload reference.

## Reject

The `<Reject>` verb rejects a call to your Telnyx number. It is effectively an exit statement from the current document, as there is no way to return to any instructions listed after the `<Reject>` verb. If placed as the very first verb in an incoming call, `<Reject>` will prevent the call from being answered and will incur no cost. If placed elsewhere in the call, the call will hang up but will be charged up to that point.

You can't nest any verbs within `<Reject>` and you can't nest `<Reject>` in any other verbs.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `reason` | The tone to play to indicate the reason the call was rejected. | `rejected`, `busy` | `rejected` |

### Example

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Reject reason="busy"/>
</Response>
```
