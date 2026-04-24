---
title: Quickstart Guide for Programmable Fax
summary: Telnyx's Programmable Fax service makes it easy to send and receive faxes from your computer or phone.
sources:
  - url: https://developers.telnyx.com/docs/programmable-fax/quickstart/index
    content_hash: 111efc739830ee6232b93c092ec60e12c7c0c22805504f05d5966b7ca6affbae
updated_at: 2026-04-10T00:00:00Z
---

# Quickstart Guide for Programmable Fax

Telnyx's Programmable Fax service makes it easy to send and receive faxes from your computer or phone. With our service, you can send faxes anywhere in the world without having to install any software or hardware.

In this guide, you'll learn how to get started with Telnyx Programmable Fax within the Telnyx Portal. Just follow these simple steps:

1. Sign up for a Telnyx Account.
2. Create a Programmable Fax Application to configure how you connect your calls.
3. Buy or port a Phone Number.
4. Assign your number to the Programmable Fax Application.
5. Create an Outbound Voice Profile to configure your outbound call settings and assign it to your Programmable Fax Application.

***

## Step 1: Sign Up for a Telnyx Mission Control Portal account

Head to <a href="https://telnyx.com/sign-up">
telnyx.com/sign-up
</a> to sign up for your free Telnyx account. It’ll give you access to our Mission Control Portal where you can buy phone numbers, set up and manage Programmable Fax Applications, and more.

## Step 2: Create a programmable fax application in the Telnyx portal

* Select <a href="https://portal.telnyx.com/#/call-control/fax">
  "Programmable Fax"
  </a> in the left-hand navigation menu.
* Click "Add New App".
* For testing purposes, you can set the webhook URL using an endpoint you create at <a href="https://hookbin.com">
  [https://hookbin.com](https://hookbin.com)
  </a>.

## Step 3: Buy a phone number

You can search for, buy, and provision new numbers, or port existing numbers - all within the Numbers section of the <a href="https://portal.telnyx.com/#/app/numbers/search-numbers">
Telnyx Portal
</a>.

Simply click on "Numbers", then either "Search & Buy Numbers" or "Port Numbers" and follow the prompts.

> You can also do this programmatically via our **RESTful API**. Check out our documentation for number [searching](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers) and [ordering](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order).

## Step 4: Assign your phone number to the programmable fax application

Once your number has been purchased or ported, assign it to the Programmable Fax Application that you created in step 2. You can do this via the <a href="https://portal.telnyx.com/#/app/numbers/my-numbers">
My Numbers
</a> section of the Portal.

![Docs Images (1)](https://images.ctfassets.net/4b49ta6b3nwj/2BJYzATnJpHLpozAjst37j/208a1637c3b0cefb7a5e40d4ede66226/Docs_Images__1_.png)

## Step 5: Create an outbound voice profile (not required for Inbound)

To initiate an outbound fax, you must create an Outbound Voice Profile and assign your Programmable Fax Application to it.

Select <a href="https://portal.telnyx.com/#/app/outbound-profiles">
"Outbound Voice Profiles"
</a> on the left-hand navigation menu, click "+Add New Profile" and set up your profile name. Add the Programmable Fax Application you just created above, the traffic type, the service plan, and your desired billing method.

> You can also do this programmatically via our **RESTful API**. Check out our documentation for [Outbound Voice Profiles](https://developers.telnyx.com/docs/voice/outbound-voice-profiles).

That’s it. You're all set to start integrating Telnyx with your applications.

## Where to next?

Head over to our tutorials to learn how to [send a fax](../runbooks/send-a-fax-via-api.md) and [receive a fax](../runbooks/receive-a-fax-via-api.md) via API.

After you [setup your development environment](/development) you can also dive deeper into [sending commands](../runbooks/sending-commands.md) and [receiving webhooks](../runbooks/receiving-webhooks-for-programmable-fax.md).


## Related Pages

- [Getting Started with Telnyx Programmable Fax](../runbooks/getting-started-with-telnyx-programmable-fax.md)
- [Receiving Webhooks for Programmable Fax](../runbooks/receiving-webhooks-for-programmable-fax.md)
