---
title: Accounts, Billing, and Policies Overview
summary: A consolidated guide to Telnyx account levels and verification, Freemium
  accounts, billing methods and refunds, call surcharges, cancellation procedures,
  reseller support, and related policies— with links to key portal pages and docs.
sources:
- url: https://support.telnyx.com/en/articles/1130595-account-verification
  content_hash: 5398dd1289c1dd90112e3b6312491be1317b89f730e2c13ef71366e04c802996
- url: https://support.telnyx.com/en/articles/1130659-billing-increments
  content_hash: bb6535d6c47699634bb0111cefdcb9d2e34db999376ee2c18127e0817efdc8be
- url: https://support.telnyx.com/en/articles/1130661-does-telnyx-offer-post-paid-service
  content_hash: 37a4b06ce0a15179ea4f70e87dd717fe257529c6df3196c3cfb2244ca4fad4c6
- url: https://support.telnyx.com/en/articles/1130643-is-there-a-cancellation-fee
  content_hash: ea95ca2c252dd1f1d4cd00e347b26a74701ad459a487113882db46dc918df245
- url: https://support.telnyx.com/en/articles/1130639-what-is-your-refund-policy
  content_hash: 665c31f59954b7604eb96861ce4b8ab6b788220da3fd71634a51fc18e69963ea
- url: https://support.telnyx.com/en/articles/14327893-telnyx-freemium-accounts
  content_hash: 28eb508f94132dbd78abf967fb73e3538c3649707f539da2ed5984e9b0f50da6
- url: https://support.telnyx.com/en/articles/1130689-how-do-i-cancel-my-account
  content_hash: e47ccb5e53a5926dc6a1bc92e9870ad09843a4c3046f8326a715c591a7083803
- url: https://support.telnyx.com/en/articles/1130658-how-do-i-know-if-a-rate-has-changed
  content_hash: 2ef517180490806fc48014120ea64631173128d393dd9c8f098a86a013124378
- url: https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it
  content_hash: ff6d3d7c2c10efda6e1c700c4b6deedc4965872cadd57d4a309eac38fc58ca8a
- url: https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates
  content_hash: 505234a4862f089b634b3f5f4b3fc8e3b1bd38a016f7f31cbdc9cb4b50bc4fc1
- url: https://support.telnyx.com/en/articles/1130655-can-i-resell-your-services
  content_hash: e0405fda4d8c0f371e1a9c3ca467acde8f6d3df87af31b7fef5644ca7f4c98d9
- url: https://support.telnyx.com/en/articles/1130667-do-you-offer-service-to-call-centers
  content_hash: 1861fcd9ab1dc4b041f22ec989e86722752da68bd48da9a51589b7f12fb67408
updated_at: 2026-05-14T11:39:16Z
---

# Accounts, Billing, and Policies Overview

A consolidated guide to Telnyx account levels and verification, Freemium accounts, billing methods and refunds, call surcharges, cancellation procedures, reseller support, and related policies— with links to key portal pages and docs.

## Account levels and verification frameworks

Telnyx uses two account-level frameworks. Which one you see depends on your portal experience:

- Legacy Level 1/Level 2: You’ll see an Account Settings > Verifications tab.
- TPVE (Trial–Paid–Verified–Enterprise): You’ll see an Account Levels page at https://portal.telnyx.com/#/account/account-levels. New signups from June 2025 onward may see this experience.

Legacy Level 1 capabilities
- Most users are auto-verified to Level 1 after email confirmation.
- Buy a local number in your home country.
- Assign a connection or messaging profile to a number.
- Set up messaging and US voice capabilities.
- Create a multi-user organization.
- Outbound SMS limited to 50/day.

Legacy Level 2 capabilities (unlocks advanced features)
- Buy international numbers.
- Enable international calling and call forwarding.
- Higher messaging send rates: account-wide from 600 to 3000; toll-free from 6 to 1200.
- Use alphanumeric sender ID for international messaging.
- Submit hosted SMS and 10DLC orders.
- Order SIMs internationally or with a freemail address.
- Removes payment address restrictions and top-up limits.

Apply for Legacy Level 2
- Prereqs: Level 1 verified, contact number and company name in Account Settings > Profile, and a payment method on file.
- Steps: Go to https://portal.telnyx.com/#/account/my-account/verifications, expand Level 2, submit the form. Only organization owners can access. Approval may take up to 48 hours. If declined, see the appeal article at https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status.

TPVE framework (Trial, Paid, Verified, Enterprise)
- Trial: default for new signups.
- Paid: when a payment method is added.
- Verified: after business verification.
- Enterprise: for high-volume customers (contact sales at https://telnyx.com/contact-us).
- Account level is org-wide; privileges (API access, limits) are defined by level and displayed in the interface.
- See feature matrices and API access by level:
  - Account Levels developer docs: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities
  - V2 APIs access table: https://us-west-1.telnyxstorage.com/telnyx-support-kb-collaterals/api.telnyx.com.html
  - S3 APIs access table: https://us-west-1.telnyxstorage.com/telnyx-support-kb-collaterals/telnyxstorage.com.html

## Freemium accounts (AI-only)
- Try Telnyx AI products with no credit card or payment setup. Sign up at https://telnyx.com/sign-up and log in via magic link.
- Included: $25 in AI credits (auto-applied) and one US local phone number. Credit covers AI product usage and the included number.
- Scope: Limited to AI products (e.g., Inference, AI Assistants). Non-AI products return errors until you upgrade.
- Credit expiry: Usage stops after the $25 is consumed; to continue, upgrade to a full account and add funds.
- Upgrading: In the portal, go to Account Level > Upgrade and verify via LinkedIn or GitHub (two attempts total). Upon approval, you become a standard Telnyx trial with access to all products; the $25 AI credit is replaced with a $5 account-wide credit. Each LinkedIn/GitHub can verify only one Telnyx account.
- Billing: Freemium accounts cannot top up; add funds only after upgrading.
- Cancellation or email reuse: Contact support at https://telnyx.com/contact-us.

## Billing model, refunds, and rate change notices
- Pre-paid only: Telnyx does not offer post-paid service.
- No contracts or cancellation fees: You can cancel without penalties.
- Refunds:
  - No refunds for Bitcoin (BTC) payments.
  - No refunds for payments 180+ days old (any method).
  - Unused funds not matching the above can be refunded by emailing billing@telnyx.com.
  - Pay-as-you-go charges for services already consumed are not refundable.
- Rate changes: Telnyx emails customers whenever rates change.

## Voice billing: increments and channel billing
Billing increments
- Standard increments are 60/60. A call of 11 seconds bills as 60 seconds; 96 seconds bills as 120 seconds.
- International calling generally uses 60-second increments but may vary by destination; download the latest international rates in the portal: https://portal.telnyx.com/#/app/pricing.
- 6-second billing is no longer offered.

Channel billing (inbound)
- Pay a flat per-channel fee for unlimited inbound minutes. Each channel allows one concurrent inbound call across any numbers enabled for channel billing.
- Applicability: Standard DIDs only. Toll-free and international DIDs are pay-per-minute.
- Sharing: Channels are shared across all numbers set to channel billing on the account. You can mix pay-per-minute and channel-billed numbers.
- Capacity planning: Provision enough channels to cover expected simultaneous inbound calls; excess calls receive busy tone.
- Setup steps:
  1) Log in at https://portal.telnyx.com/#/app/home.
  2) Go to Numbers > Channels and use +/– to add or remove channels.
  3) On each number’s settings, choose Channel as the billing method under Billing.

## Abandoned outbound call surcharge (effective Nov 1, 2025)
- If more than 20% of your outbound calls are abandoned by the originator before answer, a surcharge of $0.005 per abandoned call applies.
- Definition: A call the caller disconnects during ringing/setup is considered abandoned. Calls to disconnected numbers also count as abandoned.
- Scope: Outbound only. If the threshold is exceeded, the surcharge applies to all abandoned calls for the period, not just the excess.
- What to do: Review dialer/validation call patterns and keep abandoned rate below 20%.
- Tracking options:
  - Reports dashboard pie chart at https://portal.telnyx.com/#/reports/dashboard.
  - Reporting > Usage Reports (Advanced Version): Product = SIP Trunking; Dimensions = Direction, Hangup Details; Metrics = Attempted; Filter Direction = outbound; Breakout where recv_cancel indicates abandoned.

## Cancel accounts, remove members, and re-enable
- Remove a member: Organization and Members at https://portal.telnyx.com/#/advanced-features/members.
- Cancel your own account: Email support@telnyx.com from the account owner’s email and include the account Security Passphrase.
- Find your Security Passphrase: Portal > Account Security at https://portal.telnyx.com/#/account/my-account/security. This is not your login password.
- Re-enable a cancelled account: Email support@telnyx.com from the address to be reactivated (org owners can request for sub-members; include their email).

## Reselling and multi-tenant support
- Mission Control is designed for multi-tenant use with tagging, segregation, and real-time reporting.
- All portal functionality is backed by publicly available APIs, enabling you to build ordering and provisioning into your own platform: https://developers.telnyx.com.

## Service for call centers
- Telnyx serves call centers and considers them an ideal customer profile. Contact us to get started: https://telnyx.com/contact-us.
