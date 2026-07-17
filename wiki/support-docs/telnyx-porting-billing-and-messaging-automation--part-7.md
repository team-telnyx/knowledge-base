---
title: Telnyx Porting, Billing, and Messaging Automation
summary: This page consolidates Telnyx support documentation covering number porting
  (CSRs, LOAs, automated validation, porting requirements, and the auto-generated
  LOA feature), billing models (per-minute billing increments and channel billing
  with zone-based pricing), CLI/CLD validation for North American calls, and Zapier-based
  SMS automations including forwarding texts to mobile or email, automated replies,
  and the Textable integration.
sources:
- url: https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier
- url: https://support.telnyx.com/en/articles/1130659-billing-increments
- url: https://support.telnyx.com/en/articles/1130678-channel-billing-and-how-to-use-it
- url: https://support.telnyx.com/en/articles/1516776-automated-port-request-validation
- url: https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa
- url: https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number
- url: https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier
- url: https://support.telnyx.com/en/articles/3685327-textable-setup-guide
- url: https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email
- url: https://support.telnyx.com/en/articles/6247033-cli-cld-validation-faq
- url: https://support.telnyx.com/en/articles/6460777-porting-requirements
- url: https://support.telnyx.com/en/articles/8268276-loa-template-download
- url: https://support.telnyx.com/en/articles/8428806-channel-billing
- url: https://support.telnyx.com/en/articles/8588086-auto-generated-letter-of-authorization-loa
updated_at: 2026-07-17T09:02:58Z
---

# Telnyx Porting, Billing, and Messaging Automation

*Part 7 of 7 — see also: [Part 1](telnyx-porting-billing-and-messaging-automation--part-1.md), [Part 2](telnyx-porting-billing-and-messaging-automation--part-2.md), [Part 3](telnyx-porting-billing-and-messaging-automation--part-3.md), [Part 4](telnyx-porting-billing-and-messaging-automation--part-4.md), [Part 5](telnyx-porting-billing-and-messaging-automation--part-5.md), [Part 6](telnyx-porting-billing-and-messaging-automation--part-6.md)*

This page consolidates Telnyx support documentation covering number porting (CSRs, LOAs, automated validation, porting requirements, and the auto-generated LOA feature), billing models (per-minute billing increments and channel billing with zone-based pricing), CLI/CLD validation for North American calls, and Zapier-based SMS automations including forwarding texts to mobile or email, automated replies, and the Textable integration.

## Textable Setup Guide

Configuring your Telnyx account with Textable is simple and should only take a few minutes.

### Configuring Textable

1. Go to <https://textable.app/signup> to sign up.
2. Enter an e-mail address and password. Click **Next**.
3. Select **Telnyx V2** as the provider.
4. Set the **Phone Number (DID)** field to the number that exists in your Telnyx account and you want to use to send/receive messages with Textable.
5. Leave the **Account ID** field empty. This is not used for Telnyx accounts.
6. Complete account setup by configuring Telnyx and copying needed data from those steps.

### Configuring Telnyx with Textable

1. First, log in a new tab (so you can easily copy/paste into the previous form on Textable Signup) to your console at <https://portal.telnyx.com/>.
2. Once logged in, go to your Messaging page at <https://portal.telnyx.com/#/programmable-messaging/profiles>.
3. Create a **Messaging Profile**:
   - Click the **Add Messaging Profile** button.
   - Name it what you'd like, but **"Textable"** would make sense.
   - Click the **Inbound** tab and set the Protocol to HTTP.
   - Set the Webhook URL to `https://app01.textable.co/receive?provider=telnyxv2`.
   - **For V2:** Go to **API Keys** from the menu or click <https://portal.telnyx.com/#/api-keys>.
   - **Create an API Key** and copy it. You will need to paste this into the Access Token field in Textable.
4. Click **Next** on Textable to complete your account setup.
5. Configure the Routing settings in Telnyx for your phone number:
   - Go to the **Numbers** section in Telnyx at <https://portal.telnyx.com/#/messaging/my-numbers>.
   - Choose the number you would like to use with Textable and click the **Routing** button.
   - Under the **SMS Messaging Profile** section on the **Routing** tab, choose **Textable** (or whatever you named your messaging profile).
   - Click **Save Changes**.
6. You can also now download and use the Textable app from the [App Store (iOS)](https://apps.apple.com/us/app/textable-voip-texting/id1355564896?ls=1) or [Google Play Store (Android)](https://play.google.com/store/apps/details?id=co.textable.textable&hl=en&utm_source=textable&utm_campaign=website&pcampaignid=MKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1).

That's it, you should be able to send and receive messages!
