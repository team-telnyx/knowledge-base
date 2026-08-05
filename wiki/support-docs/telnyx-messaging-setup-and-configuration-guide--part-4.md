---
title: Telnyx Messaging Setup and Configuration Guide
summary: This page consolidates Telnyx support documentation covering SMS setup, sending,
  and advanced messaging features. It includes guidance on SMPP, number pooling, alphanumeric
  sender IDs, hosted SMS, Postman-based API testing, Python SDK usage, and third-party
  integrations such as Easy Text Marketing.
sources:
- url: https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide
- url: https://support.telnyx.com/en/articles/3154822-number-pooling
- url: https://support.telnyx.com/en/articles/3562061-send-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/3562066-receive-a-text-with-the-telnyx-python-sdk
- url: https://support.telnyx.com/en/articles/4287554-sms-setup-with-postman
- url: https://support.telnyx.com/en/articles/4353862-creating-postman-collection-from-openapi
- url: https://support.telnyx.com/en/articles/4371498-sending-alphanumeric-sms-sender-id
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
- url: https://support.telnyx.com/en/articles/6354449-alphanumeric-sender-id
- url: https://support.telnyx.com/en/articles/6986625-easy-text-marketing-and-telnyx-integration
updated_at: 2026-08-05T13:34:18Z
---

# Telnyx Messaging Setup and Configuration Guide

*Part 4 of 4 — see also: [Part 1](telnyx-messaging-setup-and-configuration-guide--part-1.md), [Part 2](telnyx-messaging-setup-and-configuration-guide--part-2.md), [Part 3](telnyx-messaging-setup-and-configuration-guide--part-3.md)*

This page consolidates Telnyx support documentation covering SMS setup, sending, and advanced messaging features. It includes guidance on SMPP, number pooling, alphanumeric sender IDs, hosted SMS, Postman-based API testing, Python SDK usage, and third-party integrations such as Easy Text Marketing.

## Easy Text Marketing and Telnyx Integration

This onboarding guide is for Easy Text Marketing (formerly known as Rockstar SMS) SMS customers using Telnyx as their BYOC Carrier. The full setup should take less than 30 minutes from start to finish.

### Signup

Create a Telnyx Account at [telnyx.com/sign-up](https://telnyx.com/sign-up). It is free to sign up.

![Telnyx account signup page.](_images/72fb230203b7b8e9.png)

Click through the drop-downs to answer a few short onboarding prompts.

### Adding Funds

The Telnyx platform is prepaid (you only pay for what you use), so add funds at [portal.telnyx.com/#/billing/payment](https://portal.telnyx.com/#/billing/payment). Depending on your volume, $25 should be more than enough to get most people started. The only purchase in this guide is a phone number, which standard costs $1 activation and $1 per month.

!["Add Funds" section.](_images/9dff5c274ebd4297.png)

### Select the Recharge Settings

Once a payment method is added and after the first payment, auto-recharge settings can be chosen at [portal.telnyx.com/#/billing/payment](https://portal.telnyx.com/#/billing/payment).

![Auto-Recharge Preferences section.](_images/98b353bbbad3046e.png)

Copy your API Key (not the public key) at [portal.telnyx.com/#/home](https://portal.telnyx.com/#/home) to plug into the Easy Text Marketing platform.

![Mission Control Portal.](_images/5fb20439d303a7fe.png)

### Configure the Easy Text Marketing Profile

In your Easy Text Marketing Profile, select Telnyx as your SMS Gateway and enter the Telnyx API Key copied in the previous step at [rockstarsms.app/users/edit](https://rockstarsms.app/users/edit).

![RockStar Profile section.](_images/76cc3ecd417f07f9.png)

### Get a Number

In the Easy Text Marketing Dashboard, click "Get a Number" (this should automatically create a Telnyx messaging profile) at [rockstarsms.app/users/profile](https://rockstarsms.app/users/profile).

!["Get a Number" section.](_images/ea94b11e48775dcc.png)

### Assign the Messaging Profile

Return to Telnyx and assign the Messaging Profile with the Easy Text Marketing webhook to the new number at [portal.telnyx.com/#/voice/my-numbers](https://portal.telnyx.com/#/voice/my-numbers). Click the drop-down in the highlighted section and select the Easy Text Marketing Messaging Profile, which is probably listed as "Text Marketing Made Easy".

![Messaging Profile assigning section.](_images/7146d510a30e7175.png)

For help with Telnyx steps, contact [klane@telnyx.com](mailto:klane@telnyx.com). For sub-accounts ("Managed Accounts"), also reach out to [klane@telnyx.com](mailto:klane@telnyx.com). For support on the Easy Text Marketing steps, visit [rockstarsms.app/helpdesk/](https://rockstarsms.app/helpdesk/).

![RockstarSMS picture.](_images/0ac9c2a44dca2f3f.png)
