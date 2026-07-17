---
title: Telnyx Messaging
summary: A consolidated reference for Telnyx programmable messaging covering messaging
  profiles, opt-in/opt-out keywords and auto responses, 10DLC and toll-free verification,
  hosted SMS, SMPP setup, and third-party integrations.
sources:
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
- url: https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6986625-easy-text-marketing-and-telnyx-integration
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
updated_at: 2026-07-17T09:00:31Z
---

# Telnyx Messaging

*Part 1 of 4 — see also: [Part 2](telnyx-messaging--part-2.md), [Part 3](telnyx-messaging--part-3.md), [Part 4](telnyx-messaging--part-4.md)*

A consolidated reference for Telnyx programmable messaging covering messaging profiles, opt-in/opt-out keywords and auto responses, 10DLC and toll-free verification, hosted SMS, SMPP setup, and third-party integrations.

## Overview

Telnyx provides programmable messaging across long code (10DLC), toll-free, and short code numbers, with a unified set of compliance, opt-in/opt-out, and configuration requirements. This page consolidates the key concepts: messaging profiles, opt-out keywords and auto responses, 10DLC and toll-free verification, hosted SMS, SMPP, and integrations.

## Messaging Profiles

A [Messaging Profile](setting-up-a-messaging-profile.md) is a configuration that manages inbound and outbound messaging settings and is the simplest way to configure how you send and receive messages on a phone number. An SMS-capable phone number is SMS-enabled by assigning it to a Messaging Profile.

To create one, navigate to **Programmable Messaging** in the Mission Control Portal and click **Add New Profile** (or **Create your first profile** for new accounts). Enter a unique Profile Name; API v2 is selected by default. Inbound settings include webhook URLs, which are required to deliver inbound messages to your application. Outbound settings include:

- **Alphanumeric Sender ID** — used for one-way outbound international messages, typically the business name.
- **Manage Allowed Destinations** — restrict or allow international destinations to minimize fraud.
- **Number Pooling** — deliver messages from a pool of multiple phone numbers to handle higher volume.
- **MMS Fallback** — convert MMS to SMS with the media URL appended when MMS is unsupported.
- **MMS Transcoding** — compress MMS media to meet carrier size restrictions, allowing MMS up to 5MB.
- **Daily Spend Limit Per Connection** — cap outbound spend in USD per day, resetting at 00:00:00 UTC.

After saving, the Messaging Profile ID is visible in the profile settings. The profile must then be associated with a phone number under **My Numbers** by editing the Messaging Profile column. As of **March 1, 2024**, editing or creating a Messaging or Verify Profile via the Portal or API requires configuring whitelisted destination countries for outbound termination, and sending to non-US destinations requires a default Alphanumeric Sender ID.

## Receiving SMS

There is no provision in the Telnyx portal to view received SMS directly. To receive SMS on a Telnyx number, attach a webhook to the number's Messaging Profile. In **Messaging > Programmable Messaging**, select the profile, then **Inbound**, and configure the webhook URL. Once saved, inbound message contents are delivered to the webhook endpoint. A webhook URL is required to deliver inbound messages to your application.

## Opt-Out Keywords and Stop Words

Telnyx automatically processes incoming messages and recognizes English-language stop words. When a stop word is detected, the phone number is added to the opt-out list and further messages to that number are blocked.

### Opt-out scope at the messaging profile level

Opt-outs are scoped to the messaging profile by default. If a number on Messaging Profile X sends a text to a recipient who replies STOP, all numbers on Messaging Profile X are blocked from texting that recipient, while numbers on a different Messaging Profile Y can still message them.

### Recognized stop words

Telnyx recognizes the following stop words (only when they are the only words in the message):

- stop
- stopall
- stop all
- unsubscribe
- cancel
- end
- quit

For example, "stop all" is recognized but "please stop all messages" is not.

### Opt-in keywords

To opt back in, the recipient must send one of the following to the exact same number they opted out from:

- start
- unstop

When using number pooling, the opt-in must be sent to the specific number the recipient originally opted out from. The originating number can be identified by filtering MDRs for the opt-out SMS.

### Auto responses

By default, Telnyx handles the auto response to opt-outs. The generic messages are:

- Opt-out: "You have successfully been unsubscribed, you will not receive any more messages from this number. Reply START to re-subscribe."
- Opt-in: "You have successfully been re-subscribed to this number. Reply STOP to unsubscribe. Msg&Data Rates May Apply."

Custom block rules and auto responses can be configured per messaging profile by contacting [sales@telnyx.com](mailto:sales@telnyx.com).

### Keyword management

Custom keywords for opt-in, opt-out, and help messages, along with their auto responses, can be configured in the portal at [Keywords Management](https://portal.telnyx.com/#/programmable-messaging/keywords-management). Select a messaging profile to add keywords globally (Country: Global) or click **Add keywords in other languages based on country selected** to create country-specific rule sets. A maximum of 20 keywords can be added.

## Toll-Free Opt-Out Words

Opt-out handling for toll-free numbers differs from long code. The only keyword recognized for opting out of a Telnyx toll-free number is **stop**. The only opt-in keywords are **start** and **unstop**.

Auto responses for toll-free are:

- Opt-out: "NETWORK MSG: You replied with the word \"stop\" which blocks all texts sent from this number. Text back \"unstop\" to receive messages again."
- Opt-in: "NETWORK MSG: You have replied \"unstop\" and will begin receiving messages again from this number."

Because toll-free opt-out logic is handled outside of Telnyx, the opt-out/opt-in keywords and auto response content cannot be customized for toll-free numbers. If custom block rules are configured on a messaging profile, toll-free numbers should be placed on a separate profile to avoid unintended behavior.

## 10DLC Keywords and Confirmation Messages

Under 10DLC guidelines, all campaigns must include Keywords and Confirmation Messages for Opt-in, Opt-out, and Help. The recommended format is:

- **Opt-in Keyword:** START or similar keyword
- **Opt-in confirmation message:** `[Brand name]: Thanks for subscribing to [use case(s)]! Reply HELP for help. Message frequency may vary. Msg&data rates may apply. Consent is not a condition of purchase. Reply STOP to opt out.`
- **Opt-out Keyword:** STOP or similar keyword
- **Opt-out confirmation message:** `[Brand Name]: You are unsubscribed and will receive no further messages.`
- **Help Keyword:** HELP or similar keyword
- **Help confirmation message:** `[Brand name]: Please reach out to us at [website/email/phone number] for help.`

Websites referenced in help messages are permissible so long as they have clear contact information at the link provided.
