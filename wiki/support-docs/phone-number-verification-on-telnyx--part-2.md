---
title: Phone Number Verification on Telnyx
summary: 'Telnyx offers multiple verification features: Verified Numbers let you confirm
  ownership of non-Telnyx phone numbers so they can be used as Caller ID on outbound
  calls, the Verify API enables you to add phone-based verification codes to your
  own applications, and Portal 2FA/TOTP protects your Mission Control Portal account
  login.'
sources:
- url: https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr
  content_hash: e9a69a9acd1ccab089c3a1d6138e81c2a73821908ba8feb1a3a75c4c4bd8a245
- url: https://support.telnyx.com/en/articles/13854980-beta-how-to-verify-phone-numbers-using-dtmf-press-1-to-verify
  content_hash: 9aabcc488a22709ea2cc80cec9e9d4661723bcc82e09aa2daa0820b199806657
- url: https://support.telnyx.com/en/articles/3739748-2fa-totp-setup
  content_hash: f113a7ed6e199ae37151faba0b055d460f53044b520705c62176d963dd581630
- url: https://support.telnyx.com/en/articles/5367966-introducing-the-verify-api
  content_hash: cee0692d25130887bdedfecbb3e4a5fba0d8d0af290f222e937ccc629d3e101c
- url: https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy
  content_hash: 6694db0932af7533a5e86b20846863796f969a8fe5f2b08b2e6aa4b05bbcfdaf
- url: https://support.telnyx.com/en/articles/6790265-verified-numbers-faq
  content_hash: a4a018a51997db5c535a2208f7e7d9d27fe35f91d8c61328f5e4d0c7793ee5a8
- url: https://support.telnyx.com/en/articles/6988813-verified-numbers
  content_hash: a5b09b58059e19c33e4972765182cbe21611220ee85d6cf2fc67e6882b4f4f68
updated_at: 2026-06-11T11:43:04Z
---

# Phone Number Verification on Telnyx

*Part 2 of 2 — see also: [Part 1](phone-number-verification-on-telnyx--part-1.md)*

Telnyx offers multiple verification features: Verified Numbers let you confirm ownership of non-Telnyx phone numbers so they can be used as Caller ID on outbound calls, the Verify API enables you to add phone-based verification codes to your own applications, and Portal 2FA/TOTP protects your Mission Control Portal account login.

## Telnyx Verify API

Telnyx Verify is a developer product for adding phone-based user verification to your own application. It is separate from both Verified Numbers (Caller ID ownership) and Portal 2FA (account login protection).

### Create a Verify Profile

A Verify Profile controls settings for your verification flow, including channel, message behavior, timeout, and optional webhook URLs. Create one in the Mission Control Portal under **Verify → New Verify Profile**, or via the API.

### Send a Verification Code

After creating a profile, trigger a verification request. For SMS:

```
curl -X POST "https://api.telnyx.com/v2/verifications/sms" \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer $TELNYX_API_KEY" \
  --data '{
    "phone_number": "+13035551234",
    "verify_profile_id": "YOUR_VERIFY_PROFILE_ID"
  }'
```

Other channels include voice call, flash call, and PSD2-specific codes. You can also specify the language for voice or SMS delivery.

### Verify the Submitted Code

Your application must verify the code the user enters:

```
curl -X POST "https://api.telnyx.com/v2/verifications/by_phone_number/%2B13035551234/actions/verify" \
  --header "Content-Type: application/json" \
  --header "Accept: application/json" \
  --header "Authorization: Bearer $TELNYX_API_KEY" \
  --data '{
    "code": "123456",
    "verify_profile_id": "YOUR_VERIFY_PROFILE_ID"
  }'
```

If the code is valid and has not expired, verification succeeds. If incorrect or expired, prompt the user to try again or request a new code.

### Verify Webhooks

Add a webhook URL to your Verify Profile to receive real-time status updates about verification events. See the [receiving webhooks documentation](https://developers.telnyx.com/docs/identity/verify/receiving-webhooks).

### Production Recommendations

- Rate limit verification requests by user, phone number, IP address, and session.
- Add CAPTCHA or authenticated-session checks before triggering a verification.
- Use destination allowlists during testing.
- Set reasonable code timeouts and retry limits.
- Monitor for unusual traffic patterns, SMS pumping, toll fraud, and repeated failed attempts.
- Avoid responses that reveal whether a phone number or account exists.
- Review Verify Profile spend controls and alerting before launch.

For tutorials and best practices, see the [Verify quickstart](https://developers.telnyx.com/docs/identity/verify/quickstart).

## Mission Control Portal 2FA/TOTP

Two-factor authentication protects your Mission Control Portal account login. It is separate from both the Verify API and Verified Numbers.

### Authenticator App (TOTP)

TOTP (Time-Based One-Time Password) is the recommended method. It works with standard authenticator apps such as Google Authenticator, Microsoft Authenticator, and 1Password. It does not depend on SMS or voice-call delivery.

**Setup:**

1. Go to **Account → Security Settings** in the Portal.
2. Enable **Two-Factor Authentication** and select **TOTP**.
3. Scan the QR code with your authenticator app.
4. Enter the temporary code shown by the app to activate TOTP.
5. Save the backup codes shown after setup.

### SMS/Call

If an authenticator app is not available, you can receive a verification code by SMS or voice call. Code delivery depends on your carrier, network coverage, roaming, and retry limits.

**Setup:**

1. Go to **Account → Security Settings** in the Portal.
2. Enable **Two-Factor Authentication** and select **SMS/Call**.
3. Enter a phone number and choose SMS or Call.
4. Enter the received code to activate 2FA.
5. Save the backup codes shown after setup.

### Backup Codes and Recovery

- Backup codes are displayed once; each can be used only once.
- Store them securely, separate from the device you use for 2FA.
- Do not share backup codes or verification codes with anyone.
- If you lose access to your 2FA device and backup codes, contact [support@telnyx.com](mailto:support@telnyx.com) for account recovery.

### Changing Devices

Before replacing a phone or switching authenticator apps, update your 2FA setup while you still have access to the old device. Transfer or re-add the Telnyx entry in the new app, then test your next Portal sign-in before retiring the old device.

### SSO/SAML Accounts

If your organization uses SSO/SAML, multi-factor authentication may be managed by your identity provider rather than Telnyx Portal 2FA settings.

### API Key Security

Portal 2FA protects interactive sign-in only. It does not replace API key security. Store API keys securely, rotate them when needed, and remove unused keys.

## Pricing

### Verified Numbers

Pay only for successful verifications, plus a channel-based delivery charge:

| Method | Cost |
|---|---|
| SMS | $0.03 per successful verification + [SMS API pricing](https://telnyx.com/pricing/messaging) |
| Voice Call | $0.03 per successful verification + [Voice API pricing](https://telnyx.com/pricing/call-control) |
| Flash Call | $0.03 per successful verification + [Flash pricing](https://telnyx.com/pricing/call-control) |

### Telnyx Verify API

See current [Verify API pricing](https://telnyx.com/pricing/verify-api).

## Troubleshooting

| Issue | Solution |
|---|---|
| Verification call not received | Verify the phone number is correct and can receive calls |
| User didn't press 1 in time | Retry the verification call |
| Rate limit exceeded | Add delays between requests |
| Invalid phone number format | Ensure numbers are in E.164 format (e.g., `+15412345678`) |
| Authenticator code not working | Confirm you are using the correct entry, use the current code, and check your device date/time settings |
| SMS/Call code not received | Confirm the phone can receive messages/calls, wait before retrying to avoid rate limits |
| Login attempt limit exceeded | Wait before trying again; if urgent, contact [support@telnyx.com](mailto:support@telnyx.com) |
| Lost 2FA device and no backup codes | Contact [support@telnyx.com](mailto:support@telnyx.com) for account recovery |
