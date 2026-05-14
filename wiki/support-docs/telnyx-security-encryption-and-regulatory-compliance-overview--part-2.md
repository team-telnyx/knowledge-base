---
title: Telnyx Security, Encryption, and Regulatory Compliance Overview
summary: A concise guide to Telnyx’s SOC certifications, privacy posture, voice encryption
  options, and key U.S. regulatory requirements affecting customers—covering the FCC’s
  STIR/SHAKEN third‑party authentication rules, Do‑Not‑Originate (DNO) blocking, and
  Texas’s Mini‑TCPA updates for text messaging.
sources:
- url: https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications
- url: https://support.telnyx.com/en/articles/10806916-understanding-the-fcc-s-eighth-report-and-order-on-third-party-authentication
- url: https://support.telnyx.com/en/articles/12933869-understanding-the-fcc-s-new-do-not-originate-dno-requirements-effective-december-15-2025
- url: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
- url: https://support.telnyx.com/en/articles/12141904-legal-update-texas-s-mini-tcpa-now-applies-to-texts
updated_at: 2026-05-14T11:41:52Z
---

# Telnyx Security, Encryption, and Regulatory Compliance Overview

*Part 2 of 2 — see also: [Part 1](telnyx-security-encryption-and-regulatory-compliance-overview--part-1.md)*

A concise guide to Telnyx’s SOC certifications, privacy posture, voice encryption options, and key U.S. regulatory requirements affecting customers—covering the FCC’s STIR/SHAKEN third‑party authentication rules, Do‑Not‑Originate (DNO) blocking, and Texas’s Mini‑TCPA updates for text messaging.

## Customer actions checklist
- Security and privacy
  - Create a Trust Center account and request needed SOC reports (under NDA as required).
  - Review your access control, change management, monitoring, and vendor practices against your obligations.
  - Configure data locality for CDRs/MDRs as needed; enable privacy request workflows.
- Encryption
  - Enable TLS/SRTP on devices and Telnyx Connections for encrypted signaling and media.
- STIR/SHAKEN compliance
  - Determine if you are an OSP with network control and if you claimed Partial/Complete in the RMD.
  - If required: obtain OCN, FRN/Filer ID (499‑A), RMD registration, STI‑PA SPC token, approved CA certificate; then sign calls using Telnyx’s Hosted Signing Service.
  - If a pure reseller without network control: update RMD to “No STIR/SHAKEN Implementation.”
- DNO blocking
  - Implement DNO screening against invalid, unallocated, unused, and owner‑requested inbound‑only numbers by December 15, 2025.
- Texas texting compliance
  - If based in Texas or texting Texas residents, assess registration requirements, honor quiet hours, maintain opt‑out processes, and evaluate exemptions.

## Disclaimers and support
- This page is for general informational purposes only and is not legal advice. Consult qualified counsel regarding your specific obligations.
- For regulatory questions, you may contact regulatory@telnyx.com.
- For product configuration and support, use the Telnyx portal and Help Center resources.
