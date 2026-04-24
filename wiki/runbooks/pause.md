---
title: Pause
summary: The `` verb waits silently for a specified number of seconds or one second by default.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/pause/index
    content_hash: 98acafdb394351ae3ae33647048a42af061ab4aba65f2abf0cb071a804b5d3cf
updated_at: 2026-04-10T00:00:00Z
---

# Pause

The `` verb waits silently for a specified number of seconds or one second by default. No nouns can be nested within ``, and a self-closing tag must be used.

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
      <td><code>length</code></td>
      <td> Seconds to pause </td>
      <td><code>1</code> - <code>180</code></td>
      <td><code>1</code></td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Pause length="5"/>

```
