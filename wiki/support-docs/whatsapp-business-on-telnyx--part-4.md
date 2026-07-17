---
title: WhatsApp Business on Telnyx
summary: A comprehensive guide to using WhatsApp Business Platform on Telnyx, covering
  account setup via Embedded Signup, message types (template and free-form), the 24-hour
  conversation window, template creation and approval, per-message billing, WhatsApp
  Business Calling, troubleshooting, and frequently asked questions.
sources:
- url: https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform
- url: https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained
- url: https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window
- url: https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide
- url: https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx
- url: https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx
- url: https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates
- url: https://support.telnyx.com/en/articles/13986488-whatsapp-faq
- url: https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide
- url: https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers
- url: https://support.telnyx.com/en/collections/18868947-whatsapp-business
updated_at: 2026-07-17T09:09:49Z
---

# WhatsApp Business on Telnyx

*Part 4 of 7 — see also: [Part 1](whatsapp-business-on-telnyx--part-1.md), [Part 2](whatsapp-business-on-telnyx--part-2.md), [Part 3](whatsapp-business-on-telnyx--part-3.md), [Part 5](whatsapp-business-on-telnyx--part-5.md), [Part 6](whatsapp-business-on-telnyx--part-6.md), [Part 7](whatsapp-business-on-telnyx--part-7.md)*

A comprehensive guide to using WhatsApp Business Platform on Telnyx, covering account setup via Embedded Signup, message types (template and free-form), the 24-hour conversation window, template creation and approval, per-message billing, WhatsApp Business Calling, troubleshooting, and frequently asked questions.

## Pricing and Billing

### Per-Message Billing

As of July 1, 2025, WhatsApp uses a per-message billing model for template messages. Each template message delivered is charged individually based on its category and the recipient's country. Non-template (free-form) messages sent within a customer service window are not charged.

### Message Categories and Rates

Rates vary by message category and the recipient's country. The four categories are:

| Category | Sent By | Typical Use | Billed? |
| --- | --- | --- | --- |
| **Marketing** | Business (template) | Promotions, offers, product updates | Per message delivered |
| **Utility** | Business (template) | Order updates, receipts, account alerts | Per message delivered |
| **Authentication** | Business (template) | OTP, verification codes | Per message delivered |
| **Service** | Business (free-form reply) | Customer support, inquiries | Free within service window |

Marketing templates are typically the most expensive, followed by Utility, then Authentication.

Marketing and Authentication template messages are billed even when sent within an active customer service window. Only non-template (free-form) replies are free during the service window.

### Conversation Billing

Each conversation is billed once when it opens. The conversation type determines the rate:

| Conversation Type | How It Opens | Duration |
| --- | --- | --- |
| **Service** | Customer messages you, you reply with free-form | 24 hours from window open |
| **Marketing** | You send a Marketing template | 24 hours from template send |
| **Utility** | You send a Utility template | 24 hours from template send |
| **Authentication** | You send an Authentication template | 24 hours from template send |

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

Conversations initiated from Click-to-WhatsApp ads or Facebook Page buttons are free for the first 72 hours. Refer to [Meta's pricing documentation](https://developers.facebook.com/docs/whatsapp/pricing) for current free entry point details.

### Viewing Costs

You can track WhatsApp messaging costs in the Telnyx Portal under **Messaging → Message Detail Records**. Each record includes the `billing_type` field so you can see which category was billed.
