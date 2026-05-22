---
title: 'Telnyx 10DLC: Registration, Compliance, Throughput, Fees, and Special Cases'
summary: 'A consolidated guide to A2P 10DLC on Telnyx: who must register, how Brands/Campaigns
  work, carrier vetting and throughput, fees, compliance requirements and forbidden
  use cases, plus guidance for ISVs, shared and mock campaigns, and a healthcare (chiropractor)
  example.'
sources:
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
- url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
- url: https://support.telnyx.com/en/articles/5593977-isvs-10dlc
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
- url: https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges
- url: https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance
- url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
- url: https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
updated_at: 2026-05-20T14:17:37Z
---

# Telnyx 10DLC: Registration, Compliance, Throughput, Fees, and Special Cases

*Part 1 of 2 — see also: [Part 2](telnyx-10dlc-registration-compliance-throughput-fees-and-special-cases--part-2.md)*

A consolidated guide to A2P 10DLC on Telnyx: who must register, how Brands/Campaigns work, carrier vetting and throughput, fees, compliance requirements and forbidden use cases, plus guidance for ISVs, shared and mock campaigns, and a healthcare (chiropractor) example.

## What 10DLC Is and Who It Applies To
10DLC is the carrier-mandated framework for A2P messaging over US (+1) local long codes. As of February 3, 2025, unregistered 10DLC traffic is blocked. Any business sending SMS/MMS from US long codes must register a Brand and Campaign(s). Toll-Free and Short Code have their own programs and are not governed by 10DLC, though they still require verification/registration.

Key points:
- Virtually all business messaging is A2P and subject to 10DLC.
- Non‑US entities can register but must follow the same rules.
- P2P exemptions are rare and strictly limited to true person-to-person use.

## Registration Workflow at a Glance
1) Create a 10DLC Brand (one Brand per EIN). Optionally submit for third‑party vetting to improve throughput.
2) Create a Campaign (choose an appropriate Use Case; Mixed allows up to five sub‑use cases).
3) Assign phone numbers to the Campaign.
4) Await manual reviews by The Campaign Registry (TCR) and carriers.
5) Send only content consistent with the declared Use Case and opt‑in.

Tips:
- Pre-create and obtain approval for campaigns before porting numbers to Telnyx to avoid assignment conflicts with the losing carrier.
- You cannot share a number across multiple Brands or Campaigns.

## Brands, Campaigns, and Numbers: Relationship & Limits
- One EIN → one Brand.
- A Brand can have multiple Campaigns (up to five per Brand).
- A Campaign can have multiple Numbers; a Number can belong to only one Campaign (and its parent Brand).
- T-Mobile caps per-Campaign numbers at 49; adding numbers is also subject to daily industry limits—try again the next business day if you hit a cap.

## Vetting, Trust/Brand Tier, and Throughput
Third‑party vetting partners approved by TCR include Aegis Mobile, WMC Global, and CampaignVerify (for political). Vetting yields a score that determines Brand Tier and materially impacts throughput—especially for Marketing or Mixed use cases.

Throughput basics:
- SMS throughput is measured in message segments per second (MPS). A standard GSM‑7 segment is up to 160 characters; multi‑part messages reserve UDH bytes, reducing each segment to 153 characters. Up to 10 segments are supported per message.
- MPS is assigned per Campaign based on Use Case and Brand Tier and is shared across all numbers on that Campaign.
- T-Mobile sets a Brand‑level daily allowance; AT&T uses Campaign “Message Class.” Verizon provides no public method but still requires 10DLC compliance.

Illustrative limits:
- T-Mobile Brand-level daily caps (Standard Campaigns): Top (75–100 vetting score): 200k; High‑Mid (50–74): 40k; Low‑Mid (25–49): 10k; Low (1–24): 2k. Unvetted Brands typically default to Low.
- AT&T Message Class (examples, SMS/MMS TPM):
  - Classes A/B (score 75–100): ~4500/2400 TPM
  - C/D (50–74): ~2400/1200 TPM
  - E/F (1–49): ~240/150 TPM
  - T (basic/unregistered): ~75/50 TPM
- MMS: undeclared industry limits vary; historically AT&T/T‑Mobile ~0.84 mps (50 per minute per number), Verizon higher (e.g., 25 mps). MMS has higher carrier surcharges than SMS.

## Fees and Carrier Surcharges
Registration fees (pass‑through at cost):
- Brand registration application: $4.50
- Campaign review (manual vetting): $15 per review/submission
- Monthly Campaign fees: $1.50/mo for Low Volume Mixed; $10/mo for most Standard Campaigns; $3/mo Charity; $5/mo Emergency. Billed for three months up front, then monthly.

Carrier per‑message surcharges (registered traffic):
- T‑Mobile: SMS $0.003 send/receive; MMS $0.01 send/receive
- AT&T: SMS $0.003 send, free to receive; MMS $0.0075 send, free to receive
- Verizon: SMS $0.0031 send, free to receive; MMS $0.0052 send, free to receive
- US Cellular: SMS $0.005 send, free to receive; MMS $0.01 send, free to receive

Unregistered traffic (significantly higher; support may be limited):
- T‑Mobile: SMS $0.011 send/receive (rising to $0.012 by Dec 1, 2024); MMS $0.020 (to $0.021)
- AT&T: SMS $0.01 send/receive; MMS $0.015 send/receive

T‑Mobile special/high‑volume fees (examples):
- Business Review for >200k/day per Brand: $5,000 one‑time (currently waived)
- Number Pool request (≥50 numbers on a Brand): $50 one‑time

T‑Mobile non‑compliance fines (pass‑through examples):
- Text enablement prior to ownership verification: $10,000/violation
- Program evasion (e.g., snowshoeing): $1,000/violation
- Content violations (e.g., SHAFT‑C, spam, phishing): $10,000/violation
- Fraud: $2,000; Illegal content esp. cannabis: $1,000; Other illegal/SHAFT: $500

## Compliance Requirements for Campaign Approval
Your registration and traffic must align with CTIA and carrier codes of conduct. Key requirements:

Call‑to‑Action (CTA) and Opt‑In
- Clearly display: program/brand name and product description; “Message frequency may vary”; “Standard message and data rates may apply”; “Reply STOP to opt out”; “Reply HELP for help”; links to Terms & Conditions and Privacy Policy (not pop‑ups); opt‑in language specific to text messages only (email/phone consent must be separate).
- If opt‑in occurs via a website: include a phone field that is not required; show explicit consent text near a checkbox; include links to Privacy Policy and T&C; place opt‑out instruction (“Text STOP to opt out”) in proximity to the CTA.
- If opt‑in is verbal, by form, keyword, or QR: include the script, exact keyword, number, and/or the form/screenshot URL in your Message Flow. First message from the business requires prior consumer consent unless responding to a consumer‑initiated inquiry (implied consent case).

Required keywords and confirmations
- Provide examples and auto‑responses for START/OPT‑IN (confirmation includes brand/program name, HELP, frequency, and rates), STOP (confirm opt‑out and no further messages), and HELP (brand/program name and customer care contact).

Sample messages and consistency
- Up to five varied samples matching the declared Use Case(s). For Mixed, include one per sub‑use case.
- Samples, brand, website, and campaign description must be consistent; include opt‑out language in at least one sample. Include embedded links/phone numbers in samples if those attributes are enabled.

Privacy Policy and Terms
- Must be accessible via URL in the registration (CTA/T&C fields). Pop‑ups are not accepted for T&C.
- Privacy Policy must forbid sharing/selling SMS opt‑in data and consent for promotional/marketing purposes. Recommended language: “We will not share your opt‑in to an SMS campaign with any third party for purposes unrelated to providing you with the services of that campaign… All the above categories exclude text messaging originator opt‑in data and consent; this information will not be shared with any third parties.”

Political and age‑restricted programs
- Political campaigns require CampaignVerify or Aegis verification; disclose if donations will be solicited and how they are secured/accredited.
- For age‑restricted content, implement robust age verification (e.g., government ID, third‑party identity checks, credit card verification, DOB capture). Simple “reply YES” is insufficient.

Common rejection reasons
- Prohibited content; inconsistent brand/website/samples; generic/free email domain for large enterprises; non‑working website; missing/incorrect CTA/T&C/Privacy links; missing opt‑out in samples; keyword/auto‑response issues; indicating “marketing” in CTA but not in Use Case (or vice versa).
