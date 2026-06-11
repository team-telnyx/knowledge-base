---
title: Telnyx Account Management and Billing
summary: A comprehensive guide to setting up, verifying, managing, and billing for
  a Telnyx Mission Control Portal account, including organizations, payment methods,
  invoices, taxes, notifications, and account lifecycle.
sources:
- url: https://support.telnyx.com/en/articles/1130595-account-verification
- url: https://support.telnyx.com/en/articles/1130639-what-is-your-refund-policy
- url: https://support.telnyx.com/en/articles/1130643-is-there-a-cancellation-fee
- url: https://support.telnyx.com/en/articles/1130644-do-i-have-to-sign-a-contract
- url: https://support.telnyx.com/en/articles/1130655-can-i-resell-your-services
- url: https://support.telnyx.com/en/articles/1130658-how-do-i-know-if-a-rate-has-changed
- url: https://support.telnyx.com/en/articles/1130659-billing-increments
- url: https://support.telnyx.com/en/articles/1130661-does-telnyx-offer-post-paid-service
- url: https://support.telnyx.com/en/articles/1130689-how-do-i-cancel-my-account
- url: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- url: https://support.telnyx.com/en/articles/1189141-get-started-with-organizations
- url: https://support.telnyx.com/en/articles/14327893-telnyx-freemium-accounts
- url: https://support.telnyx.com/en/articles/2185372-where-can-i-see-pricing-options
- url: https://support.telnyx.com/en/articles/3317613-billing-decimal-values-considered
- url: https://support.telnyx.com/en/articles/3562148-requesting-numbers
- url: https://support.telnyx.com/en/articles/4277896-notification-settings
- url: https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups
- url: https://support.telnyx.com/en/articles/4280610-how-to-setup-your-account-settings
- url: https://support.telnyx.com/en/articles/4404409-resources-on-your-account
- url: https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account
- url: https://support.telnyx.com/en/articles/6420959-sales-gst-telecommunication-taxes-usf-fees-trf
- url: https://support.telnyx.com/en/articles/6987563-invoice-overview
- url: https://support.telnyx.com/en/articles/7045419-ach-direct-debit-payment-method
- url: https://support.telnyx.com/en/articles/7984661-how-to-reset-your-password
- url: https://support.telnyx.com/en/articles/8228452-email-notification-international-spend-limit
- url: https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing
- url: https://support.telnyx.com/en/articles/8379618-bitcoin-payment-method
- url: https://support.telnyx.com/en/articles/8648864-what-happens-with-my-numbers-after-my-account-gets-abolished-for-negative-balance
updated_at: 2026-06-11T11:32:58Z
---

# Telnyx Account Management and Billing

*Part 1 of 4 — see also: [Part 2](telnyx-account-management-and-billing--part-2.md), [Part 3](telnyx-account-management-and-billing--part-3.md), [Part 4](telnyx-account-management-and-billing--part-4.md)*

A comprehensive guide to setting up, verifying, managing, and billing for a Telnyx Mission Control Portal account, including organizations, payment methods, invoices, taxes, notifications, and account lifecycle.

## Signing Up for a Telnyx Account

You can create a Telnyx account at [telnyx.com/sign-up](https://telnyx.com/sign-up) using either Single Sign-On (Gmail or Microsoft) or a direct sign-up form. A **business email address** is required; certain free email providers are disallowed. After entering your details, you must verify your email address and may be required to complete a phone verification via a one-time passcode.

A Know Your Customer (KYC) identity check may also be prompted during sign-up to prevent fraud and misuse. Once verified, you will be asked to provide your organization name and select your use case (e.g., SMS, SIP Trunking) to optimize your onboarding flow.

New accounts from October 2022 onward are limited to **USD** as the account currency, and existing accounts cannot change their currency.

### Single Sign-On (SSO)

Organizations can enable SAML-based SSO with providers including Auth0, Microsoft Azure AD, Okta, Google GSuite, OneLogin, and LastPass. To configure SSO, navigate to **My Account → Single Sign-On** in the portal, enter your SAML provider details, and import the IdP settings. After enabling SSO, users have 72 hours to transition before password login is disabled.

## Freemium Accounts

Freemium accounts let developers try Telnyx AI products with **no credit card and no commitment**. Sign-up uses a **magic link** (a one-time login URL sent to your email) instead of a password.

Freemium accounts include:
- **$25 in AI credits** (automatically applied)
- **One US local phone number** at no cost
- Full access to AI products (Telnyx Inference, AI Assistants, etc.)

Freemium accounts are limited to AI products only. Attempting to use non-AI products (Voice, Messaging, Wireless, etc.) will return an API error. You cannot add funds to a Freemium account.

### Upgrading to a Full Account

1. Log in to the [Telnyx Portal](https://portal.telnyx.com)
2. Click your **profile icon** → **Account Level** → **Upgrade**
3. Verify identity through **LinkedIn** or **GitHub** (two attempts allowed, one per method)

After upgrading, the $25 AI credit is replaced with a **$5 full-credit** usable across all Telnyx products. If both verification methods are rejected, you can [create a new account](https://telnyx.com/sign-up) with a business email or contact Telnyx Support.

To cancel a Freemium account, contact [Telnyx Support](https://telnyx.com/contact-us).

## Account Verification

Telnyx uses a **tiered account verification system** to prevent abuse. Your account may fall under one of two frameworks:

### Legacy Framework: Level 1 and Level 2

You are on this framework if you see a **"Verifications" tab** in your account settings.

**Level 1** — Most users are automatically Level 1 verified after confirming their email. Level 1 allows:
- Buying a local number in your home country
- Assigning connections or messaging profiles
- Setting up messaging and voice capabilities (US only)
- Creating a multi-user organization
- Outbound messages limited to **50 per day**

**Level 2** — Removes many restrictions and unlocks:
- Buying international numbers
- International calling and call forwarding
- Increased message send rates (account-wide: 600 → 3000; toll-free: 6 → 1200)
- Alphanumeric sender ID for international messaging
- Hosted SMS and 10DLC orders
- International SIM card orders or orders with freemail addresses
- Removal of payment address restrictions and top-up limits

**To apply for Level 2:**
1. Ensure your account is Level 1 verified
2. Add a contact number and company name under **Account Settings > Profile**
3. Have a payment method on file
4. Go to [Account Settings > Verifications](https://portal.telnyx.com/#/account/my-account/verifications)
5. Expand the Level 2 section, fill out the form, and click **Request Level 2 Verification**

Approval or rejection takes up to **48 hours**. Only organization owners can access this section. If unsuccessful, see the [appeal process](https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status).

### TPVE Framework (Trial-Paid-Verified-Enterprise)

New signups from June 2025 onward may see an **"Account Levels" page** instead of a Verifications tab. This framework categorizes accounts into:

1. **Trial** — Default for new signups
2. **Paid** — Once a payment method is added
3. **Verified** — After business verification
4. **Enterprise** — For high-volume customers (contact [sales](https://telnyx.com/contact-us))

Account level is shared across the organization, and privileges are defined by level. See the [Account Levels Developer Docs](https://developers.telnyx.com/docs/account-setup/levels-and-capabilities) for full details.

## Account Settings

The [Account](https://portal.telnyx.com/#/account/general) section is accessed via your profile icon in the top right corner of the portal.

### Account Information

Enter personal details (used for verification and support contact), redeem promo codes, and choose a **data storage location** (United States, Germany, or Australia). The data storage location can only be changed **once**.

### Access Control IPs

Add your SIP signalling or media IPs to prevent your traffic from being blocked during network security actions.

### Security

- **Email** — Change your account email address (requires current password)
- **Password** — Update your password; must contain at least one punctuation mark or symbol, at least one uppercase letter, and be at least 12 characters long. You can also reset via the [password reset page](https://portal.telnyx.com/#/login/password-reset)
- **Sign in via email link** — Log in using a one-time link sent to your email instead of a password
- **Two-Factor Authentication (2FA)** — Set up via [TOTP](https://telnyx.com/resources/totp-meaning) app or phone code
- **Security Passphrase** — Used to verify your identity when contacting support (different from your account password); found in the [Account Security](https://portal.telnyx.com/#/account/my-account/security) section
- **Account Verification ID** — Another identifier for support interactions
- **Numeric Security Codes** — Ephemeral codes that rotate every 3 minutes for support verification
