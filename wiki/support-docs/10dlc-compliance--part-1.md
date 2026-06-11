---
title: 10DLC Compliance
summary: 10DLC (10 Digit Long Code) is the mandatory compliance framework for application-to-person
  (A2P) SMS and MMS traffic sent from US local long-code numbers. All businesses must
  register a Brand and Campaign through The Campaign Registry (TCR) or face blocked
  traffic, higher fees, and substantial fines from mobile network operators.
sources:
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
- url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
- url: https://support.telnyx.com/en/articles/5593977-isvs-10dlc
- url: https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges
- url: https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance
- url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
- url: https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging
- url: https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory
updated_at: 2026-06-11T11:10:47Z
---

# 10DLC Compliance

*Part 1 of 3 — see also: [Part 2](10dlc-compliance--part-2.md), [Part 3](10dlc-compliance--part-3.md)*

10DLC (10 Digit Long Code) is the mandatory compliance framework for application-to-person (A2P) SMS and MMS traffic sent from US local long-code numbers. All businesses must register a Brand and Campaign through The Campaign Registry (TCR) or face blocked traffic, higher fees, and substantial fines from mobile network operators.

## Overview of 10DLC

10DLC governs A2P texting using traditional 10-digit phone numbers in the United States. Introduced in 2021, it protects consumers from spam while giving businesses higher messaging throughput than person-to-person (P2P) long-code routes. As of **February 4, 2025**, all unregistered 10DLC traffic is blocked—registration is no longer optional.

The key players in the 10DLC ecosystem are:

- **Brands** — Business identities tied to an Employer Identification Number (EIN).
- **Mobile Network Operators (MNOs)** — AT&T, T-Mobile (including Sprint), Verizon, and UScellular. Each sets its own throughput rules.
- **The Campaign Registry (TCR)** — The central hub appointed by carriers to manage 10DLC Brands and Campaigns.
- **Third-Party Vetting Partners** — Aegis Mobile, WMC Global, and CampaignVerify (for political campaigns). Vetting produces a score that can increase throughput.

Telnyx provides tools via the Mission Control Portal and APIs to create Brands, Campaigns, and assign numbers, interfacing directly with TCR. However, compliance responsibility—and any resulting fees or fines—rests with the business.

## Who Must Register

10DLC applies to virtually all traffic sent by or on behalf of a business from +1 long-code numbers (excluding Toll-Free and Short Code). This includes:

- Businesses currently sending A2P traffic over long codes.
- Resellers and Independent Service Vendors (ISVs) whose customers send A2P traffic.

Even messages manually triggered by a human are generally considered A2P. P2P exemptions are rare and require that messages are not sent on behalf of any business, are written and sent by individuals, traffic is roughly symmetrical (1:1 or 1:3), and the business has an excellent compliance history. Contact support to request a P2P Carrier Use Case Questionnaire if you believe you qualify.

Toll-Free numbers are not covered by 10DLC but have their own registration requirements (see [Toll-Free Messaging](toll-free-messaging.md)). 10DLC does not support handset receipts or Free-To-End-User programs.
