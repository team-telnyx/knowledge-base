---
title: Telnyx Wireless and Messaging Reference
summary: A consolidated reference covering Telnyx eSIM setup (QR code and manual activation),
  manual IMSI selection, SIM connectivity logs and wireless connectivity states, SIM
  data limits and notifications, SIM theft prevention via IMEI authorization, MMS
  sending/receiving with FAQs, group messaging, bulk messaging via Google Sheets,
  number pooling, and the international voice spend limit.
sources:
- url: https://support.telnyx.com/en/articles/10067533-manual-esim-activation-guide
- url: https://support.telnyx.com/en/articles/11017501-understanding-wireless-connectivity-states-telnyx-api
- url: https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving
- url: https://support.telnyx.com/en/articles/3154822-number-pooling
- url: https://support.telnyx.com/en/articles/3403998-sim-data-limits-notifications
- url: https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx
- url: https://support.telnyx.com/en/articles/5666594-sim-connectivity-logs
- url: https://support.telnyx.com/en/articles/5761437-sim-card-theft-prevention
- url: https://support.telnyx.com/en/articles/8117401-how-to-setup-a-telnyx-esim-via-qr-code
- url: https://support.telnyx.com/en/articles/8228452-email-notification-international-spend-limit
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
- url: https://support.telnyx.com/en/articles/9183726-manual-imsi-selection-on-telnyx-sim
updated_at: 2026-07-17T08:59:32Z
---

# Telnyx Wireless and Messaging Reference

*Part 3 of 4 — see also: [Part 1](telnyx-wireless-and-messaging-reference--part-1.md), [Part 2](telnyx-wireless-and-messaging-reference--part-2.md), [Part 4](telnyx-wireless-and-messaging-reference--part-4.md)*

A consolidated reference covering Telnyx eSIM setup (QR code and manual activation), manual IMSI selection, SIM connectivity logs and wireless connectivity states, SIM data limits and notifications, SIM theft prevention via IMEI authorization, MMS sending/receiving with FAQs, group messaging, bulk messaging via Google Sheets, number pooling, and the international voice spend limit.

## Group Messaging (Bulk MMS)

Group Messaging is designed for businesses across +1 numbers within the US and Canada seeking streamlined, efficient, and secure two-way conversations. It builds upon the MMS protocol to facilitate multi-party conversations. See the [Group Messaging developer documentation](https://developers.telnyx.com/docs/messaging/messages/group-messaging) and the [Send a Message API reference](https://developers.telnyx.com/api-reference/messages/send-a-message#send-a-message).

### Sending a group message

```
curl -i -X POST \
https://api.telnyx.com/v2/messages/group_mms \
-H 'Authorization: Bearer <YOUR_TOKEN_HERE>' \
-H 'Content-Type: application/json' \
-d '{
"from": "+13125790427",
"to": ["+18655551234", "+13125551234"],
"text": "Greetings from Telnyx!",
"media_urls": ["http://placekitten.com/320/240"]
}'
```

### Webhook and detail record behavior

- Individual webhook status updates are received for each recipient following the v2 schema.
- Inbound and outbound delivery webhooks show all participants of the group message.
- Handset delivery status is not available for non-Telnyx recipients; their status is marked as `unknown`.
- Individual message detail records are cut per recipient via the portal and reporting APIs.
- An additional `group_message_id` attribute correlates each individual record to the overarching group message conversation, returned via API response, webhooks, and detailed records.

### Limitations

- Group Messaging supports a maximum of 8 recipients per conversation.
- Standard MMS protocol limitations apply.
- Only available via the v2 API; ensure a v2 webhook version is selected on the messaging profile.
- Charged per recipient; standard MMS rates and carrier passthrough fees apply.
- Only US and CAN destinations are supported.
- Only LONGCODES are supported; Toll-Free and Short Code are not supported.

## Bulk Messaging with Google Sheets

A Google Apps Script can automate sending SMS messages from a Google Sheet via the Telnyx API.

### Prerequisites

- Telnyx account with API key, phone number, and messaging profile
- Access to Google Sheets

### Telnyx setup

1. Sign up for a Telnyx account at [telnyx.com/sign-up](https://telnyx.com/sign-up).
2. [Acquire a number](https://portal.telnyx.com/#/messaging/my-numbers/buy) with SMS capabilities.
3. Create a [messaging profile](https://portal.telnyx.com/#/programmable-messaging/profiles).
4. Configure the number's Messaging Profile to the created profile.
5. Acquire a Telnyx API key from the [API Keys](https://portal.telnyx.com/#/api-keys) page.

### Google Sheets setup

Create a sheet with three columns: Destination Phone Number, Message Text Body, and Status of Message. Open **Extensions** → **Apps Script** and paste the following code:

```
var API_KEY = "your_telnyx_api_key";
var fromNumber = "+your_telnyx_phone_number";

function sendTelnyxMessage(to, body) {
  var data = {
    'to': to,
    'from': fromNumber,
    'text': body
  };
  var options = {
    'method' : 'post',
    'payload' : JSON.stringify(data)
  };
  options.headers = {
    'Content-Type': 'application/json',
    "Accept": "application.json",
    "Authorization": "Bearer " + API_KEY
  }
  UrlFetchApp.fetch('https://api.telnyx.com/v2/messages', options);
}

function sendFromSheets(){
  var sheet = SpreadsheetApp.getActiveSheet();
  var startRow = 2;
  var numRows = sheet.getLastRow() - 1;
  var dataRange = sheet.getRange(startRow, 1, numRows, 2);
  var data = dataRange.getValues();

  for (var i = 0; i < data.length; i++){
    var row = data[i];
    var status;
    try {
      var response_data = sendTelnyxMessage("+" + row[0], row[1]);
      status = "Sent Successfully";
    } catch(err) {
      Logger.log(err);
      status = "Error Sending";
    }
    sheet.getRange(startRow + i, 3).setValue(status);
  }
}

function sendAll(){
  sendFromSheets();
}
```

The script reads phone numbers and message bodies from the sheet, sends each via the Telnyx API, and updates the third column with the status ("Sent Successfully" or "Error Sending").

### Adding a send button

Insert a drawing (e.g. a textbox) on the sheet via **Insert** → **Drawing**, then assign the script function `sendAll` to it. Clicking the button iterates through the list and sends messages, updating the status column.

Sending to international destinations may result in the `from` number being overridden to an Alphanumeric Sender ID.

## Number Pooling

Number Pooling allows the automatic selection of originating numbers in a message request from a pool of all numbers assigned to a given messaging profile. It maintains balance across all numbers to ensure high deliverability with all carriers, helping maintain number health amid stricter carrier regulations on SMS throughput.

### Maximum throughput

There is a limit of 6 SMS per minute per virtual number for SMS sent from a long code due to local carrier regulations. Sending more quickly results in rejection. To increase throughput, purchase more numbers and spread traffic across them (e.g. 10 numbers = 10 SMS per second). This does not apply to messages sent from a short code or Toll-Free number.

### Enabling the feature

1. Navigate to the messaging section of the portal.
2. Click the edit icon on the chosen messaging profile.
3. Click on number pooling to enable the feature.

See the [developer documentation](https://developers.telnyx.com/api/messaging/send-message) for sending a message using number pooling.

### Advanced options

- **Weights:** The ratio of toll-free vs long codes chosen when sending messages. For example, with 2 Toll-Free and 5 Long Code numbers, Long Code weight 1 and Toll-Free weight 10, sending 1000 messages results in each long code selected ~40 times and each toll-free ~400 times (10x more often). Frequencies differ slightly due to the distributed nature of the feature.
- **Skip Unhealthy Numbers:** Automatically removes unhealthy numbers from the pool. Health metrics consider deliverability rate and spam detection by upstream carriers. Numbers with deliverability below 25% or spam detection over 75% are considered unhealthy.
- **Sticky Sender:** Remembers which originating number was last used to send a message to a given destination and tries to use the same originating number for future communications.
- **Geomatch:** Sends messages from a number with the same local area code as the recipient, if available in the pool. If no matching area code is available, a random healthy number is chosen. Geomatch currently only matches US area codes.
