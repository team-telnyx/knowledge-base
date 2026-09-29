---
source_url: https://support.telnyx.com/en/articles/4371498-sending-alphanumeric-sms-sender-id
title: "Sending Alphanumeric SMS - Sender ID"
description: "This article gives an overview of how you can start sending Alphanumeric… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 003def3fc410c658c6a1817e455108e7f1e73a6c5e83cb2c86a5c47824eac275
---







# Sending Alphanumeric SMS - Sender ID

This article gives an overview of how you can start sending Alphanumeric… See Telnyx guidance and requirements.




Make sure you've configured your account, such as purchasing a number, creating a messaging profile, and associating that messaging profile with that number.
​
More details about Sending SMS using API V1 can be reviewed [here](https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman).
​
POSTMAN is a RESTful HTTP client and can be downloaded from here.

Make sure to also check out our Alphanumeric capabilities in this [article](https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id).

And for [specific error codes click here](https://developers.telnyx.com/api/errors):
​

![Breaking line](_images/682991ade0be9812.png)

## **What is the Alphanumeric Sender ID?**

[Alphanumeric Sender ID](https://developers.telnyx.com/docs/messaging/messages/alphanumeric-sender-id) allows you to set your company name or brand as the Sender ID when sending one-way SMS messages to international destinations.

Alphanumeric Sender IDs must be between 3 and up to 11 characters in length. Accepted characters include both upper- and lowercase ASCII letters, the digits 0 through 9, and space: A-Z, a-z, 0-9. They may not be only numbers.

Alphanumeric Sender ID can be set dynamically on the POST request to our API when sending an SMS. You just need to set a valid alphanumeric ID in the FROM field and we will use that.
​

Consider that you need to have your account verified to Level 2 in order to use this feature. At this time, alphanumeric is not supported by the carriers in the US or Canada.

![Breaking Line](_images/682991ade0be9812.png)

## **Sending Alphanumeric SMS Via API V1**

At this stage, you are ready to send SMS.

1. Open up, [Postman](https://www.postman.com/postman). "POST" to "<https://sms.telnyx.com/messages>"
2. In "Headers", set your "x-profile-secret" to the secret under your Messaging Profile.
3. In the "Body", you can paste in the following:

```
{
"from": "Alphanumeric_id",
"to": "+1[intended recipient]",
"body": "Hello World"
}
```

## **Video demo showing sending Alphanumeric SMS via Postman**

Kudos! now you know how to send Alphanumeric SMS using API V1.

![Breaking Line](_images/682991ade0be9812.png)

## **Sending Alphanumeric SMS Via API V2**

You can send one way alphanumeric messages via our [API V2](https://developers.telnyx.com/api/messaging/send-message).

**Example:**

```
curl --location --request POST 'https://api.telnyx.com/v2/messages' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer KEYXXX' \
--data-raw '{
"from": "MyCompany",
"to": "+destination_number",
"messaging_profile_id": "abcdefghi-35bc-4c53-aa60-515de9de707c",
"text": "Hello World!",
"webhook_url": "for real time updates"
}'
```

![Breaking Line](_images/682991ade0be9812.png)
