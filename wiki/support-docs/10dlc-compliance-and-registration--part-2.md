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

*Part 2 of 5 — see also: [Part 1](10dlc-compliance-and-registration--part-1.md), [Part 3](10dlc-compliance-and-registration--part-3.md), [Part 4](10dlc-compliance-and-registration--part-4.md), [Part 5](10dlc-compliance-and-registration--part-5.md)*

10DLC is the mandatory US carrier framework for A2P SMS and MMS traffic sent from +1 long code numbers. This page consolidates Telnyx's 10DLC guidance — including who it applies to, how to register a Brand and Campaign, throughput and vetting rules, message flow templates, fees and non-compliance fines, and the February 3, 2025 enforcement deadline after which unregistered traffic is blocked.

## Throughput

Throughput is the maximum number of messages you can send in a given period — segments per second (MPS), per minute (MPM), or per day. Each registered Campaign is assigned a maximum MPS based on Brand Tier (derived from Vetting Score) and Campaign type. The MPS limit is shared across all numbers attached to your Campaign and all wireless Carriers.

A message segment consists of up to 160 standard characters. An SMS with more characters and/or nonstandard characters (such as emojis) can count as multiple segments. Telnyx supports up to 10 segments before messages are rejected for being too long.

### Campaign Use Case Categories

- **Declared:** Specific Use Cases (e.g., two-factor authentication).
- **Mixed:** A combination of multiple Use Cases (up to five Sub-Use Cases).
- **Marketing:** Marketing-related content.
- **Special:** Charity, emergency, political, and other.

Declared Use Case Campaigns may receive a higher MPS than a Mixed or Marketing Campaign with the same Brand Score. **It is important to correctly classify your Use Case** — incorrectly classified use cases can result in Deactivated Campaigns and hefty fines.

### AT&T Throughput (Message Class System)

AT&T sets throughput based on Campaign, using an AT&T "Message Class" determined by Use Case and (in many cases) Vetting Score. Russell 3000 brands may default to a high score immediately.

| Class | Use Case | Vetting Score Requirement | TPM (SMS) | TPM (MMS) | Variable Rate depending on score |
|-------|----------|---------------------------|-----------|-----------|----------------------------------|
| A, B | Dedicated, Mixed / Marketing | 75–100 | 4500 | 2400 | Y |
| C, D | Dedicated, Mixed / Marketing | 50–74 | 2400 | 1200 | Y |
| E, F | Dedicated, Mixed / Marketing | 1–49 | 240 | 150 | Y |
| T | Basic / Unregistered | 0 / NA | 75 | 50 | N/A |

Special Use Case examples:

| Message Class | Use Case | Vetting Score Reqmt | AT&T TPM (SMS) | AT&T TPM (MMS) | Variable Rate Based on Score |
|---------------|----------|---------------------|---------------|----------------|------------------------------|
| K | Political | — | 4500 | 2400 | N* |
| T | UCaaS Low Vol | — | 75 | 50 | N |
| B / D / F | UCaaS High Vol | — | 240 (B) / 2400 (D) / 4500 (F) | 150 (B) / 1200 (D) / 2400 (F) | Y |

*Vetting is mandatory for Brands conducting political Campaigns.

### T-Mobile Throughput (Brand-Based)

T-Mobile sets limits at the Brand level, not Campaign. For Standard Campaigns:

| Brand Tier | Vetting Score Requirements | T-Mobile Daily Cap |
|------------|----------------------------|--------------------|
| Top | 75–100 | 200,000 |
| High Mid | 50–74 | 40,000 |
| Low Mid | 25–49 | 10,000 |
| Low | 1–24 | 2,000 |

Brands which are not Vetted and are not on the Russell 3000 may default to a Low Brand Tier for T-Mobile throughput.

### Verizon Throughput

Verizon has not declared any throughput guidance as of September 2023. However, since Verizon has joined the TCR, Telnyx recommends following 10DLC best practices.

### MMS Throughput

As of April 2023, undeclared industry limits for MMS were estimated at:

| | AT&T / T-Mobile | Verizon |
|---|---|---|
| MMS Per Second Max | 0.84 | 25 |
| MMS Per Minute Max | 50 (per number) | — |

## Special Use Cases

The following Campaign Use Cases are treated differently and often require pre-approval, post-approval, and/or vetting:

1. Agents and Franchises
2. Carrier Exemptions
3. Charity
4. Conversational Messaging
5. Emergency
6. Political
7. Social
8. Sweepstake

In some cases, they require a different vetting agent (such as Aegis or CampaignVerify for political campaigns). Federal political campaigns can be verified via [Campaign Verify](https://www.campaignverify.org/) or [Aegis](https://aegismobile.com/). If you did not register via Telnyx, you can import the verification token they provided.
