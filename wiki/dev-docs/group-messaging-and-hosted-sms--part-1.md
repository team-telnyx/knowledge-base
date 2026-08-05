---
title: Group Messaging and Hosted SMS
summary: Telnyx messaging capabilities covering group MMS messaging for multi-party
  conversations and Hosted SMS for adding programmable messaging to numbers that remain
  with an existing voice provider, including internal transfers between Telnyx accounts.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/group-messaging
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/index
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/internal-transfer
updated_at: 2026-08-05T13:55:37Z
---

# Group Messaging and Hosted SMS

*Part 1 of 3 — see also: [Part 2](group-messaging-and-hosted-sms--part-2.md), [Part 3](group-messaging-and-hosted-sms--part-3.md)*

Telnyx messaging capabilities covering group MMS messaging for multi-party conversations and Hosted SMS for adding programmable messaging to numbers that remain with an existing voice provider, including internal transfers between Telnyx accounts.

## Group Messaging

Send group MMS messages to multiple recipients in a single API call. Group messaging uses the MMS protocol to create multi-party conversations where all participants can see and reply to each other, just like a group text on a phone.

### Prerequisites

- A [Telnyx account](https://telnyx.com/sign-up)
- A [Messaging Profile](messaging-profile.md) with an MMS-enabled phone number
- An [API key](https://portal.telnyx.com/#/app/api-keys)

### How group messaging works

Group messaging builds on the MMS protocol to enable multi-party conversations:

1. Send a message to the `/v2/messages/group_mms` endpoint with multiple `to` numbers.
2. Telnyx delivers the message to all recipients as a group MMS conversation.
3. When any recipient replies, all participants (including the Telnyx number) receive the reply.
4. Inbound group messages arrive via [Receiving Webhooks](receiving-webhooks.md) with a `cc` field listing all participants.

**Group messaging constraints:**

- Maximum of **8 recipients** per conversation (plus the sender)
- **MMS protocol only** — all messages are billed at MMS rates
- **US and Canada destinations only**
- Requires a **v2 webhook version** on the messaging profile for inbound messages
- Charged **per recipient** — standard MMS rates plus carrier passthrough fees apply

### Send a group message

Set the API key as an environment variable:

```
export TELNYX_API_KEY="YOUR_API_KEY"
```

Send a group MMS to multiple recipients. Text, media, or both can be included.

**Text + Media**

```
curl -X POST https://api.telnyx.com/v2/messages/group_mms \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -d '{
    "from": "+15551234567",
    "to": ["+15559876543", "+15558765432"],
    "text": "Hey team, check out this photo!",
    "media_urls": ["https://example.com/photo.jpg"]
  }'
```

**Text only**

```
curl -X POST https://api.telnyx.com/v2/messages/group_mms \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TELNYX_API_KEY" \
  -d '{
    "from": "+15551234567",
    "to": ["+15559876543", "+15558765432"],
    "text": "Hey team, lunch at noon?"
  }'
```

A successful response includes per-recipient status:

```
{
  "data": {
    "record_type": "message",
    "direction": "outbound",
    "id": "403188fd-58c5-4557-a8de-1700a358d768",
    "type": "MMS",
    "messaging_profile_id": "1e0df9c5-8716-4bcf-8fb2-9f6d9527fd95",
    "from": "+15551234567",
    "to": [
      {
        "phone_number": "+15559876543",
        "status": "queued",
        "carrier": "T-MOBILE USA, INC.",
        "line_type": "Wireless"
      },
      {
        "phone_number": "+15558765432",
        "status": "queued",
        "carrier": "CELLCO PARTNERSHIP DBA VERIZON WIRELESS",
        "line_type": "Wireless"
      }
    ],
    "text": "Hey team, check out this photo!",
    "media": [
      {
        "url": "https://example.com/photo.jpg",
        "content_type": null,
        "sha256": null,
        "size": null
      }
    ],
    "encoding": "GSM-7",
    "parts": 1,
    "cost": {
      "amount": "0.0800",
      "currency": "USD"
    }
  }
}
```

Save the `id` to correlate delivery webhooks with the group message.

### Receive group messages

When someone replies to the group conversation, a `message.received` webhook is delivered. The `cc` field lists all other participants in the conversation:

```
{
  "data": {
    "event_type": "message.received",
    "id": "0d7c4fbe-d075-435f-b71b-694391743967",
    "occurred_at": "2023-08-08T13:03:05.129+00:00",
    "payload": {
      "cc": [
        "+15558765432",
        "+15557654321",
        "+15551234567"
      ],
      "direction": "inbound",
      "encoding": "UCS-2",
      "from": {
        "carrier": "AT&T",
        "line_type": "Wireless",
        "phone_number": "+15559876543"
      },
      "id": "9d12c9d0-5172-429a-8fb9-cc9da297717f",
      "media": [],
      "messaging_profile_id": "1e0df9c5-8716-4bcf-8fb2-9f6d9527fd95",
      "record_type": "message",
      "text": "Sounds good, see you at noon!",
      "to": [
        {
          "carrier": "Telnyx",
          "line_type": "Wireless",
          "phone_number": "+15551234567",
          "status": "webhook_delivered"
        }
      ],
      "type": "MMS"
    },
    "record_type": "event"
  }
}
```

**Key fields for inbound group messages:**

| Field | Description |
| --- | --- |
| `from.phone_number` | The participant who sent the reply |
| `to` | The Telnyx number(s) in the conversation |
| `cc` | All other participants in the group conversation |

### Webhooks and delivery tracking

Group messages generate individual webhook events and detail records for each recipient:

- **Per-recipient webhooks:** A separate `message.finalized` event is delivered for each recipient with its individual delivery status.
- **`group_message_id`:** A unique identifier returned in the API response, webhooks, and detail records that lets you correlate all individual records back to the original group message.
- **Non-Telnyx recipient status:** Handset delivery confirmation is not available for non-Telnyx recipients — their status will show as `unknown`.

Example delivery webhook:

```
{
  "data": {
    "event_type": "message.finalized",
    "id": "b40653f5-91cd-46b1-9542-0c092bd29795",
    "occurred_at": "2023-08-08T10:29:36.090+00:00",
    "payload": {
      "direction": "outbound",
      "from": {
        "phone_number": "+15551234567"
      },
      "group_message_id": "403189d4-b1d6-4993-b263-6470e5224430",
      "id": "403189d4-b1d6-4993-b263-6470e5224430",
      "to": [
        {
          "phone_number": "+15559876543",
          "status": "delivered"
        }
      ],
      "text": "Hey team, check out this photo!",
      "type": "MMS"
    },
    "record_type": "event"
  }
}
```

### Comparison with other providers

| Feature | Telnyx | Twilio | Vonage |
| --- | --- | --- | --- |
| Group MMS support | ✅ Native, single API call | ⚠️ Requires Conversations API | ❌ Not natively supported |
| Max participants | 8 + sender | 10 total | N/A |
| Dedicated endpoint | ✅ `/v2/messages/group_mms` | ❌ Requires Conversations setup | N/A |
| Setup complexity | Single POST request | Multi-step (create conversation, add participants) | N/A |
| Per-recipient tracking | ✅ Individual webhooks | ✅ Via Conversations events | N/A |
| US/Canada support | ✅ | ✅ | N/A |

### Troubleshooting

**Messages not delivered to all recipients**

- Verify all `to` numbers are valid US or Canadian wireless numbers.
- Group MMS requires MMS-capable handsets — landlines and some VoIP numbers won't receive them.
- Check that the 8-recipient limit has not been exceeded.

**Not receiving inbound group messages**

- Ensure the messaging profile uses **v2 webhook version** — go to [Messaging](https://portal.telnyx.com/#/app/messaging), edit the profile, and confirm the webhook version.
- Verify the webhook URL is accessible and returning `200 OK`.

**Status shows 'unknown' for recipients**

This is expected for non-Telnyx recipients. The MMS protocol does not reliably support delivery receipts across all carriers. Only Telnyx-to-Telnyx messages will show confirmed delivery status.
