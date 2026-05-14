---
title: 'Telnyx DID Numbers: Types, Coverage, Ordering, and Restrictions'
summary: Learn what DID numbers are, the number types Telnyx offers (local, toll‑free,
  and international), where they’re available, how to buy them, and the ordering restrictions
  tied to account verification and signup details.
sources:
- url: https://support.telnyx.com/en/articles/1130699-did-numbers-that-telnyx-offers
- url: https://support.telnyx.com/en/articles/1130702-where-can-i-buy-dids-in-the-us-canada
- url: https://support.telnyx.com/en/articles/1130704-what-is-a-did
- url: https://support.telnyx.com/en/articles/1130664-countries-that-telnyx-offers-termination-in
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
- url: https://support.telnyx.com/en/articles/1458084-global-number-types
- url: https://support.telnyx.com/en/articles/1424680-international-coverage
updated_at: 2026-05-14T11:38:09Z
---

# Telnyx DID Numbers: Types, Coverage, Ordering, and Restrictions

Learn what DID numbers are, the number types Telnyx offers (local, toll‑free, and international), where they’re available, how to buy them, and the ordering restrictions tied to account verification and signup details.

## DID basics
A Direct Inward Dialing (DID) number is a virtual phone number that works like a regular number but isn’t tied to a POTS landline. After you configure your Telnyx account, your DID becomes the number people can call to reach you globally.

## Number types Telnyx offers
- Domestic local (long‑code): Typical local business numbers with coverage across the United States and Canada. Telnyx supports instant provisioning for voice, fax, SMS, and MMS. See the domestic coverage map for availability: https://telnyx.com/resources/telnyx-domestic-coverage-map
- Domestic toll‑free (+1): Telnyx is a managing Responsible Organization (RespOrg QIT01) and can acquire, manage, and route toll‑free calls, with the ability to quickly reroute traffic during service impairments.
- Toll‑free voice quickship: You can purchase pre‑provisioned voice toll‑free numbers for instant use by selecting quickship in the number search UI. If quickship isn’t selected, voice routing can take up to one hour to activate after order completion. Quickship applies to voice (inbound) only. API reference: https://developers.telnyx.com/api/numbers/list-available-phone-number-blocks
- Toll‑free messaging (US/CA): Telnyx supports toll‑free SMS and MMS. Messaging is not instantly provisioned—submit your use case first to avoid spam blocks. Details: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- International numbers: Telnyx provides local, national, toll‑free, shared‑cost, and mobile numbers in select countries. Some countries require documentation at checkout or shortly after; you’ll have 10 days to submit required documents or numbers may be removed from your account. Requirements overview: https://support.telnyx.com/en/articles/5469551-international-numbers-required-documents

## US and Canada local availability
Telnyx offers DIDs in every US state and every Canadian province, with coverage in over 20,000 rate centers across the US and Canada.

## International number availability
Telnyx proposes numbers in many countries worldwide. Explore the coverage list: https://support.telnyx.com/en/articles/1424680-international-coverage and the interactive global coverage map: https://telnyx.com/global-coverage

## Outbound voice termination coverage
Telnyx offers outbound call termination to every country. International termination pricing is available in the portal: https://portal.telnyx.com/#/pricing/voice

## How to buy numbers and check pricing
- Review pricing: https://telnyx.com/pricing/numbers
- Create a Telnyx account (Mission Control Portal)
- Search and buy numbers instantly in the portal. Guidance: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers

## Ordering restrictions and verification requirements
To combat fraud and protect the platform, Telnyx enforces ordering restrictions based on account verification level and signup details.

- +1 toll‑free restrictions for freemail accounts (effective Sept 22, 2025):
  - Freemail domains (e.g., gmail.com, yahoo.com, outlook.com) created on or after Sept 22, 2025 cannot order +1 toll‑free numbers, regardless of verification level.
  - Freemail accounts created before that date, and non‑freemail (corporate/custom domain) accounts, may order +1 toll‑free if other qualifications are met.

- Legacy Level 1 / Level 2 framework:
  - Accounts created after Mar 24, 2025 with Level 1 (L1): can only order local numbers from their account’s country of origin.
  - Accounts created before Mar 24, 2025 with L1: cannot order toll‑free numbers; no other restrictions.
  - Level 2 (L2): no ordering restrictions.

- Trial‑Paid‑Verified‑Enterprise (TPVE) framework:
  - See capabilities, restrictions, and upgrade steps: https://developers.telnyx.com/docs/account-setup/levels-and-capabilities

- Sub‑users and managed accounts:
  - Sub‑user restrictions follow the organization owner’s signup date and verification status.
  - Managed accounts’ restrictions are based on each individual Manager/Managed account’s signup date and verification status.

- Verification help: https://support.telnyx.com/en/articles/1130595-account-verification

## Notes and timelines to remember
- Quickship ensures instant voice readiness for toll‑free; without quickship, allow up to one hour for activation.
- International numbers that require documents must be fully submitted within 10 days or the numbers may be removed.
- Freemail +1 toll‑free ordering block applies to freemail accounts created on/after Sept 22, 2025.
