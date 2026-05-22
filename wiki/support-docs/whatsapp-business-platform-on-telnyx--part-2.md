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

*Part 2 of 2 — see also: [Part 1](whatsapp-business-platform-on-telnyx--part-1.md)*

A concise guide to using WhatsApp Business with Telnyx: how it works, onboarding and setup, message types and the 24‑hour window, templates and approvals, pricing and billing, webhooks, troubleshooting, and WhatsApp Business Calling for voice.

## Troubleshooting quick reference
- Embedded signup fails: Ensure Meta Business Manager admin access; clear cookies/use private window; disable popup‑blocking extensions; confirm the number isn’t linked to a different BSP.
- Number verification fails: Wait between attempts; try voice call verification (especially for landlines); confirm the number isn’t already registered and can receive calls/SMS.
- Display name issues: Set/adjust in Meta Business Manager → WhatsApp Accounts → Phone Numbers; wait up to 48 hours for review; avoid submitting templates before approval.
- Error 40008 on send: Often a template issue (pending, rejected, paused, disabled), name/language mismatch, expired 24‑hour window (use a template), invalid recipient/no WhatsApp, exceeded messaging limit, or unregistered sender number.
- Free‑form send fails: Likely outside the 24‑hour window; re‑engage with an approved template.
- Delivered but not read: Recipients can disable read receipts; lack of “read” doesn’t always mean unread.
- Quality downgrade/pauses: Reduce complaint drivers, improve targeting and content, include opt‑out on Marketing, and adjust frequency; paused templates can be edited to improve and reused after changes propagate.

## WhatsApp Business Calling (voice)
What it is: Voice calling between your Telnyx numbers and WhatsApp users, routed directly and securely via Meta (not over the PSTN). You can receive user‑initiated calls and, with permission, place business‑initiated calls — leveraging Telnyx Programmable Voice features (SIP connections, Voice API, AI Assistants, recording, analytics).

Availability and requirements:
- WABA required. The Telnyx number used for WhatsApp Calling must belong to the same Telnyx account where you configure calling.
- Your WABA must have a daily messaging limit of at least 2,000 unique recipients to enable Calling (separate from call limits).
- User‑initiated calls: Available wherever WhatsApp Business is available.
- Business‑initiated calls: Not available for business numbers in USA, Canada, Egypt, Vietnam, or Nigeria (based on the number’s country code). You must obtain the user’s calling permission first.

Enable in Mission Control (high level):
1) Voice Suite → WhatsApp Calling → Connect WhatsApp Business (embedded Meta flow) and select the WABA. 2) Associate and verify your Telnyx number. 3) Confirm configuration and ensure your WABA shows Active. 4) Voice Suite → WhatsApp Calling → WhatsApp Numbers → select your number and toggle WhatsApp Calling on.

Place and receive calls:
- Receiving (user‑initiated): Users can call from the chat call button, from a CTA in your messages, or via deep links/QR — routed to your Telnyx number and handled by your SIP/Voice application.
- Placing (business‑initiated): From your SIP connection or Voice API using the WhatsApp‑enabled Telnyx number as the From. Use a SIP URI like: <destination_number>@whatsapp-<your_telnyx_number_without_plus>.sip.telnyx.com (E.164 for both numbers). Ensure the user has granted permission and your number is eligible by country.

Calling permissions:
- How to obtain: Send a call permission request (template or free‑form within service window), accept a user’s callback (temporary permission auto‑granted if “Allow Callbacks” is enabled in Meta’s call settings), or the user grants via your Business Profile.
- Limits on requests: Max 1 request per 24 hours and 2 per 7 days per user; limits reset after a connected call.
- Duration: Temporary permission lasts 7 days; permanent permission is also supported.
- Unanswered behavior: After 2 consecutive unanswered business‑initiated calls, WhatsApp nudges the user; after 4 consecutive unanswered calls, permission is auto‑revoked.

Calling pricing and limits:
- Telnyx platform fee: $0.0025/min for user‑initiated and business‑initiated calls. Business‑initiated calls may incur additional WhatsApp Calling charges per Meta’s rate deck. See your portal pricing for specifics.
- Concurrency: Up to 1,000 concurrent calls per business number.
- PSTN: Bridging WhatsApp calls to the PSTN is not supported.

## Developer resources
- Quickstart, embedded signup, and send guides: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart, https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup, https://developers.telnyx.com/docs/messaging/whatsapp/send-messages
- Receiving webhooks: https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks
- Meta pricing reference: https://developers.facebook.com/docs/whatsapp/pricing
