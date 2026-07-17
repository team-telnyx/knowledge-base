---
title: Telnyx Messaging
summary: Telnyx Messaging is a unified API for application-to-person (A2P) messaging
  across 10DLC long codes, toll-free numbers, short codes, alphanumeric sender IDs,
  RCS, and WhatsApp. This page covers sender type selection, messaging profiles, phone
  number configuration, 10DLC and toll-free registration, campaign management, message
  encoding, MMS, rate limiting, number pooling, opt-in/opt-out compliance, webhooks,
  error codes, spend limits, RCS, WhatsApp Business messaging, hosted SMS, international
  compliance, and common use cases like 2FA and appointment reminders.
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
- url: https://developers.telnyx.com/docs/messaging/messages/2fa/index
- url: https://developers.telnyx.com/docs/messaging/messages/advanced-opt-in-out/index
- url: https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id/index
- url: https://developers.telnyx.com/docs/messaging/messages/appointment-reminder
- url: https://developers.telnyx.com/docs/messaging/messages/chat-sdk-adapter
- url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
- url: https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index
- url: https://developers.telnyx.com/docs/messaging/messages/error-codes/index
- url: https://developers.telnyx.com/docs/messaging/messages/geomatch
- url: https://developers.telnyx.com/docs/messaging/messages/group-messaging
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/index
- url: https://developers.telnyx.com/docs/messaging/messages/hosted-sms/internal-transfer
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
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-capabilities/index
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-deeplinks
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started/index
- url: https://developers.telnyx.com/docs/messaging/messages/receive-message
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-rcs-webhooks/index
- url: https://developers.telnyx.com/docs/messaging/messages/receiving-webhooks/index
- url: https://developers.telnyx.com/docs/messaging/messages/schedule-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-an-rcs-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-receive-mms/index
- url: https://developers.telnyx.com/docs/messaging/messages/short-code/index
- url: https://developers.telnyx.com/docs/messaging/messages/smart-encoding/index
- url: https://developers.telnyx.com/docs/messaging/messages/smil-template
- url: https://developers.telnyx.com/docs/messaging/messages/sticky-sender/index
- url: https://developers.telnyx.com/docs/messaging/messages/url-shortening/index
- url: https://developers.telnyx.com/docs/messaging/messages/zapier-integration
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/index
- url: https://developers.telnyx.com/docs/messaging/toll-free-verification/troubleshooting
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup
- url: https://developers.telnyx.com/docs/messaging/whatsapp/embedded-signup/tech-provider
- url: https://developers.telnyx.com/docs/messaging/whatsapp/manage-templates
- url: https://developers.telnyx.com/docs/messaging/whatsapp/quickstart/index
- url: https://developers.telnyx.com/docs/messaging/whatsapp/send-messages/index
updated_at: 2026-07-17T09:15:02Z
---

# Telnyx Messaging

*Part 3 of 5 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 2](telnyx-messaging--part-2.md), [Part 4](telnyx-messaging--part-4.md), [Part 5](telnyx-messaging--part-5.md)*

Telnyx Messaging is a unified API for application-to-person (A2P) messaging across 10DLC long codes, toll-free numbers, short codes, alphanumeric sender IDs, RCS, and WhatsApp. This page covers sender type selection, messaging profiles, phone number configuration, 10DLC and toll-free registration, campaign management, message encoding, MMS, rate limiting, number pooling, opt-in/opt-out compliance, webhooks, error codes, spend limits, RCS, WhatsApp Business messaging, hosted SMS, international compliance, and common use cases like 2FA and appointment reminders.

## Message Encoding

SMS messages are encoded into segments of 140 bytes each.

| Encoding | Bits/Char | Single Segment | Multi-Part Segment |
| --- | --- | --- | --- |
| GSM 7-bit | 7 | 160 chars | 153 chars |
| ASCII 7-bit | 7 | 160 chars | 153 chars |
| ASCII 8-bit | 8 | 140 chars | 134 chars |
| UTF-16 | 16 | 70 chars | 67 chars |

A single non-GSM-7 character (like an emoji or curly quote) switches the entire message to UTF-16, cutting capacity from 160 to 70 characters per segment.

### Smart Encoding

Smart encoding automatically replaces Unicode characters with visually similar GSM-7 characters, keeping messages in the more efficient GSM-7 encoding. Enable it on a messaging profile or per-request using the `encoding` parameter (`auto`, `gsm7`, or `ucs2`).

## MMS

MMS is supported on Long Code, Toll-Free, and Short Code numbers in the US and Canada. Include `media_urls` in your message request to send MMS. You can send up to 10 media files per message.

### Carrier Size Limits

| Carrier | Long Code | Toll-Free | Short Code |
| --- | --- | --- | --- |
| AT&T | 1 MB | 600 KB | 600 KB |
| T-Mobile | 1.5 MB | 600 KB | 1 MB |
| Verizon | 1 MB | 600 KB | 1.2 MB |

The safe maximum across all carriers and sender types is 600 KB. Enable `mms_transcoding` on your messaging profile to automatically resize oversized media.

### MMS Converter

When enabled on a messaging profile via `mms_fall_back_to_sms`, MMS messages are converted to SMS for destinations that don't support MMS. Media URLs appear on their own line after the message body.

## Rate Limiting

### Account-Level Limits

| Message Type | Default Rate Limit | Max Queue Length |
| --- | --- | --- |
| SMS | 50 messages/second | 720,000 |
| MMS | 15 messages/second | 216,000 |
| RCS | 1 message/second | 14,400 |

### Sender-Level Limits

| Sender Type | Rate Limit | Per | Max Queue Length |
| --- | --- | --- | --- |
| Long Code | 0.1 MPS | Number | 1,440 |
| Toll-Free | 20 MPS | Number | 288,000 |
| Short Code | 1,000 MPS | Number | 14,400,000 |
| Alphanumeric | 0.1 MPS | Sender ID | 1,440 |

When you exceed rate limits, excess messages are queued for up to 4 hours. When a queue is full, additional messages return error code `40318`.

## Number Pool

Number Pool automatically distributes outbound messages across multiple phone numbers. Enable it on a messaging profile by setting `number_pool_settings`:

| Parameter | Description |
| --- | --- |
| `long_code_weight` | Weight for long code selection (0 removes from pool) |
| `toll_free_weight` | Weight for toll-free selection (0 removes from pool) |
| `skip_unhealthy` | Skip numbers with poor delivery rates |
| `sticky_sender` | Reuse same number for recipient when possible |
| `geomatch` | Match sender to recipient's geographic area |

Weights are ratios, not percentages. With `long_code_weight: 5` and `toll_free_weight: 1`, approximately 5 out of every 6 messages use a long code.

### Sticky Sender

Maintains the same sender number for each recipient. Mappings expire after 8 days of no messages. Priority order: Sticky Sender → Geomatch → Weight distribution → Skip unhealthy.

### Geomatch

Selects a sender number matching the recipient's area code. Supports NANP numbers only (US, Canada, Caribbean). Requires Number Pool to be enabled.

## Opt-In/Opt-Out Management

### Default Behavior

Telnyx handles standard opt-in/out keywords automatically. Block rules operate at the messaging profile level.

**Opt-out keywords:** `STOP`, `STOPALL`, `STOP ALL`, `UNSUBSCRIBE`, `CANCEL`, `END`, `QUIT`

**Opt-in keywords:** `START`, `UNSTOP`

### Custom Auto-Responses

Configure custom keyword responses per country using ISO 3166-1 alpha-2 codes via the `autoresp_configs` endpoint. Default operations (`start`, `stop`, `help`) require a minimum 20 characters for the auto-response message. Each configuration supports a maximum of 20 trigger keywords.

### Toll-Free Limitations

Toll-free numbers have a separate carrier-level opt-out system. The carrier sends its own auto-reply ("NETWORK MSG") that cannot be customized or removed.

## Webhooks

### Webhook URL Hierarchy

1. Per-message URLs (`webhook_url` and `webhook_failover_url` in the send request)
2. Messaging profile URLs
3. No webhook (events still available in Message Detail Records)

### Event Types

| Event | Trigger | Direction |
| --- | --- | --- |
| `message.received` | Inbound SMS/MMS arrives | Inbound |
| `message.sent` | Outbound message accepted by carrier | Outbound |
| `message.finalized` | Terminal delivery state reached | Outbound |

### Delivery Statuses

| Status | Description |
| --- | --- |
| `queued` | Message accepted and queued |
| `sent` | Delivered to carrier gateway |
| `delivered` | Carrier confirmed delivery to handset |
| `failed` | Delivery failed |
| `gw_timeout` | No response from gateway |
| `dlr_timeout` | No delivery receipt from carrier |

### Retry Policy

- Timeout: 2 seconds (API v2)
- Retries: Up to 3 attempts per URL with exponential backoff
- Failover: If all retries fail, Telnyx tries the failover URL
- Total attempts: Up to 6 (3 primary + 3 failover)

### Signature Verification

All webhooks are signed using Ed25519 public key cryptography. Each request includes `telnyx-signature-ed25519` and `telnyx-timestamp` headers. The signature is computed over `{timestamp}|{json_payload}`. Reject webhooks where the timestamp is more than 5 minutes old.

### Webhook IP Allowlist

`192.76.120.192/27`

## 10DLC Event Notifications

Configure webhooks for brand, campaign, and phone number lifecycle events.

### Brand Events

| Payload Type | Description |
| --- | --- |
| `REGISTRATION` | Failures during registration |
| `REVET` | Revetting request result |
| `ORDER_EXTERNAL_VETTING` | Vetting order status |
| `TCR_BRAND_UPDATE` | Notifications from TCR |

### Campaign Events

| Payload Type | Description |
| --- | --- |
| `REGISTRATION` | Registration failures |
| `TELNYX_REVIEW` | Telnyx compliance review (`ACCEPTED`/`REJECTED`) |
| `NUMBER_POOL_PROVISIONED` | Number pool provisioned |
| `NUMBER_POOL_DEPROVISIONED` | Number pool deprovisioned |
| `TCR_EVENT` | TCR notifications |
| `MNO_REVIEW` | MNO/DCA review results |
| `TELNYX_EVENT` | System events (e.g., `DORMANT` for suspension) |
| `VERIFIED` | Campaign fully provisioned with MNOs |

### Phone Number Events

| Payload Type | Description |
| --- | --- |
| `ASSIGNMENT` | Phone number assignment process |
| `DELETION` | Phone number removal process |
| `STATUS_UPDATE` | Phone number status changed (`ADDED`, `DELETED`, `PENDING`, `FAILED`) |

### Campaign Appeals

- **Native campaigns:** Use the appeal API endpoint or campaign update to re-enter review.
- **Partner campaigns:** CSP sends a `CAMPAIGN_NUDGE` event to trigger re-review.
