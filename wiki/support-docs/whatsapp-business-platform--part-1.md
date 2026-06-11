---
title: WhatsApp Business Platform
summary: WhatsApp Business Platform is Meta's API-based solution for sending and receiving
  WhatsApp messages at scale. Telnyx integrates as an official Business Solution Provider
  (BSP), offering API infrastructure for messaging, template management, phone number
  registration, webhook delivery, and WhatsApp Business Calling — all through the
  Telnyx Portal and API.
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
updated_at: 2026-06-11T11:36:03Z
---

# WhatsApp Business Platform

*Part 1 of 5 — see also: [Part 2](whatsapp-business-platform--part-2.md), [Part 3](whatsapp-business-platform--part-3.md), [Part 4](whatsapp-business-platform--part-4.md), [Part 5](whatsapp-business-platform--part-5.md)*

WhatsApp Business Platform is Meta's API-based solution for sending and receiving WhatsApp messages at scale. Telnyx integrates as an official Business Solution Provider (BSP), offering API infrastructure for messaging, template management, phone number registration, webhook delivery, and WhatsApp Business Calling — all through the Telnyx Portal and API.

## Key Components

### WhatsApp Business Account (WABA)

A WABA is the top-level container for your WhatsApp business presence. It holds your phone numbers, message templates, and business profile. Each WABA is linked to a Meta Business Manager account. A Meta Business Manager account is required to create a WABA and register phone numbers.

### Business Solution Provider (BSP)

Telnyx is an official Meta BSP, providing the API infrastructure to send and receive WhatsApp messages, manage templates, and handle phone number registration — all through the Telnyx API and Portal.

### Meta Business Manager

Meta Business Manager is Meta's platform for managing business assets. During Telnyx's Embedded Signup flow, you connect your Meta Business Manager to authorize Telnyx as your BSP.

## Setting Up WhatsApp on Telnyx

### Prerequisites

- A Telnyx account ([portal.telnyx.com](https://portal.telnyx.com))
- A Meta Business Manager account ([business.facebook.com](https://business.facebook.com))
- A phone number to register with WhatsApp (cannot be currently used with personal WhatsApp or the WhatsApp Business App)

### Embedded Signup Flow

1. **Start** — Log in to the Telnyx Portal, navigate to **Messaging → WhatsApp**, and click **Get Started** or **Add WhatsApp Business Account**. You'll be redirected to Facebook/Meta to authenticate.
2. **Connect Meta Business Manager** — Log in with a Facebook account that has admin access, select or create a Meta Business Manager, grant Telnyx the required permissions, and select or create a WABA.
3. **Register a phone number** — Enter the phone number, choose a display name, and verify via phone call or SMS. For landline numbers, use phone call verification. The embedded signup flow currently requires a Telnyx-owned number with an active messaging profile; bring-your-own-number is not yet supported through the portal signup flow.
4. **Complete setup** — Once verified, your WABA appears under **Messaging → WhatsApp**. From here you can view WABA details, configure webhook URLs, manage your business profile, and create message templates.
5. **Create your first template** — Before sending business-initiated messages, you need at least one approved template. Use the Telnyx API to create one and wait for Meta's approval (typically 24–48 hours).
6. **Send your first message** — Once approved, send messages via the Telnyx API.

### Signup Troubleshooting

- **Flow fails** — Ensure your Facebook account has admin access. Clear browser cookies and try an incognito/private window. Disable browser extensions that block Facebook popups. Check for an existing WABA linked to a different BSP for the same number.
- **Phone verification fails** — Wait a few minutes between attempts (rate limit applies). If using SMS on a landline, switch to phone call verification.
- **Number already in use** — The number is registered with WhatsApp on a phone. Delete the WhatsApp account from the phone first (WhatsApp → Settings → Account → Delete my account).
- **Display name not set or rejected** — Go to Meta Business Manager → WhatsApp Accounts → your WABA → Phone Numbers to set the display name. It must match or relate to your verified business name. Review takes up to 48 hours. Do not submit templates until the display name is approved.

## Message Types

WhatsApp messages fall into two categories based on how conversations are initiated.

### Template Messages (Business-Initiated)

Template messages are pre-approved message formats submitted to Meta for review. They are **required** to start a new conversation with a customer or to message a customer outside the 24-hour conversation window. Templates have three categories, each with different billing rates:

| Category | Use Cases | Example |
|---|---|---|
| **Marketing** | Promotions, offers, updates | "Hi {{1}}, our spring sale starts tomorrow! Get 20% off with code SPRING20." |
| **Utility** | Transaction updates, alerts | "Your order {{1}} has shipped. Track it here: {{2}}" |
| **Authentication** | OTP, verification codes | "Your verification code is {{1}}. It expires in 10 minutes." |

Templates support variable substitution using `{{1}}`, `{{2}}`, etc. They can include headers (text, image, video, or document), body text, footers, and buttons (quick reply or call-to-action).

### Free-Form Messages (Session Messages)

Free-form messages can be sent **only within a 24-hour window** after the customer last messaged you. These create Service conversations and support rich content types:

- **Text** — Plain text up to 4,096 characters
- **Image** — JPEG, PNG (with optional caption up to 1,024 characters)
- **Video** — MP4 (with optional caption)
- **Document** — PDF, DOC, etc. (with optional caption and filename)
- **Audio** — OGG, MP3, etc.
- **Sticker** — WebP format
- **Location** — GPS coordinates with name and address
- **Contacts** — Contact cards (1–257 per message)
- **Interactive** — Quick reply buttons, CTA URL buttons, list messages, location request messages, carousel messages

### When to Use Which Message Type

| Scenario | Message Type |
|---|---|
| Customer hasn't messaged you yet | Template (required) |
| 24-hour window has expired | Template (required) |
| Customer messaged within last 24 hours | Free-form or Template (your choice) |
| Sending OTP or verification code | Authentication Template |
| Sending order update or receipt | Utility Template |
| Sending promotion or offer | Marketing Template |
| Responding to a customer's question | Free-form (within 24hr window) |

## The 24-Hour Conversation Window

WhatsApp uses a 24-hour conversation window to control when businesses can send free-form messages. The window opens when a customer messages you, and lasts for 24 hours from the customer's last message.

### What Opens the Window

- A customer sends you a message (text, image, button reply, etc.)
- A customer taps a call-to-action button in a previous message
- A customer replies to a template message

Each new message from the customer resets the 24-hour timer.

### During the Window (Open)

While the window is open, you can send both free-form messages and template messages. Free-form messages within the window create **Service** conversations, which are typically the lowest-cost conversation category.

### After the Window Closes (Expired)

Once 24 hours have passed since the customer's last message:

- Free-form messages will **fail**
- You must use an approved **template message** to re-initiate contact
- The template message opens a new conversation (billed at the template's category rate)

### Tips for the Conversation Window

- **Respond promptly** — The 24-hour window starts from the customer's message, not your reply. Delays eat into your free-form messaging time.
- **Use templates strategically** — Have relevant templates pre-approved and ready for follow-ups after the window closes.
- **Monitor via webhooks** — Use delivery status webhooks to track whether messages succeeded or failed due to window expiration.
