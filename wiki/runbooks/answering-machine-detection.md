---
title: Answering Machine Detection
summary: Telnyx's Programmable Voice lets you build custom answering machine detection features into your voice applications.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection/index
    content_hash: 5596759c176dc7ee5d71580d0a874b7b324244b8575c8c182bb69658c6391a50
updated_at: 2026-04-10T00:00:00Z
---

# Answering Machine Detection

Telnyx's Programmable Voice lets you build custom answering machine detection features into your voice applications.

Outbound calls placed with the Telnyx Voice API can be enabled with Answering Machine Detection (AMD, Voicemail Detection).

When a call is answered, Telnyx runs real-time detection to determine if it was picked up by a human or a machine and sends webhooks with the analysis result.

## AMD settings

The `answering_machine_detection` value when creating an outbound call or transferring an inbound call can be set to one of the following:

<table>
  <tbody>
    <tr>
      <td>Setting</td>
      <td>Description</td>
      <td>Webhooks Sent</td>
    </tr>

    <tr>
      <td><code>detect</code></td>
      <td><em>Only</em> detect if answering machine or human.</td>
      <td><code>call.machine.detection.ended</code></td>
    </tr>

    <tr>
      <td><code>detect\_beep</code></td>
      <td>Listens for a <em>final</em> "beep" sound after detecting a <code>machine</code></td>
      <td><code>call.machine.detection.ended</code> and <code>call.machine.greeting.ended</code> <strong>only</strong> if a beep is detected</td>
    </tr>

    <tr>
      <td><code>detect\_words</code></td>
      <td>After a <code>machine</code> is detected, a 30 second long beep detection will begin. Note the answering machine may still be playing it's greeting while the 30 seconds is counting down.</td>
      <td><code>call.machine.detection.ended</code> and <code>call.machine.greeting.ended</code> when the beep is detected or at the end of 30 seconds.</td>
    </tr>

    <tr>
      <td><code>greeting\_end</code></td>
      <td>Listens for extended periods of silence or a beep in the greeting to determine if a greeting has ended.</td>
      <td><code>call.machine.detection.ended</code> and <code>call.machine.greeting.ended</code></td>
    </tr>

    <tr>
      <td><code>premium</code></td>
      <td><strong>RECOMMENDED</strong> Premium AMD uses advanced speech recognition technology and machine learning to achieve exceptional accuracy in determining whether a call has been connected to a live person or a machine.</td>
      <td><code>call.machine.premium.detection.ended</code> with one of <code>human\_residence</code> or <code>human\_business</code> or <code>machine</code> or <code>silence</code> or <code>fax\_detected</code> or <code>not\_sure</code>. If a beep is detected a <code>call.machine.premium.greeting.ended</code> webhook with <code>beep\_detected</code> is also sent. If a beep is detected before <code>call.machine.premium.detection.ended</code>, <code>call.machine.premium.greeting.ended</code> is sent. If a beep is detected after <code>call.machine.premium.detection.ended</code>, both webhooks will be sent.</td>
    </tr>
  </tbody>
</table>

### Sample dial request

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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

### General order of operations

1. Create outbound call.
2. Receive `call.initiated` webhook.
3. Receive `call.answered` webhook when the call is answered either by human or machine.
4. Receive `call.machine.detection.ended` webhook with human/machine status.
5. Receive `call.machine.greeting.ended` webhook when beep detected or 30 second timeout.

x. **Important** at any point, the callee could hangup generating a `call.hangup` webhook.

## Webhooks

### call.machine.detection.ended

The `call.machine.detection.ended` is sent when Telnyx can make a determination on human or machine.

The `data.payload.result` will contain the information about the answering machine:

<table>
  <tbody>
    <tr>
      <td>Result</td>
      <td>Description</td>
    </tr>

    <tr>
      <td><code>human</code></td>
      <td>Human answered call</td>
    </tr>

    <tr>
      <td><code>machine</code></td>
      <td>Machine answered call</td>
    </tr>

    <tr>
      <td><code>not\_sure</code></td>
      <td><em>Recommended</em> to treat as if human answered.</td>
    </tr>
  </tbody>
</table>

#### Sample Webhook

```json theme={null}
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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

### call.machine.greeting.ended

If the `answering_machine_detection` was set to `detect_beep`, `detect_words`, `greeting_end` you could receive a final webhook when the prompt (or beep detection) has finished.

The `data.payload.result` will contain the information about the answering machine:

<table>
  <tbody>
    <tr>
      <td>Result</td>
      <td>Description</td>
      <td>AMD Setting</td>
    </tr>

    <tr>
      <td><code>ended</code></td>
      <td>Greeting is over.</td>
      <td><strong>ONLY</strong> sent when setting is <code>greeting\_end</code></td>
    </tr>

    <tr>
      <td><code>beep\_detected</code></td>
      <td>Beep has been detected</td>
      <td><code>detect\_beep</code> and <code>detect\_words</code></td>
    </tr>

    <tr>
      <td><code>not\_sure</code></td>
      <td>30 second beep detection timeout fired after detecting a <code>machine</code></td>
      <td><code>detect\_beep</code> and <code>detect\_words</code></td>
    </tr>
  </tbody>
</table>

#### Sample Webhook

```json theme={null}
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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

## AMD premium Webhooks

### call.machine.premium.detection.ended

The `call.machine.premium.detection.ended` webhook is sent when the AMD process can determine whether the call was answered by a `human` or a `machine`. It is possible to specify the number of milliseconds that Telnyx should attempt to perform the detection via the `total_analysis_time_millis` setting. By default, the timeout is set to 30 seconds. If the timeout is reached before the detection is finished, the result in the webhook will be `not_sure`.

The `data.payload.result` will contain the information about the answering machine:

<table>
  <tbody>
    <tr>
      <td>Result</td>
      <td>Description</td>
    </tr>

    <tr>
      <td><code>human\_residence</code></td>
      <td>A human answered the call</td>
    </tr>

    <tr>
      <td><code>human\_business</code></td>
      <td>A human answered call</td>
    </tr>

    <tr>
      <td><code>machine</code></td>
      <td>A machine answered the call</td>
    </tr>

    <tr>
      <td><code>silence</code></td>
      <td>No sound was detected</td>
    </tr>

    <tr>
      <td><code>fax\_detected</code></td>
      <td>A Fax machine answered the call</td>
    </tr>

    <tr>
      <td><code>not\_sure</code></td>
      <td>Not identifiable, or the configured AMD timeout was reached before the result was available.</td>
    </tr>
  </tbody>
</table>

#### Sample Webhook

```json theme={null}
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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added

### call.machine.premium.greeting.ended

If a <code>machine</code> answered the call, you may receive a final webhook when the beep detection has finished. This webhook is <em>optional</em> and will only be sent if one of two happens:

* a beep is detected. In this case, the result is `beep_detected`.
* the optional AMD timeout is reached after the call was answered by a <code>machine</code>, but no beep was heard. For this case, the result is `no_beep_detected`.

The `data.payload.result` will contain the information about the answering machine:

<table>
  <tbody>
    <tr>
      <td>Result</td>
      <td>Description</td>
      <td>AMD Setting</td>
    </tr>

    <tr>
      <td><code>beep\_detected</code></td>
      <td>Greeting is over.</td>
      <td><strong>ONLY</strong> sent when a <code>machine</code> answered the call, and a beep was heard.</td>
    </tr>

    <tr>
      <td><code>no\_beep\_detected</code></td>
      <td><strong>ONLY</strong> sent when a <code>machine</code> answered the call, and the AMD timeout was reached before a beep was heard.</td>

      <td />
    </tr>
  </tbody>
</table>

#### Sample Webhook

```json theme={null}
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

<Callout type="info">
  After pasting the above content, Kindly check and remove any new line added


## Related Pages

- [TeXML Answering Machine Detection Support](../runbooks/texml-answering-machine-detection-support.md)
