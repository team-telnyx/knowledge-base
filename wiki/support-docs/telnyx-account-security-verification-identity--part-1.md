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

*Part 1 of 5 — see also: [Part 2](telnyx-account-security-verification-identity--part-2.md), [Part 3](telnyx-account-security-verification-identity--part-3.md), [Part 4](telnyx-account-security-verification-identity--part-4.md), [Part 5](telnyx-account-security-verification-identity--part-5.md)*

This page consolidates Telnyx guidance on account verification (legacy Level 1/Level 2 and the newer Trial-Paid-Verified-Enterprise framework), Mission Control Portal two-factor authentication, the Telnyx Verify API for embedding 2FA in your own applications, fraud prevention and account compromise recovery, blocked account guidelines, refunds, TLS/SSL certificate handling, and webhook certificate authority errors.

## Account Verification Frameworks

Telnyx uses a tiered account verification system to prevent abuse and ensure responsible use of communication services. There are two possible frameworks an account may fall under:

- The **Level 1 / Level 2 framework** (Legacy)
- The **Trial-Paid-Verified-Enterprise (TPVE) framework**

You are using the legacy framework if you see the **Verifications** tab in your account settings. You are using the TPVE framework if you see the **Account Levels** page instead.

### Legacy Framework: Level 1 & Level 2

Most users are automatically Level 1 verified after confirming their email. Level 1 allows you to:

- Buy a local number in your home country
- Assign a connection or messaging profile to a number
- Set up messaging and voice capabilities (US only)
- Create a multi-user organization
- Send up to 50 outbound messages per day

Level 2 removes many restrictions and unlocks advanced features:

- Buy international numbers
- Enable international calling and call forwarding
- Increase message send rates (account-wide from 600 to 3000; toll-free from 6 to 1200)
- Use alphanumeric sender ID for international messaging
- Submit orders for hosted SMS and 10DLC
- Order SIM cards internationally or with a freemail address
- Remove payment address restrictions and payment top-up limits

To apply for Level 2, the account must already be Level 1 verified, have a contact number and company name added under **Account Settings > Profile**, and have a payment method on file. Only organization owners can access the Verifications section.

Steps to apply:

1. Go to **Account Settings > Verifications** in the Mission Control Portal.
2. Expand the **Level 2** section.
3. Fill out the form and click **Request Level 2 Verification**.

A Telnyx team member may reach out to clarify use case or verify details. Approval or rejection may take up to 48 hours. If verification was unsuccessful, see [Appeal Level 2 Verification Status](appeal-level-2-verification-status.md) for next steps.

### TPVE Framework

New signups from June 2025 onward may be presented with a revised account levels section in place of the legacy verification system. The TPVE framework categorizes accounts into:

1. **Trial** – Default for new signups
2. **Paid** – Once a payment method is added
3. **Verified** – After business verification
4. **Enterprise** – For high-volume customers (discuss with the sales team)

Key TPVE characteristics:

- Account level is shared across the organization
- Privileges (e.g., API access, message limits) are defined by level
- The interface clearly shows your current level and upgrade options

For full capabilities of each level, refer to the [Account Levels Developer Docs](https://developers.telnyx.com/docs/account-setup/levels-and-capabilities), the [V2 APIs Access Table](https://us-west-1.telnyxstorage.com/telnyx-support-kb-collaterals/api.telnyx.com.html), and the [S3 APIs Access Table](https://us-west-1.telnyxstorage.com/telnyx-support-kb-collaterals/telnyxstorage.com.html).
