---
title: Schedule SMS and MMS Messages
summary: Schedule SMS and MMS messages to send at a specific time in the future using
  the Telnyx messaging API. Use scheduled messaging for appointment reminders, marketing
  campaigns, time-zone-aware notifications, and any scenario where precise delivery
  timing matters.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/schedule-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-an-rcs-message/index
updated_at: 2026-08-05T13:56:55Z
---

# Schedule SMS and MMS Messages

*Part 3 of 3 — see also: [Part 1](schedule-sms-and-mms-messages--part-1.md), [Part 2](schedule-sms-and-mms-messages--part-2.md)*

Schedule SMS and MMS messages to send at a specific time in the future using the Telnyx messaging API. Use scheduled messaging for appointment reminders, marketing campaigns, time-zone-aware notifications, and any scenario where precise delivery timing matters.

## Retrieve a scheduled message

Check the status of a scheduled message with `GET /v2/messages/{id}`:

```
curl -X GET https://api.telnyx.com/v2/messages/b0c7e8cb-6227-4c74-9f32-c7f80c30934b \
  -H "Authorization: Bearer $TELNYX_API_KEY"
```

```python
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),
)

response = client.messages.retrieve("b0c7e8cb-6227-4c74-9f32-c7f80c30934b")

print(response.data)
```

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'],
});

const response = await client.messages.retrieve(
  'b0c7e8cb-6227-4c74-9f32-c7f80c30934b'
);

console.log(response.data);
```

The retrieve endpoint can only access messages created within the last **10 days**. For older messages, generate an [MDR report](https://portal.telnyx.com/#/app/reporting/mdr).

## Cancel a scheduled message

Cancel a message that hasn't been sent yet with `DELETE /v2/messages/{id}`:

```
curl -X DELETE https://api.telnyx.com/v2/messages/b0c7e8cb-6227-4c74-9f32-c7f80c30934b \
  -H "Authorization: Bearer $TELNYX_API_KEY"
```

```python
import os
from telnyx import Telnyx

client = Telnyx(
    api_key=os.environ.get("TELNYX_API_KEY"),
)

response = client.messages.delete("b0c7e8cb-6227-4c74-9f32-c7f80c30934b")

print(response.data)
```

```javascript
import Telnyx from 'telnyx';

const client = new Telnyx({
  apiKey: process.env['TELNYX_API_KEY'],
});

const response = await client.messages.del(
  'b0c7e8cb-6227-4c74-9f32-c7f80c30934b'
);

console.log(response.data);
```

**Cancellation rules:**

- The message must have `status: "scheduled"`
- The `send_at` time must be more than **1 minute** in the future
- Once a message begins sending, it cannot be cancelled

## Webhooks

Scheduled messages trigger the same [messaging webhooks](receiving-webhooks.md) as immediate messages. The webhook sequence is:

1. **`message.sent`** — Fires when the message is sent at the scheduled time
2. **`message.finalized`** — Fires when delivery is confirmed or fails

Example webhook payload for a scheduled message:

```json
{
  "data": {
    "event_type": "message.sent",
    "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "occurred_at": "2026-02-15T14:30:01Z",
    "payload": {
      "id": "b0c7e8cb-6227-4c74-9f32-c7f80c30934b",
      "direction": "outbound",
      "type": "SMS",
      "from": {
        "phone_number": "+15551234567"
      },
      "to": [
        {
          "phone_number": "+15559876543",
          "status": "sent"
        }
      ],
      "text": "Reminder: Your appointment is tomorrow at 10 AM."
    }
  }
}
```

## Use cases

### Appointment reminders

Schedule reminders 24 hours before an appointment:

```python
from datetime import datetime, timedelta, timezone
import os
from telnyx import Telnyx

client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

appointment_time = datetime(2026, 2, 16, 10, 0, tzinfo=timezone.utc)
reminder_time = appointment_time - timedelta(hours=24)

response = client.messages.send(
    from_="+15551234567",
    to="+15559876543",
    text=f"Reminder: Your appointment is tomorrow at {appointment_time.strftime('%I:%M %p')} UTC.",
    send_at=reminder_time.isoformat()
)

print(f"Reminder scheduled for {reminder_time.isoformat()}, message ID: {response.data.id}")
```

### Time-zone-aware campaigns

Send marketing messages during business hours in each recipient's time zone:

```python
from datetime import datetime, timezone, timedelta
import os
from telnyx import Telnyx

client = Telnyx(api_key=os.environ.get("TELNYX_API_KEY"))

recipients = [
    {"number": "+15551234567", "tz_offset": -5},  # EST
    {"number": "+15559876543", "tz_offset": -8},  # PST
    {"number": "+15557654321", "tz_offset": -6},  # CST
]

for recipient in recipients:
    # Send at 10:00 AM in each recipient's local time
    local_10am = datetime(2026, 2, 16, 10, 0, tzinfo=timezone(timedelta(hours=recipient["tz_offset"])))
    utc_time = local_10am.astimezone(timezone.utc)

    response = client.messages.send(
        from_="+15550001111",
        to=recipient["number"],
        text="Weekend flash sale! 20% off with code WEEKEND20.",
        send_at=utc_time.isoformat()
    )
    print(f"Scheduled for {recipient['number']} at {utc_time.isoformat()}")
```

## Limits and rate limiting

- **Scheduling window:** 5 minutes to 5 days in the future
- **Maximum scheduled messages:** 1 million at any given time
- **Accuracy:** Messages are sent within 1 minute of the scheduled time
- **Rate limits:** The same [messaging rate limits](rate-limiting.md) apply to scheduled messages as to immediate messages — both when creating the scheduled message and when it's sent

## Comparison with other providers

| Feature | Telnyx | Twilio | Vonage |
| --- | --- | --- | --- |
| Scheduling window | 5 min – 5 days | 15 min – 35 days | Not natively supported |
| Cancellation | ✅ Up to 1 min before send time | ✅ Up to 1 hour before send time | N/A |
| Dedicated endpoint | ✅ `/v2/messages/schedule` | ❌ Same endpoint only | N/A |
| Requires Messaging Service | ❌ Optional | ✅ Required | N/A |
| Additional cost | ❌ Free | ❌ Free | N/A |
| Accuracy | ~1 minute | ~15 minutes | N/A |

## Next steps

- [Send Your First Message](send-your-first-message.md) — New to Telnyx messaging? Start here
- [Receiving Webhooks](receiving-webhooks.md) — Handle delivery confirmations and inbound messages
- [Rate Limiting](rate-limiting.md) — Understand messaging throughput limits
- [API Reference](https://developers.telnyx.com/docs/messaging/messages/schedule-message) — Full API parameter documentation
