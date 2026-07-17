---
title: Telnyx Mission Control Account Setup and Messaging
summary: This page covers how to sign up for a Telnyx Mission Control account, configure
  it for voice and messaging, send SMS and Alphanumeric SMS via Postman using API
  v1 and v2, understand global Alphanumeric Sender ID capabilities by country, and
  access useful Mission Control resources.
sources:
- url: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- url: https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman
- url: https://support.telnyx.com/en/articles/4371498-sending-alphanumeric-sms-sender-id
- url: https://support.telnyx.com/en/articles/4404409-resources-on-your-account
- url: https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account
- url: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id
- url: https://support.telnyx.com/en/articles/8219294-messaging-in-mission-control
updated_at: 2026-07-17T09:08:16Z
---

# Telnyx Mission Control Account Setup and Messaging

*Part 3 of 5 — see also: [Part 1](telnyx-mission-control-account-setup-and-messaging--part-1.md), [Part 2](telnyx-mission-control-account-setup-and-messaging--part-2.md), [Part 4](telnyx-mission-control-account-setup-and-messaging--part-4.md), [Part 5](telnyx-mission-control-account-setup-and-messaging--part-5.md)*

This page covers how to sign up for a Telnyx Mission Control account, configure it for voice and messaging, send SMS and Alphanumeric SMS via Postman using API v1 and v2, understand global Alphanumeric Sender ID capabilities by country, and access useful Mission Control resources.

## Sending Alphanumeric SMS

Before sending Alphanumeric SMS, configure your account by purchasing a number, creating a messaging profile, and associating that messaging profile with the number. See [SMS Setup with Postman](sms-setup-with-postman.md) for more details about sending SMS using API v1. See [Alphanumeric Sender ID](alphanumeric-sender-id.md) for Alphanumeric capabilities and [specific error codes](https://developers.telnyx.com/api/errors).

### What is the Alphanumeric Sender ID?

[Alphanumeric Sender ID](https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id) allows you to set your company name or brand as the Sender ID when sending one-way SMS messages to international destinations.

Alphanumeric Sender IDs must be between 3 and up to 11 characters in length. Accepted characters include both upper- and lowercase ASCII letters, the digits 0 through 9, and space: A-Z, a-z, 0-9. They may not be only numbers.

The Alphanumeric Sender ID can be set dynamically on the POST request to the Telnyx API when sending an SMS. Set a valid alphanumeric ID in the `from` field and Telnyx will use it.

Your account must be verified to Level 2 in order to use this feature. At this time, alphanumeric is not supported by the carriers in the US or Canada.

### Sending Alphanumeric SMS via API v1

1. Open Postman. **POST** to `https://sms.telnyx.com/messages`.
2. In **Headers**, set your `x-profile-secret` to the secret under your Messaging Profile.
3. In the **Body**, paste the following:

```
{
"from": "Alphanumeric_id",
"to": "+1[intended recipient]",
"body": "Hello World"
}
```

### Sending Alphanumeric SMS via API v2

You can send one-way alphanumeric messages via [API v2](https://developers.telnyx.com/api/messaging/send-message).

**Example:**

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
