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

*Part 1 of 5 — see also: [Part 2](telnyx-messaging--part-2.md), [Part 3](telnyx-messaging--part-3.md), [Part 4](telnyx-messaging--part-4.md), [Part 5](telnyx-messaging--part-5.md)*

Telnyx Messaging is a unified API for application-to-person (A2P) messaging across 10DLC long codes, toll-free numbers, short codes, alphanumeric sender IDs, RCS, and WhatsApp. This page covers sender type selection, messaging profiles, phone number configuration, 10DLC and toll-free registration, campaign management, message encoding, MMS, rate limiting, number pooling, opt-in/opt-out compliance, webhooks, error codes, spend limits, RCS, WhatsApp Business messaging, hosted SMS, international compliance, and common use cases like 2FA and appointment reminders.

## Overview

Telnyx Messaging is a unified API for application-to-person (A2P) messaging across multiple sender types: 10DLC long codes, toll-free numbers, short codes, alphanumeric sender IDs, RCS, and WhatsApp. The platform handles brand and campaign registration, throughput management, opt-in/opt-out compliance, webhooks, and delivery tracking. This page consolidates the full messaging surface area into a single reference.

## Choosing a Sender Type

Sender type selection depends on use case, destination, volume, and regulatory requirements.

| Sender Type | Throughput | Two-Way | Voice | MMS | Best For |
| --- | --- | --- | --- | --- | --- |
| 10DLC Long Code | 3–75 MPS (vetting-dependent) | Yes | Yes | US/CA | US A2P messaging, local presence |
| Toll-Free | 3–150 MPS | Yes | Yes | US/CA | Customer service, national reach |
| Short Code | 200+ MPS | Yes | No | US/CA | High-volume alerts, 2FA, mass notifications |
| RCS | 100+ MPS | Yes | No | Rich media | Android rich messaging, branded experiences |
| Alphanumeric | 100+ MPS | No | No | No | International one-way branded messaging |

**Key constraints:**

- 10DLC is required for A2P messaging to US mobile numbers (enforced by carriers since 2023).
- Alphanumeric sender IDs cannot send to the US, Canada, or Puerto Rico.
- Toll-free and short code numbers only work for US/CA destinations.
- MMS is supported on long code, toll-free, and short code in the US/CA only.

## Messaging Profiles

A messaging profile is the central configuration object that groups phone numbers, defines webhook URLs, and controls features like number pooling, smart encoding, and spend limits. Every phone number used for messaging must be assigned to a messaging profile.

### Profile Settings

| Setting | Description | Default |
| --- | --- | --- |
| Webhook URL | Where inbound messages and delivery status events are sent | None (required) |
| Number Pool | Distribute messages across multiple numbers automatically | Disabled |
| Sticky Sender | Keep the same sender number for each recipient | Disabled |
| Geomatch | Select sender numbers based on geographic proximity | Disabled |
| Smart Encoding | Replace Unicode characters with GSM-7 equivalents | Disabled |
| MMS Transcoding | Automatically resize media for carrier limits | Disabled |
| Spend Limit | Daily spend cap to prevent unexpected costs | Disabled |
| URL Shortening | Shorten URLs in outbound messages | Disabled |

### Common Configurations

**Transactional (OTP, alerts):**

```json
{
  "name": "Transactional Messages",
  "webhook_url": "https://api.example.com/webhooks/sms",
  "smart_encoding": true,
  "daily_spend_limit_enabled": true,
  "daily_spend_limit": "100.00"
}
```

**Marketing campaigns:**

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

## Phone Number Configuration

Before a phone number can send or receive messages, it must be assigned to a messaging profile and have messaging enabled.

### Messaging Enablement by Number Type

| Number Type | Messaging Ready? | Additional Steps |
| --- | --- | --- |
| Long code (US) | After 10DLC registration | Register brand + campaign |
| Toll-free (US/CA) | After verification | Submit toll-free verification |
| Short code | After provisioning | Short code setup |
| Long code (non-US) | Typically immediate | Check country-specific requirements |
| Alphanumeric sender ID | After registration | Alphanumeric ID setup |

US long codes without 10DLC registration will experience carrier filtering and potential message blocking.
