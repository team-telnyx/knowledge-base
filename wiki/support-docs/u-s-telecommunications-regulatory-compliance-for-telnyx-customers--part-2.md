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

*Part 2 of 7 — see also: [Part 1](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-1.md), [Part 3](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-3.md), [Part 4](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-4.md), [Part 5](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-5.md), [Part 6](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-6.md), [Part 7](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-7.md)*

This page consolidates the key U.S. telecommunications regulatory requirements affecting Telnyx customers, including the STIR/SHAKEN call authentication framework, the FCC's Eighth Report and Order on third-party authentication, Robocall Mitigation Database registration, Do-Not-Originate (DNO) blocking rules, the Reassigned Numbers Database, Texas Mini-TCPA (SB 140) telemarketing rules, exhausted area codes, and number lifecycle management after account abolishment.

## FCC Eighth Report and Order on Third-Party Authentication

The FCC has issued new compliance requirements in its [Eighth Report and Order concerning third-party authentication](https://docs.fcc.gov/public/attachments/FCC-24-120A1.pdf). These rules, which impact originating service providers (OSPs) with a STIR/SHAKEN obligation, took effect September 18, 2025.

The FCC prohibits the use of "third-party authentication," defined as an arrangement in which a provider subject to a STIR/SHAKEN implementation obligation contracts with a third party to perform the technical function of signing calls on the provider's behalf. The FCC limits permissible third-party authentication arrangements to those in which the provider subject to the STIR/SHAKEN implementation obligation:

1. Independently determines attestation levels in accordance with STIR/SHAKEN technical standards, and
2. Ensures that all calls are authenticated using its own certificate obtained from a STIR/SHAKEN Certificate Authority, rather than relying on a third party's certificate.

Any use of a third party to sign traffic without meeting these requirements constitutes a violation of the Commission's caller ID authentication rules.

Additionally, the FCC mandates that any provider certifying to partial or full STIR/SHAKEN implementation in the Robocall Mitigation Database must be registered with the STIR/SHAKEN Policy Administrator, obtain its own SPC token from the Policy Administrator, use that token to generate a certificate with the Certificate Authority, and authenticate all calls using that certificate.

### Who Must Secure Their Own SPC Tokens

The Eighth Report and Order clarifies that originating service providers (OSPs) with control over their network infrastructure must obtain a Service Provider Code (SPC) token from the STIR/SHAKEN Policy Administrator and then present that token to a STIR/SHAKEN Certificate Authority to obtain a certificate.

For Telnyx customers, this means Telnyx will require you to obtain your own SPC token to properly sign and authenticate your calls if:

- You use both Telnyx and another provider and either:
  1. Send calls using numbers from another operator across the Telnyx network, or
  2. Send calls from Telnyx numbers across another provider's network
- You intend to spoof caller ID (which you may only do if you are whitelisted for legitimate caller ID spoofing)

Telnyx's internal policies will not require you to obtain an SPC token if:

- You exclusively use Telnyx numbers for both origination and termination
- You only use a limited number of outside [Verified Numbers](verified-numbers.md)

### Steps to Obtain an SPC Token

If you determine that you qualify as an OSP with a STIR/SHAKEN implementation obligation, you must complete the following steps:

1. **Obtain an OCN (or "Company Code")**: Before obtaining an SPC token, your company must have an Operating Company Number (OCN) from the National Exchange Carrier Association (NECA). OCNs uniquely identify telecommunications service providers per industry standard ATIS-0300251. For more information, visit the [NECA website](https://www.neca.org/business-solutions/company-codes).
2. **Register to File 499-A**: You must be prepared to file FCC Form 499-A before securing an SPC token. Registration includes obtaining an FCC registration number (FRN) from the Commission registration system (CORES) and obtaining a Filer ID from USAC's E-File system. Read the [2025 Telecommunications Reporting Worksheet Instructions](https://www.usac.org/wp-content/uploads/service-providers/documents/forms/2025/2025-FCC-Form-499A-Form-Instructions.pdf) for more information.
3. **Register in the Robocall Mitigation Database**: Your company must have a valid active registration in the FCC's Robocall Mitigation Database (RMD). Before filing in the RMD, your company must have a CORES account and FRN. See the FCC's [external filing instructions](https://www.fcc.gov/sites/default/files/rmd-instructions.pdf).
4. **Register with iConectiv**: Register with the Secure Telephone Identity Policy Administrator (STI-PA), currently managed by iConectiv. Fill out the iConectiv Service Provider registration form available on the STI-PA website. You will need to provide:
   - Legal business name and contact information
   - Type of voice service provider (e.g., facilities-based, VoIP, reseller)
   - Evidence of your authorization to provide voice services in the U.S. (such as an FCC 499 Filer ID or Operating Company Number)
   - For detailed instructions, refer to the official [iConectiv Service Provider Guide](https://authenticate.iconectiv.com/service-provider-authenticate).
5. **Select a Certificate Authority**: Once your organization has successfully activated its account with the STI-PA and received its SPC token, select a Certification Authority (CA) authorized by the STI-PA. The CA will issue your organization's STIR/SHAKEN certificate. Only CAs on the official STI-PA approved list are permitted to issue these certificates.
6. **Sign Your Own Calls With Telnyx**: After obtaining your STIR/SHAKEN certificate from an approved Certification Authority, you can begin signing your outbound calls using your own credentials. Telnyx's Hosted Signing Service allows you to use your certificate without building signing infrastructure in-house. This service enables your organization to:
   - Digitally sign calls with your own certificate, meeting industry and regulatory standards
   - Maintain full control over attestation levels (A, B, or C) for your U.S. traffic
   - For more information, see the [Product Guide](https://developers.telnyx.com/docs/development/stir-shaken/hosted-cert).
