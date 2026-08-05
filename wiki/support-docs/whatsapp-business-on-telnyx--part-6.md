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

*Part 6 of 6 — see also: [Part 1](whatsapp-business-on-telnyx--part-1.md), [Part 2](whatsapp-business-on-telnyx--part-2.md), [Part 3](whatsapp-business-on-telnyx--part-3.md), [Part 4](whatsapp-business-on-telnyx--part-4.md), [Part 5](whatsapp-business-on-telnyx--part-5.md)*

A consolidated reference for using the WhatsApp Business Platform through Telnyx as a Meta Business Solution Provider. It covers account setup, message types and templates, conversation-based billing, webhooks, voice calling, troubleshooting, and frequently asked questions.

## Frequently Asked Questions

### General

- **What phone number types can I use with WhatsApp?** You can use landline numbers, mobile numbers, or toll-free numbers. The number cannot be currently registered with the WhatsApp consumer app or WhatsApp Business App. If it is, you must delete that account first.
- **Can I use the same number for SMS and WhatsApp?** Yes. Your Telnyx number can be used for both SMS/MMS and WhatsApp simultaneously.
- **Which countries are supported?** WhatsApp Business Platform is available globally wherever WhatsApp operates. You can send messages to any WhatsApp user worldwide. Conversation rates vary by destination country.
- **Do I need a Meta Business Manager account?** Yes. A Meta Business Manager account is required to create a WhatsApp Business Account (WABA). You'll connect it during the Embedded Signup flow.

### Messaging

- **What is the maximum message size?** Text messages can be up to 4,096 bytes. Media captions are limited to 1,024 bytes. Header text is limited to 1,024 bytes.
- **How many contacts can I send in one message?** You can include 1–257 contacts in a single contact card message.
- **Can I send messages to non-WhatsApp users?** No. The recipient must have WhatsApp installed and an active account on the destination phone number.
- **What interactive message types are supported?** Telnyx supports quick reply buttons, CTA URL buttons, list messages, location request messages, and carousel messages.
- **Can I send bulk messages?** You can send messages programmatically at scale via the API. However, you are subject to Meta's messaging limit tiers (starting at 1,000 unique recipients per 24 hours for new WABAs). You must use approved templates for business-initiated conversations.

### Templates

- **How long does template approval take?** Typically 24–48 hours, but it can take longer during high-volume periods. There is no way to expedite the review.
- **How many templates can I have?** Meta allows up to 6,000 templates per WABA. In practice, keep your template library focused and well-organized.
- **Can I edit an approved template?** You can edit certain aspects of approved templates (like header media type), but changes to the body or category require re-approval. In many cases, it's easier to create a new template.

### Billing

- **Am I charged per message or per conversation?** Per conversation. When a conversation opens (either by you sending a template or by a customer messaging you), you're charged once for that conversation category. All messages within the next 24 hours are included.
- **What are free entry point conversations?** Conversations initiated from Click-to-WhatsApp ads or Facebook Page buttons are free for the first 72 hours.
- **How do I track WhatsApp costs?** Each delivery status webhook includes a `billing_type` field indicating the conversation category. You can also view costs in the Telnyx Portal under Message Detail Records.

### Technical

- **What API endpoint do I use?** `POST /v2/messages/whatsapp` — for sending all WhatsApp message types (template, text, media, interactive, etc.).
- **Do I need a `messaging_profile_id`?** No. For WhatsApp sends, the messaging profile is automatically resolved from the `from` phone number.
- **What error code does WhatsApp use?** WhatsApp errors typically return error code `40008`, which is a catch-all covering template issues (pending, rejected, paused, disabled) and delivery failures. The response body contains additional details from the Meta API.

## Related Resources

- [What is WhatsApp Business Platform?](what-is-whatsapp-business-platform.md)
- [WhatsApp Message Types Explained](whatsapp-message-types-explained.md)
- [WhatsApp 24-Hour Conversation Window](whatsapp-24-hour-conversation-window.md)
- [WhatsApp Message Templates Guide](whatsapp-message-templates-guide.md)
- [WhatsApp Pricing on Telnyx](whatsapp-pricing-on-telnyx.md)
- [How to Set Up WhatsApp on Telnyx](how-to-set-up-whatsapp-on-telnyx.md)
- [How to Create WhatsApp Message Templates](how-to-create-whatsapp-message-templates.md)
- [How to Configure WhatsApp Webhooks](how-to-configure-whatsapp-webhooks.md)
- [WhatsApp FAQ](whatsapp-faq.md)
- [WhatsApp Troubleshooting Guide](whatsapp-troubleshooting-guide.md)
- [Enabling WhatsApp Business Calling on Telnyx Numbers](enabling-whatsapp-business-calling-on-telnyx-numbers.md)
- [WhatsApp Quickstart Guide](https://developers.telnyx.com/docs/messaging/whatsapp/quickstart)
- [Embedded Signup Guide](https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup)
- [Send WhatsApp Messages](https://developers.telnyx.com/docs/messaging/whatsapp/send-messages)
- [Receiving Webhooks Guide](https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks)
- [Meta's pricing documentation](https://developers.facebook.com/docs/whatsapp/pricing)
- [Meta call permission request flow](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling/user-call-permissions#call-permission-request-flow-and-sample-messages)
- [Meta calling permissions](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling/user-call-permissions)
- [Meta call settings](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling/call-settings#configure-update-business-phone-number-calling-settings)
