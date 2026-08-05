---
title: RCS Getting Started
summary: RCS (Rich Communication Services) is a messaging protocol that delivers app-like
  experiences in the native messaging app without requiring a download. This guide
  covers the Telnyx RCS approval process, how to create a messaging profile, send
  rich cards and suggested replies, and handle incoming RCS messages via webhooks.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/rcs-getting-started/index
- url: https://developers.telnyx.com/docs/messaging/messages/receive-message
updated_at: 2026-08-05T13:57:03Z
---

# RCS Getting Started

*Part 1 of 4 — see also: [Part 2](rcs-getting-started--part-2.md), [Part 3](rcs-getting-started--part-3.md), [Part 4](rcs-getting-started--part-4.md)*

RCS (Rich Communication Services) is a messaging protocol that delivers app-like experiences in the native messaging app without requiring a download. This guide covers the Telnyx RCS approval process, how to create a messaging profile, send rich cards and suggested replies, and handle incoming RCS messages via webhooks.

## What is RCS?

RCS is a messaging protocol that delivers app-like experiences in the native messaging app—no app download required. Unlike SMS/MMS, RCS supports:

- **Rich cards** with images, titles, and action buttons
- **Carousels** for product showcases
- **Suggested replies** for quick responses
- **Read receipts** and typing indicators
- **High-resolution media** (images, video, files)

RCS is currently supported on Android devices. Apple announced RCS support in iOS 18.

## Prerequisites

- A [Telnyx account](https://telnyx.com/sign-up)

## Approval process

RCS requires agent registration and carrier approval before you can send messages to the general public. The process is similar to short code approval:

1. **Submit your RCS Agent.** [Contact sales](https://telnyx.com/contact-us) to start the onboarding process. Provide your brand details, use case, and sample message content.
2. **Testing stage.** Once submitted, Telnyx moves your agent into a testing stage. During this phase, you can invite beta test numbers using the API to test your integration while waiting for carrier approval.
3. **Carrier approval.** Carriers review and approve your agent. This process typically takes **4–6 weeks**, similar to short code approval.
4. **Go live.** Once approved, your RCS Agent can send messages to any RCS-capable device.

You don't have to wait for full carrier approval to start testing. Once your agent is in testing stage, you can add beta numbers and send test messages via the API.

## Create a Messaging Profile

1. Navigate to [Messaging](https://portal.telnyx.com/#/app/messaging) in the portal.
2. Click **Add new profile**, give it a name (e.g., "RCS Profile"), and click **Save**.
3. Copy the Messaging Profile ID—you'll need it when sending messages.

## Get your API key

Go to [API Keys](https://portal.telnyx.com/#/app/api-keys) and copy your API key (or create one if needed).
