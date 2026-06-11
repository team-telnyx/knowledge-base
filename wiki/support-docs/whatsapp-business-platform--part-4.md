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

*Part 4 of 5 — see also: [Part 1](whatsapp-business-platform--part-1.md), [Part 2](whatsapp-business-platform--part-2.md), [Part 3](whatsapp-business-platform--part-3.md), [Part 5](whatsapp-business-platform--part-5.md)*

WhatsApp Business Platform is Meta's API-based solution for sending and receiving WhatsApp messages at scale. Telnyx integrates as an official Business Solution Provider (BSP), offering API infrastructure for messaging, template management, phone number registration, webhook delivery, and WhatsApp Business Calling — all through the Telnyx Portal and API.

## WhatsApp Business Calling

WhatsApp Business Calling lets your business receive and place voice calls with WhatsApp users using your Telnyx numbers. Calls are routed directly and securely between Telnyx and Meta rather than through the PSTN, enabling integration with Telnyx Programmable Voice, AI Assistants, call recording, and real-time analytics.

### Requirements

- A WhatsApp Business Account (WABA)
- A Telnyx phone number linked to your WABA (must belong to the same Telnyx account where the WhatsApp Calling configuration is being created)
- A WABA associated with a business/portfolio that has a daily messaging limit of at least 2,000 unique recipients. If not met, Meta may reject Calling enablement with the error "Calling APIs cannot be enabled for this phone number."

### Availability

| Call Type | Availability |
|---|---|
| User-initiated calls | Available wherever WhatsApp Business is available |
| Business-initiated calls | Not available for business numbers in: USA, Canada, Egypt, Vietnam, Nigeria (based on phone number's country code) |

### Enabling WhatsApp Business Calling

1. Navigate to **Voice Suite → WhatsApp Calling** in Mission Control.
2. Click **Connect WhatsApp Business** to trigger the embedded signup with Meta.
3. Select the WABA to associate with WhatsApp Calling.
4. Select the Telnyx phone number to enable. The number must be active and able to receive calls or SMS — Meta sends a verification code to confirm ownership.
5. Enter the verification code and confirm your configuration.
6. Navigate to **Voice Suite → WhatsApp Calling → WhatsApp Numbers**, select your number, open the **Calling** tab, and toggle **WhatsApp Calling** to enabled.

### User-Initiated Calls

Once enabled, your business can receive calls from any WhatsApp user via:

- **Call button in chat** — A call icon appears in the WhatsApp chat interface with your business
- **Click-to-call button** — Via an interactive message or template you send
- **Deep link** — A call link embedded on your website, app, or QR code

Calls connect through WhatsApp and are routed to your Telnyx number, handled by your existing SIP connection or Programmable Voice application like a regular inbound call.

### Business-Initiated Calls

You can initiate a call to any WhatsApp number from one of your SIP connections or Programmable Voice applications using the following dial string format:

`<destination_number>@whatsapp-<your_telnyx_number>.sip.telnyx.com`

Where `<destination_number>` is the WhatsApp user's phone number in E.164 format (e.g., `+447911123456`) and `<your_telnyx_number>` is your WhatsApp-enabled Telnyx number in E.164 format without the leading `+`.

**Example:** If your Telnyx number is `+447418613982` and you want to call `+447911123456`:

`+447911123456@whatsapp-447418613982.sip.telnyx.com`

This SIP URI can be used as the destination when placing WhatsApp calls from SIP, Voice API, or TeXML workflows.

### Obtaining Calling Permission

Before placing a business-initiated call, you must obtain the user's calling permission. There are three methods:

1. **Send a call permission request** — Send a free-form or templated message requesting calling permission. Rate limits: maximum 1 request per 24 hours per user, maximum 2 requests per 7 days per user. These limits reset automatically once a connected call takes place.
2. **Callback permission** — When enabled in your Meta Business Suite phone number call settings ("Allow Callbacks"), a temporary calling permission is automatically granted after a WhatsApp user calls your business.
3. **Permission via Business Profile** — WhatsApp users can grant permission directly from your WhatsApp Business profile by saving your number as a contact, opening the contact, tapping **View Contact** → **Business Call Permission**, and selecting a permission option.

**Permission durations:**

- **Temporary** — Valid for 7 days
- **Permanent** — Granted by the user indefinitely

### Unanswered Call Behaviour

WhatsApp monitors consecutive missed business-initiated calls on a per-user basis:

- After **2 consecutive unanswered calls**, WhatsApp sends the user a nudge notification
- After **4 consecutive unanswered calls**, permission is **automatically revoked** and you'll need to request it again

Only call users who are expecting to hear from you to avoid hitting this limit.

### WhatsApp Calling Pricing

A flat fee of **$0.0025/min** applies to both user-initiated and business-initiated WhatsApp calls. Business-initiated calls are also subject to additional WhatsApp Calling charges based on the applicable rate deck. Check **My Pricing** in the portal or contact your account representative for rates.

### WhatsApp Calling FAQ

- **Can I bridge WhatsApp calls to PSTN?** No. WhatsApp Calling is on-net to WhatsApp users only.
- **Do calls count against messaging limits?** No. Calling has separate limits. However, Meta requires the WABA to have a ≥ 2,000 daily messaging limit to enable Calling.
- **Is there a limit on concurrent calls?** Yes. Meta's maximum is 1,000 concurrent calls per business number.
