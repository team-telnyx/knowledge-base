---
title: 10DLC Onboarding and Phone Number Assignment
summary: Comprehensive guide to registering brands, vetting, creating campaigns, and
  assigning phone numbers for 10DLC A2P messaging on Telnyx — covering both direct
  customer and ISV/reseller architectures, plus bulk operations, webhooks, appeals,
  and troubleshooting.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/isv-reseller-onboarding
- url: https://developers.telnyx.com/docs/messaging/10dlc/phone-number-assignment
- url: https://developers.telnyx.com/docs/messaging/10dlc/quickstart/index
updated_at: 2026-08-05T13:48:57Z
---

# 10DLC Onboarding and Phone Number Assignment

*Part 5 of 5 — see also: [Part 1](10dlc-onboarding-and-phone-number-assignment--part-1.md), [Part 2](10dlc-onboarding-and-phone-number-assignment--part-2.md), [Part 3](10dlc-onboarding-and-phone-number-assignment--part-3.md), [Part 4](10dlc-onboarding-and-phone-number-assignment--part-4.md)*

Comprehensive guide to registering brands, vetting, creating campaigns, and assigning phone numbers for 10DLC A2P messaging on Telnyx — covering both direct customer and ISV/reseller architectures, plus bulk operations, webhooks, appeals, and troubleshooting.

## Troubleshooting

### Brand registration rejected

Common causes:
- **EIN mismatch:** The EIN must match the legal business name exactly as registered with the IRS.
- **Invalid address:** Use the physical business address, not a P.O. box.
- **Missing website:** A working website is strongly recommended for higher vetting scores.

**Fix:** Correct the information and resubmit. Brand registration is free to retry. See the [10DLC Troubleshooting Guide](10dlc-troubleshooting-guide.md) for detailed brand failure resolution steps.

### Low vetting score

Vetting scores depend on business age and size, online presence and reputation, EIN verification, and industry vertical.

**Options:**
- Request **Enhanced Vetting** for a more thorough review (may improve score).
- Ensure your website is live, professional, and matches your brand information.
- Check that your EIN and business name match IRS records exactly.

See [10DLC Rate Limits](10dlc-rate-limits.md) for how scores map to throughput.

### Campaign rejected by carrier

Carriers may reject campaigns for vague or misleading sample messages, missing opt-out language in samples, use case that doesn't match message content, or prohibited content (cannabis, gambling in some states, etc.).

**Fix:** Review and update your sample messages, ensure opt-out language is included, and verify your use case is accurate.

### Campaign sharing shows PENDING for days

**Cause:** Telnyx hasn't processed the sharing request yet, or there's a data mismatch.

**Fix:**
1. Verify the campaign is fully approved at your upstream CSP.
2. Confirm you shared to the correct downstream CSP (Telnyx's TCR ID).
3. Contact [Telnyx support](https://support.telnyx.com) with the TCR Campaign ID.

### Cannot assign numbers to shared campaign

**Cause:** Campaign sharing hasn't been accepted, or numbers aren't 10DLC-eligible.

**Fix:**
1. Check sharing status — must be `ACCEPTED`.
2. Verify numbers are long codes (not toll-free or short codes).
3. Ensure numbers aren't already assigned to another campaign.
4. Check that numbers are on the same Telnyx account.

### Number not found

**Cause:** The phone number isn't on your Telnyx account or isn't in E.164 format.

**Fix:**
- Verify the number is in your account: `GET /v2/phone_numbers?filter[phone_number]=+15551234567`.
- Ensure E.164 format: `+1` followed by 10 digits (e.g., `+15551234567`).

### Number not assigned to a messaging profile

**Cause:** Numbers must be assigned to a messaging profile before campaign assignment.

**Fix:**

```bash
curl -X PATCH https://api.telnyx.com/v2/phone_numbers/+15551234567 \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"messaging_profile_id": "PROFILE_ID"}'
```

### Campaign not active

**Cause:** The campaign hasn't been approved by carriers yet.

**Fix:**
- Check campaign status: `GET /v2/10dlc/campaignBuilder/{campaignId}`.
- Wait for carrier approval (1–5 business days).
- Set up [Event Notifications](10dlc-event-notifications.md) to get notified when the campaign is approved.

### Number already assigned to another campaign

**Cause:** Each number can only be assigned to one campaign at a time.

**Fix:**
1. Remove the number from the current campaign: `DELETE /v2/10dlc/phoneNumberCampaign/+15551234567`.
2. Assign it to the new campaign.

### Messages failing with 40002 (spam) on shared campaign

**Cause:** Message content doesn't match registered campaign samples, or throughput exceeds campaign limits.

**Fix:**
1. Compare actual message content against registered samples.
2. Check [10DLC Rate Limits](10dlc-rate-limits.md) for your vetting score.
3. Ensure opt-out keywords (STOP, etc.) are properly handled.
4. Review the [error code reference](message-error-codes.md) for specific guidance.

### Messages still being filtered after assignment

**Cause:** Carrier provisioning takes time after assignment.

**Fix:**
- Wait 24–72 hours for all carriers to propagate.
- Check MNO metadata on the campaign for per-carrier status.
- Verify the number is sending the same type of content registered in the campaign.
- Check [Message Detail Records](message-detail-records.md) for specific error codes.

### Messages still being filtered after registration

Even with 10DLC registration, messages can be filtered if content doesn't match the registered campaign use case, messages look like spam (identical content to many recipients), links are flagged by carrier content filters, or volume exceeds your campaign's throughput allocation.

**Fix:** Ensure message content matches your campaign description. Personalize messages. Use link shorteners carefully. Monitor [Message Detail Records](message-detail-records.md) for delivery issues.

### Bulk assignment partially failing

**Cause:** Some numbers may have issues while others succeed.

**Fix:**
- Check each error response for the specific reason.
- Common issues: number on different account, already assigned, not on messaging profile.
- Use the bulk assignment script above with error tracking to identify which numbers failed and why.

### Customer wants to switch from shared to dedicated campaign

1. Register a new brand for the customer (if not already done).
2. Submit brand for vetting.
3. Create a new campaign under their brand.
4. Wait for campaign approval.
5. Reassign their phone numbers from the shared campaign to the new dedicated campaign.
6. Traffic switches immediately — no downtime required.

## Next steps

- [10DLC Rate Limits](10dlc-rate-limits.md) — Understand throughput by vetting score and carrier.
- [10DLC Event Notifications](10dlc-event-notifications.md) — Set up webhooks for brand and campaign status changes.
- [Campaign Registration](campaign-registration.md) — Details on campaign use cases and requirements.
- [Partner Campaigns API](partner-campaigns-api.md) — Full API reference for shared campaign management.
- [Number Pool](number-pool.md) — Distribute sending across multiple numbers automatically.
- [Send Message](send-message.md) — Start sending once numbers are assigned and provisioned.
- [Sole Proprietor](sole-proprietor.md) — Special 10DLC registration for sole proprietors without an EIN.
