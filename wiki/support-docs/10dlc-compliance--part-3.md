---
title: 10DLC Compliance
summary: 10DLC (10 Digit Long Code) is the mandatory compliance framework for application-to-person
  (A2P) SMS and MMS traffic sent from US local long-code numbers. All businesses must
  register a Brand and Campaign through The Campaign Registry (TCR) or face blocked
  traffic, higher fees, and substantial fines from mobile network operators.
sources:
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
  content_hash: f0ba52f0d5594e2b190d52c8f19837f1b60e58221649fee06bf212d56b645a3b
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
  content_hash: 07f91a97a3331277fd2fe0d2ef7e37178432594c87aa13969aef8b5e27450bbd
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
  content_hash: 54651f622c365df6722b1c021dfed1349e1958ce387be017a8f2734d21580362
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
  content_hash: 3b46b15924c5883df3214410e67c0f02bb14ecb0ee3cd1769996715b6c891e90
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
  content_hash: bd106bb9b5cb7262013679d900f6eaab74650e6565c5a676a247379f6c7c0d07
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
  content_hash: 25c1106c094619bdd2dc507005df38013bd5d4b5e533642f3494ddd6ee53d1a2
- url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
  content_hash: 1137a07baf13fe64132a3219624937bbbc57bba59e3b758b65c2af66d4e002f7
- url: https://support.telnyx.com/en/articles/5593977-isvs-10dlc
  content_hash: c1fc8664b49abe4a12b5e529bd13933add28eeb490d171b93c83d71e6f1f3100
- url: https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges
  content_hash: 0f2a10c9c17383440e0efc0772db0f218dc4fbfcf3977f66512353fd66fa4c24
- url: https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance
  content_hash: ec7b612bdbdb4209316d95e83815cd41d0347d83e43fed9c8fa52370395bf13b
- url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
  content_hash: 24ce24f29ae0ad50ee8429b666d8436473df95655e27374ecd768b5954843800
- url: https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging
  content_hash: d321f07c0c4fd433b360fb23f5dccef8cc71daab7ae9eae00357918b1638bb0e
- url: https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory
  content_hash: 7fb43f7ce8d0a2e8b017ea3bc178e938063a04a87ce716bb4cdce84ecfdc9569
updated_at: 2026-06-11T11:10:47Z
---

# 10DLC Compliance

*Part 3 of 3 — see also: [Part 1](10dlc-compliance--part-1.md), [Part 2](10dlc-compliance--part-2.md)*

10DLC (10 Digit Long Code) is the mandatory compliance framework for application-to-person (A2P) SMS and MMS traffic sent from US local long-code numbers. All businesses must register a Brand and Campaign through The Campaign Registry (TCR) or face blocked traffic, higher fees, and substantial fines from mobile network operators.

## ISV (Independent Service Vendor) Requirements

An ISV sells products or services to other businesses that are the actual message senders. ISVs must:

- Create a **separate Brand** for each end-user business.
- Create **separate Campaigns** for each end-user.
- **Never share phone numbers across Brands**—each number must be associated with only one Brand/Campaign. Violating this can result in fines and blocked traffic.

To migrate shared-number architectures, iteratively create dedicated messaging profiles, buy or assign dedicated phone numbers, create Brands and Campaigns per end-user, and assign numbers accordingly.

Alternatives to per-end-user Brands include: (1) Using one brand/campaign with an approved T-Mobile Number Pooling agreement (unlikely unless you are a franchise), or (2) Using Number Lookup tools to identify and exclude T-Mobile subscribers. Using one brand/campaign across end-users without MNO approval **will likely result in fines and traffic blocking**.

## Brand Vetting and Throughput

### Vetting Score

A **Vetting Score** is strongly recommended for campaigns with material traffic or complex compliance requirements. A brand without a vetting score will tend to receive low throughput for complex use cases like Marketing.

Order vetting by editing a Verified Brand in the Portal and entering a vetting ID/token from completed external vetting, or use the [10DLC API vetting endpoints](https://developers.telnyx.com/api/messaging/10dlc/create-brand-post).

### AT&T Throughput (Message Class-based)

AT&T sets throughput per Campaign based on Message Class, determined by Use Case and Vetting Score:

| Message Class | Use Case | Vetting Score | SMS TPM | MMS TPM |
|---|---|---|---|---|
| A, B | Dedicated, Mixed/Marketing | 75–100 | 4,500 | 2,400 |
| C, D | Dedicated, Mixed/Marketing | 50–74 | 2,400 | 1,200 |
| E, F | Dedicated, Mixed/Marketing | 1–49 | 240 | 150 |
| T | Basic/Unregistered | 0/N/A | 75 | 50 |

Common Special Use Cases:

| Message Class | Use Case | SMS TPM | MMS TPM |
|---|---|---|---|
| K | Political | 4,500 | 2,400 |
| T | UCaaS Low Vol | 75 | 50 |
| B/D/F | UCaaS High Vol | 240/2,400/4,500 | 150/1,200/2,400 |

Vetting is mandatory for political campaigns. Russell 3000 brands may default to a high score immediately.

### T-Mobile Throughput (Brand-level Daily Cap)

T-Mobile sets a daily messaging limit at the Brand level shared across all Campaigns:

| Brand Tier | Vetting Score | Daily Cap |
|---|---|---|
| Top | 75–100 | 200,000 |
| High Mid | 50–74 | 40,000 |
| Low Mid | 25–49 | 10,000 |
| Low | 1–24 | 2,000 |

Brands not vetted and not on the Russell 3000 may default to Low tier.

### Verizon Throughput

Verizon has not declared specific throughput guidance as of September 2023 but is part of 10DLC, so compliance is still required.

### MMS Throughput

10DLC Campaigns include both SMS and MMS. MMS throughput does not change based on vetting, but carrier surcharges are higher. Estimated undeclared MMS rate limits (as of April 2023):

| Carrier | MMS Per Second | MMS Per Minute |
|---|---|---|
| AT&T / T-Mobile | 0.84 | 50 (per number) |
| Verizon | 25 | — |

### Message Segment Details

A standard SMS (GSM-7) contains up to 160 characters per segment. Multi-part messages use a User Data Header (UDH) of 7 bytes, reducing each segment to **153 characters**. Up to 10 segments are supported before messages are rejected. MPS limits are shared across all numbers attached to a Campaign.

## Fees and Charges

Telnyx does not add a markup on 10DLC fees; all are passed through at cost.

### Registration Fees

| Item | Cost |
|---|---|
| Brand Registration | $4.50 (one-time) |
| Campaign Review | $15.00 per review (manual review fee from carriers) |
| Monthly Campaign Cost | $1.50/mo (Low Volume Mixed), $2.00/mo (Sole Proprietor), $3.00/mo (Charity), $5.00/mo (Emergency), $10.00/mo (standard volume including Marketing, Mixed, 2FA, Customer Care, Political, and most other use cases) |

Campaign fees are billed for three months initially, then on a monthly recurring basis. Declaring a false Use Case to achieve lower fees or higher throughput can result in deactivated campaigns and hefty fines.

### Carrier Message Fees (Registered Traffic)

| Carrier | SMS | MMS |
|---|---|---|
| T-Mobile | $0.003 send & receive | $0.01 send & receive |
| AT&T | $0.003 send / Free receive | $0.0075 send / Free receive |
| Verizon | $0.0031 send / Free receive | $0.0052 send / Free receive |
| US Cellular | $0.005 send / Free receive | $0.01 send / Free receive |

### Carrier Message Fees (Unregistered Traffic)

Fees are significantly higher for unregistered traffic. Carriers may also refuse technical support for delivery issues.

| Carrier | SMS | MMS |
|---|---|---|
| T-Mobile | $0.012 send & receive | $0.021 send & receive |
| AT&T | $0.01 send & receive | $0.015 send & receive |

### T-Mobile Special Fees

| Item | Cost |
|---|---|
| Special Business Review (daily volume >200,000/Brand) | $5,000 one-time (currently waived) |
| Number Pool Request (≥50 numbers/Campaign) | $50 one-time |

## Non-Compliance Fines

T-Mobile imposes pass-through fines for major compliance violations:

| Violation | Fine |
|---|---|
| Text enablement (sending before verifying ownership/authorization) | $10,000 per violation |
| Grey Route (A2P over P2P routes) | $10 per message (currently on hold) |
| Long Code Program Evasion (snowshoeing, dynamic routing, non-approved number replacement) | $1,000 per violation |
| Content Violation (3rd+ SHAFT-C, spam, phishing, Severity 0) | $10,000 per violation |
| Fraud (phishing, smishing, social engineering) | $2,000 |
| Illegal content (especially cannabis; must be legal in all 50 states) | $1,000 |
| Other illegal content including SHAFT | $500 |

## Key Definitions

- **10DLC** — 10 Digit Long Code; the protocol for local long-code A2P messaging in the US.
- **A2P** — Application-to-Person messaging; covers all messages sent by or on behalf of a business.
- **Brand** — The trading name of the company sending messages, tied to an EIN.
- **Campaign** — An organization of 10DLC-registered numbers and their use cases, governed by TCR.
- **MO** — Messaging Origination; a message sent to an A2P number.
- **MT** — Messaging Termination; a message sent from an A2P number to an end user's handset.
- **P2P** — Person-to-person messaging not on behalf of a business. Most business messages are considered A2P regardless of how they are triggered.
- **TCR** — The Campaign Registry; the entity appointed by carriers to manage 10DLC registration records.

## Contact and Support

- **10DLC-specific questions:** [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com)
- **Non-compliance or portal issues:** [support@telnyx.com](mailto:support@telnyx.com)
- **Add notification email addresses:** Email [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) with your main Telnyx username email
- **24/7 chat support:** Available via the [Mission Control Portal](https://portal.telnyx.com/)
