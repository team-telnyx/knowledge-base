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

*Part 3 of 5 — see also: [Part 1](texml-verbs-reference--part-1.md), [Part 2](texml-verbs-reference--part-2.md), [Part 4](texml-verbs-reference--part-4.md), [Part 5](texml-verbs-reference--part-5.md)*

A comprehensive reference for all TeXML verbs supported by Telnyx, including attributes, child elements, examples, and expected callbacks for building programmable voice applications.

## Dial

The `<Dial>` verb transfers an existing call to another destination. The call ends if the called party does not answer, the number does not exist, or Telnyx receives a busy signal.

### Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `action` | URL for next TeXML instructions when the `<Dial>` call ends. | — | — |
| `method` | HTTP method for `action`. | `GET`, `POST` | `POST` |
| `callerId` | Caller ID in E.164 format. | — | — |
| `fromDisplayName` | Caller ID name (SIP From Display Name). Max 128 chars; letters, numbers, spaces, and `- _ ~ ! . +`. If omitted, defaults to the `callerId` number. | — | — |
| `hangupOnStar` | Let the initial caller hang up on the called party by pressing `*`. Does not apply to Conference noun. | — | `false` |
| `timeout` | Seconds to wait for the called party to answer. | `5`–`120` | `30` |
| `timeLimit` | Maximum call duration in seconds. | `60`–`14400` | `14400` |
| `record` | Record both legs of the call. Works with `<Number>` and `<Sip>` nouns only. Use the `record` attribute on `<Conference>` for conference recording. | `do-not-record`, `record-from-answer`, `record-from-ringing`, `record-from-answer-dual`, `record-from-ringing-dual` | `do-not-record` |
| `recordingChannels` | Number of channels in the final recording. | `single`, `dual` | `single` |
| `recordMaxLength` | Maximum recording length in seconds (0 = infinite). | `0`–`14400` | `0` |
| `recordingStatusCallback` | URL for recording availability webhooks. | — | — |
| `recordingStatusCallbackMethod` | HTTP method for `recordingStatusCallback`. | `GET`, `POST` | `POST` |
| `recordingStatusCallbackEvent` | Recording events for webhooks, space-separated. | `in-progress`, `completed`, `absent` | `completed` |
| `sendRecordingUrl` | Whether the recording URL is sent in callbacks. | — | `true` |
| `ringTone` | Country-specific ringback tone. | Country codes (e.g., `us`, `uk`, `de`, `jp`, etc.) | `us` |
| `audioUrl` | URL to an audio file played as a custom ringback tone. Overrides `ringTone` when set. | — | — |
| `answerOnBridge` | Preserve ringing state on the caller's side until the dialed call is answered. Only takes effect when the inbound call has not yet been answered. | — | `false` |
| `sequential` | When `true` with multiple `<Number>`/`<Sip>` nouns, dial each destination one at a time in order. If `false` (default), all destinations are dialed simultaneously and the first answered call is connected. | — | `false` |
| `passDiversionHeader` | Pass the Diversion SIP header from the inbound call to the outbound dial attempt. | — | `false` |
| `machineDetectionSpeechThreshold` | Max greeting duration in ms; longer greetings are classified as machines. Only with Premium detection mode. | — | — |
| `machineDetectionSpeechEndThreshold` | Silence duration in ms after a greeting before classifying as a machine. Only with Premium detection mode. | — | — |
| `machineDetectionSilenceTimeout` | Max initial silence duration in ms before classifying as silence. Only with Premium detection mode. | — | — |

### Child Nouns

| Noun | Description |
|---|---|
| `Number` | Specifies a phone number to dial. |
| `Sip` | Specifies a SIP endpoint to dial. |
| `Queue` | Adds the call to a queue. |

### Number Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `statusCallback` | URL for outbound call event webhooks. | — | — |
| `statusCallbackEvent` | Call events for webhooks, space-separated. | `initiated`, `ringing`, `answered`, `amd`, `dtmf`, `completed` | `completed` |
| `statusCallbackMethod` | HTTP method for `statusCallback`. | `GET`, `POST` | `POST` |
| `url` | URL to a TeXML document executed for the called party before connection (can contain `<Gather>` and `<Hangup>`). The callee hears ringback while the document executes. | — | — |
| `method` | HTTP method for `url`. | `GET`, `POST` | `POST` |
| `sendDigits` | DTMF tones to play when the call is answered. Supports 0–9, `*`, `#`, and `w` (0.5s pause). | — | — |
| `machineDetection` | Enable Answering Machine Detection. Add `amd` to `statusCallbackEvent` to receive the detection result. | `Enable`, `DetectMessageEnd`, `Disable` | `Disable` |
| `detectionMode` | AMD mode. Use `PremiumCallScreening` for premium iOS call screening detection. | `Regular`, `Premium`, `PremiumCallScreening` | `Regular` |
| `machineDetectionTimeout` | Overall detection timeout in ms. | `500`–`60000` | `3500` |
| `machineDetectionPromptEndTimeout` | Silence duration threshold after a call screening prompt, in ms. Only for `PremiumCallScreening`. | `1000`–`120000` | — |

### Sip Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `username` | SIP authentication username. | — | — |
| `password` | SIP authentication password. | — | — |
| `statusCallback` | URL for outbound call event webhooks. | — | — |
| `statusCallbackEvent` | Call events for webhooks, space-separated. | `initiated`, `ringing`, `answered`, `amd`, `dtmf`, `completed` | `completed` |
| `statusCallbackMethod` | HTTP method for `statusCallback`. | `GET`, `POST` | `POST` |
| `url` | URL to a TeXML document for the called party before connection. | — | — |
| `method` | HTTP method for `url`. | `GET`, `POST` | `POST` |
| `machineDetection` | Enable Answering Machine Detection. | `Enable`, `DetectMessageEnd`, `Disable` | `Disable` |
| `detectionMode` | AMD mode. | `Regular`, `Premium`, `PremiumCallScreening` | `Regular` |
| `machineDetectionTimeout` | Overall detection timeout in ms. | `500`–`60000` | `3500` |
| `machineDetectionPromptEndTimeout` | Silence threshold after call screening prompt, in ms. Only for `PremiumCallScreening`. | `1000`–`120000` | — |

### Queue Attributes

| Attribute | Description | Options | Default |
|---|---|---|---|
| `url` | URL to a TeXML document executed on the queued call before bridging. Supports `<Play>`, `<Say>`, `<Gather>`, `<Pause>`, and `<Redirect>`. | — | — |
| `method` | HTTP method for `url`. | `GET`, `POST` | `POST` |

### Simultaneous and Sequential Dialing

Multiple `<Number>` and `<Sip>` nouns can be dialed simultaneously (default) or sequentially.

Simultaneous — all destinations dialed at once, first to answer is connected:

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

Sequential — each destination tried in order, next only if current is not answered:

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

### Examples

Basic dial:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial action="/nextinstructions.php" callerId="+13120001234">+19999999999</Dial>
</Response>
```

Dial with status callback:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial action="/nextinstructions.php" callerId="+13120001234">
      <Number statusCallback="https://foo.com/my_call_stats" statusCallbackEvent="initiated ringing answered completed">+19999999999</Number>
    </Dial>
</Response>
```

Dial with AMD enabled:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Dial action="/nextinstructions.php" callerId="+13120001234">
      <Number statusCallback="https://foo.com/my_call_stats" statusCallbackEvent="initiated ringing answered completed amd" machineDetection="Enable" detectionMode="Regular">+19999999999</Number>
    </Dial>
</Response>
```

### Expected Callbacks

If `action` is set, a callback is sent when the dialed call ends. See [Dial Action Callback](https://developers.telnyx.com/api-reference/callbacks/texml-call-completed) for the full payload. The `error_code` and `error_message` fields are provided only for failed calls.

If `statusCallbackEvent` is set:

| Event | Callback Reference |
|---|---|
| `initiated` | [Call Initiated](https://developers.telnyx.com/api-reference/callbacks/texml-call-initiated) |
| `ringing` | [Call Ringing](https://developers.telnyx.com/api-reference/callbacks/texml-call-ringing) |
| `answered` | [Call Answered](https://developers.telnyx.com/api-reference/callbacks/texml-call-answered) |
| `completed` | [Call Completed](https://developers.telnyx.com/api-reference/callbacks/texml-call-completed) |

If `machineDetection` is enabled, an AMD callback is sent. See [AMD Callback](https://developers.telnyx.com/api-reference/callbacks/texml-call-amd).

If `deepfakeDetection` is set to `Enable`, a deepfake detection callback is sent to `deepfakeDetectionCallbackUrl` (or to `statusCallback` if `deepfake` is in `statusCallbackEvent`). The callback payload includes `DeepfakeResult` (`real`, `fake`, or `silence_timeout`), `DeepfakeScore` (0.0–1.0), and `DeepfakeConsistency` (0–100). On failure, `DeepfakeError` is sent instead.

If `recordingStatusCallbackEvent` is set:

| Event | Callback Reference |
|---|---|
| `in-progress` | [Recording In Progress](https://developers.telnyx.com/api-reference/callbacks/texml-recording-in-progress) |
| `completed` | [Recording Completed](https://developers.telnyx.com/api-reference/callbacks/texml-recording-completed) |
