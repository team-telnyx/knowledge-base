---
title: Telnyx Compliance, Security, and Platform Reference
summary: A comprehensive reference for Telnyx regulatory compliance obligations, security
  certifications, privacy practices, and key platform operational details — covering
  STIR/SHAKEN, FCC mandates, SOC audits, HIPAA, GDPR/CCPA, the Reassigned Numbers
  Database, P2P SMS exemptions, configuration propagation, and BYOC Genesys integration.
sources:
- url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
  content_hash: 67ee5a4378cda34b22669a4edc5f1925fb15b17fb7d3df43185bfd41478988d4
- url: https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications
  content_hash: 2b00e4c40be23e8f5e6d8b498837c82ac949e40bf00070dafa1b2855e5b545d6
- url: https://support.telnyx.com/en/articles/12901901-understanding-configuration-propagation-delays-in-mission-control-portal-and-api
  content_hash: 056e70a4c1d28bc5d0d9d3df1ccdbf278417fe9bf3ba3ed4050e840cc711fe77
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
  content_hash: 8c00b9aa07357e8d25a598fbdf4427471e341bc0884ddfc96abd5d756eb2cad8
- url: https://support.telnyx.com/en/articles/3347891-hipaa-baas-and-the-conduit-exception
  content_hash: c5df94264f27b812390ce017f8ef890db223f16fca99b9434ec0d8ea51d4a2d1
- url: https://support.telnyx.com/en/articles/4557103-telnyx-privacy-policy
  content_hash: 52b9cee458ba618dd725be8b39606bb73124227173e321b447a07b61e0fd2b48
- url: https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx
  content_hash: 3ed45bcc93c15873a6b90d4faa89b4c1848b163dd9f3183fa9ab31f0860dbd45
- url: https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database
  content_hash: 8e5e86140d4a3301f5ae5a654f92de4fdbc0631efe3a1f4b50e599e6a89b36f8
- url: https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs
  content_hash: c7f2d8d7965abfc1368a2b9ca731972644ec147a989d7d4c14bd0c1615163242
- url: https://support.telnyx.com/en/articles/5883839-what-is-the-reassigned-numbers-database
  content_hash: d9cee1dd07e51e4df40626dbca4595f63c0bfa52827c904524a8a59c8cdf6554
- url: https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys
  content_hash: 531786ea6bae25ec05258db23e53bb7eebaeac53bcaff8eddadaf61dd2b6040f
- url: https://support.telnyx.com/en/articles/8685561-p2p-definition-and-exemption-process
  content_hash: 86b9d3397acf1f7f2d3720fd46fcb02ce272d955298f4e81764795dd321fb8b7
updated_at: 2026-06-11T11:44:06Z
---

# Telnyx Compliance, Security, and Platform Reference

*Part 2 of 3 — see also: [Part 1](telnyx-compliance-security-and-platform-reference--part-1.md), [Part 3](telnyx-compliance-security-and-platform-reference--part-3.md)*

A comprehensive reference for Telnyx regulatory compliance obligations, security certifications, privacy practices, and key platform operational details — covering STIR/SHAKEN, FCC mandates, SOC audits, HIPAA, GDPR/CCPA, the Reassigned Numbers Database, P2P SMS exemptions, configuration propagation, and BYOC Genesys integration.

## Robocall Mitigation Database (RMD)

Since September 28, 2021, the FCC requires that intermediate providers and voice service providers (VSPs) may not accept traffic directly from VSPs that are not listed in the [Robocall Mitigation Database](https://fccprod.servicenowservices.com/rmd?id=rmd_listings). This includes both U.S. and foreign VSPs using North American Numbering Plan resources to send voice traffic to U.S. subscribers. Telnyx has registered with the RMD to ensure compliance and uninterrupted service.

### Who Is a Voice Service Provider

A VSP is any service interconnected with the PSTN that furnishes voice communications to an end user using NANP resources (47 C.F.R. 64.1600(r)(1)).

### RMD Registration Requirements

Before filing, you need a CORES account and an FRN. The filing must include:
- Business name, contact information, FRN, and ownership information.
- Type of filing (voice service provider, gateway provider, or non-gateway intermediate provider); select all applicable roles.
- Whether you are a U.S. or foreign service provider.
- Certification of full, partial, or no STIR/SHAKEN implementation.
- A robocall mitigation plan describing the reasonable steps taken to avoid origination, carrying, or processing of illegal robocall traffic. All providers — including intermediate providers and those lacking control over the infrastructure to implement STIR/SHAKEN — must file certifications and robocall mitigation plans.

Consult legal counsel to determine whether your entity must register.

## FCC Do-Not-Originate (DNO) Requirements

Effective December 15, 2025, the FCC's [FCC 25-15](https://www.federalregister.gov/documents/2025/03/24/2025-04811/advanced-methods-to-target-and-eliminate-unlawful-robocalls) expands DNO blocking obligations. Previously, only gateway providers were required to block calls from DNO numbers. Under the new rules, **all U.S. voice service providers in the call path** must block outbound calls that appear to originate from a number on a "reasonable DNO list."

This obligation applies to any entity listed in the RMD as a voice service provider, gateway provider, or non-gateway intermediate provider, regardless of position in the call path.

### What Is a DNO List

A DNO list identifies numbers that should never originate outbound calls — for example, inbound-only government hotlines or numbers associated with impersonation scams. DNO protection prevents bad actors from spoofing trusted inbound-only numbers to blast fraudulent outbound calls.

### Four Categories of a Reasonable DNO List

1. **Invalid Numbers** — Not dialable under the North American Numbering Plan (e.g., invalid NPA-NXX formats).
2. **Unallocated Numbers** — Valid NANP numbers never assigned to a provider.
3. **Unused Numbers** — Numbers allocated to a provider but not yet assigned to an end user.
4. **Numbers Requested for DNO Blocking** — Inbound-only numbers whose owner has requested DNO protection, including government inbound-only numbers and private-sector inbound-only numbers used in impersonation scams.

Providers may include additional categories as long as the list remains "reasonable" under the Order. The FCC does not mandate a single centralized list.

## Reassigned Numbers Database

Authorized by the FCC in December 2018, the [Reassigned Numbers Database](https://www.fcc.gov/reassigned-numbers-database) enables callers to determine whether a telephone number has been permanently disconnected, so they know the number is no longer assigned to the intended recipient.

As a service provider, Telnyx is mandated to submit data to the database monthly. Telnyx offers customers a **15-day reinstatement period** during which a previously disconnected number can be repurchased. After 15 days, the number is permanently disconnected and included in the next reporting period (which occurs on the 15th of each month). Once reported, the wider industry is made aware and should no longer attempt to contact the disconnected number.

Important considerations:
- Any consent previously given to third parties (e.g., pharmacies) to contact you through that number is no longer applicable; you must re-establish communications.
- If you buy back a number later, all previously associated settings must be manually reconfigured.

## SOC Compliance and Certifications

Telnyx undergoes independent audits validating its security and compliance controls. These SOC reports provide third-party assurance around data security, availability, confidentiality, and integrity across services including Programmable Voice, Messaging, Wireless, and Video.

| Certification | Focus | Customer Impact |
|---------------|-------|----------------|
| SOC 2 Type I | Control design at a point in time | Confirms security processes are properly structured |
| SOC 2 Type II | Operational effectiveness over a period | Demonstrates consistency and reliability over time |
| SOC 3 | Public summary of SOC 2 | Allows broad sharing without disclosing sensitive detail |

### Requesting SOC Reports

Detailed audit reports (e.g., SOC 2 Type II) are sensitive and shared under NDA. Request them via the [Telnyx Trust Center](https://trust.telnyx.com/) by selecting the desired report, logging in or completing the request form, and signing an NDA if required.

### Security Practices Validated by SOC Audits

- **Governance:** Formal information security program with documented policies covering security, availability, and confidentiality.
- **Risk & Compliance:** Periodic structured risk assessments with remediation tracking; alignment with NIST, ISO, and CIS frameworks.
- **Access Control:** Role-based access control (RBAC), least-privilege principles, MFA for administrative access, routine access reviews, and physical security controls at data centers.
- **Operations & Incident Response:** Continuous monitoring and alerting; defined incident response workflows.
- **Change Management & Secure Development:** Structured approval for infrastructure and software changes; static/dynamic scanning, penetration testing, and threat modeling prior to deployment.
- **Vendor Controls:** Security assessments before vendor engagement; contracts with confidentiality, security, and data return/deletion clauses; periodic vendor reviews.

## Privacy and Data Protection

### GDPR and CCPA Compliance

Telnyx complies with the GDPR (General Data Protection Regulation 2016/679) and CCPA. Personal data is processed according to legal obligations, and customer data is only used for authorized purposes or as required by law. Data subjects may access, correct, erase, or object to processing of their personal data through Telnyx's [Request to Control and Review Data](https://telnyx.com/request-to-control-review-data) mechanism. Telnyx responds to GDPR/CCPA rights requests within one month.

For full details, see the [Telnyx Privacy Policy](https://telnyx.com/privacy-policy).

### Data Locality

Telnyx offers a choice of where to store call detail records (CDRs) and message detail records (MDRs) at rest, providing data locality options.

### Processor and Controller Roles

Depending on usage, Telnyx may act as a data processor or controller, always ensuring compliance with contractual and legal privacy obligations.
