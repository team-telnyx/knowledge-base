---
title: Messaging Profiles
summary: A messaging profile is the central configuration object for Telnyx messaging.
  It groups phone numbers, defines webhook URLs, and controls features such as number
  pooling, smart encoding, MMS transcoding, MMS-to-SMS fallback, spend limits, and
  URL shortening. Every phone number used for messaging must be assigned to a messaging
  profile.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/messaging-profiles-overview/index
- url: https://developers.telnyx.com/docs/messaging/messages/mms-converter
- url: https://developers.telnyx.com/docs/messaging/messages/mms-transcoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/number-pool/index
- url: https://developers.telnyx.com/docs/messaging/messages/phone-number-configuration/index
updated_at: 2026-08-05T13:56:37Z
---

# Messaging Profiles

*Part 6 of 6 — see also: [Part 1](messaging-profiles--part-1.md), [Part 2](messaging-profiles--part-2.md), [Part 3](messaging-profiles--part-3.md), [Part 4](messaging-profiles--part-4.md), [Part 5](messaging-profiles--part-5.md)*

A messaging profile is the central configuration object for Telnyx messaging. It groups phone numbers, defines webhook URLs, and controls features such as number pooling, smart encoding, MMS transcoding, MMS-to-SMS fallback, spend limits, and URL shortening. Every phone number used for messaging must be assigned to a messaging profile.

## Common configurations

### Transactional (OTP, alerts)

```json
{
  "name": "Transactional Messages",
  "webhook_url": "https://api.example.com/webhooks/sms",
  "smart_encoding": true,
  "daily_spend_limit_enabled": true,
  "daily_spend_limit": "100.00"
}
```

Best for OTP codes, account alerts, and order confirmations. Low volume, high priority. Smart encoding reduces costs.

### Marketing campaigns

```json
{
  "name": "Marketing Campaigns",
  "webhook_url": "https://api.example.com/webhooks/marketing",
  "number_pool_settings": {
    "geomatch": true,
    "sticky_sender": true,
    "skip_unhealthy": true
  },
  "smart_encoding": true,
  "mms_transcoding": true,
  "daily_spend_limit_enabled": true,
  "daily_spend_limit": "500.00"
}
```

Best for promotional messages and newsletters. Number pool for throughput. Higher spend limit for volume.

### Support / Conversational

```json
{
  "name": "Customer Support",
  "webhook_url": "https://api.example.com/webhooks/support",
  "number_pool_settings": {
    "sticky_sender": true
  },
  "smart_encoding": true
}
```

Best for two-way conversations. Sticky sender ensures customers always see the same number.

## Troubleshooting

- **Number not appearing in `messaging_phone_numbers` list** — The number may not have messaging capabilities, may not have finished provisioning, or may be on a different Telnyx account. Verify the number's capabilities via `GET /v2/phone_numbers/{id}` and check for `messaging` in the features.
- **Messages failing with 'number not associated with messaging profile'** — The `from` number in your send request isn't assigned to a messaging profile. Assign the number to a profile, or use the messaging profile's number pool to automatically select a number.
- **Inbound messages not triggering webhooks** — The number isn't assigned to a messaging profile, the messaging profile doesn't have a webhook URL configured, or your webhook endpoint is returning errors. Verify the number → profile → webhook URL chain.
- **Number shows messaging enabled but messages are filtered** — For US long codes, messages may be filtered by carriers if 10DLC registration isn't complete. Complete 10DLC brand and campaign registration. For toll-free, complete verification.
- **Cannot assign number to a messaging profile** — The number may already be assigned to a different product (voice connection, etc.) that conflicts, the messaging profile ID may be invalid, or the number may belong to a different organization. Check the profile ID, verify number ownership, and ensure no conflicting product assignments.

## Related resources

- [Number Pool](number-pool.md) — Distribute messages across multiple numbers for higher throughput.
- [Smart Encoding](smart-encoding.md) — Reduce SMS costs by replacing Unicode with GSM-7 characters.
- [Spend Limits](spend-limits.md) — Set daily spend caps to prevent unexpected costs.
- [Webhooks](webhooks.md) — Receive inbound messages and delivery status updates.
- [Sticky Sender](sticky-sender.md) — Maintain sender consistency for recipients.
- [Geomatch](geomatch.md) — Match sender to recipient geography.
- [Send & Receive MMS Tutorial](send-receive-mms-tutorial.md) — Full tutorial for building an MMS application with media storage.
- [SMIL Templates](smil-templates.md) — Customize the layout of your MMS media with SMIL templates.
- [Send Your First Message](send-your-first-message.md) — Get started with the Telnyx Messaging API.
- [Messages API Reference](messages-api-reference.md) — API reference for sending messages with media.
- [Rate Limiting](rate-limiting.md) — Understand messaging throughput limits.
- [10DLC Registration](10dlc-registration.md) — Register your brand and campaign for US long code messaging.
- [Toll-Free Verification](toll-free-verification--part-1.md) — Verify toll-free numbers for messaging.
