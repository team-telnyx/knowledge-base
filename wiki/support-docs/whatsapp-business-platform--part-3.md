---
title: WhatsApp Business Platform
summary: WhatsApp Business Platform is Meta's API-based solution for sending and receiving
  WhatsApp messages at scale. Telnyx integrates as an official Business Solution Provider
  (BSP), offering API infrastructure for messaging, template management, phone number
  registration, webhook delivery, and WhatsApp Business Calling — all through the
  Telnyx Portal and API.
sources:
- url: https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform
- url: https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained
- url: https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window
- url: https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide
- url: https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx
- url: https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx
- url: https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates
- url: https://support.telnyx.com/en/articles/13986487-how-to-configure-whatsapp-webhooks
- url: https://support.telnyx.com/en/articles/13986488-whatsapp-faq
- url: https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide
- url: https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers
- url: https://support.telnyx.com/en/collections/18868947-whatsapp-business
updated_at: 2026-06-11T11:36:03Z
---

# WhatsApp Business Platform

*Part 3 of 5 — see also: [Part 1](whatsapp-business-platform--part-1.md), [Part 2](whatsapp-business-platform--part-2.md), [Part 4](whatsapp-business-platform--part-4.md), [Part 5](whatsapp-business-platform--part-5.md)*

WhatsApp Business Platform is Meta's API-based solution for sending and receiving WhatsApp messages at scale. Telnyx integrates as an official Business Solution Provider (BSP), offering API infrastructure for messaging, template management, phone number registration, webhook delivery, and WhatsApp Business Calling — all through the Telnyx Portal and API.

## Sending and Receiving Messages

### Sending Messages

Use `POST /v2/messages/whatsapp` to send all WhatsApp message types (template, text, media, interactive, etc.). No `messaging_profile_id` is needed — the messaging profile is automatically resolved from the `from` phone number.

### Receiving Messages and Delivery Status via Webhooks

Configure webhook endpoints to receive real-time notifications when customers send you WhatsApp messages and when your outbound messages are delivered, read, or fail.

**Via the Telnyx Portal:** Go to **Messaging → WhatsApp**, select your WABA, navigate to the webhook configuration section, enter your webhook URL (must be HTTPS), and save.

**Via the API:** Use the WABA webhook configuration endpoint to set your webhook URL programmatically. You can also specify a `webhook_url` per message when sending.

**Inbound message webhooks** include: sender's phone number, message type, message content, timestamp, and message ID (for replying with context).

**Delivery status webhooks:**

| Status | Meaning |
|---|---|
| `sent` | Message accepted by WhatsApp |
| `delivered` | Message delivered to recipient's device |
| `read` | Recipient opened/read the message |
| `failed` | Message could not be delivered |

Delivery status webhooks include the `billing_type` field (e.g., `whatsapp_marketing`, `whatsapp_utility`, `whatsapp_service`) so you can track costs.

### Webhook Requirements

- **HTTPS** — Your endpoint must use HTTPS with a valid SSL certificate
- **200 response** — Return a 200 status code within 5 seconds to acknowledge receipt
- **Idempotency** — You may receive the same webhook multiple times; handle duplicates gracefully using the message ID

For development, tools like [ngrok](https://ngrok.com) or [Hookdeck](https://hookdeck.com) can expose a local endpoint to inspect incoming webhook payloads.

## Conversation Categories and Pricing

### Per-Message Billing

As of July 1, 2025, WhatsApp uses a per-message billing model for template messages. Each template message delivered is charged individually based on its category and the recipient's country. Non-template (free-form) messages sent within a customer service window are not charged.

| Category | Sent By | Typical Use | Billed? |
|---|---|---|---|
| **Marketing** | Business (template) | Promotions, offers, product updates | Per message delivered |
| **Utility** | Business (template) | Order updates, receipts, account alerts | Per message delivered |
| **Authentication** | Business (template) | OTP, verification codes | Per message delivered |
| **Service** | Business (free-form reply) | Customer support, inquiries | Free within service window |

Marketing templates are typically the most expensive, followed by Utility, then Authentication. **Marketing and Authentication template messages are billed even when sent within an active customer service window.** Only non-template (free-form) replies are free during the service window.

### Billing Type Determination

The `billing_type` field appears in delivery status webhooks (DLRs) with one of these values:

- `whatsapp_marketing` — Marketing template message
- `whatsapp_utility` — Utility template message
- `whatsapp_authentication` — Authentication template, same country as WABA
- `whatsapp_authentication_international` — Authentication template, different country from WABA
- `whatsapp_service` — Non-template reply within service window (free)

### Free Entry Point Conversations

Messages that start from certain entry points have special pricing:

- Click-to-WhatsApp ads on Facebook or Instagram
- Facebook Page call-to-action buttons

Conversations initiated from these entry points are free for the first 72 hours. Refer to [Meta's pricing documentation](https://developers.facebook.com/docs/whatsapp/pricing) for current details.

### Tracking Costs

You can track WhatsApp messaging costs in the Telnyx Portal under **Messaging → Message Detail Records**. Each record includes the `billing_type` field so you can see which category was billed.
