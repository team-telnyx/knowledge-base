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

*Part 4 of 6 — see also: [Part 1](messaging-profiles--part-1.md), [Part 2](messaging-profiles--part-2.md), [Part 3](messaging-profiles--part-3.md), [Part 5](messaging-profiles--part-5.md), [Part 6](messaging-profiles--part-6.md)*

A messaging profile is the central configuration object for Telnyx messaging. It groups phone numbers, defines webhook URLs, and controls features such as number pooling, smart encoding, MMS transcoding, MMS-to-SMS fallback, spend limits, and URL shortening. Every phone number used for messaging must be assigned to a messaging profile.

## URL Shortening

Automatically shorten URLs in outbound messages. Shortened URLs use your configured domain and track click-through rates.

| Setting | Description |
| --- | --- |
| `url_shortener_settings.domain` | Custom domain for shortened URLs |
| `url_shortener_settings.prefix` | URL prefix |
| `url_shortener_settings.replace_blacklist_only` | Only replace blacklisted URLs |
| `url_shortener_settings.send_webhooks` | Send click-tracking webhooks |
