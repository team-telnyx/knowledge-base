---
title: Telnyx Account Security, Verification & Identity
summary: This page consolidates Telnyx guidance on account verification (legacy Level
  1/Level 2 and the newer Trial-Paid-Verified-Enterprise framework), Mission Control
  Portal two-factor authentication, the Telnyx Verify API for embedding 2FA in your
  own applications, fraud prevention and account compromise recovery, blocked account
  guidelines, refunds, TLS/SSL certificate handling, and webhook certificate authority
  errors.
sources:
- url: https://support.telnyx.com/en/articles/1130595-account-verification
- url: https://support.telnyx.com/en/articles/1130639-what-is-your-refund-policy
- url: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
- url: https://support.telnyx.com/en/articles/3610162-prevent-telnyx-account-fraud
- url: https://support.telnyx.com/en/articles/3739748-2fa-totp-setup
- url: https://support.telnyx.com/en/articles/5367966-introducing-the-verify-api
- url: https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy
- url: https://support.telnyx.com/en/articles/7020727-account-compromise-what-to-do
- url: https://support.telnyx.com/en/articles/7915224-blocked-account-guidelines
- url: https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com
- url: https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error
- url: https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status
- url: https://support.telnyx.com/en/collections/3968260-telnyx-identity-verification-tools
updated_at: 2026-08-05T13:26:47Z
---

# Telnyx Account Security, Verification & Identity

*Part 3 of 5 — see also: [Part 1](telnyx-account-security-verification-identity--part-1.md), [Part 2](telnyx-account-security-verification-identity--part-2.md), [Part 4](telnyx-account-security-verification-identity--part-4.md), [Part 5](telnyx-account-security-verification-identity--part-5.md)*

This page consolidates Telnyx guidance on account verification (legacy Level 1/Level 2 and the newer Trial-Paid-Verified-Enterprise framework), Mission Control Portal two-factor authentication, the Telnyx Verify API for embedding 2FA in your own applications, fraud prevention and account compromise recovery, blocked account guidelines, refunds, TLS/SSL certificate handling, and webhook certificate authority errors.

## Telnyx Verify API

Telnyx Verify helps you add phone-based user verification to your own application. You can use it to send a one-time verification code to a user, then confirm the code they submit back to your app. It is a developer product for building verification flows into your own application and is separate from two-factor authentication used to protect your Telnyx Mission Control Portal account.

### Before You Begin

You need:

- A Telnyx account
- A Telnyx API key
- A Verify Profile configured for the verification channel you want to use
- An application or backend service that can call the Telnyx Verify API

Keep your API key secure. Do not place it in client-side code, public repositories, or screenshots.

### Create a Verify Profile

A Verify Profile controls settings for your verification flow, such as the channel, message behavior, timeout, and optional webhook URLs. You can create and manage Verify Profiles in the Telnyx Portal, or create them with the Verify API. When creating a profile, choose the channel settings your application needs.

### Send a Verification Code

After you have a Verify Profile, your application can trigger a verification request. For SMS verification, the request must include the user's phone number and the `verify_profile_id` for the Verify Profile you want to use.

Example:

```
curl -X POST "https://api.telnyx.com/v2/verifications/sms" \
   --header "Content-Type: application/json" \
   --header "Accept: application/json" \
   --header "Authorization: Bearer $TELNYX_API_KEY" \
   --data '{     "phone_number": "+13035551234",     "verify_profile_id": "YOUR_VERIFY_PROFILE_ID"   }'
```

You can also use other documented Verify channels, such as voice call or flash call, when they are enabled and configured for your use case.

### Verify the Submitted Code

Sending the code is only the first step. Your application must also verify the code the user enters. Use the Verify API to submit the user's phone number, the code, and the same `verify_profile_id` used when the verification was created.

Example:

```
curl -X POST "https://api.telnyx.com/v2/verifications/by_phone_number/%2B13035551234/actions/verify" \
   --header "Content-Type: application/json" \
   --header "Accept: application/json" \
   --header "Authorization: Bearer $TELNYX_API_KEY" \
   --data '{     "code": "123456",     "verify_profile_id": "YOUR_VERIFY_PROFILE_ID"   }'
```

If the code is valid and has not expired, the verification succeeds. If the code is incorrect or expired, prompt the user to try again or request a new code according to your application's retry policy.

### Optional: Receive Verify Webhooks

You can configure Verify webhooks if your application needs real-time status updates about verification events. Add a webhook URL to your Verify Profile, then make sure your application is ready to receive and process Telnyx webhook requests.

### Production Recommendations

Before using Verify in production:

- Rate limit verification requests by user, phone number, IP address, and session
- Add CAPTCHA, authenticated-session checks, or other abuse controls before triggering a verification
- Use destination allowlists when testing or when your use case allows a restricted destination set
- Set reasonable code timeouts and retry limits
- Monitor for unusual traffic patterns, SMS pumping, toll fraud, and repeated failed attempts
- Avoid responses that reveal whether a phone number or account exists in your system
- Review your Verify Profile spend controls and alerting before launch

### Verify API Channels and Features

The Verify API supports delivering verification codes through multiple channels:

- SMS
- Voice call
- Flash call
- PSD2-specific verification codes
- Specifying the language for verification codes delivered through voice call or SMS

Users who have already integrated with the API should read the release notes carefully and plan for any changes.

### Pricing

Current Verify pricing is available at [telnyx.com/pricing/verify-api](https://telnyx.com/pricing/verify-api).

### Need Help?

If you have questions about configuring Telnyx Verify, contact Telnyx Support at [support@telnyx.com](mailto:support@telnyx.com) with your Verify Profile ID, the channel you are using, the request timestamp, and any error response returned by the API.

## Preventing Account Fraud

Telnyx recommends starting with the basics to protect your account:

1. Secure your account passwords.
2. Review access logs on a regular basis.
3. Restrict web access to your PBX/VoIP system.

On the Mission Control Portal, you can apply channel limit settings on your [connections](https://portal.telnyx.com/#/voice/connections) and [outbound profiles](https://portal.telnyx.com/#/outbound-profiles) settings.

### Connections

You can use a [Tech Prefix](https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix) on your connection in order to segment traffic if you use the same IP address for multiple clients. Using multiple outbound profiles for each connection can allow you to have more granular control for the subsequent outbound profile settings.

### Outbound Profiles

Outbound profiles include a **max daily spend limit**, a **max destination rate limit**, the ability to **blacklist certain countries**, and a setting for how many **concurrent calls** can be active at any time. For international service plans, you can allow or disallow regions or certain countries within those regions.

### Best Practices to Secure Your Account

- **Update password** — Update your Telnyx account password every 30, 60, or 90 days to secure your account in case of password leaks and to restrict access for former employees.
- **Rotate API keys** — Delete old keys and generate new ones if you are extensively using Telnyx endpoints. Implement an API key update policy where the old key is purged and a new key is generated.
- **Update SIP connection credentials** — Update connection credentials similarly to periodic portal password updates. This can be automated by updating the connection settings via API requests.
- **Review notification settings for suspicious outbound voice traffic** — If Telnyx detects unusual outbound voice traffic patterns, you will receive an email notification immediately. Patterns monitored include multiple calls concurrently or in quick succession to the same destination prefix, multiple ongoing calls to the same high-cost destination, and multiple long-lived concurrent calls. Make sure your notifications settings are correctly set up so they are sent to the appropriate email addresses.
- **Set 2FA authentication** — 2FA neutralizes the risks associated with compromised passwords. Enable 2FA on your account at [portal.telnyx.com/#/account/my-account/security](https://portal.telnyx.com/#/account/my-account/security).

### Reporting Abuse

You can report abuse via the [Telnyx report abuse form](https://telnyx.com/report-abuse), by emailing [abuse@telnyx.com](mailto:abuse@telnyx.com), or through the chat widget.

### Spoofing, Robocalling, and STIR/SHAKEN

For more on these topics, see:

- [What is spoofing and why does it matter?](https://telnyx.com/resources/what-is-spoofing-and-why-does-it-matter)
- [STIR/SHAKEN explained](https://telnyx.com/resources/shaken-stir-explained)
