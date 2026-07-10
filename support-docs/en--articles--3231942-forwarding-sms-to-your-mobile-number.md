---
source_url: https://support.telnyx.com/en/articles/3231942-forwarding-sms-to-your-mobile-number
scraped: 2026-07-08
content_hash: d24fdc801a0fea18759deda195635698b6e41638f30f9e0400198e2413a5c41e
---

Forwarding SMS to Your Mobile Number | Telnyx Help Center

[Skip to main content](#main-content)

# Forwarding SMS to Your Mobile Number

Set up SMS forwarding from your Telnyx number to your mobile phone with Zapier

Written by Nobin Bera

January 24, 2026

Table of contents

## **Overview**

This guide walks you through setting up a Zapier automation (called a "Zap") that forwards all inbound text messages received by your Telnyx number to your personal mobile number.

**Estimated Setup Time:** 15 minutes

---

## **Prerequisites**

Before you begin, ensure you have the following:

1. **Telnyx Account**: Sign up at <https://telnyx.com/sign-up> if you don't have one
2. **SMS-enabled phone number**: Purchase an SMS-capable number from the Telnyx Portal
3. **Messaging Profile**: Created and assigned to your Telnyx number
4. **API V2 Key**: Generated in the Telnyx Mission Control Portal
5. **Zapier Account**: Free accounts available at [https://zapier.com](https://zapier.com/)

---

## **Creating the SMS Forwarding Zap**

## **Step 1: Connect to the Telnyx Integration on Zapier**

1. Visit the Telnyx Zapier Integration page: <https://zapier.com/apps/telnyx/integrations>
2. Click **Connect** to add Telnyx to your Zapier account
3. If prompted, sign in to your Zapier account  
   ​

## **Step 2: Create a New Zap**

1. Go to your Zapier Dashboard: <https://zapier.com/app/dashboard>
2. Click **Create Zap** (or **Make a Zap!**) in the top-right corner  
   ​

## **Step 3: Configure the Trigger (Receive a Message)**

1. In the **App** search field, search for and select **Telnyx**
2. Under **Choose Trigger Event**, select **Receive a Message**
3. Click **Continue**
4. Select the Telnyx account to use for receiving messages

   * If your account isn't listed, click **Add Account** and enter your API V2 Key
5. Click **Continue**

**Important:** All messages received by numbers associated with the selected messaging profile will trigger this Zap. We highly recommend attaching only a single number to messaging profiles used for Zapier automations.

## **Step 4: Test the Trigger**

1. Click **Test Trigger** (or **Find Message**)
2. Zapier will pull in a sample inbound message webhook to set up the action stage
3. If successful, you'll see sample message data
4. Click **Continue** to proceed to the Action step  
   ​

## **Step 5: Configure the Action (Send SMS)**

1. In the **Do This...** step, search for and select **Telnyx**
2. Under **Choose Action Event**, select **Send SMS**
3. Click **Continue**
4. Select your Telnyx account (or sign in if prompted)
5. Click **Continue**  
   ​

## **Step 6: Customize the SMS Settings**

Configure the following fields:

|  |  |
| --- | --- |
| **Field** | **Value** |
| **Source Number** | Enter your Telnyx number in E.164 format (e.g., +14155551234) |
| **Destination Number** | Enter your personal mobile number in E.164 format (e.g., +13105559876) |
| **Message Content** | See format below |

For the **Message Content** field, enter something like:

```
FWD FROM: [From Phone Number]   
BODY: [Text]
```

**Note:** "From Phone Number" and "Text" are dynamic fields from the trigger. Use the dropdown on the right side of the Message Content field to insert these variables into your message body.

* Click **Continue**  
  ​

## **Step 7: Test Your Zap**

1. Click **Test Step** (or **Send Test**)
2. You should receive a test message on your mobile phone similar to:

   FWD FROM: +16365553226 BODY: Sample Text Sent From Zapier!

**Troubleshooting:** If the test fails, verify that:

* Your Source and Destination numbers are in E.164 format (include +1 for US/Canada)
* Your Telnyx number is messaging-enabled and assigned to a messaging profile
* Your 10DLC registration is complete (for US long codes)

## **Step 8: Activate Your Zap**

1. If the test was successful, click **Publish** (or **Turn on Zap**)
2. Your Zap is now active!

---

## **How It Works**

Once activated, your Zap will:

1. **Trigger**: When someone sends a text message to your Telnyx number
2. **Action:** Automatically forward that message to your personal mobile number with the sender's phone number and message content

---

## **Best Practices**

* **Use a dedicated messaging profile** — Attach only one number to profiles used for Zapier to avoid unintended triggers
* **Monitor your Zap** — Check Zapier's Task History to ensure messages are being forwarded successfully
* **Use E.164 format** — Always include the country code (e.g., +1 for US) when entering phone numbers

---

Related Articles

[Automated Replies for Messages using Zapier](https://support.telnyx.com/en/articles/3232529-automated-replies-for-messages-using-zapier)[Zapier: Forward Texts to Email](https://support.telnyx.com/en/articles/3723768-zapier-forward-texts-to-email)[Receiving SMS on your Telnyx number](https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number)[SMS for Ported In Phone Numbers](https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers)[How to Verify Phone Numbers behind an IVR](https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr)

Did this answer your question?

😞😐😃

Table of contents
