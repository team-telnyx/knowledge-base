---
title: Receiving Webhooks for Telnyx Verify
summary: You can choose to be notified about events on your send verifications by configuring webhooks on your verify profile.
sources:
  - url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks/index
    content_hash: 0ba6b8f2e432c7a90a783e43c889df72a5624428e7d9aabb325ad3d77e54f9cb
updated_at: 2026-04-10T00:00:00Z
---

# Receiving Webhooks for Telnyx Verify

You can choose to be notified about events on your send verifications by configuring webhooks on your verify profile.

***

## Verify delivery status updates

The Telnyx Verify Service will attempt to notify you about the following delivery events for the send verification request:

* verify.sent
* verify.failed
* verify.delivered

#### Delivery status Payload

Here is an example of a webhook event where a delivery receipt is returned to the sender after sending a verification:

```json theme={null}
{
  "data": {
    "event_type": "verify.delivered",
    "id": "3bb6321b-abd5-4d60-8cf8-1e6026bb1c41",
    "occurred_at": "2025-10-08T17:16:09.602+00:00",
    "payload": {
      "created_at": "2025-10-08T17:16:08.436941",
      "custom_code": "25565",
      "delivery_status": "delivered",
      "extension": null,
      "failed_attempts": 0,
      "id": "010d9dee-d86d-47d0-8d6c-20c0f95a79ec",
      "mccmnc": null,
      "phone_number": "+13125000000",
      "profile_id": "49000192-1bdb-c56f-3de7-e008ef6da16b",
      "record_type": "verification",
      "status": "pending",
      "timeout_secs": null,
      "type": "sms",
      "updated_at": "2025-10-08T17:16:09.592765"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://webhook.site/af3a92e7-e150-442c-9fe6-61658ce26b1a"
  }
}
```

#### Delivery statuses

<table>
  <tbody>
    <tr>
      <td>Delivery Status</td>
      <td>Description</td>
    </tr>

    <tr>
      <td>sent</td>
      <td>The verification has been sent to the upstream provider.</td>
    </tr>

    <tr>
      <td>delivered</td>
      <td>The upstream provider has confirmed delivery of the verification.</td>
    </tr>

    <tr>
      <td>sending\_failed</td>
      <td>Telnyx has failed to send the verification to the upstream provider. Please reach out to our support if you have received this status.</td>
    </tr>

    <tr>
      <td>delivery\_failed</td>
      <td>The upstream provider has failed to send the verification to the receiver. Please reach out to our support if you have received this status.</td>
    </tr>

    <tr>
      <td>delivery\_unconfirmed</td>
      <td>There is no indication whether or not the verification has reached the receiver. Please reach out to our support if you have received this status</td>
    </tr>
  </tbody>
</table>

<hr />

## Real-time verification status updates

Telnyx Verify now supports webhooks for instant verification status notifications, eliminating the need to poll the API for verification completion.

### Benefits

* **Eliminates polling** - No need to repeatedly check verification status through API calls.
* **Event-driven workflow** - React immediately to verification state changes in real-time.
* **Faster user experience** - Process verification completions instantly without delays.
* **Improved efficiency** - Reduces server load and unnecessary API requests.

Configure webhooks on your Verify profile to receive real-time updates when verifications complete. For specific webhook event types, payload structures, and configuration details, refer to the [Telnyx API documentation](https://developers.telnyx.com/api-reference/profiles/list-messaging-profiles#list-messaging-profiles) or contact Telnyx support.

<hr />

### Telnyx Webhook IPs

If you use an ACL or Firewall on your network, make sure you whitelist the following subnet(s):

<table>
  <tbody>
    <tr>
      <td />
    </tr>

    <tr>
      <td><i>192.76.120.192/27</i></td>
    </tr>
  </tbody>
</table>


## Related Pages

- [Receiving Webhooks for Messaging](../runbooks/receiving-webhooks-for-messaging.md)
- [Receiving Webhooks for Programmable Voice](../runbooks/receiving-webhooks-for-programmable-voice.md)
- [Receiving Webhooks for Programmable Fax](../runbooks/receiving-webhooks-for-programmable-fax.md)
- [Quickstart for Telnyx Verify](../tutorial/quickstart-for-telnyx-verify.md)
- [Receiving RCS Webhooks](../runbooks/receiving-rcs-webhooks.md)
