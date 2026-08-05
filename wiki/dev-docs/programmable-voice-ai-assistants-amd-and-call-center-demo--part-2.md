---
title: 'Programmable Voice: AI Assistants, AMD, and Call Center Demo'
summary: 'This page covers three Programmable Voice capabilities on Telnyx: attaching
  a pre-configured AI assistant to an active call (including adding participants and
  stopping the assistant), configuring Answering Machine Detection (AMD) for outbound
  calls with standard and Premium modes plus iOS Call Screening support, and building
  a TeXML-based call center demo that forwards calls to multiple SIP-connected agents
  with optional voicemail and custom audio.'
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ai-assistant-start
- url: https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-center
updated_at: 2026-08-05T14:03:06Z
---

# Programmable Voice: AI Assistants, AMD, and Call Center Demo

*Part 2 of 3 — see also: [Part 1](programmable-voice-ai-assistants-amd-and-call-center-demo--part-1.md), [Part 3](programmable-voice-ai-assistants-amd-and-call-center-demo--part-3.md)*

This page covers three Programmable Voice capabilities on Telnyx: attaching a pre-configured AI assistant to an active call (including adding participants and stopping the assistant), configuring Answering Machine Detection (AMD) for outbound calls with standard and Premium modes plus iOS Call Screening support, and building a TeXML-based call center demo that forwards calls to multiple SIP-connected agents with optional voicemail and custom audio.

## Answering Machine Detection

Outbound calls placed with the Telnyx Voice API can be enabled with Answering Machine Detection (AMD, Voicemail Detection). When a call is answered, Telnyx runs real-time detection to determine if it was picked up by a human or a machine and sends webhooks with the analysis result.

### AMD Settings

The `answering_machine_detection` value when creating an outbound call or transferring an inbound call can be set to one of the following:

| Setting | Description | Webhooks Sent |
| --- | --- | --- |
| `detect` | *Only* detect if answering machine or human. | `call.machine.detection.ended` |
| `detect_beep` | Listens for a *final* "beep" sound after detecting a `machine` | `call.machine.detection.ended` and `call.machine.greeting.ended` **only** if a beep is detected |
| `detect_words` | After a `machine` is detected, a 30 second long beep detection will begin. Note the answering machine may still be playing it's greeting while the 30 seconds is counting down. | `call.machine.detection.ended` and `call.machine.greeting.ended` when the beep is detected or at the end of 30 seconds. |
| `greeting_end` | Listens for extended periods of silence or a beep in the greeting to determine if a greeting has ended. | `call.machine.detection.ended` and `call.machine.greeting.ended` |
| `premium` | **RECOMMENDED** Premium AMD uses advanced speech recognition technology and machine learning to achieve exceptional accuracy in determining whether a call has been connected to a live person or a machine. | `call.machine.premium.detection.ended` with one of `human_residence` or `human_business` or `machine` or `silence` or `fax_detected` or `not_sure`. If a beep is detected a `call.machine.premium.greeting.ended` webhook with `beep_detected` is also sent. If a beep is detected before `call.machine.premium.detection.ended`, `call.machine.premium.greeting.ended` is sent. If a beep is detected after `call.machine.premium.detection.ended`, both webhooks will be sent. |
| `premium_ios_call_screening_detection` | Premium AMD with iOS Call Screening support. Use this when calls may be answered by Apple Call Screening and you need to detect the screening prompt before continuing AMD. | `call.machine.premium.detection.ended`, `call.machine.premium.greeting.ended` with `result=prompt_ended` when the screening prompt ends without a beep, and `call.machine.premium.call_screening.detected` with `result=screening` when an Apple Call Screening tone is detected. |

#### Sample Dial Request

```
POST https://api.telnyx.com/v2/calls HTTP/1.1
Content-Type: application/json; charset=utf-8
Authorization: Bearer YOUR_API_KEY

{
  "connection_id" : "1494404757140276705",
  "to"            : "+19198675309",
  "from"          : "+19842550944",
  "webhook_url"   : "https://webhook_url.com/outbound_call_events",
  "answering_machine_detection" : "detect_words"
}
```

### iOS Call Screening Detection

Set `answering_machine_detection` to `premium_ios_call_screening_detection` to run Premium AMD with support for Apple Call Screening. In this mode, Telnyx uses Premium AMD first. If the initial Premium AMD result is `machine`, Telnyx listens for the iOS call-screening prompt to complete or for an Apple Call Screening tone.

When an Apple Call Screening tone is detected, Telnyx sends `call.machine.premium.call_screening.detected` with `result=screening` and then restarts Premium AMD on the screened call. If the screening prompt ends without a beep, Telnyx sends `call.machine.premium.greeting.ended` with `result=prompt_ended`. Use this webhook as the signal that your application can provide the response to the iOS screening prompt, such as who is calling and why.

Use `answering_machine_detection_config.prompt_end_timeout_millis` to control the maximum amount of time Telnyx waits for the iOS call-screening prompt to end after Premium AMD initially detects a `machine`. The default is `30000` milliseconds. The minimum value is `1000` milliseconds and the maximum value is `120000` milliseconds.

#### Sample Dial Request with iOS Call Screening Detection

```
{
  "connection_id": "1494404757140276705",
  "to": "+19198675309",
  "from": "+19842550944",
  "webhook_url": "https://webhook_url.com/outbound_call_events",
  "answering_machine_detection": "premium_ios_call_screening_detection",
  "answering_machine_detection_config": {
    "total_analysis_time_millis": 30000,
    "greeting_duration_millis": 2000,
    "prompt_end_timeout_millis": 30000
  }
}
```

#### iOS Call Screening Detection Order of Operations

1. Create an outbound call or transfer an inbound call with `answering_machine_detection` set to `premium_ios_call_screening_detection`.
2. Receive `call.initiated` webhook.
3. Receive `call.answered` webhook when the call is answered.
4. Receive `call.machine.premium.detection.ended` with the initial Premium AMD result.
5. If the initial result is `machine`, Telnyx waits for the call-screening prompt to end or for an Apple Call Screening tone.
6. If the prompt ends without a beep, receive `call.machine.premium.greeting.ended` with `result=prompt_ended`. After receiving this webhook, your application can provide the response to the iOS screening prompt, such as who is calling and why.
7. If an Apple Call Screening tone is detected, receive `call.machine.premium.call_screening.detected` with `result=screening`.
8. After the screening tone is detected, Telnyx restarts Premium AMD on the screened call. Expect another `call.machine.premium.detection.ended` webhook with the post-screening classification.
9. If the restarted Premium AMD detects a machine and later detects a beep, expect `call.machine.premium.greeting.ended` with `result=beep_detected`.

### General Order of Operations

1. Create outbound call.
2. Receive `call.initiated` webhook.
3. Receive `call.answered` webhook when the call is answered either by human or machine.
4. Receive `call.machine.detection.ended` webhook with human/machine status.
5. Receive `call.machine.greeting.ended` webhook when beep detected or 30 second timeout.

**Important:** at any point, the callee could hangup generating a `call.hangup` webhook.

### Standard Webhooks

#### call.machine.detection.ended

The `call.machine.detection.ended` is sent when Telnyx can make a determination on human or machine. The `data.payload.result` will contain the information about the answering machine:

| Result | Description |
| --- | --- |
| `human` | Human answered call |
| `machine` | Machine answered call |
| `not_sure` | *Recommended* to treat as if human answered. |

Sample webhook:

```
{
  "data": {
    "event_type": "call.machine.detection.ended",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "occurred_at": "2018-02-02T22:25:27.521992Z",
    "payload": {
      "call_control_id": "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ",
      "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
      "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
      "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
      "connection_id": "7267xxxxxxxxxxxxxx",
      "from": "+35319605860",
      "result": "machine",
      "to": "+13129457420"
    },
    "record_type": "event"
  }
}
```

#### call.machine.greeting.ended

If the `answering_machine_detection` was set to `detect_beep`, `detect_words`, or `greeting_end` you could receive a final webhook when the prompt (or beep detection) has finished. The `data.payload.result` will contain the information about the answering machine:

| Result | Description | AMD Setting |
| --- | --- | --- |
| `ended` | Greeting is over. | **ONLY** sent when setting is `greeting_end` |
| `beep_detected` | Beep has been detected | `detect_beep` and `detect_words` |
| `not_sure` | 30 second beep detection timeout fired after detecting a `machine` | `detect_beep` and `detect_words` |

Sample webhook:

```
{
  "data": {
    "event_type": "call.machine.greeting.ended",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "occurred_at": "2018-02-02T22:25:27.521992Z",
    "payload": {
      "call_control_id": "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ",
      "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
      "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
      "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
      "connection_id": "7267xxxxxxxxxxxxxx",
      "from": "+35319605860",
      "result": "ended",
      "to": "+13129457420"
    },
    "record_type": "event"
  }
}
```

### AMD Premium Webhooks

#### call.machine.premium.detection.ended

The `call.machine.premium.detection.ended` webhook is sent when the AMD process can determine whether the call was answered by a `human` or a `machine`. It is possible to specify the number of milliseconds that Telnyx should attempt to perform the detection via the `total_analysis_time_millis` setting. By default, the timeout is set to 30 seconds. If the timeout is reached before the detection is finished, the result in the webhook will be `not_sure`.

The `data.payload.result` will contain the information about the answering machine:

| Result | Description |
| --- | --- |
| `human_residence` | A human answered the call |
| `human_business` | A human answered call |
| `machine` | A machine answered the call |
| `silence` | No sound was detected |
| `fax_detected` | A Fax machine answered the call |
| `not_sure` | Not identifiable, or the configured AMD timeout was reached before the result was available. |

Sample webhook:

```
{
  "data": {
    "event_type": "call.machine.premium.detection.ended",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "occurred_at": "2018-02-02T22:25:27.521992Z",
    "payload": {
      "call_control_id": "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ",
      "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
      "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
      "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
      "connection_id": "7267xxxxxxxxxxxxxx",
      "from": "+35319605860",
      "result": "machine",
      "to": "+13129457420"
    },
    "record_type": "event"
  }
}
```

#### call.machine.premium.greeting.ended

If a `machine` answered the call, you may receive a final webhook when the beep detection has finished. This webhook is *optional* and will only be sent if one of three things happens:

- A beep is detected. In this case, the result is `beep_detected`.
- The optional AMD timeout is reached after the call was answered by a `machine`, but no beep was heard. For this case, the result is `no_beep_detected`.
- The iOS call-screening prompt ends without a beep when using `premium_ios_call_screening_detection`. For this case, the result is `prompt_ended`. After receiving this result, your application can provide the response to the iOS screening prompt, such as who is calling and why.

The `data.payload.result` will contain the information about the answering machine:

| Result | Description | AMD Setting |
| --- | --- | --- |
| `beep_detected` | Greeting is over. | **ONLY** sent when a `machine` answered the call, and a beep was heard. |
| `no_beep_detected` | **ONLY** sent when a `machine` answered the call, and the AMD timeout was reached before a beep was heard. | |
| `prompt_ended` | The iOS call-screening prompt ended without a beep. After receiving this result, your application can provide the response to the iOS screening prompt, such as who is calling and why. | **ONLY** sent when using `premium_ios_call_screening_detection`. |

Sample webhook:

```
{
  "data": {
    "event_type": "call.machine.premium.greeting.ended",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "occurred_at": "2018-02-02T22:25:27.521992Z",
    "payload": {
      "call_control_id": "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ",
      "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
      "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
      "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
      "connection_id": "7267xxxxxxxxxxxxxx",
      "from": "+35319605860",
      "result": "beep_detected",
      "to": "+13129457420"
    },
    "record_type": "event"
  }
}
```

#### call.machine.premium.call_screening.detected

The `call.machine.premium.call_screening.detected` webhook is sent when `premium_ios_call_screening_detection` detects an Apple Call Screening tone. The `data.payload.result` value is `screening`.

After this webhook is sent, Telnyx restarts Premium AMD on the screened call. This webhook is not terminal; expect another `call.machine.premium.detection.ended` webhook with the post-screening classification, and possibly `call.machine.premium.greeting.ended` if a beep is detected after the restart.

Sample webhook:

```
{
  "data": {
    "event_type": "call.machine.premium.call_screening.detected",
    "id": "0ccc7b54-4df3-4bca-a65a-3da1ecc777f0",
    "occurred_at": "2018-02-02T22:25:27.521992Z",
    "payload": {
      "call_control_id": "v2:T02llQxIyaRkhfRKxgAP8nY511EhFLizdvdUKJiSw8d6A9BborherQ",
      "call_leg_id": "428c31b6-7af4-4bcb-b7f5-5013ef9657c1",
      "call_session_id": "428c31b6-abf3-3bc1-b7f4-5013ef9657c1",
      "client_state": "aGF2ZSBhIG5pY2UgZGF5ID1d",
      "connection_id": "7267xxxxxxxxxxxxxx",
      "from": "+35319605860",
      "result": "screening",
      "to": "+13129457420"
    },
    "record_type": "event"
  }
}
```
