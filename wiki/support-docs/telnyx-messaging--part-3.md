---
title: Telnyx Messaging
summary: A consolidated guide to Telnyx messaging capabilities, covering SMS and MMS
  sending and receiving, messaging profile configuration, Zapier-based automations,
  third-party integrations, bulk and group messaging, and frequently asked questions
  about MMS limits, file types, and delivery behavior.
sources:
- url: https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving
- url: https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number
- url: https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier
- url: https://support.telnyx.com/en/articles/3270136-telnyx-global-sims-faqs
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
- url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
- url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
- url: https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number
- url: https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx
- url: https://support.telnyx.com/en/articles/7885470-chiro8000-and-telnyx-integration
- url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
- url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
updated_at: 2026-08-05T13:35:00Z
---

# Telnyx Messaging

*Part 3 of 3 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 2](telnyx-messaging--part-2.md)*

A consolidated guide to Telnyx messaging capabilities, covering SMS and MMS sending and receiving, messaging profile configuration, Zapier-based automations, third-party integrations, bulk and group messaging, and frequently asked questions about MMS limits, file types, and delivery behavior.

## Third-Party Integrations

### Textable

[Textable](https://textable.app/signup) is a VoIP texting app that integrates with Telnyx V2. To set it up:

1. Sign up at Textable, select **Telnyx V2** as the provider, and enter the Telnyx phone number (DID) you want to use. Leave the **Account ID** field empty.
2. In the Telnyx Portal, create a Messaging Profile (e.g., named "Textable"). On the **Inbound** tab, set the protocol to HTTP and the webhook URL to `https://app01.textable.co/receive?provider=telnyxv2`.
3. Create an API V2 key in the Telnyx Portal and paste it into the **Access Token** field in Textable.
4. In Telnyx, go to **Numbers**, select the number, click **Routing**, and assign the "Textable" messaging profile under **SMS Messaging Profile**.
5. Download the Textable app from the [App Store](https://apps.apple.com/us/app/textable-voip-texting/id1355564896?ls=1) or [Google Play](https://play.google.com/store/apps/details?id=co.textable.textable&hl=en&utm_source=textable&utm_campaign=website&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1).

### Chiro8000

Chiro8000 is a chiropractic practice management system that integrates with Telnyx for appointment reminder texts. Setup steps:

1. Sign up at [telnyx.com/sign-up](https://telnyx.com/sign-up) and add funds (Telnyx is prepaid).
2. Purchase a local SMS-enabled number from the Mission Control Portal.
3. Create a messaging profile and assign it to the number under **My Numbers**.
4. In Chiro8000, go to **Options > Calendar**, enable **Telnyx**, open **Telnyx Configuration**, and enter your API key and Telnyx phone number.
5. Configure appointment reminders under **Reminders** in the Chiro8000 calendar.

For US local numbers, 10DLC compliance is required as of December 1, 2024. Toll-free numbers also require a (less expensive) verification process. Contact [10DLCquestions@telnyx.com](mailto:10DLCquestions@telnyx.com) for help. Optional steps include setting up low balance notifications, auto-recharge, two-factor authentication, and daily voice spend limits.

## Bulk Messaging with Google Sheets

A no-database approach to bulk SMS uses Google Sheets and Apps Script. Prerequisites: a Telnyx account with an API key, an SMS-enabled phone number, and a messaging profile assigned to that number.

In a Google Sheet, create three columns: **Destination Phone Number**, **Message Text Body**, and **Status of Message**. Open **Extensions > Apps Script** and paste the following script, replacing `API_KEY` and `fromNumber` with your values:

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
    'payload': JSON.stringify(data)
  };
  options.headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + API_KEY
  };
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
      sendTelnyxMessage("+" + row[0], row[1]);
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

The script reads each row, sends the message via the Telnyx V2 API, and writes the result to the third column. Insert a drawing on the sheet, assign it to the `sendAll` function, and click the button to dispatch all messages. Sending to international destinations may override the `from` number with an Alphanumeric Sender ID.

## Telnyx Global SIMs (IoT)

Telnyx also offers IoT SIM and eSIM products for data connectivity. Key facts:

- SIMs are **data only** — no voice.
- **Two-way SMS** is supported via AT commands.
- SIMs work internationally; see the [International IoT SIM Coverage](https://telnyx.com/iot-global-coverage#table-iot-global-coverage) page.
- US orders under 50 SIMs ship via USPS (a few days to most US destinations; longer to Alaska and Hawaii). Orders over 50 SIMs should contact sales for expedited shipping. International orders may take more than 7 business days.
- Pricing: $1 per triple-cut plastic SIM or MFF2 embedded SIM chip, $0.70 per over-the-air eSIM. Monthly recurring charge is $2 per active SIM and $0.20 per inactive SIM. Data starts at $0.0125 per MB, billed to the nearest MB, with pay-as-you-go available.
- No fees for suspending or reactivating SIMs; disabled SIMs have no MRC.
- SIMs are auto-provisioned once registered to an account in standby or active state.
- Data limits can be set per SIM or SIM Group via the portal and API, with near-real-time usage reporting. See [SIM Reporting & Analytics](sim-reporting-analytics.md).
- Unbranded SIMs are available for resellers with a minimum order of 5,000.
- SIMs can be transferred between Telnyx accounts by deleting from the source account and re-registering on the destination account using the registration code. Contact [support@telnyx.com](mailto:support@telnyx.com) for help with registration codes.
