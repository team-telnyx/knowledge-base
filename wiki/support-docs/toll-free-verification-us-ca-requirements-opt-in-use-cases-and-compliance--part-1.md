---
title: 'Toll-Free Verification (US/CA): Requirements, Opt-In, Use Cases, and Compliance'
summary: 'End-to-end guide to getting US/CA toll-free numbers verified for messaging
  with Telnyx: how to submit, mandatory 2026 business identity requirements, opt-in
  and privacy/T&Cs standards (now mirroring 10DLC/short code), use case selection,
  Canada-specific rules, prohibited content, statuses, timelines, and how to resolve
  common rejection reasons.'
sources:
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/10245573-us-short-code-ordering-process
- url: https://support.telnyx.com/en/articles/10245615-short-code-brand-and-content-provider-registration-process
- url: https://support.telnyx.com/en/articles/11385511-short-code-compliance-quick-reference-guide
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
- url: https://support.telnyx.com/en/articles/1130703-can-i-call-toll-free-with-my-telnyx-number
updated_at: 2026-05-14T11:23:21Z
---

# Toll-Free Verification (US/CA): Requirements, Opt-In, Use Cases, and Compliance

*Part 1 of 2 — see also: [Part 2](toll-free-verification-us-ca-requirements-opt-in-use-cases-and-compliance--part-2.md)*

End-to-end guide to getting US/CA toll-free numbers verified for messaging with Telnyx: how to submit, mandatory 2026 business identity requirements, opt-in and privacy/T&Cs standards (now mirroring 10DLC/short code), use case selection, Canada-specific rules, prohibited content, statuses, timelines, and how to resolve common rejection reasons.

## What Toll-Free Verification Is and Why It’s Required
Before you can send outbound SMS/MMS from a US/CA toll-free number, the number must be verified. Verification ties your traffic to a clearly identified business, validates compliant opt-in practices, and aligns toll-free standards with 10DLC and short code. Verified numbers enjoy better deliverability and fewer blocks.

- Typical review time: about 5 business days (can vary with volume).
- Re-submitting a new verification for an already-approved number overwrites the prior approval and the number becomes unverified until re-approved.

See also: [Toll-Free Messaging](toll-free-messaging.md).

## Submission Paths, Timeline, and Statuses
- Submit in the Telnyx Portal: Real Time Communications > Messaging > Compliance > Toll-Free Verification or via the direct link: https://portal.telnyx.com/#/programmable-messaging/toll-free-messaging
- Submit via API: https://developers.telnyx.com/api/messaging/toll-free-verification/submit-verification-request

Statuses after submission:
- Waiting for Telnyx: Internal review for eligibility and compliance.
- Waiting for Customer: Update requested; decline reason explains required changes.
- Waiting for Vendor: Approved by Telnyx; pending carrier approvals.
- Rejected: Declined by Telnyx or carriers; reason provided.
- Verified: Fully approved; you may begin sending.

## Mandatory Business Identity Requirements (2026 update)
Effective February 17, 2026, carriers require government-issued business identifiers. Your submission must include:
- Business Registration Number (BRN): For US, the 9‑digit EIN; for Canada, the BN.
- Business Registration Type: One of EIN, CBN, CRN, NEQ, PROVINCIAL_NUMBER, VAT, ACN, ABN, BRN, SIREN, SIRET, NZBN, UST-IDNR, CIF, NIF, CNPJ, UID.
- Legal Entity/Organization Type: Private Company, Publicly Traded Company, Charity/Non-Profit, Government, or Sole Proprietor.
- Issuing Country: Country of legal registration.
- Privacy Policy link: Must explicitly state SMS opt‑in data will not be sold/shared with third parties for marketing.
- Terms & Conditions link: Service agreement applicable to messaging program.
- Opt‑In Keyword: START, YES, BEGIN, or a brand keyword for resubscription after STOP.

Notes:
- Exact legal name must match IRS/registration records. Use DBA to reflect the public-facing brand if different.
- Business contact email should match the website’s domain and be visible on the site.
- Sole Proprietors: Select Sole Proprietor and leave BRN/Type/Country blank. If rejected for “registration number missing/invalid,” Telnyx can escalate for manual verification; contact tfverification@telnyx.com.

## Filling Out the Verification Form: Field-by-Field
1) Business Identification
- Business name, corporate website, and email domain should match; explain any differences in “Additional Information.”
- Website must clearly show brand name, contact info, product/services, About, Contact Us, Privacy Policy, and Terms.
- Use a business email on the same domain as the site (avoid freemail where possible).
- Provide a valid business address, a contact number, and a human contact’s first/last name.

2) Messaging Details
- Expected Message Volume: Approximate via provided options.
- Use Case: Select the most accurate category; if more than one, choose Mixed and describe each in detail. Keep all mentions (use case field, description, opt-in form) consistent.
- Description/Summary: Explain who you will message, why, what types of messages, and compliance controls.
- Message Content: Provide realistic samples for every selected use case; include brand identification and opt‑out language (e.g., “Reply STOP to opt out”).

3) Opt-In Workflow & Evidence
- Provide a clear, verifiable description and an Opt‑In Image URL (link to the live page or a publicly accessible screenshot/diagram). See templates in [Toll Free Opt in Workflow Description](toll-free-opt-in-workflow-description.md).
- For digital, include the URL and how users reach the form. For sign-in gated flows, include hosted screenshots.
- For paper or verbal consent, link to hosted scans or scripts and explain where/how users encounter them. For inbound-message flows, specify the number users text and where it’s published.

4) ISV/Reseller Information
- If your Telnyx account domain differs from the end brand’s domain, complete the Reseller field or the request will be set to Waiting for Customer.

5) Additional Supporting Details
- If submitting more than 5 toll-free numbers, provide a detailed, specific justification (e.g., per-location or per-team routing).
- Use a public document link if you need more space, and summarize its contents in the form.

## Opt-In Requirements and Disclosures (now mirroring 10DLC/short code)
Your opt-in must be explicit, brand-specific, and documented. Disclosures must include:
- Clear description of what users are subscribing to.
- “Reply STOP to opt out” and “Reply HELP for help.”
- “Message and data rates may apply.”
- Message frequency (e.g., “Message frequency may vary”).
- Links to Terms & Conditions and Privacy Policy.
- Separate, unchecked checkboxes:
  - One for transactional messaging (if applicable).
  - A distinct checkbox for marketing messaging, when applicable.
  - SMS consent must be separate from email consent.
- Privacy policy must state that messaging data will not be shared or sold to third parties for marketing purposes.

If marketing is selected, marketing SMS must have its own checkbox. For inbound-message (conversational) opt-in, include disclosures in the first response message at minimum.

## Documenting Your Opt-In: Workflow Templates
Choose one and describe it precisely in your request. Host screenshots publicly if needed.
- Digital: “Subscribers opt in digitally; they start at [URL] and navigate to [URL] where the opt-in form is located.” If behind login, include a hosted screenshot link.
- Verbal: “Subscribers call/visit [number/address] published at [location URL]. If they request SMS, we read a script. See Opt-In Image URL for the full script.”
- Paper: “Subscribers opt in via paper form. See screenshot at [hosted URL].”
- Inbound Message: “Subscribers opt in by texting us first. They find our number at [location URL].”

See templates: [Toll Free Opt in Workflow Description](toll-free-opt-in-workflow-description.md).

## Selecting and Describing Your Use Case
Pick the best-fit use case. If you send both marketing and non-marketing content or have multiple categories, select Mixed and document each component consistently across the form and opt-in material.
- Common use cases: 2FA, App Notifications, Booking Confirmations, Conversational/Alerts, Courier Services & Deliveries, Fundraising, General Marketing, Mixed, Order Notifications, Political, System Alerts.
- Additional options include Appointments, Billing, Events & Planning, Fraud Alerts, HR/Staffing, Real Estate Services, Surveys, Webinar/Workshop Reminders, and more.

Detailed guidance: [How to Pick a Toll Free Use Case](how-to-pick-a-toll-free-use-case.md).

## Multi-Number Requests and ISV/Reseller Scenarios
- More than 5 numbers: Provide a precise rationale (e.g., one number per storefront; list each location and assigned number and what it’s used for).
- ISVs/Resellers: If your portal account is not on the same domain as the end business, populate the Reseller field to avoid delays.
