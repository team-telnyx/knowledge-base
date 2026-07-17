---
title: 10DLC Registration and Compliance
summary: A consolidated reference for registering and operating 10DLC messaging on
  Telnyx, covering the end-to-end brand and campaign workflow, mock testing, CTA and
  message flow requirements, opt-in form design, privacy policy language, sample messages,
  age gates, political campaigns, common errors, and associated fees.
sources:
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
- url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
updated_at: 2026-07-17T09:00:56Z
---

# 10DLC Registration and Compliance

*Part 2 of 5 — see also: [Part 1](10dlc-registration-and-compliance--part-1.md), [Part 3](10dlc-registration-and-compliance--part-3.md), [Part 4](10dlc-registration-and-compliance--part-4.md), [Part 5](10dlc-registration-and-compliance--part-5.md)*

A consolidated reference for registering and operating 10DLC messaging on Telnyx, covering the end-to-end brand and campaign workflow, mock testing, CTA and message flow requirements, opt-in form design, privacy policy language, sample messages, age gates, political campaigns, common errors, and associated fees.

## Mock Brands and Campaigns

Mock brands and campaigns let you test API behavior, webhook events, and provisioning pipelines at no cost. They cannot be used for real 10DLC traffic and incur no registration or monthly recurring fees.

- **Portal — Mock Brand:** In the [10DLC Brand](https://portal.telnyx.com/#/messaging-10dlc/brands) tab, select "Create brand" and check "Create as a mock brand to test 10DLC." A note confirms the $4 registration fee does not apply.
- **API — Mock Brand:** Set the `mock` field to `true` when calling the [create-brand endpoint](https://telnyx.mintlify.app/api-reference/brands/create-brand).
- **Portal — Mock Campaign:** Create a campaign as normal in the [10DLC Campaign](https://portal.telnyx.com/#/messaging-10dlc/campaigns) tab and choose the mock brand. Any campaign under a mock brand is automatically a mock campaign.
- **API — Mock Campaign:** Pass the mock brand's ID as `brandId` to the [submit-campaign endpoint](https://telnyx.mintlify.app/api-reference/campaign/submit-campaign).

Mock brands and campaigns are useful for testing webhook responses for common 10DLC operations (creating campaigns, brands, assigning phone numbers). Configure webhooks when creating them; see the [event notifications documentation](https://telnyx.mintlify.app/docs/messaging/10dlc/event-notifications). When testing is complete, delete them via the standard [delete-brand](https://telnyx.mintlify.app/api-reference/brands/delete-brand) and [deactivate-campaign](https://telnyx.mintlify.app/api-reference/campaign/deactivate-campaign) endpoints, or in the Mission Control Portal.

## Creating a Campaign

Every campaign must be associated with a brand. A good Trust Score is also important, because A2P 10DLC throughput is determined by Trust Score and Campaign Use Case. See [10DLC Trust Scores & Use Cases](10dlc-trust-scores-use-cases.md).

In the Mission Control Portal, navigate to Messaging → Compliance → [10DLC Campaigns](https://portal.telnyx.com/#/messaging-10dlc/campaigns). Via the API, see the [campaigns endpoints](https://developers.telnyx.com/api/messaging/10dlc/get-campaigns).

### Campaign Fields

- **Brand** — the 10DLC brand to associate with the campaign.
- **Use Case** — Two Factor Authentication, Alerts/Notifications, Agents and Franchises, Carrier Exemptions, Charity, Customer Care (Conversational Messaging), Delivery Notifications, Emergency Alerts, Fraud Alerts, Education, Marketing, Political, Polling/Voting, Public Service Announcements, Security, Social, Sole Proprietor, or Sweepstakes. Messages that do not align with the registered use case may be subject to fines, throughput limitations, and blocks.
- **Vertical** — industry vertical that best matches the business.
- **Campaign Description** — describes who is using the campaign and what it is intended for. Example: "Appointment reminder and confirmation notifications for a dentist's office to remind their patients of newly scheduled and upcoming appointments date and times."
- **Sample Messages** — sample content representing the messages you plan to send. One sample message is required per selected use case; Marketing requires 2; Mixed requires a minimum of 2 (one per sub-use case). Messages that do not align with the registered sample can be flagged for review. Up to 5 samples are recommended, consistent with brand, campaign description, and website, and ideally within the 160-character industry best practice.
- **Campaign and Content Attributes** — indicate which apply: Subscriber opt-in, Subscriber opt-out, Subscriber help, Number pooling, Direct lending or loan arrangement, Embedded link, Embedded phone number, Affiliate marketing, Age-gated content.
- **Message Flow** — describes how users opt into the campaign. Must be 40–2048 characters and provide explicit information about how the end user opts in before the first message is sent. If opt-in is via a website form, provide the link to the specific page where opt-in is gathered; optionally include a screenshot (for example a publicly accessible Google Drive link); include a link to the privacy policy. See [Guide to 10DLC Message Flow Field](guide-to-10dlc-message-flow-field.md).
- **Opt-in Keywords** — required. Example: START, JOIN, YES. See [10DLC Keywords and Confirmation Messages](10dlc-keywords-and-confirmation-messages.md).
- **Opt-in Message** — see [10DLC Keywords and Confirmation Messages](10dlc-keywords-and-confirmation-messages.md).
- **Opt-out Keywords** — example: STOP. See [10DLC Keywords and Confirmation Messages](10dlc-keywords-and-confirmation-messages.md).
- **Opt-out Message** — see [10DLC Keywords and Confirmation Messages](10dlc-keywords-and-confirmation-messages.md).
- **Help Keywords** — example: HELP.
- **Help Message** — see [10DLC Keywords and Confirmation Messages](10dlc-keywords-and-confirmation-messages.md).

### Field Length Limits

| Field | Min | Max |
| --- | --- | --- |
| Campaign description | 40 | 4096 |
| Help message | 20 | 320 |
| Message Flow | 40 | 2048 |
| Opt-in Message | 20 | 320 |
| Opt-out Message | 20 | 320 |
| Opt-in Keywords | — | 255 |
| Opt-out Keywords | — | 255 |
| Help Keywords | — | 255 |

### After Submission

Telnyx sends automatic status update emails for every campaign to the username email on the account. To add more recipients, ask your CSM, or email [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) if you do not have one. Once "Approved" is received, assign numbers to the campaign and begin sending.

An "invalid date" or "TCR Creation Failed" status indicates TCR rejected the campaign for a technical reason (for example, a missed character requirement or the wrong number of sample messages — at least one sample per use case is required, so a Mixed campaign with 5 sub-use cases needs 5 samples). This is different from a carrier rejection. Email [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) to identify the failure reason; the campaign will need to be re-created.

## Assigning Numbers to a Campaign

Once a campaign is approved, assign numbers to it. This assumes an SMS-capable number is already set up with Telnyx; if not, [purchase](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) or [port](https://support.telnyx.com/en/articles/1130634-port-numbers-to-telnyx) one first.

- A number can only be associated with one campaign, but a campaign can have up to 49 numbers.
- The 49-number maximum is due to T-Mobile limitations. To exceed it, complete a T-Mobile Number Pool Request form (additional charges apply); Telnyx Support can help. See [10DLC Fees and Charges](10dlc-fees-and-charges.md).

In the Mission Control Portal: navigate to the Campaigns page, select the campaign, open the Assign Numbers panel, choose the Messaging Profile the number is associated with (or select individual numbers), and select the number to assign. Via the API, see the [10DLC API documentation](https://developers.telnyx.com/docs/messaging/10dlc/concepts).
