---
title: Siprec
summary: The `` instruction starts the SIPREC session on the given call.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/siprec/index
    content_hash: 7dcb843cb4ce51c7a7f7773aece738b4b47b94deff526142c2ef981a7bf231fb
updated_at: 2026-04-10T00:00:00Z
---

# Siprec

The `` instruction starts the SIPREC session on the given call.

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
      <td><code>connectorName</code></td>
      <td> Specifies which pre-configured external connector shall be used for this request. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>statusCallback</code></td>
      <td> A URL for Telnyx to send webhook requests to on each event related to siprec session. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>statusCallbackMethod</code></td>
      <td> HTTP request type used for statusCallback. </td>
      <td><code>GET</code>, <code>POST</code></td>
      <td><code>POST</code></td>
    </tr>

    <tr>
      <td><code>track</code></td>
      <td> Specifies which track should be forwarded to SRS. </td>
      <td><code>inbound\_track</code>, <code>outbound\_track</code>, <code>both\_tracks</code></td>
      <td><code>both\_tracks</code></td>
    </tr>

    <tr>
      <td><code>name</code></td>
      <td> Name of the SIPREC session. It can be used to stop the session. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>includeMetadataCustomHeaders</code></td>
      <td> Controls whether custom parameters are added as metadata, if false, they are added to sip headers. </td>

      <td />

      <td><code>false</code></td>
    </tr>

    <tr>
      <td><code>secure</code></td>
      <td> Controls whether to encrypt media sent to your SRS using SRTP and TLS. When set you need to configure SRS port in your connector to 5061. </td>

      <td />

      <td><code>false</code></td>
    </tr>

    <tr>
      <td><code>sessionTimeoutSecs</code></td>
      <td> Sets <code>Session-Expires</code> header to the INVITE. A reinvite is sent every half the value set. Useful for session keep alive. Minimum value is 90, set to 0 to disable. </td>
      <td><code>90</code> - <code>14440</code></td>
      <td><code>1800</code></td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Siprec name="siprec_session" track="both_tracks" connectorName="my-connector" statusCallback="https://example.com/siprec_callback" />

```

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Siprec name="siprec_session" />

```

## Expected callbacks

If `statusCallback` is set, SIPREC status callbacks are sent for the following events:

* `siprec-started` — SIPREC session has started
* `siprec-stopped` — SIPREC session has stopped
* `siprec-failed` — SIPREC session failed to start

See [SIPREC Callback](https://developers.telnyx.com/api-reference/callbacks/texml-siprec) for the full payload reference.


## Related Pages

- [SIPREC](../runbooks/siprec-2.md)
