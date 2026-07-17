---
source_url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
title: "Setting Up a Messaging Profile"
description: "Here we will explain how to get SMS ready with Messaging Profiles on Telnyx. See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 1e8af24eb52bb449831be3a889423fe9f4bd2032e12b6f18cdbb46ab3bc4c239
---







# Setting Up a Messaging Profile

Here we will explain how to get SMS ready with Messaging Profiles on Telnyx. See Telnyx guidance and requirements.




## **Video Walk-through for Setting up a Messaging Profile**

Are you ready to start sending SMS with Telnyx? Follow the video below to learn how to set up a Messaging Profile!

## What is a messaging profile?

A Messaging Profile is a configuration to manage your inbound and outbound messaging settings. It's the simplest way to configure how you send and receive messages on your phone number. An SMS-capable phone number is SMS-enabled by assigning it to a Messaging Profile.

## Where can I create a messaging profile?

Click on the [Programmable Messaging](https://portal.telnyx.com/#/programmable-messaging/profiles) tab in the navigation menu on the left-hand side of the Telnyx Mission Control Portal. Click **Add New Profile** on the top left-hand side.

![Include a unique Profile Name](_images/887ec359011e58c2.png)

For new users, you will see the message below instead. Simply click on **Create your first profile** to begin.

![](_images/a1624e7454c073f1.png)

## Profile Information

Enter a unique Profile Name for your Messaging Profile, by default the API version 2 is selected as this is our latest and most up-to-date API.

![](_images/a9e9fc63296b64ea.png)

## **Inbound Settings**

Configure any other desired settings, such as webhook URLs as your Inbound Settings.

![Configure your inbound settings](_images/2395c0bace2ed4cd.png)

You can read more about webhooks [here](https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks). A webhook URL is required to deliver inbound messages to your messaging application.

## **Outbound Settings**

## Alphanumeric Sender ID

You can assign an Alpha Numeric Sender ID value, which can be used for one-way outbound international messages. Generally, these would be your clients' **business names**.

![](_images/7146bd8e81b621cb.png)

### Manage Allowed Destinations

You can set a list of international destinations that you want to allow this profile to send messages to, or restrict countries to minimize any fraudulent abuse.

![](_images/f1c8d3f0879ef032.png)

### Number Pooling

Enable number pooling to deliver messages from a pool of multiple phone numbers that are associated with your messaging profile to handle higher volume. Read more information [here](https://support.telnyx.com/en/articles/3154822-number-pooling).

![](_images/2e902a0ecb76a1bf.png)

### **MMS Fallback**

Enable this toggle to send MMS messages to any destination, even to those where MMS isn't supported, by converting them to SMS with the media URL appended to the body of the message.
​

### **MMS Transcoding**

Enable this toggle to compress MMS media files (images and videos) to meet carrier size restrictions, allowing you to send MMS up to 5MB in size.

![](_images/c6b8a516482b8a66.png)

Click **Save** to create the messaging profile!

### **Enable Daily Spend Limit Per Connection**

Define the maximum amount of money in USD that can be spent on outbound messages per day. A day will reset at 00:00:00 UTC. Learn more about it [here](https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits).

![](_images/1ae323edbf305d32.png)

### Where can I find the Messaging Profile ID?

Once you've created the messaging profile successfully, you can go back into the settings to identify the Unique ID.

![](_images/5f17585a1bf4f9cb.png)

## Do I need to assign the Messaging Profile to my numbers?

Yes! Once you’ve created a Messaging Profile, you’ll need to associate the profile with a phone number so our API can deliver inbound messages and accept outbound messages from your number.

1. Click on [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) in the navigation menu on the left-hand side of the portal.
2. Find the number you want to add to your messaging profile.

   ![](_images/cdee66ce5d34f207.png)
3. Under the Messaging Profile column, hover and click on the edit (pencil) button.
4. Choose the Messaging Profile you'd like associated with the phone number from the dropdown.

   ![](_images/d6138d1bd0cd52e7.png)
5. Confirm the cost changes associated by clicking **accept**.

   ![](_images/dba73f834b13add4.png)

## **What next?**

Your messaging profile should now show an updated count under “# of phone numbers” column on your Messaging Profiles page. If the count has not changed, refresh your page to update.

You're now ready to send and receive messages using our [API](https://developers.telnyx.com/api/messaging).

Don't forget that you'll need an [API Key](https://portal.telnyx.com/#/app/api-keys) to authenticate your outbound API requests.

---

## **Messaging Profile Updates - 1st March 2024**

Existing customers who use our programmable messaging services will have received an email on the 8th of February 2024 with the following subject:

**March 1st 2024: Important: New Security Controls for Messaging.**

In order to improve the security of Telnyx’s Messaging platform for end users, we will be implementing two changes effective **March 1st, 2024:**

* Editing / Creating a Messaging or Verify Profile via the Portal and API will require users to configure [whitelisted destination countries](#h_c6b0cebb82) for outbound termination.

  + Existing profiles will not be affected unless edited.
* When attempting to send to non-US destinations, Telnyx now requires a default [Alphanumeric sender ID](#h_08c67c1b03) to be named on the Messaging Profile. In the past, this was not required.

---

Related Articles

[MMS Sending and Receiving](https://support.telnyx.com/en/articles/3102823-mms-sending-and-receiving)[Automated Replies for Messages using Zapier](https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier)[Textable Setup Guide](https://support.telnyx.com/en/articles/3685327-textable-setup-guide)[Telnyx Messaging Error Codes](https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes)[Group Messaging - Bulk Sending MMS](https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms)

Did this answer your question?

😞😐😃
