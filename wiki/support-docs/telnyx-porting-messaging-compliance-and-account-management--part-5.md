---
title: Telnyx Porting, Messaging Compliance, and Account Management
summary: This page consolidates Telnyx guidance on porting numbers from Skype and
  VoIP resellers, resolving Canadian reseller porting errors, cancelling accounts,
  configuring Skype for Business SIP trunks, toll-free messaging verification and
  opt-in workflows, SMS opt-out keywords, WhatsApp conversation windows, and handling
  toll-free carrier rejections.
sources:
- url: https://support.telnyx.com/en/articles/10715399-porting-away-from-skype
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
- url: https://support.telnyx.com/en/articles/1130689-how-do-i-cancel-my-account
- url: https://support.telnyx.com/en/articles/1130698-skype-set-up-skype-for-biz-sip-trunk
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
- url: https://support.telnyx.com/en/articles/13986482-whatsapp-24-hour-conversation-window
- url: https://support.telnyx.com/en/articles/14708130-porting-numbers-away-from-resellers-aircall-intercom-ringcentral-vonage-etc
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
updated_at: 2026-08-05T13:26:16Z
---

# Telnyx Porting, Messaging Compliance, and Account Management

*Part 5 of 5 — see also: [Part 1](telnyx-porting-messaging-compliance-and-account-management--part-1.md), [Part 2](telnyx-porting-messaging-compliance-and-account-management--part-2.md), [Part 3](telnyx-porting-messaging-compliance-and-account-management--part-3.md), [Part 4](telnyx-porting-messaging-compliance-and-account-management--part-4.md)*

This page consolidates Telnyx guidance on porting numbers from Skype and VoIP resellers, resolving Canadian reseller porting errors, cancelling accounts, configuring Skype for Business SIP trunks, toll-free messaging verification and opt-in workflows, SMS opt-out keywords, WhatsApp conversation windows, and handling toll-free carrier rejections.

## Toll-Free Carrier Rejections

Toll-free submissions may be rejected by carriers for various reasons. Below are common rejection messages and their solutions.

### Consent and Opt-In Issues

- **Agreeing to receive messages must be optional** — The SMS opt-in is forced by submitting a form with a phone number. Solution: Make the phone number field optional, or add a checkbox to the SMS disclosures. Resubmit once updated.
- **Consent for messaging cannot be part of other agreements** — The SMS opt-in has been grouped with a product/service or terms and conditions. Solution: Provide a separate opt-in for SMS consent only, or remove terms and conditions from the opt-in language. The SMS opt-in must be optional. Resubmit once edited.
- **Marketing messages require express written consent** — Marketing and promotional SMS cannot be mentioned with any other use case in the same opt-in disclosure. Solution: Add a separate opt-in for marketing and promotional SMS. Opt-ins stating "receive promotional or marketing and informational SMS" will be rejected — the word "informational" must be defined. Resubmit after correction.
- **Opt-in — consent for messaging is a requirement for service** — The SMS is not optional and is mandatory to use or purchase service. Solution: Make the SMS opt-in optional by adding a checkbox. Resubmit once updated.
- **Opt-in does not match the use case** — The opt-in disclosure mentions a use case that does not align with the use case selected in the submission. Solution: Update the opt-in to match the use case, or edit the use case in the submission to match the opt-in. Resubmit.
- **Opt-in example must be complete, branded, and legible** — The opt-in image provided was not branded, missing details, or blurry. Solution: Provide a new screenshot for the opt-in link and resubmit.
- **Opt-ins must clearly reflect the end business** — The opt-in is branded with something other than what was submitted for verification, or contains a placeholder business name. Solution: Update the opt-in and resubmit.
- **Opt-in URL not accessible** — The opt-in link provided was inaccessible or returned a 404. Solution: Update the link and verify it works. Resubmit. If this is an error, email tfverification@telnyx.com for investigation.

### Business Information Issues

- **Business email address must use an official domain** — The business email domain does not match the business website domain or the contact email on the website. Solution: Update the email address in the submission and resubmit.
- **Business information could not be verified** — Contact, email, address, or URL is invalid. The business details do not match what is present on the website. Solution: Ensure business details on the website match the submission details; if absent, add them to the website. Resubmit once completed.
- **Business registration number is missing or invalid** — The wrong business name was entered, or the company is less than 6 months old and the IRS only does batch updates quarterly. Solution: Email tfverification@telnyx.com and provide the business registration document. Do not resubmit.
- **Contact name must belong to a business representative** — The first and last name entered is unintelligible or does not make sense (e.g., First Name: FRANK, Last Name: FRANK). Solution: Update the contact name and resubmit.
- **End business details must be accurate and complete** — The brand name or DBA within the opt-in does not match the business details in the submission. Solution: Ensure the brand name or DBA is correctly entered in the submission, or update the brand name in the opt-in disclosure language. Resubmit.
- **Entity misclassification (legal entity type mismatch)** — The business entity selected does not match the official record. This often occurs when sole proprietor is selected but the business is actually a private entity with a BRN. Solution: Update business details and resubmit.
- **Social platform must be established and active** — The social media link (Facebook, Instagram, or LinkedIn) is missing business contact details. Solution: Update the social media page with contact details and resubmit.
- **Website is password protected or requires login** — The website is behind a login wall. Solution: Make the website public. Resubmit.
- **Website must be established and active** — The website is missing one or more required elements: Home Page, Contact Information (address/email/etc), Products/Services offered, About page, Contact Us page, Privacy and Terms page. Solution: Update the website and resubmit.
- **Invalid or inaccessible website URL** — The website was inaccessible with the provided URL. Solution: Ensure the website is live and the domain is public. If this is an error, email tfverification@telnyx.com for investigation.

### Content and Use Case Issues

- **Disallowed content — cannabis, CBD, or other illegal substances** — The business website promotes, markets, or sells cannabis. Solution: Remove all cannabis-related content from the website. If the use case is 2FA, Employee Alerts, or HR/Staffing, no action may be needed (handled case by case). Resubmit.
- **Disallowed content — third-party lead generation or multi-level marketing** — Any reference to lead generation using third-party affiliates is prohibited. Solution: Remove all lead generation language from the website. Lead alerts and lead management are allowed. Resubmit.
- **SHAFT violation — alcohol message content without a 21+ robust age gate** — The website or checkout page lacks age verification to block minors from viewing alcohol content. Solution: Add an age gate to the website and resubmit.

### Volume and Risk Issues

- **Additional information requested — justification for more than 5 numbers per business** — A justification is needed when submitting 6 or more numbers in one submission, or 6 separate submissions for the same business. Solution: Provide a valid explanation in the additional use case details field for why multiple numbers are needed. Resubmit.
- **High risk — known spam campaign** — The business has been flagged by the carrier prior to joining Telnyx. Solution: This is usually a hard block. A reimmediation can be requested, but conversion rates are less than 1%. Email tfverification@telnyx.com to request an appeal at the carrier level.
- **High risk — submission flagged for high-risk domain issues** — The domain details are similar to a prior flagged business, or the domain age is very new. Solution: Email tfverification@telnyx.com to appeal. Do not resubmit.

### Submission Process Issues

- **Submission editing timed out** — The submission was not resubmitted within 7 days of rejection and the carrier's ticket ID was closed. Solution: Email tfverification@telnyx.com and request details on the rejection. Do not resubmit until feedback on the initial rejection reason is received.

For any questions, email tfverification@telnyx.com.
