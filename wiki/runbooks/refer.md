---
title: Refer
summary: The `` verb in Telnyx allows you to transfer a phone call to another SIP infrastructure during a TeXML call.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/refer/index
    content_hash: b05a99c5e416679be6d5b8a6911e4079a0bdb19f23e21a2ac7b23380fad9b2ee
updated_at: 2026-04-10T00:00:00Z
---

# Refer

The `` verb in Telnyx allows you to transfer a phone call to another SIP infrastructure during a TeXML call. You can initiate it at any point during the call. When you use the `` verb, Telnyx will replace the original call with a new call to the external system you specify, effectively transferring the call to that system.

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
      <td> Optional URL where TeXML will make a request when the Refer verb ends, to retrieve a new set of TeXML instructions to continue the call flow. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>method</code></td>
      <td> HTTP request type used to retrieve the next set of instructions. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

        sip:john@example.com

```

## Expected callbacks

If `action` is set, a callback is sent when the `` verb finishes. See [Refer Status Callback](https://developers.telnyx.com/api-reference/callbacks/texml-refer-status) for the full payload reference.
