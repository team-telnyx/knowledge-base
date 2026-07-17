---
source_url: https://support.telnyx.com/en/articles/3739748-2fa-totp-setup
title: "2FA / TOTP Setup"
description: "New 2FA & TOTP Process Guide for Mission Control Portal: Key info here. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 6fc57233fe41c25a1e41edf502ed3f282e4f549cf86a796840b46d20f4fc898e
---







# 2FA / TOTP Setup

New 2FA & TOTP Process Guide for Mission Control Portal: Key info here. See Telnyx guidance and requirements.




## Set up two-factor authentication (2FA) in Mission Control Portal

Two-factor authentication (2FA) adds an extra step when you sign in to Mission Control Portal. After entering your password, you will also enter a temporary verification code from your selected 2FA method.

This article explains how to set up 2FA for your Telnyx Portal account. It is separate from **Telnyx Verify**, which is a Telnyx product used to add verification codes to your own applications.

## Before you begin

You can set up 2FA from the **Account** section of Mission Control Portal, under the security settings.

Before enabling 2FA:

* Choose the method you want to use: **Authenticator app (TOTP)** or **SMS/Call**.
* Make sure you have access to the phone or authenticator app you plan to use.
* Be ready to save your backup codes after setup. Backup codes are shown once and each code can only be used once.
* Do not share verification codes, backup codes, QR codes, or authenticator setup details with anyone.

## Choose a 2FA method

## Authenticator app / TOTP

TOTP stands for **Time-Based One-Time Password**. A TOTP authenticator app generates a short code that changes regularly. When you sign in, you enter the current code from the app.

Use TOTP when you can. It is usually the best option because it does not depend on SMS or voice-call delivery.

Telnyx TOTP works with standard authenticator apps, including Google Authenticator, Microsoft Authenticator, 1Password, and other standards-based TOTP apps.

## SMS/Call

The SMS/Call option sends a verification code to a phone number by text message or voice call.

Use SMS/Call if an authenticator app is not available or if it is the best option for your workflow. Code delivery can depend on your phone, carrier, network coverage, roaming, and retry limits.

## Set up TOTP with an authenticator app

1. Sign in to Mission Control Portal.
2. Go to **Account** and open the security settings.
3. Enable **Two-Factor Authentication**.
4. Select the **TOTP** or authenticator-app option.
5. Open your authenticator app and scan the QR code shown in Portal.
6. Your authenticator app will show a temporary verification code.
7. Enter that code in Mission Control Portal to activate TOTP.
8. Save the backup codes shown after setup and store them securely.

The next time you sign in, enter the current code from your authenticator app when prompted.

If your app cannot scan the QR code, check whether Mission Control Portal provides a manual setup option. If a manual setup key is shown, treat it like a password and do not share it.

## Set up SMS/Call 2FA

1. Sign in to Mission Control Portal.
2. Go to **Account** and open the security settings.
3. Enable **Two-Factor Authentication**.
4. Select the **SMS/Call** option.
5. Enter a phone number that can receive SMS messages or voice calls.
6. Choose **SMS** or **Call** to receive a verification code.
7. Enter the code in Mission Control Portal to activate 2FA.
8. Save the backup codes shown after setup and store them securely.

The next time you sign in, request a code by SMS or call and enter the code when prompted.

## Backup codes and recovery

After 2FA is enabled, Mission Control Portal may show backup codes. Save them immediately.

Important backup-code rules:

* Backup codes are displayed once.
* Each backup code can only be used once.
* Store backup codes somewhere secure and separate from the device you use for 2FA.
* Do not share backup codes with anyone.

If you lose access to your authenticator app, phone number, or backup codes, contact Telnyx Support at [support@telnyx.com](mailto:support@telnyx.com) for help with account recovery. Support will guide you through the appropriate recovery process.

## Changing phones or authenticator apps

If you are replacing a phone or changing authenticator apps, update your 2FA setup before you lose access to the old device.

Recommended steps:

* Confirm you still have valid backup codes.
* If using TOTP, transfer or re-add the Telnyx entry in your new authenticator app before removing it from the old device.
* If using SMS/Call, update the phone number while you can still receive codes on the existing number.
* After making changes, test your next Portal sign-in before retiring the old device.

## SSO/SAML accounts

If your organization uses SSO/SAML to sign in to Mission Control Portal, multi-factor authentication may be managed by your organization’s identity provider instead of Telnyx Portal 2FA settings.

Follow your organization’s identity-provider policy for SSO/SAML MFA requirements.

## API access note

Mission Control Portal 2FA protects interactive Portal sign-in. It does not configure Telnyx Verify, and it does not replace API key security.

Protect your API keys separately. Store them securely, rotate them when needed, and remove keys that are no longer in use.

## Troubleshooting

## My authenticator code is not working

* Make sure you are using the correct Telnyx entry in your authenticator app.
* Use the current code. TOTP codes expire quickly.
* Confirm the date and time on your device are set correctly, preferably using automatic time settings.
* If you still cannot sign in, use a backup code if you have one.

## I did not receive an SMS or call

* Confirm the phone can receive SMS messages or voice calls.
* Wait before requesting another code to avoid retry or rate limits.
* If SMS/Call delivery is unreliable and you can still access your account, consider switching to TOTP.

## I see a request-limit or login-attempt error

If you see an error such as **“You have exceeded the maximum number of allowed requests”** or **“You have exceeded the number of login attempts allowed”**, wait before trying again. If access is urgent or you still cannot sign in, contact [support@telnyx.com](mailto:support@telnyx.com).

## I lost my 2FA device and do not have backup codes

Contact Telnyx Support at [support@telnyx.com](mailto:support@telnyx.com)for account recovery assistance.

---

Related Articles

[E911 Setup Guide](https://support.telnyx.com/en/articles/1130683-e911-setup-guide)[How to setup your Account Settings](https://support.telnyx.com/en/articles/4280610-how-to-setup-your-account-settings)[Introducing the Verify API](https://support.telnyx.com/en/articles/5367966-introducing-the-verify-api)[Telnyx Verify: 2FA made easy](https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy)[Zoiper 5 Pro: Telnyx Setup](https://support.telnyx.com/en/articles/5717957-zoiper-5-pro-telnyx-setup)

Did this answer your question?

😞😐😃
