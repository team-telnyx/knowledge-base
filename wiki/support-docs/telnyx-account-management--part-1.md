---
title: Telnyx Account Management
summary: This page covers Telnyx account management topics including verification
  frameworks (legacy Level 1/Level 2 and TPVE), account settings configuration, two-factor
  authentication setup, API key management, the Telnyx Verify API for application-based
  verification, fraud prevention best practices, account compromise response, blocked
  account guidelines, account cancellation, refund policy, and privacy policy.
sources:
- url: https://support.telnyx.com/en/articles/1130595-account-verification
- url: https://support.telnyx.com/en/articles/1130639-what-is-your-refund-policy
- url: https://support.telnyx.com/en/articles/1130689-how-do-i-cancel-my-account
- url: https://support.telnyx.com/en/articles/3610162-prevent-telnyx-account-fraud
- url: https://support.telnyx.com/en/articles/3739748-2fa-totp-setup
- url: https://support.telnyx.com/en/articles/4280610-how-to-setup-your-account-settings
- url: https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them
- url: https://support.telnyx.com/en/articles/4557103-telnyx-privacy-policy
- url: https://support.telnyx.com/en/articles/5367966-introducing-the-verify-api
- url: https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy
- url: https://support.telnyx.com/en/articles/7020727-account-compromise-what-to-do
- url: https://support.telnyx.com/en/articles/7915224-blocked-account-guidelines
- url: https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status
- url: https://support.telnyx.com/en/collections/3968260-telnyx-identity-verification-tools
updated_at: 2026-07-17T09:01:50Z
---

# Telnyx Account Management

*Part 1 of 2 — see also: [Part 2](telnyx-account-management--part-2.md)*

This page covers Telnyx account management topics including verification frameworks (legacy Level 1/Level 2 and TPVE), account settings configuration, two-factor authentication setup, API key management, the Telnyx Verify API for application-based verification, fraud prevention best practices, account compromise response, blocked account guidelines, account cancellation, refund policy, and privacy policy.

## Account Verification

Telnyx uses a tiered account verification system to prevent abuse and ensure responsible use of communication services. There are two possible frameworks an account may fall under: the legacy Level 1 / Level 2 framework, and the Trial-Paid-Verified-Enterprise (TPVE) framework.

### Legacy Framework: Level 1 and Level 2

You are using the legacy framework if you see the **Verifications** tab in your account settings.

**Level 1** is granted automatically after confirming your email. It allows you to:

- Buy a local number in your home country
- Assign a connection or messaging profile to a number
- Set up messaging and voice capabilities (US only)
- Create a multi-user organization

Outbound messages are limited to 50 per day at this level.

**Level 2** removes many restrictions and unlocks advanced features:

- Buy international numbers
- Enable international calling and call forwarding
- Increase message send rates (account-wide from 600 to 3000; toll-free from 6 to 1200)
- Use alphanumeric sender ID for international messaging
- Submit orders for hosted SMS and 10DLC
- Order SIM cards internationally or with a freemail address
- Remove payment address restrictions and payment top-up limits

To apply for Level 2, the account must already be Level 1 verified, have a contact number and company name added under **Account Settings > Profile**, and have a payment method on file. Only organization owners can access the Verifications section. From the portal, navigate to **Account Settings > Verifications**, expand the **Level 2** section, fill out the form, and click **Request Level 2 Verification**. A Telnyx team member may reach out to clarify the use case, and approval or rejection may take up to 48 hours.

If a Level 2 verification request is denied, the appeal process involves answering questions about intended use, business purpose, business website, and confirming that account details match the payment method on file. Appeals and supporting documentation should be sent to [kyc.verifications@telnyx.com](mailto:kyc.verifications@telnyx.com).

### TPVE Framework

New signups from June 2025 onward may be presented with the TPVE framework instead of the legacy verification system. You are using the TPVE framework if you see the **Account Levels** page rather than a Verifications tab. The framework categorizes accounts into:

1. **Trial** – Default for new signups
2. **Paid** – Once a payment method is added
3. **Verified** – After business verification
4. **Enterprise** – For high-volume customers (discuss with the sales team)

Key TPVE characteristics include that the account level is shared across the organization, privileges such as API access and message limits are defined by level, and the interface clearly shows the current level and upgrade options.

## Account Settings

The **Account** section in Mission Control Portal is accessed from the profile icon in the top right corner. It contains the following areas:

- **Account Information** – Personal details used for verification and support contact. Promo codes can be redeemed here. The **Data Storage Location** setting lets you choose between the United States, Germany, or Australia to comply with regional regulations. This setting can only be changed once.
- **Access Control IPs** – A list of SIP signal or media IPs that originate traffic to the Telnyx network, preventing SIP traffic from being blocked during network security actions.
- **Security** – Settings for email, password, sign-in via email link, two-factor authentication, security passphrase, account verification ID, and numeric security codes (which rotate every 3 minutes).

## Two-Factor Authentication (2FA) and TOTP

Two-factor authentication adds an extra step when signing in to Mission Control Portal. After entering a password, a temporary verification code from the selected 2FA method is also required. This is separate from Telnyx Verify, which is a product used to add verification codes to your own applications.

Before enabling 2FA, choose a method (authenticator app/TOTP or SMS/Call), ensure access to the phone or app, and be ready to save backup codes. Verification codes, backup codes, QR codes, and authenticator setup details should never be shared.

**TOTP (Time-Based One-Time Password)** uses an authenticator app such as Google Authenticator, Microsoft Authenticator, 1Password, or other standards-based TOTP apps. TOTP is generally the best option because it does not depend on SMS or voice-call delivery.

**SMS/Call** sends a verification code to a phone number by text message or voice call. Delivery depends on the phone, carrier, network coverage, roaming, and retry limits.

To set up TOTP: sign in to Mission Control Portal, go to **Account** and open the security settings, enable Two-Factor Authentication, select the TOTP option, scan the QR code with the authenticator app, enter the temporary code to activate, and save the backup codes.

To set up SMS/Call 2FA: sign in, open security settings, enable 2FA, select SMS/Call, enter a phone number, choose SMS or Call to receive a code, enter the code to activate, and save the backup codes.

Backup codes are displayed once and each can only be used once. They should be stored securely and separately from the 2FA device. If access to the authenticator app, phone number, and backup codes is lost, contact [support@telnyx.com](mailto:support@telnyx.com) for account recovery.

When changing phones or authenticator apps, confirm valid backup codes first, transfer or re-add the Telnyx entry in the new app before removing it from the old device, update the phone number for SMS/Call while still able to receive codes, and test the next Portal sign-in before retiring the old device.

For SSO/SAML accounts, multi-factor authentication may be managed by the organization's identity provider rather than Telnyx Portal 2FA settings.

Portal 2FA protects interactive sign-in only. It does not configure Telnyx Verify and does not replace API key security. API keys should be stored securely, rotated when needed, and removed when no longer in use.

### Troubleshooting 2FA

- **Authenticator code not working** – Use the correct Telnyx entry, use the current code (TOTP codes expire quickly), confirm the device date and time are correct, or use a backup code.
- **SMS or call not received** – Confirm the phone can receive messages, wait before requesting another code to avoid rate limits, or consider switching to TOTP.
- **Request-limit or login-attempt errors** – Wait before retrying, or contact [support@telnyx.com](mailto:support@telnyx.com) if access is urgent.
- **Lost 2FA device without backup codes** – Contact [support@telnyx.com](mailto:support@telnyx.com) for account recovery.

## API Keys

Telnyx uses API Keys (for v2 endpoints) or API Tokens (for v1 endpoints) to authenticate API requests.

To create an API v2 Key: log in to the portal, click the Account Settings option in the account icon, then click [API Keys](https://portal.telnyx.com/#/api-keys). Click **Create API Key** in the top right. The key is used as the bearer token in API requests. The key is only visible at creation and must be securely stored in application environment variables. Keys can have an expiration date, be temporarily disabled via toggle, and be associated with up to 10 tags.

To create an API v1 Token: log in to the portal, click the Account Settings dropdown, click [API Keys](https://portal.telnyx.com/#/api-keys), then click the **API V1 Tokens** button in the top right. Click **Create API Token**, give it a name, and copy the token. The token is only visible at creation. API v1 requests must include two headers: `x-api-user` (account email) and `x-api-token` (account token).
