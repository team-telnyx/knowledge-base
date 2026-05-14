---
title: WhatsApp Business Platform on Telnyx
summary: 'Learn how Telnyx, as a Meta Business Solution Provider, enables WhatsApp
  Business messaging and calling: setup, message types, 24‑hour service windows, templates
  and approvals, pricing and limits, webhooks, troubleshooting, and WhatsApp Business
  Calling for voice.'
sources:
- url: https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform
  content_hash: 79f16b29c219c8bc5dcc5fd55eec5b69ce5dd3ef8a2ae13cb7bd79b4bee8f781
- url: https://support.telnyx.com/en/articles/13986481-whatsapp-message-types-explained
  content_hash: 8af98253298adff5f0765bcbd62f514276356554340c542607afea2ef0bc0cbc
- url: https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window
  content_hash: 6362444ff65b4c521c82a3b73475fdbe5a557f1d923971a01cb1445f07826872
- url: https://support.telnyx.com/en/articles/13986483-whatsapp-message-templates-guide
  content_hash: 292a1163896236308d451a7b38a0b324a1df02e205898eca8f0b89e99b47fb23
- url: https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx
  content_hash: 2f70dfcf939022696136221eeb290abfe480c1ff3d8e0ac4d506acafadaac6d9
- url: https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx
  content_hash: d25019a300a1a95ab1bb3eb13e632453c62c189f4c9fa3c92751d5a48ac927ae
- url: https://support.telnyx.com/en/articles/13986486-how-to-create-whatsapp-message-templates
  content_hash: eeea87150bf1c057f250cc7395c69c4acdc019d50d7ad3b0ecfceca277c0c97c
- url: https://support.telnyx.com/en/articles/13986487-how-to-configure-whatsapp-webhooks
  content_hash: 0e23237c6f1f2fad0a8aeb8857c10c2f215c6416f766e4b2b0df17872f53abfc
- url: https://support.telnyx.com/en/articles/13986488-whatsapp-faq
  content_hash: d63ade98bf93dae6de12a8d643cb08fcea21f2306de51cfbfc78999d6b97d2e3
- url: https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide
  content_hash: 8cb784a9ad2f1c24f136109b20737b01e318f05d7935208c6c0dcb52e33d3037
- url: https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers
  content_hash: 8f087afe7b8175396eeb959167085c3f778c9ec04159efab08b137886fb3a993
updated_at: 2026-05-14T11:25:38Z
---

# WhatsApp Business Platform on Telnyx

*Part 1 of 2 — see also: [Part 2](whatsapp-business-platform-on-telnyx--part-2.md)*

Learn how Telnyx, as a Meta Business Solution Provider, enables WhatsApp Business messaging and calling: setup, message types, 24‑hour service windows, templates and approvals, pricing and limits, webhooks, troubleshooting, and WhatsApp Business Calling for voice.

## Platform overview and components
WhatsApp Business Platform is Meta’s API-based solution for programmatic, scalable messaging. Telnyx is an official Business Solution Provider (BSP) that lets you register numbers, manage templates, send/receive messages, and configure webhooks via the Telnyx API and Portal.

Key components:
- WhatsApp Business Account (WABA): The top-level container for your WhatsApp presence. It holds phone numbers, message templates, and your business profile. A WABA is linked to your Meta Business Manager.
- Meta Business Manager: Required to create a WABA, register numbers, manage the business profile, and connect Telnyx as your BSP during Embedded Signup.
- Telnyx BSP integration: Use Telnyx Portal and API for signup, number registration, template management, sending, receiving, and webhook configuration.

Helpful developer guides:
- Quickstart: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart
- Embedded Signup: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
- Send messages: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages

## Getting started on Telnyx (Embedded Signup)
Prerequisites:
- Telnyx account and Portal access
- Meta Business Manager account
- Phone number to register with WhatsApp (must not be active on WhatsApp consumer or Business App)

Setup steps (Portal):
1) Go to Messaging → WhatsApp and start Embedded Signup. Authenticate with a Facebook account that has admin access to your Meta Business Manager.
2) Select or create your Business Manager, authorize Telnyx, and select/create a WABA.
3) Register a phone number, choose a display name, and verify the number via call or SMS (use call verification for landlines). The number cannot already be in use on WhatsApp.
4) Complete setup: your WABA appears in Telnyx. Configure webhook URLs, manage templates, and keep your Meta business profile complete (website over HTTPS, description, category, address).

Notes:
- The Portal’s Embedded Signup currently requires a Telnyx-owned number with an active messaging profile; bring-your-own-number is not supported in this flow.
- Set and get Meta approval for the phone number’s display name before submitting templates.

## Message types and 24‑hour service windows
Two ways to message:
- Template messages (business-initiated): Required to start a new conversation or when the 24-hour window is closed. Categories: Marketing, Utility, Authentication.
- Free-form messages (session messages): Allowed only within 24 hours of the customer’s last message. Suitable for service/support replies. Supports text, image, video, document, audio, sticker, location, contacts (1–257 per message), and interactive types (quick reply buttons, CTA URL buttons, list messages, location request, carousel).

24-hour service window:
- Opens when a customer messages you (any inbound message or interactive reply). Each new customer message resets the 24-hour timer.
- While open: you can send free-form or template messages. Free-form messages are considered “Service.”
- When closed: free-form messages fail; you must send an approved template to re-engage.

## Template creation and approval
Templates are pre-approved formats required for business-initiated messages (including messaging outside the 24-hour window).

Structure and rules:
- Required fields: name (lowercase, underscores only), language (e.g., en_US), category (Marketing, Utility, Authentication), and body text (up to 1,024 characters) with optional variables like #{{1}}, #{{2}}.
- Optional components: header (text/image/video/document; text headers up to 60 characters), footer (up to 60 characters, no variables), and buttons (up to 3 quick replies or 2 call-to-action buttons for URL/phone).
- Variables: number sequentially starting at #{{1}}; do not start/end the body with a variable; avoid adjacent variables without text between; keep more fixed text than variables.
- Sample values: if a component uses variables, include realistic sample values via the example field. Missing examples are the most common cause of rejection.

Categories and guidance:
- Marketing: promotions, offers, product updates. Highest scrutiny and cost. Include clear opt-out language (e.g., in the footer).
- Utility: transactional updates (order, shipping, reminders). Lower cost and typically higher approval rates. Since April 2025, promotional language leads Meta to reclassify Utility templates to Marketing.
- Authentication: OTP/verification codes, often auto-approved and lowest cost. Put the OTP in the body as a variable.

Approval process and quality:
- Submit via Telnyx API; status typically moves from PENDING to APPROVED or REJECTED within 24–48 hours (Authentication often faster).
- Meta tracks template quality (High/Medium/Low). Low quality can trigger automated pacing/pauses (escalating to disabled if issues persist).

Common rejection causes:
- Missing sample values for variables; phone number display name not set/approved; incomplete business profile; test-like or vague names/content; wrong category (e.g., promotions as Utility); variable placement/density issues; URLs in body (use CTA buttons); missing opt-out for Marketing; policy violations; duplicates.

Management tips:
- Edit and resubmit rejected templates (unlimited edits). Avoid deleting to reuse the same name (name reuse is blocked for 30 days after deletion).
- Editing approved templates triggers re-review; they can’t be used during re-review.

API reference for template sends and components: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages#template-messages

## Sending, receiving, and webhooks
Sending:
- Endpoint: POST /v2/messages/whatsapp for all WhatsApp types (template, text, media, interactive, etc.).
- From number: Telnyx resolves the messaging profile from the from phone number; you don’t need a messaging_profile_id.
- Per-message webhook override: optionally include a webhook_url when sending.

Receiving and delivery status:
- Configure a webhook URL (HTTPS) in the Portal or via API.
- Inbound message webhooks include sender, message type and content, timestamp, and message ID.
- Delivery status webhooks provide sent, delivered, read, and failed states, plus billing_type for cost attribution.

Webhook requirements and testing:
- Use HTTPS with a valid certificate; respond 200 within 5 seconds.
- Implement idempotency (the same webhook may be retried).
- For local development, use tools like ngrok or Hookdeck.

General payload details: https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks

## Pricing, billing types, and limits
Billing model (current):
- Template messages are billed per message delivered, based on category and recipient country. This applies even if sent during an active service window.
- Free-form (non-template) replies sent within the 24-hour service window are not charged.

Billing types in delivery webhooks:
- whatsapp_marketing: Marketing template
- whatsapp_utility: Utility template
- whatsapp_authentication: Authentication template (same country as WABA)
- whatsapp_authentication_international: Authentication template (destination country differs from WABA country)
- whatsapp_service: Free-form reply within service window (free)

Entry points and special pricing:
- Messages originating from certain Meta entry points (e.g., Click-to-WhatsApp ads, Facebook Page buttons) may have special pricing. Always refer to Meta’s latest pricing: https://developers.facebook.com/docs/whatsapp/pricing

Viewing costs and limits:
- Use Telnyx Portal → Messaging → Message Detail Records to review costs and billing_type.
- Messaging limit tiers apply at the WABA level (new WABAs typically start at 1,000 unique recipients per 24 hours). Obtain proper user opt-in and use approved templates for business-initiated outreach.
