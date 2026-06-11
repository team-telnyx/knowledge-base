---
title: Telnyx SMS and MMS Messaging
summary: Comprehensive guide to Telnyx programmable messaging, covering messaging
  profile setup, sending and receiving SMS/MMS, number pooling, alphanumeric sender
  IDs, SMPP, forwarding and automation, opt-out management, deliverability best practices,
  error codes, hosted messaging, and third-party integrations.
sources:
- url: https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow
- url: https://support.telnyx.com/en/articles/1130611-understand-telnyx-sms-mdr-report-log
- url: https://support.telnyx.com/en/articles/1130617-sms-long-code-deliverability-best-practices
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
- url: https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide
- url: https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving
- url: https://support.telnyx.com/en/articles/3154822-number-pooling
- url: https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number
- url: https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
- url: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
- url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
- url: https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman
- url: https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number
- url: https://support.telnyx.com/en/articles/4371498-sending-alphanumeric-sms-sender-id
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
- url: https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes
- url: https://support.telnyx.com/en/articles/6969802-message-deliverability-dashboard
- url: https://support.telnyx.com/en/articles/6986625-easy-text-marketing-and-telnyx-integration
- url: https://support.telnyx.com/en/articles/8048045-use-airexplorer-with-telnyx-storage
- url: https://support.telnyx.com/en/articles/8219294-messaging-in-mission-control
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
- url: https://support.telnyx.com/en/articles/9767793-sending-a-test-message-with-learn-and-build
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
