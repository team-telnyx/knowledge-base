---
source_url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
scraped: 2026-06-11
---

Zapier: Forward Texts to Email | Telnyx Help Center

[Skip to main content](#main-content)

# Zapier: Forward Texts to Email

In this article we will discuss how to set up text message forwarding to your inbox.

C

Written by Customer Success

May 25, 2024

Table of contents

[Jump to Instructions](#h_bc3d87c409)

We all use a lot of apps just to communicate with one another. [Zapier](https://zapier.com) connects 5,000+ apps so the conversations flow automatically. In this article you'll learn how to forward inbound text messages to your email account.

**Additional resources:**

* [Zapier Help Center](https://help.zapier.com/hc/en-us)
* [Zapier Community](https://community.zapier.com/)
* [Zapier University](https://learn.zapier.com/)

---

**IMPORTANT**: We apologise for any inconvenience, the steps outlined in this article do not currently function. Telnyx is aware that the Zap for "Receive a Message" is outdated and working on fixing it again.

# Get set up with the Telnyx Integration on Zapier

**Prerequisites**

* **Zapier**

  + Make sure that you’ve [signed up for a Zapier account](https://zapier.com/sign-up).
  + Follow this [link](https://zapier.com/apps/telnyx/integrations) to find the Telnyx Zapier integration and click the connect button to get started.
* **Telnyx Mission Control Portal**

  + Make sure you have [bought at least one phone number](https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers) that is messaging enabled.
  + Make sure you've created a [messaging profile](https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile) and assigned it to the number you have purchased.
  + Make sure you've created an [API V2 Key.](https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them)

## **1. Making your first Zap**

Let’s go ahead and make your first Zap!

1. Make sure you’re at the Zapier [homepage](https://zapier.com/app/dashboard).
2. In the top right corner, click the **Make a Zap!** button and configure the following:

   1. **Trigger app:** *Telnyx*.

      1. If Telnyx is not already in your list of triggers, you can search for it.
   2. **Choose Trigger Event:** Select *Receive a Message*.
   3. Click **Continue**.
   4. **Choose Account:** Select the account you’d like to use for receiving messages.

      1. Allow Zapier to access your Telnyx Account.
      2. Input your Telnyx API V2 Key.
   5. Click **Continue.**
3. Copy the **webhook url** that Zapier will provide and assign it to your Telnyx Messaging Profile you created in your Telnyx account.

   1. [![webhook url copy screenshot](https://downloads.intercomcdn.com/i/o/1042656597/cf06b7c3af722017ea5a3cd1/Screenshot+from+2024-05-06+13-20-34.png?expires=1781168400&signature=aaf3f5e1762939dbe1891428e3ffb4d473980da58dfcbadb0693a44301e9f6f5&req=dSAjFM97m4RWXvMW1HO4zbXW8twW%2B9I%2Bv8MtSGS2Z80E%2Bc2DxujOM937w%2FHM%0A%2Bhsf%0A)](https://downloads.intercomcdn.com/i/o/1042656597/cf06b7c3af722017ea5a3cd1/Screenshot+from+2024-05-06+13-20-34.png?expires=1781168400&signature=aaf3f5e1762939dbe1891428e3ffb4d473980da58dfcbadb0693a44301e9f6f5&req=dSAjFM97m4RWXvMW1HO4zbXW8twW%2B9I%2Bv8MtSGS2Z80E%2Bc2DxujOM937w%2FHM%0A%2Bhsf%0A)
   2. [![Programable messaging screenshot](https://downloads.intercomcdn.com/i/o/1042653624/8a798e504754e18ae2520f61/Screenshot+from+2024-05-06+13-22-06.png?expires=1781168400&signature=ff7e5e01aeb01ef5ba436ad5bb491c1ac055b072b6fc5527ef644b86ba6a986d&req=dSAjFM97noddXfMW1HO4za9OONJUQN4bqjuLvc6NGW6QPpEW4ntDrbgUNnca%0AgiMW%0A)](https://downloads.intercomcdn.com/i/o/1042653624/8a798e504754e18ae2520f61/Screenshot+from+2024-05-06+13-22-06.png?expires=1781168400&signature=ff7e5e01aeb01ef5ba436ad5bb491c1ac055b072b6fc5527ef644b86ba6a986d&req=dSAjFM97noddXfMW1HO4za9OONJUQN4bqjuLvc6NGW6QPpEW4ntDrbgUNnca%0AgiMW%0A)
4. Click **Test Trigger** to test your connection and pull in a sample inbound message webhook to set up the action stage.

   1. You should send a test message to your Telnyx number in order for the sample inbound message to reach your Zapier Webhook.
   2. If successful, Zapier will display the inbound message record as seen below.
   3. [![Test Trigger on zap screenshot](https://downloads.intercomcdn.com/i/o/1042658762/c8b7d52dabc6ad6df2f06846/Screenshot+from+2024-05-06+13-27-34.png?expires=1781168400&signature=840faa9ef2dd9e7385c4cf4495e4d8aa5f86271c8f838e9be739f857b1884427&req=dSAjFM97lYZZW%2FMW1HO4zbe13NML2f1O5M7sFfOniVAq9pTJzGzwOJxfPxmr%0ADe13%0A)](https://downloads.intercomcdn.com/i/o/1042658762/c8b7d52dabc6ad6df2f06846/Screenshot+from+2024-05-06+13-27-34.png?expires=1781168400&signature=840faa9ef2dd9e7385c4cf4495e4d8aa5f86271c8f838e9be739f857b1884427&req=dSAjFM97lYZZW%2FMW1HO4zbe13NML2f1O5M7sFfOniVAq9pTJzGzwOJxfPxmr%0ADe13%0A)
   4. Click **Continue with selected record**

      1. See [section 2](#h_ae2f30fc8a) for this part of the configuration.

[Back to Top](#h_bc3d87c409)

## 2. Integrate your Zap with your Email

Here you can search for your email provider, for example, Gmail.

1. Choose the *Send an email* action.
2. Click **Continue**.

   1. [![Zap with your Email integration screenshot ](https://downloads.intercomcdn.com/i/o/1042662147/7e95e4f3a2ba6a1a0f0cb1b8/Screenshot+from+2024-05-06+13-31-17.png?expires=1781168400&signature=961af0181ba917f418124245d5825a63addffefb37e4a8ba171e5ddfb894387d&req=dSAjFM94n4BbXvMW1HO4zcDUsddUflWg3XO5Z%2BHErh51RsSqjUZn1R%2FaijuN%0AdB2u%0A)](https://downloads.intercomcdn.com/i/o/1042662147/7e95e4f3a2ba6a1a0f0cb1b8/Screenshot+from+2024-05-06+13-31-17.png?expires=1781168400&signature=961af0181ba917f418124245d5825a63addffefb37e4a8ba171e5ddfb894387d&req=dSAjFM94n4BbXvMW1HO4zcDUsddUflWg3XO5Z%2BHErh51RsSqjUZn1R%2FaijuN%0AdB2u%0A)
3. Choose an existing gmail account, or follow the directions to link a new account
4. Enter the email where you’d like to receive copies of your inbound messages.
5. Add Cc or Bcc as you wish
6. Choose your email address as the **To** address
7. For **Subject**, enter something unique (you most likely will want to filter this subject out from your inbox)
8. In the body enter something like this

   1. **From:** FROM\_PHONE\_NUMBER\_ZAPIER\_VARIABLE
   2. **To:** TO\_PHONE\_NUMBER\_ZAPIER\_VARIABLE
   3. **Body:** TEXT\_ZAPIER\_VARIABLE
   4. [![Zap email integration screenshot](https://downloads.intercomcdn.com/i/o/1042671803/3cfc266d421ef3487e667e17/Screenshot+from+2024-05-06+13-40-23.png?expires=1781168400&signature=32e77a99fc491719308e758fc0d6e95dabacde1a1cb21823e9377a8029945c16&req=dSAjFM95nIlfWvMW1HO4zXJgNUlbXhDTJ%2BEH4atuMrqV2AEAeozLy%2Fsq4lmT%0Ai3o8%0A)](https://downloads.intercomcdn.com/i/o/1042671803/3cfc266d421ef3487e667e17/Screenshot+from+2024-05-06+13-40-23.png?expires=1781168400&signature=32e77a99fc491719308e758fc0d6e95dabacde1a1cb21823e9377a8029945c16&req=dSAjFM95nIlfWvMW1HO4zXJgNUlbXhDTJ%2BEH4atuMrqV2AEAeozLy%2Fsq4lmT%0Ai3o8%0A)
9. Click **Continue.**

   1. [![Zap with your Email integration screenshot ](https://downloads.intercomcdn.com/i/o/1042673193/3641479c55ac59acfef36275/Screenshot+from+2024-05-06+13-40-54.png?expires=1781168400&signature=51d9874906f9df630f0db536c5fce53f83827d9644c14e591b0fce8c5a2da459&req=dSAjFM95noBWWvMW1HO4zchfCKGJ9Z3%2FTDuPohg2BI8dh3S5VdFqTzS%2FNnm6%0AFgGq%0A)](https://downloads.intercomcdn.com/i/o/1042673193/3641479c55ac59acfef36275/Screenshot+from+2024-05-06+13-40-54.png?expires=1781168400&signature=51d9874906f9df630f0db536c5fce53f83827d9644c14e591b0fce8c5a2da459&req=dSAjFM95noBWWvMW1HO4zchfCKGJ9Z3%2FTDuPohg2BI8dh3S5VdFqTzS%2FNnm6%0AFgGq%0A)
   2. Review the data and then click **Test Step**.

[Back to Top](#h_bc3d87c409)

## 3. Test your Zap

If the test step was successful, you should have received the email with the message contents.

[![Telnyx forwarded message screenshot](https://downloads.intercomcdn.com/i/o/1042677627/c6d5f1acc10b3406b75083d2/Screenshot+from+2024-05-06+13-45-38.png?expires=1781168400&signature=01d621795befb2ab2b0307842b760adbc1a44ec5b2000619de72aa80b944eed1&req=dSAjFM95moddXvMW1HO4zWVITwD79206kAyo1pYIJscytxIebLSbrmP55JHO%0AEBhPKZgZnH42SZ%2Bkgzg%3D%0A)](https://downloads.intercomcdn.com/i/o/1042677627/c6d5f1acc10b3406b75083d2/Screenshot+from+2024-05-06+13-45-38.png?expires=1781168400&signature=01d621795befb2ab2b0307842b760adbc1a44ec5b2000619de72aa80b944eed1&req=dSAjFM95moddXvMW1HO4zWVITwD79206kAyo1pYIJscytxIebLSbrmP55JHO%0AEBhPKZgZnH42SZ%2Bkgzg%3D%0A)

At this point you can click **Publish** to turn on the Zap.

[![](https://downloads.intercomcdn.com/i/o/1042675124/df9c01116c8f006b80457754/Screenshot+from+2024-05-06+13-42-50.png?expires=1781168400&signature=ef992574e3850ede48514abc5fa09a5754050179f2bac8586cd8815e7568253b&req=dSAjFM95mIBdXfMW1HO4zcycUSatN0iERvmU4iHu%2BhK2rW1H%2BaATxVLh4dHM%0ATuCmwi2vGN2Bf1QX0Q0%3D%0A)](https://downloads.intercomcdn.com/i/o/1042675124/df9c01116c8f006b80457754/Screenshot+from+2024-05-06+13-42-50.png?expires=1781168400&signature=ef992574e3850ede48514abc5fa09a5754050179f2bac8586cd8815e7568253b&req=dSAjFM95mIBdXfMW1HO4zcycUSatN0iERvmU4iHu%2BhK2rW1H%2BaATxVLh4dHM%0ATuCmwi2vGN2Bf1QX0Q0%3D%0A)

You've now set up a quick way to forward inbound messages from your Telnyx number to your real number.

[Back to Top](#h_bc3d87c409)

---

**Additional Resources**

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally, you can check out:

* [Zapier Help Center](https://help.zapier.com/hc/en-us)
* [Zapier Community](https://community.zapier.com/)
* [Zapier University](https://learn.zapier.com/)

---

Related Articles

[Forwarding SMS to Your Mobile Number](https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number)[Automated Replies for Messages using Zapier](https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier)[Textable Setup Guide](https://support.telnyx.com/en/articles/3685327-textable-setup-guide)[Receiving SMS on your Telnyx number](https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number)[Forwarding SMS/MMS Automation using Telnyx Flow](https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow)

Did this answer your question?

😞😐😃

Table of contents
