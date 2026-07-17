---
title: 10DLC Compliance and Registration
summary: 10DLC is the mandatory US carrier framework for A2P SMS and MMS traffic sent
  from +1 long code numbers. This page consolidates Telnyx's 10DLC guidance — including
  who it applies to, how to register a Brand and Campaign, throughput and vetting
  rules, message flow templates, fees and non-compliance fines, and the February 3,
  2025 enforcement deadline after which unregistered traffic is blocked.
sources:
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
- url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
- url: https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges
- url: https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance
- url: https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging
- url: https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory
updated_at: 2026-07-17T09:00:19Z
---

# 10DLC Compliance and Registration

*Part 1 of 5 — see also: [Part 2](10dlc-compliance-and-registration--part-2.md), [Part 3](10dlc-compliance-and-registration--part-3.md), [Part 4](10dlc-compliance-and-registration--part-4.md), [Part 5](10dlc-compliance-and-registration--part-5.md)*

10DLC is the mandatory US carrier framework for A2P SMS and MMS traffic sent from +1 long code numbers. This page consolidates Telnyx's 10DLC guidance — including who it applies to, how to register a Brand and Campaign, throughput and vetting rules, message flow templates, fees and non-compliance fines, and the February 3, 2025 enforcement deadline after which unregistered traffic is blocked.

## Overview

10 Digit Long Code (10DLC) is the mandatory industry compliance framework that governs application-to-person (A2P) SMS and MMS messaging sent from US (+1) long code numbers. Introduced in 2021, 10DLC was created by mobile carriers to protect consumers from spam while giving businesses a sanctioned way to send higher-throughput A2P traffic over local numbers. From **February 3, 2025**, any 10DLC traffic that is not registered is blocked altogether, and unregistered traffic is subject to significantly higher carrier fees.

## Who 10DLC Applies To

10DLC applies to virtually all traffic sent by — or on behalf of — businesses from +1 long code numbers (not Toll Free or Short Code). This includes:

- Businesses currently sending A2P traffic over long codes.
- Resellers and Independent Service Vendors (ISVs) with customers sending A2P traffic over long codes.

Toll-free numbers require separate registration but are not explicitly covered under 10DLC guidelines. Short codes are governed by their own program.

### P2P Exemptions

Person-to-person traffic is not strictly required to register, but Telnyx observes that most "P2P" use cases are in fact A2P and should be registered. You may qualify for P2P registration only if all of the following are true:

- Messages are not sent on behalf of any business or agent of a business.
- You are not a cloud communication service suite.
- All messages are written and sent by individuals to other individuals.
- Traffic is roughly symmetrical (1:1 or 1:3 max) and resembles normal human-to-human communication.
- Your business has an excellent compliance history (Telnyx reviews your traffic history with us, so this is typically only offered to long-term committed customers).

If you believe you qualify, contact support to request a Carrier P2P Use Case Questionnaire.

## Key Players

The 10DLC ecosystem is made up of four key roles:

- **Brands** — The trading identity of the business sending messages, tied to an Employer Identification Number (EIN).
- **Mobile Network Operators (MNOs)** — AT&T, T-Mobile (including former Sprint), Verizon, and UScellular. MNOs set throughput limits and charge per-message fees.
- **Third-Party Vetting Partners** — Aegis Mobile, WMC Global, and CampaignVerify (the designated vetting partner for political campaigns).
- **The Campaign Registry (TCR)** — The central hub that maintains the database of approved 10DLC brands and campaigns and interfaces directly with the MNOs.

## How to Register for 10DLC

To comply with 10DLC, you must:

1. Register a Brand.
2. (Optional but recommended) Vet the Brand.
3. Register a Campaign.
4. Assign numbers to the Campaign.
5. Await results of manual review.
6. Send traffic under those campaign numbers according to 10DLC guidelines and your declared Use Case(s).

Failure to complete these steps can result in throttled traffic, higher fees, and fines.

### Registration Steps with Telnyx

1. [Register your brand](https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand) by entering your business details in the Mission Control Portal.
2. [Create your campaign](https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign) by providing information about what type of messages you'll send.
3. [Assign your phone numbers](https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign) to your campaign.

You can submit registration requests via the Mission Control Portal or via the [10DLC API endpoints](https://developers.telnyx.com/docs/messaging/10dlc). Brand and Campaign information is passed to The Campaign Registry (TCR) for manual review, and Campaigns (but not Brands) are also manually reviewed by Carriers — an industry-wide mandatory step for all A2P 10DLC registrations.

### Porting Numbers to Telnyx

Before porting numbers to Telnyx, create your 10DLC campaigns in the Telnyx Portal and wait until they are approved. After approval, start the porting process, but before the numbers fully port, work with your old carrier to have the 10DLC campaigns removed from their system. Otherwise, the newly ported numbers will still be tied to the losing carrier and cannot be assigned to your Telnyx 10DLC campaigns.

## Relationship Between Brands, Numbers, and Campaigns

- **Brands per organization:** One Brand per EIN. Additional Brands require their own unique EIN.
- **Campaigns per Brand:** A Brand can have multiple Campaigns, with a maximum of five Campaigns per Brand.
- **Numbers per Campaign:** A Campaign can have multiple numbers. As of September 2023, the T-Mobile limit is 49 numbers. If you have fewer than 49 numbers but cannot add more, you may have hit the industry's daily number-adding limit — try again in one business day.
- **Campaigns or Brands per Number:** A Number can only be used in one Campaign and its parent Brand.

## Brand Score, Brand Tier, and Vetting Score

As of mid-2023, Brand Score has been deprecated in favor of Brand Tier, which is determined by Vetting Score. Brand Tier is used by Carriers — especially T-Mobile and AT&T — to help calculate throughput.

A Brand without a Vetting Score will tend to lead to low throughput for complex Campaign Use Cases like Marketing. Telnyx strongly recommends Vetting Scores for any Campaigns with material traffic or similarly complex compliance requirements.

You can order Brand Vetting by:

1. Editing a Verified Brand in the Portal and completing a Brand, then entering your Vetting ID or Vetting token from a completed External Vetting.
2. Using the [Vetting Endpoints](https://developers.telnyx.com/api/messaging/10dlc/create-brand-post) in the 10DLC API.
