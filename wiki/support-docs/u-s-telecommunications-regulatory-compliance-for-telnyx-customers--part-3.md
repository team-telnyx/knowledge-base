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

*Part 3 of 7 — see also: [Part 1](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-1.md), [Part 2](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-2.md), [Part 4](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-4.md), [Part 5](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-5.md), [Part 6](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-6.md), [Part 7](u-s-telecommunications-regulatory-compliance-for-telnyx-customers--part-7.md)*

This page consolidates the key U.S. telecommunications regulatory requirements affecting Telnyx customers, including the STIR/SHAKEN call authentication framework, the FCC's Eighth Report and Order on third-party authentication, Robocall Mitigation Database registration, Do-Not-Originate (DNO) blocking rules, the Reassigned Numbers Database, Texas Mini-TCPA (SB 140) telemarketing rules, exhausted area codes, and number lifecycle management after account abolishment.

## Robocall Mitigation Database (RMD)

The FCC maintains a record of originating, intermediate, and gateway service providers and their STIR/SHAKEN implementation status in the Robocall Mitigation Database (RMD). Beginning September 28, 2021, intermediate providers and voice service providers (VSPs) may no longer accept traffic directly from voice service providers that are not listed in the RMD.

In accordance with FCC directives (FCC 24-73, FCC 23-18), all carriers, including Telnyx, have an obligation to begin blocking incoming calls leveraging US Calling Line Identity (CLI) from voice service providers not registered on the Database. This includes both US and foreign voice service providers that use US North American Numbering Plan resources to send voice traffic to residential or business subscribers in the United States. Foreign voice service providers were temporarily exempted from the September 28th blocking date, but the FCC updated this rule to include foreign service providers that use US numbers starting April 11, 2023.

### Voice Service Provider Definition

A voice service provider is defined as "any service that is interconnected with the public switched telephone network and that furnishes voice communications to an end user using resources from the North American Numbering Plan or any successor to the North American Numbering Plan adopted by the Commission under section 251(e)(1) of the Communications Act of 1934, as amended" (47 C.F.R. 64.1600(r)(1)).

### RMD Registration Requirements

Before submitting a filing on the RMD website, you will need a Commission Registration System (CORES) account and an FCC Registration Number (FRN). Visit <https://apps.fcc.gov/cores/userLogin.do> for account setup.

The FCC requires businesses to provide:

- Business name, contact information, FRN number, and ownership information
- Type of filing (voice service provider, gateway provider, or non-gateway intermediate provider). If you serve more than one role in the call chain, the FCC has instructed providers to select all options that apply.
- Whether you are a U.S. or foreign service provider
- Certification of full, partial, or no STIR/SHAKEN implementation
- A robocall mitigation plan. All providers, regardless of whether they are required to implement STIR/SHAKEN—including all intermediate providers and providers that lack control over the network infrastructure necessary to implement STIR/SHAKEN—are required to file certifications and robocall mitigation plans. These plans must describe the specific "reasonable steps" the provider has taken to avoid the origination, carrying, or processing of illegal robocall traffic.

### RMD and the Eighth Report and Order

In the Eighth Report and Order, the FCC mandates that any OSP certifying that they have "Partial" or "Complete" STIR/SHAKEN implementation in the RMD must have an SPC token and digital certificate.

- Pure resellers who do not have control over their network infrastructure cannot claim to have "Partial" or "Complete" STIR/SHAKEN Implementation in their RMD filings. Instead, these providers must select "No STIR/SHAKEN Implementation" and include an explanatory note indicating their exemption due to a lack of control over the network infrastructure necessary to implement STIR/SHAKEN, pursuant to [47 CFR 64.6305(d)(2)(i)](https://www.ecfr.gov/current/title-47/part-64/subpart-HH#p-64.6305(d)(2)).
- If you have stated in the RMD that your company has "Complete" or "Partial" STIR/SHAKEN implementation, Telnyx will no longer be able to sign calls on your behalf.
- If you have improperly certified and instead are a pure reseller with no control over the network infrastructure, you must update your RMD registration to properly reflect your status.

For more detailed guidance, see the FCC's Second Report and Order, paragraphs 19–23, and the Sixth Caller ID Authentication Report and Order at 20, 22-23, paras. 36, 40-41; 47 CFR § 64.6305(d)(2),(e)(2), (f)(2).

## FCC Do-Not-Originate (DNO) Requirements

The FCC has adopted new rules that expand the industry's responsibilities around blocking calls from Do-Not-Originate (DNO) numbers. A DNO list identifies numbers that should never be used to originate outbound calls—for example, inbound-only government hotlines or numbers associated with impersonation scams.

Historically, only gateway providers (U.S.-based intermediate providers that receive and pass along calls from foreign service providers) were required to block outbound calls originating from numbers on their own DNO lists. Under the FCC's new rules ([FCC 25-15](https://www.federalregister.gov/documents/2025/03/24/2025-04811/advanced-methods-to-target-and-eliminate-unlawful-robocalls)), all U.S. voice service providers in the call path must block calls that appear to originate from a number on a "reasonable DNO list." These rules took effect on December 15, 2025.

### What Counts as a "Reasonable DNO List"

The FCC does not mandate a single centralized DNO list. Instead, providers must maintain and consult a DNO list covering four categories of numbers:

1. **Invalid Numbers**: Numbers that are not dialable under the North American Numbering Plan (e.g., numbers with invalid NPA-NXX formats).
2. **Unallocated Numbers**: Valid NANP numbers that have never been assigned to a provider.
3. **Unused Numbers**: Numbers that a provider has been allocated but has not yet assigned to an end user.
4. **Numbers Requested for DNO Blocking**:
   - Inbound-only numbers that the owner of the number has requested be added to the DNO list
   - Inbound-only government numbers when the government entity has requested DNO protection
   - Private-sector inbound-only numbers used in impersonation scams, when the number owner requests blocking

Providers may also include additional categories, as long as the overall list remains "reasonable" as defined in the Order.

This obligation applies regardless of your position in the call path. If you are listed in the Robocall Mitigation Database as a voice service provider, gateway provider, or non-gateway intermediate provider, this rule applies to you.
