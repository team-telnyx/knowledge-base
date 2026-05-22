---
title: 'STIR/SHAKEN, Robocall Mitigation, DNO, and RND: Telnyx Customer Guide'
summary: A single-source guide to U.S. and Canadian caller ID authentication and robocall
  rules that affect Telnyx customers, including STIR/SHAKEN obligations, the FCC’s
  Eighth Report and Order on third‑party authentication, Robocall Mitigation Database
  (RMD) requirements, Do‑Not‑Originate (DNO) blocking, SHAKEN/STIR SIP parameters,
  and the U.S. Reassigned Numbers Database (RND)—plus how Telnyx helps you comply
  and what actions you may need to take.
sources:
- url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
  content_hash: 303e197a9170ba9c7e2caa745e2089e3eb6189836aee9d8067adaa99276820b2
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
  content_hash: 47161a2c5429a1a0c5537425d3d57631406ff48eb0fa046c606d5e405adef26a
- url: https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx
  content_hash: 301e3fe00c35728d1f2013b3720b1e6fa3cbc8bc101235d24de1bfdc18efe0fb
- url: https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database
  content_hash: 4656996b55997e507c6960d9866dbbfbd806d7a7ac18dfcf62812e7c9299bd6f
- url: https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs
  content_hash: bf74e92542f38639d5b5961f0651ad2dbc915d065c4350392878558a519c3947
- url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
  content_hash: 6a9e9aefa0f424485db3c0863b483dd08fd578c975c068c17c6c3a2d2bc3ed51
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
  content_hash: 3ec2ba1a3de87e24ab0c034e37eda87d7294f963884ecd555a8f498b70b3f9b9
- url: https://support.telnyx.com/en/articles/5883839-what-is-the-reassigned-numbers-database
  content_hash: d6e479b687e46cb9d59909bf775d2717001710dc2f33c96044b00513ee1c65dc
- url: https://support.telnyx.com/en/articles/6228388-aca-feedback-process
  content_hash: 6b841cce9bb35df1c5d4b9941cc6992a8aaeff1bc56a68a38c41b5a3c20ca5ea
- url: https://support.telnyx.com/en/collections/12044103-regulatory
  content_hash: fb21e7dd688a6dcf7d864cbe57092f47e5e7f5c53bd7e4ced802d53e876db5bf
updated_at: 2026-05-20T14:39:18Z
---

# STIR/SHAKEN, Robocall Mitigation, DNO, and RND: Telnyx Customer Guide

*Part 1 of 2 — see also: [Part 2](stir-shaken-robocall-mitigation-dno-and-rnd-telnyx-customer-guide--part-2.md)*

A single-source guide to U.S. and Canadian caller ID authentication and robocall rules that affect Telnyx customers, including STIR/SHAKEN obligations, the FCC’s Eighth Report and Order on third‑party authentication, Robocall Mitigation Database (RMD) requirements, Do‑Not‑Originate (DNO) blocking, SHAKEN/STIR SIP parameters, and the U.S. Reassigned Numbers Database (RND)—plus how Telnyx helps you comply and what actions you may need to take.

## Key dates and scope

- STIR/SHAKEN has been in effect since June 30, 2021; small providers were required to sign their own calls starting June 30, 2022.
- FCC Eighth Report and Order on third‑party authentication takes effect September 18, 2025. It restricts “third‑party authentication” for originating service providers (OSPs) with a STIR/SHAKEN obligation.
- New DNO blocking rules apply to all U.S. voice service providers in the call path beginning December 15, 2025.

This page summarizes what these changes mean for Telnyx customers operating in the U.S. and Canada.

## STIR/SHAKEN basics and what to expect from Telnyx

- STIR/SHAKEN authenticates caller ID for IP voice. Originating providers attach an Identity header and an attestation level that is validated downstream.
- Attestation levels:
  - Full (A): Provider knows the customer, the right to use the number, and that the call originated on its network.
  - Partial (B): Provider knows the customer but not the number’s right‑to‑use details.
  - Gateway (C): Provider cannot verify the customer and/or number.
- Telnyx authenticates every outbound call with a valid U.S. caller ID that originates on the Telnyx platform and applies attestation per the above. To increase the likelihood of A attestation, port numbers to Telnyx.
- On‑net calls that carry Identity/verstat headers require TCP or TLS transport to avoid SIP header fragmentation; UDP is not supported for Identity header pass‑through.

## Canada: STIR/SHAKEN and accessibility

- For Canadian CLIs, Telnyx (via Canadian partners) handles SHAKEN/STIR signing—no customer action or extra cost. Attestation logic mirrors U.S. behavior (A when your Canadian CLI is in your Mission Control account; otherwise B).
- Accessibility feedback (Canada): To provide feedback in line with the Accessible Canada Act, email acafeedback@telnyx.com with your name, phone, email, relation to Telnyx, and a description of your feedback.

## FCC Eighth Report and Order: third‑party authentication

The FCC prohibits “third‑party authentication” where a provider subject to STIR/SHAKEN contracts a third party to sign calls, unless BOTH are true:

1) The provider independently determines attestation levels per STIR/SHAKEN standards; and
2) The provider authenticates calls using its own certificate issued from a STIR/SHAKEN Certificate Authority (CA) using its own SPC token.

If you certify “Partial” or “Complete” STIR/SHAKEN in the Robocall Mitigation Database (RMD), you must be registered with the STIR/SHAKEN Policy Administrator (STI‑PA), obtain your own SPC token, use it to obtain a certificate from an approved CA, and sign calls with that certificate. Otherwise, using a third party to sign constitutes a violation of caller ID authentication rules. See the Order: https://docs.fcc.gov/public/attachments/FCC-24-120A1.pdf

### Who must secure their own SPC token (Telnyx guidance)

You will need your own SPC token if you are an OSP with control over your network infrastructure and, for example:

- You use both Telnyx and another provider and either:
  - Send calls using numbers from another operator across Telnyx’s network; or
  - Send calls from Telnyx numbers across another provider’s network.
- You intend to legitimately spoof caller ID (only if whitelisted).

You generally do not need your own SPC token under Telnyx policies if:

- You exclusively use Telnyx numbers for origination and termination; or
- You use only a limited number of outside Verified Numbers (see: https://support.telnyx.com/en/articles/6790265-verified-numbers-faq).

### RMD certification implications

- Pure resellers without control over network infrastructure cannot claim “Partial” or “Complete” STIR/SHAKEN in RMD filings (see 47 CFR 64.6305(d)(2)(i)). They must select “No STIR/SHAKEN Implementation” with an explanatory note.
- If you have certified “Complete” or “Partial” in the RMD, Telnyx will not sign calls on your behalf; you must sign using your own certificate.
- If you mis‑certified (e.g., you are a pure reseller), update your RMD registration to reflect your actual status.

## How to obtain your own STIR/SHAKEN credentials

If you qualify as an OSP with a STIR/SHAKEN implementation obligation:

1) Obtain an Operating Company Number (OCN/Company Code) from NECA: https://www.neca.org/business-solutions/company-codes
2) Prepare to file FCC Form 499‑A (get an FRN via CORES and a USAC Filer ID). 2025 499‑A instructions: https://www.usac.org/wp-content/uploads/service-providers/documents/forms/2025/2025-FCC-Form-499A-Form-Instructions.pdf
3) Register in the FCC Robocall Mitigation Database (RMD). Filing instructions: https://www.fcc.gov/sites/default/files/rmd-instructions.pdf
4) Register with the STI‑PA (iConectiv) and obtain your SPC token. Guidance: https://authenticate.iconectiv.com/service-provider-authenticate
5) Choose an STI‑PA‑approved Certificate Authority. Use your SPC token to obtain your STIR/SHAKEN certificate.
6) Sign your own calls. Telnyx’s Hosted Signing Service lets you use your certificate and retain control of attestation while avoiding in‑house signing infrastructure. Product guide: https://developers.telnyx.com/docs/development/stir-shaken/hosted-cert

## Robocall Mitigation Database (RMD)

- Since September 28, 2021, U.S. intermediate and voice service providers must block traffic from providers not listed in the RMD. This applies to U.S. and (as of April 11, 2023) foreign providers that use U.S. NANP resources.
- Who is a “voice service provider”: see 47 C.F.R. 64.1600(r)(1).
- Before filing, obtain a CORES account and FRN: https://apps.fcc.gov/cores/userLogin.do
- Your RMD filing includes: business/ownership info; your role(s) (voice service provider, gateway provider, non‑gateway intermediate provider); U.S. or foreign status; certification of STIR/SHAKEN implementation (full/partial/none); and a robocall mitigation plan.
- All providers, including those not implementing STIR/SHAKEN (e.g., intermediates or those lacking network control), must file certifications and mitigation plans describing reasonable steps to prevent illegal robocalls (see FCC 24‑73, FCC 23‑18).
- Consult legal counsel to determine filing obligations for your entity.

## Do‑Not‑Originate (DNO) requirements (effective December 15, 2025)

- Historically, only gateway providers had to block calls that appeared to originate from numbers on their DNO lists. Under the new rules (FCC 25‑15), all U.S. providers in the call path must block calls that appear to originate from numbers on a “reasonable DNO list.” Federal Register summary: https://www.federalregister.gov/documents/2025/03/24/2025-04811/advanced-methods-to-target-and-eliminate-unlawful-robocalls
- A reasonable DNO list covers at least:
  1) Invalid numbers (not dialable under NANP);
  2) Unallocated numbers (valid format but never assigned to a provider);
  3) Unused numbers (allocated to a provider but not assigned to an end user);
  4) Numbers the owner has requested for DNO blocking (e.g., inbound‑only government hotlines or private inbound‑only numbers used in impersonation scams, upon request).
- Obligation applies if you are listed in the RMD as a voice service provider, gateway provider, or non‑gateway intermediate provider.
