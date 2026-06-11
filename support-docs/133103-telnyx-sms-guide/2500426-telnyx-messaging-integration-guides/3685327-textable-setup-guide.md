---
source_url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
scraped: 2026-06-11
---

Textable Setup Guide | Telnyx Help Center

[Skip to main content](#main-content)

# Textable Setup Guide

Here we will explain how you can easily set up your Textable account to use Telnyx's SMS service.

Written by Telnyx Engineering

Updated over 3 weeks ago

Table of contents

# **Step-by-Step Guide to Configuring Textable**

Configuring your Telnyx account with Textable is pretty simple and should only take a few minutes.

**Configuring Textable**

1. Go to <https://textable.app/signup> to sign up.
2. Enter an e-mail address and password. Click Next.
3. Select “Telnyx V2” as the provider.
4. Set **Phone Number (DID)** field to the number that exists in your Telnyx account and you want to use to send / receive messages with Textable.
5. Leave **Account ID** field empty. We do not use this for Telnyx accounts.
6. Complete account setup by Configuring Telnyx and copying needed data from those steps.

## Configuring Telnyx with Textable

1. First, you should login in a new tab (so you can easily copy / paste into the previous form on Textable Signup) to your console at [https://portal.telnyx.com/.](https://portal.telnyx.com/)
2. Once logged in, go to your Messaging page at <https://portal.telnyx.com/#/programmable-messaging/profiles>
3. Here, you will need to create a **Messaging Profile**  
   - Click “Add Messaging Profile” button.  
   - Name it what you’d like, but **“Textable”** would make sense.  
   - Click the “Inbound” tab and set the Protocol to HTTP.  
   - Set the Webhook URL to “<https://app01.textable.co/receive?provider=telnyxv2>"  
   ​ **For V2: Go to “API Keys” from the menu or click** <https://portal.telnyx.com/#/api-keys>  
   ​ **Create an API Key and copy it. You will need to paste this into the Access Token field in Textable.**
4. **Click Next on Textable to complete your account setup.**
5. We must now configure the Routing settings in Telnyx for your phone number.  
   - Go to the **Numbers** section in Telnyx [(https://portal.telnyx.com/#/messaging/my-numbers)](https://portal.telnyx.com/#/messaging/my-numbers)  
   - Choose the number you would like to use with Textable and click the “Routing” button.  
   - Under the **SMS Messaging Profile** section on the **Routing** tab, choose “Textable” (or whatever you named your messaging profile.)  
   - Click “Save Changes”
6. You can also now download and use the Textable app from [App Store (iOS)](https://apps.apple.com/us/app/textable-voip-texting/id1355564896?ls=1) or [Google Play Store (Android)](https://play.google.com/store/apps/details?id=co.textable.textable&hl=en&utm_source=textable&utm_campaign=website&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1)

That’s it, you should be able to send and receive messages!

---

Related Articles

[Forwarding SMS to Your Mobile Number](https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number)[Setting Up a Messaging Profile](https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile)[Easy Text Marketing and Telnyx Integration](https://support.telnyx.com/en/articles/6986625-easy-text-marketing-and-telnyx-integration)[How to Configure a SIP Trunk](https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk)[Bulk Messaging with Sheets](https://support.telnyx.com/en/articles/8268223-bulk-messaging-with-sheets)

Did this answer your question?

😞😐😃

Table of contents
