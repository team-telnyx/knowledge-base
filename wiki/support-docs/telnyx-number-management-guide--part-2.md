---
title: Telnyx Number Management Guide
summary: A consolidated reference for managing phone numbers on Telnyx, covering ordering
  restrictions, toll-free verification, verified (non-Telnyx) numbers, IVR and DTMF
  verification flows, use-case selection, and the sunset Google Verified Calls product.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
- url: https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/13854980-beta-how-to-verify-phone-numbers-using-dtmf-press-1-to-verify
- url: https://support.telnyx.com/en/articles/5941652-google-verified-calls-faq
- url: https://support.telnyx.com/en/articles/6790265-verified-numbers-faq
- url: https://support.telnyx.com/en/articles/6988813-verified-numbers
- url: https://support.telnyx.com/en/collections/3968222-telnyx-number-management-guide
updated_at: 2026-08-05T13:26:15Z
---

# Telnyx Number Management Guide

*Part 2 of 5 — see also: [Part 1](telnyx-number-management-guide--part-1.md), [Part 3](telnyx-number-management-guide--part-3.md), [Part 4](telnyx-number-management-guide--part-4.md), [Part 5](telnyx-number-management-guide--part-5.md)*

A consolidated reference for managing phone numbers on Telnyx, covering ordering restrictions, toll-free verification, verified (non-Telnyx) numbers, IVR and DTMF verification flows, use-case selection, and the sunset Google Verified Calls product.

## Toll-Free Verification

Before sending your first outbound message from a toll-free phone number, you must verify the number. Toll-Free Verification requires specific data to identify the end business and confirm proper measures are in place for compliant traffic. Incomplete submissions may be rejected.

Approval timelines are typically 5 business days or less, depending on request volume.

### Submitting a Verification Request

You can submit a request via:

- **Telnyx Portal:** portal.telnyx.com → Real Time Communications → Messaging → Compliance → [Toll Free Verification](https://portal.telnyx.com/#/programmable-messaging/toll-free-messaging) → Submit Verification Request
- **Telnyx API:** [Submit Verification Request](https://developers.telnyx.com/api/messaging/toll-free-verification/submit-verification-request)

### Verification Statuses

- **Waiting for Telnyx** — Telnyx reviews submissions for platform eligibility and compliance.
- **Waiting for Customer** — Telnyx has changes it would like you to make; the decline reason describes the required steps.
- **Waiting for Vendor** — Approved by Telnyx and pending carrier approval.
- **Rejected** — Rejected by Telnyx or the carriers; the decline reason explains why.
- **Verified** — Approved by both Telnyx and the carriers; you may begin sending outbound text messages.

Submitting a new Verification Request for an already approved toll-free number overwrites the existing approval and leaves the number unverified until the new request is approved.

### Verification Form Fields

**1. Business Identification**

- **Business Name** — Should match the website domain and email domain, or differences should be explained in the additional information field.
- **Corporate Website** — Include a business website or social media page showing the business name, contact information, products/services, an About page, a Contact Us page, and a Privacy and Terms page.
- **Email Address** — The website domain should match the email domain. Freemail contacts (e.g., Gmail) can be cause for decline.
- **Business Address** — A valid business address.
- **Contact Number** — A contact number for the business using the toll-free number (not the toll-free number being verified).
- **Business Contact** — Must be a person's first and last name, not a business or department name.

**2. Messaging Details**

- **Expected Message Volume** — Approximate, based on available dropdown options.
- **Use Case** — The specific purpose for messaging. Examples include conversational, marketing, transactional notifications, or fraud alerts. For mixed use cases, describe each in the Use Case description field. Every SMS use case mentioned on the opt-in form must appear here. See [How to Pick a Toll Free Use Case](how-to-pick-a-toll-free-use-case.md) for guidance.
- **Description of the Use Case / Summary** — Explains the types of messages, intended audience, and relevant compliance measures.
- **Message Content** — Provide samples for each use case selected and described in the summary.

**3. Opt-in Workflow Description / Opt-in Image URL**

Provide a link, image link, or scanned copy of the opt-in. The opt-in process must be clearly documented. There are four opt-in methods:

1. **Digital** — Include the URL or screenshot of the branded opt-in form and how subscribers reach it.
2. **Paper** — Include a link to the uploaded branded file and how subscribers receive it.
3. **Verbal** — Include the script users hear, how they receive it, and where (e.g., phone number to call, in-person address). Include all standard disclaimers.
4. **Inbound Message** — Provide the phone number they text into and how they learn it.

If you do not have a link for the opt-in image URL field (e.g., verbal consent), provide a link to a publicly accessible Google Doc or Dropbox file that diagrams the opt-in process.

Subscribers must receive these disclaimers before the first message (except for inbound text opt-ins, which may include them in the first message):

> You are subscribing to [brand name] for [use case (transactional or marketing)]. Reply STOP to opt out. Reply HELP for help. Standard message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlinked].

For marketing use cases, the marketing SMS opt-in must have its own compliant checkbox separate from other use cases. Example opt-in form structure:

- **[Checkbox 1]** By checking this box and submitting this form, you consent to receive transactional text messages for [use case(s)] from (Company Name). Reply STOP to opt out. Reply HELP for help. Standard message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlinked].
- **[Checkbox 2]** By checking this box and submitting this form, you consent to receive text messages for marketing from (Company Name). Reply STOP to opt out. Reply HELP for help. Message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlinked].

Notes:

- Privacy policy should include language such as "We will not share or sell your mobile information with third parties for promotional or marketing purposes."
- Checkboxes must be optional and cannot be pre-checked.
- The opt-in form should be branded with the same brand being registered.
- The business name should appear on the opt-in form within the message content.
- The SMS opt-in checkbox should be unchecked by default.
- SMS consent should be separate from other communication consents (e.g., email).
- SMS opt-in and privacy policy acceptance must have separate checkboxes.

**4. ISV/Reseller Information**

If the Telnyx account username domain does not match the business website and email domain, the request will be set to Waiting For Customer until the Reseller field is accurately filled in. If the Telnyx account is for the same domain as the business being registered, leave the Reseller field blank.

**5. Additional Supporting Details**

If submitting more than 5 toll-free numbers in a single Verification Request, include a detailed explanation for why multiple numbers are needed. Be specific — for example, if multiple numbers are needed for multiple store locations, explain each location and the number assigned to it.

If you run out of characters, use a publicly accessible Google Doc, paste the link into the VR, and describe the content in the VR as well.

### Age Gating

The opt-in form or website needs an age gate whenever marketing something not legal to consume under a certain age in any of the 50 states (e.g., alcohol). The age gate should be a birthdate entry that does not allow the user to proceed if the date is less than the required age — not a simple YES/NO gate. Restaurants that offer alcohol but will not promote it via SMS do not need an age gate, but must state in the VR that no alcohol will be promoted via SMS.

### Political Use Cases

- Indicate whether donations will be solicited in the use case summary.
- The opt-in form needs a separate checkbox from transactional or marketing consent for political consent in mixed use cases.
- Privacy policy must explicitly state that "No mobile information will be sold or shared with third parties for promotional or marketing purposes."

### Charity / Fundraising

- Select the Fundraising use case unless you have multiple use cases (in which case select Mixed).
- The opt-in form needs a fundraising or charity checkbox separate from other consents, and the checkbox disclaimers should mention that donations will be solicited.
- The use case summary should mention that donations will be solicited.

### Prohibited Content

This is not a comprehensive list:

- Loan soliciting/promotion
- CBD-related content
- Gambling

### Canadian Toll-Free Numbers

Canadian toll-free numbers must complete all of the above plus collect double opt-in: after the initial opt-in, a confirmation message must be sent and the subscriber must reply affirmatively to subscribe.

### Toll-Free Error Codes

| Reason | Eligibility for Resubmission |
| --- | --- |
| No Reason Provided | Not Eligible |
| Content Violation - SHAFT (Sex, Hate, Alcohol, Firearms, Tobacco/Vape, Marijuana/CBD) | Not Eligible |
| Campaign Violation - Age Gate Not Present / Not Acceptable | Eligible with Robust Age Gate Implemented |
| Known Spam Campaign | Not Eligible |
| Disallowed Content - Loan Marketing, 3rd Party Debt Collection, Gambling, Sweepstakes, Stock Alerts, Cryptocurrency, Risk Investment, Debt Reduction, Credit Repair, 3rd Party Lead Generation, Federally Illegal Substances | Not Eligible |
| Known Phishing Campaign | Not Eligible |
| High Risk - Fraud | Not Eligible |
| High Risk - Deceptive Marketing | Not Eligible |
| High Risk - Public URL Shortener | Eligible if changed to a branded URL domain |
| High Risk - Non-secured URL | Eligible if corrected to HTTPS |
| Invalid Information - Can't Verify Business Information | Eligible if business details are corrected |
| Invalid Information - Can't Validate URL (Website inaccessible) | Eligible if website access is restored |
| Invalid Information - ISV Contact Provided Instead of End User | Eligible if corrected |
| Opt-in - Not sufficient for campaign type (Express Consent Required) | Eligible if express consent is provided |
| Opt-in - Consent for messaging is a requirement for service | Eligible if consent is documented |
| Opt-in - No opt-in provided | Eligible if opt-in is provided |
| Opt-in - Shared with 3rd Parties | Eligible if language is updated to remove 3rd-party sharing |
| Campaign Violation - Single Number Used for Multiple Businesses | Eligible if each business is assigned a unique toll-free number |
| Opt-in - List Opt-in Relies on Organizational/Government Exemption | Not Eligible |
| Additional Information Requested - Justification for more than 5 numbers per business | Eligible if justification is provided |
| Additional Information Requested - Opt-in Information Not Provided | Eligible if updated |
| Additional Information Requested - Business Information Not Valid | Eligible if corrected |
| Submission Editing Timed Out | 7 days from submission to carriers for Telnyx to resubmit without changes. Portal users can make a small change and save to create a new VR ID; API users may need to take additional action. |
| Number Not Provisioned to Your Organization | Not Eligible |
