---
title: Redirect
summary: The `` verb transfers control of a call to the TeXML document to another TeXML application.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/redirect/index
    content_hash: 73ebc53f4a727fe4ba373f61ee3847800b6b3ffb27858ee2bd93e708f48759f0
updated_at: 2026-04-10T00:00:00Z
---

# Redirect

The `` verb transfers control of a call to the TeXML document to another TeXML application. This is useful to create a tree structure of TeXML files for different applications. No nouns can be nested within ``

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
      <td><code>method</code></td>
      <td> The type of requested used `` URL. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Redirect method="POST">https://example.com/next-instructions

```
