---
title: Telnyx Messaging Setup and Configuration Guide
summary: This page consolidates Telnyx support documentation covering SMS setup, sending,
  and advanced messaging features. It includes guidance on SMPP, number pooling, alphanumeric
  sender IDs, hosted SMS, Postman-based API testing, Python SDK usage, and third-party
  integrations such as Easy Text Marketing.
sources:
- url: https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide
- url: https://support.telnyx.com/en/articles/3154822-number-pooling
- url: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman
- url: https://support.telnyx.com/en/articles/4353862-creating-postman-collection-from-openapi
- url: https://support.telnyx.com/en/articles/4371498-sending-alphanumeric-sms-sender-id
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
- url: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id
- url: https://support.telnyx.com/en/articles/6986625-easy-text-marketing-and-telnyx-integration
updated_at: 2026-08-05T13:34:18Z
---

# Telnyx Messaging Setup and Configuration Guide

*Part 2 of 4 — see also: [Part 1](telnyx-messaging-setup-and-configuration-guide--part-1.md), [Part 3](telnyx-messaging-setup-and-configuration-guide--part-3.md), [Part 4](telnyx-messaging-setup-and-configuration-guide--part-4.md)*

This page consolidates Telnyx support documentation covering SMS setup, sending, and advanced messaging features. It includes guidance on SMPP, number pooling, alphanumeric sender IDs, hosted SMS, Postman-based API testing, Python SDK usage, and third-party integrations such as Easy Text Marketing.

## Alphanumeric Sender ID

[Alphanumeric Sender ID](https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id) allows you to set your company name or brand as the Sender ID when sending one-way SMS messages to international destinations. Alphanumeric Sender IDs must be between 3 and up to 11 characters in length. Accepted characters include both upper- and lowercase ASCII letters, the digits 0 through 9, and space: A-Z, a-z, 0-9. They may not be only numbers.

The Alphanumeric Sender ID can be set dynamically on the POST request to the API when sending an SMS by setting a valid alphanumeric ID in the FROM field. Your account must be verified to Level 2 in order to use this feature. At this time, alphanumeric is not supported by the carriers in the US or Canada.

### Sending Alphanumeric SMS via API v1

1. Open Postman and POST to `https://sms.telnyx.com/messages`.
2. In Headers, set `x-profile-secret` to the secret under your Messaging Profile.
3. In the Body, paste the following:

```
{
"from": "Alphanumeric_id",
"to": "+1[intended recipient]",
"body": "Hello World"
}
```

### Sending Alphanumeric SMS via API v2

You can send one-way alphanumeric messages via [API V2](https://developers.telnyx.com/api/messaging/send-message).

Example:

```
curl --location --request POST 'https://api.telnyx.com/v2/messages' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer KEYXXX' \
--data-raw '{
"from": "MyCompany",
"to": "+destination_number",
"messaging_profile_id": "abcdefghi-35bc-4c53-aa60-515de9de707c",
"text": "Hello World!",
"webhook_url": "for real time updates"
}'
```

### Global Alphanumeric Sender ID Capabilities

Depending on the destination, Alphanumeric Sender IDs may be maintained, overwritten to ensure delivery, or require pre-registration. Telnyx allows customers to always submit using an Alphanumeric Sender ID and will make any necessary adjustments to ensure delivery. The full country-by-country table is available in the [Alphanumeric Sender ID](alphanumeric-sender-id.md) article.

To request Alphanumeric Sender ID registration, your account must go through the [Level 2 verification](https://support.telnyx.com/en/articles/1130595-account-verification#level-2) process. Additional restrictions may apply depending on the destination country (use case, minimum volume, company location). To register an Alphanumeric Sender ID, contact [alpha_sender_id@telnyx.com](mailto:alpha_sender_id@telnyx.com) with the country or countries, estimated monthly volume, and a brief description of your use case.
