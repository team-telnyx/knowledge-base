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

*Part 3 of 6 — see also: [Part 1](telnyx-10dlc-process--part-1.md), [Part 2](telnyx-10dlc-process--part-2.md), [Part 4](telnyx-10dlc-process--part-4.md), [Part 5](telnyx-10dlc-process--part-5.md), [Part 6](telnyx-10dlc-process--part-6.md)*

A consolidated guide to registering, managing, and troubleshooting 10DLC brands, campaigns, and number assignments on the Telnyx platform, including fees, ISV requirements, sole proprietor registration, mock testing, suspension handling, and publicly traded brand authentication.

## Assign Numbers to a Campaign

Once your campaign is approved, you need to assign a number or numbers to it. This guide assumes you have set up an SMS-capable phone number with Telnyx already; if not, you need to either purchase or port one first. See [How to assign a number to a campaign](how-to-assign-a-number-to-a-campaign.md).

Important notes about assignment:

- A number can only be associated to one campaign, but a campaign can have up to 49 numbers.
- The 49 number maximum is due to T-Mobile limitations.
- If you wish to exceed this maximum, you must complete a T-Mobile Number Pool Request form, incurring additional charges. Telnyx Support can help you with this process.

To assign a number in the Mission Control Portal:

1. Navigate to the Campaigns page on the Portal.
2. Select the Campaign you wish to assign Phone Numbers to. You will be redirected to the Campaign Details page.
3. Navigate to the Assign Numbers panel.
4. Select the Messaging Profile the number is associated with, or select individual numbers to assign to said profile.
5. Select the number you wish to assign the campaign to.

### Number Assignment Status

Even if you have taken the step of assigning a number to a 10DLC campaign, you are not necessarily ready to start sending right away. The number assignment process can take anywhere from a few minutes to a few days; the normal timeline is around 2 hours. See [10DLC Number Assignment Status](10dlc-number-assignment-status.md).

You can check a number assignment's status using the [Get All Phone Number Campaigns API](https://developers.telnyx.com/api/messaging/10dlc/get-all-phone-number-campaigns):

1. Open the test endpoint black box.
2. Enter your API key for the bearer token. The API key is located on the homepage of your Telnyx account.
3. Enter your search parameters. Easiest is to use the Telnyx or TCR Campaign id that you assigned the number to.
4. If the status next to the number in question is `ASSIGNED`, then the number is successfully assigned.
5. If it is assigned but you still had deliverability issues, check the timestamp of the undelivered message against the timestamp for the last update on the assigned number. Normally you will see that it was all messages that were sent prior to the assignment process being complete.
6. If you still have deliverability issues, reach out to support@telnyx.com.

If assigning a DID to a 10DLC Campaign fails, reach out to 10dlcquestions@telnyx.com with your Telnyx account email, Campaign IDs, and any errors returned. See [Assigning DID to a 10DLC Campaign Fails](assigning-did-to-a-10dlc-campaign-fails.md).

## Campaign Suspension for Inactivity

If you see that your campaign has a TCR status of "Suspended," that normally means it is dormant from inactivity. The solution is normally assigning phone numbers to the campaign twice. The first time the campaign will reactivate and the number assignment will fail. The second time the number assignment will work. The reason for this is that T-Mobile charges a $250 per month fine for campaigns they deem as inactive, so Telnyx proactively puts campaigns in a suspended state before they get hit with the fine. See [10DLC Campaign Suspended](10dlc-campaign-suspended.md).

### Automatic Suspension Triggers

Your 10DLC campaign will be automatically suspended if all of these conditions are met:

- No activity for 15 consecutive days
- No active phone numbers assigned to the campaign
- Campaign is currently deployed with T-Mobile

This is a protective measure to prevent carrier fines for dormant campaigns.

### Webhook Notification

You can enable a webhook event when there is a suspension:

- For campaigns created in the Telnyx Portal or API: use the [Update My Campaign API](https://developers.telnyx.com/api/messaging/10dlc/update-campaign), or update the webhook field on the campaign's page in the portal, or set it when you first create the campaign using the webhook field on a new campaign submission.
- For campaigns created in the TCR Portal or API: use the [Update Single Shared Campaign API](https://developers.telnyx.com/api/messaging/10dlc/update-shared-campaign).

When your campaign is suspended due to inactivity, you will receive a webhook notification (if configured) with the following information:

```
{ "campaignId": "your-campaign-id", "type": "TELNYX_EVENT", "status": "DORMANT", "description": "Campaign has been marked as dormant" }
```

When you receive this notification, you should immediately take steps to reactivate your campaign.

### How to Prevent Suspension

- Keep phone numbers assigned (numbers should be added with T-Mobile). Maintain at least one active phone number on your campaign.
- Monitor usage. Regularly review your campaign activity.
- Set up webhooks. Configure webhook URLs in your campaign settings to receive real-time alerts.
- Plan ahead. If you know a campaign will be inactive, consider sending some traffic periodically.

### How to Reactivate a Suspended Campaign

Step 1: Assign Phone Numbers. Add or reassign phone numbers to your suspended campaign using the [Create New Phone Number Campaign API](https://developers.telnyx.com/api/messaging/10dlc/create-phone-number-campaign) or Mission Control Portal.

Step 2: Resume the Campaign. The system will automatically attempt to resume your campaign when you assign numbers. Allow 1-2 minutes for processing. The first number assignment will fail but should unsuspend the campaign.

Step 3: Verify Activation. Check your campaign status via the API or Mission Control Portal. Status should change from TCR_SUSPENDED back to active. Once the campaign is active you should be able to assign numbers now so that a suspension does not happen again.

### Troubleshooting Reactivation

If standard reactivation doesn't work, try these steps:

Option 1: Wait and Retry. The system uses automatic retry intervals: 1 minute → 10 minutes → 1 hour. Wait for the full retry cycle before attempting again.

Option 2: Manual Process:

1. Remove all phone numbers from the campaign.
2. Wait 2-3 minutes.
3. Re-add phone numbers to the campaign.
4. Monitor for confirmation webhook.

Option 3: Contact Support. If you've tried the above and your campaign is still suspended, contact Telnyx Support (Support@telnyx.com) with:

- Campaign ID
- TCR Campaign ID (if available)
- Timestamp of when you attempted reactivation
- Any error messages received

The support team can check for carrier-level issues, verify campaign status with T-Mobile, manually trigger reactivation if needed, and review your account for billing or compliance issues.

### Important Notes

- Avoid Carrier Fines: T-Mobile charges fees for inactive campaigns.
- Maintain Compliance: Dormant campaigns may impact your sender reputation.
- Cost Management: Suspended campaigns help you avoid unnecessary charges.
- Suspended campaigns may affect your monthly billing. Review your campaign costs regularly. Deactivate campaigns you no longer need instead of leaving them inactive.
- Messages sent from a suspended campaign may be blocked or rejected by carriers.
- Reactivation is free. However, leaving campaigns dormant may result in carrier fees.
- Reactivation typically takes 1-5 minutes after reassigning phone numbers.
