---
title: WhatsApp Business Platform on Telnyx
summary: 'A concise guide to using WhatsApp Business with Telnyx: how it works, onboarding
  and setup, message types and the 24‑hour window, templates and approvals, pricing
  and billing, webhooks, troubleshooting, and WhatsApp Business Calling for voice.'
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
updated_at: 2026-05-20T14:30:12Z
---

# WhatsApp Business Platform on Telnyx

*Part 1 of 2 — see also: [Part 2](whatsapp-business-platform-on-telnyx--part-2.md)*

A concise guide to using WhatsApp Business with Telnyx: how it works, onboarding and setup, message types and the 24‑hour window, templates and approvals, pricing and billing, webhooks, troubleshooting, and WhatsApp Business Calling for voice.

## What it is and how it works
WhatsApp Business Platform is Meta’s API for programmatic messaging at scale. Telnyx is an official Business Solution Provider (BSP), giving you API access to send/receive WhatsApp messages, manage templates, and register numbers, all tied to your Meta Business Manager.

Key building blocks:
- WhatsApp Business Account (WABA): Container for your business presence (phone numbers, templates, business profile), linked to your Meta Business Manager.
- Meta Business Manager: Where you authorize Telnyx during embedded signup, manage your WABA, phone numbers, display name, and business profile.
- Telnyx (BSP): Provides the messaging API, webhooking, number registration workflow, and portal management.

Typical flow with Telnyx:
1) Embedded signup in the Telnyx Portal to create/connect a WABA and register a phone number. 2) Create templates and get Meta approval. 3) Send messages via POST /v2/messages/whatsapp. 4) Receive inbound messages and delivery statuses via webhooks.

## Onboarding and prerequisites
- Accounts: Telnyx account and Meta Business Manager admin access.
- Phone number: Landline, mobile, or toll‑free supported. The number cannot be active on the WhatsApp consumer or Business app; delete that account first if needed.
- Telnyx-owned number: The embedded signup currently requires a Telnyx number with an active messaging profile (bring‑your‑own number via portal signup isn’t supported yet).
- Display name and business profile: Set and get the display name approved, and complete the business profile (HTTPS website, description, industry, address) before submitting any templates.
- Business verification: Completing Meta’s business verification improves approval odds and limits.

Setup steps (Portal):
- Mission Control → Messaging → WhatsApp → Get Started → authenticate with Facebook and connect/select your Meta Business Manager and WABA.
- Register and verify your number (SMS or phone call; choose call for landlines).
- Configure webhook URLs for inbound messages and delivery receipts.
- Create at least one template, wait for approval, then send your first message.

## Message types and the 24‑hour window
Two send modes govern how and when you can message:
- Template messages (business‑initiated): Required to start a new conversation or to reach a user after 24 hours of their last message. Categories: Marketing, Utility, Authentication.
- Free‑form messages (session replies): Allowed only within 24 hours after the user last messaged you; supports text, media, location, contacts, and interactive content (quick replies, CTA URL buttons, list messages, carousels, and location requests).

24‑hour window basics:
- Opens when the user messages you (or replies/taps CTA), and resets with each new user message.
- While open: You may send free‑form and/or template messages.
- After expiry: Free‑form messages fail; you must use an approved template to re‑engage.

When to use what:
- No prior user message or window expired: Use a template (required).
- Responding within 24 hours: Use free‑form or a template.
- OTP/verification: Authentication template. Transactional updates: Utility template. Promotions/offers: Marketing template.

## Sending and receiving with the Telnyx API
- Endpoint: POST /v2/messages/whatsapp for all types (template, text, media, interactive, etc.).
- From number: Telnyx resolves the messaging profile from your WhatsApp‑registered “from” number (messaging_profile_id not required for WhatsApp sends).
- Inbound and delivery: Configure webhooks to receive customer messages and status updates (sent, delivered, read, failed). Webhooks include message metadata and billing_type.
- Content limits (common): Text up to ~4,096 characters; media captions up to ~1,024 characters. Supported media: images, videos, documents, audio, stickers; plus location, contacts, and interactive components.

## Templates: structure, approval, and quality
What templates are: Pre‑approved formats required for business‑initiated messaging (outside the 24‑hour window). Categories: Marketing, Utility, Authentication.

Structure and rules (highlights):
- Name: Lowercase with underscores/numbers; avoid names like “test”, “sample”, “demo”.
- Language: e.g., en_US, es, pt_BR.
- Components: Body (required; up to 1,024 chars), optional Header (text/image/video/document; text headers typically up to 60 chars), optional Footer (up to 60 chars; no variables), optional Buttons (up to 3 quick replies or 2 CTAs for URL/phone).
- Variables: Use placeholders like #{{1}}, #{{2}}. Number sequentially; don’t start/end the body with a variable; don’t place variables adjacent without text.
- Samples: Always include sample values for any component with variables. Meta reviewers use them to evaluate the rendered message.

Approval process:
- Submit via the Telnyx API; status progresses PENDING → APPROVED or REJECTED (Authentication templates are often auto‑approved; Marketing/Utility reviewed in ~24–48 hours).
- Edit and resubmit rejections without limit. Editing approved templates triggers re‑review and temporarily blocks sending with that template.

Quality and pacing:
- Meta rates templates (High/Medium/Low) based on user feedback (blocks, spam reports, engagement). Low quality may trigger automatic pauses that escalate (e.g., 3 hours → 6 hours → permanent disable). New or lower‑quality templates may be delivery‑paced.

Common rejection causes (fix these first):
- Missing sample values for variables, no/invalid display name, incomplete business profile.
- Vague content, excessive variables, variables at start/end, adjacent variables.
- Wrong category (e.g., promotional content submitted as Utility). Since April 2025, Meta auto‑reclassifies promotional Utility templates as Marketing, affecting pricing.
- URLs in body (use CTA URL buttons; avoid URL shorteners and wa.me links).
- Missing opt‑out language for Marketing; prohibited content per Meta Commerce Policy; duplicate/similar templates.

## Pricing and billing
Model in Telnyx (as of July 1, 2025):
- Template messages are billed per message delivered, by category (Marketing, Utility, Authentication) and destination country.
- Free‑form (non‑template) replies within the 24‑hour service window are not charged.
- Template messages sent during an open window are still billed per their category.

billing_type values in delivery webhooks:
- whatsapp_marketing, whatsapp_utility, whatsapp_authentication, whatsapp_authentication_international, whatsapp_service (free window replies).

Special entry points: Messages originating from certain Meta entry points (e.g., Click‑to‑WhatsApp ads, Facebook Page buttons) may have special pricing. Refer to Meta’s pricing docs for current details.

Track costs in Mission Control under Messaging → Message Detail Records (look for billing_type on each record).

## Webhooks: events and requirements
What you receive:
- Inbound messages: Sender, type (text/media/location/contacts/interactive), content payload, timestamp, message ID.
- Delivery statuses: sent, delivered, read, failed — with billing_type and error info when applicable.

Requirements and best practices:
- HTTPS endpoint with valid certificate; respond 200 within 5 seconds.
- Implement idempotency: dedupe by message ID because retries can occur.
- For local testing, use tools like ngrok or Hookdeck to expose and inspect your endpoint.

## Limits, compliance, and best practices
- Messaging limits: New WABAs start with lower daily unique recipient tiers (e.g., ~1,000/24h) that increase with quality and volume. Respect rate limits to avoid errors.
- Opt‑in and relevance: Obtain user consent and send expected, relevant content to minimize blocks/reports and protect quality ratings and limits.
- Respond promptly: The 24‑hour window starts from the user’s message; slow replies reduce your free‑form window.
- Prepare templates in advance: Have approved templates ready for follow‑ups after the window expires.
