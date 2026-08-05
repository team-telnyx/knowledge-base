---
title: Send WhatsApp Messages
summary: Send WhatsApp messages via the Telnyx API using `POST /v2/messages/whatsapp`.
  The same endpoint handles every message type — template, text, media, location,
  contacts, interactive, and reactions — with the `whatsapp_message.type` field selecting
  the payload shape. Templates are required to start conversations outside the 24-hour
  customer service window; text, media, and interactive messages are only allowed
  inside that window.
sources:
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
updated_at: 2026-08-05T13:59:07Z
---

# Send WhatsApp Messages

*Part 3 of 3 — see also: [Part 1](send-whatsapp-messages--part-1.md), [Part 2](send-whatsapp-messages--part-2.md)*

Send WhatsApp messages via the Telnyx API using `POST /v2/messages/whatsapp`. The same endpoint handles every message type — template, text, media, location, contacts, interactive, and reactions — with the `whatsapp_message.type` field selecting the payload shape. Templates are required to start conversations outside the 24-hour customer service window; text, media, and interactive messages are only allowed inside that window.

## Webhook Events

Configure webhooks on your messaging profile to receive real-time delivery status updates. Monitor these key events:

- `message.sent` — Message successfully submitted to WhatsApp
- `message.delivered` — Message delivered to recipient's device
- `message.read` — Recipient opened and read the message (when enabled by recipient)
- `message.failed` — Message delivery failed (with error details)
- `message.received` — Inbound message from a customer

Example webhook payload:

```json
{
  "data": {
    "event_type": "message.sent",
    "id": "msg_123abc",
    "occurred_at": "2023-01-01T12:00:00.000Z",
    "payload": {
      "id": "msg_123abc",
      "type": "whatsapp",
      "to": "+15557654321",
      "from": "+15551234567",
      "text": "Hello John! Welcome to our WhatsApp updates.",
      "direction": "outbound",
      "parts": 1,
      "tags": [],
      "messaging_profile_id": "your_messaging_profile_id",
      "billing_type": "whatsapp_marketing",
      "valid_until": "2023-01-01T12:30:00.000Z"
    }
  }
}
```

## Common Issues

### Template not approved

**Symptoms:** API returns a `40008` error indicating the template was not found or not approved.

**Solutions:**

- Verify template status in Portal under **Messaging → WhatsApp → Send Messages**
- Ensure template name matches exactly (case-sensitive)
- Wait for Meta's approval (typically 24-48 hours for first templates)
- Review Meta's template guidelines for approval requirements

### Phone number not verified

**Symptoms:** API returns a `40008` error indicating the sender phone number is not registered with WhatsApp.

**Solutions:**

- Complete phone number verification in the Telnyx Portal
- Ensure number is added to your WhatsApp Business Account
- Verify the number through Meta's verification process
- Check that the number hasn't been used with personal WhatsApp

### Outside 24-hour window

**Symptoms:** Free-form (session) message fails with a `40008` error. WhatsApp requires a template to initiate conversations outside the 24-hour window.

**Solutions:**

- Use approved message templates for outbound messaging
- Only send free-form messages within 24 hours of customer's last message
- Check conversation window status via webhook events
- Consider switching to template-based messaging for customer re-engagement

### Invalid recipient

**Symptoms:** Message status webhook returns `undeliverable` with Meta API error details in the response.

**Solutions:**

- Verify recipient has WhatsApp installed and active
- Ensure phone number format includes country code (+1…)
- Check that recipient hasn't blocked your business number
- Confirm recipient's WhatsApp account is not banned or restricted

## Next Steps

- [Quickstart: Send Your First WhatsApp Message](quickstart-send-your-first-whatsapp-message.md) — Send your first WhatsApp message end-to-end
- [Embedded Signup](embedded-signup.md) — Set up your WhatsApp Business Account and verify your number
- [Receiving Webhooks](receiving-webhooks.md) — Handle inbound messages and delivery status callbacks
