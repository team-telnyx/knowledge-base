---
title: Telnyx Mission Control Account Setup
summary: A consolidated guide to creating and configuring a Telnyx Mission Control
  account, covering sign-up, verification, Freemium and Managed Accounts, AI Assistants,
  messaging, voice, and the in-portal AI support assistant.
sources:
- url: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
- url: https://support.telnyx.com/en/articles/12232444-comprehensive-ai-assistants-configuration-walk-through
- url: https://support.telnyx.com/en/articles/14327893-telnyx-freemium-accounts
- url: https://support.telnyx.com/en/articles/4404409-resources-on-your-account
- url: https://support.telnyx.com/en/articles/4951492-managed-accounts
- url: https://support.telnyx.com/en/articles/5295540-how-to-sign-up-for-a-telnyx-account
- url: https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant
- url: https://support.telnyx.com/en/articles/8219294-messaging-in-mission-control
- url: https://support.telnyx.com/en/articles/9767793-sending-a-test-message-with-learn-and-build
- url: https://support.telnyx.com/en/collections/19623087-ai-assistant
updated_at: 2026-08-05T13:32:36Z
---

# Telnyx Mission Control Account Setup

*Part 2 of 5 — see also: [Part 1](telnyx-mission-control-account-setup--part-1.md), [Part 3](telnyx-mission-control-account-setup--part-3.md), [Part 4](telnyx-mission-control-account-setup--part-4.md), [Part 5](telnyx-mission-control-account-setup--part-5.md)*

A consolidated guide to creating and configuring a Telnyx Mission Control account, covering sign-up, verification, Freemium and Managed Accounts, AI Assistants, messaging, voice, and the in-portal AI support assistant.

## Setting Up Mission Control for Messaging

Before configuring a messaging system, review the [Acceptable Use Policy for Messaging](acceptable-use-policy-for-messaging.md). For a guided setup with some programming context, use the messaging [Learn & Build](https://portal.telnyx.com/#/app/programmable-messaging/learn-and-build) tool after completing the first two steps.

Requirements:

1. **Level 1 Verification** — required to assign a connection or messaging profile to a DID.
2. **Payments** — add a payment method to top up the balance.
3. **Messaging Profile Setup** — a messaging profile contains the basic settings for messages. Telnyx messaging is fully programmatic, so a webhook URL is required to receive inbound messages and track outbound messages.
4. **DIDs** — a DID (or TN) is required to send and receive messages. Number types include:
   - **Regular number (10-Digit Long Code)** — e.g. +1 234 567 8910, +52 2345 1232.
   - **Toll-free number** — a national number that allows caller fees to be passed to the receiver (except for messaging).
   - **Short code** — used for high-volume messaging such as 2FA codes.

Numbers must be explicitly SMS and/or MMS enabled. Each type has different requirements and pricing depending on location. Numbers acquired without SMS capabilities cannot be enabled later. Numbers can also be ported into Telnyx.

After acquiring a DID, assign the messaging profile via the numbers main page or the number configuration page.

### Messaging Notes

- If a messaging profile cannot be assigned and the column shows **Not SMS Capable**, the number is not capable of sending or receiving messages. Confirm the messaging features icon shows **SMS Available** when searching and purchasing numbers.
- The error **"Could not enable messaging on the number."** when assigning a messaging profile to an SMS-capable number may be related to provisioning with the central authority that handles carrier NetNumber ID routing updates. If the error persists, contact support.

### Traffic Type and Registration

Messaging is categorized as A2P (Application-to-Person) or P2P (Person-to-Person). For A2P traffic, check local regulations. In the US and Canada, registering for 10DLC (soon mandatory) or Toll-Free Messaging is strongly recommended; lead time can be up to four weeks or more depending on the use case and required documents.

### Additional Messaging Resources

- To increase the default sending rate, obtain [Level 2 Verification](account-verification.md).
- For purchasing toll-free and 10-digit numbers, see [Search and Buy Numbers](search-and-buy-numbers.md).
- For country-specific SMS guidelines, see the country-specific SMS guidelines collection.
- For Short Code information, see the Short Code supported carriers article.
- For SMPP, see the Short Message Peer-to-Peer Set-up Guide.
- For Alphanumeric sending (available outside the US and Canada), see the Alphanumeric SMS Sender ID article.

## Sending a Test Message with Learn and Build

The Learn and Build feature in Mission Control enables sending a test SMS without using the API directly.

### Step 1: Portal Setup

Before sending a test message:

- Find a phone number using the Telnyx Search & Buy numbers feature.
- Purchase a phone number.

### Step 2: Set Up a Messaging Profile

Before sending a test message:

- Set up a Messaging Profile.
- Associate the Messaging Profile with a phone number.

### Step 3: Send and Receive a Message

Once a phone number and Messaging Profile are in place:

- Compose a test message or choose a template (Order Notifications, Inbound Marketing, Reminders, Surveys).
- The **From** number is the phone number assigned to the Messaging Profile.
- Enter a **To** number — using a mobile phone is recommended so the message can be seen.
- For a **Blank Message**, type the message in the box.
- An image can be included.
- Click **Send Message**.
- The **Raw Response** box populates with information from the webhook sent to the URL associated with the Messaging Profile.

If setup is correct, the message is received on the destination device. Receiving can be tested by replying from the mobile phone.

### Step 4: Development Environment Setup

To build an application with the Telnyx SMS API:

- Obtain API keys, displayed on this screen.
- Install a Telnyx SDK of choice; each option includes additional support documentation.

### Step 5: Build the App

Choose from tutorials to learn how to build and scale the app. If no matching use case is found, support is available 24/7 in the Mission Control Portal.
