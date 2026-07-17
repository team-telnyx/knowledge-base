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

*Part 4 of 5 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 2](telnyx-messaging--part-2.md), [Part 3](telnyx-messaging--part-3.md), [Part 5](telnyx-messaging--part-5.md)*

Telnyx Messaging is a unified API for application-to-person (A2P) messaging across 10DLC long codes, toll-free numbers, short codes, alphanumeric sender IDs, RCS, and WhatsApp. This page covers sender type selection, messaging profiles, phone number configuration, 10DLC and toll-free registration, campaign management, message encoding, MMS, rate limiting, number pooling, opt-in/opt-out compliance, webhooks, error codes, spend limits, RCS, WhatsApp Business messaging, hosted SMS, international compliance, and common use cases like 2FA and appointment reminders.

## Error Codes

### Delivery Errors (40xxx)

| Code | Error | Action |
| --- | --- | --- |
| `40001` | Not routable | Verify recipient can receive SMS/MMS |
| `40002` | Blocked as spam (temporary) | Reduce sending rate |
| `40003` | Blocked as spam (permanent) | Use different sending number |
| `40010` | Not 10DLC registered | Register for 10DLC |
| `40016` | T-Mobile sending limit | Reduce rate or improve vetting |
| `40017` | AT&T spam rejection | Review content |
| `40018` | AT&T sending limit | Reduce rate or improve vetting |
| `40020` | Artificial traffic inflation | Wait 24 hours |

### API Request Errors (403xx)

| Code | Error | Action |
| --- | --- | --- |
| `40300` | Blocked (STOP) | Do not retry |
| `40305` | Invalid 'from' address | Assign number to messaging profile |
| `40310` | Invalid 'to' address | Verify E.164 format |
| `40318` | Queue full | Back off and retry |
| `40333` | Spend limit reached | Increase limit or wait for reset |

### Retriable vs Permanent

| Category | Codes | Action |
| --- | --- | --- |
| Auto-retriable | `40006`, `40008` | Retry with exponential backoff |
| Retriable after intervention | `40002`, `40005`, `40011`, `40014`, `40016`, `40017`, `40018`, `40318` | Fix rate/content before retrying |
| Temporary hold | `40020`, `40320` | Wait |
| Permanent | `40001`, `40003`, `40010`, `40300`, `40314`, `40322` | Do not retry |

## Spend Limits

Messaging profiles can be configured with a daily spending limit. When the limit is reached:

- New messages are rejected with HTTP 429 and error code `40333`
- A `messaging-profile.spend-limit-reached` webhook is sent
- An email notification is sent to your account

The running spend total resets automatically at midnight UTC each day.

## RCS Messaging

RCS delivers app-like experiences in the native messaging app with rich cards, carousels, suggested replies, read receipts, and typing indicators. Currently supported on Android devices; Apple announced RCS support in iOS 18.

### Approval Process

RCS requires agent registration and carrier approval (typically 4–6 weeks). During the testing stage, you can invite beta test numbers to test your integration.

### RCS Capabilities

Check whether a recipient's device supports RCS before sending:

| Feature | Use For |
| --- | --- |
| `RICHCARD_STANDALONE` | Single rich card support |
| `RICHCARD_CAROUSEL` | Swipeable carousel cards |
| `ACTION_OPEN_URL` | Open URL button |
| `ACTION_DIAL` | Phone call button |
| `ACTION_VIEW_LOCATION` | View map location |
| `ACTION_CREATE_CALENDAR_EVENT` | Add calendar event |

### RCS Webhooks

RCS webhooks differ structurally from SMS/MMS:

- Message body is nested under `payload.body.text` (not `payload.text`)
- Media is under `payload.body.user_file` with GCS URLs
- Read receipts are supported via `message.read` events
- Inbound messages route via the RCS Agent's webhook URL; outbound status via messaging profile

## WhatsApp Business Messaging

### Embedded Signup

Connect your Facebook Business Manager to Telnyx and provision WhatsApp Business Account (WABA) resources through a browser-based workflow. The process progresses through states: `initiated` → `facebook_auth` → `waba_created` → `phone_registered` → `verified`.

### Tech Provider Embedded Signup

ISVs and SaaS platforms can embed Meta's WhatsApp onboarding flow directly into their own portal. Two integration paths:

- **Hosted signup (recommended):** Telnyx manages the signup UI and backend processing. Generate a time-limited onboarding URL via `POST /v2/whatsapp/hosted_signups`.
- **Custom integration:** Embed Meta's Facebook SDK directly for full control over the UX.

### Message Templates

WhatsApp requires pre-approved templates for business-initiated conversations. Templates must be approved by Meta (typically 24–48 hours).

**Template categories:**

| Category | Use Case | Pricing Tier |
| --- | --- | --- |
| `AUTHENTICATION` | OTP codes, login verification | Lowest |
| `UTILITY` | Order updates, shipping, account alerts | Medium |
| `MARKETING` | Promotions, newsletters, product launches | Highest |

### Sending Messages

All message types use `POST /v2/messages/whatsapp`. The `whatsapp_message` object determines the message type. Supported types: `text`, `template`, `image`, `video`, `document`, `audio`, `sticker`, `location`, `contacts`, `interactive`, `reaction`.

Text, media, and interactive messages can only be sent within a 24-hour conversation window. Outside this window, use an approved template message.

## Hosted SMS

Hosted SMS lets you add messaging capabilities to phone numbers that stay with your current voice provider. Your existing voice service continues uninterrupted — Telnyx handles only SMS/MMS routing.

**Process:** Eligibility check → Create order → Verify ownership via SMS code → Upload LOA and recent provider bill → Telnyx review (1–3 business days).

### Internal Hosted SMS Transfer

Move messaging-enabled numbers between two Telnyx accounts without going through the standard carrier porting process. The current owner has 72 hours to approve or reject; auto-approval occurs if no action is taken. When a number is internally transferred, any 10DLC campaign registrations are automatically deleted.

## Alphanumeric Sender ID

Send SMS using a custom text identifier (1–11 characters, letters/numbers/spaces, must contain at least one letter) instead of a phone number. One-way only — recipients cannot reply.

**Rate limits:** Level 1 (unverified): 6 messages/minute. Level 2 (verified): 60 messages/minute.

Alphanumeric senders cannot send to the US, Canada, or Puerto Rico. Configure a fallback long code for these destinations.

## International SMS Compliance

### Sender ID Types by Country

| Country | Alphanumeric | Long Code | Short Code | Pre-Registration |
| --- | --- | --- | --- | --- |
| United States | No | Yes (10DLC) | Yes | 10DLC required |
| Canada | No | Yes | Yes | Short code approval |
| United Kingdom | Yes | Yes | Yes | Recommended |
| Germany | Yes | Yes | Yes | No |
| France | Yes | Yes | Yes | OACP required |
| India | Yes (registered) | No | No | DLT mandatory |
| Australia | Yes | Yes | Yes | Sender ID registration |
| Brazil | Yes | Yes | Yes | No |
| Mexico | Yes | Yes | Yes | No |

### India DLT Registration

India requires Distributed Ledger Technology (DLT) registration for all A2P SMS:

1. Entity registration on a DLT platform (JioConnect, Vodafone DLT, Airtel DLT, or BSNL DLT)
2. Header (sender ID) registration
3. Template registration — every message template must be pre-approved
4. Content category — transactional, promotional, or service

Promotional messages to users on the Do Not Disturb (DND) registry will be blocked. Promotional messages are restricted to 9 AM – 9 PM IST.

## URL Shortening

Telnyx provides custom URL shortening to improve brand awareness and bypass spam filters. By default, only URLs from a supported blacklist (bit.ly, tinyurl, etc.) are converted. Disable `replace_blacklist_only` to shorten all domains.

## Zapier Integration

Connect Telnyx SMS to 7,000+ apps without code. Available triggers: "Receive a Message." Available actions: "Send SMS." Limitations include polling delay (up to 15 minutes on free plans), no MMS media support, and no delivery status tracking.

## Vercel Chat SDK Adapter

`@telnyx/chat-sdk-adapter` is the official Telnyx adapter for the Vercel Chat SDK, enabling SMS/MMS bots in Next.js applications. Use a dedicated messaging profile prefixed with `[Chat SDK]` for per-profile analytics, spend limits, and isolated webhook URLs.
