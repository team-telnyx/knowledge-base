---
source_url: https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number
scraped: 2026-06-11
---

Receiving SMS on your Telnyx number | Telnyx Help Center

[Skip to main content](#main-content)

# Receiving SMS on your Telnyx number

Begin your journey with Telnyx: Learn how to sign up and set up a Mission Control account effectively.

Written by Shubam

December 27, 2024

Table of contents

# **Prerequisites for Receiving SMS**

Make sure you've configured your account, such as purchasing a number, creating a messaging profile, and associating that messaging profile with that number.

​

[![Breaking Line](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)

## **Receiving SMS on Telnyx**

First of all, there is no provision on the Telnyx portal where you can receive the SMS.

In order to receive SMS on your Telnyx purchased number, you need to attach a webhook to the number's respective messaging profile.

You can find more details about Webhook in the below section of this article.

So let's take this example DID which is connected to a **Telnyx** messaging profile.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1313556744/c39eea25a1fb613de734d9035117/image.png?expires=1781168400&signature=390b7ab647e0bc98629829c60334def878ac5cf3fadde639be8df45c1c029686&req=dSMmFcx7m4ZbXfMW1HO4zQ%2B2w8HkcHKytOkK8hw73CFJRRkKZHtS5sI186eV%0AljRNkENaxMHtdaPgiaI%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1313556744/c39eea25a1fb613de734d9035117/image.png?expires=1781168400&signature=390b7ab647e0bc98629829c60334def878ac5cf3fadde639be8df45c1c029686&req=dSMmFcx7m4ZbXfMW1HO4zQ%2B2w8HkcHKytOkK8hw73CFJRRkKZHtS5sI186eV%0AljRNkENaxMHtdaPgiaI%3D%0A)

Now, in the messaging profile section, you need to attach a webhook, as highlighted in the green box. To do this, go to **Messaging > Programmable Messaging**, select the messaging profile, and then select **Inbound**.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1313558973/b20879017159fe3668b391d8bb5c/image.png?expires=1781168400&signature=bc30f952a7d8b980775d38d4bcf3f6486d7c43bb7dc6462d6c87b938b9fd383a&req=dSMmFcx7lYhYWvMW1HO4zZAGxK0X9B0HLN3U8HFHoUw%2BZdh9OIxvHq3ohkKx%0AfYYrl%2BoQr0g%2FJLKo2gI%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1313558973/b20879017159fe3668b391d8bb5c/image.png?expires=1781168400&signature=bc30f952a7d8b980775d38d4bcf3f6486d7c43bb7dc6462d6c87b938b9fd383a&req=dSMmFcx7lYhYWvMW1HO4zZAGxK0X9B0HLN3U8HFHoUw%2BZdh9OIxvHq3ohkKx%0AfYYrl%2BoQr0g%2FJLKo2gI%3D%0A)

Webhook can be customized and has to be set up by the customer, however, for this demo, we have generated a webhook from this website <https://webhook.site/>

Once the webhook is saved in the messaging profile, the content of your incoming SMS to Telnyx number can be seen in the webhook.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1313560409/7a4105a2b5e7a0f74312d3696282/image.png?expires=1781168400&signature=e77bc74356bc2c883707aa12ea67f61264361557678b09c9e1f95cabdfc6d794&req=dSMmFcx4nYVfUPMW1HO4zQavMNXmgZAL2nfXzZGMS427bUDxGG0m9r9L%2F0cn%0AuN83buHIf30B7JVeudU%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1313560409/7a4105a2b5e7a0f74312d3696282/image.png?expires=1781168400&signature=e77bc74356bc2c883707aa12ea67f61264361557678b09c9e1f95cabdfc6d794&req=dSMmFcx4nYVfUPMW1HO4zQavMNXmgZAL2nfXzZGMS427bUDxGG0m9r9L%2F0cn%0AuN83buHIf30B7JVeudU%3D%0A)

The below image shows SMS was sent to the Telnyx number i.e. +13125790011 with all the other details.

[![Sent SMS dashboard. ](https://downloads.intercomcdn.com/i/o/236771146/8b5ea594a5153fc21f31940d/Screenshot+2020-08-16+at+10.51.01+pm.png?expires=1781168400&signature=9a8a44cea1157104ad0a90481553a71b95dcb9048b272d7b7dc05bbfb1e05e86&req=diMhEc5%2FnIVZFb4f3HP0gOaMUucznIReEH84P4CN3tY6L94lKLtS9rSbag4g%0AeAoJjKTrqo0F5GjX0w%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/236771146/8b5ea594a5153fc21f31940d/Screenshot+2020-08-16+at+10.51.01+pm.png?expires=1781168400&signature=9a8a44cea1157104ad0a90481553a71b95dcb9048b272d7b7dc05bbfb1e05e86&req=diMhEc5%2FnIVZFb4f3HP0gOaMUucznIReEH84P4CN3tY6L94lKLtS9rSbag4g%0AeAoJjKTrqo0F5GjX0w%3D%3D%0A)

[![Breaking Line](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)

## **Video demo showing how to receive SMS on your Telnyx Number**

Kudos! now you know how to receive SMS on your Telnyx number.

[![Breaking Line](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)](https://downloads.intercomcdn.com/i/o/226483939/ed2cce9ed61fd46892a4a082/line.png?expires=1781168400&signature=cf4ff574480a4910c10f9dbc15623b32ab383e262e65c79dff7166141bc4a86b&req=diIhEsF9lIJWFb4f3HP0gLK9YgWB0hmnv1b6t%2BUbITS%2FJqOzeJ%2BGW47VUXMj%0ATzhhI2kdGNG%2B32RirQ%3D%3D%0A)

Learn how to [receive SMS on your Telnyx number](https://developers.telnyx.com/docs/messaging/messages/receive-message).

More details: What are webhook?

<https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks>

And for specific error codes here: <https://developers.telnyx.com/api/errors>

---

Related Articles

[Forwarding SMS to Your Mobile Number](https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number)[Resources on Your Account](https://support.telnyx.com/en/articles/4404409-resources-on-your-account)[Telnyx Verify: 2FA made easy](https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy)[Setting Up Telnyx Voicemail](https://support.telnyx.com/en/articles/5989560-setting-up-telnyx-voicemail)[Group Messaging - Bulk Sending MMS](https://support.telnyx.com/en/articles/8255134-group-messaging-bulk-sending-mms)

Did this answer your question?

😞😐😃

Table of contents
