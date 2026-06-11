---
title: 10DLC Compliance
summary: 10DLC (10 Digit Long Code) is the mandatory compliance framework for application-to-person
  (A2P) SMS and MMS traffic sent from US local long-code numbers. All businesses must
  register a Brand and Campaign through The Campaign Registry (TCR) or face blocked
  traffic, higher fees, and substantial fines from mobile network operators.
sources:
- url: https://support.telnyx.com/en/articles/10509796-10dlc-registration-deadline-february-3
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
- url: https://support.telnyx.com/en/articles/11421359-10dlc-for-chiropractors
- url: https://support.telnyx.com/en/articles/11788086-10dlc-authentication-for-publicly-traded-brands
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
- url: https://support.telnyx.com/en/articles/13545282-guide-to-sole-proprietor-10dlc-brand-and-campaign-registration
- url: https://support.telnyx.com/en/articles/3679260-frequently-asked-questions-about-10dlc
- url: https://support.telnyx.com/en/articles/5593977-isvs-10dlc
- url: https://support.telnyx.com/en/articles/5634625-10dlc-fees-and-charges
- url: https://support.telnyx.com/en/articles/5664840-telnyx-10dlc-compliance
- url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
- url: https://support.telnyx.com/en/articles/6325731-register-for-10dlc-messaging
- url: https://support.telnyx.com/en/articles/6417677-telnyx-10dlc-compliance-directory
updated_at: 2026-06-11T11:10:47Z
---

# 10DLC Compliance

*Part 2 of 3 — see also: [Part 1](10dlc-compliance--part-1.md), [Part 3](10dlc-compliance--part-3.md)*

10DLC (10 Digit Long Code) is the mandatory compliance framework for application-to-person (A2P) SMS and MMS traffic sent from US local long-code numbers. All businesses must register a Brand and Campaign through The Campaign Registry (TCR) or face blocked traffic, higher fees, and substantial fines from mobile network operators.

## The 10DLC Registration Process

Compliance follows three core steps:

1. **Create a Brand** — Register your business identity.
2. **Create a Campaign** — Declare your messaging use case.
3. **Assign numbers** — Link phone numbers to your approved Campaign.

### Step 1: Create a Brand

In the [Mission Control Portal](https://portal.telnyx.com), navigate to **Messaging → 10DLC → Brands** and click **Create Brand**, or use the [10DLC API](https://developers.telnyx.com/api/messaging/10dlc/create-brand-post).

**Required business information:**

| Field | Notes |
|---|---|
| Legal Company Name | Must match the name under which your EIN is issued |
| DBA or Brand Name | Required even if same as legal name |
| Entity Type | Charity/Non-Profit, Government, Private Company, or Publicly Traded Company |
| Vertical | Industry vertical that best matches your business |
| Country of Registration | Country where your business is registered |
| Website | URL for your business website |
| EIN | Employer Identification Number (US) or alternative business ID |
| Stock Symbol / Exchange | Required only for Publicly Traded Companies |
| Reseller | Check if you are an ISV |
| Business Address | Must match the address associated with your EIN |
| Brand Contact Email | Individual's email (not a group alias) |
| Brand Contact Phone | Phone number of an authorized representative |

For US brands, information **must match IRS Form CP-575** to achieve "Verified" status. TCR uses the IRS database as its source of truth. If information does not match, the brand will remain permanently unverified (see [10DLC Unverified Brand](10dlc-unverified-brand.md)). There is a one-time, non-refundable **$4 brand registration fee** passed through from TCR.

After registration, the brand goes through automatic identity verification. Brands can also be submitted for **third-party vetting** to achieve better throughput and commercial terms.

#### Publicly Traded Brands and Auth+

Publicly Traded brands must complete the **Auth+** two-factor authentication process. When creating the brand, include a representative's individual email address that shares the domain of the brand's website. After submission, the contact receives a 2FA email from `noreply@auth.campaignregistry.com` containing a Verification PIN and link. The contact must click the link and provide their first name, last name, job title, and the PIN within **7 days**. Until Auth+ is completed, no new campaigns can be created for Publicly Traded brands.

For existing Publicly Traded brands that need Auth+ triggered, email the brand ID and business contact email to [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com). As of August 1, 2025, there is a fee for Auth+ attempts; consult the Telnyx portal for current pricing.

#### Canadian Brands

When registering a Canadian brand:

- Use **Provincial or Federal Corporation/Registry ID Numbers** in place of the EIN (for Private/Public Profit types). These are the IDs created when the business is initially formed—not the Canada Federal Business Number (BN) or CRA Tax Account Numbers.
- If you only have a BN or CRA number, you can still create the brand but it will require manual vetting—have your official registration documents ready.
- Provinces sometimes change records over time, which can cause mismatches with TCR data. Keep official registration documents handy.

#### Sole Proprietor Brands

For individuals without an EIN who operate a single-person business requiring low-volume messaging (typically ≤1,000 messages/day), the **Sole Proprietor** path is available.

**Gather required information:**

- Legal name (as on government-issued ID)
- Email address (free providers like Gmail are acceptable for Sole Proprietors)
- Mobile phone number (capable of receiving SMS for identity verification)
- Physical address (no PO Boxes or PMBs)
- Website or social media URL demonstrating business legitimacy

**Verification (OTP PIN process):**

1. After creating the Sole Proprietor brand in the portal (**Messaging → 10DLC → Brands**, entity type **Sole Proprietorship**), email [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) requesting an OTP PIN.
2. A unique PIN is sent to the mobile number on the brand.
3. Email the PIN back to [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) within **24 hours** or it expires and the brand creation process must restart.

**Sole Proprietor fees:**

| Item | Fee | Frequency |
|---|---|---|
| Brand Registration | $4.00 | One-time |
| Campaign Vetting | $15.00 | Per submission/resubmission |
| Monthly Maintenance | $2.00 | Monthly |

#### Mock Brands

For testing API behavior, webhook events, or 10DLC provisioning pipelines at no cost, you can create **mock brands** and **mock campaigns**.

- **Portal:** When creating a brand, check the box "Create as a mock brand to test 10DLC." The $4.00 registration fee is waived.
- **API:** Set the `mock` field to `true` when creating a brand.
- Any campaign created under a mock brand is automatically a mock campaign with no registration or monthly recurring fees.
- Mock campaigns **cannot** be used for real 10DLC traffic.
- Mock brands and campaigns can be deleted via the standard API deletion endpoints or in the portal when testing is complete.

### Step 2: Create a Campaign

Once your brand is **Verified**, navigate to **Messaging → 10DLC → Campaigns** and click **Create Campaign**, or use the [10DLC API](https://telnyx.mintlify.app/api-reference/campaign/submit-campaign).

**Critical requirements:**

- You **must select "True"** for Opt In, Opt Out, and HELP radio buttons. TCR will reject the campaign otherwise.
- Do **not** create a campaign before the brand is verified—this results in failed campaigns (TCR ID starting with `4b3` or status "Failed TCR Review").
- A phone number can be assigned to only one Campaign, but a Campaign can have many assigned numbers (up to 49 without special T-Mobile approval).
- A Brand can have up to five Campaigns.
- A Mixed Use Case allows up to five Sub-Use Cases on a single phone number.

**Special Use Cases** (Agents & Franchises, Carrier Exemptions, Charity, Conversational Messaging, Emergency, Political, Social, Sweepstake) may require pre-approval, post-approval, and/or different vetting agents. Political campaigns must be vetted via [CampaignVerify](https://www.campaignverify.org/) or [Aegis](https://aegismobile.com/).

**Campaign description example (Chiropractor):**

For chiropractors, select **Healthcare** as the vertical and **Low Volume Mixed** with a **Customer Care** sub-use case. The campaign description should describe sending SMS customer care messages to patients. The CTA/Message Flow must detail how consent is obtained (e.g., verbal opt-in at the front desk with disclosure language), and auto-response messages must be configured for START, STOP, and HELP keywords. Sample messages must include the brand name and opt-out instructions. Campaign content attributes should set Subscriber opt-in, Subscriber help, and Subscriber opt-out to "Yes," and Direct lending, Embedded link, Embedded phone number, Number pooling, Affiliate marketing, and Age-gated content to "No."

**Sole Proprietor Campaigns:** Select the **Sole Proprietor** use case. Provide a message flow describing how users opt in, and at least two sample messages that include your brand name and opt-out instructions (e.g., "Reply STOP to unsubscribe").

### Step 3: Campaign Review

After submission, Telnyx reviews the campaign (same day or next business day). You will receive one of two emails at your Telnyx account's main username email:

- **Sent for Carrier Review** — The campaign has been submitted downstream. Carrier review takes **3 business days or less**.
- **Flagged for Corrections** — The campaign contains incorrect or impermissible content with feedback on what needs updating. No further action is taken until you notify [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com). Reply on the same email thread for each campaign.

After carrier review, you receive one of two emails:

- **Approved** — You can assign up to 49 numbers and begin messaging.
- **Declined** — You'll receive error codes explaining why. See [10DLC Carrier Error Codes and Explanations](10dlc-carrier-error-codes-and-explanations.md). Respond on the same email thread with questions or updates for resubmission.

For Sole Proprietor campaigns, carrier approval typically takes **3–7 business days**.

### Step 4: Assign Numbers to Campaign

After approval, link your numbers:

1. Navigate to **Numbers → My Numbers** in the portal.
2. Select the number(s) you wish to use.
3. In the **10DLC** section, assign your approved Brand and Campaign.
4. Click **Save**.

If you encounter a daily number-adding limit, try again in one business day (an industry constraint on bulk number assignments).

**When porting numbers to Telnyx:** Create and approve your 10DLC campaigns in Telnyx first, then begin the porting process. Before the numbers fully port, work with your old carrier to remove the 10DLC campaigns from their system—otherwise the numbers will remain tied to the losing carrier and cannot be assigned to Telnyx campaigns.
