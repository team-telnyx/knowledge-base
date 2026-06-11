---
title: WhatsApp Business Platform
summary: WhatsApp Business Platform is Meta's API-based solution for sending and receiving
  WhatsApp messages at scale. Telnyx integrates as an official Business Solution Provider
  (BSP), offering API infrastructure for messaging, template management, phone number
  registration, webhook delivery, and WhatsApp Business Calling — all through the
  Telnyx Portal and API.
sources:
- url: https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform
  content_hash: e0dfd5a11bbda9ff91f7df2855b9014ff72d33baca35f781d78b0dd85ee3e9bb
- url: https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained
  content_hash: b84d28529808c576a61aeada7084c8b65d5f9d1d15a70b1c8d12042e741b10f8
- url: https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window
  content_hash: 2fe960b316229561d9e5c4d5e72ed3e97453f4146e10647d69e5a910dd51a413
- url: https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide
  content_hash: 634a8860642b2ab4a646a4abc5e096ac2d02e3e3e9096a061bc789c933edbc28
- url: https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx
  content_hash: c5c2d8afa84fa2f3c8ffc41d130ad99378188500be16a63f43d53f87f776535c
- url: https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx
  content_hash: b9ca1b42fad01cb5e8d456c64f5fcffe912ea4340988c5c059337afc0df07b99
- url: https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates
  content_hash: 74058f9e355d530d49435da50f83446fe490c185dc4037bbdff4f573030f8ab2
- url: https://support.telnyx.com/en/articles/13986487-how-to-configure-whatsapp-webhooks
  content_hash: 3165ce048d08e449a328ce473f21437e7ae480a5538c6e42f26e248bbfc6b475
- url: https://support.telnyx.com/en/articles/13986488-whatsapp-faq
  content_hash: 3154493d577f0184d1eb3aada07d2d4a697e2aee678a15ce304768eccaf2ff21
- url: https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide
  content_hash: ef49ad423dce5870a1ec3750586ab5e0d36e8fe0021539a57a44a99997dfc767
- url: https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers
  content_hash: a2578fc25c4f85421f3ff1fa1e72d87f822a3c32562eeb46e5ceebc64dc25fe8
- url: https://support.telnyx.com/en/collections/18868947-whatsapp-business
  content_hash: a08410203f8a1c793e98f264117954f1dc3cbeac4a31512069af01c4fd6125f8
updated_at: 2026-06-11T11:36:03Z
---

# WhatsApp Business Platform

*Part 5 of 5 — see also: [Part 1](whatsapp-business-platform--part-1.md), [Part 2](whatsapp-business-platform--part-2.md), [Part 3](whatsapp-business-platform--part-3.md), [Part 4](whatsapp-business-platform--part-4.md)*

WhatsApp Business Platform is Meta's API-based solution for sending and receiving WhatsApp messages at scale. Telnyx integrates as an official Business Solution Provider (BSP), offering API infrastructure for messaging, template management, phone number registration, webhook delivery, and WhatsApp Business Calling — all through the Telnyx Portal and API.

## Troubleshooting

### Template Issues

- **Template rejected** — Check common rejection reasons in order: missing sample values, no display name, incomplete business profile, template name issues, wrong category, vague content, variable placement errors. Edit and resubmit — there is no limit on edits. Do not delete and recreate (names cannot be reused for 30 days).
- **Template stuck in PENDING** — Meta's review typically takes 24–48 hours. Authentication templates are usually auto-approved within minutes. If pending for more than 48 hours, check the status in Meta Business Manager directly. If pending for more than 7 days, delete and resubmit with improved content.
- **Template category changed by Meta** — Since April 2025, Meta auto-reclassifies templates that don't match their category. If a template contains promotional language, submit it as Marketing from the start.

### Message Delivery Issues

- **Error code 40008** — This is the general WhatsApp error code; the response body contains the specific Meta API error. Common causes: template still pending, template rejected, template paused (wait for pause to lift or edit the template), template disabled (create a new one), template name or language mismatch, 24-hour window expired, invalid recipient, rate limit exceeded, phone number not registered.
- **Free-form messages fail** — Non-template messages can only be sent within the 24-hour conversation window. Outside the window, only approved template messages can be sent.
- **Message sent but not delivered** — Recipient may be offline (WhatsApp will retry), may have blocked your number, or may have no storage space. Check delivery status webhooks for specific error details.
- **Message not showing as "read"** — Read receipts are only sent if the recipient has read receipts enabled. Many users disable this.

### Quality Rating Issues

- **Quality rating dropped to Yellow or Red** — Customers are reporting or blocking your messages. Review message relevance, ensure proper opt-in, reduce frequency, and improve template content and targeting.
- **Messaging limit reduced** — If quality drops to Red, Meta may reduce your messaging limit tier. Improve quality by reducing blocks and reports, and your tier will gradually increase.
- **Template paused by Meta** — Pause durations escalate: 3 hours → 6 hours → permanently disabled. Edit the template content to improve relevance; changes take effect within 2 minutes.

### WhatsApp Calling Issues

- **Calling toggle** — Confirm "Calling" is enabled for the number in Mission Control.
- **Geo eligibility** — If business-initiated calling fails, check the business phone number's country code against the exclusions (USA, Canada, Egypt, Vietnam, Nigeria).
- **Permission state** — For business-initiated calls, verify user permission (temporary or permanent). If absent, send a permission request first.
- **Business-initiated call failing** — Verify dial string format, ensure the WhatsApp user has granted valid calling permissions, confirm the WhatsApp-enabled number is assigned to the same connection originating the call, check that temporary permission hasn't expired, and confirm permission wasn't auto-revoked after repeated unanswered calls.

## FAQ

### Phone Numbers

- **What phone number types can I use?** Landline, mobile, or toll-free numbers. The number cannot be currently registered with the WhatsApp consumer app or WhatsApp Business App.
- **Can I use the same number for SMS and WhatsApp?** Yes. Your Telnyx number can be used for both SMS/MMS and WhatsApp simultaneously.
- **Which countries are supported?** WhatsApp Business Platform is available globally wherever WhatsApp operates. You can send messages to any WhatsApp user worldwide. Conversation rates vary by destination country.

### Messaging

- **What is the maximum message size?** Text messages up to 4,096 bytes. Media captions up to 1,024 bytes. Header text up to 1,024 bytes.
- **How many contacts in one message?** 1–257 contacts in a single contact card message.
- **Can I send messages to non-WhatsApp users?** No. The recipient must have WhatsApp installed and an active account.
- **Can I send bulk messages?** You can send messages programmatically at scale via the API, subject to Meta's messaging limit tiers (starting at 1,000 unique recipients per 24 hours for new WABAs). You must use approved templates for business-initiated conversations.

### Billing

- **Am I charged per message or per conversation?** Per message delivered (as of July 1, 2025). Template messages are charged individually based on category and recipient country. Free-form (non-template) replies within the service window are free.
- **How do I track WhatsApp costs?** Each delivery status webhook includes a `billing_type` field. You can also view costs in the Telnyx Portal under Message Detail Records.

### Technical

- **What API endpoint do I use?** `POST /v2/messages/whatsapp` for sending all WhatsApp message types.
- **Do I need a messaging_profile_id?** No. The messaging profile is automatically resolved from the `from` phone number.
- **What error code does WhatsApp use?** WhatsApp errors typically return error code `40008`, which is a catch-all covering template issues and delivery failures. The response body contains additional details from the Meta API.
