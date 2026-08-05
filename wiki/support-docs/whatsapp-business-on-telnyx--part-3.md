---
title: WhatsApp Business on Telnyx
summary: A consolidated reference for using the WhatsApp Business Platform through
  Telnyx as a Meta Business Solution Provider. It covers account setup, message types
  and templates, conversation-based billing, webhooks, voice calling, troubleshooting,
  and frequently asked questions.
sources:
- url: https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform
- url: https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained
- url: https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide
- url: https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx
- url: https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx
- url: https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates
- url: https://support.telnyx.com/en/articles/13986487-how-to-configure-whatsapp-webhooks
- url: https://support.telnyx.com/en/articles/13986488-whatsapp-faq
- url: https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide
- url: https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers
- url: https://support.telnyx.com/en/collections/18868947-whatsapp-business
updated_at: 2026-08-05T13:34:13Z
---

# WhatsApp Business on Telnyx

*Part 3 of 6 — see also: [Part 1](whatsapp-business-on-telnyx--part-1.md), [Part 2](whatsapp-business-on-telnyx--part-2.md), [Part 4](whatsapp-business-on-telnyx--part-4.md), [Part 5](whatsapp-business-on-telnyx--part-5.md), [Part 6](whatsapp-business-on-telnyx--part-6.md)*

A consolidated reference for using the WhatsApp Business Platform through Telnyx as a Meta Business Solution Provider. It covers account setup, message types and templates, conversation-based billing, webhooks, voice calling, troubleshooting, and frequently asked questions.

## Conversation Window and Billing

### Per-Message Billing

As of July 1, 2025, WhatsApp uses a per-message billing model for template messages. Each template message delivered is charged individually based on its category and the recipient's country. Non-template (free-form) messages sent within a customer service window are not charged.

### Message Categories and Rates

Rates vary by message category and the recipient's country:

| Category | Sent By | Typical Use | Billed? |
| --- | --- | --- | --- |
| **Marketing** | Business (template) | Promotions, offers, product updates | Per message delivered |
| **Utility** | Business (template) | Order updates, receipts, account alerts | Per message delivered |
| **Authentication** | Business (template) | OTP, verification codes | Per message delivered |
| **Service** | Business (free-form reply) | Customer support, inquiries | Free within service window |

Marketing templates are typically the most expensive, followed by Utility, then Authentication. Marketing and Authentication template messages are billed even when sent within an active customer service window — only non-template (free-form) replies are free during the service window.

### Service Window

When a customer messages your business, a 24-hour service window opens. During this window, you can send free-form (non-template) replies at no charge. Template messages sent during this window are still billed per their category.

### How Billing Type is Determined

Telnyx determines the billing type from the template category and the destination country. The `billing_type` field appears in delivery status webhooks (DLRs) with one of these values:

- `whatsapp_marketing` — Marketing template message
- `whatsapp_utility` — Utility template message
- `whatsapp_authentication` — Authentication template, same country as WABA
- `whatsapp_authentication_international` — Authentication template, different country from WABA
- `whatsapp_service` — Non-template reply within service window (free)

### Free Entry Point Conversations

Messages that start from certain entry points have special pricing:

- Click-to-WhatsApp ads on Facebook or Instagram
- Facebook Page call-to-action buttons

Refer to [Meta's pricing documentation](https://developers.facebook.com/docs/whatsapp/pricing) for current free entry point details. Conversations initiated from Click-to-WhatsApp ads or Facebook Page buttons are free for the first 72 hours.

### Viewing Costs

You can track WhatsApp messaging costs in the Telnyx Portal under **Messaging → Message Detail Records**. Each record includes the `billing_type` field so you can see which category was billed.

## Webhooks

### Setting Up Webhooks

Webhooks let you receive real-time notifications when customers send you WhatsApp messages and when your outbound messages are delivered, read, or fail. Configure your webhook URL through the WABA webhook settings in the Telnyx API or Portal.

Via the Telnyx Portal:

1. Go to **Messaging → WhatsApp**
2. Select your WhatsApp Business Account
3. Navigate to the webhook configuration section
4. Enter your webhook URL (must be HTTPS)
5. Save the configuration

Via the API, use the WABA webhook configuration endpoint to set your webhook URL programmatically. You can also specify a `webhook_url` per message when sending via `POST /v2/messages/whatsapp`.

### Webhook Events

**Inbound Messages** — When a customer sends you a message, you receive a webhook with the message content. The payload includes:

- Sender's phone number
- Message type (text, image, video, document, audio, location, contacts, interactive reply)
- Message content (text body, media URL, location coordinates, etc.)
- Timestamp
- Message ID (for replying with context)

**Delivery Status Updates** — For each outbound message, you receive status webhooks as the message progresses:

| Status | Meaning |
| --- | --- |
| `sent` | Message accepted by WhatsApp |
| `delivered` | Message delivered to recipient's device |
| `read` | Recipient opened/read the message |
| `failed` | Message could not be delivered |

Delivery status webhooks include the `billing_type` field (e.g., `whatsapp_marketing`, `whatsapp_utility`, `whatsapp_service`) so you can track costs.

### Webhook Requirements

- **HTTPS** — Your endpoint must use HTTPS with a valid SSL certificate
- **200 response** — Return a 200 status code within 5 seconds to acknowledge receipt
- **Idempotency** — You may receive the same webhook multiple times; handle duplicates gracefully using the message ID

### Testing Webhooks

For development, you can use tools like [ngrok](https://ngrok.com) or [Hookdeck](https://hookdeck.com) to expose a local endpoint to the internet and inspect incoming webhook payloads.
