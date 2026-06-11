---
title: 10DLC Campaign Registration and Compliance
summary: A comprehensive guide to registering, configuring, and maintaining compliant
  10DLC campaigns on Telnyx, covering use cases, trust scores, opt-in methods, message
  flow, CTA requirements, keyword configuration, number assignment, shared campaigns,
  and approval best practices.
sources:
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
  content_hash: 52724a201fd5374074a0eb90e9410468b85a7658feedbe8a9d47840d78861363
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
  content_hash: 1642b9aa15da6996121686960f14303b8ae52ce210e2da3f8d83db58714cc412
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
  content_hash: 8ad5cdae420fd7df4a80633f0af9e3ae25b2442e724a222f7a3e1070264f0351
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
  content_hash: 770ca9ba38e331a0bef2ee21c47f1bcb1145a0bc5ca188b8c03c487ac05a2dab
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
  content_hash: e626ef28a6a0be235fefc591464a31366236db066180b4f1bf535dcad173c9c9
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
  content_hash: 2bd820c19999d71842708f2f7ec38f7c7406888e79ed9c0b45dc2eec3f465904
- url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
  content_hash: d6bd1ec81d473ca63ef7c249bc414517b46feea43b2132519727076e3bfa6773
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
  content_hash: ba5b36e22886219329a142b32b5efc7c594b903d68df43b065b45e80b485d78b
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
  content_hash: 639b3ec94281b897babf04a81683f8dda03b1be42c8865bc196cdaffea808c7a
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
  content_hash: e8663aa9412e6dc56b01f487761c2cf0bce4e360dd4cf455c7b9a0d3343fdcac
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
  content_hash: 5695a125b887d6ce58992c100db1af80399f925aa5b3dbf4f323ff550d0dc73a
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
  content_hash: 1672ce4b25969e32d5e38d4007ed007a55568633b07ad0b102d6ef139f1bcf16
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
  content_hash: 10cadb4c1a4e41ac2d6f453c897e739d96f4e1efe24ab346ee6fed9dd87bcd25
updated_at: 2026-06-11T11:11:29Z
---

# 10DLC Campaign Registration and Compliance

*Part 4 of 4 — see also: [Part 1](10dlc-campaign-registration-and-compliance--part-1.md), [Part 2](10dlc-campaign-registration-and-compliance--part-2.md), [Part 3](10dlc-campaign-registration-and-compliance--part-3.md)*

A comprehensive guide to registering, configuring, and maintaining compliant 10DLC campaigns on Telnyx, covering use cases, trust scores, opt-in methods, message flow, CTA requirements, keyword configuration, number assignment, shared campaigns, and approval best practices.

## Campaign Approval Best Practices

To maximize approval chances, follow these guidelines:

- **No forbidden use cases** — Avoid prohibited content such as cannabis, hate speech, etc.
- **Consistency across brand, website, and sample messages** — The brand and website must match what appears in sample messages.
- **Consistency between sample messages and use cases** — A political campaign with 2FA sample messages will be rejected.
- **Consistency between email domain and company name** — Large corporations should use dedicated email domains, not generic ones (e.g., gmail).
- **Submit only real, working websites** — Non-functional websites will result in rejection. For customers lacking websites, provide a Google Business Profile or a social media link (LinkedIn/Instagram).
- **Send messages according to the registered brand** — Registering as a technology company but sending messages for a construction company will result in rejection.
- **Collect consumer opt-in appropriately** — Follow [CTIA guidelines](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf) for handling consumer consent.
- **Opt-in language on website** — If your message flow indicates web opt-in, the opt-in language must be present on the site.
- **Include opt-out in sample messages** — At least one sample must include opt-out language.
- **Express opt-in everywhere a phone number is collected** — Every form field collecting a phone number (contact pages, donation pages, etc.) must have opt-in language and an unchecked checkbox with consent, opt-out instructions, and links to Privacy Policy and T&C.

## Assigning Numbers to a Campaign

Once your campaign is approved, the next step is assigning phone numbers. A number can only be associated with one campaign, but a campaign can have up to 49 numbers (a T-Mobile limitation). To exceed 49 numbers, you must complete a T-Mobile Number Pool Request form, incurring additional charges. Contact Telnyx Support for assistance.

### Via the Mission Control Portal

1. Navigate to the **Campaigns** page.
2. Select the campaign to assign numbers to (redirects to Campaign Details).
3. Go to the **Assign Numbers** panel.
4. Select the Messaging Profile associated with the number, or select individual numbers.
5. Choose the number(s) to assign.

### Via the API

Use the [10DLC API endpoints](https://developers.telnyx.com/docs/messaging/10dlc/concepts) to assign numbers programmatically.

If assignment fails, contact [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) with your Telnyx account email, Campaign IDs, and any errors returned.

## Number Assignment Status

Assigning a number to a campaign does not mean you can send immediately. The assignment process can take anywhere from a few minutes to a few days, with the normal timeline around 2 hours.

Check assignment status using the [Get All Phone Number Campaigns endpoint](https://developers.telnyx.com/api/messaging/10dlc/get-all-phone-number-campaigns):

1. Enter your API key for the bearer token (found on your Telnyx account homepage).
2. Enter your search parameters (easiest is the Telnyx or TCR Campaign ID).
3. If the status is `ASSIGNED`, the number is successfully assigned.
4. If assigned but you still have deliverability issues, compare the timestamp of the undelivered message against the last update timestamp on the assigned number — normally, failed messages were sent before the assignment process completed.
5. If issues persist, contact [support@telnyx.com](mailto:support@telnyx.com).

## Shared Campaigns

A shared campaign is registered directly through The Campaign Registry rather than through Telnyx. In this model, Telnyx acts as the **upstream connectivity partner (upstream CNP)** for your campaign, and your organization is the **downstream CNP**.

> **Note:** Using shared campaigns limits Telnyx's ability to troubleshoot issues with your 10DLC campaigns and throughput. In most cases, creating brands and campaigns through the Telnyx portal is recommended.

### Importing Shared Campaigns

1. **Provide your CSP ID to Telnyx** — Find your CSP ID in the [Campaign Registry CSP Portal](https://csp.campaignregistry.com/login) and share it with your account manager or email [support@telnyx.com](mailto:support@telnyx.com). Association typically takes up to two business days.
2. **Share the campaign** — In the Campaign Registry CSP Portal, choose the campaign and select Telnyx as the connectivity partner. This submits a review request to Telnyx.
3. **Approval** — After Telnyx reviews and approves the shared campaign, Telnyx will appear as the connectivity partner in your Campaign Registry CSP Portal.

The Telnyx CSP ID is: **SS4XJ6D**.

### Adding Telnyx Numbers to Shared Campaigns

The only way to associate Telnyx numbers with shared campaigns is via the [Bulk Phone Number Campaigns endpoint](https://developers.telnyx.com/api/messaging/10dlc/post-assign-messaging-profile-to-campaign). Before making the API request:

1. Ensure all numbers are associated with the same [Messaging Profile](https://developers.telnyx.com/docs/messaging/messages/mission-control-portal-set-up).
2. Obtain the Messaging Profile ID from the [portal](https://portal.telnyx.com/#/app/messaging) or [by API](https://developers.telnyx.com/api/messaging/list-messaging-profiles).
3. Obtain the TCR ID of your shared campaign from the Campaign Registry CSP Portal.

After submitting the API request, you can check the status of the entire request or individual numbers via the Telnyx API.

### Shared Campaign Limitations

- **Cannot update through the Telnyx portal** — All brand and campaign information must be maintained directly through the Campaign Registry CSP Portal. Telnyx has limited visibility into shared campaign details.
- **Cannot edit a sharing request while pending** — Once you've selected Telnyx as the upstream CNP and the status is `PENDING`, you cannot rescind the sharing request or change the upstream CNP.

## Troubleshooting

If your campaign is rejected, a Telnyx team member will reach out to help fix the registration or re-submit. For any 10DLC questions or challenges, contact [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com). For number assignment issues specifically, include your Telnyx account email, Campaign IDs, and any errors returned.

For deliverability issues after assignment, see [10DLC Number Assignment Status](10dlc-number-assignment-status.md). For suspended campaigns, see [10DLC Campaign Suspended](10dlc-campaign-suspended.md). For carrier error codes, see [10DLC Carrier Error Codes Explanations](10dlc-carrier-error-codes-explanations.md).
