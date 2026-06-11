---
source_url: https://support.telnyx.com/en/articles/14668631-enabling-whatsapp-business-calling-on-telnyx-numbers
scraped: 2026-06-11
---

Enabling WhatsApp Business Calling on Telnyx Numbers | Telnyx Help Center

[Skip to main content](#main-content)

# Enabling WhatsApp Business Calling on Telnyx Numbers

Written by Telnyx Engineering

Updated over a month ago

Table of contents

WhatsApp Business Calling lets your business receive and place voice calls with WhatsApp users using your Telnyx numbers.

Users can call directly from the WhatsApp app to your numbers and Telnyx will route these calls to your SIP connection or Programmable Voice application.

Similarly, you can initiate calls from your connection or application to WhatsApp numbers.

Rather than routing through the PSTN like traditional calls, WhatsApp Business Calls are routed directly and securely between Telnyx and Meta.

By enabling WhatsApp Calling through Telnyx, you can leverage Telnyx platform capabilities, including Programmable Voice, AI Assistants, call recording, and real-time analytics, all from Mission Control Portal or the API.

---

## **Who it's for**

Businesses already using WhatsApp for customer communication that want to extend their interactions to voice, on a secure, widely adopted channel, without building a separate integration or managing a different infrastructure.

---

## **Requirements**

* A WhatsApp Business Account (WABA)
* A Telnyx phone number that will be linked to your WABA

  + The Telnyx number used for WhatsApp Calling must belong to the same Telnyx account where the WhatsApp Calling configuration is being created
* A WhatsApp Business Account associated with a business/business portfolio that has a daily messaging limit of at least 2,000 unique recipients.

  + If this requirement is not met, Meta may reject Calling enablement with the error “Calling APIs cannot be enabled for this phone number.”

---

## **Availability**

|  |  |
| --- | --- |
| **Call Type** | **Availability** |
| User-initiated calls | Available wherever WhatsApp Business is available |
| Business-initiated calls | Not available for business numbers in: USA, Canada, Egypt, Vietnam, Nigeria (based on the phone number's country code).        ⚠️ **Important:** Before placing a call, you must obtain the user's calling permission. More details on how to obtain permission below. |

# **Enable Whatsapp Business Calling in Mission Control**

These instructions will help you enable Whatsapp Business Calling in Telnyx Mission Control Portal.

If you already have a Telnyx number configured in the portal for messaging purposes and you just need to enable Whatsapp calling you can skip to step 5.

#### **Step 1 - Connect Your WhatsApp Business Account**

1. In Mission Control, navigate to **Voice Suite → WhatsApp Calling**.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360561317/8b1f8cca3c276eb135b5a48b3a1d/image.png?expires=1781167500&signature=dcee7279057c9fd681dd1cade3ee2c40c9a288e73b711e1ffe4fae4aefc80270&req=diMhFsx4nIJeXvMW1HO4zTerz6yvSFDH%2B0w12jvi5lKbBnPbWW8DktMJHjrx%0AAZ0F%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360561317/8b1f8cca3c276eb135b5a48b3a1d/image.png?expires=1781167500&signature=dcee7279057c9fd681dd1cade3ee2c40c9a288e73b711e1ffe4fae4aefc80270&req=diMhFsx4nIJeXvMW1HO4zTerz6yvSFDH%2B0w12jvi5lKbBnPbWW8DktMJHjrx%0AAZ0F%0A)

   ​
2. Click **"Connect WhatsApp Business"** which will trigger the embedded signup windows for the integration with Meta.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288707302/866e8d3a969235c1f8a8c0bc7a5e/ce4f17f6-fb1c-4f95-a29e-f7a11df3ad5e?expires=1781167500&signature=d338226514dea06407cb461fde87f12b91a2b9f8b260b227185df4ff2b85d408&req=diIvHs5%2BmoJfW%2FMW1HO4zTkTDZ5SGuWTTaT61YZRfEK5rIewYlh4iJI%2BZS23%0AlWPG%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288707302/866e8d3a969235c1f8a8c0bc7a5e/ce4f17f6-fb1c-4f95-a29e-f7a11df3ad5e?expires=1781167500&signature=d338226514dea06407cb461fde87f12b91a2b9f8b260b227185df4ff2b85d408&req=diIvHs5%2BmoJfW%2FMW1HO4zTkTDZ5SGuWTTaT61YZRfEK5rIewYlh4iJI%2BZS23%0AlWPG%0A)

   ​
3. Select the **WhatsApp Business Account (WABA)** you want to associate with WhatsApp Calling.  
   ​  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288708248/2924b1d9687c46fc92213f0e1733/74efdb95-e904-4667-b9ee-a7720449de00?expires=1781167500&signature=7c557abbddce082a77d1c5473dd43989d8452746d18462a295014c5810b9ab87&req=diIvHs5%2BlYNbUfMW1HO4zYiru%2BmyMw%2FBvW8oVSJeaaS2o%2BbI7RFf0M%2BjSaSD%0AbKXm%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288708248/2924b1d9687c46fc92213f0e1733/74efdb95-e904-4667-b9ee-a7720449de00?expires=1781167500&signature=7c557abbddce082a77d1c5473dd43989d8452746d18462a295014c5810b9ab87&req=diIvHs5%2BlYNbUfMW1HO4zYiru%2BmyMw%2FBvW8oVSJeaaS2o%2BbI7RFf0M%2BjSaSD%0AbKXm%0A)

**Step 2 - Associate your Telnyx number**

1. Select the Telnyx phone number you want to enable for WhatsApp Calling.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288722209/5e42339a45b5a281e09be3bdbf1c/3b4be067-b3eb-4b90-8d62-69dd996d3024?expires=1781167500&signature=1e57b0a6b47dbd671ce1fc31dee4cfd5987975e9cbf3b7571f34377880184cea&req=diIvHs58n4NfUPMW1HO4zaLXIZN7q%2BHEQHykF4RDoEPZ20Y44u5I4REWRATa%0AKm1Q%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288722209/5e42339a45b5a281e09be3bdbf1c/3b4be067-b3eb-4b90-8d62-69dd996d3024?expires=1781167500&signature=1e57b0a6b47dbd671ce1fc31dee4cfd5987975e9cbf3b7571f34377880184cea&req=diIvHs58n4NfUPMW1HO4zaLXIZN7q%2BHEQHykF4RDoEPZ20Y44u5I4REWRATa%0AKm1Q%0A)
2. Your Telnyx number must be active and able to receive calls or SMS (mobile numbers only) — Meta will send a verification code to confirm ownership.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288722974/29dacd7aeb5767216620128a0457/46cb4f93-3ecf-46cd-a28f-cb4ef0c1f3f5?expires=1781167500&signature=7685fc5d1be296015245cef854ddf9e77ad1efea1d99d8c288ecbb0c0f5091a0&req=diIvHs58n4hYXfMW1HO4zap4Nb7PbTEPns%2Fv3q1p6w0C2esjkXtn7w3E5cj2%0AXPdA%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288722974/29dacd7aeb5767216620128a0457/46cb4f93-3ecf-46cd-a28f-cb4ef0c1f3f5?expires=1781167500&signature=7685fc5d1be296015245cef854ddf9e77ad1efea1d99d8c288ecbb0c0f5091a0&req=diIvHs58n4hYXfMW1HO4zap4Nb7PbTEPns%2Fv3q1p6w0C2esjkXtn7w3E5cj2%0AXPdA%0A)
3. Enter the verification code once received.

#### **Step 3 - Confirm your configuration**

1. Review and confirm your WhatsApp configuration in Telnyx.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288737845/7c4cf5be3058e02531b583cdfb07/f50bd8ce-c168-4a15-a25e-9a49a0396e68?expires=1781167500&signature=80d3d45d6f1a3b6b67c067d2c6e5f03f63c14872dc09ac6073723c4664099146&req=diIvHs59molbXPMW1HO4zTuXSUU5lHIrr4kn7OLIUAbNprh8oLlmvlVVtcU0%0A0jPp%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288737845/7c4cf5be3058e02531b583cdfb07/f50bd8ce-c168-4a15-a25e-9a49a0396e68?expires=1781167500&signature=80d3d45d6f1a3b6b67c067d2c6e5f03f63c14872dc09ac6073723c4664099146&req=diIvHs59molbXPMW1HO4zTuXSUU5lHIrr4kn7OLIUAbNprh8oLlmvlVVtcU0%0A0jPp%0A)
2. You'll see a confirmation screen indicating your Meta account has been successfully connected to Telnyx.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288738449/8a878d9faeff0df8473ac70a800d/080bb181-3969-4912-95b8-6037a4e644fb?expires=1781167500&signature=bbde02c8ff32714a1e4bbaa8697aa2ddcb23153666a97948af4fb3d9308d9cab&req=diIvHs59lYVbUPMW1HO4zW51YnvnvfIJp3vJwwBxlwV5xbwiT7ZuwGhQJGE1%0AthOP%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288738449/8a878d9faeff0df8473ac70a800d/080bb181-3969-4912-95b8-6037a4e644fb?expires=1781167500&signature=bbde02c8ff32714a1e4bbaa8697aa2ddcb23153666a97948af4fb3d9308d9cab&req=diIvHs59lYVbUPMW1HO4zW51YnvnvfIJp3vJwwBxlwV5xbwiT7ZuwGhQJGE1%0AthOP%0A)
3. Navigate to **Voice Suite → WhatsApp Calling → Business Account** — your WABA should now appear with an **Active** status.

   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360571990/a37af64223c7f774f6bd5741db57/image.png?expires=1781167500&signature=2c38c77f4117bbe9472db3464b71d9b800b14346d9f70ed1c12fc04897d03c34&req=diMhFsx5nIhWWfMW1HO4zViOi3A0NYIr2o9MOOrHBVz4p%2FDdQS4dc7BQmibg%0A398n%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360571990/a37af64223c7f774f6bd5741db57/image.png?expires=1781167500&signature=2c38c77f4117bbe9472db3464b71d9b800b14346d9f70ed1c12fc04897d03c34&req=diMhFsx5nIhWWfMW1HO4zViOi3A0NYIr2o9MOOrHBVz4p%2FDdQS4dc7BQmibg%0A398n%0A)

   You can view and edit account details and settings from here.   
   It can take up to 2 minutes for this information to show up.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360574410/04b7d9afa29c08003f24952f31bb/image.png?expires=1781167500&signature=78b498bdecdc3d287d2913ca8c1c1fc913af1d6d056424c5c870c6ddd10cbe32&req=diMhFsx5mYVeWfMW1HO4zTYNG0LGBvVn2jG5jqM74r2LUiHz0PlSlMrfm6Pe%0AcBlW%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360574410/04b7d9afa29c08003f24952f31bb/image.png?expires=1781167500&signature=78b498bdecdc3d287d2913ca8c1c1fc913af1d6d056424c5c870c6ddd10cbe32&req=diMhFsx5mYVeWfMW1HO4zTYNG0LGBvVn2jG5jqM74r2LUiHz0PlSlMrfm6Pe%0AcBlW%0A)

   ​

   #### **Step 4 — Enable WhatsApp Calling in Telnyx**

1. In Mission Control, navigate to **Voice Suite → WhatsApp Calling → WhatsApp Numbers**.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360575949/3cef7d0aff8db57c860052bb251f/image.png?expires=1781167500&signature=becdac2777904e520c5f7d686e26aa62bcc67a0401c4b234520ae6dbb59a3d2b&req=diMhFsx5mIhbUPMW1HO4zT1vOmOao%2FW8PH3X3TclvzSppTtsariwONx2mvCQ%0ASGYX%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360575949/3cef7d0aff8db57c860052bb251f/image.png?expires=1781167500&signature=becdac2777904e520c5f7d686e26aa62bcc67a0401c4b234520ae6dbb59a3d2b&req=diMhFsx5mIhbUPMW1HO4zT1vOmOao%2FW8PH3X3TclvzSppTtsariwONx2mvCQ%0ASGYX%0A)

   ​
2. Select your number — it should show a **Connected** status.  
   ​

   [![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360577265/4e7a2bbab5675dcd609774098532/image.png?expires=1781167500&signature=f1adceab7e8c007bc73a1dfef29e7b993fb6d662b8fba82519ddf5b92598a4b1&req=diMhFsx5moNZXPMW1HO4zT0%2FL3QBKY1TNPVunl49qzDCyORrEF8a4eEso%2BsK%0Ancs3%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360577265/4e7a2bbab5675dcd609774098532/image.png?expires=1781167500&signature=f1adceab7e8c007bc73a1dfef29e7b993fb6d662b8fba82519ddf5b92598a4b1&req=diMhFsx5moNZXPMW1HO4zT0%2FL3QBKY1TNPVunl49qzDCyORrEF8a4eEso%2BsK%0Ancs3%0A)

   ​
3. Open the **Calling** tab and toggle **WhatsApp Calling** to enabled.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360582973/290ea84a61360f92de6e42320e28/image.png?expires=1781167500&signature=89be157dd758dee5fa8f704a727381e388b4605dd4b851458ae2237ff09a057c&req=diMhFsx2n4hYWvMW1HO4zSAHPXH043vAcf6JDzqcM5C%2FWhiEopc2K%2FYtOYlO%0A7GggOh54EYj9qJXX4fw%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2360582973/290ea84a61360f92de6e42320e28/image.png?expires=1781167500&signature=89be157dd758dee5fa8f704a727381e388b4605dd4b851458ae2237ff09a057c&req=diMhFsx2n4hYWvMW1HO4zSAHPXH043vAcf6JDzqcM5C%2FWhiEopc2K%2FYtOYlO%0A7GggOh54EYj9qJXX4fw%3D%0A)

---

# **Place and Receive Calls**

## **User-Initiated Calls**

Once WhatsApp Calling is enabled on your number, your business is ready to receive calls from any WhatsApp user.

WhatsApp users can reach you in the following ways:

* **Call button in chat** — if enabled, a call icon appears directly in the WhatsApp chat interface with your business.
* **Click-to-call button** — via an interactive message or template you send to the user.
* **Deep link** — a call link you embed on your website, app, or QR code that launches a call directly.

Regardless of how the call is initiated, it connects through WhatsApp and is routed to your Telnyx number, handled by your existing SIP connection or Programmable Voice application, just like a regular inbound call. No additional setup is required.

## **Business-Initiated Calls**

You can initiate a call to any Whatsapp Number as long as you meet these requirements:

1. You’re initiating the call from one of your SIP connections or Programmable Voice applications
2. You’re using the Whatsapp Calling number as the From number
3. The user has granted permission for you to call them
4. Your Whatsapp Calling number is not from any of these countries: USA, Canada, Egypt, Vietnam, Nigeria

To place a call to a WhatsApp user from your Telnyx number, use the following dial string format:

`<destination_number>@whatsapp-<your_telnyx_number>.sip.telnyx.com`

Where:

* `<destination_number>` is the WhatsApp user's phone number in E.164 format (e.g. `+447911123456`)
* `<your_telnyx_number>` is your WhatsApp-enabled Telnyx number in E.164 format, without the leading +

**Example:** If your Telnyx number is `+447418613982` and you want to call `+447911123456,` the dial string is:

[`+447911123456@whatsapp-447418613982.sip.telnyx.com`](mailto:%2B447911123456@whatsapp-447418613982.sip.telnyx.com)

This SIP URI can be used as the destination when placing WhatsApp calls from SIP, Voice API, or TeXML workflows.

## **Obtaining calling permission**

You can obtain calling permission from a WhatsApp user in any of the following ways:

1. **Send a call permission request to the user** — Send a free-form or templated message requesting calling permission from the user. User has the option to choose between temporary or permanent.
2. **Callback permission is provided by the WhatsApp user** — The WhatsApp user automatically provides temporary call permissions by placing a call to the business. The [callback setting must be enabled](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling/call-settings#configure-update-business-phone-number-calling-settings) on the business phone number.
3. **WhatsApp user provides call permission via Business Profile** — The WhatsApp user provides call permissions to the business through their business profile.

#### **Send a call permission request to the user**

Send a permission request to the WhatsUp user via the WhatsApp Cloud API, either as a template or free-form message   
Keep in mind the following rate limits:

* Maximum **1 request per 24 hours** per user
* Maximum **2 requests per 7 days** per user
* These limits **reset automatically** once a connected call (business- or user-initiated) takes place between you and the user.

1. **Wait for approval.** Once the user grants permission, you can place the outbound WhatsApp call from your configured Telnyx workflow.
2. **Understand permission duration.** Permissions can be:

   * **Temporary** — valid for 7 days
   * **Permanent** — granted by the user indefinitely

More details about the call permission request flow and sample message can be found [here](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling/user-call-permissions#call-permission-request-flow-and-sample-messages)

**Callback permission is provided by the WhatsApp user**

Businesses can configure the phone number call setting to allow callbacks. When enabled, a temporary calling permission is automatically granted after a WhatsApp user calls the business profile.

Go to WhatAapp Manager>Phone on your Meta Business Suite, select your number, go to Call Settings and enable "Allow Callbacks"  
​  
​

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2380452481/a894db751594e713660dff86215e/image.png?expires=1781167500&signature=abc604fea0c6e56403099cc5a9e01f3e840052dc616546070385beebfff3fd56&req=diMvFs17n4VXWPMW1HO4zVUUPkX%2FSA7T9kzUpS3w6R9cnpbypKcchlxuTiTt%0AYk0bWpWQim9aTCgb120%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2380452481/a894db751594e713660dff86215e/image.png?expires=1781167500&signature=abc604fea0c6e56403099cc5a9e01f3e840052dc616546070385beebfff3fd56&req=diMvFs17n4VXWPMW1HO4zVUUPkX%2FSA7T9kzUpS3w6R9cnpbypKcchlxuTiTt%0AYk0bWpWQim9aTCgb120%3D%0A)

#### **WhatsApp user provides call permission via Business Profile**

WhatsApp users can grant permission directly from your WhatsApp Business profile at any time by following these steps:

1. Save your Telnyx number as a WhatsApp contact
2. Open the contact — it will appear as a Business Profile
3. Tap **View Contact** → **Business Call Permission**
4. Select the desired permission option

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288900125/0b405765a647b07895651845669a/bb8cdf3b-6b07-4000-bc28-0885279c8027?expires=1781167500&signature=dff19767a717d5f442685d4cbbb2cd6e5d42fa515531b66b6f450991f03172e5&req=diIvHsB%2BnYBdXPMW1HO4zcSj8yHfgV4CeoLtyM6K5AkOY6Or3X9Un5NV9ozF%0AifSa3t5iE0TIqUqdnZA%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2288900125/0b405765a647b07895651845669a/bb8cdf3b-6b07-4000-bc28-0885279c8027?expires=1781167500&signature=dff19767a717d5f442685d4cbbb2cd6e5d42fa515531b66b6f450991f03172e5&req=diIvHsB%2BnYBdXPMW1HO4zcSj8yHfgV4CeoLtyM6K5AkOY6Or3X9Un5NV9ozF%0AifSa3t5iE0TIqUqdnZA%3D%0A)

#### **Important: Unanswered call behaviour**

WhatsApp monitors consecutive missed business-initiated calls on a per-user basis:

* After **2 consecutive unanswered calls**, WhatsApp sends the user a nudge notification.
* After **4 consecutive unanswered calls**, permission is **automatically revoked** and you'll need to request it again.

To avoid hitting this limit, only call users who are expecting to hear from you.

More information about Meta calling permissions can be found [here](https://developers.facebook.com/documentation/business-messaging/whatsapp/calling/user-call-permissions)

---

## **Troubleshooting**

* **Calling toggle** — Confirm "Calling" is enabled for the number in Mission Control.
* **Geo eligibility** — If business-initiated calling fails, check the business phone number's country code against the exclusions listed above.
* **Permission state** — For business-initiated calls, verify user permission (temporary or permanent). If absent, send a permission request first.
* **Still stuck?** — Confirm your number is a Telnyx number under your WABA.

---

## **Price**

A flat fee of **$0.0025/min** applies to both **user-initiated** and **business-initiated** WhatsApp calls.

Business-initiated calls are also subject to additional WhatsApp Calling charges based on the applicable rate deck.

To view your rates, check **My Pricing** in the portal or contact your account representative.

---

## **FAQs**

**Can I bridge WhatsApp calls to PSTN?** No. WhatsApp Calling is on-net to WhatsApp users only.

**Do calls count against messaging limits?** No. Calling has separate limits. However, Meta requires the WABA to have a ≥ 2,000 daily messaging limit to enable Calling.

**Is there a limit to how many calls I can receive at once?** Yes. Meta's maximum is 1,000 concurrent calls per business number.

**What's the difference between user-initiated and business-initiated calls?**

* **User-initiated:** The user calls your Telnyx number through WhatsApp, no special permission needed.
* **Business-initiated:** You call the user, but must first request their permission either through a template message or a free-form message during an active customer service window.
* **How do business-initiated calling permissions work?** Send a permission request (max 1 per 24 hours, 2 per 7 days per business+user). Temporary permission lasts 7 days; permanent permission is also supported. If 2 consecutive business-initiated calls go unanswered, WhatsApp notifies the user. After 4 consecutive unanswered calls, permission is auto-revoked.

**Why is my business-initiated call failing?**

Common causes include:

* The dial string is not properly formatted according to the integration requirements
* The WhatsApp user has not granted calling permission
* The user’s temporary calling permission has expired
* The calling permission was automatically revoked after repeated unanswered calls
* The WhatsApp calling number is not associated with the connection being used to place the call

Verify that the dial string matches the documented format, ensure the WhatsApp user has granted valid calling permissions, and confirm that the WhatsApp-enabled number is assigned to the same connection originating the call.

---

Related Articles

[What is WhatsApp Business Platform?](https://support.telnyx.com/en/articles/13986480-what-is-whatsapp-business-platform)[WhatsApp Pricing on Telnyx](https://support.telnyx.com/en/articles/13986484-whatsapp-pricing-on-telnyx)[How to Set Up WhatsApp on Telnyx](https://support.telnyx.com/en/articles/13986485-how-to-set-up-whatsapp-on-telnyx)[WhatsApp FAQ](https://support.telnyx.com/en/articles/13986488-whatsapp-faq)[WhatsApp Troubleshooting Guide](https://support.telnyx.com/en/articles/13986489-whatsapp-troubleshooting-guide)

Did this answer your question?

😞😐😃

Table of contents
