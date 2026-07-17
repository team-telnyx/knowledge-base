---
title: Telnyx Account, Billing, and Support Guide
summary: This page consolidates Telnyx account, billing, and support guidance, covering
  account types (including Freemium and Managed Accounts), billing setup, payment
  methods, invoices, billing groups, notification settings, the AI Chat Support Assistant,
  feature requests, bug reports, security vulnerability disclosure, and sending test
  messages via the Learn and Build feature in the Mission Control Portal.
sources:
- url: https://support.telnyx.com/en/articles/1130644-do-i-have-to-sign-a-contract
- url: https://support.telnyx.com/en/articles/14327893-telnyx-freemium-accounts
- url: https://support.telnyx.com/en/articles/4277896-notification-settings
- url: https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups
- url: https://support.telnyx.com/en/articles/4283783-feature-requests
- url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
- url: https://support.telnyx.com/en/articles/4951492-managed-accounts
- url: https://support.telnyx.com/en/articles/6987563-invoice-overview
- url: https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant
- url: https://support.telnyx.com/en/articles/9767793-sending-a-test-message-with-learn-and-build
updated_at: 2026-07-17T09:04:25Z
---

# Telnyx Account, Billing, and Support Guide

*Part 5 of 5 — see also: [Part 1](telnyx-account-billing-and-support-guide--part-1.md), [Part 2](telnyx-account-billing-and-support-guide--part-2.md), [Part 3](telnyx-account-billing-and-support-guide--part-3.md), [Part 4](telnyx-account-billing-and-support-guide--part-4.md)*

This page consolidates Telnyx account, billing, and support guidance, covering account types (including Freemium and Managed Accounts), billing setup, payment methods, invoices, billing groups, notification settings, the AI Chat Support Assistant, feature requests, bug reports, security vulnerability disclosure, and sending test messages via the Learn and Build feature in the Mission Control Portal.

## Sending a Test Message with Learn and Build

Although using the Telnyx SMS API is required to scale text messaging, the Learn and Build feature in the Mission Control Portal enables you to send a test message.

### Step 1: Portal Setup

Before sending a test message, you need to have already:

- Found a phone number using the Telnyx Search & Buy numbers feature
- Purchased a phone number

### Step 2: Set up a Messaging Profile

Before sending a test message, you are required to:

- Set up a Messaging Profile
- Associate the Messaging Profile with a phone number

### Step 3: Send and Receive a Message

Once you have a phone number and a Messaging Profile, you can send a test message:

- Compose your test message with a blank message or choose from templates (Order Notifications, Inbound Marketing, Reminders and Surveys)
- The **From** number will be the phone number assigned to the Messaging Profile
- Input a **To** number — using your mobile phone is suggested so you can see the text message
- If you chose **Blank Message**, type in a message in the box to send
- You can also include an image
- Click **Send Message**
- The **Raw Response** box will populate with information from the webhook sent to the URL associated with your Messaging Profile

If everything was set up properly, you should receive a text message from the phone number with the message you provided. You can also test receiving a message by responding to the text message on your mobile phone.

### Step 4: Development Environment Setup

To build an application with the Telnyx SMS API:

- Obtain your API keys, shown on this screen
- Install a Telnyx SDK of your choice

### Step 5: Build your App

Choose from one of the tutorials and learn how to build and scale your app.

## Support Channels

- **AI Assistant** — Available 24/7 via the Mission Control Portal widget.
- **NOC team** — Operates 24/7. See best practices for contacting them.
- **Porting team** — Available 9am - 7pm CT, Monday-Friday.
- **Numbering team** — Available 9am - 5pm CT, Monday-Friday.
