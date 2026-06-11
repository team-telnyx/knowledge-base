---
title: Telnyx Messaging
summary: Telnyx Messaging provides a comprehensive API for sending and receiving SMS
  and MMS messages, with features including messaging profiles, alphanumeric sender
  IDs, geomatching, group messaging, two-factor authentication, appointment reminders,
  advanced opt-in/out handling, configurable spend limits, hosted SMS, and detailed
  error handling.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/2fa/index
- url: https://developers.telnyx.com/docs/messaging/messages/advanced-opt-in-out/index
- url: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id/index
- url: https://developers.telnyx.com/docs/messaging/messages/appointment-reminder
- url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
- url: https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index
- url: https://developers.telnyx.com/docs/messaging/messages/error-codes/index
- url: https://developers.telnyx.com/docs/messaging/messages/geomatch
- url: https://developers.telnyx.com/docs/messaging/messages/group-messaging
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/index
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/internal-transfer
updated_at: 2026-06-11T10:36:31Z
---

# Telnyx Messaging

*Part 1 of 4 — see also: [Part 2](telnyx-messaging--part-2.md), [Part 3](telnyx-messaging--part-3.md), [Part 4](telnyx-messaging--part-4.md)*

Telnyx Messaging provides a comprehensive API for sending and receiving SMS and MMS messages, with features including messaging profiles, alphanumeric sender IDs, geomatching, group messaging, two-factor authentication, appointment reminders, advanced opt-in/out handling, configurable spend limits, hosted SMS, and detailed error handling.

## Configuration and Usage Basics

Messaging features are configured primarily using **Messaging Profiles**. You can set up several messaging profiles to differentiate between use cases. Enable messaging on a phone number by assigning it to a Messaging Profile; multiple phone numbers can be assigned to the same profile. Additional configuration, including setting webhooks, is available via the HTTP API using an API Key.

### Queuing and Throttling

If you send more messages than your rate limit allows, messages are held in a queue. If the queue time exceeds 4 hours, the message is immediately rejected.

Proper throttling is important to limit the risk of having SMS messages flagged as spam. US long code numbers are restricted to 10 messages per minute per long code. By default, Telnyx Portal accounts are limited to 1 message per second; contact [sales@telnyx.com](mailto:sales@telnyx.com) for higher limits. If you create messages at a faster rate, Telnyx queues them and sends at a reduced rate. Queued (not yet sent) messages do not appear in MDR reports.

### Characters and Encoding

- Multi-part messaging is allowed. Each part has a 160-character limit in the GSM 7-bit character set.
- Characters outside GSM 7-bit switch encoding to UTF-16, limiting each message to 70 characters.
- Spaces and commas count as characters. Messages exceeding 160 characters are separated into, and billed as, multiple messages. The mobile operator may combine them into a single message on the recipient's device.

### Default Auto-Responses

If a mobile user sends certain keywords (case-insensitive, surrounding whitespace-insensitive), that number is blocked from receiving further SMS from the account:

| Keyword | Action |
|---|---|
| `STOP`, `STOPALL`, `STOP ALL`, `UNSUBSCRIBE`, `CANCEL`, `END`, `QUIT` | Block messages |
| `START`, `UNSTOP` | Remove block |

### Glossary

| Term | Definition |
|---|---|
| MDR | Message Detail Record — details information about a specific message sent from or received on a Telnyx phone number. |
| Messaging Profile | Configures messaging settings on one or more messaging-enabled phone numbers. |
| Messaging-Capable | A phone number that could be used for text messaging. |
| Messaging-Enabled | A phone number ready and able to send and receive messages. |
| Alphanumeric Sender ID | A sender value used in place of a phone number; outbound only, 1–11 characters, must contain at least one letter. |
| Webhook | An HTTP callback used to send notifications to your server for inbound messages and delivery status updates. |

## Alphanumeric Sender ID

Alphanumeric Sender IDs let you send SMS using a custom text identifier (e.g., your brand name) instead of a phone number, making messages instantly recognizable. They are **one-way only** — recipients cannot reply.

### Format Requirements

| Requirement | Value |
|---|---|
| Length | 1–11 characters |
| Allowed characters | Letters (A-Z, a-z), numbers (0-9), spaces |
| Must contain | At least one letter |

Alphanumeric senders **cannot send to the United States, Canada, or Puerto Rico**. Use a long code or toll-free number for these destinations, or configure a **fallback long code** on your messaging profile — Telnyx will automatically use it for restricted destinations.

### Prerequisites

- A Telnyx account with Level 2 verification
- A Messaging Profile configured with your alphanumeric sender ID
- An API key

Some countries require sender ID pre-registration.

### Rate Limits

| Account Level | Rate Limit |
|---|---|
| Level 1 (unverified) | 6 messages/minute |
| Level 2 (verified) | 60 messages/minute |

### Failover Behavior

If alphanumeric delivery fails, Telnyx attempts to use a configured US fallback long code, or may use a generic alphanumeric sender ID to complete delivery.

### Common Errors

| Error | Cause | Solution |
|---|---|---|
| `InvalidFromAddress` | Invalid sender format | Use 1–11 characters with at least one letter |
| `AlphaSenderNotConfigured` | No alphanumeric sender on profile | Configure sender ID on your messaging profile |
| `UnsupportedDestination` | Sending to US/CA/PR | Use a long code or configure a fallback number |

## Geomatch

Geomatch automatically selects sender numbers that share the same area code as your recipients, boosting trust and engagement. It is part of **Number Pool** settings — you must have Number Pool enabled.

Geomatch currently supports only **NANP numbers** (US, Canada, Caribbean). International numbers do not participate in geomatching.

### How It Works

1. Your app sends a message without specifying a `from` number (using Number Pool)
2. Telnyx identifies the recipient's area code
3. Telnyx searches your number pool for a matching area code
4. If found, that number is used; otherwise a number with a different area code is selected

### Configuration

Enable Geomatch by updating your Messaging Profile's `number_pool_settings`:

```
curl -X PATCH "https://api.telnyx.com/v2/messaging_profiles/YOUR_PROFILE_ID" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"number_pool_settings": {"long_code_weight": 1, "geomatch": true}}'
```

### Selection Priority

When both Geomatch and Sticky Sender are enabled:

1. **Sticky mapping exists** — use the mapped sender (geomatch ignored)
2. **No mapping + matching area code available** — use geomatched number, create sticky mapping
3. **No mapping + no matching area code** — use any available number, create sticky mapping

For effective geomatching, ensure your number pool covers area codes where your recipients are located. Use the Phone Numbers API to audit coverage.

## Group Messaging

Send group MMS messages to multiple recipients in a single API call via the `/v2/messages/group_mms` endpoint. All participants can see and reply to each other.

### Constraints

- Maximum **8 recipients** per conversation (plus the sender)
- **MMS protocol only** — all messages billed at MMS rates
- **US and Canada destinations only**
- Requires **v2 webhook version** on your messaging profile
- Charged **per recipient** — standard MMS rates plus carrier passthrough fees apply

### Receiving Group Messages

When someone replies, you receive a `message.received` webhook with a `cc` field listing all other participants:

| Field | Description |
|---|---|
| `from.phone_number` | The participant who sent the reply |
| `to` | Your Telnyx number(s) in the conversation |
| `cc` | All other participants in the group conversation |

### Delivery Tracking

Group messages generate individual webhook events and detail records for each recipient. A `group_message_id` correlates all individual records back to the original group message. Handset delivery confirmation is not available for non-Telnyx recipients — their status shows as `unknown`.
