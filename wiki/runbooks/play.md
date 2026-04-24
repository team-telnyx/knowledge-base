---
title: Play
summary: The `` verb plays an MP3 or WAV audio file, which Telnyx fetches back to the caller from the URL you configure.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/play/index
    content_hash: f2fe742e4d9e6ca96f1146c6d51d5768a7705809140c9f15977ceffe3bf746f3
updated_at: 2026-04-10T00:00:00Z
---

# Play

The `` verb plays an MP3 or WAV audio file, which Telnyx fetches back to the caller from the URL you configure.
Alternatively, specify `mediaStorage="true"` to fetch a file you previously uploaded to Telnyx using media storage APIs. When `mediaStorage="true"` is used the verb expects a `media_name` instead of a URL.
You can also use the `digits` attribute to play DTMF tones instead of an audio file.
`` can be used independently as a verb or nested within `` as a noun to play an audio file while waiting for DTMF tones.

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
      <td><code>loop</code></td>
      <td> Times to repeat the audio </td>

      <td />

      <td><code>1</code></td>
    </tr>

    <tr>
      <td><code>mediaStorage</code></td>
      <td> When true fetches the file from Telnyx media storage using the provided media name. </td>
      <td><code>true</code>, <code>false</code></td>
      <td><code>false</code></td>
    </tr>

    <tr>
      <td><code>digits</code></td>
      <td> DTMF tones to play. The value can include digits 0-9, \*, #, and w (for a 0.5 second pause). When specified, the verb plays DTMF tones instead of an audio file. </td>

      <td />

      <td>-</td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    https://example.com/welcome.mp3

```
