---
title: Telnyx Messaging
summary: Telnyx Messaging provides APIs and infrastructure for sending and receiving
  SMS, MMS, and RCS messages globally. This page covers phone number configuration,
  messaging profiles, encoding, rate limiting, MMS handling, delivery tracking, international
  compliance, and RCS with AI integration.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance
- url: https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index
- url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
- url: https://developers.telnyx.com/docs/messaging/messages/mms-converter
- url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/number-pool/index
- url: https://developers.telnyx.com/docs/messaging/messages/phone-number-configuration/index
- url: https://developers.telnyx.com/docs/messaging/messages/rate-limiting/index
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-ai-assistant
updated_at: 2026-06-11T10:38:14Z
---

# Telnyx Messaging

*Part 1 of 5 — see also: [Part 2](telnyx-messaging-2--part-2.md), [Part 3](telnyx-messaging-2--part-3.md), [Part 4](telnyx-messaging-2--part-4.md), [Part 5](telnyx-messaging-2--part-5.md)*

Telnyx Messaging provides APIs and infrastructure for sending and receiving SMS, MMS, and RCS messages globally. This page covers phone number configuration, messaging profiles, encoding, rate limiting, MMS handling, delivery tracking, international compliance, and RCS with AI integration.

## Phone Number Configuration

Every phone number used for messaging must be assigned to a messaging profile and have messaging capabilities enabled. Different number types have different requirements before they can send messages:

| Number Type | Messaging Ready? | Additional Steps |
|---|---|---|
| Long code (US) | After 10DLC registration | Register brand + campaign |
| Toll-free (US/CA) | After verification | Submit toll-free verification |
| Short code | After provisioning | Short code setup |
| Long code (non-US) | Typically immediate | Check country-specific requirements |
| Alphanumeric sender ID | After registration | Alphanumeric ID setup |

US long codes without 10DLC registration will experience carrier filtering and potential message blocking. Always complete 10DLC registration before sending A2P messages on US long codes.

### Assigning numbers to profiles

List messaging-capable numbers on your account, then assign a number to a messaging profile:

```
curl -X PATCH "https://api.telnyx.com/v2/messaging_phone_numbers/+15551234567" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"messaging_profile_id": "400174af-0a13-4e28-b4f5-example12345"}'
```

Retrieve a number's configuration with `GET /v2/messaging_phone_numbers/+15551234567`. Response fields include `phone_number`, `messaging_profile_id`, `type` (long_code, toll_free, short_code), `country_code`, `features`, `health`, and `eligible_messaging_products`.

To unassign a number, set `messaging_profile_id` to `null`. For bulk assignment, patch each number individually with the same profile ID.

### Troubleshooting number issues

- **Number not in messaging list**: The number may lack messaging capabilities, still be provisioning, or belong to a different account.
- **Messages failing with "number not associated with messaging profile"**: Assign the number to a profile or use number pool for automatic selection.
- **Inbound messages not triggering webhooks**: Verify the number → profile → webhook URL chain. Check that your webhook endpoint is healthy.
- **Number messaging-enabled but messages filtered**: For US long codes, complete 10DLC registration; for toll-free, complete verification.

## Messaging Profiles

A messaging profile is the central configuration object for Telnyx messaging. It groups phone numbers, defines webhook URLs, and controls features. Every phone number used for messaging must be assigned to a messaging profile.

### Creating a profile

```
curl -X POST https://api.telnyx.com/v2/messaging_profiles \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "name": "My Messaging Profile",
    "webhook_url": "https://example.com/webhooks/messaging",
    "webhook_failover_url": "https://example.com/webhooks/messaging/failover"
  }'
```

You can also create profiles in the Telnyx Portal under **Messaging > Messaging Profiles**.

### Profile settings

| Setting | Description | Default |
|---|---|---|
| Webhook URL | Where inbound messages and delivery status events are sent | None (required) |
| Webhook Failover URL | Backup URL if primary is unreachable | None |
| Number Pool | Distribute messages across multiple numbers | Disabled |
| Sticky Sender | Reuse the same sender number for each recipient | Disabled |
| Geomatch | Select sender based on geographic proximity | Disabled |
| Smart Encoding | Replace Unicode characters with GSM-7 equivalents | Disabled |
| MMS Transcoding | Automatically resize media for carrier limits | Disabled |
| MMS Converter | Fall back from MMS to SMS when recipient doesn't support MMS | Disabled |
| Spend Limit | Daily spend cap to prevent unexpected costs | Disabled |
| URL Shortening | Shorten URLs in outbound messages | Disabled |

Update an existing profile to enable features:

```
curl -X PATCH https://api.telnyx.com/v2/messaging_profiles/{profile_id} \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "number_pool_settings": {
      "geomatch": true,
      "sticky_sender": true,
      "skip_unhealthy": true
    },
    "smart_encoding": true,
    "mms_transcoding": true,
    "daily_spend_limit_enabled": true,
    "daily_spend_limit": "50.00"
  }'
```

### Common profile configurations

**Transactional (OTP, alerts)**: Enable smart encoding and a daily spend limit. Low volume, high priority.

**Marketing campaigns**: Enable number pool with geomatch and sticky sender, smart encoding, MMS transcoding, and a higher spend limit.

**Customer support / conversational**: Enable sticky sender so customers always see the same number, plus smart encoding.

### Assigning phone numbers

After creating a profile, assign numbers to it via API or the portal:

```
curl -X POST https://api.telnyx.com/v2/messaging_profiles/{profile_id}/phone_numbers \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"phone_number_id": "your_phone_number_id"}'
```

## Number Pool and Sender Selection

Number Pool automatically distributes outbound messages across multiple phone numbers assigned to a messaging profile. This increases throughput, avoids per-number rate limits, and helps maintain deliverability.

### How it works

All long code and toll-free numbers assigned to a messaging profile form the pool. When you send a message, Telnyx selects an available number based on configured weights and health.

### Configuring Number Pool

```
curl -X PATCH "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "number_pool_settings": {
      "long_code_weight": 5,
      "toll_free_weight": 1,
      "skip_unhealthy": true
    }
  }'
```

| Parameter | Type | Description |
|---|---|---|
| `long_code_weight` | integer | Weight for long code selection (0 removes from pool) |
| `toll_free_weight` | integer | Weight for toll-free selection (0 removes from pool) |
| `skip_unhealthy` | boolean | Skip numbers with poor delivery rates |
| `sticky_sender` | boolean | Reuse same number for a recipient across messages |
| `geomatch` | boolean | Match sender to recipient's geographic area |

Weights are ratios, not percentages. With `long_code_weight: 5` and `toll_free_weight: 1`, approximately 5 out of every 6 messages use a long code.

### Sending with Number Pool

Omit the `from` field and specify `messaging_profile_id`. Use the dedicated endpoint:

```
curl -X POST "https://api.telnyx.com/v2/messages/number_pool" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "messaging_profile_id": "YOUR_PROFILE_ID",
    "to": "+15559876543",
    "text": "Hello from Number Pool!"
  }'
```

The response includes the actual `from` number selected. To disable Number Pool, set `number_pool_settings` to an empty object `{}`.

### Related features

- **Sticky Sender**: Ensures the same number is reused for a given recipient across messages.
- **Geomatch**: Selects a sender number matching the recipient's area, improving deliverability and trust.
- **Skip Unhealthy Numbers**: Monitors delivery success rates and excludes poorly performing numbers. If all numbers are unhealthy, sending fails rather than using an unhealthy number.

### Troubleshooting Number Pool

- **"No healthy numbers in pool"**: All numbers are flagged unhealthy and `skip_unhealthy` is enabled. Temporarily disable it, add more numbers, or investigate delivery issues.
- **Messages always from same number type**: One weight may be 0, or only one number type is assigned.
- **"messaging_profile_id required" error**: You're using the standard `/v2/messages` endpoint instead of `/v2/messages/number_pool`.
