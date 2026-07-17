---
title: 10DLC and Messaging Compliance Reference
summary: This page consolidates Telnyx 10DLC and messaging compliance guidance, including
  carrier error codes for campaign declines, suspension and reactivation procedures,
  sole proprietor registration, shared campaign imports, toll-free verification requirements,
  and the full catalog of Telnyx messaging error codes.
sources:
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
- url: https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
updated_at: 2026-07-17T09:00:38Z
---

# 10DLC and Messaging Compliance Reference

*Part 2 of 7 — see also: [Part 1](10dlc-and-messaging-compliance-reference--part-1.md), [Part 3](10dlc-and-messaging-compliance-reference--part-3.md), [Part 4](10dlc-and-messaging-compliance-reference--part-4.md), [Part 5](10dlc-and-messaging-compliance-reference--part-5.md), [Part 6](10dlc-and-messaging-compliance-reference--part-6.md), [Part 7](10dlc-and-messaging-compliance-reference--part-7.md)*

This page consolidates Telnyx 10DLC and messaging compliance guidance, including carrier error codes for campaign declines, suspension and reactivation procedures, sole proprietor registration, shared campaign imports, toll-free verification requirements, and the full catalog of Telnyx messaging error codes.

## 10DLC Campaign Suspension

If your campaign has a TCR status of "Suspended," it normally means it is dormant from inactivity. Telnyx proactively puts campaigns in a suspended state to prevent T-Mobile from charging a $250 per month fine for campaigns they deem inactive.

### Automatic Suspension Triggers

Your 10DLC campaign will be automatically suspended if all of these conditions are met:

- No activity for 15 consecutive days
- No active phone numbers assigned to the campaign
- Campaign is currently deployed with T-Mobile

This is a protective measure to prevent carrier fines for dormant campaigns.

### Webhook Notifications

You can enable a webhook event when there is a suspension:

- For campaigns created in the Telnyx Portal or API, use the [Update My Campaign API](https://developers.telnyx.com/api/messaging/10dlc/update-campaign) or update the webhook field in the campaign's page in the portal.
- For campaigns created in the TCR Portal or API, use the [Update Single Shared Campaign API](https://developers.telnyx.com/api/messaging/10dlc/update-shared-campaign).

When your campaign is suspended due to inactivity, you will receive a webhook notification (if configured) with the following information:

```
{ "campaignId": "your-campaign-id", "type": "TELNYX_EVENT", "status": "DORMANT", "description": "Campaign has been marked as dormant" }
```

When you receive this notification, you should immediately take steps to reactivate your campaign.

### Preventing Suspension

- Keep phone numbers assigned (numbers should be added with T-Mobile) — maintain at least one active phone number on your campaign.
- Monitor usage — regularly review your campaign activity.
- Set up webhooks — configure webhook URLs in your campaign settings to receive real-time alerts.
- Plan ahead — if you know a campaign will be inactive, consider sending some traffic periodically.

### Reactivating a Suspended Campaign

1. **Assign Phone Numbers:** Add or reassign phone numbers to your suspended campaign using the [Create New Phone Number Campaign API](https://developers.telnyx.com/api/messaging/10dlc/create-phone-number-campaign) or Mission Control Portal.
2. **Resume the Campaign:** The system will automatically attempt to resume your campaign when you assign numbers. Allow 1–2 minutes for processing. The first number assignment will fail but should unsuspend the campaign.
3. **Verify Activation:** Check your campaign status via the API or Mission Control Portal. Status should change from `TCR_SUSPENDED` back to active. Once the campaign is active you should be able to assign numbers now so that a suspension does not happen again.

### Troubleshooting Reactivation

If standard reactivation doesn't work, try these steps:

- **Wait and Retry:** The system uses automatic retry intervals of 1 minute → 10 minutes → 1 hour. Wait for the full retry cycle before attempting again.
- **Manual Process:** Remove all phone numbers from the campaign, wait 2–3 minutes, re-add phone numbers to the campaign, and monitor for confirmation webhook.
- **Contact Support:** If the above steps don't work, contact [Support@telnyx.com](mailto:Support@telnyx.com) with your campaign ID, TCR Campaign ID (if available), timestamp of when you attempted reactivation, and any error messages received. Support can check for carrier-level issues, verify campaign status with T-Mobile, manually trigger reactivation if needed, and review your account for billing or compliance issues.

### Frequently Asked Questions

- **How often does the system check for inactive campaigns?** The system runs daily to identify and suspend inactive campaigns.
- **Will I receive a warning before suspension?** If you have webhooks configured, you'll receive a notification when suspension occurs. We recommend monitoring your campaigns regularly.
- **Can I prevent my campaign from being suspended?** Yes, keep at least one active phone number assigned to your campaign.
- **Is there a fee to reactivate a suspended campaign?** No, reactivation is free. However, leaving campaigns dormant may result in carrier fees.
- **What happens to my messages during suspension?** Messages sent from a suspended campaign may be blocked or rejected by carriers.
- **How long does reactivation take?** Typically 1–5 minutes after reassigning phone numbers.

## 10DLC Authentication for Publicly Traded Brands

If you do not complete the Auth Plus process for Publicly Traded brands, no new campaigns will be able to be created for existing or new Publicly Traded brands. After the August 1, 2025 deadline, you can still complete the Auth Plus process, but there will be a $12.50 fee for doing so, whereas it is currently a free process.

To get the brand authenticated, reply to [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) with the business contact email address and the brand ID. The business contact email should share a domain with the brand website and be for an individual. Once you provide a business contact email, Telnyx will trigger the authentication. The contact will be sent a 2FA email containing a Verification PIN and a link. When the brand contact clicks on the link, they will be directed to a site and be prompted to enter:

- Brand Contact First Name
- Brand Contact Last Name
- Brand Contact Job Title
- Verification PIN from the 2FA email

Once they submit this information, the brand will be authenticated. The email will be from [noreply@auth.campaignregistry.com](mailto:noreply@auth.campaignregistry.com), TCR (local US text messaging regulator). The contact will have 7 days from the time they receive the 2FA email to complete the authentication. Should they fail to do so, the 2FA email will need to be resent. This is required by The Campaign Registry (TCR) in order to ensure that no service disruption occurs for this brand.
