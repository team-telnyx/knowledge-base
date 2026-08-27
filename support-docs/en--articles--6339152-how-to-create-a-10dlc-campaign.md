---
source_url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
title: "How to create a 10DLC campaign"
description: "Creating a campaign is the second step to becoming compliant with 10DLC rules. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: ba5b36e22886219329a142b32b5efc7c594b903d68df43b065b45e80b485d78b
---







# How to create a 10DLC campaign

Creating a campaign is the second step to becoming compliant with 10DLC rules. See Telnyx guidance and requirements.




## **How to create a 10DLC campaign**

If your business is sending outbound text messages using 10-digit long code (10DLC) Local phone numbers in the US, you're required to register for 10DLC. In this guide, we'll show you how to complete the second step of this process by registering campaigns, using tools provided in the Telnyx Mission Control Portal.

## **Pre-requisites**

Every campaign must be associated with a brand. If you haven't already registered your brand, you'll need to do that before you can activate a campaign and send messages. Follow this [guide](https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand) to complete this first step before moving onto creating a campaign.

Additionally, you will want to ensure that your brand has a good Trust Score, as A2P 10DLC message throughput is determined based on your Trust Score and your Campaign Use Case. Learn more on [throughput and Trust Scores in this article](https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases).

## **Creating a 10DLC campaign in the Mission Control Portal**

Once you’ve created a Business Brand in [Mission Control Portal](https://portal.telnyx.com), head to the Messaging section > Compliance > and then to the [10DLC Campaigns](https://portal.telnyx.com/#/messaging-10dlc/campaigns) tab. From here, you can get started on creating a campaign.

## **Creating a 10DLC campaign using the Telnyx API**

If you'd prefer to create your brand using a simple API command, you can find details in our [API reference documentation](https://developers.telnyx.com/api/messaging/10dlc/get-campaigns).

## **Information you'll need to register your 10DLC campaigns**

A campaign contains information about the messages you intend to send. You'll be asked for the following information when registering a 10DLC campaign.

## What is message flow?

When adding a new campaign, "Message Flow" refers to the process of how users opt into the campaign. For example, users might visit a website and add their phone number to agree to receive messages. This information needs to be added when registering a 10DLC campaign.

**Message Flow:** <https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field>

Please note that the length of the "Message Flow" description should be between 40 and 2048 characters.

|  |  |
| --- | --- |
| **Item** | **Description** |
| Brand | The 10DLC brand you want to associate this campaign with. |
| Use case | The use case that best matches your campaign.  **Standard use cases:** * 2FA * Account Notification * Customer Care (Conversational Messaging) * Delivery Notifications * Fraud Alert Messaging * Higher Education * Low Volume Mixed * Machine-to-Machine (M2M) * Marketing * Mixed * Polling/Voting * Public Service Announcement * Security Alert  **Special use cases:** * Agents and Franchises * Carrier Exemptions * Charity * Emergency * K-12 Education * Platform Free Trial * Political * Proxy * Public Safety (Restricted) * Social * Sole Proprietor * Sweepstake * UCaaS Low Volume * UCaaS High Volume  Some special use cases carry extra requirements — for example: Political (requires a [CampaignVerify](https://www.campaignverify.org/) token, double opt-in for verbal consent, and donation disclosure), Charity (must include "donations will be solicited"; 501(c)(3) required), and Sole Proprietor (only 1 active campaign, 1 number, and no Inc/LLC/Group/Enterprise in the brand name — see the [Sole Proprietor guide](https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration)). See [10DLC Use Cases](https://support.telnyx.com/en/articles/10684248-10dlc-use-cases) for full descriptions.  *Messages sent that do not align with your registered use case may be subject to fines and throughput limitations and blocks.* |
| Vertical | The industry vertical which best matches your business. |
| Campaign description | The description of your campaign. |
| Sample messages | Sample content that represents the messages you plan to send to end users. You may add multiple sample messages. You need one sample message for each selected use case. A marketing use case requires 2 sample messages. A Mixed use case requires a minimum of 2 sample messages but should have one for each selected use case.    *Messages sent that do not align with the registered sample message can be flagged for review.* |
| Campaign and content attributes | Indicate which content attributes you will or will not be providing:  * Subscriber opt-in * Subscriber opt-out * Subscriber help * Number pooling * Direct lending or loan arrangement * Embedded link * embedded phone number * Affiliate marketing * Age-gated content |
| Message Flow | The customers need to add information of how the users opt in to the campaign.    Example: The users visit the website and add their phone number to agree receiving the messages. |
| Opt-in Keywords | Required field.  Example: START, JOIN, YES    <https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages> |
| Opt-in Message | Please follow this format: ​<https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages> |
| Opt-out Keywords | Example: STOP ​ Please follow this format: ​<https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages> |
| Opt-out Message | Please follow this format: ​<https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages> |
| Help Keywords | The end users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request.    Example keyword: HELP |
| Help Message | Please follow this format: ​<https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages> |

|  |  |  |
| --- | --- | --- |
| **Field** | **Min length** | **Max length** |
| Campaign description | 40 | 4096 |
| Help message | 20 | 320 |
| Message Flow | 40 | 2048 |
| Opt in Message | 20 | 320 |
| Opt out Message | 20 | 320 |
| Opt-in Keywords |  | 255 |
| Opt-out Keywords |  | 255 |
| Help Keywords |  | 255 |

**Next steps after registering your campaign**

The next step after you’ve registered your campaign is it will be reviewed and either approved or declined. We will send automatic status update emails for every campaign to the username email on the account. If you would like for more email addresses to receive 10dlc status notifications please ask your CSM to add the email. If you have no csm you can request the addition by messaging [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com). Once you have received the "Approved" status notification for the campaign you [assign numbers to it](https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign) and begin sending! Congrats :).

**What the review process looks like:**

* You **must select "True"** for the **Opt in, Opt out, and HELP** radio buttons — if not, TCR will reject the campaign creation.
* Telnyx reviews the campaign first — **same day or next business day**, depending on submission time. You will receive either a **"Sent for Carrier Review"** email (the campaign was submitted downstream; carrier review takes **3 business days or less**) or a **"Flagged for Corrections"** email (the campaign contains incorrect or impermissible content; no further action will be taken until you notify the 10DLC squad at [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com)).
* After carrier review you'll receive either an **Approved** email (assign up to 49 numbers and begin messaging) or a **Declined** email explaining why, including error codes — see [10DLC Carrier Error Codes and Explanations](https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations).
* Please **reply on the same email thread** for each campaign with questions or updates for resubmission.
* Campaigns with a **TCR ID starting with `4b3`** or a status of **"Failed TCR Review"** were not created successfully. This often happens if the campaign is created **before the brand is verified**.

Note: If you are receiving an "invalid date" or TCR Creation Failed status for your campaign in the Telnyx portal then this indicates that TCR (the regulating body of US local text messaging) has rejected the campaign due to a technical issue with your submission such as a character requirement was missed or the wrong number of sample messages was added (you must have at least one sample message per use case selected so if you select Mixed and then have 5 sub Use Cases then you must have 5 sample messages). It is different than a carrier rejection. If you are having this issue please reach out to us at [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) and we will work with our messaging team to identify the failure reason. Then we will communicate the failure reason to you and the campaign will need to be re-created.

If you have any messaging compliance questions please reach out to us at [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com).

---

Related Articles

[How to create a 10DLC brand](https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand)[10DLC Campaign Approval Best Practices](https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices)[10DLC Campaign Compliance Requirements](https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements)[10DLC Campaign Suspended](https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended)[Guide to Sole Proprietor 10DLC Brand and Campaign Registration](https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration)

Did this answer your question?

😞😐😃
