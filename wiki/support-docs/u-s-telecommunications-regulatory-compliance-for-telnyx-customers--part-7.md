---
title: U.S. Telecommunications Regulatory Compliance for Telnyx Customers
summary: This page consolidates the key U.S. telecommunications regulatory requirements
  affecting Telnyx customers, including the STIR/SHAKEN call authentication framework,
  the FCC's Eighth Report and Order on third-party authentication, Robocall Mitigation
  Database registration, Do-Not-Originate (DNO) blocking rules, the Reassigned Numbers
  Database, Texas Mini-TCPA (SB 140) telemarketing rules, exhausted area codes, and
  number lifecycle management after account abolishment.
sources:
- url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
- url: https://support.telnyx.com/en/articles/4640720-what-is-an-exhausted-npa
- url: https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx
- url: https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database
- url: https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs
- url: https://support.telnyx.com/en/articles/5883839-what-is-the-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
- url: https://support.telnyx.com/en/articles/8648864-what-happens-with-my-numbers-after-my-account-gets-abolished-for-negative-balance
- url: https://support.telnyx.com/en/collections/12044103-regulatory
updated_at: 2026-07-17T09:01:52Z
---

# U.S. Telecommunications Regulatory Compliance for Telnyx Customers

*Part 7 of 7 — see also: [Part 1](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-1.md), [Part 2](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-2.md), [Part 3](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-3.md), [Part 4](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-4.md), [Part 5](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-5.md), [Part 6](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-6.md)*

This page consolidates the key U.S. telecommunications regulatory requirements affecting Telnyx customers, including the STIR/SHAKEN call authentication framework, the FCC's Eighth Report and Order on third-party authentication, Robocall Mitigation Database registration, Do-Not-Originate (DNO) blocking rules, the Reassigned Numbers Database, Texas Mini-TCPA (SB 140) telemarketing rules, exhausted area codes, and number lifecycle management after account abolishment.

## Canadian STIR/SHAKEN Implementation

Telnyx handles all Canadian STIR/SHAKEN compliance requirements on behalf of customers. Outbound calls originating with Canadian CLI receive appropriate signings from Telnyx's Canadian partners.

The attestation definitions used in Canada are the same as in the US:

- **Full Attestation (A)**: The provider knows the customer, knows they have the right to use the originating number, and knows the call originated on their network. For numbers purchased in the Telnyx portal, you should expect to receive an 'A Attestation'.
- **Partial Attestation (B)**: The provider knows the customer but the customer may be using another provider's phone number. The call is legitimate but the provider can't fully attest because of missing information.
- **Gateway Attestation (C)**: The provider can't verify the customer or the phone number and has no way of knowing whether the call is legitimate. The originating provider will still attest to the call in order to mark that the call originated on their network.

If you have your Canadian CLI listed in your Telnyx Mission Control Portal (whether the number was purchased from Telnyx or ported into Telnyx), you will receive an A attestation. If your CLI is not listed in your Telnyx Mission Control Portal, you will receive a B attestation.

There is no additional charge for SHAKEN/STIR services in Canada. All calls originating on the Telnyx network with Canadian CLI will receive an attestation, and no action is required from the customer. Customers will not be notified of the attestation they receive from Telnyx, but customers should be able to predict the attestation level based on the requirements outlined above.

## Disclaimer

The information provided in this Telnyx support article is for general informational purposes only and should not be construed as legal advice. Please consult with a qualified attorney for guidance on legal or regulatory compliance.
