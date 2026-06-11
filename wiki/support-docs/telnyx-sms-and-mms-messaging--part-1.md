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
