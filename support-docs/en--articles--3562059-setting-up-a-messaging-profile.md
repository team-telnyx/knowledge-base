---
source_url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
scraped: 2026-06-11
---

Setting Up a Messaging Profile | Telnyx Help Center

[Skip to main content](#main-content)

# Setting Up a Messaging Profile

Here we will explain how to get SMS ready with Messaging Profiles on Telnyx.

Written by Telnyx Sales

September 16, 2024

Table of contents

# **Video Walk-through for Setting up a Messaging Profile**

Are you ready to start sending SMS with Telnyx? Follow the video below to learn how to set up a Messaging Profile!

# What is a messaging profile?

A Messaging Profile is a configuration to manage your inbound and outbound messaging settings. It's the simplest way to configure how you send and receive messages on your phone number. An SMS-capable phone number is SMS-enabled by assigning it to a Messaging Profile.

## Where can I create a messaging profile?

Click on the [Programmable Messaging](https://portal.telnyx.com/#/programmable-messaging/profiles) tab in the navigation menu on the left-hand side of the Telnyx Mission Control Portal. Click **Add New Profile** on the top left-hand side.

[![Include a unique Profile Name](https://downloads.intercomcdn.com/i/o/1147285756/cb27b3064a3c0364b481d5f5/Screenshot+Capture+-+2024-08-15+-+15-48-31.png?expires=1781168400&signature=1713b892c07baa8c2ae453caba17f7d82a27d66a8053292acf3224b60b371abf&req=dSEjEct2mIZaX%2FMW1HO4zVASmYRlwlYR4sPSDGlqfDb%2BVKqHzZiabXUFoCj7%0A%2Bmoc5uRvmdS5ZoLxM%2FU%3D%0A)](https://downloads.intercomcdn.com/i/o/1147285756/cb27b3064a3c0364b481d5f5/Screenshot+Capture+-+2024-08-15+-+15-48-31.png?expires=1781168400&signature=1713b892c07baa8c2ae453caba17f7d82a27d66a8053292acf3224b60b371abf&req=dSEjEct2mIZaX%2FMW1HO4zVASmYRlwlYR4sPSDGlqfDb%2BVKqHzZiabXUFoCj7%0A%2Bmoc5uRvmdS5ZoLxM%2FU%3D%0A)

For new users, you will see the message below instead. Simply click on **Create your first profile** to begin.

[![](https://downloads.intercomcdn.com/i/o/1148552370/ac68c4f0f454b1bb91263afe/Screenshot+Capture+-+2024-08-16+-+12-47-38.png?expires=1781168400&signature=694279179987bdf7e1683e425a25317253c7227ebde510b04208637450e4576c&req=dSEjHsx7n4JYWfMW1HO4zVIIVCwsnzSQMwp7%2FdVG%2FbGaEcNkDZ%2BtkdSkHMiC%0AVM0Q1LifVC0zZsExoHo%3D%0A)](https://downloads.intercomcdn.com/i/o/1148552370/ac68c4f0f454b1bb91263afe/Screenshot+Capture+-+2024-08-16+-+12-47-38.png?expires=1781168400&signature=694279179987bdf7e1683e425a25317253c7227ebde510b04208637450e4576c&req=dSEjHsx7n4JYWfMW1HO4zVIIVCwsnzSQMwp7%2FdVG%2FbGaEcNkDZ%2BtkdSkHMiC%0AVM0Q1LifVC0zZsExoHo%3D%0A)

## Profile Information

Enter a unique Profile Name for your Messaging Profile, by default the API version 2 is selected as this is our latest and most up-to-date API.

[![](https://downloads.intercomcdn.com/i/o/1147289041/55db1678db10540de9379fab/Screenshot+Capture+-+2024-08-15+-+15-51-59.png?expires=1781168400&signature=b1facc496aabdccbfea651dba84dda267ee47cdee6cdd8807a7d66ea3f55297c&req=dSEjEct2lIFbWPMW1HO4zdD%2BBHAEjQsnKjYi2AWf%2B%2F0f9yyOibgnUfpIJe1d%0AYMqaqmICf5l5unP5vvI%3D%0A)](https://downloads.intercomcdn.com/i/o/1147289041/55db1678db10540de9379fab/Screenshot+Capture+-+2024-08-15+-+15-51-59.png?expires=1781168400&signature=b1facc496aabdccbfea651dba84dda267ee47cdee6cdd8807a7d66ea3f55297c&req=dSEjEct2lIFbWPMW1HO4zdD%2BBHAEjQsnKjYi2AWf%2B%2F0f9yyOibgnUfpIJe1d%0AYMqaqmICf5l5unP5vvI%3D%0A)

## **Inbound Settings**

Configure any other desired settings, such as webhook URLs as your Inbound Settings.

[![Configure your inbound settings](https://downloads.intercomcdn.com/i/o/1147290106/39f275bdd04156683a626491/Screenshot+Capture+-+2024-08-15+-+15-53-14.png?expires=1781168400&signature=aa6ad6013b2e23a06be830a67ae808117a18be6b7e31908edee1be32b6bdd22e&req=dSEjEct3nYBfX%2FMW1HO4zdEBUXowcRGBrTBwfHtEWo8Qb8hMf6ZowPoM3333%0A8S%2FshN%2BiRPISC%2FsCks0%3D%0A)](https://downloads.intercomcdn.com/i/o/1147290106/39f275bdd04156683a626491/Screenshot+Capture+-+2024-08-15+-+15-53-14.png?expires=1781168400&signature=aa6ad6013b2e23a06be830a67ae808117a18be6b7e31908edee1be32b6bdd22e&req=dSEjEct3nYBfX%2FMW1HO4zdEBUXowcRGBrTBwfHtEWo8Qb8hMf6ZowPoM3333%0A8S%2FshN%2BiRPISC%2FsCks0%3D%0A)

You can read more about webhooks [here](https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks). A webhook URL is required to deliver inbound messages to your messaging application.

## **Outbound Settings**

## Alphanumeric Sender ID

You can assign an Alpha Numeric Sender ID value, which can be used for one-way outbound international messages. Generally, these would be your clients' **business names**.

[![](https://downloads.intercomcdn.com/i/o/1147291386/99bd36ef74ad22d2a37bc0e0/Screenshot+Capture+-+2024-08-15+-+15-54-24.png?expires=1781168400&signature=c608da2e5a8cc7a2708544982934cd151b46db3b0dd95349c2952385b942621f&req=dSEjEct3nIJXX%2FMW1HO4zchlHZDHuu5HOAJMdmZ9nDEmA39j%2BUU3DP0K%2Bo9q%0AENn8VqFYZzCIArTgElM%3D%0A)](https://downloads.intercomcdn.com/i/o/1147291386/99bd36ef74ad22d2a37bc0e0/Screenshot+Capture+-+2024-08-15+-+15-54-24.png?expires=1781168400&signature=c608da2e5a8cc7a2708544982934cd151b46db3b0dd95349c2952385b942621f&req=dSEjEct3nIJXX%2FMW1HO4zchlHZDHuu5HOAJMdmZ9nDEmA39j%2BUU3DP0K%2Bo9q%0AENn8VqFYZzCIArTgElM%3D%0A)

### Manage Allowed Destinations

You can set a list of international destinations that you want to allow this profile to send messages to, or restrict countries to minimize any fraudulent abuse.

[![](https://downloads.intercomcdn.com/i/o/1147293212/a7826acd0bd67d97e974e606/Screenshot+Capture+-+2024-08-15+-+15-56-41.png?expires=1781168400&signature=8fbaa3796ae67bfe0534c416678c67f2f611ca0664a1cb07caceb6177b89c88b&req=dSEjEct3noNeW%2FMW1HO4zQiN8U%2BEyi6QWB1bDm3WWZuZERJ8fwg4tAHKn7z3%0AiH4PV212qCQP%2FzdaOpA%3D%0A)](https://downloads.intercomcdn.com/i/o/1147293212/a7826acd0bd67d97e974e606/Screenshot+Capture+-+2024-08-15+-+15-56-41.png?expires=1781168400&signature=8fbaa3796ae67bfe0534c416678c67f2f611ca0664a1cb07caceb6177b89c88b&req=dSEjEct3noNeW%2FMW1HO4zQiN8U%2BEyi6QWB1bDm3WWZuZERJ8fwg4tAHKn7z3%0AiH4PV212qCQP%2FzdaOpA%3D%0A)

### Number Pooling

Enable number pooling to deliver messages from a pool of multiple phone numbers that are associated with your messaging profile to handle higher volume. Read more information [here](https://support.telnyx.com/en/articles/3154822-number-pooling).

[![](https://downloads.intercomcdn.com/i/o/1147295210/58e7719a73b13fbd64a423eb/Screenshot+Capture+-+2024-08-15+-+15-58-28.png?expires=1781168400&signature=e93bf81fc6827da3f63c5bc2d9a3d4614b47fc2c433968b434c674357e580bdd&req=dSEjEct3mINeWfMW1HO4zTDH0RjVJjTXCUcaKNyrBsM2Dez%2F3irijHhonpFw%0ADLZ51C%2Buf%2F%2FoikuZfXo%3D%0A)](https://downloads.intercomcdn.com/i/o/1147295210/58e7719a73b13fbd64a423eb/Screenshot+Capture+-+2024-08-15+-+15-58-28.png?expires=1781168400&signature=e93bf81fc6827da3f63c5bc2d9a3d4614b47fc2c433968b434c674357e580bdd&req=dSEjEct3mINeWfMW1HO4zTDH0RjVJjTXCUcaKNyrBsM2Dez%2F3irijHhonpFw%0ADLZ51C%2Buf%2F%2FoikuZfXo%3D%0A)

### **MMS Fallback**

Enable this toggle to send MMS messages to any destination, even to those where MMS isn't supported, by converting them to SMS with the media URL appended to the body of the message.  
​

### **MMS Transcoding**

Enable this toggle to compress MMS media files (images and videos) to meet carrier size restrictions, allowing you to send MMS up to 5MB in size.

[![](https://downloads.intercomcdn.com/i/o/1147295816/90c9f84d9c307da363a3d226/Screenshot+Capture+-+2024-08-15+-+15-59-33.png?expires=1781168400&signature=5f8751de58b4530446fd032ebb5e45402865f0cd9f5efa694404cd73306f2542&req=dSEjEct3mIleX%2FMW1HO4zYC5sspCn8WjOEGsB%2BScKMKKZdwUDpo7B9U%2BQQKj%0AIPO6dv85YJtoXm0JKgg%3D%0A)](https://downloads.intercomcdn.com/i/o/1147295816/90c9f84d9c307da363a3d226/Screenshot+Capture+-+2024-08-15+-+15-59-33.png?expires=1781168400&signature=5f8751de58b4530446fd032ebb5e45402865f0cd9f5efa694404cd73306f2542&req=dSEjEct3mIleX%2FMW1HO4zYC5sspCn8WjOEGsB%2BScKMKKZdwUDpo7B9U%2BQQKj%0AIPO6dv85YJtoXm0JKgg%3D%0A)

Click **Save** to create the messaging profile!

### **Enable Daily Spend Limit Per Connection**

Define the maximum amount of money in USD that can be spent on outbound messages per day. A day will reset at 00:00:00 UTC. Learn more about it [here](https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits).

[![](https://downloads.intercomcdn.com/i/o/1181662667/d98226d36ae07ac2a16c45c3/Screenshot+from+2024-09-16+15-59-43.png?expires=1781168400&signature=516805e0e1dc8a3af4f09c7863bdd32919f92d6812134bd90e292951c0022713&req=dSEvF894n4dZXvMW1HO4zfc4QqaWdzbVA%2FSEODPZMQbfjF6JOZGRs71t0xGn%0AyXMc5SHpmOY9FtGLrhw%3D%0A)](https://downloads.intercomcdn.com/i/o/1181662667/d98226d36ae07ac2a16c45c3/Screenshot+from+2024-09-16+15-59-43.png?expires=1781168400&signature=516805e0e1dc8a3af4f09c7863bdd32919f92d6812134bd90e292951c0022713&req=dSEvF894n4dZXvMW1HO4zfc4QqaWdzbVA%2FSEODPZMQbfjF6JOZGRs71t0xGn%0AyXMc5SHpmOY9FtGLrhw%3D%0A)

### Where can I find the Messaging Profile ID?

Once you've created the messaging profile successfully, you can go back into the settings to identify the Unique ID.

[![](https://downloads.intercomcdn.com/i/o/1147297630/8b43781dd3928824bfc9747f/Screenshot+Capture+-+2024-08-15+-+16-01-26.png?expires=1781168400&signature=6cd6cf56ee9de8a1dadbf6c0afe81b12bc6db11322a2188beb2aee1b7d4b6009&req=dSEjEct3modcWfMW1HO4zczqb%2FPz%2Bhy6TDz6KuJHnQqVVf0xMaHPGwo%2BS2%2B6%0AzOTT8pVgxFbgascy%2FBo%3D%0A)](https://downloads.intercomcdn.com/i/o/1147297630/8b43781dd3928824bfc9747f/Screenshot+Capture+-+2024-08-15+-+16-01-26.png?expires=1781168400&signature=6cd6cf56ee9de8a1dadbf6c0afe81b12bc6db11322a2188beb2aee1b7d4b6009&req=dSEjEct3modcWfMW1HO4zczqb%2FPz%2Bhy6TDz6KuJHnQqVVf0xMaHPGwo%2BS2%2B6%0AzOTT8pVgxFbgascy%2FBo%3D%0A)

## Do I need to assign the Messaging Profile to my numbers?

Yes! Once you’ve created a Messaging Profile, you’ll need to associate the profile with a phone number so our API can deliver inbound messages and accept outbound messages from your number.

1. Click on [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) in the navigation menu on the left-hand side of the portal.
2. Find the number you want to add to your messaging profile.

   [![](https://downloads.intercomcdn.com/i/o/1147302539/f4135207b05b50c9535eba63/Screenshot+2024-08-15+at+4_04_48%E2%80%AFPM+%282%29.png?expires=1781168400&signature=3a3df532957d2c44631f6e4eec39c43468aae119f4f3b27f8fffe7eefccbe3c6&req=dSEjEcp%2Bn4RcUPMW1HO4zUHtf0lDk%2F7B04gN6FDcaSnrceamtMaLHPYCBbgo%0Aqj07%0A)](https://downloads.intercomcdn.com/i/o/1147302539/f4135207b05b50c9535eba63/Screenshot+2024-08-15+at+4_04_48%E2%80%AFPM+%282%29.png?expires=1781168400&signature=3a3df532957d2c44631f6e4eec39c43468aae119f4f3b27f8fffe7eefccbe3c6&req=dSEjEcp%2Bn4RcUPMW1HO4zUHtf0lDk%2F7B04gN6FDcaSnrceamtMaLHPYCBbgo%0Aqj07%0A)
3. Under the Messaging Profile column, hover and click on the edit (pencil) button.
4. Choose the Messaging Profile you'd like associated with the phone number from the dropdown.

   [![](https://downloads.intercomcdn.com/i/o/1147304187/504fae6f5cc5d27bff3dbc3d/Screenshot+2024-08-15+at+4_07_59%E2%80%AFPM+%282%29.png?expires=1781168400&signature=5ee08d70cac77ca982562f39338f4872d2c69fa80b7344caf84d8db775aeb9b0&req=dSEjEcp%2BmYBXXvMW1HO4zTEUcb7NBOMKwsQE%2BxmXo2riKk1xDb3jl3PzvAIr%0AhUbZ%0A)](https://downloads.intercomcdn.com/i/o/1147304187/504fae6f5cc5d27bff3dbc3d/Screenshot+2024-08-15+at+4_07_59%E2%80%AFPM+%282%29.png?expires=1781168400&signature=5ee08d70cac77ca982562f39338f4872d2c69fa80b7344caf84d8db775aeb9b0&req=dSEjEcp%2BmYBXXvMW1HO4zTEUcb7NBOMKwsQE%2BxmXo2riKk1xDb3jl3PzvAIr%0AhUbZ%0A)
5. Confirm the cost changes associated by clicking **accept**.

   [![](https://downloads.intercomcdn.com/i/o/1147306231/be949e8186cd6650b6dbc20b/Screenshot+Capture+-+2024-08-15+-+16-11-24.png?expires=1781168400&signature=26b27010d97278cc4360babb698f4aa4b9d89f78f7512611df3ce2cc4f44d35b&req=dSEjEcp%2Bm4NcWPMW1HO4zTiIOIYL245mVKD8TGwV2rueNhvo%2FeZq%2B2VTG7HT%0A8aN0%0A)](https://downloads.intercomcdn.com/i/o/1147306231/be949e8186cd6650b6dbc20b/Screenshot+Capture+-+2024-08-15+-+16-11-24.png?expires=1781168400&signature=26b27010d97278cc4360babb698f4aa4b9d89f78f7512611df3ce2cc4f44d35b&req=dSEjEcp%2Bm4NcWPMW1HO4zTiIOIYL245mVKD8TGwV2rueNhvo%2FeZq%2B2VTG7HT%0A8aN0%0A)

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

Table of contents
