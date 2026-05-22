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
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
- url: https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx
- url: https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database
- url: https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs
- url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
- url: https://support.telnyx.com/en/articles/11358700-what-is-the-u-s-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/5883839-what-is-the-reassigned-numbers-database
- url: https://support.telnyx.com/en/articles/6228388-aca-feedback-process
- url: https://support.telnyx.com/en/collections/12044103-regulatory
updated_at: 2026-05-20T14:39:18Z
---

# STIR/SHAKEN, Robocall Mitigation, DNO, and RND: Telnyx Customer Guide

*Part 2 of 2 — see also: [Part 1](stir-shaken-robocall-mitigation-dno-and-rnd-telnyx-customer-guide--part-1.md)*

A single-source guide to U.S. and Canadian caller ID authentication and robocall rules that affect Telnyx customers, including STIR/SHAKEN obligations, the FCC’s Eighth Report and Order on third‑party authentication, Robocall Mitigation Database (RMD) requirements, Do‑Not‑Originate (DNO) blocking, SHAKEN/STIR SIP parameters, and the U.S. Reassigned Numbers Database (RND)—plus how Telnyx helps you comply and what actions you may need to take.

## SHAKEN/STIR SIP parameters and on‑net identity

- Telnyx includes the verstat parameter in P‑Asserted‑Identity to convey identity verification and attestation results for inbound PSTN and Telnyx on‑net calls.
- Verstat values include:
  - TN‑Validation‑Passed (A attestation)
  - TN‑Validation‑Passed‑B (B attestation)
  - TN‑Validation‑Passed‑C (C attestation)
  - TN‑Validation‑Failed (invalid/failed verification)
  - No‑TN‑Validation (no Identity header provided)
- To receive Identity headers on the B‑leg, ensure:
  - SHAKEN/STIR pass‑through is enabled on your connection, and
  - Transport is TCP or TLS (Identity headers are not sent over UDP to prevent fragmentation).

Example:
P-Asserted-Identity:"John Doe"<sip:+18889809750@sip.telnyx.com;verstat=TN-Validation-Passed>

## U.S. Reassigned Numbers Database (RND)

- The RND helps determine if a number has been permanently disconnected (and likely reassigned) since you obtained consent, reducing wrong‑party calls and TCPA risk. Overview: https://www.fcc.gov/reassigned-numbers-database and portal: https://www.reassigned.us
- Providers (including Telnyx) must submit permanently disconnected numbers monthly. Telnyx gives customers a 15‑day reinstatement window before reporting a disconnected number in the next monthly update.
- Query results and meaning:
  - Yes: Disconnected after your provided consent/last‑contact date (don’t call without new consent).
  - No: Not disconnected since that date (grants safe harbor if later found reassigned).
  - No Data: No record (no safe harbor).
- Who should use it: Businesses that place outbound calls/SMS to U.S. numbers and rely on prior consent should check the RND as part of TCPA compliance to maintain safe harbor protections.
- Registration and pricing: Email support@reassigned.us to request access; pricing by query‑volume tier: https://reassigned.us/pricing

## Practical compliance tips and next steps

- If you certify “Partial” or “Complete” STIR/SHAKEN in the RMD, obtain your own SPC token/certificate and sign your traffic; Telnyx can host signing while you control attestation.
- If you are a pure reseller without network control, certify “No STIR/SHAKEN Implementation” and maintain a robust robocall mitigation plan.
- Maintain and enforce a reasonable DNO list and ensure network blocking is in place by December 15, 2025.
- Use TCP/TLS on Telnyx connections to receive Identity/verstat headers on net and from the PSTN; review verstat data in your systems for fraud and routing decisions.
- Scrub outbound campaigns with the RND to reduce wrong‑party calls and preserve TCPA safe harbor.
- Ensure you are registered in the RMD (and, if applicable, CORES/FRN, USAC 499‑A, STI‑PA) and keep filings up to date.
- When in doubt, consult qualified counsel; Telnyx support can help with implementation details at support@telnyx.com.

Disclaimer: The information provided here is for general informational purposes only and should not be construed as legal advice. Consult qualified counsel for legal or regulatory guidance.
