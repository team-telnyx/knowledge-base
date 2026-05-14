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
