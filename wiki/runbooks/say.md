---
title: Say
summary: The `` verb speaks the text specified back to the caller, enabling text-to-speech for any application.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/say/index
    content_hash: d9b380aa1bac6ef2417bd7f9eab162dac004eaf2a30296d72eed3d4ec78759ce
updated_at: 2026-04-10T00:00:00Z
---

# Say

The `` verb speaks the text specified back to the caller, enabling text-to-speech for any application.

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
      <td><code>voice</code></td>
      <td> Optional text-to-speech voice type. For premium text-to-speech use alice or prescribe a specific Amazon Polly voice in the form of Polly.VoiceId. If you want to use neural voice, use the following format: Polly.VoiceId-Neural. The ElevenLabs integration requires providing an API key that can stored in the secrets storage integration secrets documentation for more details. The voice can be specified in the following way: ElevenLabs.ModelId.VoiceId. For basic text-to-speech use man or woman. Only en-US language is supported in that case. </td>
      <td><code>alice</code>, <code>Polly.VoiceId</code>, <code>Polly.VoiceId-Neural</code>, <code>ElevenLabs.ModelId.VoiceId</code>, <code>man</code>, <code>woman</code></td>
      <td><code>man</code></td>
    </tr>

    <tr>
      <td><code>language</code></td>
      <td> ISO language type to be used if voice type alice is selected. If man or woman is selected, the language accent will always be en-US. This parameter is ignored when a specific Amazon Polly voice is used. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>loop</code></td>
      <td> The number of times to repeat the text. 0 means infinite. </td>
      <td><code>0</code> - <code>10</code></td>
      <td><code>1</code></td>
    </tr>

    <tr>
      <td><code>gender</code></td>
      <td> Specifies the gender of the voice. Only applicable when using Azure voices (Azure.\*). </td>
      <td><code>Male</code>, <code>Female</code></td>
      <td>-</td>
    </tr>

    <tr>
      <td><code>effect</code></td>
      <td> Applies an audio effect to the spoken text. Only applicable when using Azure voices (Azure.\*). </td>
      <td><code>eq\_telecomhp8k</code>, <code>eq\_car</code></td>
      <td>-</td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Say voice="alice">This is a premium Amazon Polly text-to-speech message!

```
