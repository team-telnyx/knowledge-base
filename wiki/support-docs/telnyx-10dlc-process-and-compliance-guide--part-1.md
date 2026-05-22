---
title: Telnyx 10DLC Process and Compliance Guide
summary: All US A2P messaging sent from local 10-digit long code (10DLC) numbers must
  be registered. This guide consolidates Telnyx’s end‑to‑end 10DLC process, deadlines,
  brand and campaign setup, opt-in/opt-out requirements, privacy policy language,
  shared and sole proprietor workflows, number assignment, review timelines, and troubleshooting
  tips.
sources:
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
  content_hash: 56c3dcab871bcdc0ab6232b281a94221e5d6b99ecaaeafb5f08d32fb2a702826
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
  content_hash: 07f91a97a3331277fd2fe0d2ef7e37178432594c87aa13969aef8b5e27450bbd
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
  content_hash: 1642b9aa15da6996121686960f14303b8ae52ce210e2da3f8d83db58714cc412
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
  content_hash: ebc18383ec12a57fd90c1686f156d82b3328c7505c53046fdb7999ae82dce2a2
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
  content_hash: 517aa55bed935632cdb945d6eef7257cf50aa3e98ea893be02332ddfbddd55c8
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
  content_hash: d42dcbd08bb330e0aa10504286cf75d33dcd7460d03daf8b7b267d00291933e2
- url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
  content_hash: f9c5a17c24934515d5664d936d5250072b6dae72debcdf562669a656085595c1
- url: https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging
  content_hash: 41b3d9d42f3f05bda073e7efad630e56fbd411ae28934d528f44894c226aa9db
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
  content_hash: 36328b4581d3a63fcbf63cdd83163f2e1a7f5b3b8acc378c785c301d4f07eb07
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
  content_hash: 1f109a5292115327d38a9154cb49bf4fb36572998a878799e4bb014c82528cdb
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
  content_hash: 2ec6095b46f56710ce82d658bb58389efc5083ba146c4bd25d2751da4a6e313f
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
  content_hash: e3c89476e3ab511fbbca21c3432b0dc2bd5e8992985711bb44d3a98cd6bdf2f3
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
  content_hash: 3b46b15924c5883df3214410e67c0f02bb14ecb0ee3cd1769996715b6c891e90
updated_at: 2026-05-20T14:06:51Z
---

# Telnyx 10DLC Process and Compliance Guide

*Part 1 of 2 — see also: [Part 2](telnyx-10dlc-process-and-compliance-guide--part-2.md)*

All US A2P messaging sent from local 10-digit long code (10DLC) numbers must be registered. This guide consolidates Telnyx’s end‑to‑end 10DLC process, deadlines, brand and campaign setup, opt-in/opt-out requirements, privacy policy language, shared and sole proprietor workflows, number assignment, review timelines, and troubleshooting tips.

## Enforcement timeline and scope
• As of February 4, 2025, US mobile operators and The Campaign Registry (TCR) block unregistered 10DLC SMS traffic. This is an industry-wide requirement, not a Telnyx policy. See [Register for 10DLC Messaging](register-for-10dlc-messaging.md).

## End-to-end 10DLC workflow at Telnyx
1) Create and verify your Brand
2) Create a Campaign tied to that Brand
3) Assign your US local numbers to the approved Campaign

Notes
• All three steps are required before sending. 
• Telnyx offers both Portal and API flows for registration and number assignment.

## Create and verify your 10DLC brand
Where to create
• Mission Control Portal: Messaging → 10DLC → Brands
• API option available (see Telnyx API docs)

Required information (must be complete and accurate)
• Legal company name, DBA, entity type, vertical, country of registration, website
• EIN and issuing country (for US entities). US brand data must match IRS Form CP‑575 exactly to achieve Verified status; mismatches remain unverified until corrected. See [10DLC Unverified Brand](10dlc-unverified-brand.md).
• Business address matching IRS records (US), brand contact email and phone
• Publicly traded brands: stock symbol/exchange and see Auth Plus notes below

Canadian brands
• Use Provincial or Federal corporation/registry ID (not CRA BN or tax account numbers if avoidable). Keep official registration documents handy for possible manual vetting.

Billing
• One-time $4 brand registration fee (TCR pass‑through). See [10DLC Fees and Charges](10dlc-fees-and-charges.md).

Optional: third‑party vetting
• Can improve commercial terms/throughput. Request in brand settings in the Portal.

## Create a compliant 10DLC campaign
Where to create
• Mission Control Portal: Messaging → Compliance → 10DLC Campaigns
• API option available

Pre‑requisites and best practices
• Brand must be Verified before campaign creation. 
• Ensure Opt-in, Opt-out, and Help attributes are set to True; missing these causes TCR rejection.
• Throughput depends on Trust Score and Use Case. See [10DLC: Trust Scores & Use Cases](10dlc-trust-scores-use-cases.md) and [10DLC Use Cases](10dlc-use-cases.md).

Key fields and constraints
• Use case: select the most accurate type (e.g., 2FA, Marketing, Mixed, Low Volume Mixed, etc.)
• Campaign description: 40–4096 chars
• Message Flow (how users opt in): 40–2048 chars; provide concrete steps and URLs. See [Guide to 10DLC Message Flow Field](guide-to-10dlc-message-flow-field.md).
• Sample messages: include one per selected use case (Marketing requires two). Content you send must align with samples.
• Keywords and confirmation messages: provide Opt‑in, Opt‑out, and Help keywords and autoresponses (see section below).
• Content attributes: declare use of links, phone numbers, affiliate marketing, age‑gated content, number pooling, lending, etc.

Common creation errors
• TCR ID starting with “4b3” or status “Failed TCR Review” indicates unsuccessful creation—often due to creating the campaign before the brand is verified.
• “Invalid date” or “TCR Creation Failed” in the Portal usually means a formatting/length/sample‑message issue. Recreate after correcting; contact 10dlcquestions@telnyx.com for the failure reason.

## Opt‑in, keywords, and confirmation messaging
Keywords (examples)
• Opt‑in: START (or similar)
• Opt‑out: STOP (or similar)
• Help: HELP (or similar)

Required confirmation messages (fill in your Brand/use case details)
• Opt‑in confirmation: “[Brand]: Thanks for subscribing to [use case(s)]! Reply HELP for help. Message frequency may vary. Msg&data rates may apply. Consent is not a condition of purchase. Reply STOP to opt out.”
• Opt‑out confirmation: “[Brand]: You are unsubscribed and will receive no further messages.”
• Help confirmation: “[Brand]: Please reach out to us at [website/email/phone] for help.” (Websites are acceptable if the linked page shows clear contact info.)

Digital opt‑in form essentials
• Include clear disclosures: “By providing your phone number, you agree to receive SMS [use case(s)] from [Brand]. Message frequency may vary. Standard message & data rates may apply. Reply STOP to opt out. Reply HELP for help. We will not share mobile information with third parties for promotional or marketing purposes.”
• SMS consent must be specific, explicit, optional, and not bundled with other consents; checkbox should be unchecked by default.
• If Political/Charity use case will solicit donations, add “Donations may be solicited.” For Marketing, explicitly state “You are opting into marketing texts.”
• Non‑digital flows must be documented in Message Flow. See [Guide to 10DLC Message Flow Field](guide-to-10dlc-message-flow-field.md).

See also [10DLC Campaign Compliance Requirements](10dlc-campaign-compliance-requirements.md) and [How to create a 10DLC campaign](how-to-create-a-10dlc-campaign.md).

## Privacy policy requirements for 10DLC
• The policy must be the Brand’s own (resellers cannot substitute their policy; Google’s generic policy is not accepted).
• Either link your privacy policy on the opt‑in form or place the required language on the form itself.
• Minimum carrier‑approved language: “Your mobile information will not be sold or shared with third parties for promotional or marketing purposes.”
• Stronger, preferred language should also cover any non‑sale transfers/sharing: e.g., “All the above categories exclude text messaging originator opt‑in data and consent; this information will not be shared with any third parties… We may share your Personal Data, including SMS opt‑in/consent status, only with third parties who help deliver messaging services (platform providers, phone companies, vendors). We will not share your SMS opt‑in with third parties for purposes unrelated to delivering the campaign’s services.”

## Submission, review, and outcomes
Telnyx review
• Same day or next business day, depending on submission time. You’ll receive one of two emails:
  – Sent for Carrier Review: submitted downstream; carriers typically respond within 3 business days or less.
  – Flagged for Corrections: incorrect or impermissible content; update as instructed and reply on the same email thread. No further action occurs until you confirm changes to 10dlcquestions@telnyx.com.

Carrier outcome
• Approved: assign up to 49 numbers and begin messaging. See [How to assign a number to a campaign](how-to-assign-a-number-to-a-campaign.md).
• Declined: you’ll receive reasons and error codes. See [10DLC Carrier Error Codes and Explanations](10dlc-carrier-error-codes-and-explanations.md). Reply on the same thread with questions/updates for resubmission.

Notifications
• To add recipients for status emails, write to 10dlcquestions@telnyx.com from your account’s main username email.

## Assign numbers to approved campaigns
Key rules
• A number can be on only one campaign at a time.
• A campaign can have up to 49 numbers (T‑Mobile limitation). To exceed 49, submit a T‑Mobile Number Pool Request; additional fees apply. See [10DLC Fees and Charges](10dlc-fees-and-charges.md).

Portal flow (high level)
• Go to Campaigns → select your campaign → Assign Numbers → choose the Messaging Profile or specific numbers → assign and save. See [How to assign a number to a campaign](how-to-assign-a-number-to-a-campaign.md).
