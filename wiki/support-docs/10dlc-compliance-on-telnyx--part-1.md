---
title: 10DLC Compliance on Telnyx
summary: 10DLC (10 Digit Long Code) is the mandatory US industry framework for application-to-person
  (A2P) SMS and MMS sent from standard 10-digit long code numbers. This page consolidates
  Telnyx's guidance on registration deadlines, brand and campaign setup, use cases,
  throughput, prohibited content, carrier error codes, and related compliance obligations.
sources:
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
- url: https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
- url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
- url: https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance
- url: https://support.telnyx.com/en/articles/6228388-aca-feedback-process
- url: https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging
- url: https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory
updated_at: 2026-08-05T13:24:50Z
---

# 10DLC Compliance on Telnyx

*Part 1 of 3 — see also: [Part 2](10dlc-compliance-on-telnyx--part-2.md), [Part 3](10dlc-compliance-on-telnyx--part-3.md)*

10DLC (10 Digit Long Code) is the mandatory US industry framework for application-to-person (A2P) SMS and MMS sent from standard 10-digit long code numbers. This page consolidates Telnyx's guidance on registration deadlines, brand and campaign setup, use cases, throughput, prohibited content, carrier error codes, and related compliance obligations.

## Overview of 10DLC

10 Digit Long Code (10DLC) is the industry standard that governs application-to-person (A2P) SMS and MMS traffic sent from traditional 10-digit US long code numbers. It was introduced in 2021 to give businesses a sanctioned platform for sending A2P messages on long codes, with the goals of protecting consumers from spam and improving deliverability through higher throughput than legacy P2P long code traffic.

From **February 3, 2025**, any 10DLC traffic that is not registered is blocked altogether. This enforcement was driven by The Campaign Registry (TCR) and the major US mobile operators, not by Telnyx. Telnyx had been alerting customers about the change since November 2023 through email and portal banners.

10DLC does not support handset receipts (use short code or toll-free instead) and does not currently support Free To End User programs.

## Who 10DLC Applies To

10DLC applies to virtually all traffic sent by — or on behalf of — businesses from +1 long code numbers (not toll-free or short code). This includes:

- Businesses currently sending A2P traffic over long codes.
- Resellers and Independent Service Vendors (ISVs) whose customers send A2P traffic over long codes.

Toll-free numbers are not governed by 10DLC, though they require their own registration. See [Toll-Free Messaging](toll-free-messaging.md) for details.

P2P traffic is technically exempt, but in practice almost all messages sent by a business — even if manually triggered — are treated as A2P. A P2P exemption is only available if messages are not sent on behalf of any business, the sender is not a cloud communications suite, all messages are written and sent by individuals, traffic is roughly symmetrical (1:1 or 1:3 max), and the business has an excellent compliance history with Telnyx.

## Key Players in the 10DLC Ecosystem

- **Brands** — The trading identity of the business sending messages, tied to an Employer Identification Number (EIN). One Brand per EIN.
- **Mobile Network Operators (MNOs)** — AT&T, T-Mobile (and Sprint), Verizon, and UScellular. Each MNO sets its own throughput rules.
- **Third-Party Vetting Partners** — Aegis Mobile, WMC Global, and CampaignVerify (the designated vetting partner for political campaigns).
- **The Campaign Registry (TCR)** — The central hub that maintains the database of approved 10DLC brands and campaigns and interfaces directly with the MNOs.

## How to Register for 10DLC

To comply with 10DLC, a business must:

1. Register a Brand.
2. (Recommended) Vet the Brand to obtain a Vetting Score.
3. Register a Campaign describing the use case.
4. Assign phone numbers to the campaign.
5. Await manual review by TCR and the carriers.
6. Send traffic under those campaign numbers according to 10DLC guidelines and the declared use case.

Failure to complete these steps can result in throttled traffic, higher fees, and fines from carriers.

Registration can be completed through the [Mission Control Portal](mission-control-portal.md) or via the 10DLC API endpoints. Non-US brands can be added through the portal, but all 10DLC rules and penalties still apply.

For step-by-step instructions, see [Register for 10DLC Messaging](register-for-10dlc-messaging.md), [How to create a 10DLC brand](how-to-create-a-10dlc-brand.md), and [How to create a 10DLC campaign](how-to-create-a-10dlc-campaign.md).

## Relationship Between Brands, Numbers, and Campaigns

- **Brands per organization:** One Brand per EIN.
- **Campaigns per Brand:** Up to five.
- **Numbers per Campaign:** Multiple. As of September 2023, the T-Mobile limit is 49 numbers per campaign.
- **Campaigns or Brands per Number:** A number can only belong to one Campaign and its parent Brand.

If you cannot add a number to a campaign even though you have fewer than 49, you may have hit the industry's daily number-adding limit; try again in one business day.

When porting numbers into Telnyx, create and get the 10DLC campaigns approved first, then port the numbers, and have the losing carrier remove the campaigns from their system before the port completes.

## Brand Score, Brand Tier, and Vetting Score

As of mid-2023, Brand Score has been deprecated in favor of **Brand Tier**, which is determined by the **Vetting Score**. Brand Tier is used by carriers — especially T-Mobile and AT&T — to help calculate throughput.

A Brand without a Vetting Score will tend to receive low throughput for complex use cases such as Marketing. Telnyx strongly recommends Vetting for any campaign with material traffic or complex compliance requirements.

Vetting can be ordered by editing a Verified Brand in the portal and completing a Brand Vetting, or by entering a Vetting ID/token from an external vetting, or via the Vetting Endpoints in the 10DLC API.

## Throughput

Throughput is the maximum number of messages you can send in a given period — segments per second (MPS), per minute (MPM), or per day. A message segment is up to 160 standard GSM-7 characters; longer messages or messages with non-GSM characters are split into multiple segments. Telnyx supports up to 10 segments before rejecting a message as too long. In multi-part SMS, each segment is limited to 153 characters because of the 7-byte User Data Header.

### AT&T (Message Class-based)

AT&T sets throughput per Campaign based on the AT&T "Message Class," which is determined by use case and (in many cases) Vetting Score. Russell 3000 brands may default to a high score without vetting.

| Class | Use Case | Vetting Score | TPM (SMS) | TPM (MMS) | Variable Rate |
| --- | --- | --- | --- | --- | --- |
| A, B | Dedicated, Mixed / Marketing | 75–100 | 4500 | 2400 | Y |
| C, D | Dedicated, Mixed / Marketing | 50–74 | 2400 | 1200 | Y |
| E, F | Dedicated, Mixed / Marketing | 1–49 | 240 | 150 | Y |
| T | Basic / Unregistered | 0 / NA | 75 | 50 | N/A |

Special use case classes include Political (Class K, 4500 SMS / 2400 MMS TPM, vetting mandatory) and UCaaS Low/High Volume variants.

### T-Mobile (Brand-based)

T-Mobile sets throughput at the Brand level as a daily cap shared across all campaigns.

| Brand Tier | Vetting Score | T-Mobile Daily Cap |
| --- | --- | --- |
| Top | 75–100 | 200,000 |
| High Mid | 50–74 | 40,000 |
| Low Mid | 25–49 | 10,000 |
| Low | 1–24 | 2,000 |

Unvetted brands that are not on the Russell 3000 may default to a Low Brand Tier for T-Mobile.

### Verizon

Verizon has not declared throughput guidance, but as a member of TCR, following 10DLC best practices is required to deliver to Verizon customers.

### MMS

10DLC campaigns include both SMS and MMS. MMS throughput is unchanged from SMS, but the carrier surcharge for MMS is higher. Undeclared industry MMS limits as of April 2023 were approximately 0.84 MPS / 50 MPM per number on AT&T and T-Mobile, and 25 MPS on Verizon.
