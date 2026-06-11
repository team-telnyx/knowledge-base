---
title: 10DLC Campaign Registration and Compliance
summary: A comprehensive guide to registering, configuring, and maintaining compliant
  10DLC campaigns on Telnyx, covering use cases, trust scores, opt-in methods, message
  flow, CTA requirements, keyword configuration, number assignment, shared campaigns,
  and approval best practices.
sources:
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
- url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
updated_at: 2026-06-11T11:11:29Z
---

# 10DLC Campaign Registration and Compliance

*Part 1 of 4 — see also: [Part 2](10dlc-campaign-registration-and-compliance--part-2.md), [Part 3](10dlc-campaign-registration-and-compliance--part-3.md), [Part 4](10dlc-campaign-registration-and-compliance--part-4.md)*

A comprehensive guide to registering, configuring, and maintaining compliant 10DLC campaigns on Telnyx, covering use cases, trust scores, opt-in methods, message flow, CTA requirements, keyword configuration, number assignment, shared campaigns, and approval best practices.

## Overview

In the US, A2P 10DLC (Application-to-Person 10-Digit Long Code) messaging requires businesses to register brands and campaigns to remain compliant with carrier rules. A campaign contains information about the messages you intend to send, including the opt-in process, sample messages, keywords, and content attributes. Messages sent that do not align with your registered use case may be subject to fines, throughput limitations, and blocks.

## Use Cases

Standard 10DLC use cases include:

- **2FA** — Authentication, verification, or one-time passcodes.
- **Account Notification** — Standard notifications for account holders (e.g., password reset, low-balance, suspicious login, transaction alerts).
- **Customer Care** — All customer care interaction, including account management and support.
- **Delivery Notifications** — Status notifications about delivery of a product or service.
- **Fraud Alert Messaging** — Notifications regarding potential fraudulent activity.
- **Higher Education** — Messaging on behalf of colleges, universities, or school districts. Not for the "free to the consumer" messaging model.
- **Low Volume Mixed** — For brands with multiple use cases needing very low throughput (e.g., test/demo accounts, small businesses). Maximum of 5 sub-use cases.
- **Machine-to-Machine (M2M)** — Wireless communication between physical assets with no human interaction. Subscriber-facing campaigns are prohibited. This is a dedicated use case.
- **Marketing** — Any communication including marketing and/or promotional content.
- **Mixed** — For brands running multiple use cases on the same campaign. Minimum 2, maximum 5 sub-use cases. Fees tend to be higher than specific use cases.
- **Polling and Voting** — Surveys and polling/voting campaigns.
- **Public Service Announcement** — Informational messaging to raise awareness about important issues.
- **Security Alert** — Notifications that system security has been compromised.

Additional use cases available in the portal include Agents and Franchises, Carrier Exemptions, Charity, Education, Emergency Alerts, Political, Social, Sole Proprietor, and Sweepstakes.

Political campaigns must also be verified at [campaignverify.com](https://campaignverify.com), which supplies a token upon successful verification.

## Trust Scores and Throughput

A2P 10DLC message sending throughput is measured in message segments per second (MPS). Each segment consists of up to 160 GSM-7 encoded characters; longer messages or different encodings use multiple segments. Throughput is determined by your **Trust Score** and your **Campaign Use Case**.

Trust Scores are assigned when a brand is registered via a reputation algorithm administered by The Campaign Registry (TCR). The score does **not** change over time, so starting with a good Trust Score is important. The algorithm is believed to be primarily determined by brand footprint (larger brands score higher) and the quality and consistency of the registration request (fewer discrepancies = better score).

On top of per-second throughput limits, T-Mobile imposes separate daily message limits toward their subscribers, which cannot be exceeded without a special business review. See [10DLC Fees and Charges](10dlc-fees-and-charges.md) for details.

To confirm whether a campaign use case is acceptable for your brand, use the Qualify By Use Case endpoint in the [Telnyx API](https://developers.telnyx.com/api/messaging/10dlc/get-campaigns).

## Creating a 10DLC Campaign

Every campaign must be associated with a brand. If you haven't registered a brand, complete that first by following [How to Create a 10DLC Brand](how-to-create-a-10dlc-brand.md). Ensure your brand has a good Trust Score before proceeding.

### Via the Mission Control Portal

Navigate to **Messaging > Compliance > 10DLC Campaigns** in the [Mission Control Portal](https://portal.telnyx.com/#/messaging-10dlc/campaigns) to create a new campaign.

### Via the Telnyx API

Use the Campaign API as documented in the [API reference](https://developers.telnyx.com/api/messaging/10dlc/get-campaigns).

### After Registration

Once submitted, campaigns are reviewed and either approved or declined. Automatic status update emails are sent to the username email on the account. To add additional email addresses for 10DLC notifications, contact your CSM or email [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com).

A $15 per-submission (or resubmission) carrier review fee applies. If a campaign is denied by external vetting, additional charges may occur with resubmission.

If you receive an "invalid date" or "TCR Creation Failed" status, this indicates TCR rejected the campaign due to a technical issue (e.g., a character requirement was missed, or the wrong number of sample messages was added). This is different from a carrier rejection. Contact [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) for help identifying the failure reason; the campaign will then need to be re-created.

## Campaign Registration Fields

| Field | Description | Length Constraints |
|---|---|---|
| Brand | The 10DLC brand to associate the campaign with. | — |
| Use Case | The use case matching your campaign. | — |
| Vertical | The industry vertical matching your business. | — |
| Campaign Description | Description of your campaign. | 40–4,096 characters |
| Sample Messages | Sample content representing messages you plan to send. One sample per selected use case; marketing requires 2; mixed should have one per sub-use case. | — |
| Campaign & Content Attributes | Indicate which attributes apply: subscriber opt-in, opt-out, help, number pooling, direct lending, embedded link, embedded phone number, affiliate marketing, age-gated content. | — |
| Message Flow | How users opt into the campaign. | 40–2,048 characters |
| Opt-in Keywords | Keywords for opting in (e.g., START, JOIN, YES). | Max 255 characters |
| Opt-in Message | Confirmation message sent on opt-in. | 20–320 characters |
| Opt-out Keywords | Keywords for opting out (e.g., STOP). | Max 255 characters |
| Opt-out Message | Confirmation message sent on opt-out. | 20–320 characters |
| Help Keywords | Keywords for requesting help (e.g., HELP). | Max 255 characters |
| Help Message | Message sent in response to help keyword. | 20–320 characters |
