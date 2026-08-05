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

*Part 2 of 5 — see also: [Part 1](telnyx-account-security-verification-identity--part-1.md), [Part 3](telnyx-account-security-verification-identity--part-3.md), [Part 4](telnyx-account-security-verification-identity--part-4.md), [Part 5](telnyx-account-security-verification-identity--part-5.md)*

This page consolidates Telnyx guidance on account verification (legacy Level 1/Level 2 and the newer Trial-Paid-Verified-Enterprise framework), Mission Control Portal two-factor authentication, the Telnyx Verify API for embedding 2FA in your own applications, fraud prevention and account compromise recovery, blocked account guidelines, refunds, TLS/SSL certificate handling, and webhook certificate authority errors.

## Mission Control Portal 2FA / TOTP

Two-factor authentication (2FA) adds an extra step when you sign in to Mission Control Portal. After entering your password, you also enter a temporary verification code from your selected 2FA method. This is separate from [Telnyx Verify](telnyx-verify.md), which is a developer product for adding verification codes to your own applications.

### Before You Begin

You can set up 2FA from the **Account** section of Mission Control Portal, under the security settings. Before enabling 2FA:

- Choose the method you want to use: **Authenticator app (TOTP)** or **SMS/Call**
- Make sure you have access to the phone or authenticator app you plan to use
- Be ready to save your backup codes after setup (they are shown once and each can only be used once)
- Do not share verification codes, backup codes, QR codes, or authenticator setup details with anyone

### Choosing a 2FA Method

**Authenticator app / TOTP** — TOTP (Time-Based One-Time Password) generates a short code that changes regularly. Use TOTP when you can; it does not depend on SMS or voice-call delivery. Telnyx TOTP works with standard authenticator apps including Google Authenticator, Microsoft Authenticator, 1Password, and other standards-based TOTP apps.

**SMS/Call** — Sends a verification code to a phone number by text message or voice call. Use this if an authenticator app is not available. Code delivery can depend on your phone, carrier, network coverage, roaming, and retry limits.

### Setting Up TOTP with an Authenticator App

1. Sign in to Mission Control Portal.
2. Go to **Account** and open the security settings.
3. Enable **Two-Factor Authentication**.
4. Select the **TOTP** or authenticator-app option.
5. Open your authenticator app and scan the QR code shown in Portal.
6. Enter the temporary verification code shown in your authenticator app.
7. Save the backup codes shown after setup and store them securely.

If your app cannot scan the QR code, check whether Mission Control Portal provides a manual setup option. If a manual setup key is shown, treat it like a password and do not share it.

### Setting Up SMS/Call 2FA

1. Sign in to Mission Control Portal.
2. Go to **Account** and open the security settings.
3. Enable **Two-Factor Authentication**.
4. Select the **SMS/Call** option.
5. Enter a phone number that can receive SMS messages or voice calls.
6. Choose **SMS** or **Call** to receive a verification code.
7. Enter the code in Mission Control Portal to activate 2FA.
8. Save the backup codes shown after setup and store them securely.

### Backup Codes and Recovery

After 2FA is enabled, Mission Control Portal may show backup codes. Save them immediately. Important rules:

- Backup codes are displayed once
- Each backup code can only be used once
- Store backup codes somewhere secure and separate from the device you use for 2FA
- Do not share backup codes with anyone

If you lose access to your authenticator app, phone number, or backup codes, contact Telnyx Support at [support@telnyx.com](mailto:support@telnyx.com) for help with account recovery.

### Changing Phones or Authenticator Apps

If you are replacing a phone or changing authenticator apps, update your 2FA setup before you lose access to the old device:

- Confirm you still have valid backup codes
- If using TOTP, transfer or re-add the Telnyx entry in your new authenticator app before removing it from the old device
- If using SMS/Call, update the phone number while you can still receive codes on the existing number
- After making changes, test your next Portal sign-in before retiring the old device

### SSO/SAML Accounts

If your organization uses SSO/SAML to sign in to Mission Control Portal, multi-factor authentication may be managed by your organization's identity provider instead of Telnyx Portal 2FA settings. Follow your organization's identity-provider policy for SSO/SAML MFA requirements.

### API Access Note

Mission Control Portal 2FA protects interactive Portal sign-in. It does not configure Telnyx Verify, and it does not replace API key security. Protect your API keys separately: store them securely, rotate them when needed, and remove keys that are no longer in use.

### Troubleshooting

**My authenticator code is not working**

- Make sure you are using the correct Telnyx entry in your authenticator app
- Use the current code; TOTP codes expire quickly
- Confirm the date and time on your device are set correctly, preferably using automatic time settings
- If you still cannot sign in, use a backup code if you have one

**I did not receive an SMS or call**

- Confirm the phone can receive SMS messages or voice calls
- Wait before requesting another code to avoid retry or rate limits
- If SMS/Call delivery is unreliable and you can still access your account, consider switching to TOTP

**I see a request-limit or login-attempt error**

If you see an error such as "You have exceeded the maximum number of allowed requests" or "You have exceeded the number of login attempts allowed", wait before trying again. If access is urgent or you still cannot sign in, contact [support@telnyx.com](mailto:support@telnyx.com).

**I lost my 2FA device and do not have backup codes**

Contact Telnyx Support at [support@telnyx.com](mailto:support@telnyx.com) for account recovery assistance.
