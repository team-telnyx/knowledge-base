---
title: Schedule SMS and MMS Messages
summary: Schedule SMS and MMS messages to send at a specific time in the future using
  the Telnyx messaging API. Use scheduled messaging for appointment reminders, marketing
  campaigns, time-zone-aware notifications, and any scenario where precise delivery
  timing matters.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/schedule-message/index
- url: https://developers.telnyx.com/docs/messaging/messages/send-an-rcs-message/index
updated_at: 2026-08-05T13:56:55Z
---

# Schedule SMS and MMS Messages

*Part 1 of 3 — see also: [Part 2](schedule-sms-and-mms-messages--part-2.md), [Part 3](schedule-sms-and-mms-messages--part-3.md)*

Schedule SMS and MMS messages to send at a specific time in the future using the Telnyx messaging API. Use scheduled messaging for appointment reminders, marketing campaigns, time-zone-aware notifications, and any scenario where precise delivery timing matters.

## Overview

Schedule SMS and MMS messages to send at a specific time in the future. Use scheduled messaging for appointment reminders, marketing campaigns, time-zone-aware notifications, and any scenario where precise delivery timing matters.

## Prerequisites

- A [Telnyx account](https://telnyx.com/sign-up)
- A [Messaging Profile](messaging-profile.md) with an assigned phone number
- An [API key](https://portal.telnyx.com/#/app/api-keys)

## How scheduled messaging works

When you schedule a message, Telnyx stores it and delivers it at the specified time. Here's how it works:

1. You send a request with a `send_at` timestamp set in the future
2. Telnyx validates the request and returns a message resource with `status: "scheduled"`
3. At the scheduled time (accurate to the minute), Telnyx sends the message
4. Standard [messaging webhooks](receiving-webhooks.md) fire as the message is processed and delivered

**Scheduling constraints:**

- `send_at` must be at least **5 minutes** in the future
- `send_at` must be no more than **5 days** in the future
- Scheduling accuracy is up to **1 minute**
- Maximum of **1 million** scheduled messages at any given time
