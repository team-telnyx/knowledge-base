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

*Part 1 of 6 — see also: [Part 2](telnyx-10dlc-process--part-2.md), [Part 3](telnyx-10dlc-process--part-3.md), [Part 4](telnyx-10dlc-process--part-4.md), [Part 5](telnyx-10dlc-process--part-5.md), [Part 6](telnyx-10dlc-process--part-6.md)*

A consolidated guide to registering, managing, and troubleshooting 10DLC brands, campaigns, and number assignments on the Telnyx platform, including fees, ISV requirements, sole proprietor registration, mock testing, suspension handling, and publicly traded brand authentication.

## Overview

If you are sending outbound texts from local US numbers to local US numbers, you must comply with 10DLC regulations. The end-to-end process on Telnyx involves creating a brand, creating a campaign, undergoing Telnyx and carrier review, and then assigning numbers to the approved campaign. This page consolidates the full lifecycle, including special cases for ISVs, sole proprietors, publicly traded brands, mock testing, suspension handling, and the associated fees.

## Create a Brand

For every perceived sender, you need to create a brand. See [How to create a 10DLC brand](how-to-create-a-10dlc-brand.md) for the full walkthrough.

Key requirements:

- The brand information must match the IRS Form CP-575 to achieve "Verified" status, because The Campaign Registry (TCR) uses the IRS database as its source of truth.
- For US brands, if the information entered does not match the IRS Form CP-575, the brand will remain permanently unverified.
- There is a one-time, non-refundable cost of $4 for registering a brand, passed through from the Campaign Registry.
- After registration, the brand automatically goes through an identity verification process; status is immediately available in the Mission Control Portal.
- If your brand is not verified, the most likely cause is an error in the information provided. Review all brand information for correctness, and if there is an error in the EIN, reach out to the Telnyx team for assistance.
- Third-party vetting is available to achieve better commercial terms; once a brand is created, an option to request third-party verification appears in brand settings in the Mission Control Portal.

### Business Information

You will be asked for the following business information when registering a 10DLC brand. This information is used by mobile network operators to verify your brand and can affect the throughput allowed to your campaigns. Ensure all information is correct, complete, and free of typos, as these issues can limit throughput or cause verification delays.

- Legal Company Name: The official, legal name of your business. This should match the name under which your EIN is issued.
- DBA or Brand Name: Doing Business As (DBA) or any trade names. This field is required, even if your brand name is the same as your Legal Company name.
- Legal form: Charity / Non-Profit Organization, Government, Private Company, or Publicly Traded Company.
- Vertical: The industry vertical which best matches your business.
- Country of Registration: The country in which your business is registered.
- Website: A URL directing to your business' website.
- EIN Issuing Country: The country that issued your business' EIN or identification number.
- EIN: Your business' Employer Identification Number. If your business does not have an EIN, use this field for an alternative business identification number supplied by your relevant issuing country.
- Stock Symbol and Stock Exchange: Required only for Publicly Traded Companies.
- Reseller: Check this box if your business re-sells products and services to other end users who are also businesses (Independent Service Vendors / ISVs). See [ISVs & 10DLC](isvs-10dlc.md).
- Business Address, City, State / Region, and Postal Code / Zip Code: The official, legal address of your business. This should match the name under which your EIN is issued.

### Brand Contact Details

- Email Address: The email address of an authorized representative for your business. Should be an individual's email and not a group alias.
- Phone Number: The phone number of an authorized representative for your business.

### Publicly Traded Brands and the Auth+ Process

If you create a brand and select the Public_Profit entity type because that brand is publicly traded on the US stock market, you will be required to complete a 2FA process to verify the brand. See [10DLC Authentication for Publicly Traded Brands](10dlc-authentication-for-publicly-traded-brands.md).

- The Auth+ process requires a representative individual's email address that matches the web domain of the brand when creating a new brand.
- Once you submit your brand, the contact email you entered will receive an email from noreply@auth.campaignregistry.com within a few days. Open it, click the link, and fill out a short form with your name, title, and contacts, then save. That completes the Auth+ process.
- If you have an existing Public_Profit brand that you need to create a new campaign for, send the brand id and brand business contact to 10dlcquestions@telnyx.com and Telnyx will trigger the 2FA email for you.
- Until the Auth+ process is completed, no new campaigns will be able to be created for Public_Profit brands.
- As of August 1, 2025, there is a $15 fee for Auth+ attempts (refer to the Telnyx portal for up-to-date pricing). After that date, you can still complete the Auth+ process, but there will be a small $12.5 fee for doing so whereas it is currently a free process.
- The contact will be sent a 2FA email containing a Verification PIN and a link. When the brand contact clicks on the link, they will be directed to a site and prompted to enter Brand Contact First Name, Brand Contact Last Name, Brand Contact Job Title, and the Verification PIN from the 2FA email. Once submitted, the brand will be authenticated.
- The contact has 7 days from the time they receive the 2FA email to complete the authentication. If they fail to do so, the 2FA email will need to be resent.

### Canadian Brands

Additional advice when registering a Canadian brand:

- In place of the EIN, provide your Provincial or Federal Corporation/Registry ID Numbers (Private Profit, Public Profit brand types). These are the identification numbers created when a business is initially formed and registered in their home province or with Corporations Canada as a federal corporation (these are not the same as the Canada federal business number, which is created for taxation purposes).
- Avoid using your Canadian Federal Business Number (BN) or Canadian Revenue Agency Tax Account Numbers in the EIN section. However, if this is the only identifier you have available, you can still create the brand with this information, just have your official registration documents prepared as the brand will need to be manually vetted.
- When using your Provincial identification number, provinces sometimes make changes over time which cause the original business registration to be misaligned with the currently posted information on the business. Have your official registration documents handy in case a manual vet of your brand needs to take place.
