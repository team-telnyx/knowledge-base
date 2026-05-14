---
title: Telnyx 10DLC Registration and Compliance Guide
summary: End-to-end guide to registering brands and campaigns for US A2P 10DLC with
  Telnyx, including brand types, message flow and consent requirements, privacy policy
  language, submission timelines, number assignment, testing options, and troubleshooting.
sources:
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
updated_at: 2026-05-14T11:21:28Z
---

# Telnyx 10DLC Registration and Compliance Guide

*Part 1 of 2 — see also: [Part 2](telnyx-10dlc-registration-and-compliance-guide--part-2.md)*

End-to-end guide to registering brands and campaigns for US A2P 10DLC with Telnyx, including brand types, message flow and consent requirements, privacy policy language, submission timelines, number assignment, testing options, and troubleshooting.

## Who needs 10DLC (and by when)
If you send outbound SMS from local US 10-digit long codes (10DLC) to US recipients, your traffic must be registered with The Campaign Registry (TCR). As of February 4, 2025, unregistered SMS traffic is blocked. Register your brand and campaign before sending to avoid filtering.

## Brand types and prerequisites
- Standard brands (businesses with EIN): Brand information must exactly match IRS CP-575 records; TCR validates against the IRS database.
- Publicly traded brands: Must complete TCR Auth Plus (one-time email/2FA authentication of a brand contact). After Aug 1, 2025, a ~$12.50 fee applies if not already completed.
- Sole proprietor brands (no EIN): Intended for single individuals with low-volume needs (typically ~1,000 messages/day). Requires OTP PIN verification via mobile.
- Mock brands (testing only): Free, used to test APIs/webhooks. Not valid for real traffic.
- Numbers: Have at least one local US number to assign after approval.

## Step 1: Create and verify your brand
1) Create the brand in the Telnyx Mission Control Portal (Messaging > 10DLC > Brands).
- Ensure legal entity details match official records; mismatches prevent “Verified” status.

2) Verification by brand type
- Standard brands: Achieve “Verified” by exact IRS match.
- Publicly traded (Auth Plus): Email 10dlcquestions@telnyx.com with your brand ID and a business-contact email using the brand’s domain. The contact receives a noreply@auth.campaignregistry.com 2FA email with a PIN and link, then submits: First/Last name, Job title, and the PIN within 7 days to authenticate the brand.
- Sole proprietor: Email 10dlcquestions@telnyx.com requesting an OTP PIN after creating the brand. Telnyx sends a PIN to your mobile; reply with that PIN within 24 hours to complete verification.
- Mock: When creating the brand, select/mock=true to waive fees (test only).

## Step 2: Choose a use case and prepare compliant content
Select the use case that best matches your traffic. Common categories include:
- 2FA, Account Notification, Customer Care, Delivery Notifications, Fraud Alert, Higher Education, Security Alert
- Marketing
- Polling and Voting, Public Service Announcement
- Mixed (2–5 sub-use cases) or Low Volume Mixed (≤5 sub-use cases for small/low-throughput brands)
- Machine-to-Machine (dedicated, no subscriber-facing messaging)

Before you submit a campaign, prepare:
- Message flow (how users opt in)
- Opt-in form or consent wording
- Keywords and confirmation messages (START/STOP/HELP)
- Sample messages including opt-out instructions
- Privacy policy language (or equivalent verbiage on the opt-in form)

## Message flow and consent (what to write in the campaign)
Carriers require a clear description of how subscribers opt in. Document one of these methods in your campaign details (fill in your brand specifics):

- Digital consent (web form/contact page)
  - Describe the URL/path and include a screenshot link. Disclose: “By providing your phone number, you agree to receive SMS [use case]. Message frequency may vary. Standard message & data rates may apply. Reply STOP to opt out; HELP for help. Consent is not a condition of purchase. Your mobile information will not be sold or shared with third parties for promotional or marketing purposes.” Link to your privacy policy or include compliant privacy verbiage on the form.

- Verbal consent (phone/in-person)
  - State how users learn your number/address. Provide the agent script with all required disclosures. After consent, send a confirmation SMS. For marketing/political content, explicitly confirm via YES reply before sending those categories.

- Physical consent (paper form)
  - Note where the form is completed, include required disclaimers, and link to a copy of the form. Send a confirmation SMS after data entry.

- Keyword opt-in or inbound message
  - Publish a number/keyword on a site, flyer, QR code, etc. The first auto-reply must include required disclosures and a link/screenshot showing where the number/keyword is advertised.

Important additions:
- If marketing content will be sent, explicitly say users are opting in to marketing SMS.
- For political/charity use cases where fundraising may occur, include: “Donations may be solicited.”

## Required keywords and confirmation messages
All campaigns must define keywords and autoresponses:
- Opt-in keyword: START (or similar)
  - Opt-in confirmation: “[Brand]: Thanks for subscribing to [use case]. Reply HELP for help. Message frequency may vary. Msg & data rates may apply. Consent is not a condition of purchase. Reply STOP to opt out.”
- Opt-out keyword: STOP (or similar)
  - Opt-out confirmation: “[Brand]: You are unsubscribed and will receive no further messages.”
- Help keyword: HELP (or similar)
  - Help confirmation: “[Brand]: Please reach out at [website/email/phone] for help.”
Notes: A website is acceptable in HELP if it clearly lists contact information.

## Opt-in form essentials (digital)
- Place required disclosures visibly near the phone field/checkbox.
- Provide a specific, optional SMS consent checkbox (unchecked by default). Do not bury consent in T&Cs or make it mandatory.
- Set expectations about message types and frequency.
- Add “You are opting into marketing texts” for Marketing use cases.
- Add “Donations may be solicited” for Political/Charity when applicable.

## Privacy policy language (what carriers expect)
Include compliant privacy language on the opt-in page and/or in a linked privacy policy for the brand being registered (reseller or generic policies, including Google’s, are not accepted). Carriers commonly approve verbiage such as:
- “Your mobile information will not be sold or shared with third parties for promotional or marketing purposes.”
And a stronger, preferred statement:
- “All the above categories exclude text messaging originator opt-in data and consent; this information will not be shared with any third parties. We will not share your opt-in to an SMS campaign with any third party for purposes unrelated to providing you with the services of that campaign. We may share your Personal Data, including your SMS opt-in or consent status, with third parties that help us deliver messages (e.g., platform providers, phone companies, vendors).”
Ensure the language covers sharing as well as selling.

## Step 3: Create your 10DLC campaign
- Only submit once your brand shows Verified.
- In the campaign form, set Opt-in, Opt-out, and HELP to True. TCR will reject submissions if any are False.
- Provide detailed Message Flow, sample messages (include brand name and “Reply STOP to opt out”), and any required links/screenshots.

Review process and outcomes:
- Telnyx review: Same day or next business day, depending on submission time.
- If “Sent for Carrier Review”: Carriers typically respond within 3 business days (volume can affect timing; some cases, e.g., Sole Proprietor, can take 3–7 business days).
- If “Flagged for Corrections”: You’ll receive feedback; reply on the same email thread to 10dlcquestions@telnyx.com with updates. No further action occurs until you confirm changes.
- Approval: You can assign up to 49 numbers to the campaign and begin messaging.
- Decline: You’ll receive reasons and error codes; update and resubmit on the same email thread.

Common submission pitfalls:
- Campaigns with TCR ID starting “4b3” or status “Failed TCR Review” were not created successfully—often caused by submitting before brand verification.
