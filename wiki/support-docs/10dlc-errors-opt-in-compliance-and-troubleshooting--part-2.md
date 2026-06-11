---
title: 10DLC Errors, Opt-In Compliance, and Troubleshooting
summary: A practical guide to avoiding 10DLC campaign declines, documenting compliant
  opt-in flows, verifying brands, resolving number assignment problems, and reactivating
  suspended campaigns on Telnyx.
sources:
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
- url: https://support.telnyx.com/en/articles/10715184-10dlc-unverified-brand
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
updated_at: 2026-05-20T14:08:45Z
---

# 10DLC Errors, Opt-In Compliance, and Troubleshooting

*Part 2 of 2 — see also: [Part 1](10dlc-errors-opt-in-compliance-and-troubleshooting--part-1.md)*

A practical guide to avoiding 10DLC campaign declines, documenting compliant opt-in flows, verifying brands, resolving number assignment problems, and reactivating suspended campaigns on Telnyx.

## Reactivating suspended campaigns (TCR_SUSPENDED/DORMANT)
Telnyx automatically suspends inactive T-Mobile–deployed campaigns to help you avoid T‑Mobile’s dormant‑campaign fines.
- Suspension triggers: 15 consecutive days of no activity, no active numbers assigned, and deployed with T‑Mobile.
- Reactivation steps:
  1) Assign a phone number to the campaign; the first attempt usually reactivates the campaign but fails assignment.
  2) Assign the number again after 1–2 minutes; assignment should succeed and status returns to active.
- Prevent suspension: Keep at least one active number assigned, monitor usage, configure webhooks, and send periodic traffic if a campaign will be quiet.
- Webhooks: Configure a campaign webhook via API to receive a dormant/suspended notification when triggered: Update Campaign (Telnyx Portal/API) https://developers.telnyx.com/api/messaging/10dlc/update-campaign or Update Shared Campaign https://developers.telnyx.com/api/messaging/10dlc/update-shared-campaign
- Troubleshooting: If reassigning twice doesn’t work, wait through automatic retries (1m → 10m → 1h), then try removing all numbers, wait 2–3 minutes, and re‑add. If still stuck, contact support (see below).

## Number assignment timelines and status checks
- Assignment can take minutes to a few days; ~2 hours is typical. Don’t send traffic until assignment is complete.
- Check status via API: https://developers.telnyx.com/api/messaging/10dlc/get-all-phone-number-campaigns
  - Status ASSIGNED indicates completion.
  - If undelivered messages occurred, compare their timestamps to the assignment’s last‑updated time—messages sent before completion commonly fail.
- If issues persist after ASSIGNED status, contact support.

## When DID assignment fails outright
If assigning a DID to a 10DLC campaign fails, email 10dlcquestions@telnyx.com with your Telnyx account email, campaign IDs (Telnyx and TCR if available), and any error messages.

## Support and useful APIs
- Create phone number–campaign assignment: https://developers.telnyx.com/api/messaging/10dlc/create-phone-number-campaign
- Update campaign (webhook configuration, etc.): https://developers.telnyx.com/api/messaging/10dlc/update-campaign
- Update shared campaign: https://developers.telnyx.com/api/messaging/10dlc/update-shared-campaign
- Check number–campaign assignments: https://developers.telnyx.com/api/messaging/10dlc/get-all-phone-number-campaigns
- Telnyx Support: support@telnyx.com
- 10DLC questions/escalations: 10dlcquestions@telnyx.com
