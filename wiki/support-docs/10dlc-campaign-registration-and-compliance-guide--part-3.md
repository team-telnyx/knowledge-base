---
title: 10DLC Campaign Registration and Compliance Guide
summary: A consolidated reference for registering and maintaining 10DLC (10-Digit
  Long Code) A2P messaging campaigns on Telnyx, covering message flow, opt-in forms,
  keywords, privacy policy, sample messages, vetting, shared campaigns, and common
  carrier errors.
sources:
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- url: https://support.telnyx.com/en/articles/10645583-10dlc-privacy-policy
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
- url: https://support.telnyx.com/en/articles/10715016-10dlc-inaccurate-or-inconsistency-error
- url: https://support.telnyx.com/en/articles/10744086-10dlc-error-806
- url: https://support.telnyx.com/en/articles/4557103-telnyx-privacy-policy
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
- url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
updated_at: 2026-08-05T13:25:10Z
---

# 10DLC Campaign Registration and Compliance Guide

*Part 3 of 5 — see also: [Part 1](10dlc-campaign-registration-and-compliance-guide--part-1.md), [Part 2](10dlc-campaign-registration-and-compliance-guide--part-2.md), [Part 4](10dlc-campaign-registration-and-compliance-guide--part-4.md), [Part 5](10dlc-campaign-registration-and-compliance-guide--part-5.md)*

A consolidated reference for registering and maintaining 10DLC (10-Digit Long Code) A2P messaging campaigns on Telnyx, covering message flow, opt-in forms, keywords, privacy policy, sample messages, vetting, shared campaigns, and common carrier errors.

## Opt-In Form Requirements

A compliant digital opt-in form must include all required disclaimers, an explicit and optional SMS consent checkbox, and clear subscriber expectations.

![Example compliant opt-in form](_images/064b741afa8cc908.png)

Key requirements:

1. All required disclaimers are present:
   > "By providing your phone number, you agree to receive SMS [Use Case(s)] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. We will not share mobile information with third parties for promotional or marketing purposes."
2. The SMS consent checkbox is specific, explicit, and optional. It is not buried in terms and conditions, not combined with other consents (such as "I agree to the terms and conditions"), and not a mandatory field.
3. The subscriber knows what to expect.
4. The SMS opt-in checkbox is unchecked by default.
5. For Political or Charity use cases where donations will be solicited, add "Donations may be solicited" to the opt-in disclaimers.
6. For Marketing use cases, add language such as "You are opting into marketing texts" to the opt-in disclaimers.

## Keywords and Confirmation Messages

Every campaign must define keywords and confirmation messages for opt-in, opt-out, and help. Use the following template, replacing bracketed variables with your brand and campaign details.

- **Opt-in Keyword:** START (or similar keyword)
- **Opt-in confirmation message:** [Brand name]: Thanks for subscribing to [use case(s)]! Reply HELP for help. Message frequency may vary. Msg&data rates may apply. Consent is not a condition of purchase. Reply STOP to opt out.
- **Opt-out Keyword:** STOP (or similar keyword)
- **Opt-out confirmation message:** [Brand Name]: You are unsubscribed and will receive no further messages.
- **Help Keyword:** HELP (or similar keyword)
- **Help confirmation message:** [Brand name]: Please reach out to us at [website/email/phone number] for help.

Websites are acceptable in the help confirmation so long as they have clear contact information at the link provided.

## Sample Messages

Sample messages must correspond to the registered use case. If a campaign is registered under multiple use cases (mixed), a sample message for each use case should be provided. Each use case selected must have at least one representative sample message; a dedicated marketing use case or a mixed use case requires at least two sample messages.

- Provide links if the link attribute for the campaign is checked off.
- Provide up to five samples that characterize the different content you intend to send.
- Samples must be consistent with brand, campaign description, and website.
- Recommended to follow the 160-character limit to align with industry best practice.

> Example: Upcoming Appointment: March 5, 2024 2pm w/ Dr. Crentist at 1725 Slough Avenue in Scranton, PA. Call 18005551234 to reschedule if needed.

## Privacy Policy Requirements

The privacy policy must be for the brand being registered. Resellers cannot substitute their own privacy policy in place of the brand's, and a Google Privacy Policy will not be accepted in place of the brand's privacy policy.

Carriers look for compliant verbiage either in the privacy policy (linked from the opt-in form) or directly on the opt-in form. The bare minimum accepted by carriers is language to the effect of:

> Your mobile information will not be sold or shared with third parties for promotional or marketing purposes.

Carriers prefer more robust sharing verbiage, such as:

> All the above categories exclude text messaging originator opt-in data and consent; this information will not be shared with any third parties.
>
> We will not share your opt-in to an SMS campaign with any third party for purposes unrelated to providing you with the services of that campaign. We may share your Personal Data, including your SMS opt-in or consent status, with third parties that help us provide our messaging services, including but not limited to platform providers, phone companies, and any other vendors who assist us in the delivery of text messages.

The verbiage must cover any method of transfer. Stating only that mobile data will not be sold is insufficient; it must also cover sharing, including transfers without a sale (such as between affiliates or partner businesses), which is prohibited under 10DLC.

Any mention of third-party data sharing, renting, or selling is disallowed unless the disclosure above is included. If the privacy policy already provides for data sharing or selling to nonaffiliated third parties, it must clarify that such sharing or selling will not include a customer's SMS opt-in data or consent status. If the privacy policy does not currently mention data sharing, a similar clarification must be inserted.

## Terms and Conditions

Comprehensive terms and conditions may be presented in full beneath the call-to-action or accessed from a link in proximity to the CTA. Popups are not a method for displaying terms and conditions. Where feasible, message senders may combine multiple program components (for example, call-to-action and terms and conditions).

The following SMS program disclosures must be included within the terms and conditions:

- Program (brand) name.
- Message frequency disclosure (not required for single-message programs).
- Product description.
- Customer care contact information.
- Opt-out information (not required for single-message programs).
- "Message and data rates may apply" disclosure (not required for FTEU-rated programs).

The terms must include the types of messages consumers can expect to receive, texting cadence, message and data rate notices, any associated costs, privacy policy, opt-out instructions, and other terms of use.
