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

*Part 5 of 5 — see also: [Part 1](10dlc-registration-and-compliance--part-1.md), [Part 2](10dlc-registration-and-compliance--part-2.md), [Part 3](10dlc-registration-and-compliance--part-3.md), [Part 4](10dlc-registration-and-compliance--part-4.md)*

A consolidated reference for registering and operating 10DLC messaging on Telnyx, covering the end-to-end brand and campaign workflow, mock testing, CTA and message flow requirements, opt-in form design, privacy policy language, sample messages, age gates, political campaigns, common errors, and associated fees.

## Campaign Approval Best Practices

Effective January 26, 2023, all new Telnyx US 10DLC campaign registrations (Standard, Low Volume Standard, and Sole Proprietor 2.0) are subject to a manual vetting process and a $15 campaign verification fee at the time of external vetting. If a campaign is denied by external vetting, additional charges may occur with re-submission.

To maximize the chance of approval:

- **Avoid forbidden use cases** — do not register campaigns involving prohibited content such as cannabis or hate speech.
- **Keep brand, website, and sample messages consistent** — the brand and website must match what is included in sample messages.
- **Keep sample messages and use cases consistent** — registering a political campaign with sample messages like "Your one-time password is: 123456" will be rejected.
- **Keep email domain and company name consistent** — registering a brand as Telnyx with a gmail-domain email address will be rejected. This applies to large corporations that should have dedicated email domains.
- **Submit only real, working websites** — if the opt-in process is via the website, the URL must work.
- **Send messages according to the registered brand** — registering a technology brand and sending messages for a construction-company customer will be rejected.
- **Collect consumer opt-in appropriately** — send messages only to people who really want to receive them. See the [CTIA Messaging Principles and Best Practices](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf).
- **Make opt-in language available on the website** — if the message flow indicates opt-in happens on the company website, the website must include language such as *"By providing your phone number, you agree to receive text messages from Telnyx. Message & data rates may apply. Message frequency varies."*
- **Include opt-out language in at least one sample message** — for example, *"Please reply STOP to opt out"*.
- **Use express opt-in** — every place that requires a phone number must have opt-in language and a checkbox (contact pages, donation pages, etc.). Opt-in language must include consent and opt-out instructions and links to the Privacy Policy and Terms and Conditions.
- **Privacy Policy must not allow sharing/selling of end-user information to third parties.**
- **Embedded links/numbers** — if the campaign was created with the Embedded Phone Number or Embedded Link attributes, the samples must contain the phone number or link.

If a campaign is rejected, someone from the Telnyx team will reach out to help fix the registration or re-submit a new campaign.

## Common Errors and Troubleshooting

### 10DLC Error (806)

> Unable to verify, needs compliant and accurate CTA information. Update with specific path for mobile opt-in, HELP instructions, STOP instructions, message frequency disclosure, "message and data rates may apply" disclosure and link to the message program privacy policy, or language referring to the privacy policy. (806)

This error relates to the Message Flow field. In plain terms, the message flow either did not sufficiently document or did not contain a compliant opt-in process. Update the message flow to follow one of the formats in [Guide to 10DLC Message Flow Field](guide-to-10dlc-message-flow-field.md) and update the opt-in form to include all necessary disclaimers per [10DLC Opt in Form](10dlc-opt-in-form.md).

### TCR Creation Failed / Invalid Date

Indicates TCR rejected the campaign for a technical reason (missed character requirement, wrong number of sample messages). Different from a carrier rejection. Email [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com) to identify the failure reason; the campaign will need to be re-created.

### Unverified Brand

The most likely cause is an error in the submitted information. Review all brand fields for correctness. If the EIN is wrong, contact the Telnyx team for assistance. See [10DLC Unverified Brand](10dlc-unverified-brand.md).

## Fees Summary

- **Brand registration:** one-time, non-refundable $4 fee (passed through from TCR).
- **Campaign vetting:** $15 per submission or resubmission review fee (passed through from carriers).
- **Auth+ (Publicly Traded brands):** $15 per attempt as of August 1, 2025; check the Telnyx portal for current pricing.
- **T-Mobile Number Pool:** additional charges apply to exceed the 49-number-per-campaign limit. See [10DLC Fees and Charges](10dlc-fees-and-charges.md).
- **Mock brands and campaigns:** no registration or monthly recurring fees.

## Key Contacts

- **10DLC questions:** [10dlcquestions@telnyx.com](mailto:10dlcquestions@telnyx.com)
- **Non-compliance or portal issues:** [support@telnyx.com](mailto:support@telnyx.com)
- **Auth+ verification email:** [noreply@auth.campaignregistry.com](mailto:noreply@auth.campaignregistry.com)
