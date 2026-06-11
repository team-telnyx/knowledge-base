---
source_url: https://support.telnyx.com/en/articles/13986488-whatsapp-faq
scraped: 2026-06-11
---

WhatsApp FAQ | Telnyx Help Center

[Skip to main content](#main-content)

# WhatsApp FAQ

Frequently asked questions about WhatsApp Business Platform on Telnyx.

Written by Telnyx Engineering

March 16, 2026

Table of contents

# General

## What phone number types can I use with WhatsApp?

You can use landline numbers, mobile numbers, or toll-free numbers. The number cannot be currently registered with the WhatsApp consumer app or WhatsApp Business App. If it is, you must delete that account first.

## Can I use the same number for SMS and WhatsApp?

Yes. Your Telnyx number can be used for both SMS/MMS and WhatsApp simultaneously.

## Which countries are supported?

WhatsApp Business Platform is available globally wherever WhatsApp operates. You can send messages to any WhatsApp user worldwide. Conversation rates vary by destination country.

## Do I need a Meta Business Manager account?

Yes. A Meta Business Manager account is required to create a WhatsApp Business Account (WABA). You'll connect it during the Embedded Signup flow.

# Messaging

## What is the maximum message size?

Text messages can be up to 4,096 bytes. Media captions are limited to 1,024 bytes. Header text is limited to 1,024 bytes.

## How many contacts can I send in one message?

You can include 1–257 contacts in a single contact card message.

## Can I send messages to non-WhatsApp users?

No. The recipient must have WhatsApp installed and an active account on the destination phone number.

## What interactive message types are supported?

Telnyx supports these interactive types: quick reply buttons, CTA URL buttons, list messages, location request messages, and carousel messages.

## Can I send bulk messages?

You can send messages programmatically at scale via the API. However, you are subject to Meta's messaging limit tiers (starting at 1,000 unique recipients per 24 hours for new WABAs). You must use approved templates for business-initiated conversations.

# Templates

## How long does template approval take?

Typically 24–48 hours, but it can take longer during high-volume periods. There is no way to expedite the review.

## How many templates can I have?

Meta allows up to 6,000 templates per WABA. In practice, keep your template library focused and well-organized.

## Can I edit an approved template?

You can edit certain aspects of approved templates (like header media type), but changes to the body or category require re-approval. In many cases, it's easier to create a new template.

# Billing

## Am I charged per message or per conversation?

Per conversation. When a conversation opens (either by you sending a template or by a customer messaging you), you're charged once for that conversation category. All messages within the next 24 hours are included.

## What are free entry point conversations?

Conversations initiated from Click-to-WhatsApp ads or Facebook Page buttons are free for the first 72 hours.

## How do I track WhatsApp costs?

Each delivery status webhook includes a `billing_type` field indicating the conversation category. You can also view costs in the Telnyx Portal under Message Detail Records.

# Technical

## What API endpoint do I use?

`POST /v2/messages/whatsapp` — for sending all WhatsApp message types (template, text, media, interactive, etc.).

## Do I need a messaging\_profile\_id?

No. For WhatsApp sends, the messaging profile is automatically resolved from the `from` phone number.

## What error code does WhatsApp use?

WhatsApp errors typically return error code `40008`, which is a catch-all covering template issues (pending, rejected, paused, disabled) and delivery failures. The response body contains additional details from the Meta API.

---

Related Articles

[What is WhatsApp Business Platform?](https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform)[WhatsApp Pricing on Telnyx](https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx)[How to Set Up WhatsApp on Telnyx](https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx)[WhatsApp Troubleshooting Guide](https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide)[Enabling WhatsApp Business Calling on Telnyx Numbers](https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers)

Did this answer your question?

😞😐😃

Table of contents
