---
title: 10DLC and Messaging Compliance Reference
summary: This page consolidates Telnyx 10DLC and messaging compliance guidance, including
  carrier error codes for campaign declines, suspension and reactivation procedures,
  sole proprietor registration, shared campaign imports, toll-free verification requirements,
  and the full catalog of Telnyx messaging error codes.
sources:
- url: https://support.telnyx.com/en/articles/10547022-10dlc-carrier-error-codes-explanations
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
- url: https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
updated_at: 2026-07-17T09:00:38Z
---

# 10DLC and Messaging Compliance Reference

*Part 3 of 7 — see also: [Part 1](10dlc-and-messaging-compliance-reference--part-1.md), [Part 2](10dlc-and-messaging-compliance-reference--part-2.md), [Part 4](10dlc-and-messaging-compliance-reference--part-4.md), [Part 5](10dlc-and-messaging-compliance-reference--part-5.md), [Part 6](10dlc-and-messaging-compliance-reference--part-6.md), [Part 7](10dlc-and-messaging-compliance-reference--part-7.md)*

This page consolidates Telnyx 10DLC and messaging compliance guidance, including carrier error codes for campaign declines, suspension and reactivation procedures, sole proprietor registration, shared campaign imports, toll-free verification requirements, and the full catalog of Telnyx messaging error codes.

## Sole Proprietor 10DLC Brand and Campaign Registration

For small business owners and freelancers without a federal Tax ID (EIN), the Sole Proprietor registration is the required path for sending compliant A2P (Application-to-Person) messages to local US numbers.

### Prerequisites

Before you begin, ensure you have a Telnyx account and at least one local US 10-digit long code (10DLC) number. You must also meet the following criteria:

- You do **not** have an EIN (Employer Identification Number).
- You are a single individual operating a business.
- You require low-volume messaging (typically 1,000 messages per day).

### Step 1: Gather Required Information

Accuracy and consistency are critical for 10DLC approval. Ensure the following details match your legal identity exactly:

- **Legal Name:** Your full name as it appears on government-issued ID.
- **Email Address:** A permanent business or personal email (free providers like Gmail are permitted for Sole Proprietors, unlike large corporations).
- **Mobile Phone Number:** A valid mobile number capable of receiving SMS (required for identity verification).
- **Physical Address:** Your primary residence or business location (PO Boxes/PMBs are not accepted).
- **Website or Social Media:** A URL (e.g., LinkedIn, professional Facebook page, or business website) that demonstrates your business's legitimacy.

### Step 2: Create a Sole Proprietor Brand

1. Log in to the [Telnyx Mission Control Portal](https://portal.telnyx.com/).
2. Navigate to **Messaging** > **10DLC** > **Brands**.
3. Click **Create New Brand**.
4. For **Entity Type**, select **Sole Proprietorship**.
5. Fill in the information gathered in Step 1.
6. Click **Save**.

### Step 3: Brand Verification (OTP PIN Process)

Sole Proprietor brands require a manual verification loop to confirm identity. You must complete the following within **24 hours** once the PIN is received:

1. **Request the PIN:** Send an email to [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) stating that you have created a Sole Proprietor brand and need an OTP PIN for verification.
2. **Receive the PIN:** Telnyx will send a unique OTP PIN to the mobile phone number associated with your brand.
3. **Verify:** Email the OTP PIN back to [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com).
4. **Important:** If the PIN is not returned within 24 hours, it will expire, and you will need to restart the brand creation process.

### Step 4: Create a 10DLC Campaign

Once your brand status shows as **Verified**, you can submit your messaging use case for review.

1. Navigate to **Messaging** > **10DLC** > **Campaigns**.
2. Click **Create New Campaign**.
3. Select your **Sole Proprietor Brand** and choose the **Sole Proprietor** use case.
4. **Message Flow:** Describe how users opt into your messages. Example: "Users visit [YourURL.com] and enter their phone number to receive alerts. They must check a box to agree to SMS terms. Consent is not a condition of purchase."
5. **Sample Messages:** Provide at least two examples. These must include your **Brand Name** and **Opt-out instructions** (e.g., "Reply STOP to unsubscribe").

### Step 5: Assign Numbers to Your Campaign

After the carriers approve your campaign (typically **3–7 business days**), you must link your numbers to the campaign to avoid filtered traffic.

1. Go to **Numbers** > **My Numbers**.
2. Select the number(s) you wish to use.
3. In the **10DLC** section, assign your approved **Brand** and **Campaign**.
4. Click **Save**.

### Sole Proprietor Fees

| Item | Estimated Fee | Frequency |
| --- | --- | --- |
| Brand Registration | $4.00 | One-time |
| Campaign Vetting | $15.00 | Per submission/resubmission |
| Monthly Maintenance | $2.00 | Monthly |
