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
