---
source_url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
scraped: 2026-06-11
---

10DLC Campaign Suspended | Telnyx Help Center

[Skip to main content](#main-content)

# 10DLC Campaign Suspended

10DLC Campaign Suspension

K

Written by Klane Pedrie

November 12, 2025

Table of contents

# Why is my 10DLC / TCR Campaign Suspended?

If you see that your campaign has a TCR status of "Suspended" that normally means that it is dormant from inactivity. The solution normally is assigning phone numbers to the campaign twice. The first time the campaign will reactivate and the number assignment will fail. The second time the number assignment will work. The reason for this is that T-Mobile charges a $250 per month fine for campaigns they deem as inactive so we proactively put campaigns in a suspended state before they get hit with the fine.

10DLC Campaign Suspension for Inactivity - Customer Guide

Overview

To help customers avoid T-Mobile fines and maintain campaign compliance, Telnyx has implemented an automatic campaign suspension system for inactive 10DLC campaigns. This guide explains how it works and what actions customers should take.

---

How It Works

Automatic Suspension Triggers

Your 10DLC campaign will be automatically suspended if all of these conditions are met:

✅ No activity for 15 consecutive days  
✅ No active phone numbers assigned to the campaign   
✅ Campaign is currently deployed with T-Mobile

Important: This is a protective measure to prevent carrier fines for dormant campaigns.

---

New Webhook Notification

Real-Time Alerts

Using these commands you can enable a webhook event when there is a suspension:

Campaigns created in the Telnyx Portal or API: [Update My Campaign API | Telnyx](https://developers.telnyx.com/api/messaging/10dlc/update-campaign) or you can go to the campaign's page in the portal and update the webhook field or set it when you first create the campaign using the webhook field on a new campaign submission.

Campaigns created in the TCR Portal or API: [Update Single Shared Campaign API | Telnyx](https://developers.telnyx.com/api/messaging/10dlc/update-shared-campaign)

When your campaign is suspended due to inactivity, you will receive a webhook  
 notification (if configured) with the following information:

`{ "campaignId": "your-campaign-id", "type": "TELNYX_EVENT", "status": "DORMANT", "description": "Campaign has been marked as dormant" }`

Action Required: When you receive this notification, you should immediately take steps to reactivate your campaign (see below).

---

How to Prevent Suspension

Best Practices

1. Keep phone numbers assigned (Numbers should be added with T-Mobile) - Maintain at least one active phone number on your campaign
2. Monitor usage - Regularly review your campaign activity
3. Set up webhooks - Configure webhook URLs in your campaign settings to receive real-time alerts
4. Plan ahead - If you know a campaign will be inactive, consider sending some traffic periodically.

---

How to Reactivate a Suspended Campaign

If your campaign has been suspended, follow these steps to reactivate it:

Step 1: Assign Phone Numbers

* Add or reassign phone numbers to your suspended campaign
* Use the [Create New Phone Number Campaign API | Telnyx](https://developers.telnyx.com/api/messaging/10dlc/create-phone-number-campaign) or Mission Control Portal

Step 2: Resume the Campaign

* The system will automatically attempt to resume your campaign when you assign numbers
* Allow 1-2 minutes for processing
* The first number assignment will fail but should unsuspend the campaign

Step 3: Verify Activation

* Check your campaign status via the API or Mission Control Portal
* Status should change from TCR\_SUSPENDED back to active
* Once the campaign is active you should be able to assign numbers now so that a suspension does not happen again.

---

Troubleshooting

"I've tried reassigning numbers twice but it's not working"

If standard reactivation doesn't work, try these steps:

Option 1: Wait and Retry

* The system uses automatic retry intervals: 1 minute → 10 minutes → 1 hour
* Wait for the full retry cycle before attempting again

Option 2: Manual Process

1. Remove all phone numbers from the campaign
2. Wait 2-3 minutes
3. Re-add phone numbers to the campaign
4. Monitor for confirmation webhook

Option 3: Contact Support

If you've tried the above and your campaign is still suspended:

Contact Telnyx Support ([Support@telnyx.com](mailto:Support@telnyx.com)) with:

* Campaign ID
* TCR Campaign ID (if available)
* Timestamp of when you attempted reactivation
* Any error messages received

Our support team can:

* Check for carrier-level issues
* Verify campaign status with T-Mobile
* Manually trigger reactivation if needed
* Review your account for billing or compliance issues

---

Important Notes

Why This Matters

* Avoid Carrier Fines: T-Mobile charges fees for inactive campaigns
* Maintain Compliance: Dormant campaigns may impact your sender reputation
* Cost Management: Suspended campaigns help you avoid unnecessary charges

Billing Impact

* Suspended campaigns may affect your monthly billing
* Review your campaign costs regularly
* Deactivate campaigns you no longer need instead of leaving them inactive

Campaign Monitoring

We recommend:

* Setting up webhook notifications for all campaigns
* Regularly reviewing campaign activity (at least weekly)
* Keeping documentation of which campaigns are actively in use

---

Frequently Asked Questions

Q: How often does the system check for inactive campaigns? A: The system runs daily to identify and suspend inactive campaigns.

Q: Will I receive a warning before suspension? A: If you have webhooks configured,  
 you'll receive a notification when suspension occurs. We recommend monitoring your campaigns regularly.

Q: Can I prevent my campaign from being suspended? A: Yes, keep at least one active phone number assigned to your campaign.

Q: Is there a fee to reactivate a suspended campaign? A: No, reactivation is free.  
 However, leaving campaigns dormant may result in carrier fees.

Q: What happens to my messages during suspension? A: Messages sent from a suspended  
 campaign may be blocked or rejected by carriers.

Q: How long does reactivation take? A: Typically 1-5 minutes after reassigning phone  
 numbers.

---

Support

For additional assistance, please contact:

* Telnyx Support Portal: [Telnyx Help Center](https://support.telnyx.com/)
* Email: [support@telnyx.com](mailto:support@telnyx.com)
* If you are unsure if the campaign was ever approved please reach out to [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com).

---

Related Articles

[10DLC Shared Campaigns](https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns)[How to assign a number to a campaign](https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign)[10DLC Campaign Approval Best Practices](https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices)[10DLC Number Assignment Status](https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status)[10DLC Mock Brands and Campaigns](https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns)

Did this answer your question?

😞😐😃

Table of contents
