---
title: TeXML Programmable Voice
summary: TeXML is Telnyx's XML-based markup language for controlling Programmable
  Voice calls, designed for drop-in compatibility with Twilio's TwiML. This page covers
  the TeXML quickstart, verb and noun compatibility with TwiML, REST API endpoint
  parity, and detailed reference for the core verbs including Dial, Conference, Enqueue,
  Connect, AIAssistant, AIGather, and ConversationRelay.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aigather
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/connect
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conversationrelay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/enqueue
updated_at: 2026-08-05T14:04:49Z
---

# TeXML Programmable Voice

*Part 3 of 6 — see also: [Part 1](texml-programmable-voice--part-1.md), [Part 2](texml-programmable-voice--part-2.md), [Part 4](texml-programmable-voice--part-4.md), [Part 5](texml-programmable-voice--part-5.md), [Part 6](texml-programmable-voice--part-6.md)*

TeXML is Telnyx's XML-based markup language for controlling Programmable Voice calls, designed for drop-in compatibility with Twilio's TwiML. This page covers the TeXML quickstart, verb and noun compatibility with TwiML, REST API endpoint parity, and detailed reference for the core verbs including Dial, Conference, Enqueue, Connect, AIAssistant, AIGather, and ConversationRelay.

## Dial

The `<Dial>` verb transfers an existing call to another destination. `<Dial>` ends the new call if the called party does not answer, the number does not exist, or Telnyx receives a busy signal.

### Attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `action` | Optional URL where TeXML makes a request when the `<Dial>` call ends to retrieve a new set of TeXML instructions. | — | — |
| `method` | HTTP method to use when requesting the action URL. | `GET`, `POST` | `POST` |
| `callerId` | Caller ID that must be a valid E.164 format number. | — | — |
| `fromDisplayName` | The fromDisplayName string used as the caller ID name (SIP From Display Name) presented to the destination. Max 128 characters; letters, numbers, spaces, and `-_~!.+` only. | — | — |
| `hangupOnStar` | Lets the initial caller hang up on the called party by pressing the `*` key. Does not apply for the Conference noun. | — | `false` |
| `timeout` | Number of seconds to wait for the called party to answer. | `5`–`120` | `30` |
| `timeLimit` | Maximum duration of the call in seconds. | `60`–`14400` | `14400` |
| `record` | Records both legs of a call within the associated `<Dial>` verb. Works with `<Number>` and `<Sip>` nouns only. | `do-not-record`, `record-from-answer`, `record-from-ringing`, `record-from-answer-dual`, `record-from-ringing-dual` | `do-not-record` |
| `recordingChannels` | Number of channels in the final recording. | `single`, `dual` | `single` |
| `recordMaxLength` | Maximum length for the recording in seconds (0 for infinite). | `0`–`14400` | `0` |
| `recordingStatusCallback` | Optional URL where Telnyx makes a GET or POST request when the recording is available. | — | — |
| `recordingStatusCallbackMethod` | HTTP request type for `recordingStatusCallback`. | `GET`, `POST` | `POST` |
| `recordingStatusCallbackEvent` | Recording events for which Telnyx sends a webhook. | `in-progress`, `completed`, `absent` | `completed` |
| `sendRecordingUrl` | Defines if the recording URL is sent in the callbacks. | — | `true` |
| `ringTone` | The ringback tone played back to the caller. | `at`, `au`, `bg`, `br`, `be`, `ch`, `cl`, `cn`, `cz`, `de`, `dk`, `ee`, `es`, `fi`, `fr`, `gr`, `hu`, `il`, `in`, `it`, `lt`, `jp`, `mx`, `my`, `nl`, `no`, `nz`, `ph`, `pl`, `pt`, `ru`, `se`, `sg`, `th`, `tw`, `ve`, `za`, `us`, `us-old`, `uk` | `us` |
| `audioUrl` | URL to an audio file played as a custom ringback tone. Overrides `ringTone` when set. | — | — |
| `answerOnBridge` | If true, the inbound call is not answered until the dialed call is answered, preserving the ringing state on the caller's side. | — | `false` |
| `sequential` | When true with multiple `<Number>` or `<Sip>` nouns, Telnyx dials each destination one at a time in the order listed. | — | `false` |
| `passDiversionHeader` | When true, the Diversion SIP header from the inbound call is passed through to the outbound dial attempt. | — | `false` |
| `machineDetectionSpeechThreshold` | Maximum duration of a greeting in milliseconds before classifying the call as a machine. Only used when `machineDetection` is enabled and `detectionMode` is Premium. | — | — |
| `machineDetectionSpeechEndThreshold` | Silence duration in milliseconds after a greeting to wait before classifying the call as a machine. Only used when `machineDetection` is enabled and `detectionMode` is Premium. | — | — |
| `machineDetectionSilenceTimeout` | Maximum duration of initial silence in milliseconds before classifying the call as silence. Only used when `machineDetection` is enabled and `detectionMode` is Premium. | — | — |

### Child verbs/nouns

- **`<Number>`** — Specifies a phone number to dial.
- **`<Sip>`** — Specifies a SIP endpoint to dial.
- **`<Queue>`** — Adds a call to a queue.

### Number attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `statusCallback` | URL for Telnyx to send webhook requests on each event in `statusCallbackEvent` for outbound calls only. | — | — |
| `statusCallbackEvent` | Call events for which Telnyx sends a webhook. | `initiated`, `ringing`, `answered`, `amd`, `dtmf`, `completed` | `completed` |
| `statusCallbackMethod` | HTTP request type for `statusCallback`. | `GET`, `POST` | `POST` |
| `url` | Optional URL to another TeXML document containing `<Gather>` and `<Hangup>` verbs so the called party can take an action before the two parties are connected. | — | — |
| `method` | HTTP request type for `url`. | `GET`, `POST` | `POST` |
| `sendDigits` | DTMF tones to play when the call is answered. Digits 0-9, `#`, `*`, and `w` (0.5 second pause). | — | — |
| `machineDetection` | Enables Answering Machine Detection. Add `amd` event type to `statusCallbackEvent` to receive the detection result webhook. | `Enable`, `DetectMessageEnd`, `Disable` | `Disable` |
| `detectionMode` | Sets the Answering Machine Detection mode. | `Regular`, `Premium`, `PremiumCallScreening` | `Regular` |
| `machineDetectionTimeout` | Maximum timeout threshold for overall detection, in milliseconds. | `500`–`60000` | `3500` |
| `machineDetectionPromptEndTimeout` | Silence duration threshold after a call screening prompt before ending prompt detection, in milliseconds. Only used when `machineDetection` is enabled and `detectionMode` is `PremiumCallScreening`. | `1000`–`120000` | — |
| `sipRegion` | Geographic region of the SIP infrastructure Telnyx uses when dialing the destination. | `US`, `Europe`, `Canada`, `Australia`, `Middle East` | `US` |

### Sip attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `username` | Username for SIP authentication. | — | — |
| `password` | Password for SIP authentication. | — | — |
| `statusCallback` | URL for Telnyx to send webhook requests on each event in `statusCallbackEvent` for outbound calls only. | — | — |
| `statusCallbackEvent` | Call events for which Telnyx sends a webhook. | `initiated`, `ringing`, `answered`, `amd`, `dtmf`, `completed` | `completed` |
| `statusCallbackMethod` | HTTP request type for `statusCallback`. | `GET`, `POST` | `POST` |
| `url` | Optional URL to another TeXML document containing `<Gather>` and `<Hangup>` verbs. | — | — |
| `method` | HTTP request type for `url`. | `GET`, `POST` | `POST` |
| `machineDetection` | Enables Answering Machine Detection. | `Enable`, `DetectMessageEnd`, `Disable` | `Disable` |
| `detectionMode` | Sets the Answering Machine Detection mode. | `Regular`, `Premium`, `PremiumCallScreening` | `Regular` |
| `machineDetectionTimeout` | Maximum timeout threshold for overall detection, in milliseconds. | `500`–`60000` | `3500` |
| `machineDetectionPromptEndTimeout` | Silence duration threshold after a call screening prompt before ending prompt detection, in milliseconds. | `1000`–`120000` | — |
| `sipRegion` | Geographic region of the SIP infrastructure Telnyx uses when dialing the destination. | `US`, `Europe`, `Canada`, `Australia`, `Middle East` | `US` |

### Queue attributes

| Attribute | Description | Options | Default |
| --- | --- | --- | --- |
| `url` | Optional URL to another TeXML document containing `<Play>`, `<Say>`, `<Gather>`, `<Pause>`, and `<Redirect>` verbs. Executed on the queued call before bridging. | — | — |
| `method` | HTTP request type for `url`. | `GET`, `POST` | `POST` |

### Simultaneous dialing

Multiple `<Number>` and `<Sip>` nouns within a `<Dial>` verb dial multiple destinations at the same time. The first person to answer is connected; the rest are hung up:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial>
    <Number>+18775551212</Number>
    <Sip>sip:connection@sip.telnyx.com</Sip>
    <Number>+18771234567</Number>
  </Dial>
</Response>
```

### Sequential dialing

Set `sequential="true"` to dial multiple `<Number>` and `<Sip>` nouns one at a time in the order listed. Telnyx attempts the next destination only if the current attempt completes without being answered:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Dial sequential="true">
    <Number>+18775551212</Number>
    <Sip>sip:connection@sip.telnyx.com</Sip>
    <Number>+18771234567</Number>
  </Dial>
</Response>
```

### Expected callbacks

If `action` is set, a callback is sent when the dialed call ends. The `error_code` and `error_message` fields are provided only in case of failed calls.

If `statusCallbackEvent` is set, the following webhooks are sent:

| Event | Callback Reference |
| --- | --- |
| `initiated` | [Call Initiated](https://developers.telnyx.com/api-reference/callbacks/texml-call-initiated) |
| `ringing` | [Call Ringing](https://developers.telnyx.com/api-reference/callbacks/texml-call-ringing) |
| `answered` | [Call Answered](https://developers.telnyx.com/api-reference/callbacks/texml-call-answered) |
| `completed` | [Call Completed](https://developers.telnyx.com/api-reference/callbacks/texml-call-completed) |

If `machineDetection` is enabled, an AMD callback is sent to `amdStatusCallback`. If `deepfakeDetection` is set to `Enable`, a deepfake detection callback is sent to `deepfakeDetectionCallbackUrl` (or to `statusCallback` if `"deepfake"` is included in `statusCallbackEvent`). The callback payload includes `DeepfakeResult` (`real`, `fake`, or `silence_timeout`), `DeepfakeScore` (0.0–1.0), and `DeepfakeConsistency` (0–100). On detection failure, a `DeepfakeError` field is sent instead.

If `recordingStatusCallbackEvent` is set, the following webhooks are sent:

| Event | Callback Reference |
| --- | --- |
| `in-progress` | [Recording In Progress](https://developers.telnyx.com/api-reference/callbacks/texml-recording-in-progress) |
| `completed` | [Recording Completed](https://developers.telnyx.com/api-reference/callbacks/texml-recording-completed) |
