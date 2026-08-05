---
title: Telnyx 10DLC Process
summary: A consolidated guide to registering, managing, and troubleshooting 10DLC
  brands, campaigns, and number assignments on the Telnyx platform, including fees,
  ISV requirements, sole proprietor registration, mock testing, suspension handling,
  and publicly traded brand authentication.
sources:
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
- url: https://support.telnyx.com/en/articles/10723378-10dlc-campaign-suspended
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
- url: https://support.telnyx.com/en/articles/5593977-isvs-10dlc
- url: https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges
- url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
updated_at: 2026-08-05T13:25:29Z
---

# Telnyx 10DLC Process

*Part 4 of 6 — see also: [Part 1](telnyx-10dlc-process--part-1.md), [Part 2](telnyx-10dlc-process--part-2.md), [Part 3](telnyx-10dlc-process--part-3.md), [Part 5](telnyx-10dlc-process--part-5.md), [Part 6](telnyx-10dlc-process--part-6.md)*

A consolidated guide to registering, managing, and troubleshooting 10DLC brands, campaigns, and number assignments on the Telnyx platform, including fees, ISV requirements, sole proprietor registration, mock testing, suspension handling, and publicly traded brand authentication.

## ISVs and 10DLC

An Independent Service Vendor (ISV) is a type of business that sells products and services to other end users who are also businesses. If your end-users are a separate business entity, you are in fact an ISV. For example, a SaaS product that sells messaging services to doctor's offices is considered an ISV. A business that specializes in SMS marketing for other businesses is also considered an ISV. See [ISVs & 10DLC](isvs-10dlc.md).

![Diagram showing Telnyx directly connected to an ISV, with that ISV in turn reselling to several customers.](_images/84865f0646e6af38.png)

### How ISVs Register for 10DLC

If your business is an ISV, for every end-user you're reselling to, you will need to create a separate brand. After creating the brand, you will need to create campaigns so that you can assign campaign IDs to the phone numbers. It is critical that you do not share the phone numbers across multiple brands. By doing so, you will violate the terms of usage for 10DLC and potentially will get fined and blocked until the traffic is compliant.

Once you create your campaign, assign the campaign ID to a set of phone numbers. You can assign a maximum number of 49 phone numbers without requiring special permission from T-Mobile, obtained by completing their [form [PDF]](https://assets.ctfassets.net/taysl255dolk/7jAkNNeHEqfeNMF3PnukdG/603e4f4177ac79bd239fcdb87e41f900/TMUS-10DLC-Number-Pool-Request_v2.0.numbers).

![A pictorial representation of 10DLC campaigns for ISVs.](_images/eb030506379b5f21.png)

### Sharing Traffic Among Numbers

To be 10DLC compliant, every number needs to be associated with a campaign, and each campaign can only be associated with one brand. This means that no two brands can be on the same number. If you are currently sharing numbers across brands, unless you have a special arrangement with the mobile network operators, you will need to update your messaging architecture such that only one brand is using any given number to send messages. Mobile network operators will not approve ISVs for special consideration in this case.

We recommend that you take an iterative approach to migrate this architecture end-user by end-user:

1. Create a new Messaging Profile.
2. Buy or use a dedicated Phone Number for this Messaging Profile.
3. Create a 10DLC Brand for the end-user.
4. Create a 10DLC Campaign.
5. Assign the 10DLC Campaign to the Phone Number.

Now in your messaging application's backend code, add logic such that the end-user you're working on starts using the Messaging Profile and Phone Number created above.

### Alternatives to Creating Brands and Campaigns for Each End-User

If you'd like to keep using long-code numbers to send A2P messages, your options are limited to the following:

1. Using one brand and one campaign across end-users, with an approved Number Pooling agreement with T-Mobile. Unless your business is a franchise, this is unlikely to be approved by T-Mobile.
2. Using one brand and one campaign across end-users, without explicit approval from mobile network operators. This will likely result in your business receiving fines from mobile network operators, and will likely lead to mobile network operators blocking your traffic.
3. Use Number Lookup tools to identify and exclude T-Mobile numbers from receiving messages as part of your customers' campaigns.

Toll-free numbers can also be used to send A2P messages, and are not subject to 10DLC requirements. There is, however, an approval process for sending messages via Toll-free numbers, and similar restrictions apply to using the same number across multiple end-users.

## Sole Proprietor Registration

For small business owners and freelancers without a federal Tax ID (EIN), the Sole Proprietor registration is the required path for sending compliant A2P messages to local US numbers. See [Guide to Sole Proprietor 10DLC Brand and Campaign Registration](guide-to-sole-proprietor-10dlc-brand-and-campaign-registration.md).

### Prerequisites

Before you begin, ensure you have a Telnyx account and at least one local US 10-digit long code (10DLC) number. You must also meet the following criteria:

- You do not have an EIN (Employer Identification Number).
- You are a single individual operating a business.
- You require low-volume messaging (typically 1,000 messages per day).

### Step 1: Gather Required Information

Accuracy and consistency are critical for 10DLC approval. Ensure the following details match your legal identity exactly:

- Legal Name: Your full name as it appears on government-issued ID.
- Email Address: A permanent business or personal email (free providers like Gmail are permitted for Sole Proprietors, unlike large corporations).
- Mobile Phone Number: A valid mobile number capable of receiving SMS (required for identity verification).
- Physical Address: Your primary residence or business location (PO Boxes/PMBs are not accepted).
- Website or Social Media: A URL (e.g., LinkedIn, professional Facebook page, or business website) that demonstrates your business's legitimacy.

### Step 2: Create a Sole Proprietor Brand

1. Log in to the Telnyx Mission Control Portal.
2. Navigate to Messaging > 10DLC > Brands.
3. Click Create New Brand.
4. For Entity Type, select Sole Proprietorship.
5. Fill in the information gathered in Step 1.
6. Click Save.

### Step 3: Brand Verification (OTP PIN Process)

Sole Proprietor brands require a manual verification loop to confirm identity. You must complete the following within 24 hours once the PIN is received:

1. Request the PIN: Send an email to 10dlcquestions@telnyx.com stating that you have created a Sole Proprietor brand and need an OTP PIN for verification.
2. Receive the PIN: Telnyx will send a unique OTP PIN to the mobile phone number associated with your brand.
3. Verify: Email the OTP PIN back to 10dlcquestions@telnyx.com.
4. Important: If the PIN is not returned within 24 hours, it will expire, and you will need to restart the brand creation process.

### Step 4: Create a 10DLC Campaign

Once your brand status shows as Verified, you can submit your messaging use case for review.

1. Navigate to Messaging > 10DLC > Campaigns.
2. Click Create New Campaign.
3. Select your Sole Proprietor Brand and choose the Sole Proprietor use case.
4. Message Flow: Describe how users opt into your messages. Example: "Users visit [YourURL.com] and enter their phone number to receive alerts. They must check a box to agree to SMS terms. Consent is not a condition of purchase."
5. Sample Messages: Provide at least two examples. These must include your Brand Name and Opt-out instructions (e.g., "Reply STOP to unsubscribe").

### Step 5: Assign Numbers to Your Campaign

After the carriers approve your campaign (typically 3-7 business days), you must link your numbers to the campaign to avoid filtered traffic.

1. Go to Numbers > My Numbers.
2. Select the number(s) you wish to use.
3. In the 10DLC section, assign your approved Brand and Campaign.
4. Click Save.

### Sole Proprietor Fees

| Item | Estimated Fee | Frequency |
| --- | --- | --- |
| Brand Registration | $4.00 | One-time |
| Campaign Vetting | $15.00 | Per submission/resubmission |
| Monthly Maintenance | $2.00 | Monthly |
