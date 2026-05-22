---
title: 'Telnyx 10DLC: Registration, Compliance, Throughput, Fees, and Special Cases'
summary: 'A consolidated guide to A2P 10DLC on Telnyx: who must register, how Brands/Campaigns
  work, carrier vetting and throughput, fees, compliance requirements and forbidden
  use cases, plus guidance for ISVs, shared and mock campaigns, and a healthcare (chiropractor)
  example.'
sources:
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
  content_hash: 180098a86a20eebf82d20f8a3fd3319a45aa6a4346309b5fa6ddb5f6023f5da3
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
  content_hash: 7a231be6387689243f529c075579a6218dabc596f5a1e3777d33ba058dcc8ed9
- url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
  content_hash: 87cd93a701417906b28510020559da52841b58af8cb556b988eca9d0c531f76a
- url: https://support.telnyx.com/en/articles/5593977-isvs-10dlc
  content_hash: eec4125b334eeacb74096e2fb18aa8b0fc457f2d94aaad0b833b02447dc0cbe0
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
  content_hash: 89208147df966b5d330f497179333a88e359027a49227e0e27fbfdcde9d5242a
- url: https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges
  content_hash: c96c064e8f23c5df43d3fa819a9ba45a9b6c3916df915c335a97e8d9e08bd934
- url: https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance
  content_hash: 0cee26744f7dd320379cf174b498d74beee0a5406f5e2b2a7af73f389cf722ca
- url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
  content_hash: d2af96cc56cdc0abfc084dd6b5514a0f91e5956f744926ba6d330cddcccd2be8
- url: https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory
  content_hash: 4f2b7b45cb3b0e1df3924357f45b2de75381a55b9ab431ee9af9a2db9ba083a1
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
  content_hash: 8b5320478eb2fb9d1c16bf70d3683f984b9d8661e5452d4f7e1fae3432d8ad6c
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
  content_hash: cd42f265d1f65bb28837b5018c5f0a656ddeba9eccb58c95bd902817c2743b75
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
  content_hash: 06c9f07c05422c16db8028cf30396fd263fd1264dab3705a84653a354e2a9688
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
  content_hash: 5322f8be78843ac345d3b4ff3cf6b4a18c6d2d92fc4641ab499e878a6a199c99
updated_at: 2026-05-20T14:17:37Z
---

# Telnyx 10DLC: Registration, Compliance, Throughput, Fees, and Special Cases

*Part 2 of 2 — see also: [Part 1](telnyx-10dlc-registration-compliance-throughput-fees-and-special-cases--part-1.md)*

A consolidated guide to A2P 10DLC on Telnyx: who must register, how Brands/Campaigns work, carrier vetting and throughput, fees, compliance requirements and forbidden use cases, plus guidance for ISVs, shared and mock campaigns, and a healthcare (chiropractor) example.

## Forbidden and Restricted Messaging Use Cases (US and Canada)
Prohibited categories include illegal products/substances; gambling/betting; SHAFT content (sex, hate, alcohol, firearms, tobacco—with alcohol only potentially permitted in the US with strict age controls; firearms/tobacco/vape not permitted on standard channels); deceptive/fraudulent content (phishing, misleading financial offers, opaque lead gen). Carriers evaluate both message content and the overall business model/use case. Additional notes:
- Use branded, recognizable domains; avoid public URL shorteners.
- Obtain and honor clear, verifiable consent; align all content with the registered Use Case.
- Carriers may enforce based on complaints, opt‑out rates, or traffic anomalies, even if not explicitly listed above.

## ISVs: Multi‑Tenant Architecture and Compliance
If you resell to other businesses (ISV):
- Create a separate Brand and Campaign(s) for each end‑customer.
- Do not share numbers across Brands. Each number must map to exactly one Campaign/Brand.
- T‑Mobile permits up to 49 numbers per Campaign; ≥50 requires a Number Pool request. Franchises or special models may be considered, but approval is uncommon for generic ISV pooling.
- Migration approach: create a dedicated Messaging Profile and number, register Brand/Campaign for one end‑customer, assign the number to the Campaign, then route that customer’s traffic via the new resources. Repeat per customer.
- Alternatives: seek explicit T‑Mobile number pooling approval (unlikely for non‑franchise ISVs), exclude T‑Mobile traffic, or use Toll‑Free (separate verification program and similar single‑tenant requirements apply).

## Shared Campaigns (Registered Directly at TCR)
You can register Brands/Campaigns directly with TCR and then share them to Telnyx as the connectivity partner (CNP). Notes:
- Provide your CSP ID to Telnyx Support/Account Manager so it can be associated with your Telnyx account (typically up to two business days). Telnyx CSP ID: SS4XJ6D.
- In the TCR CSP Portal, select the campaign and share it to Telnyx; Telnyx will review and, upon approval, appear as the connectivity partner.
- Assign Telnyx numbers to shared campaigns via the Bulk Phone Number Campaigns API. All numbers must belong to the same Messaging Profile. Use the Messaging Profile ID and the campaign’s TCR ID.
- You cannot edit shared campaign details via the Telnyx Portal; manage Brand/Campaign details in the TCR CSP Portal. Pending sharing requests cannot be rescinded or redirected by the downstream CNP.

## Mock Brands and Campaigns (Testing)
Use mock registrations to test APIs, webhooks, and provisioning flows without cost:
- In the Mission Control Portal, select “Create brand” and check “Create as a mock brand to test 10DLC” (the $4.00 registration fee is waived). In the API, set mock=true on brand creation.
- Create campaigns under the mock Brand; associated fees are waived; no vetting/validation occurs.
- Mock campaigns cannot be used for real 10DLC traffic; they are strictly for testing logic and webhook flows.
- Delete via standard Brand/Campaign deletion endpoints or in the Portal when testing is complete.

## Healthcare Example: Chiropractor 10DLC Registration Template
- Vertical: Healthcare; Use Case: Low Volume Mixed with Customer Care sub‑use case.
- Campaign Description: “Campaign to send SMS customer care messages to [Name of Practice] patients.”
- Message Flow (verbal consent in‑office or by phone): staff asks whether the patient would like SMS customer care messages. If yes, read disclosure: “By providing your phone number, you agree to receive SMS customer care messages from [Name of Practice]. Message frequency may vary. Standard message and data rates may apply. Reply STOP to opt out. Reply HELP for help. We will not share mobile information with third parties for promotional or marketing purposes.” Record consent, then send confirmation SMS.
- Auto‑responses:
  - START/Opt‑In: “You have agreed to receive SMS customer care messages from [Practice]. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help.”
  - STOP/Opt‑Out: “[Practice]: You are unsubscribed and will receive no further messages.”
  - HELP: “[Practice]: Please reach out to us at [Front Desk Number] for help.”
- Sample message: “Appointment Time: 2/6/2025 12:15 PM. Appointment Type: Office Visit. With: [Name of Practice].”
- Attributes: Subscriber opt‑in/help/opt‑out = Yes; No direct lending; No embedded links or numbers unless samples include them; No age‑gated content; No affiliate marketing; Number pooling = No.

## Practical Checklist Before You Submit a Campaign
- Campaign description clearly states who is sending and why.
- Message Flow details exactly how opt‑in occurs (URL to the specific page, and optionally a screenshot link; include Privacy Policy link).
- Website opt‑in: non‑required phone field; explicit SMS‑only consent text; checkbox; links to Privacy Policy and T&C; “Text STOP to opt out” inline.
- Keywords and auto‑responses provided for START/HELP/STOP.
- 3–5 varied sample messages aligned to Use Case(s), including at least one with opt‑out language; include embedded links/numbers in samples if those attributes are enabled.
- Privacy Policy/T&C URLs included in registration (no pop‑ups for T&C) and prohibit sharing/selling SMS opt‑in data for marketing.
- Brand, domain, samples, and declared Use Case(s) are consistent (e.g., if CTA mentions “marketing,” the Campaign Use Case must include Marketing, and the description should reflect it).
- Content complies with prohibited/restricted categories; avoid public URL shorteners; identify your brand in each message.

## Notes on MMS, Pricing, and Support
- 10DLC Campaigns include both SMS and MMS. MMS throughput patterns differ by carrier and often have tighter limits; MMS surcharges are higher.
- Telnyx passes through 10DLC fees at cost; carriers may refuse technical support for unregistered traffic.
- For very high scale or special needs, consider Short Code or Toll‑Free as alternatives.

## Where to Get Help
- Register via the Mission Control Portal or the Telnyx 10DLC APIs. For compliance or edge cases (e.g., political, franchises, high‑volume reviews), engage Telnyx Support or your Account Manager.
- For political verification: CampaignVerify or Aegis. For shared campaigns: coordinate CSP ID mapping and campaign sharing via the TCR CSP Portal.
