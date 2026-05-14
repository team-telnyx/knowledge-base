---
title: Telnyx Security, Encryption, and Regulatory Compliance Overview
summary: A concise guide to Telnyx’s SOC certifications, privacy posture, voice encryption
  options, and key U.S. regulatory requirements affecting customers—covering the FCC’s
  STIR/SHAKEN third‑party authentication rules, Do‑Not‑Originate (DNO) blocking, and
  Texas’s Mini‑TCPA updates for text messaging.
sources:
- url: https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications
  content_hash: ce1a46fb6cdc61500b014fa36be4fef9ff54799cac1ab1f79895c3d313f1dd63
- url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
  content_hash: a99b27606087d7002b2047e39dcfe625961169e2e6fd7a0c2fd772627f68abd8
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
  content_hash: 47161a2c5429a1a0c5537425d3d57631406ff48eb0fa046c606d5e405adef26a
- url: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
  content_hash: bc75b87c95ae11b0cb265b6af5ce086ce3666a3d1e4fa43ef094e8f74a3a4edf
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
  content_hash: 3d84d9f16afa2941c930560e572b4e15b7686bdedbb8e91829115ac823a05308
updated_at: 2026-05-14T11:41:52Z
---

# Telnyx Security, Encryption, and Regulatory Compliance Overview

*Part 1 of 2 — see also: [Part 2](telnyx-security-encryption-and-regulatory-compliance-overview--part-2.md)*

A concise guide to Telnyx’s SOC certifications, privacy posture, voice encryption options, and key U.S. regulatory requirements affecting customers—covering the FCC’s STIR/SHAKEN third‑party authentication rules, Do‑Not‑Originate (DNO) blocking, and Texas’s Mini‑TCPA updates for text messaging.

## SOC compliance and certifications
Telnyx undergoes independent SOC audits that provide third‑party assurance over security, availability, confidentiality, and integrity.

- SOC 2 Type I: Evaluates control design at a point in time.
- SOC 2 Type II: Assesses operating effectiveness over a period.
- SOC 3: Public, high‑level summary of SOC 2.

Certifications cover services including Programmable Voice, Messaging, Wireless, and Video.

## How to access SOC reports
Sensitive trust documents (e.g., SOC 2 Type II) are available under NDA via the Trust Center at https://trust.telnyx.com.

- Go to trust.telnyx.com
- Select the report (e.g., SOC 2 Type II)
- Log in or submit the request form
- Be prepared to sign an NDA for full reports

## Practices validated by SOC audits
- Governance and policy: Formal information security program with documented policies.
- Risk and compliance: Periodic risk assessments; risk‑based alignment with frameworks (e.g., NIST, ISO, CIS).
- Access control: RBAC, least privilege, MFA for elevated access, routine reviews, timely deprovisioning; physical data center controls.
- Operations and incident response: Continuous monitoring and alerting; defined response workflows.
- Change management and secure development: Structured change approvals; SAST/DAST, penetration testing, and threat modeling.
- Vendor management: Due‑diligence assessments, contractual safeguards, and periodic reviews.

## Privacy and data handling
Telnyx maintains commitments reflected in its Privacy Policy (https://telnyx.com/privacy-policy):

- GDPR/CCPA compliance and lawful processing.
- Limited use and purpose restriction of customer data.
- Data subject rights (access, correction, erasure, objection) via request mechanisms.
- Data locality options for CDRs/MDRs at rest.
- Processor/controller roles determined by use case with contractual safeguards.

## Voice encryption options (TLS/SRTP)
By default, calls are not encrypted. If your equipment supports it, enable TLS for SIP signaling and SRTP for RTP media to encrypt traffic.

- Outbound: Configure your device for TLS and SRTP—no extra Telnyx portal setup needed.
- Inbound: Enable TLS/SRTP on the Connections page in the Telnyx portal (Voice → SIP Trunking → Connection settings). See TLS/SRTP details at https://support.telnyx.com/en/articles/4404575-tls-and-srtp.
- Network posture: Telnyx uses a private backbone to carry media off the public internet where possible, reducing exposure to public hops.

## FCC Eighth Report and Order: third‑party authentication for STIR/SHAKEN
Effective September 18, 2025, the FCC prohibits “third‑party authentication” unless the originating service provider (OSP):

1) Independently determines attestation levels per STIR/SHAKEN standards; and
2) Authenticates calls using its own certificate from a STIR/SHAKEN Certificate Authority (issued via its SPC token from the Policy Administrator), not a third party’s certificate.

Providers certifying “Partial” or “Complete” STIR/SHAKEN in the Robocall Mitigation Database (RMD) must be registered with the Policy Administrator, obtain their own SPC token, get a certificate from an approved CA, and sign calls with that certificate. The Order: https://docs.fcc.gov/public/attachments/FCC-24-120A1.pdf

## Who needs an SPC token (and when Telnyx will require it)
OSPs with control over their network infrastructure must obtain an SPC token and certificate.

Telnyx will require you to secure your own SPC token if you:
- Use Telnyx alongside another provider and either send calls using numbers from another operator across Telnyx’s network, or send calls from Telnyx numbers across another provider’s network; or
- Spoof caller ID (only if whitelisted for legitimate spoofing).

Telnyx will not require an SPC token if you:
- Exclusively use Telnyx numbers for both origination and termination; or
- Use only a limited number of outside Verified Numbers (see https://support.telnyx.com/en/articles/6790265-verified-numbers-faq).

RMD implications:
- Pure resellers without network control cannot claim “Partial” or “Complete” STIR/SHAKEN and must select “No STIR/SHAKEN Implementation” (47 CFR 64.6305(d)(2)(i)).
- If you claimed “Partial/Complete,” Telnyx cannot sign calls on your behalf. Update your RMD if you are a pure reseller.

## How to obtain and use your STIR/SHAKEN certificate
If you qualify as an OSP with an implementation obligation:

1) Obtain an OCN (Company Code) from NECA: https://www.neca.org/business-solutions/company-codes
2) Prepare to file FCC Form 499‑A (FRN via CORES, Filer ID via USAC): https://www.usac.org/wp-content/uploads/service-providers/documents/forms/2025/2025-FCC-Form-499A-Form-Instructions.pdf
3) Register in the Robocall Mitigation Database (requires CORES/FRN): https://www.fcc.gov/sites/default/files/rmd-instructions.pdf
4) Register with the STI‑PA (iConectiv) and obtain your SPC token: https://authenticate.iconectiv.com/service-provider-authenticate
5) Select an approved Certification Authority and obtain your STIR/SHAKEN certificate (using your SPC token).
6) Sign your own calls with Telnyx: Use Telnyx’s Hosted Signing Service to apply your certificate and control attestation (A/B/C). Product guide: https://developers.telnyx.com/docs/development/stir-shaken/hosted-cert

## Do‑Not‑Originate (DNO) blocking obligations (effective December 15, 2025)
Under FCC 25‑15, all U.S. voice service providers in the call path (voice, gateway, and non‑gateway intermediate providers) must block calls that appear to originate from numbers on a “reasonable DNO list.” Rulemaking reference: https://www.federalregister.gov/documents/2025/03/24/2025-04811/advanced-methods-to-target-and-eliminate-unlawful-robocalls

What constitutes a reasonable DNO list:
- Invalid numbers: Not dialable under the NANP (e.g., invalid NPA‑NXX patterns).
- Unallocated numbers: Valid NANP numbers never assigned to a provider.
- Unused numbers: Allocated to a provider but not yet assigned to an end user.
- Numbers requested for DNO blocking: Inbound‑only numbers (including government and private‑sector numbers), added at the number owner’s request—especially those at risk of impersonation scams.

Providers may include additional categories as long as the list remains reasonable under the Order.

## Texas Mini‑TCPA update: texting now covered (effective September 1, 2025)
Texas SB 140 extends telemarketing rules to promotional/sales text messages and may require registration for businesses based in Texas or marketing to Texas residents: https://capitol.texas.gov/tlodocs/89R/billtext/pdf/SB00140F.pdf

Key changes:
- Texts treated the same as telemarketing calls (any voice or “other transmission,” including text/graphic/image, to induce a purchase).
- Quiet hours apply to texts: Mon–Sat 9 a.m.–9 p.m.; Sun 12 p.m.–9 p.m. (recipient local time), with limited exceptions (see Sec. 301.051: https://statutes.capitol.texas.gov/SOTWDocs/BC/htm/BC.301.htm).
- Registration: Covered businesses may need to register with the Texas Secretary of State, pay a $200 fee, and post a $10,000 security deposit (how‑to: https://www.sos.state.tx.us/statdoc/faqs3400.shtml). Failure to register may incur civil penalties up to $5,000 per violation.
- Exemptions: Multiple categories (e.g., existing customers, certain financial institutions, insurers, utilities with limits, newspapers/magazines/cable, nonprofits, schools, etc.; see Sec. 302.051: https://statutes.capitol.texas.gov/docs/BC/htm/BC.302.htm).
- Expanded private right of action: Violations (e.g., quiet hours, failure to register, ignoring opt‑outs, use of autodialers) are actionable per instance, including mental anguish damages.
