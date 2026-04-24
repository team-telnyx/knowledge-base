---
title: Dial
summary: The `` verb transfers an existing call to another destination.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/dial/index
    content_hash: 09c0b1d9171e17834b85c016b7dfe873217b5bdde84bb7790ebc3bce07b6b1d0
updated_at: 2026-04-10T00:00:00Z
---

# Dial

The `` verb transfers an existing call to another destination. `` will end this new call if: the called party does not answer, the number does not exist, or Telnyx receives a busy signal.

## Attributes

<table>
  <thead>
    <tr>
      <th>ATTRIBUTE</th>
      <th>DESCRIPTION</th>
      <th>OPTIONS</th>
      <th>DEFAULT</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>action</code></td>
      <td> Optional URL where TeXML will make a request when the `` call ends to retrieve a new set of TeXML instructions to continue the call flow. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>method</code></td>
      <td> HTTP method to use when requesting the action URL. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>callerId</code></td>
      <td> Caller ID that must be a valid E.164 format number. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>fromDisplayName</code></td>
      <td> The fromDisplayName string to be used as the caller id name (SIP From Display Name) presented to the destination. The string should have a maximum of 128 characters, containing only letters, numbers, spaces, and -\_\~!.+ special characters. If omitted, the display name will be the same as the number in the callerId field. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>hangupOnStar</code></td>
      <td> The hangupOnStar attribute lets the initial caller hang up on the called party by pressing the '\*' key on their phone. Does not apply for the Conference noun. </td>

      <td />

      <td><code>false</code></td>
    </tr>

    <tr>
      <td><code>timeout</code></td>
      <td> The number of seconds to wait for the called party to answer the call. </td>
      <td><code>5</code> - <code>120</code></td>
      <td><code>30</code></td>
    </tr>

    <tr>
      <td><code>timeLimit</code></td>
      <td> The maximum duration of the call in seconds. </td>
      <td><code>60</code> - <code>14400</code></td>
      <td><code>14400</code></td>
    </tr>

    <tr>
      <td><code>record</code></td>
      <td> The record attribute lets you record both legs of a call within the associated `` verb. It works with the `` and `` nouns only. If you want to record the conference, please use the record attribute on `` noun. Recordings are available in two options: single or dual. </td>
      <td><code>do-not-record</code>, <code>record-from-answer</code>, <code>record-from-ringing</code>, <code>record-from-answer-dual</code>, <code>record-from-ringing-dual</code></td>
      <td><code>do-not-record</code></td>
    </tr>

    <tr>
      <td><code>recordingChannels</code></td>
      <td> The number of channels in the final recording. Possible values are: single (for mono) and dual (for stereo). Defaults to single. </td>
      <td><code>single</code>, <code>dual</code></td>
      <td><code>single</code></td>
    </tr>

    <tr>
      <td><code>recordMaxLength</code></td>
      <td> Defines the maximum length for the recording in seconds (0 for infinite) </td>
      <td><code>0</code> - <code>14400</code></td>
      <td><code>0</code></td>
    </tr>

    <tr>
      <td><code>recordingStatusCallback</code></td>
      <td> Optional URL that tells Telnyx where to make its GET or POST request when the recording is available. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>recordingStatusCallbackMethod</code></td>
      <td> HTTP request type used for recordingStatusCallback. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>recordingStatusCallbackEvent</code></td>
      <td> The recording events for which Telnyx should send a webhook. Multiple events are separated by a space. </td>
      <td><code>in-progress</code>, <code>completed</code>, <code>absent</code></td>
      <td><code>completed</code></td>
    </tr>

    <tr>
      <td><code>sendRecordingUrl</code></td>
      <td> Defines if the recording URL is sent in the callbacks. </td>

      <td />

      <td><code>true</code></td>
    </tr>

    <tr>
      <td><code>ringTone</code></td>
      <td> The ringback tone played back to the caller. </td>
      <td><code>at</code>, <code>au</code>, <code>bg</code>, <code>br</code>, <code>be</code>, <code>ch</code>, <code>cl</code>, <code>cn</code>, <code>cz</code>, <code>de</code>, <code>dk</code>, <code>ee</code>, <code>es</code>, <code>fi</code>, <code>fr</code>, <code>gr</code>, <code>hu</code>, <code>il</code>, <code>in</code>, <code>it</code>, <code>lt</code>, <code>jp</code>, <code>mx</code>, <code>my</code>, <code>nl</code>, <code>no</code>, <code>nz</code>, <code>ph</code>, <code>pl</code>, <code>pt</code>, <code>ru</code>, <code>se</code>, <code>sg</code>, <code>th</code>, <code>tw</code>, <code>ve</code>, <code>za</code>, <code>us</code>, <code>us-old</code>, <code>uk</code></td>
      <td><code>us</code></td>
    </tr>

    <tr>
      <td><code>audioUrl</code></td>
      <td> A URL to an audio file that will be played as a custom ringback tone to the caller while waiting for the call to be answered. When set, overrides the ringTone attribute. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>answerOnBridge</code></td>
      <td> If set to true, the inbound call will not be answered until the dialed call is answered. This preserves the ringing state on the caller's side. Only takes effect when the inbound call has not yet been answered. </td>

      <td />

      <td><code>false</code></td>
    </tr>

    <tr>
      <td><code>passDiversionHeader</code></td>
      <td> When set to true, the Diversion SIP header from the inbound call is passed through to the outbound dial attempt. </td>

      <td />

      <td><code>false</code></td>
    </tr>

    <tr>
      <td><code>machineDetectionSpeechThreshold</code></td>
      <td> Maximum duration of a greeting in milliseconds. If a greeting is longer than this value, the call is classified as a machine. Only used when machineDetection is enabled and detectionMode is Premium. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>machineDetectionSpeechEndThreshold</code></td>
      <td> Silence duration in milliseconds after a greeting to wait before classifying the call as a machine. Only used when machineDetection is enabled and detectionMode is Premium. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>machineDetectionSilenceTimeout</code></td>
      <td> Maximum duration of initial silence in milliseconds before the call is classified as a machine. Only used when machineDetection is enabled and detectionMode is Premium. </td>

      <td />

      <td>-</td>
    </tr>
  </tbody>
</table>

## Child verbs/nouns

<table>
  <thead>
    <tr>
      <th>NOUN/VERB</th>
      <th>DESCRIPTION</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>Number</code></td>
      <td> Specifies a phone number to dial. </td>
    </tr>

    <tr>
      <td><code>Sip</code></td>
      <td> The `` noun specifies a SIP endpoint to dial. </td>
    </tr>

    <tr>
      <td><code>Queue</code></td>
      <td> The `` noun allows you to add a call to a queue. </td>
    </tr>
  </tbody>
</table>

## Number Attributes

<table>
  <thead>
    <tr>
      <th>ATTRIBUTE</th>
      <th>DESCRIPTION</th>
      <th>OPTIONS</th>
      <th>DEFAULT</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>statusCallback</code></td>
      <td> A URL for Telnyx to send webhook requests to on each event specified in the statusCallbackEvent attribute for outbound calls only. Inbound Status Callback events can be configured for TeXML the connection settings in the Mission Control Portal. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>statusCallbackEvent</code></td>
      <td> The call events for which Telnyx should send a webhook. Multiple events are separated by a space. </td>
      <td><code>initiated</code>, <code>ringing</code>, <code>answered</code>, <code>amd</code>, <code>dtmf</code>, <code>completed</code></td>
      <td><code>completed</code></td>
    </tr>

    <tr>
      <td><code>statusCallbackMethod</code></td>
      <td> HTTP request type Telnyx should use when requesting the statusCallback URL. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>url</code></td>
      <td> Optional URL to another TeXML document that can contain `` and `` verbs so that the called party can chose to take an action on the incoming call before the two parties are connected. The callee will continue to hear ringback while the url document is executed. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>method</code></td>
      <td> HTTP request type used for url. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>sendDigits</code></td>
      <td> Specifies DTMF tones to play when the call is answered. The value can include: digits 0-9, #, \*, and w. 'w' indicates a 0.5 second pause. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>machineDetection</code></td>
      <td> Enables Answering Machine Detection. Note: add amd event type to statusCallbackEvent list to receive the detection result webhook. </td>
      <td><code>Enable</code>, <code>DetectMessageEnd</code>, <code>Disable</code></td>
      <td><code>Disable</code></td>
    </tr>

    <tr>
      <td><code>detectionMode</code></td>
      <td> Sets the Answering Detection mode. </td>
      <td><code>Regular</code>, <code>Premium</code></td>
      <td><code>Regular</code></td>
    </tr>

    <tr>
      <td><code>machineDetectionTimeout</code></td>
      <td> Maximum timeout threshold for overall detection, in milliseconds. </td>
      <td><code>500</code> - <code>60000</code></td>
      <td><code>3500</code></td>
    </tr>
  </tbody>
</table>

## Sip Attributes

<table>
  <thead>
    <tr>
      <th>ATTRIBUTE</th>
      <th>DESCRIPTION</th>
      <th>OPTIONS</th>
      <th>DEFAULT</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>username</code></td>
      <td> Username to use for SIP authentication. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>password</code></td>
      <td> Password to use for SIP authentication. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>statusCallback</code></td>
      <td> A URL for Telnyx to send webhook requests to on each event specified in the statusCallbackEvent attribute for outbound calls only. Inbound Status Callback events can be configured for TeXML the connection settings in the Mission Control Portal. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>statusCallbackEvent</code></td>
      <td> The call events for which Telnyx should send a webhook. Multiple events are separated by a space. </td>
      <td><code>initiated</code>, <code>ringing</code>, <code>answered</code>, <code>amd</code>, <code>dtmf</code>, <code>completed</code></td>
      <td><code>completed</code></td>
    </tr>

    <tr>
      <td><code>statusCallbackMethod</code></td>
      <td> HTTP request type Telnyx should use when requesting the statusCallback URL. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>url</code></td>
      <td> Optional URL to another TeXML document that can contain `` and `` verbs so that the called party can chose to take an action on the incoming call before the two parties are connected. The callee will continue to hear ringback while the url document is executed. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>method</code></td>
      <td> HTTP request type used for url. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>machineDetection</code></td>
      <td> Enables Answering Machine Detection. Note: add amd event type to statusCallbackEvent list to receive the detection result webhook. </td>
      <td><code>Enable</code>, <code>DetectMessageEnd</code>, <code>Disable</code></td>
      <td><code>Disable</code></td>
    </tr>

    <tr>
      <td><code>detectionMode</code></td>
      <td> Sets the Answering Detection mode. </td>
      <td><code>Regular</code>, <code>Premium</code></td>
      <td><code>Regular</code></td>
    </tr>

    <tr>
      <td><code>machineDetectionTimeout</code></td>
      <td> Maximum timeout threshold for overall detection, in milliseconds. </td>
      <td><code>500</code> - <code>60000</code></td>
      <td><code>3500</code></td>
    </tr>
  </tbody>
</table>

## Queue Attributes

<table>
  <thead>
    <tr>
      <th>ATTRIBUTE</th>
      <th>DESCRIPTION</th>
      <th>OPTIONS</th>
      <th>DEFAULT</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>url</code></td>
      <td> Optional URL to another TeXML document that can contain ``, ``, ``, `` and `` verbs. The document will be executed on the queued call before bridging the calls. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>method</code></td>
      <td> HTTP request type used for url. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>
  </tbody>
</table>

## Simultaneous dialing

You can use multiple `` and `` nouns within a `` verb to dial multiple phone numbers and SIP addresses at the same time. The first person to answer the call will be connected to the caller, while the rest of the call attempts are hung up:

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    +18775551212
    sip:connection@sip.telnyx.com
    +18771234567

```

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Dial action="/nextinstructions.php" callerId="+13120001234">+19999999999

```

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Dial action="/nextinstructions.php" callerId="+13120001234">
      <Number statusCallback="https://foo.com/my_call_stats" statusCallbackEvent="initiated ringing answered completed">+19999999999

```

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Dial action="/nextinstructions.php" callerId="+13120001234" hangupOnStar="true">
      <Sip statusCallback="https://foo.com/my_sip_call_stats" statusCallbackEvent="initiated">sip:connection@sip.telnyx.com

```

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Dial action="/nextinstructions.php" callerId="+13120001234">
      <Number statusCallback="https://foo.com/my_call_stats" statusCallbackEvent="initiated ringing answered completed amd" machineDetection="Enable" detectionMode="Regular">+19999999999

```

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Dial action="/nextinstructions.php" callerId="+13120001234">
      <Number statusCallback="https://foo.com/my_call_stats" statusCallbackEvent="initiated ringing answered completed amd" machineDetection="Enable" detectionMode="Regular">+19999999999

```

## Expected callbacks

If `action` is set, a callback is sent when the dialed call ends. See [Dial Action Callback](https://developers.telnyx.com/api-reference/callbacks/texml-call-completed) for the full payload reference.

The `error_code` and `error_message` fields are provided only in case of failed calls. The full list of errors can be found under the [API Errors](../reference/api-error-codes.md) page.

If `statusCallbackEvent` is set, the following webhooks are sent based on configured events:

| Event       | Callback Reference                                              |
| ----------- | --------------------------------------------------------------- |
| `initiated` | [Call Initiated](https://developers.telnyx.com/api-reference/callbacks/texml-call-initiated) |
| `ringing`   | [Call Ringing](https://developers.telnyx.com/api-reference/callbacks/texml-call-ringing)     |
| `answered`  | [Call Answered](https://developers.telnyx.com/api-reference/callbacks/texml-call-answered)   |
| `completed` | [Call Completed](https://developers.telnyx.com/api-reference/callbacks/texml-call-completed) |

If `machineDetection` is enabled, an AMD callback is sent to `amdStatusCallback`. See [AMD Callback](https://developers.telnyx.com/api-reference/callbacks/texml-call-amd) for the full payload reference.

If `recordingStatusCallbackEvent` is set, the following webhooks are sent:

| Event         | Callback Reference                                                            |
| ------------- | ----------------------------------------------------------------------------- |
| `in-progress` | [Recording In Progress](https://developers.telnyx.com/api-reference/callbacks/texml-recording-in-progress) |
| `completed`   | [Recording Completed](https://developers.telnyx.com/api-reference/callbacks/texml-recording-completed)     |
