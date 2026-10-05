---
title: "Guide to Sole Proprietor 10DLC Brand and Campaign Registration"
summary: "For small business owners and freelancers without a federal Tax ID (EIN), the Sole Proprietor registration is the required path for sending compliant A2P (Application-to-Person) messages to local US numbers."
sources:
- url: "https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration"
updated_at: 2026-07-23T17:53:31Z
tags: [support-docs]
source_path: "support-docs/en--articles--13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration.md -->

# Guide to Sole Proprietor 10DLC Brand and Campaign Registration

For small business owners and freelancers without a federal Tax ID (EIN), the Sole Proprietor registration is the required path for sending compliant A2P (Application-to-Person) messages to local US numbers.

---

## Prerequisites

Before you begin, ensure you have a Telnyx account and at least one local US 10-digit long code (10DLC) number. You must also meet the following criteria:

- You do **not** have an EIN (Employer Identification Number).
- You are a single individual operating a business.
- You require low-volume messaging (typically 1,000 messages per day).

---

## Step 1: Gather Required Information

Accuracy and consistency are critical for 10DLC approval. Ensure the following details match your legal identity exactly:

- **Legal Name:** Your full name as it appears on government-issued ID.
- **Email Address:** A permanent business or personal email (free providers like Gmail are permitted for Sole Proprietors, unlike large corporations).
- **Mobile Phone Number:** A valid mobile number capable of receiving SMS (required for identity verification).
- **Physical Address:** Your primary residence or business location (PO Boxes/PMBs are not accepted).
- **Website or Social Media:** A URL (e.g., LinkedIn, professional Facebook page, or business website) that demonstrates your business's legitimacy.

---

## Step 2: Create a Sole Proprietor Brand

1. Log in to the [Telnyx Mission Control Portal](https://portal.telnyx.com/).
2. Navigate to **Messaging** > **10DLC** > **Brands**.
3. Click **Create New Brand**.
4. For **Entity Type**, select **Sole Proprietorship**.
5. Fill in the information gathered in Step 1.
6. Click **Save**.

---

## Step 3: Brand Verification (OTP PIN Process)

Sole Proprietor brands require a manual verification loop to confirm identity. You must complete the following within **24 hours** once the PIN is received:

1. **Request the PIN:** Send an email to **[10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com)** stating that you have created a Sole Proprietor brand and need an OTP PIN for verification.
2. **Receive the PIN:** Telnyx will send a unique OTP PIN to the mobile phone number associated with your brand.
3. **Verify:** Email the OTP PIN back to **[10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com)**.
4. **Important:** If the PIN is not returned within 24 hours, it will expire, and you will need to restart the brand creation process.

## **API Option: Triggering and Verifying the OTP PIN**

For users who prefer to automate the OTP verification process via the Telnyx API, the following endpoints are available. Full documentation is available in the

Sole Proprietor 10DLC Registration developer docs: https://developers.telnyx.com/docs/messaging/10dlc/sole-proprietor

## **Step 3a — Trigger OTP**

Sends a 6-digit PIN via SMS to the mobile phone number associated with the brand:

curl -X POST https://api.telnyx.com/v2/10dlc/brand/{brand\_id}/smsOtp \

-H "Content-Type: application/json" \

-H "Authorization: Bearer YOUR\_API\_KEY" \

-d '{

"pinSms": "Your Telnyx verification code is @OTP\_PIN@. This code expires in 24 hours.",

"successSms": "Your Telnyx 10DLC brand has been verified successfully."

}'

The @OTP\_PIN@ placeholder is replaced with the actual 6-digit PIN when the SMS is sent.

## **Step 3b — Check OTP Status (optional)**

Poll the delivery status to confirm the SMS was received:

curl -X GET https://api.telnyx.com/v2/10dlc/brand/{brand\_id}/smsOtp \

-H "Authorization: Bearer YOUR\_API\_KEY"

Possible delivery statuses:

| **Status** | **Description** |
| --- | --- |
| PENDING | OTP request submitted, awaiting delivery |
| DELIVERED\_HANDSET | SMS delivered to the mobile device |
| DELIVERY\_FAILED | SMS delivery failed |
| VERIFIED | OTP PIN successfully verified |
| EXPIRED | OTP PIN expired (24-hour window) |

## **Step 3c — Verify OTP PIN**

Once the user receives the PIN and provides it back, verify it:

curl -X PUT https://api.telnyx.com/v2/10dlc/brand/{brand\_id}/smsOtp \

-H "Content-Type: application/json" \

-H "Authorization: Bearer YOUR\_API\_KEY" \

-d '{

"otpPin": "123456"

}'

Upon successful verification:

- The brand identityStatus changes to VERIFIED
- The successSms message is sent to the mobile phone
- The brand registration fee is charged
- You can now create campaigns

If the OTP expires, simply call the trigger endpoint again to send a new PIN.

---

## Step 4: Create a 10DLC Campaign

Once your brand status shows as **Verified**, you can submit your messaging use case for review.

1. Navigate to **Messaging** > **10DLC** > **Campaigns**.
2. Click **Create New Campaign**.
3. Select your **Sole Proprietor Brand** and choose the **Sole Proprietor** use case.
4. **Message Flow:** Describe how users opt into your messages.

   - *Example:* "Users visit [YourURL.com] and enter their phone number to receive alerts. They must check a box to agree to SMS terms. Consent is not a condition of purchase."
5. **Sample Messages:** Provide at least two examples. These must include your **Brand Name** and **Opt-out instructions** (e.g., "Reply STOP to unsubscribe").

---

## Step 5: Assign Numbers to Your Campaign

After campaign review is complete (typically **2–3 business days**), you must link your numbers to the campaign to avoid filtered traffic. This review timeframe is not carrier-specific; carrier provisioning follows separately.

1. Go to **Numbers** > **My Numbers**.
2. Select the number(s) you wish to use.
3. In the **10DLC** section, assign your approved **Brand** and **Campaign**.
4. Click **Save**.

---

## Fees and Charges

The following fees are passed through from the carriers for Sole Proprietor registrations:

| **Item** | **Estimated Fee** | **Frequency** |
| --- | --- | --- |
| **Brand Registration** | $4.50 | One-time |
| **Campaign Vetting** | $15.00 | Per submission/resubmission |
| **Monthly Maintenance** | $2.00 | Monthly |

---

Notes #1:

If the entity's legal name or website contains any of the following terms, the entity does NOT qualify as a Sole Proprietor and must register as a standard business brand using a federal Tax ID (EIN).

| **Category** | **Disqualifying Terms** |
| --- | --- |
| Business suffixes | LLC, Inc, Ltd, Corp, Company, LLP |
| Education | School, College, University, Academy |
| Finance / Banking | Bank, Loan, Mortgage, Cash, Money, Fund, Wealth, Investment, Capital, Credit, Union, Lending, Financial, Collections, Insurance |
| Healthcare | Hospital, Clinic, Vet, Health, Spa |
| Real Estate | Property, Real Estate, Management, Agency, Home, Buyer |
| Organizations | Church, Club, Group, Charity, Center, Ministry, Ministries, Chamber |
| Government / Non-profit | County, .gov, .org |
| Other | Software, Marketing, Media, Employees, Staff, .ai |

Notes #2:

Multiple campaigns for the same Sole Proprietor brand cannot be created. This includes campaigns created in other platforms. Only a single campaign can be created for a Sole Prop brand.

## Additional Resources

- [10DLC Campaign Compliance Requirements](https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements)
- [Guide to 10DLC Message Flow Field](https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field)
- [Frequently Asked Questions about 10DLC](https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc)

For further assistance, please reach out to **[10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com)**.
