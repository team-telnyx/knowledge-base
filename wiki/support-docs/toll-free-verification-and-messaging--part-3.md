---
title: Toll-Free Verification and Messaging
summary: Toll-Free numbers on Telnyx require verification before sending outbound
  messages. This page covers the full verification process, form requirements, use
  case selection, opt-in workflows, prohibited content, carrier rejections, and related
  topics such as opt-out handling, webhook notifications, and number porting.
sources:
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
  content_hash: b686f9918f8f56de652bf15acf4cbf8e746da09154937eff1d6faa660f34f0aa
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
  content_hash: 0135186e7b4fd205be673cc95b9ad6c8e30e89e905c085cd4157bf7efe3aabc3
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
  content_hash: 206304a57044394aac7a609baf4be472c03ceee1447f9d2acf7f69b396d0235a
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
  content_hash: 5ee6a03aefda713deafa0ae83b16bf07fd2dec44809ec471d7c40c5ac40f1e26
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
  content_hash: 43bdb2eabd3bc3d48a149584065c6066b73726c25ecc0ae49b63f997ae66da3e
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
  content_hash: 2d5cf51c514e71e157dba2fbcf416914b8ce9b9aef54e73d86ac21085db352eb
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
  content_hash: da947cbf3c93bc63dd00aca6f9271eb7b8aade9000cd5752e28fb21327517f30
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
  content_hash: ffddea700ce5dce3372ec56ece6a70c99416d1eeff831cd3365835e1171b774f
- url: https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status
  content_hash: 0359479f1a54f703908e8dbe4cd931cde68a43a5469a9a88dd61a6f072e384c3
- url: https://support.telnyx.com/en/articles/8673249-us-ca-toll-free-number-porting
  content_hash: 8097a44aff492ea1e8cc159bb25603f72d88dfb326bec5d45ee750403e85a78d
updated_at: 2026-06-11T11:12:33Z
---

# Toll-Free Verification and Messaging

*Part 3 of 4 — see also: [Part 1](toll-free-verification-and-messaging--part-1.md), [Part 2](toll-free-verification-and-messaging--part-2.md), [Part 4](toll-free-verification-and-messaging--part-4.md)*

Toll-Free numbers on Telnyx require verification before sending outbound messages. This page covers the full verification process, form requirements, use case selection, opt-in workflows, prohibited content, carrier rejections, and related topics such as opt-out handling, webhook notifications, and number porting.

## Carrier Rejections and Error Codes

The table below lists common carrier rejection reasons and eligibility for resubmission:

| Reason | Eligibility for Resubmission |
|---|---|
| No Reason Provided | Not Eligible |
| Content Violation — SHAFT (Sex, Hate, Alcohol, Firearms, Tobacco/Vape, Marijuana/CBD) | Not Eligible |
| Campaign Violation — Age Gate Not Present / Not Acceptable | Eligible with robust age gate implemented |
| Known Spam Campaign | Not Eligible |
| Disallowed Content — Loan Marketing, 3rd Party Debt Collection, Gambling, Sweepstakes, Stock Alerts, Cryptocurrency, Risk Investment, Debt Reduction, Credit Repair, 3rd Party Lead Generation, Federally Illegal Substances | Not Eligible |
| Known Phishing Campaign | Not Eligible |
| High Risk — Fraud | Not Eligible |
| High Risk — Deceptive Marketing | Not Eligible |
| High Risk — Public URL Shortener | Eligible if changed to a branded URL domain |
| High Risk — Non-secured URL | Eligible if corrected to HTTPS |
| Invalid Information — Can't Verify Business Information | Eligible if business details are corrected |
| Invalid Information — Can't Validate URL (Website inaccessible) | Eligible if website access is restored |
| Invalid Information — ISV Contact Provided Instead of End User | Eligible if corrected |
| Opt-in — Not sufficient for campaign type (Express Consent Required) | Eligible if express consent is provided |
| Opt-in — Consent for messaging is a requirement for service | Eligible if consent is made optional (add a checkbox) |
| Opt-in — No opt-in provided | Eligible if opt-in is provided |
| Opt-in — Shared with 3rd Parties | Eligible if language is updated to remove 3rd-party sharing |
| Campaign Violation — Single Number Used for Multiple Businesses | Eligible if each business is assigned a unique toll-free number |
| Opt-in — List Opt-in Relies on Organizational/Government Exemption | Not Eligible |
| Additional Information Requested — Justification for more than 5 numbers per business | Eligible if justification is provided |
| Additional Information Requested — Opt-in Information Not Provided | Eligible if updated |
| Additional Information Requested — Business Information Not Valid | Eligible if corrected |
| Submission Editing Timed Out | You have 7 days from carrier submission to resubmit without changes. Portal users can make a small edit and save to create a new VR ID. API users should contact support. |
| Number Not Provisioned to Your Organization | Not Eligible |

**Additional carrier rejection reasons with solutions:**

- **Agreeing to receive messages must be optional:** The phone number field must be optional, or a checkbox must be added to SMS disclosures.
- **Business email address must use an official domain:** Update the email to match the business website domain.
- **Business information could not be verified:** Ensure business details on the website match the submission; add missing details to the website.
- **Business registration number is missing or invalid:** Email [tfverification@telnyx.com](mailto:tfverification@telnyx.com) with the business registration document. Do not resubmit.
- **Consent for messaging cannot be part of other agreements:** Provide a separate opt-in for SMS consent only; remove terms and conditions from opt-in language.
- **Contact name must belong to a business representative:** Update the contact name to a real person's first and last name.
- **Disallowed content — cannabis/CBD:** Remove all cannabis-related content from the website. (Exception: If the use case is 2FA, Employee Alerts, or HR/Staffing, no action may be needed — handled case by case.)
- **Disallowed content — third-party lead generation/MLM:** Remove all lead generation language from the business website. Lead alerts and lead management are allowed.
- **End business details must be accurate and complete:** Ensure the brand/DBA in the opt-in matches the toll-free submission.
- **Entity misclassification (legal entity type mismatch):** Update business entity type to match the official record.
- **High risk — known spam campaign:** This is usually a hard block. Email [tfverification@telnyx.com](mailto:tfverification@telnyx.com) to request an appeal at the carrier level (less than 1% conversion rate).
- **High risk — submission flagged for high-risk domain issues:** Email [tfverification@telnyx.com](mailto:tfverification@telnyx.com) to appeal. Do not resubmit.
- **Invalid or inaccessible website URL:** Ensure the website is live and the domain is public. If this is an error, email [tfverification@telnyx.com](mailto:tfverification@telnyx.com).
- **Marketing messages require express written consent:** Marketing and promotional SMS must have a separate opt-in from transactional use cases. Opt-ins that combine "promotional or marketing and informational SMS" will be rejected — the word "informational" must be defined as a specific transactional use case with a separate opt-in.
- **Opt-in does not match the use case:** Update the opt-in or use case to align with each other.
- **Opt-in example must be complete, branded, and legible:** Provide a new, clear, branded screenshot.
- **Opt-ins must clearly reflect the end business:** Update opt-in branding to match the submitted business name.
- **SHAFT violation — alcohol message content without a 21+ robust age gate:** Add a birthdate-entry age gate to the website.
- **Social platform must be established and active:** Update social media page with business contact details.
- **Website is password protected or requires login:** Make the website public.
- **Website must be established and active:** Add missing elements — home page, contact information, products/services, about page, contact us page, privacy and terms page.

For any questions about carrier rejections, email [tfverification@telnyx.com](mailto:tfverification@telnyx.com).

## Sole Proprietor Submissions

As of early 2026, carriers strongly prefer — and often mandate — an EIN for all toll-free verifications. Obtaining an EIN from the IRS is considered the best practice for instant approval, even if you have no employees.

**When submitting as a Sole Proprietor:**

- **Business Registration Number:** Leave blank
- **Business Registration Type:** Leave blank
- **Issuing Country:** Leave blank
- **Legal Entity or Organization Type:** Select Sole Proprietor

Submissions without an EIN (using the SOLE_PROPRIETOR classification) can be subject to **manual verification**, which may involve uploading a government-issued ID and a "live selfie," adding time to the approval process.

If a sole proprietor submission is rejected for a missing or invalid business registration number, email [tfverification@telnyx.com](mailto:tfverification@telnyx.com) with any business registration forms so Telnyx can file an appeal for manual verification with the carrier aggregators.

## Opt-Out Keywords

Toll-free numbers handle opt-out and opt-in keywords differently from other number types:

- **Opt-out keyword:** `STOP` (the only recognized opt-out keyword)
- **Opt-in keywords:** `START` and `UNSTOP`

When a recipient opts out:

> NETWORK MSG: You replied with the word "stop" which blocks all texts sent from this number. Text back "unstop" to receive messages again.

When a recipient opts back in:

> NETWORK MSG: You have replied "unstop" and will begin receiving messages again from this number.

On opt-out, Telnyx blocks further communications from the toll-free number to the opted-out number. Senders have up to 24 hours to remove the recipient from their list. Because opt-out logic for toll-free numbers is handled outside Telnyx, custom block rules and auto responses cannot be applied to toll-free numbers. It is recommended to separate toll-free numbers into their own messaging profile if custom block rules are configured.
