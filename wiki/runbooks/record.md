---
title: Record
summary: The `` verb creates an audio file with the call audio.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/record/index
    content_hash: db4dc95c37467f3b04411565cb6779b2473718ecd17e2256c7a5e2a98a32241b
updated_at: 2026-04-10T00:00:00Z
---

# Record

The `` verb creates an audio file with the call audio. If a recordingStatusCallback, Telnyx will deliver the URL for the recording to that address once the call has ended. Recording URLs are valid for 10 minutes after the call has ended. All recordings are also available via the <a href="https://portal.telnyx.com/">Telnyx Mission Control Portal</a>
**Note** In addition to recording, the `` verb supports automatic transcription by setting `transcription="true"` and providing a `transcriptionCallback` URL. The transcription result will be sent via webhook.

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
      <td> Optional URL where TeXML will make a request when the `` ends to retrieve a new set of TeXML instructions to continue the call flow sent with additional request parameters. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>method</code></td>
      <td> HTTP request type used to retrieve the next set of instructions. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>finishOnKey</code></td>
      <td> Set of digits specified together, any one of which will end the recording. Supported characters values: Any digit, #, \*. </td>

      <td />

      <td><code>1234567890\*#</code></td>
    </tr>

    <tr>
      <td><code>timeout</code></td>
      <td> The number of seconds that Telnyx will wait for the recording to be stopped if silence is detected. The timer only starts when the speech is detected. Please note that the transcription is used to detect silence and the related charge will be applied. 0 for infinite. </td>

      <td />

      <td><code>0</code></td>
    </tr>

    <tr>
      <td><code>maxLength</code></td>
      <td> Defines the maximum length for the recording in seconds. 0 for infinite. </td>
      <td><code>0</code> - <code>14400</code></td>
      <td><code>3600</code></td>
    </tr>

    <tr>
      <td><code>playBeep</code></td>
      <td> Whether or not a sound is played before the start of a recording. </td>

      <td />

      <td><code>true</code></td>
    </tr>

    <tr>
      <td><code>trim</code></td>
      <td> Will remove silence from the beginning and end of the recording when set to trim-silence. </td>
      <td><code>trim-silence</code></td>
      <td>-</td>
    </tr>

    <tr>
      <td><code>channels</code></td>
      <td> When using dual channels, the final audio file will be stereo recorded with the first leg on channel A, and the rest on channel B. </td>
      <td><code>single</code>, <code>dual</code></td>
      <td><code>dual</code></td>
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
      <td><code>transcription</code></td>
      <td> Enables automatic transcription of the recorded audio. When set to 'true', a transcription will be generated and delivered to the transcriptionCallback URL. </td>
      <td><code>true</code>, <code>false</code></td>
      <td><code>false</code></td>
    </tr>

    <tr>
      <td><code>transcriptionCallback</code></td>
      <td> The URL where Telnyx will send the transcription result once available. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>transcriptionEngine</code></td>
      <td> Specifies the engine to use for transcription. </td>
      <td><code>A</code>, <code>B</code></td>
      <td><code>A</code></td>
    </tr>

    <tr>
      <td><code>transcriptionLanguage</code></td>
      <td> Language to use for transcription when transcription is enabled. </td>

      <td />

      <td><code>en-US</code></td>
    </tr>

    <tr>
      <td><code>format</code></td>
      <td> The format of the recording file. </td>
      <td><code>mp3</code>, <code>wav</code></td>
      <td><code>mp3</code></td>
    </tr>

    <tr>
      <td><code>recordingStatusCallbackEvent</code></td>
      <td> The recording events for which Telnyx should send a webhook to the recordingStatusCallback URL. Multiple events are separated by a space. </td>
      <td><code>in-progress</code>, <code>completed</code></td>
      <td><code>completed</code></td>
    </tr>
  </tbody>
</table>

## Examples

Example 1

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Record action="https://example.com/recording-complete" 
            maxLength="30" 
            playBeep="true"/>

```

Example 2

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

  <Say voice="Telnyx.KokoroTTS.af">This call will be recorded and transcribed for quality purposes.
  <Record 
    action="https://example.com/recording-complete" 
    method="POST"
    maxLength="60"
    timeout="5"
    transcription="true"
    transcriptionEngine="A"
    transcriptionCallback="https://example.com/transcription-result" />

```

## Expected callbacks

If `action` or `statusCallback` is set, recording status callbacks are sent:

| Event         | Callback Reference                                                            |
| ------------- | ----------------------------------------------------------------------------- |
| `in-progress` | [Recording In Progress](https://developers.telnyx.com/api-reference/callbacks/texml-recording-in-progress) |
| `completed`   | [Recording Completed](https://developers.telnyx.com/api-reference/callbacks/texml-recording-completed)     |

If `transcribe` is enabled, a transcription callback is sent to `transcribeCallback`:

See [Transcription Callback](https://developers.telnyx.com/api-reference/callbacks/texml-transcription) for the full payload reference.
