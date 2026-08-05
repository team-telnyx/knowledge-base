---
title: International SMS Compliance, Encoding, and Message Detail Records
summary: A consolidated reference covering country-specific SMS compliance requirements
  for the top international destinations, SMS message encoding and segment calculation,
  and how to use Message Detail Records (MDRs) to track delivery, cost, and errors.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/international-sms-compliance
- url: https://developers.telnyx.com/docs/messaging/messages/message-detail-records/index
- url: https://developers.telnyx.com/docs/messaging/messages/message-encoding/index
updated_at: 2026-08-05T13:56:16Z
---

# International SMS Compliance, Encoding, and Message Detail Records

*Part 5 of 6 — see also: [Part 1](international-sms-compliance-encoding-and-message-detail-records--part-1.md), [Part 2](international-sms-compliance-encoding-and-message-detail-records--part-2.md), [Part 3](international-sms-compliance-encoding-and-message-detail-records--part-3.md), [Part 4](international-sms-compliance-encoding-and-message-detail-records--part-4.md), [Part 6](international-sms-compliance-encoding-and-message-detail-records--part-6.md)*

A consolidated reference covering country-specific SMS compliance requirements for the top international destinations, SMS message encoding and segment calculation, and how to use Message Detail Records (MDRs) to track delivery, cost, and errors.

## Message Detail Records (MDRs)

A Message Detail Record (MDR) describes a specific message request—including its current status, cost, and metadata. Telnyx creates an MDR when a message is submitted and updates it as the message progresses through delivery.

**When to use MDRs:**

- **Delivery tracking** — Check if a message was delivered, failed, or is still in progress.
- **Debugging** — Investigate delivery issues by examining message status and error codes.
- **Cost verification** — Confirm message costs after delivery for billing reconciliation.
- **Audit trail** — Retrieve message history for compliance and record-keeping.

### Retrieve an MDR

Fetch a message record using its UUID. The UUID is returned when you send a message and is also included in webhook events.

```bash
curl -X GET "https://api.telnyx.com/v2/messages/834f3d53-8a3c-4aa0-a733-7f2d682a72df" \
  -H "Authorization: Bearer YOUR_API_KEY"
```

**Example response:**

```json
{
  "data": {
    "record_type": "message",
    "id": "834f3d53-8a3c-4aa0-a733-7f2d682a72df",
    "direction": "outbound",
    "type": "SMS",
    "messaging_profile_id": "16fd2706-8baf-433b-82eb-8c7fada847da",
    "from": {
      "phone_number": "+18445550001",
      "carrier": "Telnyx",
      "line_type": "VoIP"
    },
    "to": [
      {
        "phone_number": "+18665550002",
        "status": "delivered",
        "updated_at": "2019-01-23T18:10:02.574Z"
      }
    ],
    "text": "Hello, World!",
    "webhook_url": "https://www.example.com/hooks",
    "webhook_failover_url": "https://www.example.com/hooks-backup",
    "use_profile_webhooks": false,
    "encoding": "GSM-7",
    "parts": 1,
    "cost": {
      "amount": "0.0050",
      "currency": "USD"
    },
    "errors": [],
    "created_at": "2019-01-23T18:10:00.000Z",
    "updated_at": "2019-01-23T18:10:02.574Z",
    "valid_until": "2019-01-23T18:25:00.000Z"
  }
}
```

### MDR schema

| Field | Type | Description |
| --- | --- | --- |
| `id` | UUID | Unique identifier for the message request |
| `direction` | string | `inbound` or `outbound` |
| `type` | string | Message type: `SMS`, `MMS`, or `RCS` |
| `messaging_profile_id` | UUID | The messaging profile used to send/receive |
| `from` | object | Sender details including `phone_number`, `carrier`, `line_type` |
| `to` | array | Recipients with `phone_number`, `status`, `updated_at` |
| `text` | string | Message body content |
| `media_urls` | array | Media attachment URLs (MMS only) |
| `encoding` | string | Character encoding: `GSM-7` or `UCS-2` |
| `parts` | integer | Number of message segments |
| `cost` | object | `amount` and `currency` (may be `null` until finalized) |
| `errors` | array | Error details if delivery failed |
| `webhook_url` | string | URL for delivery status webhooks |
| `webhook_failover_url` | string | Backup webhook URL |
| `use_profile_webhooks` | boolean | Whether to use profile-level webhooks |
| `created_at` | ISO 8601 | When the message was submitted |
| `updated_at` | ISO 8601 | Last status update time |
| `valid_until` | ISO 8601 | Expiration time for pending messages |

**Cost may be null:** When retrieved immediately after sending, `cost` may be `null` because pricing is calculated asynchronously. The final cost appears in the `message.finalized` webhook event.

### Message status

The `status` field in the `to` array indicates where the message is in its lifecycle.

**Outbound statuses:**

| Status | Description | Final? |
| --- | --- | --- |
| `queued` | Message accepted and queued for sending | No |
| `sent` | Delivered to carrier gateway | No |
| `delivered` | Carrier confirmed delivery to handset | ✓ Yes |
| `failed` | Delivery failed (see `errors` array) | ✓ Yes |
| `gw_timeout` | No response from gateway | ✓ Yes |
| `dlr_timeout` | No delivery receipt from carrier | ✓ Yes |

**Inbound statuses:**

| Status | Description |
| --- | --- |
| `received` | Message received by Telnyx |
| `delivered` | Message delivered to your webhook |

Rather than polling for status, configure a webhook URL to receive real-time status updates as `message.sent`, `message.delivered`, or `message.finalized` events.

### Common error codes

When a message fails, the `errors` array contains details:

```json
{
  "errors": [
    {
      "code": "40301",
      "title": "Destination number blocked",
      "detail": "The recipient has opted out of messages from this sender"
    }
  ]
}
```

| Error Code | Description | Resolution |
| --- | --- | --- |
| `40300` | Invalid destination | Verify the phone number format |
| `40301` | Destination blocked | Recipient has opted out—remove from list |
| `40310` | Carrier rejected | Message content may have triggered spam filters |
| `40311` | Undeliverable | Number is unreachable (landline, disconnected) |
| `40400` | Sender not registered | Register for 10DLC or toll-free verification |
| `40500` | Rate limit exceeded | Slow down sending or request higher limits |

## Best practices for international messaging

1. **Check country requirements before launch** — Review this guide and contact Telnyx support for any country not listed. Requirements vary significantly and change frequently.
2. **Use the right sender type** — Alphanumeric sender IDs are preferred in most international markets (except US/Canada). They build brand recognition and improve open rates.
3. **Localize your messages** — Send messages in the recipient's language. Many countries require or strongly recommend this for commercial messaging.
4. **Respect time zones and quiet hours** — Even where not legally required, sending during business hours dramatically reduces complaints and opt-outs.
5. **Include opt-out in every message** — Universal best practice. Use language appropriate to the country (e.g., "STOP" in English-speaking countries, "ARRÊT" in France).
6. **Maintain consent records** — Store when and how each recipient consented. GDPR requires you to prove consent if challenged. Keep records for at least 4 years.
7. **Monitor delivery rates by country** — Use [MDRs](message-detail-records.md) to track delivery rates per country. Sudden drops may indicate registration issues or content filtering.
8. **Enable smart encoding** — Turn on [smart encoding](smart-encoding.md) on your messaging profile to automatically handle Unicode-to-GSM-7 substitutions. This is the single biggest cost-saving measure.
9. **Validate before sending** — Use encoding detection helpers to check segment counts before sending. Alert your application when messages will be unexpectedly expensive.
10. **Sanitize input text** — If you accept user-generated content, sanitize it before sending. Strip or replace invisible Unicode characters, curly quotes, and other common problem characters.
11. **Keep messages concise** — Stay under 160 characters (GSM-7) or 70 characters (UTF-16) to avoid multi-part message overhead.
12. **Use the right channel** — For messages that need emojis, rich formatting, or non-Latin scripts, consider MMS or RCS instead of SMS.
