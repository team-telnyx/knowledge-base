---
title: Suppression
summary: The `` instruction starts noise suppression on the call to improve audio quality.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/suppression/index
    content_hash: 3316cc0af8b5af865a1c60e0eade49b0e5cac3bd6f7501385d91cf8fef1820ca
updated_at: 2026-04-10T00:00:00Z
---

# Suppression

The `` instruction starts noise suppression on the call to improve audio quality.

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
      <td><code>direction</code></td>
      <td> Specifies which side of the audio shall be denoised. </td>
      <td><code>inbound</code>, <code>outbound</code>, <code>both</code></td>
      <td><code>inbound</code></td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Suppression direction="both" />

```


## Related Pages

- [Noise Suppression](../runbooks/noise-suppression.md)
