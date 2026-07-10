---
source_url: https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets
scraped: 2026-07-08
content_hash: a00ef0e757539a0ecf2e8b36a50934074b2d00575238c93bb3f50ba497f673c5
---

Bulk Messaging with Sheets | Telnyx Help Center

[Skip to main content](#main-content)

# Bulk Messaging with Sheets

Send many SMS or MMS using Google Sheets connected to the Telnyx Messaging API

K

Written by Klane Pedrie

May 20, 2026

Table of contents

# Send Messages in Bulk Using Google Sheets with the Telnyx API

The most straightforward way to catalogue people, things, and events is by the use of spreadsheets. If you start a business or a project, chances are you won't be wanting to invest initially in highly structured databases or spend time creating robust resources to keep track of your relatively small project base.  
​  
That's where this tutorial comes in: together we will be forming a basic application that will mass send messages from a Google Sheets spreadsheet with just one run input. No need for external library setup or convoluted implementations! Everything can be done all from one source.

---

## **Prerequisites**

* Telnyx Account (<https://telnyx.com/sign-up>)

  + Telnyx API Key: <https://portal.telnyx.com/#/api-keys>
  + Telnyx Phone Number: <https://portal.telnyx.com/#/messaging/my-numbers>
  + Messaging Profile: <https://portal.telnyx.com/#/programmable-messaging/profiles>
* Access to Google Sheets (<https://www.google.com/sheets/about/>)

## Step 1 : Telnyx setup

You need to sign up for a Telnyx account to acquire a Telnyx phone number and API key. Then configure the number to have SMS capabilities.

1. **Sign up for Telnyx account**

   1. Set up a developer account with Telnyx from <https://telnyx.com/sign-up>
2. **Obtain a number with SMS capabilities for the app**

   1. After creating an account and signing in, you need to [acquire a number](https://portal.telnyx.com/#/messaging/my-numbers/buy) for the application. Search for a number by selecting your preferred 'Region' or 'Area Code'.
   2. Make sure that the number supports SMS feature(Very Important!) as it will be used by our application.
3. **Create a messaging profile**

   1. Next create a [messaging profile](https://portal.telnyx.com/#/programmable-messaging/profiles) by clicking on "Add new profile" and provide a suitable profile name to it(you do not need to provide any other detail for now).
4. **Configure the number for messaging**

   1. Go to the [numbers](https://portal.telnyx.com/#/messaging/my-numbers) page, look for the number you created and set the number's `Messaging Profile` to the profile you created in the previous step.
5. **Acquire Telnyx API key**

   1. Go to the [API Keys](https://portal.telnyx.com/#/api-keys) page and copy the API Key for the future steps. Incase there is no API Key, then create one.

***You now should now have a Telnyx Phone number and an API key. Take note of both of these.***

## Step 2 : Google Sheets Setup

Open up a fresh Google Sheets page. In here we will construct 3 columns:

* Destination Phone Number
* Message Text Body
* Status of Message

It will look like this:

![Google Sheets page section. ](_images/f3c4c869a4c3f23d.png)

## **NOTES**

You can expand with more header options as you please, but for this tutorials purpose we will only be going through those three listed above.

Afterwords, click on extensions then Apps Script:  
​

![Extensions section of the Google Sheets page. ](_images/400901b7f11d185f.png)

Here we will be adding a new script that will be linked with the sheet.   
​

![AppScript addition. ](_images/a384c5c3d5fe1d58.png)

Paste the following code below into the new script that you have created.

## Javascript Code

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

## **What does the script do?**

This Google Apps Script enables automated sending of text messages using the Telnyx API from data stored in a Google Sheet.

The script comprises several key components:

1. **Variable Declarations**: Two variables, **API\_KEY** and **fromNumber**, store the API key for authenticating requests to the Telnyx API and the phone number from which messages will be sent, respectively. Make sure to add your values into these variables.
2. **sendTelnyxMessage Function**: This function constructs and sends an HTTP POST request to the Telnyx API for sending a text message. It takes two parameters, `to` and `body`, representing the recipient's phone number and the message content. The function uses these parameters, along with the `fromNumber` and `API\_KEY`, to create the request.
3. **sendFromSheets Function**: This function reads phone numbers and message bodies from a Google Sheet, where each row contains a phone number in the first column and a message body in the second column. It iterates through each row, sending messages via the `sendTelnyxMessage` function. After attempting to send a message, it updates the third column of the sheet with the status of the sending operation ("Sent Successfully" or "Error Sending").
4. **sendAll Function**: This is a simple wrapper function that calls `sendFromSheets` to initiate the message-sending process based on the sheet's data.

In summary, the script automates the process of sending text messages to a list of recipients with personalised messages based on the contents of a Google Sheet, providing feedback on the success or failure of each message directly in the sheet.

Take note of the name of the 3rd function we created: **sendAll()**. We will be using this for the next step. Now we should be all set from the code side.  
​  
Let's go back to our spreadsheet. To enact the function to send all in a relatively pain-free way, we should create a button. Thankfully Google Sheets makes this process incredibly simple!

Click on insert drawing at the top of the page.

![Insert function on the Google Sheets page. ](_images/792fc880a7dbcc44.png)

In this menus we can use our creativity to create a good looking button, but in developer fashion for right now we will just make a textbox:

![Drawing section of the Google Sheets page.](_images/c2a949d51201b40a.png)

The button will be posted on our spreadsheet. Let's add the function to it:

![Google Sheets page. ](_images/4259152fd4476b7b.png)

We want to assign it to the function that we took note of above to it, make sure to write the exact main function name of the script here **sendAll**. Click OK.

![Assign Script section of the Google Sheets page](_images/877b42910e57e01d.png)

And that's it!

At this point, fill in the destination phone numbers and the text of the message you want to include. Once you're ready, you can click the **Send All** button which will execute on your google sheet and populate the status of the message as seen below.

## **TEST IT OUT**

Let's test our app. Once you click on the newly created **Send All** button, it will go through your list and columns until it reaches the end and send texts. It will also update the status column and inform you if the messages were delivered or not! Here's my example below:

![](_images/89f45d7175526538.png)

Take note that sending to international destinations may result in the **from number** being overridden to an Alphanumeric Sender ID. You can read more about this [here](https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id).

## Step 3 : Next Steps

From here, you have a good base to work with. We've created a simple spreadsheet application that goes through the 1st column of phone numbers and sends the text bodies of the 2nd column while giving status updates to the 3rd.  
​

We can start expanding this for future business needs. Add more things to track like sent/received statuses, order fulfilment, you can even add parsing ability to the texts you receive and highlight messages based on the context of the text message. The possibilities are limitless!

---

Related Articles

[MMS Sending and Receiving](https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving)[Setting Up a Messaging Profile](https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile)[Telnyx Messaging Error Codes](https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes)[Easy Text Marketing and Telnyx Integration](https://support.telnyx.com/en/articles/6986625-easy-text-marketing-and-telnyx-integration)[Group Messaging - Bulk Sending MMS](https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms)

Did this answer your question?

😞😐😃

Table of contents
