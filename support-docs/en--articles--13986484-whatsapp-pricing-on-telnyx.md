---
source_url: https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx
title: "WhatsApp Pricing on Telnyx"
description: "How WhatsApp conversation-based billing works on Telnyx, including categories and billing types. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 1f023ad9a43a9da1b49fbc59c69cb007328b5a4a5dfe7a4fcbc3bbd483de26cf
---







# WhatsApp Pricing on Telnyx

How WhatsApp conversation-based billing works on Telnyx, including categories and billing types. See Telnyx guidance and requirements.




## Per-Message Billing

As of July 1, 2025, WhatsApp uses a per-message billing model for template messages. Each template message delivered is charged individually based on its category and the recipient's country. Non-template (free-form) messages sent within a customer service window are not charged.

## Message Categories and Rates

Rates vary by message category and the recipient's country. The four categories are:

|  |  |  |  |
| --- | --- | --- | --- |
| Category | Sent By | Typical Use | Billed? |
| **Marketing** | Business (template) | Promotions, offers, product updates | Per message delivered |
| **Utility** | Business (template) | Order updates, receipts, account alerts | Per message delivered |
| **Authentication** | Business (template) | OTP, verification codes | Per message delivered |
| **Service** | Business (free-form reply) | Customer support, inquiries | Free within service window |

Marketing templates are typically the most expensive, followed by Utility, then Authentication.

**Important:** Marketing and Authentication template messages are billed even when sent within an active customer service window. Only non-template (free-form) replies are free during the service window.

## Service Window

When a customer messages your business, a 24-hour service window opens. During this window, you can send free-form (non-template) replies at no charge. Template messages sent during this window are still billed per their category.

## How Billing Type is Determined

Telnyx determines the billing type from the template category and the destination country. The `billing_type` field appears in delivery status webhooks (DLRs) with one of these values:

* `whatsapp_marketing` — Marketing template message
* `whatsapp_utility` — Utility template message
* `whatsapp_authentication` — Authentication template, same country as WABA
* `whatsapp_authentication_international` — Authentication template, different country from WABA
* `whatsapp_service` — Non-template reply within service window (free)

## Free Entry Point Conversations

Messages that start from certain entry points have special pricing:

* Click-to-WhatsApp ads on Facebook or Instagram
* Facebook Page call-to-action buttons

Refer to [Meta's pricing documentation](https://developers.facebook.com/docs/whatsapp/pricing) for current free entry point details.

## Viewing Costs

You can track WhatsApp messaging costs in the Telnyx Portal under **Messaging → Message Detail Records**. Each record includes the `billing_type` field so you can see which category was billed.

## Related Resources

* [Send WhatsApp Messages (API Guide)](https://developers.telnyx.com/docs/messaging/whatsapp/send-messages)
