---
title: 10DLC Campaign Registration and Compliance Guide
summary: A consolidated reference for registering and maintaining 10DLC (10-Digit
  Long Code) A2P messaging campaigns on Telnyx, covering message flow, opt-in forms,
  keywords, privacy policy, sample messages, vetting, shared campaigns, and common
  carrier errors.
sources:
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
- url: https://support.telnyx.com/en/articles/4557103-telnyx-privacy-policy
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
- url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
updated_at: 2026-08-05T13:25:10Z
---

# 10DLC Campaign Registration and Compliance Guide

*Part 1 of 5 — see also: [Part 2](10dlc-campaign-registration-and-compliance-guide--part-2.md), [Part 3](10dlc-campaign-registration-and-compliance-guide--part-3.md), [Part 4](10dlc-campaign-registration-and-compliance-guide--part-4.md), [Part 5](10dlc-campaign-registration-and-compliance-guide--part-5.md)*

A consolidated reference for registering and maintaining 10DLC (10-Digit Long Code) A2P messaging campaigns on Telnyx, covering message flow, opt-in forms, keywords, privacy policy, sample messages, vetting, shared campaigns, and common carrier errors.

## Overview

10DLC (10-Digit Long Code) is the carrier-mandated framework for application-to-person (A2P) SMS messaging on standard US long codes. Every brand and campaign must be registered with The Campaign Registry (TCR) and reviewed by carriers before traffic can be sent. Telnyx acts as the messaging service provider and, in most cases, the upstream connectivity partner (CNP) that shares the campaign with mobile network operators (MNOs).

Effective January 26, 2023, all new Telnyx US 10DLC campaign registrations (Standard, Low Volume Standard, and Sole Proprietor 2.0) are subject to a manual vetting process and a $15 campaign verification fee per submission or resubmission. If a campaign is denied, additional charges may apply on resubmission.

## Trust Scores, Throughput, and Use Cases

US A2P 10DLC throughput is set by your Trust Score and your campaign Use Case.

- **Throughput** is measured in message segments per second (MPS). Each segment is up to 160 GSM-7 characters; longer messages or non-GSM-7 encoding produce multiple segments. T-Mobile also imposes separate daily message limits toward its subscribers that require a special business review to exceed.
- **Trust Scores** are assigned to a Brand by a reputation algorithm at registration. The score does not change over time. It is believed to be driven primarily by brand footprint (larger brands score higher) and the quality and consistency of the brand registration (fewer discrepancies score better).
- **Use Cases** determine MPS and fees. Use cases range from marketing to operational (notifications, 2FA, customer care, etc.). Mixed-use campaigns allow reuse of a single phone number but typically carry higher fees than single-use-case campaigns.
- **Political campaigns** must additionally be verified at [campaignverify.com](https://campaignverify.com), which issues a token that must be associated with the campaign.

To confirm whether a use case is acceptable for a brand, use the Qualify By Use Case Endpoint. To request brand vetting, use the Brand API.

## Campaign Description

The campaign description must explain who the entity using the campaign is and what the campaign is intended for.

> Example: Appointment reminder and confirmation notifications for a dentist's office to remind their patients of newly scheduled and upcoming appointment dates and times.
