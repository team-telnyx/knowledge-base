---
title: Telnyx Regulatory & Compliance Reference
summary: A consolidated reference for Telnyx customers covering U.S. and state regulatory
  requirements, FCC compliance programs (STIR/SHAKEN, RMD, RND, DNO), Telnyx security
  certifications, traffic surcharges, and number lifecycle policies that affect voice
  and messaging services.
sources:
- url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
- url: https://support.telnyx.com/en/articles/1130616-number-not-portable-tn-not-portable-error
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
- url: https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications
- url: https://support.telnyx.com/en/articles/12805746-surcharge-for-high-abandoned-call-rates
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
- url: https://support.telnyx.com/en/articles/15668484-calls-per-second-cps-limits
- url: https://support.telnyx.com/en/articles/5883839-what-is-the-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/7834487-calls-per-second-cps-surcharge
- url: https://support.telnyx.com/en/articles/8648864-what-happens-with-my-numbers-after-my-account-gets-abolished-for-negative-balance
- url: https://support.telnyx.com/en/collections/12044103-regulatory
updated_at: 2026-08-05T13:26:15Z
---

# Telnyx Regulatory & Compliance Reference

*Part 1 of 5 — see also: [Part 2](telnyx-regulatory-compliance-reference--part-2.md), [Part 3](telnyx-regulatory-compliance-reference--part-3.md), [Part 4](telnyx-regulatory-compliance-reference--part-4.md), [Part 5](telnyx-regulatory-compliance-reference--part-5.md)*

A consolidated reference for Telnyx customers covering U.S. and state regulatory requirements, FCC compliance programs (STIR/SHAKEN, RMD, RND, DNO), Telnyx security certifications, traffic surcharges, and number lifecycle policies that affect voice and messaging services.

## Overview

Telnyx operates within a layered regulatory environment that includes FCC rules on caller-ID authentication, robocall mitigation, reassigned number tracking, and do-not-originate blocking, as well as state telemarketing laws and industry security standards. This page consolidates the key compliance obligations, Telnyx policies, and operational surcharges that customers should understand when sending U.S. voice or messaging traffic through the Telnyx network.

## FCC Eighth Report and Order on Third-Party Authentication

The FCC's [Eighth Report and Order on third-party authentication](https://docs.fcc.gov/public/attachments/FCC-24-120A1.pdf) takes effect **September 18, 2025** and impacts originating service providers (OSPs) with a STIR/SHAKEN implementation obligation.

The Order prohibits "third-party authentication," defined as an arrangement in which an OSP subject to STIR/SHAKEN contracts with a third party to perform the technical function of signing calls on its behalf. Permissible third-party authentication arrangements are limited to those in which the OSP:

1. Independently determines attestation levels in accordance with STIR/SHAKEN technical standards, and
2. Ensures that all calls are authenticated using its own certificate obtained from a STIR/SHAKEN Certificate Authority, rather than relying on a third party's certificate.

Any use of a third party to sign traffic without meeting these requirements is a violation of the Commission's caller ID authentication rules. The Order also mandates that any provider certifying to **partial or full STIR/SHAKEN implementation** in the Robocall Mitigation Database must be registered with the STIR/SHAKEN Policy Administrator, obtain its own SPC token, use that token to generate a certificate with a Certificate Authority, and authenticate all calls using that certificate.

### Who Must Secure Their Own SPC Token

OSPs with control over their network infrastructure must obtain a Service Provider Code (SPC) token from the STIR/SHAKEN Policy Administrator and present it to a Certificate Authority to obtain a certificate. Telnyx will require customers to obtain their own SPC token if they:

- Use both Telnyx and another provider and either send calls using numbers from another operator across the Telnyx network, or send calls from Telnyx numbers across another provider's network, or
- Intend to spoof caller ID (only permitted if whitelisted for legitimate caller ID spoofing).

Telnyx will **not** require an SPC token if the customer exclusively uses Telnyx numbers for both origination and termination, or only uses a limited number of outside [Verified Numbers](verified-numbers.md).

### Robocall Mitigation Database Implications

Pure resellers who do not have control over their network infrastructure cannot claim "Partial" or "Complete" STIR/SHAKEN Implementation in their RMD filings. They must select "No STIR/SHAKEN Implementation" and include an explanatory note citing [47 CFR 64.6305(d)(2)(i)](https://www.ecfr.gov/current/title-47/part-64/subpart-HH#p-64.6305(d)(2)). If a customer has stated "Complete" or "Partial" STIR/SHAKEN implementation in the RMD, Telnyx will no longer be able to sign calls on their behalf. Improperly certified pure resellers must update their RMD registration to reflect their actual status.

### Steps to Become Compliant

OSPs that qualify under the new rules must complete the following steps:

1. **Obtain an OCN (Company Code)** from the [NECA](https://www.neca.org/business-solutions/company-codes) per industry standard ATIS-0300251.
2. **Register to file FCC Form 499-A**, including obtaining an FRN from CORES and a Filer ID from USAC's E-File system. See the [2025 Telecommunications Reporting Worksheet Instructions](https://www.usac.org/wp-content/uploads/service-providers/documents/forms/2025/2025-FCC-Form-499A-Form-Instructions.pdf).
3. **Register in the Robocall Mitigation Database** using the FCC's [external filing instructions](https://www.fcc.gov/sites/default/files/rmd-instructions.pdf).
4. **Register with iConectiv** (the Secure Telephone Identity Policy Administrator) by completing the [Service Provider registration form](https://authenticate.iconectiv.com/service-provider-authenticate), providing legal business name and contact information, voice service provider type, and evidence of authorization to provide U.S. voice services.
5. **Select a Certificate Authority** from the STI-PA approved list to issue the organization's STIR/SHAKEN certificate using the SPC token.
6. **Sign calls with Telnyx** using the Telnyx Hosted Signing Service, which allows customers to use their own certificate without building signing infrastructure in-house, maintain full control over attestation levels (A, B, or C), and meet industry and regulatory standards. See the [Hosted STIR/SHAKEN Product Guide](https://developers.telnyx.com/docs/development/stir-shaken/hosted-cert).

## FCC Do-Not-Originate (DNO) Requirements

Effective **December 15, 2025**, the FCC's new rules in [FCC 25-15](https://www.federalregister.gov/documents/2025/03/24/2025-04811/advanced-methods-to-target-and-eliminate-unlawful-robocalls) expand DNO obligations beyond gateway providers. All U.S. voice service providers in the call path must block calls that appear to originate from a number on a "reasonable DNO list." This obligation applies to any provider listed in the Robocall Mitigation Database as a voice service provider, gateway provider, or non-gateway intermediate provider, regardless of position in the call path.

A DNO list contains telephone numbers that should never place outbound calls. The goal is to prevent bad actors from spoofing trusted inbound-only numbers (such as IRS hotlines or bank support lines) to run impersonation scams.

A "reasonable DNO list" must cover four categories:

1. **Invalid Numbers** – numbers not dialable under the North American Numbering Plan (e.g., invalid NPA-NXX formats).
2. **Unallocated Numbers** – valid NANP numbers that have never been assigned to a provider.
3. **Unused Numbers** – numbers allocated to a provider but not yet assigned to an end user.
4. **Numbers Requested for DNO Blocking** – inbound-only numbers whose owner has requested DNO protection, inbound-only government numbers requested by the government entity, and private-sector inbound-only numbers used in impersonation scams when the owner requests blocking.

Providers may include additional categories as long as the overall list remains "reasonable" as defined in the Order.
