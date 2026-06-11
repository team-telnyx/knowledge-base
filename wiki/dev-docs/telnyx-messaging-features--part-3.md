---
title: Telnyx Messaging Features
summary: Covers Telnyx messaging capabilities including MMS SMIL templates, Sticky
  Sender, URL Shortening, Zapier integration, toll-free verification, and the full
  WhatsApp Business messaging workflow from embedded signup through template management
  and message sending.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
  content_hash: d29aa01a72d9457e2c15bca36d1a114fad0d8a8fd2d7b721484dbeb7d7ea9663
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
  content_hash: b60693e817349ec8df4be29ac868e8661434934e8c3047b7acc28151d7d666ae
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
  content_hash: 4c488d1b1e1c401b24857bbee9b2dc380feeb3307e7bce07ecaa412fe56d304f
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
  content_hash: aad83743cb42ebbc89f6978b6f626af75781bd0d86f1dc76eec2c92463a1daa1
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
  content_hash: 4252b4aba3308d22e312c4bfc31ff2bf8b9dad3363bc6fa0d6dd8cc1765f4379
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
  content_hash: 73f55d4531a2ff98fb6c9a7234dfb34e6b4429f9a1fdbc66b6c62d286cb29463
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
  content_hash: 2ed927e07af5e37713ddd6b340998cd8842b6303ef28e2428218537475463b8c
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
  content_hash: bb93e5d911b134f7064cd7997b82d901cca70eae5ee880c925434e16bb05f284
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
  content_hash: ed0efe6efb4a082f13f54662244ee901249886ad4eed11780a77d535efca8e89
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
  content_hash: abd0f4264c0b578171e98a4800bc241b283f1640a411eb55d283297c41637ae9
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
  content_hash: 6c916c387118b87a1258ad874d5461c0bf493edb141be63764cac4cb36a2cdcb
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
