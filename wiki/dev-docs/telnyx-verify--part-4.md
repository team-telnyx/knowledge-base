---
title: Telnyx Verify
summary: The Telnyx Verify API enables robust two-factor authentication and phone-number
  verification using carrier-grade voice and messaging. This page consolidates the
  Verify quickstart, custom templates, DTMF confirmation, webhooks, security best
  practices, and rate-limiting/fraud-prevention guidance into a single reference covering
  SMS, call, flashcall, and DTMF confirm verification methods, profile configuration,
  code verification, and production hardening.
sources:
- url: https://developers.telnyx.com/docs/identity/number-lookup/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/custom-templates
- url: https://developers.telnyx.com/docs/identity/verify/dtmf-confirm
- url: https://developers.telnyx.com/docs/identity/verify/index
- url: https://developers.telnyx.com/docs/identity/verify/quickstart/index
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
updated_at: 2026-07-17T09:13:37Z
---

# Telnyx Verify

*Part 4 of 6 — see also: [Part 1](telnyx-verify--part-1.md), [Part 2](telnyx-verify--part-2.md), [Part 3](telnyx-verify--part-3.md), [Part 5](telnyx-verify--part-5.md), [Part 6](telnyx-verify--part-6.md)*

The Telnyx Verify API enables robust two-factor authentication and phone-number verification using carrier-grade voice and messaging. This page consolidates the Verify quickstart, custom templates, DTMF confirmation, webhooks, security best practices, and rate-limiting/fraud-prevention guidance into a single reference covering SMS, call, flashcall, and DTMF confirm verification methods, profile configuration, code verification, and production hardening.

## Webhooks

Telnyx Verify supports webhooks to receive instant notifications when users complete verification, eliminating the need for polling. This enables event-driven workflows for faster user experiences.

### Delivery status updates

The Telnyx Verify Service will attempt to notify you about the following delivery events for the send verification request:

- `verify.sent`
- `verify.failed`
- `verify.delivered`

Example webhook payload:

```
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

| Delivery Status | Description |
| --- | --- |
| `sent` | The verification has been sent to the upstream provider. |
| `delivered` | The upstream provider has confirmed delivery of the verification. |
| `sending_failed` | Telnyx has failed to send the verification to the upstream provider. Contact support if you receive this status. |
| `delivery_failed` | The upstream provider has failed to send the verification to the receiver. Contact support if you receive this status. |
| `delivery_unconfirmed` | There is no indication whether or not the verification has reached the receiver. Contact support if you receive this status. |

### Real-time verification status updates

Telnyx Verify supports webhooks for instant verification status notifications, eliminating the need to poll the API for verification completion.

**Benefits:**
- **Eliminates polling** — No need to repeatedly check verification status through API calls.
- **Event-driven workflow** — React immediately to verification state changes in real-time.
- **Faster user experience** — Process verification completions instantly without delays.
- **Improved efficiency** — Reduces server load and unnecessary API requests.

Configure webhooks on your Verify profile to receive real-time updates when verifications complete. For specific webhook event types, payload structures, and configuration details, refer to the [Telnyx API documentation](https://developers.telnyx.com/api-reference/profiles/list-messaging-profiles#list-messaging-profiles) or contact Telnyx support.

#### DTMF webhook payloads

For DTMF confirmations, verification completes on the call — no verify endpoint call is needed. Receive the outcome via webhooks.

Accepted (digit `1` pressed):

```
{
  "data": {
    "event_type": "verification.complete",
    "payload": {
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "phone_number": "+13035551234",
      "status": "accepted",
      "type": "dtmf_confirm",
      "verify_profile_id": "YOUR_PROFILE_ID"
    }
  }
}
```

Failed (wrong digit, timeout, or call failure):

```
{
  "data": {
    "event_type": "verification.complete",
    "payload": {
      "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "phone_number": "+13035551234",
      "status": "invalid",
      "type": "dtmf_confirm",
      "verify_profile_id": "YOUR_PROFILE_ID"
    }
  }
}
```

As a polling alternative, you can fetch the verification status directly:

```
curl https://api.telnyx.com/v2/verifications/{verification_id} \
  -H "Authorization: Bearer $TELNYX_API_KEY"
```

### Telnyx webhook IPs

If you use an ACL or firewall on your network, make sure you whitelist the following subnet:

- `192.76.120.192/27`
