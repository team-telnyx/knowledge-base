---
title: 10DLC Registration and Compliance
summary: A consolidated reference for registering and operating 10DLC messaging on
  Telnyx, covering the end-to-end brand and campaign workflow, mock testing, CTA and
  message flow requirements, opt-in form design, privacy policy language, sample messages,
  age gates, political campaigns, common errors, and associated fees.
sources:
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
- url: https://support.telnyx.com/en/articles/10646301-telnyx-10dlc-process
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
- url: https://support.telnyx.com/en/articles/12812898-10dlc-mock-brands-and-campaigns
- url: https://support.telnyx.com/en/articles/5896911-how-to-create-a-10dlc-brand
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
updated_at: 2026-07-17T09:00:56Z
---

# 10DLC Registration and Compliance

*Part 1 of 5 — see also: [Part 2](10dlc-registration-and-compliance--part-2.md), [Part 3](10dlc-registration-and-compliance--part-3.md), [Part 4](10dlc-registration-and-compliance--part-4.md), [Part 5](10dlc-registration-and-compliance--part-5.md)*

A consolidated reference for registering and operating 10DLC messaging on Telnyx, covering the end-to-end brand and campaign workflow, mock testing, CTA and message flow requirements, opt-in form design, privacy policy language, sample messages, age gates, political campaigns, common errors, and associated fees.

## Overview

10DLC (10-Digit Long Code) is the US carrier framework for application-to-person (A2P) messaging on local numbers. Any business sending outbound SMS from a US local 10DLC number to a US local number must register a brand and a campaign with The Campaign Registry (TCR) before traffic can flow. Telnyx provides both a Mission Control Portal workflow and a set of APIs for registration, and the same compliance rules apply regardless of which surface is used.

The end-to-end process is: create a verified brand, create a campaign under that brand, pass Telnyx and carrier review, then assign numbers to the approved campaign. Throughout, the campaign must include a compliant call-to-action (CTA), message flow, opt-in/opt-out/HELP keywords and responses, sample messages, and a privacy policy that protects SMS opt-in data.

## End-to-End 10DLC Process

For outbound texts from local US numbers to local US numbers, follow these steps:

1. **Create a Brand.** Every perceived sender needs a brand. Brand information must match IRS Form CP-575 to reach "Verified" status, because TCR uses the IRS database as its source of truth. See [How to create a 10DLC brand](how-to-create-a-10dlc-brand.md).
2. **Create a Campaign.** Once the brand is Verified, create a campaign under it. You must select "True" for the Opt-in, Opt-out, and HELP radio buttons or TCR will reject the campaign. Campaigns with a TCR ID starting with `4b3` or a status of "Failed TCR Review" were not created successfully, which often happens when the campaign is created before the brand is verified. See [How to create a 10DLC campaign](how-to-create-a-10dlc-campaign.md).
3. **Telnyx Review.** Telnyx reviews the campaign the same day or next business day. You will receive one of two emails at the account's main username address:
   - *Sent for Carrier Review* — submitted downstream; carrier review takes 3 business days or less depending on volume.
   - *Flagged for Corrections* — campaign contains incorrect or impermissible content; no further action is taken until the 10DLC squad is notified at [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com). Reply on the same email thread for each campaign.
4. **Carrier Outcome.** Once the carrier responds, you receive either:
   - *Approved* — assign up to 49 numbers to the campaign and begin messaging. See [How to assign a number to a campaign](how-to-assign-a-number-to-a-campaign.md).
   - *Declined* — email explains why, including error codes. See [10DLC Carrier Error Codes Explanations](10dlc-carrier-error-codes-explanations.md).
5. **Ongoing.** To add email addresses for campaign status notifications, email [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) with the main Telnyx username email. For non-compliance or portal issues, contact [support@telnyx.com](mailto:support@telnyx.com).

## Creating a Brand

A brand represents the legal entity sending the messages. In the Mission Control Portal, navigate to Messaging → [10DLC Brand](https://portal.telnyx.com/#/messaging-10dlc/brands) and select "Create a brand". Via the API, see the [create-brand endpoint](https://developers.telnyx.com/api/messaging/10dlc/create-brand-post).

### Business Information

For US brands, if the entered information does not match IRS Form CP-575 the brand will remain permanently unverified. All fields should be correct, complete, and free of typos, since errors can limit throughput or delay verification.

- **Legal Company Name** — official legal name; must match the name under which the EIN is issued.
- **DBA or Brand Name** — Doing Business As or trade names. Required even if it matches the legal name.
- **Legal Form** — Charity/Non-Profit, Government, Private Company, or Publicly Traded Company.
- **Vertical** — industry vertical that best matches the business.
- **Country of Registration** — country where the business is registered.
- **Website** — URL directing to the business website.
- **EIN Issuing Country** — country that issued the EIN or alternative ID.
- **EIN** — Employer Identification Number issued by the IRS. If the business has no EIN, use an alternative business identification number from the relevant issuing country.
- **Stock Symbol / Stock Exchange** — required only for Publicly Traded Companies.
- **Reseller** — check if the business resells products and services to other end-user businesses (Independent Service Vendors / ISVs). See [10DLC for ISVs](10dlc-for-isvs.md).
- **Business Address, City, State/Region, Postal Code** — must match the name under which the EIN is issued.

### Brand Contact Details

- **Email Address** — an authorized representative's individual email, not a group alias.
- **Phone Number** — an authorized representative's phone number.

### Publicly Traded Brands and the Auth+ Process

Brands selecting the Public_Profit entity type because they are publicly traded on the US stock market must complete a 2FA process to verify the brand. The contact email must match the web domain of the brand. After submission, the contact email receives a message from [noreply@auth.campaignregistry.com](mailto:noreply@auth.campaignregistry.com); open the link and complete the short form with name, title, and contacts. Until Auth+ is complete, no new campaigns can be created for Public_Profit brands. For existing Public_Profit brands that need a new campaign, send the brand ID and brand business contact to [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) to trigger the 2FA email. As of August 1, 2025 there is a $15 fee per Auth+ attempt; check the Telnyx portal for current pricing.

### Canadian Brands

- In place of the EIN, provide Provincial or Federal Corporation/Registry ID Numbers (Private Profit, Public Profit brand types). These are the IDs created when a business is initially formed and registered in their home province or with Corporations Canada as a federal corporation — they are not the same as the Canada federal business number used for taxation.
- Avoid using the Canadian Federal Business Number (BN) or Canadian Revenue Agency Tax Account Numbers in the EIN section. If this is the only identifier available, the brand can still be created but will need to be manually vetted, so have official registration documents ready.
- Provincial IDs sometimes drift from currently posted business information; have official registration documents on hand in case a manual vet is required.

### Billing

There is a one-time, non-refundable $4 fee for registering a brand, passed through from The Campaign Registry. TCR is an independent organization that manages 10DLC brands and campaigns in coordination with mobile network operators.

### After Registration

The brand automatically goes through identity verification. TCR validates the information and the brand's identity status is immediately available in the Mission Control Portal. The most common cause of an unverified brand is an error in the submitted information; review all fields for correctness. If the EIN is wrong, contact the Telnyx team for assistance. Better commercial terms can be achieved by submitting the brand for third-party vetting, available as an option in brand settings once the brand is created.
