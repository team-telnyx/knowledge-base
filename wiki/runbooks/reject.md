---
title: Reject
summary: The `` verb rejects a call to your Telnyx number.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/reject/index
    content_hash: 224e202aa05893fc19effa570410b84b4bce5c8c636f35ec6a0dc0d841981974
updated_at: 2026-04-10T00:00:00Z
---

# Reject

The `` verb rejects a call to your Telnyx number. It is effectively an exit statement from the current document, as there is no way to return to any instructions listed after the `` verb. If placed as the very first verb in an incoming call, `` will prevent the call from being answered and will incur no cost. If placed elsewhere in the call, the call will hang up but will be charged up to that point.<br /><br />You can't nest any verbs within `` and you can't nest `` in any other verbs.

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
      <td><code>reason</code></td>
      <td> The tone to play to indicate the reason the call was rejected. </td>
      <td><code>rejected</code>, <code>busy</code></td>
      <td><code>rejected</code></td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Reject reason="busy"/>

```
