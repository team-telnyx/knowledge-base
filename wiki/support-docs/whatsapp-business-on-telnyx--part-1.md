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

*Part 1 of 6 — see also: [Part 2](whatsapp-business-on-telnyx--part-2.md), [Part 3](whatsapp-business-on-telnyx--part-3.md), [Part 4](whatsapp-business-on-telnyx--part-4.md), [Part 5](whatsapp-business-on-telnyx--part-5.md), [Part 6](whatsapp-business-on-telnyx--part-6.md)*

A consolidated reference for using the WhatsApp Business Platform through Telnyx as a Meta Business Solution Provider. It covers account setup, message types and templates, conversation-based billing, webhooks, voice calling, troubleshooting, and frequently asked questions.

## Overview

WhatsApp Business Platform is Meta's API-based solution that lets businesses send and receive messages on WhatsApp at scale. Unlike the WhatsApp Business App (designed for small businesses), the Platform is built for programmatic integration — you connect via an API through a Business Solution Provider (BSP) like Telnyx.

The platform is built around three core components:

- **WhatsApp Business Account (WABA)** — the top-level container for your WhatsApp business presence. It holds your phone numbers, message templates, and business profile. Each WABA is linked to a Meta Business Manager account.
- **Business Solution Provider (BSP)** — Telnyx is an official Meta BSP, providing the API infrastructure to send and receive WhatsApp messages, manage templates, and handle phone number registration through the Telnyx API and Portal.
- **Meta Business Manager** — Meta's platform for managing business assets. You need a Meta Business Manager account to create a WABA and register phone numbers. During Telnyx's Embedded Signup flow, you'll connect your Meta Business Manager to authorize Telnyx as your BSP.

The typical flow on Telnyx is: sign up via Embedded Signup, create and get templates approved, send messages with `POST /v2/messages/whatsapp`, and receive messages and delivery status updates via webhooks.

## Setting Up WhatsApp on Telnyx

### Prerequisites

- A Telnyx account ([portal.telnyx.com](https://portal.telnyx.com))
- A Meta Business Manager account ([business.facebook.com](https://business.facebook.com))
- A phone number to register with WhatsApp (cannot be currently used with personal WhatsApp)

### Embedded Signup Steps

1. **Start Embedded Signup** — Log in to the Telnyx Portal, navigate to **Messaging → WhatsApp**, and click **Get Started** or **Add WhatsApp Business Account**. You will be redirected to Facebook/Meta to authenticate.
2. **Connect Meta Business Manager** — Log in with a Facebook account that has admin access, select or create a Meta Business Manager, grant Telnyx the required permissions, and select or create a WABA.
3. **Register a Phone Number** — Enter the phone number, choose a display name, and verify via phone call or SMS. If registering a landline, choose phone call verification because SMS delivery to landlines can be unreliable. The embedded signup flow currently requires a Telnyx-owned number with an active messaging profile; bring-your-own-number is not yet supported through the portal signup flow. The phone number cannot be currently active on the WhatsApp consumer app or WhatsApp Business App — delete that account first if it is.
4. **Complete Setup** — Once verification is complete, your WABA appears under **Messaging → WhatsApp**. From here you can view WABA details and phone numbers, configure webhook URLs, manage your business profile via Meta Business Manager, and create and manage message templates.
5. **Create Your First Template** — Before sending business-initiated messages, you need at least one approved template. Use the Telnyx API to create a template and wait for Meta's approval (typically 24–48 hours).
6. **Send Your First Message** — Once the template is approved, send your first WhatsApp message via the Telnyx API. See the [WhatsApp Quickstart Guide](whatsapp-quickstart-guide.md) for a complete walkthrough.

### Common Signup Issues

- **Signup flow fails** — Ensure your Facebook account has admin access to the Meta Business Manager. Try clearing browser cookies and restarting the flow in an incognito/private window, and disable browser extensions that may block Facebook popups. Check that you don't have an existing WABA linked to a different BSP for the same number.
- **Phone verification fails** — Wait a few minutes between attempts (there is a rate limit on verification codes). If using SMS verification on a landline, switch to phone call verification. Ensure the number is not already registered with WhatsApp consumer app and that it can receive calls or SMS.
- **Number already in use** — The number is registered with WhatsApp on a phone. Delete the WhatsApp account from the phone (WhatsApp → Settings → Account → Delete my account) before retrying.
- **Display name not set or rejected** — Go to Meta Business Manager → WhatsApp Accounts → your WABA → Phone Numbers, click the phone number, and set the display name. The display name must match or relate to your verified business name. Review takes up to 48 hours. Do not submit templates until the display name is approved — they will be rejected.

## Message Types

WhatsApp messages fall into two categories based on how conversations are initiated.

### Template Messages (Business-Initiated)

Template messages are pre-approved message formats that you submit to Meta for review. They are required to start a new conversation with a customer or to message a customer outside the 24-hour conversation window.

Templates have three categories, each with different billing rates:

| Category | Use Cases | Examples |
| --- | --- | --- |
| **Marketing** | Promotions, offers, updates | "Hi #{{1}}, our spring sale starts tomorrow! Get 20% off with code SPRING20." |
| **Utility** | Transaction updates, alerts | "Your order #{{1}} has shipped. Track it here: #{{2}}" |
| **Authentication** | OTP, verification codes | "Your verification code is #{{1}}. It expires in 10 minutes." |

Templates support variable substitution using `#{{1}}`, `#{{2}}`, etc. They can include headers (text, image, video, or document), body text, footers, and buttons (quick reply or call-to-action).

### Free-form Messages (Session Messages)

Free-form messages can be sent only within a 24-hour window after the customer last messaged you. These create "Service" conversations and support rich content types:

- **Text** — Plain text up to 4,096 characters
- **Image** — JPEG, PNG (with optional caption up to 1,024 characters)
- **Video** — MP4 (with optional caption)
- **Document** — PDF, DOC, etc. (with optional caption and filename)
- **Audio** — OGG, MP3, etc.
- **Sticker** — WebP format
- **Location** — GPS coordinates with name and address
- **Contacts** — Contact cards (1–257 per message)
- **Interactive** — Quick reply buttons, CTA URL buttons, list messages

### When to Use Which

| Scenario | Message Type |
| --- | --- |
| Customer hasn't messaged you yet | Template (required) |
| 24-hour window has expired | Template (required) |
| Customer messaged within last 24 hours | Free-form or Template (your choice) |
| Sending OTP or verification code | Authentication Template |
| Sending order update or receipt | Utility Template |
| Sending promotion or offer | Marketing Template |
| Responding to a customer's question | Free-form (within 24hr window) |
