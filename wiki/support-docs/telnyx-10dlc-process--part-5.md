---
title: Telnyx 10DLC Process
summary: A consolidated guide to registering, managing, and troubleshooting 10DLC
  brands, campaigns, and number assignments on the Telnyx platform, including fees,
  ISV requirements, sole proprietor registration, mock testing, suspension handling,
  and publicly traded brand authentication.
sources:
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
- url: https://support.telnyx.com/en/articles/5593977-isvs-10dlc
- url: https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges
- url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
updated_at: 2026-08-05T13:25:29Z
---

# Telnyx 10DLC Process

*Part 5 of 6 — see also: [Part 1](telnyx-10dlc-process--part-1.md), [Part 2](telnyx-10dlc-process--part-2.md), [Part 3](telnyx-10dlc-process--part-3.md), [Part 4](telnyx-10dlc-process--part-4.md), [Part 6](telnyx-10dlc-process--part-6.md)*

A consolidated guide to registering, managing, and troubleshooting 10DLC brands, campaigns, and number assignments on the Telnyx platform, including fees, ISV requirements, sole proprietor registration, mock testing, suspension handling, and publicly traded brand authentication.

## Mock Brands and Campaigns

If your business wants to try creating brands and campaigns to test API behavior, webhook events, or general 10DLC provisioning pipelines, creating a mock brand and mock campaigns can be useful. Mock brands and mock campaigns can be created at no cost, allowing for a free way to test each step of your 10DLC integration. See [10DLC Mock Brands and Campaigns](10dlc-mock-brands-and-campaigns.md).

### Creating a Mock Brand in the Mission Control Portal

Once you're logged into the Mission Control Portal, head to the 10DLC Brand tab. From here, you can get started by selecting "Create brand". On the first form, there is a checkbox for "Create as a mock brand to test 10DLC." Select this option to create a mock brand. You should see a note after checking the mock brand checkbox, "The registration fee of $4.00 is not applicable for a mock brand."

### Creating a Mock Brand Using the Telnyx API

If you'd prefer to create your brand using a simple API command, see the [API reference documentation](https://telnyx.mintlify.app/api-reference/brands/create-brand). During creation of the brand, set the "mock" field to true.

### Creating a Mock Campaign in the Mission Control Portal

Once you've created your mock brand, create a 10DLC campaign as normal in the 10DLC Campaign tab. When creating your campaign, choose the mock brand you already created. Any campaign created under a mock brand will automatically be created as a mock campaign. Additionally, there is no registration fee or monthly recurring cost for a mock campaign. These fees are waived since there is no vetting or validation of mock campaign information.

### Creating a Mock Campaign Using the Telnyx API

If you'd prefer to create your campaign using a simple API command, see the [API reference documentation](https://telnyx.mintlify.app/api-reference/campaign/submit-campaign). When supplying the "brandId" field, use the brand ID of the mock brand you already created.

### Notes on Mock Brands and Campaigns

- Mock campaigns cannot be used for real 10DLC traffic.
- Mock brands and campaigns are meant to be used for testing webhook responses for common 10DLC operations such as creating campaigns, brands, and assigning phone numbers to campaigns. These events can all be tested with mock brands and campaigns by configuring webhooks when creating mock brands and campaigns.
- No registration or monthly recurring fees are incurred for creating a mock brand or campaign.
- Mock brands and campaigns can be deleted when testing is complete using the standard deletion endpoint for [brands](https://telnyx.mintlify.app/api-reference/brands/delete-brand) and [campaigns](https://telnyx.mintlify.app/api-reference/campaign/deactivate-campaign), or by deletion in the Mission Control Portal.
