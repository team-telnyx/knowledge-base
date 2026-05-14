---
title: WhatsApp Business Platform on Telnyx
summary: 'Learn how Telnyx, as a Meta Business Solution Provider, enables WhatsApp
  Business messaging and calling: setup, message types, 24‑hour service windows, templates
  and approvals, pricing and limits, webhooks, troubleshooting, and WhatsApp Business
  Calling for voice.'
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
updated_at: 2026-05-14T11:25:38Z
---

# WhatsApp Business Platform on Telnyx

*Part 2 of 2 — see also: [Part 1](whatsapp-business-platform-on-telnyx--part-1.md)*

Learn how Telnyx, as a Meta Business Solution Provider, enables WhatsApp Business messaging and calling: setup, message types, 24‑hour service windows, templates and approvals, pricing and limits, webhooks, troubleshooting, and WhatsApp Business Calling for voice.

## Troubleshooting common issues
Signup and number verification:
- Embedded Signup errors: ensure Facebook admin access to the Business Manager; clear cookies, try incognito; disable popup-blocking extensions; confirm the number isn’t already linked to another BSP/WABA.
- Phone verification: respect rate limits; prefer call verification for landlines; ensure the number can receive calls/SMS; confirm it’s not already on WhatsApp consumer/Business App.
- Display name: set and get approval in Meta before submitting templates; mismatched/absent display names delay or cause template rejections.

Template problems:
- Rejections: add missing sample values, fix category, improve specificity, correct variable placement, remove URLs from body (use CTA), add Marketing opt-out, ensure business profile completeness and approved display name.
- Stuck in PENDING (>48h): check status directly in Meta Business Manager; if stale >7 days, delete and resubmit improved content.
- Category changed by Meta: Utility with promotional language will be reclassified to Marketing (affects price).

Message delivery:
- Error 40008: a generic WhatsApp error that often indicates template state/content issues (pending/rejected/paused/disabled), window expired (use a template), invalid recipient (no WhatsApp/blocked), rate limits exceeded, number not registered, or template name/language mismatch.
- Free-form failures: you’re likely outside the 24-hour window; send a template to re-open user engagement.
- Delivered but not read: users may disable read receipts; a message can be read without a read webhook.

Quality rating and limits:
- Drops to Yellow/Red indicate blocks/reports or low relevance. Improve targeting/content, ensure opt-in, and reduce frequency. Persistent issues can lower messaging limits and pause/disable templates.

## WhatsApp Business Calling (voice)
Overview:
- WhatsApp Business Calling lets your Telnyx number place and receive voice calls with WhatsApp users. Calls route securely between Telnyx and Meta (not over the PSTN) and can leverage Telnyx Programmable Voice features (SIP, AI, recording, analytics).

Who it’s for:
- Businesses already using WhatsApp messaging that want to add voice on the same channel without separate infrastructure.

Requirements:
- A WABA; a Telnyx number in the same Telnyx account where you configure Calling; and a WABA daily messaging limit of at least 2,000 unique recipients (Meta enforces this for enabling Calling).

Availability:
- User-initiated calls: available wherever WhatsApp Business is available.
- Business-initiated calls: not available for business numbers with country codes in USA, Canada, Egypt, Vietnam, Nigeria. You must obtain the user’s calling permission before calling.

Enable in Mission Control (summary):
1) Voice Suite → WhatsApp Calling → Connect WhatsApp Business (Embedded Signup) and select the WABA.
2) Associate and verify your Telnyx number (code via call or SMS where applicable).
3) Confirm configuration; the WABA should show Active under Voice Suite → WhatsApp Calling → Business Account.
4) Voice Suite → WhatsApp Calling → WhatsApp Numbers → select your number and enable WhatsApp Calling.

Place and receive calls:
- Receiving (user-initiated): once enabled, users can call via chat call button, a click-to-call action, or a deep link; Telnyx routes to your SIP connection or Programmable Voice app like a normal inbound call.
- Placing (business-initiated): ensure eligibility and user permission, then dial using the SIP URI format: <destination_number>@whatsapp-<your_telnyx_number>.sip.telnyx.com (numbers in E.164; omit leading + from your Telnyx number in the domain). Example: +447911123456@whatsapp-447418613982.sip.telnyx.com.

Obtaining calling permission:
- Send a call permission request via free-form (within window) or template message. Limits: max 1 request per 24 hours and 2 per 7 days per user; limits reset after a connected call. Users can grant temporary (7 days) or permanent permission.
- Callback permission: if “Allow Callbacks” is enabled in Meta’s call settings, a user call to your business automatically grants temporary permission.
- Users can also grant permission from your Business Profile (View Contact → Business Call Permission).

Unanswered call behavior:
- After 2 consecutive unanswered business-initiated calls, WhatsApp nudges the user; after 4, permission is automatically revoked.

Calling limitations and pricing:
- No PSTN bridging; WhatsApp Calling is on-net to WhatsApp users only.
- Meta limit: up to 1,000 concurrent calls per business number.
- Price: $0.0025/min for both user-initiated and business-initiated calls. Business-initiated calls may also incur additional WhatsApp Calling charges per your rate deck (see My Pricing in the Portal or contact your account team).

Calling troubleshooting:
- Ensure the Calling toggle is enabled; verify country eligibility; confirm user permission state (temporary/permanent); check dial string formatting; ensure the WhatsApp-enabled number is on the same connection placing the call.
