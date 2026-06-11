---
title: 10DLC Campaign Registration and Compliance
summary: A comprehensive guide to registering, configuring, and maintaining compliant
  10DLC campaigns on Telnyx, covering use cases, trust scores, opt-in methods, message
  flow, CTA requirements, keyword configuration, number assignment, shared campaigns,
  and approval best practices.
sources:
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
- url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
updated_at: 2026-06-11T11:11:29Z
---

# 10DLC Campaign Registration and Compliance

*Part 3 of 4 — see also: [Part 1](10dlc-campaign-registration-and-compliance--part-1.md), [Part 2](10dlc-campaign-registration-and-compliance--part-2.md), [Part 4](10dlc-campaign-registration-and-compliance--part-4.md)*

A comprehensive guide to registering, configuring, and maintaining compliant 10DLC campaigns on Telnyx, covering use cases, trust scores, opt-in methods, message flow, CTA requirements, keyword configuration, number assignment, shared campaigns, and approval best practices.

## Call-to-Action (CTA) Compliance

The purpose of a CTA is to ensure the consumer consents to receive text messages and understands the nature of the program. CTA language must encourage or invite a consumer to opt into a messaging program and must be clearly and unambiguously displayed with the following disclosures:

- Program (Brand) Name / Product Description
- Message Frequency Disclosure (e.g., "Message frequency may vary")
- "Standard Message and Data Rates may apply" (if non-FTEU)
- "Reply STOP to opt out" (may appear in T&C)
- "Reply Help for help"
- Terms and Conditions OR link to T&C (not a popup)
- Privacy Policy OR link to a privacy policy
- Opt-in language must be exclusively for text messages

For TCR compliance, all campaigns must include the URL for the Terms and Conditions and Privacy Policy within the CTA section, even if this information is also available on the website. TCR provides specific fields for these links.

### Express Consent

Consumers may give express permission via:

- **Text** — The customer opts in by texting a specific keyword to a designated phone number. The workflow must include both the exact keyword and the designated phone number.
- **Form (electronic or paper)** — The customer provides consent by completing a form. For paper forms, the specific form must be attached to TCR for verification.
- **Website** — The customer opts in through a webform meeting all compliance requirements (optional phone number field, explicit SMS-only consent, proper disclaimers, unchecked checkbox by default).
- **Verbal** — The customer gives verbal consent during a phone call or in person. The process must clearly outline the scenarios in which consent is given.

### Express Written Consent

Consumers may sign a form granting express written permission. When a use case involves verbal or written/email opt-in, provide the script or sample CTA to verify all CTA aspects are fulfilled. Requirements are based on the T-Mobile Code of Conduct section 2.5 and CTIA Messaging Best Practices section 5.1.1.

## Keywords and Confirmation Messages

Each campaign must include keywords and sample messages for opt-in, opt-out, and help requests. Follow [10DLC Keywords and Confirmation Messages](10dlc-keywords-and-confirmation-messages.md) for detailed templates.

- **Opt-in confirmation message** — Must include the program name or product description, message frequency disclosure, instructions on how to request help, and "message and data rates may apply" (non-FTEU).
- **Help message** — Must include the program name or product description and customer care contact information.
- **Opt-out message** — Must include the program name or product description and confirmation of opt-out with a statement that no further messages will be sent.

Keywords and respective responses that don't follow the proper format will be a cause for campaign declines.

## Sample Messages

Sample messages must correspond to the registered use case. If a campaign is registered under multiple use cases (mixed), provide a sample message for each sub-use case. A marketing use case requires a minimum of 2 sample messages. A mixed use case requires a minimum of 2 but should have one for each selected use case.

Best practices:

- Provide up to 5 samples characterizing the different content you intend to send.
- Follow the 160-character limit to correspond with industry best practice.
- Include opt-out language (e.g., "Reply STOP to opt out") in at least one sample message.
- If the campaign has embedded link or embedded phone number attributes checked, the samples must contain the link/phone number.
- Samples must be consistent with the brand, campaign description, and website.

## Privacy Policy Requirements

Message senders must maintain a privacy policy accessible from the initial CTA. Key requirements:

- The privacy policy **cannot** allow for the sharing/selling of end user information to third parties for marketing purposes.
- It must explicitly state how end user data is used and, critically, that it is **not** shared with third parties/affiliates for any marketing purposes.
- If the privacy policy provides for data sharing or selling to nonaffiliated third parties, it must clarify that such sharing will **not** include a customer's SMS opt-in data or consent status.
- If the privacy policy does not currently mention data sharing, insert a clarification that you will not share SMS opt-in or consent status for non-service-related purposes.
- Any mentioning of 3rd Party Data Sharing, Renting, or Selling is disallowed unless the following disclosure is included: *"All the above categories exclude text messaging originator opt-in data and consent; this information will not be shared with any third parties."*

**Required language example:** *"We will not share your opt-in to an SMS campaign with any third party for purposes unrelated to providing you with the services of that campaign. We may share your Personal Data, including your SMS opt-in or consent status, with third parties that help us provide our messaging services, including but not limited to platform providers, phone companies, and any other vendors who assist us in the delivery of text messages."*

## Terms and Conditions

Comprehensive T&C may be presented in full beneath the CTA or accessible via a link in proximity to it. Popups are **not** an acceptable method for displaying T&C.

Required disclosures within T&C:

- Program (Brand) name
- Message frequency disclosure (not required for single-message programs)
- Product description
- Customer care contact information
- Opt-out information (not required for single-message programs)
- "Message and data rates may apply" (not required for FTEU-rated programs)
- Types of messages consumers can expect, texting cadence, associated costs, privacy policy, opt-out instructions, and other terms of use

## Political and Charity Campaigns

In addition to the standard requirements, political and charity campaigns must address:

- Political/Organization name and website
- Verification through [campaignverify.com](https://campaignverify.com)
- If donations are part of the program: "Donations will be secured through ___ and Accreditation listing is ___" must be present in the program summary
- A valid CTA and clear product description within the SMS terms of service that clearly discloses donations will be solicited
- Both the TCR CTA and the website CTA/opt-in language must include a disclaimer that "Donations will be solicited" if applicable

## SHAFT and Age Gating

Messaging content for controlled substances or adult content may be subject to additional carrier review and must include robust age verification. Acceptable age gates include:

1. Document Upload (Government ID)
2. Third-Party Identity Verification Services
3. Credit Card Verification
4. Reply with birthdate (format: MM/DD/YYYY)
5. A web opt-in form field requiring the user to include their birthday

Simply asking a user to "reply YES/AGREE" to confirm they are over a certain age is **not** considered robust age verification.
