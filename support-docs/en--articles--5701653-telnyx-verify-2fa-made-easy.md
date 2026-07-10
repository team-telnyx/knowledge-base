---
source_url: https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy
scraped: 2026-07-08
content_hash: b5250f9d420256a9198450965d469ae3090fda76daa52db2a7d633b806d8941d
---

Telnyx Verify: 2FA made easy | Telnyx Help Center

[Skip to main content](#main-content)

# Telnyx Verify: 2FA made easy

This article describes what is and how to get started with Telnyx Verify

Written by David

May 20, 2026

Table of contents

# Telnyx Verify: add verification codes to your application

Telnyx Verify helps you add phone-based user verification to your application. You can use it to send a one-time verification code to a user, then confirm the code they submit back to your app.

**Note:** Telnyx Verify is a developer product for building verification flows into your own application. It is separate from two-factor authentication used to protect your Telnyx Mission Control Portal account. If you need help with Portal account 2FA or TOTP, use the Portal 2FA/TOTP support article instead.

**Getting Started Tutorials:**

1. [Quickstart](https://developers.telnyx.com/docs/identity/verify/quickstart)
2. [DTMF Confirmation Verifications](https://developers.telnyx.com/docs/identity/verify/dtmf-confirm)
3. [Custom Templates for Telnyx Verify](https://developers.telnyx.com/docs/identity/verify/custom-templates)
4. [Receiving Webhooks for Telnyx Verify](https://developers.telnyx.com/docs/identity/verify/receiving-webhooks)
5. [Verify Security Best Practices](https://developers.telnyx.com/docs/identity/verify/security-best-practices)
6. [Rate Limiting and Fraud Prevention](https://developers.telnyx.com/docs/identity/verify/rate-limiting-fraud-prevention)

## Before you begin

You need:

* A Telnyx account.
* A Telnyx API key.
* A Verify Profile configured for the verification channel you want to use.
* An application or backend service that can call the Telnyx Verify API.

Keep your API key secure. Do not place it in client-side code, public repositories, or screenshots.

## Create a Verify Profile

A Verify Profile controls settings for your verification flow, such as the channel, message behavior, timeout, and optional webhook URLs.

You can create and manage Verify Profiles in the Telnyx Portal, or create them with the Verify API.

When creating a profile, choose the channel settings your application needs. This article covers the basic Verify flow for sending a verification and checking the submitted code. For current setup guidance, use the Telnyx Verify quickstart:

* Verify quickstart: <https://developers.telnyx.com/docs/identity/verify/quickstart/index.md>

## Send a verification code

After you have a Verify Profile, your application can trigger a verification request.

For SMS verification, the request must include the user’s phone number and the `verify_profile_id` for the Verify Profile you want to use.

Example:

```
curl -X POST "https://api.telnyx.com/v2/verifications/sms" \  
   --header "Content-Type: application/json" \  
   --header "Accept: application/json" \  
   --header "Authorization: Bearer $TELNYX_API_KEY" \  
   --data '{     "phone_number": "+13035551234",     "verify_profile_id": "YOUR_VERIFY_PROFILE_ID"   }'
```

You can also use other documented Verify channels, such as voice call or flash call, when they are enabled and configured for your use case. Use the current Verify API reference for channel-specific request formats.

## Verify the submitted code

Sending the code is only the first step. Your application must also verify the code the user enters.

Use the Verify API to submit the user’s phone number, the code, and the same `verify_profile_id` used when the verification was created.

Example:

```
curl -X POST "https://api.telnyx.com/v2/verifications/by_phone_number/%2B13035551234/actions/verify" \  
   --header "Content-Type: application/json" \  
   --header "Accept: application/json" \  
   --header "Authorization: Bearer $TELNYX_API_KEY" \  
   --data '{     "code": "123456",     "verify_profile_id": "YOUR_VERIFY_PROFILE_ID"   }'
```

If the code is valid and has not expired, the verification succeeds. If the code is incorrect or expired, prompt the user to try again or request a new code according to your application’s retry policy.

Reference: <https://developers.telnyx.com/api-reference/verify/verify-verification-code-by-phone-number.md>

## Optional: receive Verify webhooks

You can configure Verify webhooks if your application needs real-time status updates about verification events.

Add a webhook URL to your Verify Profile, then make sure your application is ready to receive and process Telnyx webhook requests.

Reference: <https://developers.telnyx.com/docs/identity/verify/receiving-webhooks>

## Production recommendations

Before using Verify in production:

* Rate limit verification requests by user, phone number, IP address, and session.
* Add CAPTCHA, authenticated-session checks, or other abuse controls before triggering a verification.
* Use destination allowlists when testing or when your use case allows a restricted destination set.
* Set reasonable code timeouts and retry limits.
* Monitor for unusual traffic patterns, SMS pumping, toll fraud, and repeated failed attempts.
* Avoid responses that reveal whether a phone number or account exists in your system.
* Review your Verify Profile spend controls and alerting before launch.

## Pricing

Current Verify pricing is available here:

<https://telnyx.com/pricing/verify-api>

## Need help?

If you have questions about configuring Telnyx Verify, contact Telnyx Support at [support@telnyx.com](mailto:support@telnyx.com) with your Verify Profile ID, the channel you are using, the request timestamp, and any error response returned by the API.

---

Related Articles

[Introducing the Verify API](https://support.telnyx.com/en/articles/5367966-introducing-the-verify-api)[Verified Numbers](https://support.telnyx.com/en/articles/6988813-verified-numbers)[Telnyx Networking on Ubuntu](https://support.telnyx.com/en/articles/8104274-telnyx-networking-on-ubuntu)[How to Verify Phone Numbers behind an IVR](https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr)[Bot-to-Bot Support API: Ask Telnyx Knowledge Agent](https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent)

Did this answer your question?

😞😐😃

Table of contents
