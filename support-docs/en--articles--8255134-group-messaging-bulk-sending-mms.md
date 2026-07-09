---
source_url: https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms
scraped: 2026-07-08
content_hash: a9cec5f8e703d7d9dad89cd91cb4abc482072c24d77e5127c981286657c0708f
---

Group Messaging - Bulk Sending MMS | Telnyx Help Center

[Skip to main content](#main-content)

# Group Messaging - Bulk Sending MMS

Learn how to utilize Telnyx's API v2 to bulk send MMS to up to 8 recipients.

Written by Bryan McHugh

December 13, 2025

Table of contents

# **Group messaging with the Telnyx API v2**

Group Messaging is a new feature designed specifically for businesses across +1 numbers within US / CAN that are seeking a streamlined, efficient and secure two-way conversations. Group Messaging builds upon the MMS (Multimedia Messaging Service) protocol in order to facilitate multi-party conversations.

Please find our developer documentation below, which can help you with your setup:

* https://developers.telnyx.com/docs/messaging/messages/group-messaging
* [https://developers.telnyx.com/api-reference/messages/send-a-message](https://developers.telnyx.com/api-reference/messages/send-a-message#send-a-message)

## **Sending a group message with Telnyx**

Here is an example curl request to send a group MMS message:

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

## **Behavior of group messaging webhooks / detail records**

* You should receive an individual webhook status update for each recipient following the v2 schema.
* Inbound and outbound delivery webhooks will show all participants of the group message.
* Handset delivery status is not available for Non-Telnyx recipients within in a conversation. Therefore their status will be marked as `unknown` .
* We cut individual message detail records per recipient in a group message via our portal / reporting API's.
* An additional attribute called `group_message_id` is returned to allow users to correlate each individual record to the overarching group message conversation. This is returned via API response, webhooks and is also available via detailed records.

## **Group messaging limitations**

* Group Messaging takes place over the MMS protocol and supports a maximum of 8 recipients in a conversation.
* Limitations of the MMS protocol apply to group messaging, more details on this can be found here: <https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx>
* This feature is only available via our v2 API. Please ensure you have a v2 webhook version selected on your messaging profile to ensure you receive inbound messages.
* Group messaging is charged per recipient. Standard MMS rates and corresponding carrier passthrough fees apply here.
* Only US / CAN destinations are currently supported.
* Only LONGCODES are supported, Toll Free and Short code is not supported.

---

Related Articles

[MMS Sending and Receiving](https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving)[FAQs about MMS at Telnyx](https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx)[Telnyx Verify: 2FA made easy](https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy)[Bulk Messaging with Sheets](https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets)[Update Webhook Sign Key Guide](https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide)

Did this answer your question?

😞😐😃

Table of contents
