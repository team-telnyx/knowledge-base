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

*Part 5 of 5 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 2](telnyx-messaging--part-2.md), [Part 3](telnyx-messaging--part-3.md), [Part 4](telnyx-messaging--part-4.md)*

Telnyx Messaging is a unified API for application-to-person (A2P) messaging across 10DLC long codes, toll-free numbers, short codes, alphanumeric sender IDs, RCS, and WhatsApp. This page covers sender type selection, messaging profiles, phone number configuration, 10DLC and toll-free registration, campaign management, message encoding, MMS, rate limiting, number pooling, opt-in/opt-out compliance, webhooks, error codes, spend limits, RCS, WhatsApp Business messaging, hosted SMS, international compliance, and common use cases like 2FA and appointment reminders.

## Common Use Cases

### Two-Factor Authentication (2FA)

Generate cryptographically secure OTPs (6 digits, 3–5 minute expiry, max 3 attempts). Use constant-time comparison to prevent timing attacks. Rate limit: 1 OTP per phone per 60 seconds, 10 per IP per hour. Consider the [Verify API](verify-api.md) for managed OTP with built-in retry logic and multi-channel support.

### Appointment Reminders

Send reminders 24 hours before appointments (primary) and 2–3 hours before (final). Respect recipient time zones — only send between 9 AM and 8 PM local time. Use scheduled messages or cron-based job scheduling.

## Related Resources

- [10DLC Brand Registration](10dlc-brand-registration.md)
- [10DLC Campaign Registration](10dlc-campaign-registration.md)
- [10DLC Rate Limits & Throughput](10dlc-rate-limits-throughput.md)
- [10DLC Event Notifications](10dlc-event-notifications.md)
- [10DLC Troubleshooting Guide](10dlc-troubleshooting-guide.md)
- [Sole Proprietor 10DLC Registration](sole-proprietor-10dlc-registration.md)
- [ISV & Reseller 10DLC Onboarding](isv-reseller-10dlc-onboarding.md)
- [Messaging Profiles Overview](messaging-profiles-overview.md)
- [Number Pool](number-pool.md)
- [Sticky Sender](sticky-sender.md)
- [Geomatch](geomatch.md)
- [Smart Encoding](smart-encoding.md)
- [Configurable Spend Limits](configurable-spend-limits.md)
- [Advanced Opt-In/Out Management](advanced-opt-in-out-management.md)
- [Message Detail Records](message-detail-records.md)
- [Messaging Error Code Reference](messaging-error-code-reference.md)
- [Toll-Free Verification](toll-free-verification.md)
- [Toll-Free Verification Troubleshooting](toll-free-verification-troubleshooting.md)
- [Short Codes](short-codes.md)
- [RCS Getting Started](rcs-getting-started.md)
- [RCS Capabilities & Deeplinks](rcs-capabilities-deeplinks.md)
- [WhatsApp Quickstart](whatsapp-quickstart.md)
- [WhatsApp Embedded Signup](whatsapp-embedded-signup.md)
- [WhatsApp Tech Provider Embedded Signup](whatsapp-tech-provider-embedded-signup.md)
- [Manage WhatsApp Message Templates](manage-whatsapp-message-templates.md)
- [Send WhatsApp Messages](send-whatsapp-messages.md)
- [International SMS Compliance Guide](international-sms-compliance-guide.md)
- [Hosted SMS](hosted-sms.md)
- [Internal Hosted SMS Transfer](internal-hosted-sms-transfer.md)
