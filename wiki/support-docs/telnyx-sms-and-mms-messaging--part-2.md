---
title: Telnyx SMS and MMS Messaging
summary: Comprehensive guide to Telnyx programmable messaging, covering messaging
  profile setup, sending and receiving SMS/MMS, number pooling, alphanumeric sender
  IDs, SMPP, forwarding and automation, opt-out management, deliverability best practices,
  error codes, hosted messaging, and third-party integrations.
sources:
- url: https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow
  content_hash: 742b0531871ecb2b325ceaeff9950aec77ff68b6bc269bb4c596db2cfbea4dd4
- url: https://support.telnyx.com/en/articles/1130611-understand-telnyx-sms-mdr-report-log
  content_hash: 5fcf9078ffa5f93c585c964152bf8ca3c6f574efb0515e9d9b0f1ad81c2f20ae
- url: https://support.telnyx.com/en/articles/1130617-sms-long-code-deliverability-best-practices
  content_hash: 323a6b9825f680da66faad141e0ff0383bc3f6d168a68d1cf39ef435eea36127
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
  content_hash: 29e9e3ea4635d9b03eca472413a554f54515f4d06eef5fcb1e2a4bf344e14ad3
- url: https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide
  content_hash: eeec31f5316397de5edb0a1b1817b4473a61822359735b2cb5258f02b3c7d447
- url: https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving
  content_hash: 43280b0332869a7afa125df17d8848a24db21f1a2341f1fa38898a906ca901d6
- url: https://support.telnyx.com/en/articles/3154822-number-pooling
  content_hash: ad2df80267020e799b9fbbd06fec51abe76304270e764de28525101b1370ce50
- url: https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number
  content_hash: 14767eb1154d10ca27eab1f7e7bc29905a365bbc0142253224287a1dc89c7f44
- url: https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier
  content_hash: ef1e5595e71bd2abf7743d5ba38c865f69a7e52aed0b5520c193d8bee929ca0e
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
  content_hash: acd4bd72ec29f236f3d6f2be8dcd57267d0756c5d3d9f9f01e07364931883b85
- url: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
  content_hash: 6569f922cad9f0f1ba66b4caaf30fbf6d3989e385c523da0fe89acb4abe696d0
- url: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
  content_hash: 0ef11e5f0fd5cd43f8cf988923a4d40589d0817aee6966de86340060a054c8d4
- url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
  content_hash: f29693c3cfef76c2e2343b5d50f337b75e45dec08bd6883a9f7743f30605b084
- url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
  content_hash: 6d3584276d3b970e89374e515d03e81d628b84eb4ff6281d8d8175edf48b7a9c
- url: https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman
  content_hash: 0ea46ca7d946ad44e3fbab6b9af13f11074420d1c5b1cf0be60a3344614735ef
- url: https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number
  content_hash: 791d3233dad58906d25b025a61062b55c2cf2f95d6fe1ba4d739a93dd0780bb6
- url: https://support.telnyx.com/en/articles/4371498-sending-alphanumeric-sms-sender-id
  content_hash: f176c448a988a3a798b5253af45916a6cbeffa32bb72a4f209c0395c5234780d
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
  content_hash: f6f7abd47b59ccde9fc66d0d2c0ebc54df4cfeabca84c57568540eac823144db
- url: https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes
  content_hash: 442e1de50aee9320b592e6a73351e7713e79393c20b218cf374961c9f64f922e
- url: https://support.telnyx.com/en/articles/6969802-message-deliverability-dashboard
  content_hash: c5ae67d4093a874c1114754b6330003b546d97f2faeb182f8e801d0128b642c2
- url: https://support.telnyx.com/en/articles/6986625-easy-text-marketing-and-telnyx-integration
  content_hash: 2e9b0dd00e9c8e8c7c8c3a1a546bc0cf764a1e64bba4ffb5aa59f14231e18188
- url: https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage
  content_hash: e766afbb01899830a18b3a4309fa7bb0b71fc9bef6ff75a4532ece5b65cae404
- url: https://support.telnyx.com/en/articles/8219294-messaging-in-mission-control
  content_hash: d57e42ee7a0e3be1d7ff39ca3efacac558b4deed69b13e4a453526ca8b282822
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
  content_hash: 2d92129297c8d6d90a1721e1f6bba5843f9e18430657b0626066f2c06cb7deb1
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
  content_hash: 9184d0502c7c465e7246274f19c27a3d8aae6298eb87b2a6e32ab91215966311
- url: https://support.telnyx.com/en/articles/9767793-sending-a-test-message-with-learn-and-build
  content_hash: 08bd7f3d43b7a83da1919d77bba65a4d31503279675f91fd2e782104e9f00b9f
updated_at: 2026-06-11T11:37:45Z
---

# Telnyx SMS and MMS Messaging

*Part 2 of 4 — see also: [Part 1](telnyx-sms-and-mms-messaging--part-1.md), [Part 3](telnyx-sms-and-mms-messaging--part-3.md), [Part 4](telnyx-sms-and-mms-messaging--part-4.md)*

Comprehensive guide to Telnyx programmable messaging, covering messaging profile setup, sending and receiving SMS/MMS, number pooling, alphanumeric sender IDs, SMPP, forwarding and automation, opt-out management, deliverability best practices, error codes, hosted messaging, and third-party integrations.

## Number Pooling

Number Pooling automatically selects originating numbers from all numbers assigned to a messaging profile, maintaining balance to ensure high deliverability.

**Default throughput limit:** 6 SMS per minute per long code number. Spread traffic across multiple numbers to increase throughput (e.g., 10 numbers = 10 SMS/second).

### Enabling Number Pooling

Navigate to your messaging profile's edit page and enable the Number Pooling toggle.

### Advanced Options

- **Weights** — Set the ratio of toll-free vs. long code selection. A higher weight means that number type is chosen more often.
- **Skip Unhealthy Numbers** — Automatically removes numbers from the pool if deliverability falls below 25% or spam detection exceeds 75%.
- **Sticky Sender** — Remembers which originating number was used for each destination and reuses it for future messages to that recipient.
- **Geomatch** — Automatically sends from a number with the same local area code as the recipient (US area codes only).

## Alphanumeric Sender ID

Alphanumeric Sender ID allows you to set a company name or brand (3–11 characters: A-Z, a-z, 0-9, space) as the sender for one-way SMS to international destinations.

**Requirements:**
- Level 2 verified account
- Not supported by carriers in the US or Canada
- Can be set dynamically in the `from` field of API requests or as a default on the Messaging Profile

**API v2 example:**

```json
{
  "from": "MyCompany",
  "to": "+destination_number",
  "messaging_profile_id": "your-profile-id",
  "text": "Hello World!",
  "webhook_url": "https://your-webhook.url"
}
```

## SMPP Protocol

SMPP (Short Message Peer-to-Peer) is designed for customers requiring high throughput. This feature is reserved for contracted customers committing to a $5,000 minimum monthly spend for 12 months.

### Connection Parameters

| Parameter | Value |
|-----------|-------|
| Host | smpp.telnyx.com |
| Port | 2775 |
| SSL | Yes (TLS) |
| addr_ton | 1 (International) |
| addr_npi | 1 (ISDN/E163/E164) |

Username and password are provided by your account manager. Provide your Messaging Profile ID to receive credentials.

### Supported PDUs

bind_transmitter, bind_transceiver, bind_receiver, unbind, submit_sm, deliver_sm, enquire_link

### Throughput

- Long Code: 10 messages per number per minute
- Toll-Free: 1,200 messages per number per minute

## SMS Forwarding and Automation

### Forwarding with Telnyx Flow (No-Code)

Set up SMS/MMS forwarding without code using [Telnyx Flow](https://flow.telnyx.com/):

1. Log in at flow.telnyx.com and create a new workspace.
2. Create a new workflow with a blank canvas.
3. Add nodes: **Inbound Message** (trigger), **Switch** (logic), and two **Send Message** nodes (one for SMS, one for MMS).
4. Configure the Switch node with condition groups:
   - **SMS condition:** Input `{{message.received.type}}`, comparison "Equals", value "SMS"
   - **MMS condition:** Input `{{message.received.type}}`, comparison "Equals", value "MMS"
5. Connect each Switch output to its corresponding Send Message node.
6. Configure Send Message nodes with the same Messaging Profile ID, inverted From/To variables, and custom text. MMS nodes also include Subject and Media URLs fields.
7. Save and deploy the workflow.

You can test workflows directly in Telnyx Flow using the "Run Workflow" button.

### Forwarding with Zapier

Set up a Zapier automation to forward inbound SMS to your mobile number:

1. Connect the [Telnyx Zapier integration](https://zapier.com/apps/telnyx/integrations).
2. Create a Zap with **Telnyx → Receive a Message** as the trigger.
3. Select your Telnyx account using your API V2 Key.
4. Test the trigger to pull in a sample message.
5. Add **Telnyx → Send SMS** as the action:
   - Source Number: Your Telnyx number in E.164 format
   - Destination Number: Your personal mobile number in E.164 format
   - Message Content: Include dynamic fields like `From Phone Number` and `Text`
6. Test and publish the Zap.

**Prerequisites:** Telnyx account, SMS-enabled number, messaging profile, API V2 Key, and Zapier account.

### Automated Replies with Zapier

Follow a similar Zap setup but configure the Send SMS action to:
- Source Number: Your Telnyx number
- Destination Number: Use the `From Phone Number` dynamic field from the trigger (replying to the sender)
- Message Content: Your automated reply text

For US numbers, ensure your Telnyx number is associated with a registered 10DLC campaign.

### Forwarding Texts to Email with Zapier

1. Set up the Telnyx **Receive a Message** trigger as above.
2. Add an email action (e.g., Gmail → Send Email).
3. Configure email fields using dynamic variables from the trigger (From, To, Body/Text).
4. Test and publish.

**Note:** Telnyx has acknowledged that the "Receive a Message" Zap is currently outdated and being fixed.

## Opt-Out Keywords and Management

Telnyx automatically processes English-language stop words. When recognized, the sender's number is added to the opt-out list for the entire messaging profile.

### Stop Words

stop, stopall, stop all, unsubscribe, cancel, end, quit

Stop words are only recognized if they are the sole content of the message. For example, "stop all" is recognized but "please stop all messages" is not.

### Opt-In Keywords

start, unstop

The end user must send an opt-in keyword to the exact same number they opted out from. When using number pooling, check MDRs to identify which number received the opt-out.

### Auto-Response

By default, Telnyx sends automatic responses:
- Opt-out: "You have successfully been unsubscribed, you will not receive any more messages from this number. Reply START to re-subscribe."
- Opt-in: "You have successfully been re-subscribed to this number. Reply STOP to unsubscribe. Msg&Data Rates May Apply."

### Custom Keywords

Manage custom keywords at [portal.telnyx.com/#/programmable-messaging/keywords-management](https://portal.telnyx.com/#/programmable-messaging/keywords-management). Select a messaging profile, then add custom opt-in/out and help keywords with custom auto-responses globally or per country.

**Restrictions:** Maximum 20 custom keywords per profile.

### Profile-Level Opt-Out Scope

Opt-outs apply across all numbers on the same messaging profile. If number A on profile X receives a STOP, all numbers on profile X are blocked from messaging that recipient. Numbers on a different profile Y are not affected.

## Deliverability Best Practices

### Use Long Codes for Unique Messages Only

Long code SMS is intended for P2P communication or A2P use cases where a human initiates the message with recipient-specific content. Marketing campaigns should use short codes.

### Limit Send Rate

- Long codes: Maximum 10 messages per minute per number (no more than 1 message every 6 seconds)
- Account-level default: 1 message per second. Contact sales to increase.
- Exceeding limits results in throttled deliverability.

### Avoid Consecutive Number Ranges

SPAM filters flag high-volume messages from consecutive number ranges. Purchase discontiguous numbers instead.

### Limit URL Length

Long URLs cause message splitting and are more likely to be flagged by spam filters. Minimize message text when including dynamically generated URLs. URLs with "bitlylinks.com" and "bit.ly" domains are automatically blocked.

### Include Opt-Out Language

A2P messaging without opt-out language is the number-one reason for false delivery reports — carriers silently filter messages as spam. Always include opt-out instructions.
