---
title: Telnyx 10DLC Registration and Compliance Guide
summary: End-to-end guide to registering brands and campaigns for US A2P 10DLC with
  Telnyx, including brand types, message flow and consent requirements, privacy policy
  language, submission timelines, number assignment, testing options, and troubleshooting.
sources:
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
  content_hash: 07f91a97a3331277fd2fe0d2ef7e37178432594c87aa13969aef8b5e27450bbd
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
  content_hash: 52724a201fd5374074a0eb90e9410468b85a7658feedbe8a9d47840d78861363
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
  content_hash: 517aa55bed935632cdb945d6eef7257cf50aa3e98ea893be02332ddfbddd55c8
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
  content_hash: d42dcbd08bb330e0aa10504286cf75d33dcd7460d03daf8b7b267d00291933e2
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
  content_hash: 1642b9aa15da6996121686960f14303b8ae52ce210e2da3f8d83db58714cc412
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
  content_hash: 5cd5bf1f1948371f446ccefb780d5b4531e62671f2dd0c26d25bd27e63771881
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
  content_hash: 53303949333d229d69795898d3f2e3a769040e9e5f3aaf22103e4b319c3cc0f9
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
  content_hash: 54651f622c365df6722b1c021dfed1349e1958ce387be017a8f2734d21580362
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
  content_hash: 37a982b9ca22d0b1038b557daa06ea985e56d652c8f54943f3bcac05661038ac
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
  content_hash: 25c1106c094619bdd2dc507005df38013bd5d4b5e533642f3494ddd6ee53d1a2
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
  content_hash: 4fba36c10f632c6f7e972ccbedc25d5114ab5db663ac39d38c1c8972596a1451
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
  content_hash: 56c3dcab871bcdc0ab6232b281a94221e5d6b99ecaaeafb5f08d32fb2a702826
updated_at: 2026-05-14T11:21:28Z
---

# Telnyx 10DLC Registration and Compliance Guide

*Part 2 of 2 — see also: [Part 1](telnyx-10dlc-registration-and-compliance-guide--part-1.md)*

End-to-end guide to registering brands and campaigns for US A2P 10DLC with Telnyx, including brand types, message flow and consent requirements, privacy policy language, submission timelines, number assignment, testing options, and troubleshooting.

## Step 4: Assign numbers and go live
- Assign your US local numbers to the approved campaign in the portal (Numbers > My Numbers > 10DLC) or via API.
- Number-assignment propagation typically completes in about 2 hours but can take minutes to a few days.
- Check assignment status via API: https://developers.telnyx.com/api/messaging/10dlc/get-all-phone-number-campaigns
  - If status is ASSIGNED, the number is ready. If you see undelivered messages from before assignment completion, compare message timestamps to the last assignment update.

## Timelines and notifications
- Telnyx review: same/next business day. Carrier review: typically ≤3 business days; some cases may take up to a week.
- To add additional notification recipients for campaign status emails, write to 10dlcquestions@telnyx.com from your main Telnyx username email.

## Example: Chiropractor registration template
- Vertical: Healthcare
- Use case: Low Volume Mixed with Customer Care sub-use case
- Campaign description: “Campaign to send SMS customer care messages to [Practice Name] patients.”
- Message flow (verbal): Patients call [Front Desk Number] or visit [Office Address] (published at [Where Address Is Listed]). Staff explains consent, including all required disclosures. After consent, send confirmation SMS: “You have agreed to receive SMS customer care messages from [Practice]. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out; HELP for help.”
- Autoresponses:
  - START: same as confirmation above
  - STOP: “[Practice]: You are unsubscribed and will receive no further messages.”
  - HELP: “[Practice]: Please reach us at [Front Desk Number] for help.”
- Sample message: “Appointment Time: 2/6/2025 12:15 PM Appointment Type: Office Visit With: [Practice]”
- Attributes: Opt-in/Help/Opt-out = Yes; No to direct lending, age-gated, number pooling, embedded links/numbers, affiliate marketing (adjust as needed)

## Testing with mock brands and campaigns
- Use Mission Control or API to create a mock brand (mock=true) and then campaigns under it. Registration and monthly fees are waived for mocks.
- Purpose: Test API behavior, webhook notifications, and provisioning flows.
- Limitations: Mock campaigns cannot send real 10DLC traffic. Delete when done via normal deletion endpoints or in the portal.

## Fees snapshot (Sole Proprietor)
- Brand registration: ~$4 one-time
- Campaign vetting: ~$15 per submission/resubmission
- Monthly maintenance: ~$2/month
(Fees are pass-through from carriers and can change; check the latest schedule.)

## Troubleshooting and support
- Deliverability right after assignment: Confirm the number shows ASSIGNED and re-check message vs. assignment timestamps.
- Campaign submission errors: If Opt-in/Opt-out/HELP weren’t set True, update and resubmit. If TCR ID starts 4b3 or status is Failed TCR Review, re-create after ensuring brand is Verified.
- Declined campaigns: Use the provided error codes to correct issues, then reply in the same email thread for resubmission. See carrier error-code guidance: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
- Non-compliance or portal issues: support@telnyx.com
- 10DLC registration/campaign questions and notification recipients: 10dlcquestions@telnyx.com

## Helpful references
- Telnyx 10DLC process overview: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
- Create a brand: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
- Create a campaign: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
- Message flow guidance and templates: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- Opt-in form example: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- Keywords and confirmations: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- Privacy policy guidance: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
- Number assignment status API: https://developers.telnyx.com/api/messaging/10dlc/get-all-phone-number-campaigns
- Sole proprietor guide: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
- Mock brands/campaigns: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
