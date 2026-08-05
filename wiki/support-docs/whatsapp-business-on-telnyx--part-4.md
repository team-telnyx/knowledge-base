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

*Part 4 of 6 — see also: [Part 1](whatsapp-business-on-telnyx--part-1.md), [Part 2](whatsapp-business-on-telnyx--part-2.md), [Part 3](whatsapp-business-on-telnyx--part-3.md), [Part 5](whatsapp-business-on-telnyx--part-5.md), [Part 6](whatsapp-business-on-telnyx--part-6.md)*

A consolidated reference for using the WhatsApp Business Platform through Telnyx as a Meta Business Solution Provider. It covers account setup, message types and templates, conversation-based billing, webhooks, voice calling, troubleshooting, and frequently asked questions.

## WhatsApp Business Calling

WhatsApp Business Calling lets your business receive and place voice calls with WhatsApp users using your Telnyx number. Calls are routed directly and securely between Telnyx and Meta rather than through the PSTN. By enabling WhatsApp Calling through Telnyx, you can leverage Telnyx platform capabilities including Programmable Voice, AI Assistants, call recording, and real-time analytics, all from Mission Control Portal or the API.

### Who It's For

Businesses already using WhatsApp for customer communication that want to extend their interactions to voice, on a secure, widely adopted channel, without building a separate integration or managing a different infrastructure.

### Requirements

- A WhatsApp Business Account (WABA)
- A Telnyx phone number that will be linked to your WABA. The Telnyx number used for WhatsApp Calling must belong to the same Telnyx account where the WhatsApp Calling configuration is being created.
- A WhatsApp Business Account associated with a business/business portfolio that has a daily messaging limit of at least 2,000 unique recipients. If this requirement is not met, Meta may reject Calling enablement with the error "Calling APIs cannot be enabled for this phone number."

### Availability

| Call Type | Availability |
| --- | --- |
| User-initiated calls | Available wherever WhatsApp Business is available |
| Business-initiated calls | Not available for business numbers in: USA, Canada, Egypt, Vietnam, Nigeria (based on the phone number's country code). Before placing a call, you must obtain the user's calling permission. |

### Enabling Calling in Mission Control

1. **Connect Your WhatsApp Business Account** — In Mission Control, navigate to **Voice Suite → WhatsApp Calling** and click **Connect WhatsApp Business**, which triggers the embedded signup windows for the integration with Meta. Select the WABA you want to associate with WhatsApp Calling.

   ![](_images/d110c80b55518543.png)

   ![](_images/2d7116fcf9cfcc24.png)

   ![](_images/633946f79bd08aad.png)

2. **Associate your Telnyx number** — Select the Telnyx phone number you want to enable for WhatsApp Calling. Your Telnyx number must be active and able to receive calls or SMS (mobile numbers only) — Meta will send a verification code to confirm ownership. Enter the verification code once received.

   ![](_images/df1b804144d9c800.png)

   ![](_images/b81f6a7a8470b939.png)

3. **Confirm your configuration** — Review and confirm your WhatsApp configuration in Telnyx. You'll see a confirmation screen indicating your Meta account has been successfully connected to Telnyx. Navigate to **Voice Suite → WhatsApp Calling → Business Account** — your WABA should now appear with an **Active** status. It can take up to 2 minutes for this information to show up.

   ![](_images/a8f384e0355c3cdc.png)

   ![](_images/44ba3cb0da289331.png)

   ![](_images/ce85e38f2726773f.png)

   ![](_images/5d18934dc18d9e61.png)

4. **Enable WhatsApp Calling in Telnyx** — In Mission Control, navigate to **Voice Suite → WhatsApp Calling → WhatsApp Numbers**. Select your number — it should show a **Connected** status. Open the **Calling** tab and toggle **WhatsApp Calling** to enabled.

   ![](_images/06674c2ed3dfebac.png)

   ![](_images/893658dbadd451be.png)

   ![](_images/af5a55c4ec7f8018.png)

### Placing and Receiving Calls

**User-Initiated Calls** — Once WhatsApp Calling is enabled on your number, your business is ready to receive calls from any WhatsApp user. WhatsApp users can reach you via:

- **Call button in chat** — if enabled, a call icon appears directly in the WhatsApp chat interface with your business.
- **Click-to-call button** — via an interactive message or template you send to the user.
- **Deep link** — a call link you embed on your website, app, or QR code that launches a call directly.

Regardless of how the call is initiated, it connects through WhatsApp and is routed to your Telnyx number, handled by your existing SIP connection or Programmable Voice application, just like a regular inbound call. No additional setup is required.

**Business-Initiated Calls** — You can initiate a call to any WhatsApp number as long as you meet these requirements:

1. You're initiating the call from one of your SIP connections or Programmable Voice applications
2. You're using the WhatsApp Calling number as the From number
3. The user has granted permission for you to call them
4. Your WhatsApp Calling number is not from any of these countries: USA, Canada, Egypt, Vietnam, Nigeria

To place a call to a WhatsApp user from your Telnyx number, use the following dial string format:

`<destination_number>@whatsapp-<your_telnyx_number>.sip.telnyx.com`

Where:

- `<destination_number>` is the WhatsApp user's phone number in E.164 format (e.g., `+447911123456`)
- `<your_telnyx_number>` is your WhatsApp-enabled Telnyx number in E.164 format, without the leading `+`

Example: If your Telnyx number is `+447418613982` and you want to call `+447911123456`, the dial string is:

`+447911123456@whatsapp-447418613982.sip.telnyx.com`

This SIP URI can be used as the destination when placing WhatsApp calls from SIP, Voice API, or TeXML workflows.

### Obtaining Calling Permission

You can obtain calling permission from a WhatsApp user in any of the following ways:

1. **Send a call permission request to the user** — Send a free-form or templated message requesting calling permission from the user. The user has the option to choose between temporary or permanent. Rate limits: maximum 1 request per 24 hours per user, maximum 2 requests per 7 days per user. These limits reset automatically once a connected call (business- or user-initiated) takes place between you and the user. Once the user grants permission, you can place the outbound WhatsApp call from your configured Telnyx workflow. Permissions can be temporary (valid for 7 days) or permanent (granted by the user indefinitely).
2. **Callback permission is provided by the WhatsApp user** — The WhatsApp user automatically provides temporary call permissions by placing a call to the business. The callback setting must be enabled on the business phone number. In WhatsApp Manager → Phone on your Meta Business Suite, select your number, go to Call Settings, and enable "Allow Callbacks".

   ![](_images/460a474bc563eda7.png)

3. **WhatsApp user provides call permission via Business Profile** — WhatsApp users can grant permission directly from your WhatsApp Business profile at any time by saving your Telnyx number as a WhatsApp contact, opening the contact (it will appear as a Business Profile), tapping **View Contact → Business Call Permission**, and selecting the desired permission option.

   ![](_images/17a2d1db975777ea.png)

**Unanswered Call Behaviour** — WhatsApp monitors consecutive missed business-initiated calls on a per-user basis:

- After 2 consecutive unanswered calls, WhatsApp sends the user a nudge notification.
- After 4 consecutive unanswered calls, permission is automatically revoked and you'll need to request it again.

To avoid hitting this limit, only call users who are expecting to hear from you.

### Calling Pricing

A flat fee of **$0.0025/min** applies to both user-initiated and business-initiated WhatsApp calls. Business-initiated calls are also subject to additional WhatsApp Calling charges based on the applicable rate deck. To view your rates, check **My Pricing** in the portal or contact your account representative.

### Calling FAQs

- **Can I bridge WhatsApp calls to PSTN?** No. WhatsApp Calling is on-net to WhatsApp users only.
- **Do calls count against messaging limits?** No. Calling has separate limits. However, Meta requires the WABA to have a ≥ 2,000 daily messaging limit to enable Calling.
- **Is there a limit to how many calls I can receive at once?** Yes. Meta's maximum is 1,000 concurrent calls per business number.
- **What's the difference between user-initiated and business-initiated calls?** User-initiated: the user calls your Telnyx number through WhatsApp, no special permission needed. Business-initiated: you call the user, but must first request their permission either through a template message or a free-form message during an active customer service window.
- **How do business-initiated calling permissions work?** Send a permission request (max 1 per 24 hours, 2 per 7 days per business+user). Temporary permission lasts 7 days; permanent permission is also supported. If 2 consecutive business-initiated calls go unanswered, WhatsApp notifies the user. After 4 consecutive unanswered calls, permission is auto-revoked.
- **Why is my business-initiated call failing?** Common causes include: the dial string is not properly formatted according to the integration requirements; the WhatsApp user has not granted calling permission; the user's temporary calling permission has expired; the calling permission was automatically revoked after repeated unanswered calls; or the WhatsApp calling number is not associated with the connection being used to place the call. Verify that the dial string matches the documented format, ensure the WhatsApp user has granted valid calling permissions, and confirm that the WhatsApp-enabled number is assigned to the same connection originating the call.

### Calling Troubleshooting

- **Calling toggle** — Confirm "Calling" is enabled for the number in Mission Control.
- **Geo eligibility** — If business-initiated calling fails, check the business phone number's country code against the exclusions listed above.
- **Permission state** — For business-initiated calls, verify user permission (temporary or permanent). If absent, send a permission request first.
- **Still stuck?** — Confirm your number is a Telnyx number under your WABA.
