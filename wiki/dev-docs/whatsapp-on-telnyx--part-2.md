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

*Part 2 of 4 — see also: [Part 1](whatsapp-on-telnyx--part-1.md), [Part 3](whatsapp-on-telnyx--part-3.md), [Part 4](whatsapp-on-telnyx--part-4.md)*

Telnyx provides a complete WhatsApp Business Platform integration covering embedded signup (for direct customers and Tech Providers), WhatsApp Business Calling, and message template management. This page consolidates the onboarding flows, API endpoints, voice calling setup, and template lifecycle into a single reference.

## Tech Provider Embedded Signup

The Tech Provider flow lets ISVs and SaaS platforms embed Meta's WhatsApp onboarding directly into their own portal. End-customers create a WABA, claim a phone number, and start messaging without leaving the partner's application.

### Tech Provider vs. Direct Customer

| | Tech Provider | Direct Customer |
| --- | --- | --- |
| **Who uses this?** | ISVs, SaaS platforms, resellers | Individual businesses |
| **Onboarding** | Embedded in your portal | Via Telnyx portal or API |
| **WABA ownership** | Your end-customers own their WABAs | You own your WABA |
| **API calls** | You call Telnyx on behalf of customers | You call Telnyx directly |
| **Scale** | Many WABAs under one integration | One WABA per integration |

### Prerequisites

- A [Meta Business Account](https://business.facebook.com/) with admin access.
- A **Meta Tech Provider App** approved by Meta with `whatsapp_business_messaging` and `whatsapp_business_management` permissions (both require **Advanced Access** for production).
- Tech Provider onboarding completed in the [Meta App Dashboard](https://developers.facebook.com/apps/).
- A [Telnyx account](https://telnyx.com/sign-up) with an API key.

### Step 1 — Create and Configure Your Meta Tech Provider App

1. Create a new app in the [Meta App Dashboard](https://developers.facebook.com/apps/) with type **Business**.
2. Add the **WhatsApp** product to your app.
3. Under **App Review > Permissions and Features**, request `whatsapp_business_messaging` and `whatsapp_business_management`.
4. Complete Meta's [Tech Provider onboarding guide](https://developers.facebook.com/docs/development/create-an-app/business-onboarding), including business verification and agreement to Meta's Tech Provider terms.
5. Submit for App Review. While waiting, you can test in **Development Mode**; production use requires **Live Mode** and Advanced Access.

### Step 2 — Link Your Meta App to Telnyx

1. Switch your app to **Live mode** in the Meta App Dashboard.
2. Contact your Telnyx representative or [support](https://support.telnyx.com) with your **Meta App ID** and **business name**.
3. Within 1–2 business days, accept the partner invitation email from Meta.
4. After accepting, you can switch back to **Development mode** for testing — the link persists regardless of app mode.

### Step 3 — Choose Your Integration Path

| | Option A: Hosted signup (recommended) | Option B: Custom integration |
| --- | --- | --- |
| **Who it's for** | Most Tech Providers — fastest to ship | ISVs who want full control over the UX |
| **What you build** | One API call to generate a shareable URL | Facebook SDK integration in your own frontend |
| **Signup UI** | Telnyx-hosted page at `acct.fyi` | Embedded directly in your portal |
| **End-customer experience** | Clicks a link → completes Meta signup → done | Clicks a button in your app → Meta popup → you handle the response |
| **Backend code exchange** | Telnyx handles it automatically | You exchange the code with Meta's Graph API |
| **WABA registration** | Telnyx handles it automatically | You call Telnyx's registration API |

#### Option A — Hosted Signup

Generate a JWT-authenticated onboarding URL via API. The URL is valid for up to 3 days (default 24 hours):

```
curl -X POST https://api.telnyx.com/v2/whatsapp/hosted_signups \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "app_id": "123456789012345"
  }'
```

The response includes a `url` (share with the end-customer), a `jwt`, an `expires_at`, and a session `id`. When the customer visits the URL, Telnyx validates the JWT, renders a signup page, and on completion automatically handles code exchange, webhook subscription, credit line sharing, and phone number registration.

Poll signup status with `GET /v2/whatsapp/signup/{session_id}/status`.

#### Option B — Custom Integration

1. Include the Facebook JavaScript SDK in your web app and initialize it with your `appId` and API version (e.g., `v19.0`).
2. Trigger the embedded signup flow by calling `FB.login()` with your WhatsApp Business Configuration `config_id`, `response_type: 'code'`, `override_default_response_type: true`, and the appropriate `extras` (`setup`, `featureType`, `sessionInfoVersion: '3'`).
3. Exchange the returned authorization code with Meta's Graph API at `https://graph.facebook.com/v19.0/oauth/access_token` using your `client_id`, `client_secret`, and `code` to obtain an access token.
4. Extract the `waba_id` and `phone_number_id` from the embedded signup response.
5. Register the WABA with Telnyx:

```
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

After registration, the credit line is applied to your Telnyx billing account, the WABA is linked to Telnyx's messaging infrastructure, and the phone number is ready for messaging.

### Troubleshooting

- **No partner invitation email** — Confirm the app was in Live mode when you contacted Telnyx, check spam folders, and verify the Meta Business account email.
- **App Review denied** — Review rejection reasons, improve documentation and screencast, and resubmit.
- **`FB.login()` doesn't open the dialog** — Confirm the SDK is loaded, the `config_id` is correct, and the required permissions are granted.
- **401 Unauthorized from Telnyx API** — Verify the API key is valid and the `Authorization: Bearer` header is included.
- **No WABA ID returned** — Ensure `response_type` includes `code`, `override_default_response_type` is `true`, and the user completed all signup steps.
- **Hosted URL shows 'Missing Signup Token'** — Use the full URL including the `?token=` query parameter and ensure the JWT hasn't expired (max 3 days).
- **Verification code never arrives** — Verify the phone number is correct, not already registered, and try voice call verification instead of SMS.
