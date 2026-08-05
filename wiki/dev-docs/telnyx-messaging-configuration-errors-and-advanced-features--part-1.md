---
title: Telnyx Messaging Configuration, Errors, and Advanced Features
summary: This page consolidates Telnyx messaging configuration guidance, including
  messaging profile setup, configurable spend limits, error code handling, the Vercel
  Chat SDK adapter, and Geomatch for area-code-based sender selection. It covers prerequisites,
  environment variables, webhook setup, capability matrices, and best practices for
  production SMS/MMS workloads.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/chat-sdk-adapter
- url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
- url: https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index
- url: https://developers.telnyx.com/docs/messaging/messages/error-codes/index
- url: https://developers.telnyx.com/docs/messaging/messages/geomatch
updated_at: 2026-08-05T13:55:16Z
---

# Telnyx Messaging Configuration, Errors, and Advanced Features

*Part 1 of 4 — see also: [Part 2](telnyx-messaging-configuration-errors-and-advanced-features--part-2.md), [Part 3](telnyx-messaging-configuration-errors-and-advanced-features--part-3.md), [Part 4](telnyx-messaging-configuration-errors-and-advanced-features--part-4.md)*

This page consolidates Telnyx messaging configuration guidance, including messaging profile setup, configurable spend limits, error code handling, the Vercel Chat SDK adapter, and Geomatch for area-code-based sender selection. It covers prerequisites, environment variables, webhook setup, capability matrices, and best practices for production SMS/MMS workloads.

## Overview

Telnyx messaging is configured primarily through **Messaging Profiles**, which group phone numbers, webhooks, and policy settings. This page consolidates configuration guidance, spend-limit controls, error-code handling, the Vercel Chat SDK adapter, and Geomatch sender selection into a single reference.

## Messaging Configuration and Usage

Messaging features are configured primarily using **Messaging Profiles**. You can set up several messaging profiles to differentiate between use cases. You can enable messaging on a phone number by assigning it to a Messaging Profile, and multiple phone numbers can be assigned to a single profile. Additional configuration, including setting webhooks, is also available using the HTTP API and an API Key. To send messages and retrieve message details for one of your phone numbers, use the HTTP API.

### Queuing

If you send more messages than your rate limit allows, messages will be held in a queue. If the queue time is more than 4 hours, the message is immediately rejected.

### Throttling

- Proper throttling is important to limit the risk of having SMS messages flagged as SPAM. US long code numbers are restricted to sending 10 messages per minute for any single long code. If you require faster throughput, you must purchase more long codes. Ignoring these recommendations can result in mobile operators blocking your numbers.
- By default, your Telnyx Portal account is limited to sending one message per second. If you require a higher limit, contact [sales@telnyx.com](mailto:sales@telnyx.com).
- If you create messages at a faster rate, Telnyx queues the messages and sends them at a reduced rate. Messages that are queued (and not yet sent) do not appear in the MDR reports.

### Characters

- Multi-part messaging is allowed.
- Each part has a 160-character limitation when using the GSM 7-bit character set.
- If using characters outside of GSM 7-bit, encoding switches to UTF-16, which limits the message to 70 characters.
- Spaces and commas are counted as characters.
- If the message contains more than 160 characters it is separated into, and billed as, multiple messages. The mobile operator may combine into a single message on the recipient's device.

### Auto-Responses

If a mobile user sends a message containing only the following words or phrases (case-insensitive, surrounding whitespace-insensitive) to one of our numbers via SMS, that number and the account will be blocked from sending SMS to the mobile number. The customer will receive an HTTP 409 if they try:

- Cancel
- End
- Stop
- Stopall
- Stop all
- Quit
- Unsubscribe

To unblock the customer, the mobile user must send the blocked number one of the following words or phrases (case-insensitive, surrounding whitespace-insensitive):

- Start
- Unstop

### Glossary

| Term | Definition |
| --- | --- |
| MDR | A Message Detail Record (MDR) details information about a specific message that you sent from, or received on, a Telnyx phone number. |
| Messaging Profile | Used to configure messaging settings on one or more of your Telnyx messaging-enabled phone numbers. |
| Messaging-Capable | A phone number that *could* be used for text messaging. If a phone number is messaging-capable but is *not* messaging-enabled, first check that it is assigned to a messaging profile, and then that the profile is enabled. |
| Messaging-Enabled | A phone number that is ready and able to send and receive messages. All messaging-enabled phone numbers are messaging-capable. |
| Alphanumeric Sender ID | A sender value that can be used in place of a phone number. Alphanumeric Sender IDs can only be used for outbound messages; it is not possible to receive messages on an Alphanumeric Sender ID. They are also not supported for all destinations, in which case the sender might be substituted with a different value. An Alphanumeric Sender ID must be 1–11 characters in length, can only contain Latin letters, numbers, and spaces, and must contain at least one letter. |
| Webhook | An HTTP callback used to send notifications to your server. Can be used to receive inbound text messages and also delivery status updates for outbound text messages. |

## Configurable Spend Limits

Messaging profiles can be configured with a daily spending limit to prevent unexpected costs from bugs, traffic spikes, or human error. When the limit is reached, outbound messages are rejected until the limit resets at midnight UTC.

### Set Up Spend Limits

Enable the `daily_spend_limit_enabled` flag and set a `daily_spend_limit` value (in USD) on your messaging profile:

```
curl -X PATCH https://api.telnyx.com/v2/messaging_profiles/{profile_id} \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{
    "daily_spend_limit_enabled": true,
    "daily_spend_limit": "10.00"
  }'
```

The `daily_spend_limit` value is a string representing USD (e.g., `"0.50"`, `"10.00"`, `"100.00"`). It applies per messaging profile — use separate profiles for different budgets.

### When the Limit Is Reached

Once spending exceeds the configured limit, Telnyx:

1. Rejects new messages with HTTP `429` and error code `40333`
2. Sends a webhook to your configured URL
3. Sends an email notification to your account

Error response:

```
{
  "errors": [
    {
      "code": "40333",
      "title": "Messaging profile spend limit reached",
      "detail": "The daily spend limit configured on this messaging profile has been reached",
      "meta": {
        "url": "https://developers.telnyx.com/docs/overview/errors/40333"
      }
    }
  ]
}
```

Webhook payload:

```
{
  "data": {
    "event_type": "messaging-profile.spend-limit-reached",
    "id": "d21a2887-8007-4bb6-bd7d-f2874829918e",
    "occurred_at": "2024-08-20T19:17:08.918+00:00",
    "payload": {
      "configured_limit": "10.00",
      "current_cost": "10.02",
      "profile_id": "be3eb60a-a346-470a-886c-ab4e421711bd"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "https://example.com/webhook-url"
  }
}
```

There may be a short delay between reaching the limit and enforcement. A small number of additional messages may be sent during this window, causing `current_cost` to slightly exceed `configured_limit`.

### Reset and Override

The running spend total resets automatically at **midnight UTC** each day. After reset, messages can be sent until the limit is exceeded again. Changing the `daily_spend_limit` or `daily_spend_limit_enabled` values does **not** reset the running total — only the midnight UTC reset clears accumulated spend.

To send urgent messages after hitting the limit, temporarily disable the limit, send the messages, then re-enable. Re-enabling does **not** reset the counter; if you were at the limit, re-enabling will immediately block again. Either increase the limit or wait for the midnight UTC reset.

Raising the `daily_spend_limit` takes effect immediately and allows more messages until the new limit is reached.

### Best Practices

1. Set limits on all production profiles to prevent runaway costs from application bugs or compromised API keys.
2. Use separate profiles for different use cases (transactional vs. marketing), each with appropriate limits.
3. Always handle the `messaging-profile.spend-limit-reached` webhook to alert your team immediately.
4. Build in error handling for `40333` — queue messages for later delivery or switch to a backup profile.
5. Review limits regularly as messaging volume grows to avoid unexpected blocks during peak periods.
