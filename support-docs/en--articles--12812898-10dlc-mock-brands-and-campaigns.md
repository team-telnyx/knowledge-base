---
source_url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
title: "10DLC Mock Brands and Campaigns"
description: "In this article, we break down creating mock 10DLC brands and campaigns and their purpose. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: bd106bb9b5cb7262013679d900f6eaab74650e6565c5a676a247379f6c7c0d07
---







# 10DLC Mock Brands and Campaigns

In this article, we break down creating mock 10DLC brands and campaigns and their purpose. See Telnyx guidance and requirements.




If your business wants to try creating brands and campaigns to test API behavior, webhook events, or general 10DLC provisioning pipelines, creating a mock brand and mock campaigns can be useful. Mock brands and mock campaigns can be created at no cost allowing for a free way to test each step of your 10DLC integration. In this guide, we'll show you how to create mock brands and campaigns.

**Pre-requisites:**

Telnyx provides APIs and services that you can use to send text messages. We also provide a set of tools—available via our Mission Control Portal and our APIs—that you can use to register the messaging campaigns you send using the Telnyx platform for 10DLC. If you don't already have a Telnyx account, you can [sign up](https://telnyx.com/sign-up) and leverage these tools and resources to send 10DLC-compliant text messages.

## Creating a mock brand in the Mission Control Portal

Once you're logged into the [Mission Control Portal](https://portal.telnyx.com), head to the [10DLC Brand](https://portal.telnyx.com/#/messaging-10dlc/brands) tab. From here, you can get started by selecting "Create brand". On the first form, there is a checkbox for "Create as a mock brand to test 10DLC." Select this option to create a mock brand. You should see a note after checking the mock brand checkbox, "The registration fee of $4.00 is not applicable for a mock brand."

## Creating a mock brand using the Telnyx API

If you'd prefer to create your brand using a simple API command, you can find details in our [API reference documentation](https://telnyx.mintlify.app/api-reference/brands/create-brand). During creation of the brand set the "mock" field to true.

## Creating a mock campaign in the Mission Control Portal

Once you've created your mock brand, create a 10DLC campaign as normal in the [10DLC Campaign](https://portal.telnyx.com/#/messaging-10dlc/campaigns) tab. When creating your campaign, choose the mock brand you already created. Any campaign created under a mock brand will automatically be created as a mock campaign. Additionally, there is no registration fee or monthly recurring cost for a mock campaign. These fees are waived since there is no vetting or validation of mock campaign information.

## Creating a mock campaign using the Telnyx API

If you'd prefer to create your campaign using a simple API command, you can find details in our [API reference documentation](https://telnyx.mintlify.app/api-reference/campaign/submit-campaign). When supplying the "brandId" field, use the brand ID of the mock brand you already created.

## Notes on mock brands and campaigns

* Mock campaigns can not be used for real 10DLC traffic.
* Mock brands and campaigns are meant to be used for testing webhook responses for common 10DLC operations such as creating campaigns, brands, and assigning phone numbers to campaigns. These events can all be tested with mock brands and campaigns by configuring webhooks when creating mock brands and campaigns. More details on this process are found in this [documentation](https://telnyx.mintlify.app/docs/messaging/10dlc/event-notifications).
* No registration or monthly recurring fees are incurred for creating a mock brand or campaign.
* Mock brands and campaigns can be deleted when testing is complete using the standard deletion endpoint for [brands](https://telnyx.mintlify.app/api-reference/brands/delete-brand) and [campaigns](https://telnyx.mintlify.app/api-reference/campaign/deactivate-campaign), or by deletion in the mission control portal.

---

Related Articles

[Telnyx & 10DLC Compliance](https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance)[How to create a 10DLC brand](https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand)[How to create a 10DLC campaign](https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign)[10DLC Campaign Suspended](https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended)[Guide to Sole Proprietor 10DLC Brand and Campaign Registration](https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration)

Did this answer your question?

😞😐😃
