---
title: Verify Security, Rate Limiting, and Webhooks
summary: 'Operational guidance for protecting Telnyx Verify integrations: layered
  rate limiting, geo-fencing, anomaly detection, cost controls, incident response,
  code and channel security, and webhook handling for delivery and verification status
  updates.'
sources:
- url: https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention
- url: https://developers.telnyx.com/docs/identity/verify/receiving-webhooks
- url: https://developers.telnyx.com/docs/identity/verify/security-best-practices
updated_at: 2026-08-05T13:44:10Z
---

# Verify Security, Rate Limiting, and Webhooks

*Part 5 of 5 — see also: [Part 1](verify-security-rate-limiting-and-webhooks--part-1.md), [Part 2](verify-security-rate-limiting-and-webhooks--part-2.md), [Part 3](verify-security-rate-limiting-and-webhooks--part-3.md), [Part 4](verify-security-rate-limiting-and-webhooks--part-4.md)*

Operational guidance for protecting Telnyx Verify integrations: layered rate limiting, geo-fencing, anomaly detection, cost controls, incident response, code and channel security, and webhook handling for delivery and verification status updates.

## Receiving webhooks

You can choose to be notified about events on your send verifications by configuring webhooks on your verify profile.

### Verify delivery status updates

The Telnyx Verify Service will attempt to notify you about the following delivery events for the send verification request:

- `verify.sent`
- `verify.failed`
- `verify.delivered`

#### Delivery status payload

Here is an example of a webhook event where a delivery receipt is returned to the sender after sending a verification:

```json
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
| `sending_failed` | Telnyx has failed to send the verification to the upstream provider. Please reach out to support if you receive this status. |
| `delivery_failed` | The upstream provider has failed to send the verification to the receiver. Please reach out to support if you receive this status. |
| `delivery_unconfirmed` | There is no indication whether or not the verification has reached the receiver. Please reach out to support if you receive this status. |

### Real-time verification status updates

Telnyx Verify supports webhooks for instant verification status notifications, eliminating the need to poll the API for verification completion.

**Benefits:**

- **Eliminates polling** — No need to repeatedly check verification status through API calls.
- **Event-driven workflow** — React immediately to verification state changes in real-time.
- **Faster user experience** — Process verification completions instantly without delays.
- **Improved efficiency** — Reduces server load and unnecessary API requests.

Configure webhooks on your Verify profile to receive real-time updates when verifications complete. For specific webhook event types, payload structures, and configuration details, refer to the [Telnyx API documentation](https://developers.telnyx.com/api-reference/profiles/list-messaging-profiles#list-messaging-profiles) or contact Telnyx support.

### Webhook security for Verify

Secure your verification webhook endpoint to prevent spoofed delivery notifications:

1. **Allowlist Telnyx IPs** — Only accept webhooks from `192.76.120.192/27`.
2. **Use HTTPS** — Never use plain HTTP for webhook endpoints.
3. **Validate payload structure** — Check for expected fields before processing.
4. **Don't trust client-side status** — Always verify through webhooks or API, never trust client-reported verification status.

```javascript
import { createServer } from 'http';
import { networkInterfaces } from 'os';

const TELNYX_WEBHOOK_CIDR = '192.76.120.192/27';

function isFromTelnyx(ip) {
  // In production, use a proper CIDR matching library
  const parts = ip.split('.').map(Number);
  return parts[0] === 192 && parts[1] === 76 &&
         parts[2] === 120 && parts[3] >= 192 && parts[3] <= 223;
}

app.post('/webhooks/verify', (req, res) => {
  const clientIp = req.headers['x-forwarded-for']?.split(',')[0] || req.ip;

  if (!isFromTelnyx(clientIp)) {
    console.warn(`Rejected webhook from unauthorized IP: ${clientIp}`);
    return res.sendStatus(403);
  }

  // Process webhook
  const event = req.body.data;
  if (event.event_type === 'verify.delivered') {
    console.log(`Verification delivered to ${event.payload.phone_number}`);
  }

  res.sendStatus(200);
});
```

```python
import ipaddress
from flask import Flask, request, jsonify

TELNYX_WEBHOOK_SUBNET = ipaddress.ip_network("192.76.120.192/27")

@app.route("/webhooks/verify", methods=["POST"])
def handle_verify_webhook():
    client_ip = ipaddress.ip_address(
        request.headers.get("X-Forwarded-For", request.remote_addr).split(",")[0].strip()
    )

    if client_ip not in TELNYX_WEBHOOK_SUBNET:
        return jsonify(error="Forbidden"), 403

    event = request.json["data"]
    if event["event_type"] == "verify.delivered":
        print(f"Verification delivered to {event['payload']['phone_number']}")

    return jsonify(success=True), 200
```

### Telnyx webhook IPs

If you use an ACL or firewall on your network, make sure you whitelist the following subnet:

- `192.76.120.192/27`

## Security checklist

Use this checklist when implementing Telnyx Verify in production.

**Rate limiting**

- Per-phone-number rate limit (3/10min)
- Per-IP rate limit (10/hour)
- Per-account/session rate limit
- Global volume monitoring and alerting

**Fraud prevention**

- Country allowlist configured on Verify profile
- CAPTCHA before verification trigger
- Authentication required before sending verification
- SMS pumping detection (sequential numbers, country spikes)

**Code security**

- Appropriate code length (5-6 digits)
- Short timeout (300 seconds or less)
- Max failed attempts lockout (5 attempts)
- Consistent responses (no number enumeration)

**Infrastructure**

- HTTPS webhook endpoints
- Telnyx IP allowlisting for webhooks
- Server-side verification only (never trust client)
- Logging and monitoring for anomalies

## Next steps

- [Verify Quickstart](verify-quickstart.md) — Set up your first verification flow
- [Custom Templates](custom-templates.md) — Brand your verification messages
- [Verify Webhooks](verify-webhooks.md) — Receive real-time verification status updates
- [Rate Limiting and Fraud Prevention for Verify](rate-limiting-and-fraud-prevention-for-verify.md) — Advanced fraud prevention strategies
