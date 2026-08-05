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

*Part 2 of 6 — see also: [Part 1](telnyx-10dlc-process--part-1.md), [Part 3](telnyx-10dlc-process--part-3.md), [Part 4](telnyx-10dlc-process--part-4.md), [Part 5](telnyx-10dlc-process--part-5.md), [Part 6](telnyx-10dlc-process--part-6.md)*

A consolidated guide to registering, managing, and troubleshooting 10DLC brands, campaigns, and number assignments on the Telnyx platform, including fees, ISV requirements, sole proprietor registration, mock testing, suspension handling, and publicly traded brand authentication.

## Create a Campaign

Once your brand is Verified, create a campaign. See [How to create a 10DLC campaign](how-to-create-a-10dlc-campaign.md) for the full walkthrough.

Important:

- You must select "True" for Opt in, Opt out, and HELP radio buttons. If not, TCR will reject the campaign creation.
- Every campaign must be associated with a brand. If you haven't already registered your brand, you'll need to do that before you can activate a campaign and send messages.
- Ensure that your brand has a good Trust Score, as A2P 10DLC message throughput is determined based on your Trust Score and your Campaign Use Case.

Common errors to avoid:

- Campaigns with a TCR ID starting with `4b3` or a status of "Failed TCR Review" were not created successfully. This often happens if the campaign is created before the brand is verified.
- If you are receiving an "invalid date" or "TCR Creation Failed" status for your campaign in the Telnyx portal, this indicates that TCR has rejected the campaign due to a technical issue with your submission, such as a character requirement being missed or the wrong number of sample messages being added (you must have at least one sample message per use case selected, so if you select Mixed and then have 5 sub Use Cases then you must have 5 sample messages). It is different than a carrier rejection. Reach out to 10dlcquestions@telnyx.com to identify the failure reason; the campaign will need to be re-created.

### Campaign Information

A campaign contains information about the messages you intend to send. You will be asked for the following information when registering a 10DLC campaign.

- Brand: The 10DLC brand you want to associate this campaign with.
- Use case: The use case that best matches your campaign. Options include Two Factor Authentication, Alerts/Notifications, Agents and Franchises, Carrier Exemptions, Charity, Customer Care (Conversational Messaging), Delivery Notifications, Emergency Alerts, Fraud Alerts, Education, Marketing, Political, Polling/Voting, Public Service Announcements, Security, Social, Sole Proprietor, and Sweepstakes. Messages sent that do not align with your registered use case may be subject to fines and throughput limitations and blocks.
- Vertical: The industry vertical which best matches your business.
- Campaign description: The description of your campaign.
- Sample messages: Sample content that represents the messages you plan to send to end users. You may add multiple sample messages. You need one sample message for each selected use case. A marketing use case requires 2 sample messages. A Mixed use case requires a minimum of 2 sample messages but should have one for each selected use case. Messages sent that do not align with the registered sample message can be flagged for review.
- Campaign and content attributes: Indicate which content attributes you will or will not be providing: Subscriber opt-in, Subscriber opt-out, Subscriber help, Number pooling, Direct lending or loan arrangement, Embedded link, Embedded phone number, Affiliate marketing, Age-gated content.
- Message Flow: The customers need to add information of how the users opt in to the campaign. Example: The users visit the website and add their phone number to agree receiving the messages. The length of the "Message Flow" description should be between 40 and 2048 characters.
- Opt-in Keywords: Required field. Example: START, JOIN, YES.
- Opt-in Message: Follow the required format.
- Opt-out Keywords: Example: STOP.
- Opt-out Message: Follow the required format.
- Help Keywords: The end users should be able to text in a keyword to receive help. Those keywords must be provided as part of the campaign registration request. Example keyword: HELP.
- Help Message: Follow the required format.

Field length requirements:

| Field | Min length | Max length |
| --- | --- | --- |
| Campaign description | 40 | 4096 |
| Help message | 20 | 320 |
| Message Flow | 40 | 2048 |
| Opt in Message | 20 | 320 |
| Opt out Message | 20 | 320 |
| Opt-in Keywords |  | 255 |
| Opt-out Keywords |  | 255 |
| Help Keywords |  | 255 |

## Telnyx Review of the Campaign

After submission, Telnyx will review the campaign. Review happens same day or next business day, depending on submission time. You will receive one of two emails at your Telnyx account's main username email.

### Sent for Carrier Review

- The campaign has been submitted downstream.
- Carrier review takes 3 business days or less, depending on volume.

### Flagged for Corrections

- The campaign contains incorrect or impermissible content.
- You will receive feedback on what needs to be updated.
- No further action will be taken until the 10DLC squad is notified at 10dlcquestions@telnyx.com.

Please reply to the same email thread for each campaign to help us stay organized.

## After Campaign Review

Once the campaign is submitted for carrier review and Telnyx receives a response, you'll receive one of two emails.

### Approved

- Once approved, you can assign up to 49 numbers to the campaign and begin messaging. See [How to assign a number to a campaign](how-to-assign-a-number-to-a-campaign.md).

### Declined

- You'll receive an email explaining why the campaign was declined, including error codes. See [10DLC Carrier Error Codes and Explanations](https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations).

Respond on the same email thread with questions or updates for resubmission.
