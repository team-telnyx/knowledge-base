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

*Part 3 of 4 — see also: [Part 1](telnyx-sms-and-mms-messaging--part-1.md), [Part 2](telnyx-sms-and-mms-messaging--part-2.md), [Part 4](telnyx-sms-and-mms-messaging--part-4.md)*

Comprehensive guide to Telnyx programmable messaging, covering messaging profile setup, sending and receiving SMS/MMS, number pooling, alphanumeric sender IDs, SMPP, forwarding and automation, opt-out management, deliverability best practices, error codes, hosted messaging, and third-party integrations.

## Message Detail Records (MDR)

For every sent or received message, an MDR is generated. Access reports at **Reports → Reporting** in the Mission Control Portal.

MDRs are stored as JSON objects with key fields including record type, direction, status, coding, number of parts, cost, and rate.

### Message Body Privacy

Message body text is stored for up to 10 days, after which it is wiped. Hash fields can be used to identify messages after body text is removed.

### Status Values

**Sent messages:** queued, sending, sent, delivered, delivering, undelivered, expired, canceled, failed

**Received messages:** received, unread, read

### Message Encoding

| Coding | Encoding |
|--------|----------|
| 0 | GSM 7-bit (default) |
| 1 | IA5/ASCII |
| 3 | Latin 1 (ISO-8859-1) |
| 8 | UCS-2/UTF-16 |

GSM 7-bit is used when possible; otherwise UTF-16 is used.

### Message Parts and Billing

Long messages are divided into parts:
- GSM 7-bit: 160 characters per part (153 for multi-part)
- UTF-16: 70 characters per part (67 for multi-part)

Outbound messages have a maximum of 10 parts. Billing is based on the number of parts:

`rate` = price per message + carrier fee for one part
`cost` = rate × message parts

## Message Deliverability Dashboard

A real-time dashboard for monitoring and analyzing messaging usage at [portal.telnyx.com/#/reports/messaging-deliverability](https://portal.telnyx.com/#/reports/messaging-deliverability).

### Summary Headers

- Total messages
- Average deliverability percentage
- Total "In-Flight" messages (sent but no delivery receipt yet)

### Filters

- **Direction:** Outbound (inbound coming in future release)
- **Type:** All, SMS, MMS
- **Product:** All, Toll Free, Short Code, Long Code, Alphanumeric
- **Time span:** Current day, calendar month, or custom range

### Profile Statistics

Per messaging profile: Deliverability ratio, total count, delivered, not delivered, parts, and in-flight count. Click "View Profile" to navigate to the profile configuration.

**Note:** This dashboard operates in UTC 00:00, whereas usage reports use local browser time.

## Error Codes

### Invalid Request Errors (1XXXX)

| Code | Description |
|------|-------------|
| 10001 | Inactive phone number |
| 10002 | Invalid phone number |
| 10003 | Invalid URL |
| 10004 | Missing required parameter |
| 10005 | Resource not found |
| 10006 | Invalid ID |
| 10007 | Unexpected error |
| 10009 | Authentication failed |
| 10010 | Authorization failed |
| 10011 | Too many requests |
| 10015 | Bad request |
| 10016 | Phone number must be in +E.164 format |

### Account Level Errors (2XXXX)

| Code | Description |
|------|-------------|
| 20002 | API Key revoked |
| 20006 | Expired access token |
| 20012 | Account inactive (possibly insufficient funds) |
| 20013 | Account blocked |
| 20014 | Account unverified |
| 20015 | Feature not enabled |
| 20016 | Account not Level 1 verified |
| 20017 | Account not Level 2 verified |
| 20100 | Insufficient funds |

### Delivery Errors (4XXXX)

| Code | Description |
|------|-------------|
| 40001 | Not routable (landline or non-routable number) |
| 40002 | Blocked as spam — temporary |
| 40003 | Blocked as spam — permanent |
| 40004 | Rejected by destination |
| 40005 | Message expired during transmission |
| 40006 | Recipient server unavailable |
| 40008 | Undeliverable |
| 40009 | Invalid message body |
| 40010 | Unregistered 10DLC message |
| 40011 | Too many requests (upstream rate limit exceeded) |
| 40012 | Invalid messaging destination number |
| 40013 | Invalid messaging source number |
| 40014 | Message expired in queue (not billed) |
| 40015 | Blocked as spam — internal (Telnyx filter) |
| 40100 | Number not messaging enabled |
| 40150 | Toll-free number not in voice registry |
| 40151 | Message enablement pending with other provider |
| 40300 | Blocked due to STOP message |
| 40301 | Unsupported message type for the 'to' address |
| 40302 | Message too large |
| 40304 | Invalid combination of message content arguments |
| 40305 | Invalid 'from' address |
| 40306 | Alpha sender not configured |
| 40308 | Invalid 'from' address for MMS |
| 40309 | Invalid destination region (not whitelisted) |
| 40310 | Invalid 'to' address |
| 40311 | Invalid messaging profile secret |
| 40312 | Messaging profile is disabled |
| 40313 | Missing messaging profile secret |
| 40314 | Messaging disabled on account |
| 40315 | Unhealthy 'from' address (low deliverability / high spam) |
| 40316 | No content provided for message |
| 40317 | Invalid MMS content (max 10 URLs, under 1 MB) |
| 40318 | Message queue full |
| 40319 | Incompatible message type for the 'to' address |
| 40320 | Temporarily unusable 'from' address (purchase pending) |
| 40321 | No usable numbers on messaging profile |
| 40322 | Blocked due to content |
| 40328 | SMS exceeds recommended size |
| 40329 | Toll-free number not yet verified |

### 10DLC-Specific Errors

| Code | Description |
|------|-------------|
| 40016 | T-Mobile 10DLC sending limit reached (resets daily at midnight PST) |
| 40017 | AT&T 10DLC spam message rejected |
| 40018 | AT&T 10DLC sending limit reached (parts per minute exceeded) |

**Important:** Messages that fail after leaving the Telnyx network still incur charges. Toll-free numbers must be registered to avoid carrier blocks.

## Hosted SMS Messaging

Hosted SMS allows you to port the messaging portion of a number to Telnyx while leaving voice with the current provider.

### Requirements

- Level 2 verified account
- Signed Letter of Authorization (LOA) within the last 30 days
- Invoice from the current messaging provider
- Expressed consent of the authorized end user

### Submitting an Order

1. Navigate to **Messaging > Hosted Messaging** in the portal.
2. Click **Create new order** and enter up to 200 numbers plus the messaging profile.
3. Upload the LOA and bill as PDF files (max 5 MB each, no special characters in filenames).
4. Orders are processed within 24–48 business hours (Mon–Fri, 9 AM–5 PM CT, excluding holidays).

### Limitations

- Only US and Canadian local numbers and toll-free numbers are supported (not international).
- Cannot host messaging from wireless providers (including Google Voice). Zoom Phone does allow hosted messaging.
- Cannot transfer hosted messaging between Telnyx accounts.
- If voice is already with Telnyx, add a messaging profile directly rather than using hosted messaging.
- Numbers on a Telnyx LRN cannot have messaging ported to another provider.
- Known providers with blocks: Bandwidth, Aerialink, Callfire — manual intervention required.
- Toll-free hosted messaging takes a minimum of 72 hours.

## Third-Party Integrations

### Textable

1. Sign up at [textable.app](https://textable.app/signup) and select **Telnyx V2** as the provider.
2. In Telnyx, create a messaging profile named "Textable" with:
   - Inbound protocol: HTTP
   - Webhook URL: `https://app01.textable.co/receive?provider=telnyxv2`
3. Create an API key and paste it into Textable's Access Token field.
4. Assign the messaging profile to your phone number in the Telnyx portal.
5. Download the Textable app from the [App Store](https://apps.apple.com/us/app/textable-voip-texting/id1355564896) or [Google Play](https://play.google.com/store/apps/details?id=co.textable.textable).

### Easy Text Marketing

1. Create a Telnyx account and add funds.
2. Copy your API key from the Mission Control Portal.
3. In Easy Text Marketing, select Telnyx as the SMS Gateway and enter the API key.
4. Click "Get a Number" in the Easy Text Marketing dashboard (this auto-creates a messaging profile in Telnyx).
5. In Telnyx, assign the Easy Text Marketing messaging profile to your number.
