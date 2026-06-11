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

*Part 4 of 4 — see also: [Part 1](telnyx-sms-and-mms-messaging--part-1.md), [Part 2](telnyx-sms-and-mms-messaging--part-2.md), [Part 3](telnyx-sms-and-mms-messaging--part-3.md)*

Comprehensive guide to Telnyx programmable messaging, covering messaging profile setup, sending and receiving SMS/MMS, number pooling, alphanumeric sender IDs, SMPP, forwarding and automation, opt-out management, deliverability best practices, error codes, hosted messaging, and third-party integrations.

## Bulk Messaging with Google Sheets

Send bulk SMS/MMS from a Google Sheets spreadsheet using Google Apps Script:

1. Set up a Telnyx account, phone number, messaging profile, and API key.
2. Create a Google Sheet with columns: Destination Phone Number, Message Text Body, Status of Message.
3. Open **Extensions > Apps Script** and paste the Telnyx API script:
   - Set `API_KEY` to your Telnyx API key
   - Set `fromNumber` to your Telnyx phone number
   - The `sendFromSheets()` function iterates through rows, sends messages via `POST https://api.telnyx.com/v2/messages`, and updates the status column
4. Create a button in the sheet and assign it the `sendAll` function.

**Note:** Sending to international destinations may override the from number with an Alphanumeric Sender ID.

## Testing with Learn and Build

The Mission Control Portal includes a **Learn and Build** feature for testing:

1. Navigate to **Programmable Messaging > Learn and Build**.
2. Ensure you have a phone number and messaging profile set up.
3. Compose a test message (blank or from templates like Order Notifications, Reminders, Surveys).
4. The **From** number is auto-populated from your profile. Enter a **To** number.
5. Click **Send Message**. The raw webhook response appears in the portal.
6. Optionally proceed to Steps 4–5 for SDK installation and building a full application.
