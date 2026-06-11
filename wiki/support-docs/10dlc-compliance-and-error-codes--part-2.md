---
title: 10DLC Compliance and Error Codes
summary: A comprehensive reference for 10DLC campaign compliance, covering carrier
  error codes and their resolutions, required keywords and confirmation messages,
  privacy policy verbiage, brand verification requirements, campaign suspension for
  inactivity, and SMS porting considerations for ported-in phone numbers.
sources:
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
  content_hash: 9b6044d0b967707a06966ae9c750424519d3d24b6d0118951e910d3ae8f1afb7
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
  content_hash: 517aa55bed935632cdb945d6eef7257cf50aa3e98ea893be02332ddfbddd55c8
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
  content_hash: d42dcbd08bb330e0aa10504286cf75d33dcd7460d03daf8b7b267d00291933e2
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
  content_hash: c58866e0f474718c88333b11758004e24d0a2a29cbe655c05b629857b4914695
- url: https://support.telnyx.com/en/articles/10715184-10dlc-unverified-brand
  content_hash: f20137527fe8638e63a766e07a8ad4c54c633ca3245a0cf011db94ca1d6e4dcc
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
  content_hash: 37dc405587bd56e3e374454fbad57992200523b656a9c987ad3e34d2ee3999d9
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
  content_hash: df854549a7915277c5db4ee826ccd16ccb0ccdd7353f26fa06513efe8a2fc298
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
  content_hash: 0dc27d88780519b11066b2c9a4588a820a35121dafa4b43726b72789af48e692
updated_at: 2026-06-11T11:10:54Z
---

# 10DLC Compliance and Error Codes

*Part 2 of 3 — see also: [Part 1](10dlc-compliance-and-error-codes--part-1.md), [Part 3](10dlc-compliance-and-error-codes--part-3.md)*

A comprehensive reference for 10DLC campaign compliance, covering carrier error codes and their resolutions, required keywords and confirmation messages, privacy policy verbiage, brand verification requirements, campaign suspension for inactivity, and SMS porting considerations for ported-in phone numbers.

## Keywords and Confirmation Messages

Under 10DLC guidelines, all campaigns must specify keywords and confirmation messages for opt-in, opt-out, and help. Use the following templates, replacing variables with your brand and campaign details:

**Opt-in**
- Keyword: `START` or similar
- Confirmation message: `[Brand name]: Thanks for subscribing to [use case(s)]! Reply HELP for help. Message frequency may vary. Msg&data rates may apply. Consent is not a condition of purchase. Reply STOP to opt out.`

**Opt-out**
- Keyword: `STOP` or similar
- Confirmation message: `[Brand Name]: You are unsubscribed and will receive no further messages.`

**Help**
- Keyword: `HELP` or similar
- Confirmation message: `[Brand name]: Please reach out to us at [website/email/phone number] for help.`

Websites are permissible in help messages so long as they have clear contact information at the link provided.

## Privacy Policy Requirements

The privacy policy must be for the brand being registered — a reseller cannot substitute their own policy in lieu of the brand's, and Google's Privacy Policy will not be accepted.

Carriers look for verbiage either in the privacy policy (linked on the opt-in form) or directly on the opt-in form itself. The bare minimum accepted by carriers is:

> Your mobile information will not be sold or shared with third parties for promotional or marketing purposes.

A more robust, preferred version is:

> All the above categories exclude text messaging originator opt-in data and consent; this information will not be shared with any third parties.

> We will not share your opt-in to an SMS campaign with any third party for purposes unrelated to providing you with the services of that campaign. We may share your Personal Data, including your SMS opt-in or consent status, with third parties that help us provide our messaging services, including but not limited to platform providers, phone companies, and any other vendors who assist us in the delivery of text messages.

The verbiage must cover any method of transfer. If it only states that mobile data will not be **sold**, that is insufficient — it must also cover **sharing**, which could include transfers without a sale (e.g., between affiliates or friendly businesses), which is prohibited under 10DLC.

## Brand Verification

A brand is always unverified for the same reason: the legal company name, address, or EIN has been entered differently than the IRS has it (for US brands). To correct this, you need the IRS Form CP-575 (EIN Confirmation Letter). Even small discrepancies — such as entering "Street" instead of "St." — can cause a brand to remain permanently "Unverified."

**Important:** On the IRS EIN letter, the first contact name is the legal company name and the second is the DBA. Match the address and EIN exactly as they appear on the EIN letter.

### Canadian Brands

Provide your Canadian Business Number (BN) issued by the CRA. Enter only the first 9 numeric digits (e.g., from `123456789RM0001`, enter `123456789`). Ensure your legal company name is consistent with your corporation registration and properly spelled. The address should match what was used in registering with Corporations Canada. Free resources for checking details include [Canada's Business Registries](https://beta.canadasbusinessregistries.ca/search) and the [Innovation, Science and Economic Development Canada corporation search](https://ised-isde.canada.ca/cc/lgcy/fdrlCrpSrch.html).

### Non-US/Canada Brands

Enter the numeric portion of your VAT ID number. Automated VAT identification matching is currently optimized for: Croatia, Hungary, Ireland, Italy, Lithuania, Luxembourg, Latvia, Malta, Netherlands, Norway, Poland, Portugal, Romania, Sweden, Slovenia, Slovakia, Northern Ireland, United Arab Emirates, Australia, Belarus, Iceland, Malaysia, New Zealand, Saudi Arabia, Singapore, and Taiwan. If your country is not on this list, provide the primary corporation registration number or Tax ID number and note the country of issuance.

### Publicly Traded Brands

A publicly traded brand must complete a 2FA email from Aegis using an email domain that matches the website and that is not a group alias (it must go to an individual's email). For brands verified before this rule took effect (Q4 2024), the 2FA email must be completed before any new campaign can be created.

## Campaign Suspension for Inactivity

Telnyx proactively suspends inactive 10DLC campaigns to protect customers from T-Mobile's $250/month fine for dormant campaigns.

### Suspension Triggers

A campaign is automatically suspended when **all** of the following conditions are met:

- No activity for 15 consecutive days
- No active phone numbers assigned to the campaign
- Campaign is currently deployed with T-Mobile

### Webhook Notifications

To receive real-time alerts when a campaign is suspended, configure a webhook URL in your campaign settings:

- **Campaigns created in the Telnyx Portal or API:** Use the [Update Campaign API](https://developers.telnyx.com/api/messaging/10dlc/update-campaign) or set the webhook field on the campaign's portal page.
- **Campaigns created in the TCR Portal or API:** Use the [Update Single Shared Campaign API](https://developers.telnyx.com/api/messaging/10dlc/update-shared-campaign).

The webhook payload looks like:

```json
{
  "campaignId": "your-campaign-id",
  "type": "TELNYX_EVENT",
  "status": "DORMANT",
  "description": "Campaign has been marked as dormant"
}
```

### Preventing Suspension

1. Keep at least one active phone number assigned (with T-Mobile)
2. Monitor usage and regularly review campaign activity
3. Set up webhook notifications for real-time alerts
4. If a campaign will be inactive, consider sending traffic periodically

### Reactivating a Suspended Campaign

1. **Assign phone numbers** — Add or reassign phone numbers to the suspended campaign using the [Create New Phone Number Campaign API](https://developers.telnyx.com/api/messaging/10dlc/create-phone-number-campaign) or the Mission Control Portal.
2. **Resume the campaign** — The system will automatically attempt to resume when numbers are assigned. Allow 1–2 minutes for processing. The first number assignment will fail but should unsuspend the campaign; the second assignment should succeed.
3. **Verify activation** — Check that the status has changed from `TCR_SUSPENDED` back to active, then confirm number assignment is successful.

### Troubleshooting Reactivation

If standard reactivation doesn't work:

- **Wait and retry:** The system uses automatic retry intervals (1 minute → 10 minutes → 1 hour). Wait for the full cycle before retrying.
- **Manual process:** Remove all phone numbers from the campaign, wait 2–3 minutes, then re-add them and monitor for the confirmation webhook.
- **Contact support:** Email [support@telnyx.com](mailto:support@telnyx.com) with the Campaign ID, TCR Campaign ID, timestamp of reactivation attempt, and any error messages. If unsure whether a campaign was ever approved, contact [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com).

During suspension, messages sent from the campaign may be blocked or rejected by carriers. Reactivation is free, but leaving campaigns dormant may result in carrier fees.
