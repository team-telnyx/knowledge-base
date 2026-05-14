---
title: '10DLC carrier errors, brand verification issues, and campaign suspension:
  causes and fixes'
summary: A practical guide to understanding common 10DLC carrier error codes, fixing
  inconsistent registrations (602/603), correcting CTA and opt‑in compliance failures
  (806 and related), resolving unverified brand problems, and handling TCR campaign
  suspensions due to inactivity.
sources:
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
  content_hash: 9b6044d0b967707a06966ae9c750424519d3d24b6d0118951e910d3ae8f1afb7
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
  content_hash: c58866e0f474718c88333b11758004e24d0a2a29cbe655c05b629857b4914695
- url: https://support.telnyx.com/en/articles/10715184-10dlc-unverified-brand
  content_hash: c441fd50d954cbcbbb848403634706b3ae5ede5e8e13232933f485d64c65f595
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
  content_hash: 37dc405587bd56e3e374454fbad57992200523b656a9c987ad3e34d2ee3999d9
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
  content_hash: df854549a7915277c5db4ee826ccd16ccb0ccdd7353f26fa06513efe8a2fc298
updated_at: 2026-05-14T11:22:21Z
---

# 10DLC carrier errors, brand verification issues, and campaign suspension: causes and fixes

*Part 2 of 2 — see also: [Part 1](10dlc-carrier-errors-brand-verification-issues-and-campaign-suspension-causes-and-fixes--part-1.md)*

A practical guide to understanding common 10DLC carrier error codes, fixing inconsistent registrations (602/603), correcting CTA and opt‑in compliance failures (806 and related), resolving unverified brand problems, and handling TCR campaign suspensions due to inactivity.

## Campaign suspended (TCR_SUSPENDED/DORMANT): why it happens and what to do
Telnyx proactively suspends inactive campaigns to help you avoid T‑Mobile’s dormant-campaign fine (currently $250/month).

Suspension triggers (all must be true):
- No activity for 15 consecutive days
- No active phone numbers assigned to the campaign
- Campaign is deployed with T‑Mobile

Webhook notifications:
- Configure a webhook URL on the campaign (via Portal or API) to receive a suspension notice. APIs: Update campaign (https://developers.telnyx.com/api/messaging/10dlc/update-campaign) and Update shared campaign (https://developers.telnyx.com/api/messaging/10dlc/update-shared-campaign).
- Example payload: { "campaignId": "your-campaign-id", "type": "TELNYX_EVENT", "status": "DORMANT", "description": "Campaign has been marked as dormant" }

Prevent suspension:
- Keep at least one active phone number assigned (with T‑Mobile enabled) and send periodic traffic.
- Monitor usage and set up webhooks for real-time alerts.

Reactivate a suspended campaign:
1) Assign phone numbers to the campaign (Portal or API: https://developers.telnyx.com/api/messaging/10dlc/create-phone-number-campaign).
2) Wait 1–2 minutes. The first assignment typically fails but unsuspends the campaign.
3) Assign again; status should return to Active and the assignment should complete.

If reactivation fails:
- Wait for automatic retries (about 1 minute → 10 minutes → 1 hour), then try again.
- Manual approach: remove all numbers, wait 2–3 minutes, re-add, and watch for the webhook.
- Contact support (support@telnyx.com) with your Campaign ID, TCR Campaign ID, timestamps, and any error messages. The team can check carrier status, trigger reactivation, or investigate billing/compliance issues.

Operational notes:
- Messages sent while suspended may be blocked or rejected.
- Review recurring costs; deactivate campaigns you no longer need.

## Quick triage checklist before resubmitting
- Does the brand name, website, address, and tax ID exactly match official records?
- Is the selected use case reflected consistently in description, website/CTA, message flow, and samples?
- Do samples include required elements (and reflect attributes like embedded links/phones)?
- Is the opt-in path specific and documented in the Message Flow field?
- Does the CTA show program/brand name, message frequency, rates disclosure, STOP/HELP, and T&Cs/Privacy Policy links?
- Does the Privacy Policy explicitly state SMS opt-in data is not shared with third parties?
- For age-restricted content, is a working DOB gate implemented?

## Related Telnyx resources
- 10DLC Carrier Error Codes Explanations: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
- 10DLC Inaccurate or Inconsistency Error (602/603): https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
- 10DLC Error 806 guide: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
- Guide to Message Flow field: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- 10DLC Opt-in Form checklist: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- Create/Update campaigns via API: https://developers.telnyx.com/api/messaging/10dlc/update-campaign and https://developers.telnyx.com/api/messaging/10dlc/update-shared-campaign
- Assign numbers to campaigns via API: https://developers.telnyx.com/api/messaging/10dlc/create-phone-number-campaign
