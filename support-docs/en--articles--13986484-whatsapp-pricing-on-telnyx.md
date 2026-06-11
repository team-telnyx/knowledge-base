---
source_url: https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx
scraped: 2026-06-11
---

WhatsApp Pricing on Telnyx | Telnyx Help Center

[Skip to main content](#main-content)

# WhatsApp Pricing on Telnyx

How WhatsApp conversation-based billing works on Telnyx, including categories and billing types.

Written by Telnyx Engineering

March 19, 2026

Table of contents

# Per-Message Billing

As of July 1, 2025, WhatsApp uses a per-message billing model for template messages. Each template message delivered is charged individually based on its category and the recipient's country. Non-template (free-form) messages sent within a customer service window are not charged.

# Message Categories and Rates

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

# Service Window

When a customer messages your business, a 24-hour service window opens. During this window, you can send free-form (non-template) replies at no charge. Template messages sent during this window are still billed per their category.

# How Billing Type is Determined

Telnyx determines the billing type from the template category and the destination country. The `billing_type` field appears in delivery status webhooks (DLRs) with one of these values:

* `whatsapp_marketing` — Marketing template message
* `whatsapp_utility` — Utility template message
* `whatsapp_authentication` — Authentication template, same country as WABA
* `whatsapp_authentication_international` — Authentication template, different country from WABA
* `whatsapp_service` — Non-template reply within service window (free)

# Free Entry Point Conversations

Messages that start from certain entry points have special pricing:

* Click-to-WhatsApp ads on Facebook or Instagram
* Facebook Page call-to-action buttons

Refer to [Meta's pricing documentation](https://developers.facebook.com/docs/whatsapp/pricing) for current free entry point details.

# Viewing Costs

You can track WhatsApp messaging costs in the Telnyx Portal under **Messaging → Message Detail Records**. Each record includes the `billing_type` field so you can see which category was billed.

# Related Resources

* [Send WhatsApp Messages (API Guide)](https://developers.telnyx.com/docs/messaging/whatsapp/send-messages)

---

Related Articles

[What is WhatsApp Business Platform?](https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform)[WhatsApp Message Types Explained](https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained)[WhatsApp 24-Hour Conversation Window](https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window)[How to Set Up WhatsApp on Telnyx](https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx)[WhatsApp FAQ](https://support.telnyx.com/en/articles/13986488-whatsapp-faq)

Did this answer your question?

😞😐😃

Table of contents
