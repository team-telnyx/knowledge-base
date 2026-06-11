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

*Part 1 of 4 — see also: [Part 2](telnyx-sms-and-mms-messaging--part-2.md), [Part 3](telnyx-sms-and-mms-messaging--part-3.md), [Part 4](telnyx-sms-and-mms-messaging--part-4.md)*

Comprehensive guide to Telnyx programmable messaging, covering messaging profile setup, sending and receiving SMS/MMS, number pooling, alphanumeric sender IDs, SMPP, forwarding and automation, opt-out management, deliverability best practices, error codes, hosted messaging, and third-party integrations.

## Getting Started with Messaging

To use Telnyx programmable messaging, you need:

- **Level 1 Verification** — Required to assign a messaging profile to a phone number. Level 2 verification is needed for higher sending rates and alphanumeric sender IDs.
- **Payment method** — Add funds at [portal.telnyx.com/#/billing/payment](https://portal.telnyx.com/#/billing/payment). Telnyx is prepaid; you only pay for what you use.
- **A Messaging Profile** — A configuration record containing inbound/outbound settings. See [#Messaging Profiles](messaging-profiles.md).
- **A messaging-capable phone number (DID)** — Numbers must be SMS and/or MMS enabled. Purchase numbers at [portal.telnyx.com/#/app/numbers/my-numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) or port existing numbers.

Review the [Acceptable Use Policy for Messaging](https://support.telnyx.com/en/articles/1310359-acceptable-use-policy-for-messaging) before sending traffic.

## Messaging Profiles

A Messaging Profile is the central configuration for managing inbound and outbound messaging settings. A phone number becomes SMS-enabled by assigning it to a Messaging Profile.

### Creating a Profile

1. Navigate to **Programmable Messaging** in the [Mission Control Portal](https://portal.telnyx.com/#/programmable-messaging/profiles).
2. Click **Add New Profile** and enter a unique Profile Name.
3. API v2 is selected by default (the latest API version).

### Inbound Settings

Configure webhook URLs for receiving inbound messages. A webhook URL is required to deliver inbound messages to your application. Set the protocol (HTTP or HTTPS) and the webhook endpoint.

### Outbound Settings

- **Alphanumeric Sender ID** — Set a default alphanumeric sender for one-way outbound international messages (e.g., a business name). Required when sending to non-US destinations.
- **Manage Allowed Destinations** — Whitelist countries for outbound messaging to prevent fraudulent abuse. Editing or creating a profile now requires configuring whitelisted destination countries.
- **Number Pooling** — Enable to distribute outbound messages across all numbers in the profile. See [#Number Pooling](number-pooling.md).
- **MMS Fallback** — Convert MMS to SMS with the media URL appended to the body for destinations that don't support MMS.
- **MMS Transcoding** — Compress MMS media files to meet carrier size restrictions, allowing MMS up to 5 MB.
- **Daily Spend Limit Per Connection** — Define a maximum daily USD spend on outbound messages (resets at 00:00 UTC).

### Finding the Messaging Profile ID

After creation, go back into the profile settings to find the unique ID at the bottom of the configuration screen. This ID is needed for SMPP bindings and API requests.

### Assigning a Profile to a Number

1. Go to [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers).
2. Hover over the Messaging Profile column for the desired number and click the edit (pencil) icon.
3. Select the profile from the dropdown and confirm cost changes.

**Important:** Only attach a single number to messaging profiles used for Zapier automations — all numbers on the same profile will trigger the same Zap.

## Phone Numbers

Several number types are available:

| Type | Description | Throughput |
|------|-------------|------------|
| 10-Digit Long Code (10DLC) | Standard local number | 10 msg/min/number |
| Toll-Free | National number with caller-paid fees | 1,200 msg/min/number |
| Short Code | Special 5-6 digit number for high-volume A2P | High throughput |

Numbers must explicitly be SMS and/or MMS enabled. If a number shows **Not SMS Capable**, it cannot be used for messaging. When searching for numbers, ensure the messaging features icon shows **SMS Available**.

For US/Canada A2P traffic, register for 10DLC or Toll-Free messaging. Unregistered traffic may be filtered or blocked by carriers.

## Sending Messages

### API v1

Endpoint: `https://sms.telnyx.com/messages`

Authentication: `x-profile-secret` header with your Messaging Profile secret.

```json
{
  "from": "+1your_number",
  "to": "+1recipient_number",
  "body": "Hello World"
}
```

### API v2

Endpoint: `https://api.telnyx.com/v2/messages`

Authentication: `Authorization: Bearer YOUR_API_KEY` header.

```json
{
  "from": "+1your_number",
  "to": "+1recipient_number",
  "text": "Hello World"
}
```

Note the field name difference: API v1 uses `body` while API v2 uses `text`.

### Using the Python SDK

The [Telnyx Python SDK](https://developers.telnyx.com/docs/development/developer-setup) provides methods for both sending and receiving messages programmatically.

### Using Postman

Postman is a RESTful HTTP client available at [postman.com](https://www.postman.com/downloads/). Configure the appropriate endpoint, headers, and body as described above for either API version.

## Receiving Messages

There is no portal view for received SMS. To receive messages on a Telnyx number, attach a webhook URL to the number's messaging profile:

1. Navigate to **Messaging > Programmable Messaging** and select the profile.
2. Under **Inbound**, set the webhook URL where you want to receive inbound message data.
3. Save the profile.

When a message arrives, Telnyx sends a POST request to the webhook URL with the message data. You can distinguish MMS from SMS by checking the `Content-Type` header (multipart/form-data for MMS).

## MMS Messaging

### Sending MMS

**API v1 example:**

```json
{
  "from": "+1your_number",
  "to": "+1recipient_number",
  "body": {
    "text": "Did you get this image?",
    "subject": "Bear Picture",
    "media_urls": [{"img": "https://example.com/image.jpg"}]
  }
}
```

**API v2 example:**

```json
{
  "from": "+1your_number",
  "to": "+1recipient_number",
  "webhook_url": "https://your-webhook.url",
  "text": "Did you get this image?",
  "subject": "Bear Picture",
  "media_urls": ["https://example.com/image.jpg"]
}
```

### Supported File Types and Sizes

**Supported formats:** text/plain, text/vcard, image/jpeg, image/png, image/gif, video/3gpp, video/mp4

**Maximum file sizes by carrier tier:**

| Tier | Carriers | Max Size |
|------|----------|----------|
| Tier 1 | Verizon, T-Mobile, AT&T, Sprint | 1 MB |
| Tier 2 | Regional carriers | 600 KB |
| Tier 3 | Smaller carriers | 300 KB |

By default, accounts are limited to 1 MMS per second. Contact sales to increase this limit.

## Group Messaging

Group Messaging uses the MMS protocol to facilitate multi-party conversations on +1 numbers within US/CAN.

**API v2 endpoint:** `https://api.telnyx.com/v2/messages/group_mms`

```json
{
  "from": "+13125790427",
  "to": ["+18655551234", "+13125551234"],
  "text": "Greetings from Telnyx!",
  "media_urls": ["http://placekitten.com/320/240"]
}
```

**Key details:**
- Maximum 8 recipients per conversation
- Only long codes are supported (not Toll-Free or Short Code)
- Only US/CAN destinations supported
- Charged per recipient at standard MMS rates plus carrier passthrough fees
- Individual webhooks and MDRs are generated per recipient
- A `group_message_id` attribute correlates individual records to the group conversation
- Handset delivery status for non-Telnyx recipients is marked as `unknown`
