---
source_url: https://support.telnyx.com/en/articles/10523949-forwarding-sms-mms-automation-using-telnyx-flow
scraped: 2026-06-11
---

Forwarding SMS/MMS Automation using Telnyx Flow | Telnyx Help Center

[Skip to main content](#main-content)

# Forwarding SMS/MMS Automation using Telnyx Flow

A no-code solution for Forwarding Messages to your mobile number.

Written by Sergio Sales

February 12, 2025

Table of contents

## Introduction

This guide will teach you how to quickly set up Telnyx Flow to automate forwarding actions to inbound messages.

We'll cover the following scenario of Telnyx Flow implementation:

* **Set up a Message Forwarding logic that redirects all the inbound messages destined to a Telnyx number and sends them to your mobile number.**

For this tutorial, you will need to have these settings and resources in your Telnyx Account:

* Telnyx Phone Number(s) must be enabled for messaging;
* The said Phone Number must be assigned to an approved 10DLC Campaign. (Article: [Register for 10DLC](https://intercom.help/telnyx/en/articles/6325731-register-for-10dlc-messaging))
* Create a dedicated Messaging Profile and assign the Telnyx numbers to the profile ( Article: [Messaging First Steps at Telnyx](https://intercom.help/telnyx/en/articles/3562059-setting-up-a-messaging-profile))

We also suggest you read the [Getting Started with Telnyx Flow](https://intercom.help/telnyx/en/articles/9413928-getting-started-with-telnyx-flow) article for a deeper understanding of how Telnyx Flow can improve your workflows, including powerful AI tools.

## **Creation and Set up of the Workflow**

**1. Log In**: Visit [flow.telnyx.com](https://flow.telnyx.com/), where you’ll be redirected to log into your Telnyx Mission Control account. If you don’t have an account, you can sign up [here](https://portal.telnyx.com/#/login/signup).

* *Note*: You may be logged out after a period of inactivity. Simply log back into Mission Control and refresh Telnyx Flow to continue.

2. Create a New Workspace:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1370577551/cf006833d8b8af13df6cb2a22e08/Screenshot-2Bfrom-2B2024-06-03-2B11-59-04.png?expires=1781167500&signature=4bc2e08660d929812417435a867586de3ac9b5d9b7bb9956e1e40fc12b1052f4&req=dSMgFsx5moRaWPMW1HO4zZ9od2lxTKFDc6hwFwca49lZTwm%2Fq4ev97I39aoL%0ATRoke51CHRzCSCOBtCs%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1370577551/cf006833d8b8af13df6cb2a22e08/Screenshot-2Bfrom-2B2024-06-03-2B11-59-04.png?expires=1781167500&signature=4bc2e08660d929812417435a867586de3ac9b5d9b7bb9956e1e40fc12b1052f4&req=dSMgFsx5moRaWPMW1HO4zZ9od2lxTKFDc6hwFwca49lZTwm%2Fq4ev97I39aoL%0ATRoke51CHRzCSCOBtCs%3D%0A)

Image 1 - Workspace

3. Create a new Workflow with a Blank Canvas

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1370580036/df51b86e2386795ea3cb95306909/image.png?expires=1781167500&signature=549755055de7a40a92185d53d676b778c09e5d39e1ac0b5481ba224fd815a327&req=dSMgFsx2nYFcX%2FMW1HO4zWkPcE6cxETei7f5fMlbfxR13CiFVebZy8LlnzIM%0ANjASS5usXdKc51%2B7lRc%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1370580036/df51b86e2386795ea3cb95306909/image.png?expires=1781167500&signature=549755055de7a40a92185d53d676b778c09e5d39e1ac0b5481ba224fd815a327&req=dSMgFsx2nYFcX%2FMW1HO4zWkPcE6cxETei7f5fMlbfxR13CiFVebZy8LlnzIM%0ANjASS5usXdKc51%2B7lRc%3D%0A)

Image 2 - Blank Canvas

4. Right-click anywhere in the canvas to add the following nodes:

* "*Inbound Message*": the Trigger that upon receiving an inbound message will start the automation;
* "*Switch*": the logic node that will select if the inbound message is SMS or MMS;

  + Connect these 2 nodes as shown in **Image 3**.
* "*Send Message*": Node that will be responsible for the outbound action

  + Note: Add two "*Send Message*" nodes, one for SMS and one for MMS
* Click "*Save*" on the top left corner menu.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1370591837/5170992c8b82f0a4a8b3dd464687/image.png?expires=1781167500&signature=2f8aad237ace1f2d63c444d6ad0e19c315f318b9c14568cdcdd2034d665e9a5a&req=dSMgFsx3nIlcXvMW1HO4zdb9O71adnEc113a7o6rAih%2BVJLUOUrK1rPqR33V%0AlARDdx25fDdGqy5RkqY%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1370591837/5170992c8b82f0a4a8b3dd464687/image.png?expires=1781167500&signature=2f8aad237ace1f2d63c444d6ad0e19c315f318b9c14568cdcdd2034d665e9a5a&req=dSMgFsx3nIlcXvMW1HO4zdb9O71adnEc113a7o6rAih%2BVJLUOUrK1rPqR33V%0AlARDdx25fDdGqy5RkqY%3D%0A)

Image 3 - Nodes added to Canvas

5. Creating the Conditions on the Switch node:

* Add a descriptive Label: "*SMS or MMS?*"

* Add a condition group:

  + Name it "*SMS*"
  + On "*input*" type in the variable `{{message.received.type}}`
  + The comparison logic is "*Equals*"
  + On "*Value*" type in "*SMS* (without quotes)
* Click on the Blue Disk icon to save the Condition Group.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1370638289/f8ab3d610b354d3dce29fee2e3e0/image.png?expires=1781167500&signature=5bc020d8bbe8126fa90b124d15eaf8f861cd9becf86ab0ab085ad4e46877657d&req=dSMgFs99lYNXUPMW1HO4zfa%2Fqu7%2FYxTHDvONv%2BuJi390TtjfTnaHj4NOl6Xy%0ADtgqOd%2FBnXSRO4au8CI%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1370638289/f8ab3d610b354d3dce29fee2e3e0/image.png?expires=1781167500&signature=5bc020d8bbe8126fa90b124d15eaf8f861cd9becf86ab0ab085ad4e46877657d&req=dSMgFs99lYNXUPMW1HO4zfa%2Fqu7%2FYxTHDvONv%2BuJi390TtjfTnaHj4NOl6Xy%0ADtgqOd%2FBnXSRO4au8CI%3D%0A)

Image 4 - SMS Condition Group

* Add another condition group, repeating the same steps but now for the "*MMS*" condition:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1370641643/ae57b842cbc9035ea1f565e8c29e/image.png?expires=1781167500&signature=3e41e210655ffea9452db775b80e84f8a48ccca2dde6ca85899dc51a6c2c597a&req=dSMgFs96nIdbWvMW1HO4zUijLHx2%2F7Ivc5a0gisa0p2u%2FBmSeN7ZuV5qG3rS%0Ao8hLmmbrCSVv4LzI8gk%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1370641643/ae57b842cbc9035ea1f565e8c29e/image.png?expires=1781167500&signature=3e41e210655ffea9452db775b80e84f8a48ccca2dde6ca85899dc51a6c2c597a&req=dSMgFs96nIdbWvMW1HO4zUijLHx2%2F7Ivc5a0gisa0p2u%2FBmSeN7ZuV5qG3rS%0Ao8hLmmbrCSVv4LzI8gk%3D%0A)

Image 5 - All Condition Groups on Switch Node

* Connect each "*SMS*", "*MMS*" and "*Data*" Switch node output to a Send Message node:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1377332285/fb94ebe0263bd65b02a34c8a573c/image.png?expires=1781167500&signature=98d10295b9fe82a7dc502cd593e560d52a76c6ebedcdcffb6cb216265b7614cf&req=dSMgEcp9n4NXXPMW1HO4zdSY%2F9K6B%2BOUsZvQZimUI1Kk4zLhtY1jqJehPa2u%0AJmSqQrI0HcU2NHC9WZA%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1377332285/fb94ebe0263bd65b02a34c8a573c/image.png?expires=1781167500&signature=98d10295b9fe82a7dc502cd593e560d52a76c6ebedcdcffb6cb216265b7614cf&req=dSMgEcp9n4NXXPMW1HO4zdSY%2F9K6B%2BOUsZvQZimUI1Kk4zLhtY1jqJehPa2u%0AJmSqQrI0HcU2NHC9WZA%3D%0A)

Image 6 - Send Message Node Set-up

The settings for each Send Message node are similar:

* ***Type***: SMS or MMS selection (select according to the Switch output connected to the node)
* ***Messaging Profile ID***: You can choose from a drop-down menu. (Since we are originating the forwarded message from the recipient Telnyx number, the Messaging Profile ID will be the same as the Inbound Message node.)
* ***From*** and ***To***: the variables contained in the input Data that inverts the From and To of the inbound message. (The ***From*** field can also be a fixed originating number, depending on the user's choice)
* ***Text***: You can customize the message body that composes the forwarded message. In Image 6, there's an example of how to use the variables within the text field.

  + *For this Tutorial, the other sections of the Send Message Node will remain default; further details are covered in the dedicated article.*

The only distinction between the respective Send Message nodes for SMS and MMS is the dedicated field related to the MMS media: Subject and Media URLs, however with a similar logic for customization and variable usage as shown in Image 7:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1377358227/95d81e5dca0f86d0dde7a25b7d39/image.png?expires=1781167500&signature=512b06904436f0a07334eeca8e6a79a8a5ecdb75d23854773c132d9f365d61c4&req=dSMgEcp7lYNdXvMW1HO4zSt%2B1BOW1JIHc3q77SenmO2%2FpzPkMqkAtYG9WCgc%0AgoTD1627TsImzJarmIo%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1377358227/95d81e5dca0f86d0dde7a25b7d39/image.png?expires=1781167500&signature=512b06904436f0a07334eeca8e6a79a8a5ecdb75d23854773c132d9f365d61c4&req=dSMgEcp7lYNdXvMW1HO4zSt%2B1BOW1JIHc3q77SenmO2%2FpzPkMqkAtYG9WCgc%0AgoTD1627TsImzJarmIo%3D%0A)

Image 7 - MMS Send Message Set-up

And you're done!

Click the Save button to deploy your workflow settings.

# Testing your Workflow

To facilitate iterations, you can also test the workflow right from the Telnyx Flow:

* Go and click on the first nodeInbound Message and click on the "Run Workflow" green button at the top right corner, there you can type a test inbound message to execute your workflow:

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1377402878/5a17aaa3e96493df20577e7f8f38/image.png?expires=1781167500&signature=13355d252129388a5649dcf6b3e152037c5e38343704c01206a983a33f526840&req=dSMgEc1%2Bn4lYUfMW1HO4zTU7KOO0tN77cML2G7VuvnMTMvE6YWnLlOJqpbaw%0ALRqwReW82sRCbBvZqSg%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1377402878/5a17aaa3e96493df20577e7f8f38/image.png?expires=1781167500&signature=13355d252129388a5649dcf6b3e152037c5e38343704c01206a983a33f526840&req=dSMgEc1%2Bn4lYUfMW1HO4zTU7KOO0tN77cML2G7VuvnMTMvE6YWnLlOJqpbaw%0ALRqwReW82sRCbBvZqSg%3D%0A)

Image 8 - Testing the Workflow inside Telnyx Flow

We hope this article is useful in your journey as a Telnyx Customer and if you have any questions or suggestions, feel free to contact us at [support@telnyx.com](mailto:support@telnyx.com).

Thank you for reading!

---

Related Articles

[What is Telnyx?](https://support.telnyx.com/en/articles/1130637-what-is-telnyx)[Forwarding SMS to Your Mobile Number](https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number)[Automated Replies for Messages using Zapier](https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier)[FAQs about MMS at Telnyx](https://support.telnyx.com/en/articles/4450150-faqs-about-mms-at-telnyx)[Telnyx Flow](https://support.telnyx.com/en/articles/9413928-telnyx-flow)

Did this answer your question?

😞😐😃

Table of contents
