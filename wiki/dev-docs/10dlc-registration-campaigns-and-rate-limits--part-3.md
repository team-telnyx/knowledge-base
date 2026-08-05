---
title: 10DLC Registration, Campaigns, and Rate Limits
summary: A consolidated reference for registering a 10DLC brand and campaign with
  The Campaign Registry (TCR) through Telnyx, submitting for external vetting, and
  understanding how the resulting vetting score controls carrier throughput on AT&T,
  T-Mobile, and Verizon.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/10dlc-rate-limits/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/brand-registration/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-registration/index
updated_at: 2026-08-05T13:48:40Z
---

# 10DLC Registration, Campaigns, and Rate Limits

*Part 3 of 4 — see also: [Part 1](10dlc-registration-campaigns-and-rate-limits--part-1.md), [Part 2](10dlc-registration-campaigns-and-rate-limits--part-2.md), [Part 4](10dlc-registration-campaigns-and-rate-limits--part-4.md)*

A consolidated reference for registering a 10DLC brand and campaign with The Campaign Registry (TCR) through Telnyx, submitting for external vetting, and understanding how the resulting vetting score controls carrier throughput on AT&T, T-Mobile, and Verizon.

## Writing sample messages that pass review

Carriers manually review your sample messages. Poorly written samples are the #1 reason campaigns get rejected.

**Do: Include opt-out language**

Every sample should include opt-out instructions:
> "Your order #12345 has shipped! Track at <https://acme.com/track/12345>. Reply STOP to unsubscribe."

**Do: Make samples realistic and specific**

Use real-looking content with your actual brand name:
> "Hi Sarah, your Acme Corp appointment is confirmed for Tuesday at 2 PM. Reply YES to confirm or HELP for assistance."

**Do: Match samples to your use case**

If your use case is `DELIVERY_NOTIFICATION`, all samples should be about deliveries:
> ✅ "Your package has shipped via FedEx. Tracking: 1Z999AA10123456784"
> ❌ "Check out our summer sale! 30% off everything!" (This is marketing, not delivery)

**Don't: Use generic placeholder text**

Carriers reject vague samples:
> ❌ "This is a test message"
> ❌ "Hello, this is a message from our company"

**Don't: Include prohibited content**

Carriers prohibit or restrict:

- Cannabis / CBD messaging
- Gambling content (varies by state)
- Firearms sales
- Payday lending
- Content targeting minors without age gate

**Do: Describe your opt-in flow clearly**

The `messageFlow` field should explain exactly how users consent:
> "Users sign up on our website at <https://acme.com/signup> where they enter their phone number and check a box that reads: 'I agree to receive order updates via SMS from Acme Corp. Msg frequency varies. Msg & data rates may apply. Reply STOP to cancel.'"

## MNO provisioning timeline

After TCR approves your campaign, each carrier (MNO) provisions it on their network independently. This affects when you can send messages on each carrier.

| Carrier | Typical Timeline | Notes |
| --- | --- | --- |
| **T-Mobile** | Instant to 24 hours | Usually the fastest |
| **AT&T** | 1-3 business days | May require additional review for some use cases |
| **Verizon** | 1-3 business days | — |
| **US Cellular** | 3-5 business days | Smaller carrier, longer provisioning |

You can check provisioning status per carrier via the API:

```bash
curl -s https://api.telnyx.com/v2/10dlc/campaignBuilder/{campaignId} \
  -H "Authorization: Bearer YOUR_API_KEY" | jq '.data.mnoMetadata'
```

## Check campaign status

```bash
curl -s https://api.telnyx.com/v2/10dlc/campaignBuilder/{campaignId} \
  -H "Authorization: Bearer YOUR_API_KEY" | jq '{
    status: .data.status,
    usecase: .data.usecase,
    brandId: .data.brandId,
    createDate: .data.createDate
  }'
```

**Campaign statuses**

| Status | Meaning |
| --- | --- |
| `ACTIVE` | Approved and ready to send |
| `EXPIRED` | Campaign expired (renew required) |
| `SUSPENDED` | Suspended by carrier — contact support |

## List all campaigns

```bash
curl -s https://api.telnyx.com/v2/10dlc/campaignBuilder \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -G -d "page[size]=20"
```

## Handle campaign rejections

Campaigns can be rejected during carrier review. Common reasons and how to fix them:

| Rejection Reason | Fix |
| --- | --- |
| **Samples don't match use case** | Rewrite samples to match your declared use case exactly |
| **Missing opt-out language** | Add "Reply STOP to unsubscribe" to every sample |
| **Vague message flow** | Describe the exact opt-in mechanism (website form, checkout checkbox, etc.) |
| **Prohibited content** | Remove restricted content (cannabis, gambling, etc.) |
| **Brand not vetted** | Complete brand vetting before resubmitting |

### Resubmitting a rejected campaign

You cannot edit a rejected campaign. Instead, create a new campaign with corrected information:

1. Review the rejection reason (check [Event Notifications](event-notifications.md) webhooks)
2. Fix the identified issues in your samples and description
3. Create a new campaign via the API or Portal
4. Reassign your phone numbers to the new campaign

Each campaign submission incurs a TCR registration fee. Review your samples carefully before submitting to avoid repeated rejections and fees.

## Campaign compliance best practices

1. **Match content to use case** — Only send messages that match your registered campaign use case. Sending marketing from a `CUSTOMER_CARE` campaign risks suspension.
2. **Honor opt-outs immediately** — Process STOP requests within seconds. Carriers monitor compliance.
3. **Keep records** — Maintain proof of consent (opt-in records with timestamp, source, and phone number). Carriers may request this during audits.
4. **Monitor throughput** — Don't exceed your campaign's allocated throughput. Check [#Rate limits and throughput](rate-limits-and-throughput.md) for your brand score tier.
5. **Review Event Notifications** — Set up webhooks for 10DLC events to catch approval, rejection, and suspension events in real time.
