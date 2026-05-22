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
