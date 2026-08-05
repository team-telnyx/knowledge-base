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

*Part 6 of 6 — see also: [Part 1](international-sms-compliance-encoding-and-message-detail-records--part-1.md), [Part 2](international-sms-compliance-encoding-and-message-detail-records--part-2.md), [Part 3](international-sms-compliance-encoding-and-message-detail-records--part-3.md), [Part 4](international-sms-compliance-encoding-and-message-detail-records--part-4.md), [Part 5](international-sms-compliance-encoding-and-message-detail-records--part-5.md)*

A consolidated reference covering country-specific SMS compliance requirements for the top international destinations, SMS message encoding and segment calculation, and how to use Message Detail Records (MDRs) to track delivery, cost, and errors.

## Handling multi-country messaging

For platforms sending to multiple countries, implement country-aware routing:

```python
import telnyx
import os

telnyx.api_key = os.environ["TELNYX_API_KEY"]

# Country-specific configuration
COUNTRY_CONFIG = {
    "US": {
        "from": "+12025551234",  # 10DLC registered number
        "profile": "us-messaging-profile-id",
    },
    "GB": {
        "from": "YourBrand",  # Alphanumeric sender ID
        "profile": "intl-messaging-profile-id",
    },
    "IN": {
        "from": "YRBRAND",  # 6-char registered DLT header
        "profile": "india-messaging-profile-id",
    },
    "DEFAULT": {
        "from": "YourBrand",
        "profile": "intl-messaging-profile-id",
    },
}

def send_international_sms(to: str, text: str, country_code: str):
    """Send an SMS with country-appropriate sender and profile."""
    config = COUNTRY_CONFIG.get(country_code, COUNTRY_CONFIG["DEFAULT"])

    message = telnyx.Message.create(
        from_=config["from"],
        to=to,
        text=text,
        messaging_profile_id=config["profile"],
    )
    return message

# Usage
send_international_sms("+447700900123", "Your order shipped!", "GB")
send_international_sms("+12025559876", "Your order shipped!", "US")
send_international_sms("+919876543210", "Your order shipped!", "IN")
```

## Troubleshooting

**MDR not found (404):** Verify the UUID format and check that the message send request returned a `201` status. Rejected requests don't create MDRs.

**Status stuck on 'queued':** Wait a few minutes. If still queued after 5 minutes, check [system status](https://status.telnyx.com) for outages. Messages stuck beyond `valid_until` will fail.

**Cost shows null:** Cost is calculated asynchronously after the message is sent. Either wait for the `message.finalized` webhook, or retrieve the MDR again after 5-10 seconds.

## Next steps

- [Alphanumeric Sender ID](alphanumeric-sender-id.md) — Set up branded sender IDs for international messaging.
- [Smart Encoding](smart-encoding.md) — Automatically replace Unicode characters with GSM-7 equivalents to reduce costs.
- [Error Code Reference](error-code-reference.md) — Understand delivery errors including country-specific rejections.
- [10DLC Quickstart](10dlc-quickstart.md) — US-specific registration for A2P messaging.
- [Receiving Webhooks](receiving-webhooks.md) — Get real-time delivery updates.
- [Send Messages](send-messages.md) — Complete sending quickstart.
- [Messages API Reference](messages-api-reference.md) — Complete Messages API docs.
- [Messaging Profiles](messaging-profiles--part-1.md) — Configure smart encoding and other profile settings.
