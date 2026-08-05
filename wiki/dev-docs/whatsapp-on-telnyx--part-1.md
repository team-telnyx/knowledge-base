---
title: WhatsApp on Telnyx
summary: Telnyx provides a complete WhatsApp Business Platform integration covering
  embedded signup (for direct customers and Tech Providers), WhatsApp Business Calling,
  and message template management. This page consolidates the onboarding flows, API
  endpoints, voice calling setup, and template lifecycle into a single reference.
sources:
- url: https://developers.telnyx.com/docs/messaging/whatsapp/business-calling/index
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
updated_at: 2026-08-05T13:58:27Z
---

# WhatsApp on Telnyx

*Part 1 of 4 — see also: [Part 2](whatsapp-on-telnyx--part-2.md), [Part 3](whatsapp-on-telnyx--part-3.md), [Part 4](whatsapp-on-telnyx--part-4.md)*

Telnyx provides a complete WhatsApp Business Platform integration covering embedded signup (for direct customers and Tech Providers), WhatsApp Business Calling, and message template management. This page consolidates the onboarding flows, API endpoints, voice calling setup, and template lifecycle into a single reference.

## Overview

Telnyx exposes the WhatsApp Business Platform through a set of REST APIs and a portal-based onboarding flow. Businesses can connect a WhatsApp Business Account (WABA), register phone numbers, send and receive messages, manage pre-approved message templates, and — with WhatsApp Business Calling — place and receive voice calls over WhatsApp using existing Telnyx voice infrastructure.

There are two onboarding paths:

- **Direct customer** — A business connects its own Facebook Business Manager to Telnyx via the standard [WhatsApp Embedded Signup](whatsapp-embedded-signup.md) flow.
- **Tech Provider** — An ISV or SaaS platform embeds Meta's WhatsApp onboarding into its own product and provisions WABAs on behalf of its end-customers.

Both paths converge on the same Telnyx WhatsApp APIs for messaging, templates, and (optionally) voice calling.

## WhatsApp Embedded Signup (Direct Customers)

The standard embedded signup flow connects a Facebook Business Manager to Telnyx and provisions a WABA through a browser-based workflow.

### Prerequisites

- An active Telnyx account with messaging enabled, a valid payment method, and admin permissions in the [Telnyx Portal](https://portal.telnyx.com).
- A Facebook Business Manager account at [business.facebook.com](https://business.facebook.com) with admin access and (recommended) completed business verification.
- Each phone number can only be associated with one Business Manager.

### Signup Flow

The signup process is a multi-step finite state machine that progresses through these states: `initiated` → `facebook_auth` → `waba_created` → `phone_registered` → `verified`.

1. **Initiate Embedded Signup** — In the Telnyx Portal, navigate to **Messaging → WhatsApp → Getting Started** and click **Connect WhatsApp Business**. Review the permissions and click **Begin Setup**. Telnyx creates a signup session in state `initiated` and generates a secure OAuth URL.
2. **Facebook OAuth Authorization** — The browser redirects to Facebook's consent screen. Grant **WhatsApp Business Management**, **Business Asset Management**, and **Webhook Management** permissions, then select the target Business Manager. The signup state advances to `facebook_auth`.
3. **WhatsApp Business Account Creation** — Telnyx automatically creates the WABA under the connected Business Manager, applies initial configuration (timezone, business category), and pre-configures webhook endpoints. The state advances to `waba_created`.
4. **Phone Number Registration** — Select a Telnyx-owned phone number with an active messaging profile. The number is submitted to Facebook for WhatsApp registration and the state advances to `phone_registered`. Bring-your-own-number (non-Telnyx numbers) is not yet supported through the portal flow.
5. **Phone Number Verification** — Facebook verifies the number via carrier validation, SMS, or voice call. Typical duration is 1–15 minutes; complex cases can take up to 24 hours. On success, the state advances to `verified` and the number becomes available for messaging.

### API Monitoring

Track signup progress programmatically:

```
curl -X GET "https://api.telnyx.com/v2/whatsapp/signup/{signup_id}/status" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Webhook events are also delivered as `whatsapp.signup.state_updated` payloads containing the `signup_id`, `state`, `previous_state`, `waba_id`, `phone_number`, and `occurred_at`.

### Troubleshooting

- **OAuth permission denied** — Verify admin access to Business Manager and that the account is not suspended.
- **WABA creation failed** — Complete Business Manager verification, resolve policy violations, or remove unused WABAs.
- **Phone number already registered** — Disconnect the number from the previous provider or use a different number.
- **Verification timeout or failure** — Confirm the number accepts incoming calls and SMS, and that the carrier is not blocking verification attempts.
- **Webhook configuration issues** — Verify webhook URL accessibility from Facebook servers and check signature verification.
- **Browser extensions blocking signup** — Ad blockers and privacy extensions can block Facebook/Meta domains. Disable them, allowlist `facebook.com` and `meta.com`, or use Chrome Incognito mode.
