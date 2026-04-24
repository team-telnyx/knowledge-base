---
title: Conference
summary: The `` verb's `` noun allows you to connect to a conference room.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference/index
    content_hash: 6a10d9d4c2a3ccd1416c92cdec4442899a8960e8434fcbf4fe3fe22d54e65cc8
updated_at: 2026-04-10T00:00:00Z
---

# Conference

The `` verb's `` noun allows you to connect to a conference room. Much like how the `` noun allows you to connect to another phone number, the `` noun allows you to connect to a named conference room and talk with the other callers who have also connected to that room. Conference is commonly used as a container for calls when implementing hold, transfer, and barge. If the specified conference name does not exist, a new conference will be created.

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
      <td><code>muted</code></td>
      <td> Specify whether a participant is muted or not. </td>

      <td />

      <td><code>false</code></td>
    </tr>

    <tr>
      <td><code>startConferenceOnEnter</code></td>
      <td> Start the conference when a participant joins. If this is <code>false</code> and the participant joins a conference that has not started, they are muted and hear background music until a participant joins where <code>startConferenceOnEnter</code> is <code>true</code>. This is useful for implementing moderated conferences. </td>

      <td />

      <td><code>true</code></td>
    </tr>

    <tr>
      <td><code>endConferenceOnExit</code></td>
      <td> If a participant has this attribute set to <code>true</code>, then when that participant leaves, the conference ends and all other participants drop out. This is useful for implementing moderated conferences that bridge two calls and allow either call leg to continue executing TexML if the other hangs up. </td>

      <td />

      <td><code>false</code></td>
    </tr>

    <tr>
      <td><code>maxParticipants</code></td>
      <td> The maximum number of participants allowed in the conference. </td>
      <td><code>2</code> - <code>250</code></td>
      <td><code>250</code></td>
    </tr>

    <tr>
      <td><code>beep</code></td>
      <td> Specify whether a notification beep is played to the conference when a participant joins or leaves the conference. The participant joining the conference will never hear a beep. Note: this attribute does not affect the recording start beep. To disable the beep played when recording starts, set the recordBeep attribute to false. </td>
      <td><code>true</code>, <code>false</code>, <code>onEnter</code>, <code>onExit</code></td>
      <td><code>true</code></td>
    </tr>

    <tr>
      <td><code>participantLabel</code></td>
      <td> A unique label for the participant which will be added into the conference as a result of executing the TeXML instruction. The label can be used to read or update participant attributes using the TeXML REST API. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>record</code></td>
      <td> The <code>record</code> attribute lets you record entire conference. When set to <code>record-from-start</code>, recording begins immediately after the conference starts </td>
      <td><code>do-not-record</code>, <code>record-from-start</code></td>
      <td><code>do-not-record</code></td>
    </tr>

    <tr>
      <td><code>recordBeep</code></td>
      <td> If enabled, a beep sound will be played at the start of a recording. This is independent of the beep attribute, which only controls join/leave notification sounds. Set to false to disable the recording start beep. </td>

      <td />

      <td><code>true</code></td>
    </tr>

    <tr>
      <td><code>recordingStatusCallback</code></td>
      <td> Optional URL that tells Telnyx where to make its GET or POST request when the recording is available. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>recordingStatusCallbackEvent</code></td>
      <td> The recording events for which Telnyx should send a webhook. Multiple events are separated by a space. </td>
      <td><code>in-progress</code>, <code>completed</code>, <code>absent</code></td>
      <td><code>completed</code></td>
    </tr>

    <tr>
      <td><code>recordingStatusCallbackMethod</code></td>
      <td> HTTP request type used for <code>recordingStatusCallback</code>. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>recordingTimeout</code></td>
      <td> The number of seconds that Telnyx will wait for the recording to be stopped if silence is detected. The timer only starts when the speech is detected. Please note that the transcription is used to detect silence and the related charge will be applied. 0 means no timeout. </td>
      <td><code>0</code> - <code>14400</code></td>
      <td><code>0</code></td>
    </tr>

    <tr>
      <td><code>trim</code></td>
      <td> Whether to trim any leading and trailing silence from the recording. </td>
      <td><code>trim-silence</code>, <code>do-not-trim</code></td>
      <td><code>do-not-trim</code></td>
    </tr>

    <tr>
      <td><code>sendRecordingUrl</code></td>
      <td> Defines if the recording URL is sent in the callbacks. </td>

      <td />

      <td><code>true</code></td>
    </tr>

    <tr>
      <td><code>statusCallback</code></td>
      <td> A URL for Telnyx to send webhook requests to on each event specified in the <code>statusCallbackEvent</code> attribute. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>statusCallbackMethod</code></td>
      <td> HTTP method to use when requesting the status callback URL. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>statusCallbackEvent</code></td>
      <td> The conference events for which Telnyx should send a webhook on. Multiple events are separated by a space. </td>
      <td><code>start</code>, <code>end</code>, <code>join</code>, <code>leave</code>, <code>speaker</code></td>
      <td>-</td>
    </tr>

    <tr>
      <td><code>waitUrl</code></td>
      <td> A URL to an MP3 or WAV file that should be used for the conference's hold music before the conference starts. The URL can also return an XML document with instructions that will be executed while the call is waiting for the conference to start. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>waitMethod</code></td>
      <td> HTTP method to use when requesting the wait URL. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Dial  action="/nextinstructions.php">
        conference_name

```

## Expected callbacks

If `statusCallbackEvent` is set, the following webhooks are sent based on configured events:

| Event     | Callback Reference                                                       |
| --------- | ------------------------------------------------------------------------ |
| `start`   | [Conference Start](https://developers.telnyx.com/api-reference/callbacks/texml-conference-start)      |
| `end`     | [Conference End](https://developers.telnyx.com/api-reference/callbacks/texml-conference-end)          |
| `join`    | [Participant Join](https://developers.telnyx.com/api-reference/callbacks/texml-conference-join)       |
| `leave`   | [Participant Leave](https://developers.telnyx.com/api-reference/callbacks/texml-conference-leave)     |
| `speaker` | [Participant Speaker](https://developers.telnyx.com/api-reference/callbacks/texml-conference-speaker) |


## Related Pages

- [Conference participants](../runbooks/conference-participants.md)
