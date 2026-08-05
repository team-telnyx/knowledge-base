---
title: 10DLC Campaign Use Cases and Event Notifications
summary: Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages,
  opt-in/opt-out requirements, and webhook event notifications for brands, campaigns,
  and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases
- url: https://developers.telnyx.com/docs/messaging/10dlc/event-notifications/index
updated_at: 2026-08-05T13:49:31Z
---

# 10DLC Campaign Use Cases and Event Notifications

*Part 6 of 8 — see also: [Part 1](10dlc-campaign-use-cases-and-event-notifications--part-1.md), [Part 2](10dlc-campaign-use-cases-and-event-notifications--part-2.md), [Part 3](10dlc-campaign-use-cases-and-event-notifications--part-3.md), [Part 4](10dlc-campaign-use-cases-and-event-notifications--part-4.md), [Part 5](10dlc-campaign-use-cases-and-event-notifications--part-5.md), [Part 7](10dlc-campaign-use-cases-and-event-notifications--part-7.md), [Part 8](10dlc-campaign-use-cases-and-event-notifications--part-8.md)*

Comprehensive guide to Telnyx 10DLC campaign use cases, sample messages, opt-in/opt-out requirements, and webhook event notifications for brands, campaigns, and phone numbers. Includes SDK examples, retry policies, and campaign appeal mechanisms.

## Campaign Appeals and Nudging Mechanisms

When campaigns are rejected, there are different flows for getting them back into the compliance review queue depending on the campaign type and rejection reason.

### Native Campaign Appeals

For **native campaigns** rejected due to external factors (e.g., website compliance issues), customers can use the campaign appeal endpoint after addressing the issues:

```
curl -X POST 'https://api.telnyx.com/10dlc/campaign/{campaignId}/appeal' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "appealReason": "The website has been updated to include the required privacy policy and terms of service."
  }'
```

This will update the campaign status from `TELNYX_FAILED` to `TCR_ACCEPTED` and re-enter the compliance review queue.

### Partner Campaign Nudging

For **partner campaigns**, the appeal process involves the CSP (Campaign Service Provider) sending a `CAMPAIGN_NUDGE` event after reviewing and approving customer changes:

```json
{
  "data": {
    "event_type": "10dlc.campaign.update",
    "id": "example-event-id",
    "occurred_at": "2025-07-30T11:07:51.259711+00:00",
    "payload": {
      "campaignId": "C4D06C2F",
      "type": "CAMPAIGN_NUDGE",
      "nudgeIntent": "APPEAL_REJECTION",
      "description": "The campaign has been reviewed and approved after appeal.",
      "cspId": "TNX"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://your-webhook-url.com"
  }
}
```

> **Note:** `CAMPAIGN_NUDGE` events originate from TCR and use the TCR campaign ID format (e.g., `C4D06C2F`) in the `campaignId` field, unlike other campaign webhooks which use the Telnyx UUID.

### Campaign Appeal Scenarios

**1. Native Campaign Rejected for Content Issues** — When a customer submits a native campaign and Telnyx rejects it due to issues with the campaign content (e.g., unclear sample messages), the customer can make adjustments to their campaign. Using the campaign update endpoint will automatically reset the campaign's status to `TCR_ACCEPTED` so it goes back into the compliance team's review queue.

**2. Native Campaign Rejected for External Factors** — When a customer submits a native campaign and Telnyx rejects it due to factors outside the campaign object (e.g., website compliance requirements), the customer must:

- Fix the external issues (e.g., update website with required privacy policy).
- Use the appeal API endpoint to get their campaign back in the review queue.

**3. Partner Campaign Rejected (Any Reason)** — For partner campaigns rejected for either content issues or external factors, the process involves the CSP:

- Customer makes required adjustments based on rejection reasons.
- CSP reviews the changes and approves them.
- CSP forwards a `CAMPAIGN_NUDGE` event to Telnyx.
- Campaign status changes from `TELNYX_FAILED` to `TCR_ACCEPTED` and re-enters compliance review.

This nudging mechanism for partner campaigns cannot work with native campaigns.

**4. DCA Rejection for External Factors** — When Telnyx accepts a campaign but the Direct Connect Aggregator (DCA) rejects it due to external factors:

- Customer makes required external changes (e.g., website updates).
- Customer notifies Telnyx via appropriate appeal mechanism (scenarios 2 or 3).
- Once Telnyx approves the changes, Telnyx generates a nudge webhook that the DCA receives.
- Campaign re-enters DCA review queue.

**5. DCA Rejection for Content Issues** — When the DCA rejects a campaign due to campaign content issues:

- Customer updates campaign content (e.g., sample messages).
- Customer notifies Telnyx via appropriate appeal mechanism (scenarios 1 or 3).
- Once Telnyx approves the changes, Telnyx generates a nudge webhook that the DCA receives.
- Campaign re-enters DCA review queue.

### Campaign Status Flow

**Success path statuses:**

| Status | Description |
| --- | --- |
| `TCR_PENDING` | Campaign is pending review at The Campaign Registry (TCR). |
| `TCR_ACCEPTED` | Campaign has been accepted by TCR and is ready for Telnyx/MNO review. |
| `MNO_PENDING` | Campaign is pending provisioning with Mobile Network Operators (MNOs). |
| `MNO_PROVISIONED` | Campaign has been successfully provisioned with all MNOs. |

**Failure and suspension statuses:**

| Status | Description |
| --- | --- |
| `TCR_FAILED` | Campaign was rejected by TCR during initial registration. |
| `TELNYX_FAILED` | Campaign was rejected by Telnyx compliance review. Can be appealed. |
| `MNO_REJECTED` | Campaign was rejected by one or more MNOs. Can be appealed. |
| `TCR_SUSPENDED` | Campaign has been suspended due to compliance issues. |
| `TCR_EXPIRED` | Campaign has expired and is no longer active. |

### Campaign Appeal Status Flow

The typical status flow for campaign appeals is:

1. **Initial rejection**: Campaign status becomes `TELNYX_FAILED`.
2. **Customer action**: Customer addresses the rejection reasons.
3. **Appeal submission**:
   - Native campaigns: Use appeal API endpoint or campaign update.
   - Partner campaigns: CSP sends `CAMPAIGN_NUDGE`.
4. **Re-review**: Campaign status changes to `TCR_ACCEPTED` and re-enters compliance review.

The nudging mechanism for partner campaigns cannot be used with native campaigns. Native campaigns must use the direct appeal API endpoint or campaign update functionality.
