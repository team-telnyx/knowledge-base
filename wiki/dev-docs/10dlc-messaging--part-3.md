---
title: 10DLC Messaging
summary: 10DLC (10-Digit Long Code) is the industry standard for application-to-person
  (A2P) messaging on US long code numbers. Registering your brand and campaigns with
  The Campaign Registry (TCR) through Telnyx provides higher throughput, better deliverability,
  and reduced carrier filtering. Your brand's vetting score directly determines your
  messaging throughput limits across AT&T, T-Mobile, and other carriers.
sources:
- url: https://developers.telnyx.com/docs/messaging/10dlc/10dlc-rate-limits/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/brand-registration/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-registration/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/campaign-use-cases
- url: https://developers.telnyx.com/docs/messaging/10dlc/event-notifications/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/isv-reseller-onboarding
- url: https://developers.telnyx.com/docs/messaging/10dlc/phone-number-assignment
- url: https://developers.telnyx.com/docs/messaging/10dlc/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/sole-proprietor/index
- url: https://developers.telnyx.com/docs/messaging/10dlc/troubleshooting/index
- url: https://developers.telnyx.com/docs/messaging/getting-started/choosing-your-sender-type/index
updated_at: 2026-06-11T10:36:45Z
---

# 10DLC Messaging

*Part 3 of 5 — see also: [Part 1](10dlc-messaging--part-1.md), [Part 2](10dlc-messaging--part-2.md), [Part 4](10dlc-messaging--part-4.md), [Part 5](10dlc-messaging--part-5.md)*

10DLC (10-Digit Long Code) is the industry standard for application-to-person (A2P) messaging on US long code numbers. Registering your brand and campaigns with The Campaign Registry (TCR) through Telnyx provides higher throughput, better deliverability, and reduced carrier filtering. Your brand's vetting score directly determines your messaging throughput limits across AT&T, T-Mobile, and other carriers.

## Phone Number Assignment

After your brand is registered and campaign is approved, assign phone numbers to the campaign before sending messages. Only numbers assigned to an active campaign can send 10DLC A2P messages.

### Requirements

| Requirement | Details |
| --- | --- |
| Number type | US long code (10-digit) numbers only |
| Messaging profile | Number must be assigned to a messaging profile first |
| Campaign status | Campaign must be `ACTIVE` (approved by carriers) |
| One campaign per number | Each number can only be assigned to one campaign at a time |

Numbers not assigned to an active 10DLC campaign will have messages filtered or blocked by carriers.

### Assigning a Number

```
curl -X POST https://api.telnyx.com/v2/10dlc/phoneNumberCampaign \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "phoneNumber": "+15551234567",
    "campaignId": "CAMPAIGN_ID"
  }'
```

### Removing a Number

```
curl -X DELETE "https://api.telnyx.com/v2/10dlc/phoneNumberCampaign/+15551234567" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

Removing a number means it can no longer send 10DLC messages. You can reassign it to a different campaign afterward.

### Number Pool Integration

If you're using Number Pools, every number in the pool must be assigned to the same 10DLC campaign. If a number in your pool is not assigned to a campaign, messages from that number will be filtered by carriers, creating inconsistent delivery.

## 10DLC Rate Limits and Throughput

Your 10DLC throughput is determined by your brand vetting score and campaign type. Each carrier applies different rate limits.

### AT&T Throughput

AT&T assigns throughput per campaign based on a Message Class, determined by your use case type and vetting score.

**Standard use cases:**

| Message Class | Use Case | Vetting Score | SMS TPM | MMS TPM |
| --- | --- | --- | --- | --- |
| A | Standard (Dedicated) | 75–100 | 4,500 | 2,400 |
| B | Standard (Mixed/Marketing) | 75–100 | 4,500 | 2,400 |
| C | Standard (Dedicated) | 50–74 | 2,400 | 1,200 |
| D | Standard (Mixed/Marketing) | 50–74 | 2,400 | 1,200 |
| E | Standard (Dedicated) | 1–49 | 240 | 150 |
| F | Standard (Mixed/Marketing) | 1–49 | 240 | 150 |
| T | Low Volume Mixed | Any | 75 | 50 |
| W | Sole Proprietor | N/A | 15 | 50 |

**Special use cases** (fixed throughput regardless of vetting score):

| Message Class | Use Case | SMS TPM | MMS TPM |
| --- | --- | --- | --- |
| K | Political | 4,500 | 2,400 |
| P | Charity / Nonprofit | 2,400 | 1,200 |
| S | Social | 9,000 | 2,400 |
| X | Emergency / Public Safety | 4,500 | 2,400 |
| G | Proxy (per number) | 60 | 50 |
| N | Agents & Franchises (per number) | 60 | 50 |

TPM = Throughput Per Minute. AT&T measures throughput in messages per minute, not per second. To convert: 4,500 TPM ≈ 75 MPS.

### T-Mobile Throughput

T-Mobile uses daily message caps at the brand level, shared across all campaigns under that brand.

| Brand Tier | Vetting Score | Daily SMS Cap |
| --- | --- | --- |
| Top | 75–100 | 200,000 |
| High | 50–74 | 40,000 |
| Medium | 25–49 | 10,000 |
| Basic | 1–24 | 2,000 |
| Sole Proprietor | N/A | 1,000 |

T-Mobile caps are **per brand**, not per campaign. If you have 3 campaigns under one brand, they share the same daily cap. Unvetted brands default to the Basic tier (2,000/day) unless the business is listed on the Russell 3000 index.

### Verizon Throughput

Verizon has not published specific throughput numbers for 10DLC. They use content-based filtering rather than explicit rate limits. Messages that comply with your registered campaign use case are generally delivered without throttling.

### Vetting Score Impact Summary

| Score Range | AT&T SMS TPM | T-Mobile Daily Cap | Recommendation |
| --- | --- | --- | --- |
| 75–100 | 4,500 | 200,000 | ✅ Ideal for production |
| 50–74 | 2,400 | 40,000 | ⚠️ Adequate for moderate volume |
| 25–49 | 240 | 10,000 | ⚠️ Limited — consider enhanced vetting |
| 1–24 | 240 | 2,000 | ❌ Very limited — improve score |
| Unvetted | 240 | 2,000 | ❌ Get vetted immediately |

### Checking Your Scores

```
# Get brand vetting score
curl -s https://api.telnyx.com/v2/10dlc/brand/{brandId} \
  -H "Authorization: Bearer YOUR_API_KEY" | jq '.data.vettingScore'

# List campaigns with throughput info
curl -s https://api.telnyx.com/v2/10dlc/campaign \
  -H "Authorization: Bearer YOUR_API_KEY" | jq '.data[] | {campaignId, usecase, attMsgClass, attTpm, tMobileBrandTier}'
```

## Event Notifications

You can receive webhook notifications for 10DLC brand, campaign, and phone number events.

### Configuring Webhooks

Set `webhookURL` and optionally `webhookFailoverURL` when creating or updating a brand or campaign. Campaign webhooks also apply to phone numbers assigned to that campaign.

```
curl -X PUT https://api.telnyx.com/10dlc/brand/:brandid \
  -H 'Content-type: application/json' \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -d '{"webhookURL":"https://mywebhooks.com/endpoint", "webhookFailoverURL":"https://mywebhooks.com/failover"}'
```

### Event Types

Three event types are supported:
- `10dlc.brand.update` — Brand lifecycle events
- `10dlc.campaign.update` — Campaign lifecycle events
- `10dlc.phone_number.update` — Phone number assignment events

Each event payload contains `event_type`, `id`, `occurred_at`, `payload`, and `record_type`. The `meta` object contains `attempt` (delivery attempt number) and `delivered_to` (the webhook URL).

### Brand Event Payload Types

| Payload Type | Description |
| --- | --- |
| `REGISTRATION` | Failures during the registration process; `reasons` field contains errors |
| `REVET` | Result of a revetting request |
| `ORDER_EXTERNAL_VETTING` | Notification on external vetting order process |
| `TCR_BRAND_UPDATE` | Notifications from TCR: `BRAND_ADD`, `BRAND_APPEAL_ADD`, `BRAND_APPEAL_COMPLETE`, `BRAND_REVET` |

### Campaign Event Payload Types

| Payload Type | Description |
| --- | --- |
| `REGISTRATION` | Registration failures; `reasons` field contains errors |
| `TELNYX_REVIEW` | Telnyx compliance review; status `ACCEPTED` or `REJECTED` |
| `NUMBER_POOL_PROVISIONED` | Number pool provisioning success |
| `NUMBER_POOL_DEPROVISIONED` | Number pool deprovisioning |
| `TCR_EVENT` | TCR notifications: `CAMPAIGN_ADD`, `CAMPAIGN_BILLED`, `CAMPAIGN_DCA_COMPLETE`, `CAMPAIGN_EXPIRED`, `CAMPAIGN_NUDGE`, `CAMPAIGN_RESUBMISSION`, `CAMPAIGN_UPDATE`, MNO operation events |
| `MNO_REVIEW` | MNO/DCA review results; status `ACCEPTED` or `REJECTED` |
| `TELNYX_EVENT` | Telnyx system events (e.g., campaign suspension; status `DORMANT`) |
| `VERIFIED` | Campaign fully provisioned with MNOs; reaches `MNO_PROVISIONED` status |

### Phone Number Event Payload Types

| Payload Type | Description |
| --- | --- |
| `ASSIGNMENT` | Phone number assignment; `reasons` empty on success |
| `DELETION` | Phone number removal; `reasons` empty on success |
| `STATUS_UPDATE` | Status changed; status can be `ADDED`, `DELETED`, `PENDING`, or `FAILED` |

Phone numbers in webhook payloads use E.164 format (e.g., `+16715455939`).

**Note:** The `campaignId` field in webhooks contains the Telnyx UUID, not the TCR campaign ID. The TCR campaign ID (e.g., `C6X6M95`) may appear in the `description` field. `CAMPAIGN_NUDGE` events are an exception — they originate from TCR and use the TCR campaign ID format.

### Webhook Retry Policy

- **Default retry attempts:** 5
- **Default retry interval:** 30 seconds between attempts
- After 5 failed attempts, the webhook is marked as failed

### Webhook Best Practices

- Return 2xx quickly; process asynchronously
- Handle duplicates using the `id` field
- Use HTTPS endpoints
- Configure a `webhookFailoverURL` for redundancy
- Consider signature verification for added security

For local testing, use tunneling tools such as ngrok, Cloudflare Tunnel, or localtunnel.
