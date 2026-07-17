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

*Part 5 of 7 — see also: [Part 1](telnyx-porting-billing-and-messaging-automation--part-1.md), [Part 2](telnyx-porting-billing-and-messaging-automation--part-2.md), [Part 3](telnyx-porting-billing-and-messaging-automation--part-3.md), [Part 4](telnyx-porting-billing-and-messaging-automation--part-4.md), [Part 6](telnyx-porting-billing-and-messaging-automation--part-6.md), [Part 7](telnyx-porting-billing-and-messaging-automation--part-7.md)*

This page consolidates Telnyx support documentation covering number porting (CSRs, LOAs, automated validation, porting requirements, and the auto-generated LOA feature), billing models (per-minute billing increments and channel billing with zone-based pricing), CLI/CLD validation for North American calls, and Zapier-based SMS automations including forwarding texts to mobile or email, automated replies, and the Textable integration.

## CLI & CLD Validation

On June 6th, 2022, Telnyx enhanced its existing validation mechanism by adding checks to North American National Numbering databases for CLI and CLD.

### What are CLI and CLD?

Calling Line Identity (CLI) refers to the number the call came from, and Calling Line Destination (CLD) refers to the number that was dialed.

### Valid Number Format

The International Telecommunications Union (ITU) assigned country code "1" to the NANP area. The NANP conforms with ITU Recommendation E.164, the international standard for telephone numbering plans.

NANP numbers are ten-digit numbers consisting of a three-digit Numbering Plan Area (NPA) code, commonly called an area code, followed by a seven-digit local number. The format is usually represented as:

```
NXX-NXX-XXXX
```

where N is any digit from 2 through 9 and X is any digit from 0 through 9.

### What are CLI and CLD Validation?

If a CLI or CLD is in an invalid format or does not appear in the North American National Numbering databases, calls from that number will be rejected.

### Are CLI and CLD Validation Applied to All Calls?

CLI and CLD Validation will be applied to all outbound calls between NANPA (North American Numbering Plan Administration) numbers, except Toll-Free Numbers, from June 6th, 2022.

### Are Calls to International Destinations Subject to CLI and CLD Validation?

CLI and CLD validation are subject to outbound calls from Telnyx customers to the PSTN, between CLI and CLD from North American Numbering Plan geographies. These comprise the United States and its territories, Canada, Bermuda, Anguilla, Antigua & Barbuda, the Bahamas, Barbados, the British Virgin Islands, the Cayman Islands, Dominica, the Dominican Republic, Grenada, Jamaica, Montserrat, Sint Maarten, St. Kitts and Nevis, St. Lucia, St. Vincent and the Grenadines, Trinidad and Tobago, and Turks & Caicos.

### Can I Disable CLI and CLD Validation?

Since CLI and CLD validation is enabled at the service level, it will affect all customers and customers will not be able to turn off this validation.

### How Will I Know if My Calls Are Being Blocked?

If **CLI validation fails**, calls from that number will be rejected with a specific code:

- **SIP 403** "*The origination number does not have a subscriber assigned. The number is invalid.*"

If **CLD validation fails**, calls from that number will be rejected with a specific code:

- **SIP 404** "*The destination number does not have a subscriber assigned. The number is invalid.*"

Telnyx users can check this information in the Mission Control Portal through the [debugging tools](https://support.telnyx.com/en/articles/4304872-telnyx-debugging-tools).

### Is There a Way to Check if My Calls Will Be Blocked Prior to Calling?

Telnyx users can verify if numbers are CLI and CLD validated using the [Number Lookup](https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide) tool in the portal.

### Is CLI Validation Applicable to Telnyx Numbers Only?

CLI validation will be applicable to all numbers used to perform outbound calls through the Telnyx network, regardless of the number provider.

### What Should I Do if My Call Is Blocked, Even if My CLI or CLD Are Valid?

If there is a case where your call has been blocked by CLI and CLD validation, and the CLI and CLD are valid, please [report to our support team](https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support).

## Forwarding SMS to Your Mobile Number (Zapier)

This guide walks you through setting up a Zapier automation (called a "Zap") that forwards all inbound text messages received by your Telnyx number to your personal mobile number. Estimated setup time is 15 minutes.

### Prerequisites

Before you begin, ensure you have the following:

1. **Telnyx Account:** Sign up at <https://telnyx.com/sign-up> if you don't have one.
2. **SMS-enabled phone number:** Purchase an SMS-capable number from the Telnyx Portal.
3. **Messaging Profile:** Created and assigned to your Telnyx number.
4. **API V2 Key:** Generated in the Telnyx Mission Control Portal.
5. **Zapier Account:** Free accounts available at <https://zapier.com/>.

### Step 1: Connect to the Telnyx Integration on Zapier

1. Visit the Telnyx Zapier Integration page: <https://zapier.com/apps/telnyx/integrations>.
2. Click **Connect** to add Telnyx to your Zapier account.
3. If prompted, sign in to your Zapier account.

### Step 2: Create a New Zap

1. Go to your Zapier Dashboard: <https://zapier.com/app/dashboard>.
2. Click **Create Zap** (or **Make a Zap!**) in the top-right corner.

### Step 3: Configure the Trigger (Receive a Message)

1. In the **App** search field, search for and select **Telnyx**.
2. Under **Choose Trigger Event**, select **Receive a Message**.
3. Click **Continue**.
4. Select the Telnyx account to use for receiving messages.
   - If your account isn't listed, click **Add Account** and enter your API V2 Key.
5. Click **Continue**.

**Important:** All messages received by numbers associated with the selected messaging profile will trigger this Zap. We highly recommend attaching only a single number to messaging profiles used for Zapier automations.

### Step 4: Test the Trigger

1. Click **Test Trigger** (or **Find Message**).
2. Zapier will pull in a sample inbound message webhook to set up the action stage.
3. If successful, you'll see sample message data.
4. Click **Continue** to proceed to the Action step.

### Step 5: Configure the Action (Send SMS)

1. In the **Do This...** step, search for and select **Telnyx**.
2. Under **Choose Action Event**, select **Send SMS**.
3. Click **Continue**.
4. Select your Telnyx account (or sign in if prompted).
5. Click **Continue**.

### Step 6: Customize the SMS Settings

Configure the following fields:

- **Source Number:** Enter your Telnyx number in E.164 format (e.g., +14155551234).
- **Destination Number:** Enter your personal mobile number in E.164 format (e.g., +13105559876).
- **Message Content:** See format below.

For the **Message Content** field, enter something like:

```
FWD FROM: [From Phone Number]
BODY: [Text]
```

**Note:** "From Phone Number" and "Text" are dynamic fields from the trigger. Use the dropdown on the right side of the Message Content field to insert these variables into your message body.

Click **Continue**.

### Step 7: Test Your Zap

1. Click **Test Step** (or **Send Test**).
2. You should receive a test message on your mobile phone similar to:

   `FWD FROM: +16365553226 BODY: Sample Text Sent From Zapier!`

**Troubleshooting:** If the test fails, verify that:

- Your Source and Destination numbers are in E.164 format (include +1 for US/Canada).
- Your Telnyx number is messaging-enabled and assigned to a messaging profile.
- Your 10DLC registration is complete (for US long codes).

### Step 8: Activate Your Zap

1. If the test was successful, click **Publish** (or **Turn on Zap**).
2. Your Zap is now active.

### How It Works

Once activated, your Zap will:

1. **Trigger:** When someone sends a text message to your Telnyx number.
2. **Action:** Automatically forward that message to your personal mobile number with the sender's phone number and message content.

### Best Practices

- **Use a dedicated messaging profile** — Attach only one number to profiles used for Zapier to avoid unintended triggers.
- **Monitor your Zap** — Check Zapier's Task History to ensure messages are being forwarded successfully.
- **Use E.164 format** — Always include the country code (e.g., +1 for US) when entering phone numbers.
