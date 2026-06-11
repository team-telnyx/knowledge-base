---
title: Telnyx Messaging Features
summary: Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky
  Sender, URL Shortening, Zapier integration, toll-free verification, and the full
  WhatsApp Business messaging workflow from embedded signup through template management
  and message sending.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
updated_at: 2026-06-11T10:38:44Z
---

# Telnyx Messaging Features

*Part 3 of 5 — see also: [Part 1](telnyx-messaging-features--part-1.md), [Part 2](telnyx-messaging-features--part-2.md), [Part 4](telnyx-messaging-features--part-4.md), [Part 5](telnyx-messaging-features--part-5.md)*

Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky Sender, URL Shortening, Zapier integration, toll-free verification, and the full WhatsApp Business messaging workflow from embedded signup through template management and message sending.

## WhatsApp Embedded Signup

WhatsApp Embedded Signup enables businesses to connect their Facebook Business Manager account to Telnyx and provision WhatsApp Business Account (WABA) resources through a browser-based workflow.

### Prerequisites

- Active Telnyx account with messaging enabled and valid payment method
- Facebook Business Manager account with admin access
- Business verification completed (recommended for production)

Each phone number can only be associated with one Business Manager.

### Step-by-Step Process

1. **Initiate**: In the Telnyx Portal, go to **Messaging → WhatsApp → Getting Started** and click **Connect WhatsApp Business**. A signup session is created with state `initiated`.

2. **Facebook OAuth**: Browser redirects to Facebook for authorization. Grant permissions for WhatsApp Business Management, Business Asset Management, and Webhook Management. State advances to `facebook_auth`.

3. **WABA Creation**: Telnyx automatically creates your WABA under the connected Business Manager. State advances to `waba_created`.

4. **Phone Number Registration**: Select a Telnyx number from your inventory. The number must have an active messaging profile and cannot be registered with another WhatsApp provider. State advances to `phone_registered`.

5. **Phone Number Verification**: Facebook verifies the number via carrier validation, SMS, or API check. Typical duration: 1–15 minutes; complex cases up to 24 hours. State advances to `verified`.

The embedded signup flow currently requires Telnyx-owned numbers. Bring-your-own-number is not yet supported through the portal.

### Monitoring and Webhooks

Check signup status via API:

```bash
curl -X GET "https://api.telnyx.com/v2/whatsapp/signup/{signup_id}/status" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Receive real-time signup progress via webhook event `whatsapp.signup.state_updated`.

### Common Issues

- **OAuth permission denied**: Ensure admin access to Business Manager
- **WABA creation failed**: Complete Business Manager verification, resolve policy violations
- **Phone number already registered**: Disconnect from previous provider or use a different number
- **Verification timeout**: Verify number accepts calls and SMS, try a different number
- **Browser extensions blocking signup**: Disable ad blockers and privacy extensions for `facebook.com` and `meta.com` domains, or use Chrome Incognito mode

## WhatsApp Tech Provider Embedded Signup

The Tech Provider flow is designed for ISVs and SaaS platforms that need to embed Meta's WhatsApp onboarding directly into their own portal. Unlike the standard embedded signup (for direct Telnyx customers), this flow lets partners manage multiple end-customers programmatically.

| Aspect | Tech Provider | Direct Customer |
|---|---|---|
| Who uses this | ISVs, SaaS platforms | Individual businesses |
| Onboarding | Embedded in your portal | Via Telnyx Portal or API |
| WABA ownership | End-customers own their WABAs | You own your WABA |
| Scale | Many WABAs under one integration | One WABA per integration |

### Prerequisites

- A Meta Business Account with admin access
- A Meta Tech Provider App approved with `whatsapp_business_messaging` and `whatsapp_business_management` permissions (Advanced Access for production)
- Completed Tech Provider onboarding in the Meta App Dashboard
- A Telnyx account with an API key

### Implementation Steps

**Step 1 — Create and configure your Meta Tech Provider App**: Create a Business-type app in the [Meta App Dashboard](https://developers.facebook.com/apps/), add the WhatsApp product, request required permissions, complete Tech Provider onboarding, and submit for App Review.

**Step 2 — Link your Meta App to Telnyx**: Switch the app to Live mode, then contact Telnyx support with your Meta App ID and business name. Within 1–2 business days, accept the partner invitation email from Meta. After accepting, you can switch back to Development mode for testing.

**Step 3 — Implement the frontend embedded signup**: Include the Facebook SDK, trigger the signup with `FB.login()` using your `config_id` and `response_type: 'code'`, exchange the authorization code for an access token via Meta's OAuth endpoint, and extract the `waba_id` and `phone_number_id`.

**Step 4 — Register the WABA with Telnyx**: Once you have the WABA ID and phone number ID, register with Telnyx:

```bash
curl -X POST https://api.telnyx.com/v2/whatsapp/business_accounts/tech_provider \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "waba_id": "123456789012345",
    "phone_number_id": "987654321098765",
    "app_id": "123456789012345",
    "customer_id": "acme-corp-42"
  }'
```

Parameters: `waba_id` (required), `phone_number_id` (required), `app_id` (required), `customer_id` (optional identifier). After successful registration, the WABA is linked to Telnyx's messaging infrastructure and the number is ready for messaging.

### Troubleshooting

- **No partner invitation email**: Verify app was in Live mode when you contacted Telnyx; check spam folders
- **App Review denied**: Address Meta's rejection reasons, provide clearer documentation, resubmit
- **FB.login() doesn't open dialog**: Confirm SDK is loaded, check `config_id`, ensure permissions are granted
- **401 Unauthorized from Telnyx API**: Verify API key is valid and not expired
- **No WABA ID returned**: Ensure `response_type` includes `code` and `override_default_response_type` is `true`
