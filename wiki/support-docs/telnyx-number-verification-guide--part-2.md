---
title: Telnyx Number Verification Guide
summary: Telnyx provides several verification mechanisms for phone numbers used on
  its platform, including Verified Numbers for non-Telnyx numbers used as outbound
  CLI, Toll-Free Verification for outbound SMS from toll-free numbers, and Number
  Lookup for retrieving carrier and CNAM data. This page consolidates the verification
  workflows, API usage, pricing, error codes, and related number management resources.
sources:
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
- url: https://support.telnyx.com/en/articles/12386088-how-to-verify-phone-numbers-behind-an-ivr
- url: https://support.telnyx.com/en/articles/13854980-beta-how-to-verify-phone-numbers-using-dtmf-press-1-to-verify
- url: https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide
- url: https://support.telnyx.com/en/articles/5941652-google-verified-calls-faq
- url: https://support.telnyx.com/en/articles/6790265-verified-numbers-faq
- url: https://support.telnyx.com/en/articles/6988813-verified-numbers
- url: https://support.telnyx.com/en/collections/3968222-telnyx-number-management-guide
updated_at: 2026-07-17T09:01:33Z
---

# Telnyx Number Verification Guide

*Part 2 of 3 — see also: [Part 1](telnyx-number-verification-guide--part-1.md), [Part 3](telnyx-number-verification-guide--part-3.md)*

Telnyx provides several verification mechanisms for phone numbers used on its platform, including Verified Numbers for non-Telnyx numbers used as outbound CLI, Toll-Free Verification for outbound SMS from toll-free numbers, and Number Lookup for retrieving carrier and CNAM data. This page consolidates the verification workflows, API usage, pricing, error codes, and related number management resources.

## Toll-Free Verification

Before sending the first outbound message from a toll-free phone number, the number must be verified. Toll-Free Verification requires specific data to be submitted to identify the end business and confirm proper measures are in place to send compliant traffic. Incomplete submissions may be rejected. Approvals typically take 5 business days or less, depending on request volume.

### How to Submit a Verification Request

- **Telnyx Portal:** portal.telnyx.com → Real Time Communications → Messaging → Compliance → [Toll Free Verification](https://portal.telnyx.com/#/programmable-messaging/toll-free-messaging) → Submit Verification Request
- **Telnyx API:** [Submit Verification Request](https://developers.telnyx.com/api/messaging/toll-free-verification/submit-verification-request)

### Verification Statuses

- **Waiting for Telnyx** — Telnyx reviews all submissions to determine if the traffic should be allowed on the platform and for compliance requirements.
- **Waiting for Customer** — If the Telnyx review team has a change they would like made to the Verification Request, the status changes to Waiting for Customer and the decline reason describes the steps required.
- **Waiting for Vendor** — Once Telnyx approves the VR, it goes to the carriers for final approval.
- **Rejected** — If the carriers or Telnyx team reject the VR, the status is rejected and the decline reason explains why.
- **Verified** — Once Telnyx and the carriers have approved it, the status becomes Verified and outbound text messages can be sent from the toll-free number.

Submitting a new Verification Request for an already approved toll-free number overwrites the existing approval and the number becomes unverified until the new request is approved.

### Verification Form Fields

**1. Business Identification**

- **Business Name** — The business name, website domain, and email domain should match, or any difference should be explained in the additional information field.
- **Corporate Website** — Include a business website or social media page showing the business name, contact information, products/services, an About page, a Contact us page, and a Privacy and Terms page.
- **Email Address** — The website domain should match the domain of the email address provided. Freemail contacts like Gmail can be cause for decline.
- **Business Address** — Valid business address.
- **Contact Number** — Contact number for the business using the toll-free number (not the toll-free number being reviewed).
- **Business Contact** — A person's first/last name (not a business name or department).

**2. Messaging Details**

- **Expected Message Volume** — Approximate, based on the available drop-down options.
- **Use Case** — The specific purpose for which the business intends to use toll-free messaging. Examples include conversational, marketing, transactional notifications, or fraud alerts. For mixed use cases, describe the actual use cases in the Use Case description field. Every SMS use case mentioned on the opt-in form should be present here in some way. The use cases selected and mentioned anywhere on the VR or opt-in form should all be consistent.

  Available options include: 2FA, App Notifications, Appointments, Auctions, Auto Repair Services, Bank Transfers, Billing, Booking Confirmations, Business Updates, COVID-19 Alerts, Career Training, Chatbot, Conversational / Alerts, Courier Services & Deliveries, Emergency Alerts, Events & Planning, Financial Services, Fraud Alerts, Fundraising, General Marketing, General School Updates, HR / Staffing, Healthcare Alerts, Housing Community Updates, Insurance Services, Job Dispatch, Legal Services, Mixed, Motivational Reminders, Notary Notifications, Order Notifications, Political, Public Works, Real Estate Services, Religious Services, Repair and Diagnostics Alerts, Rewards Program, Surveys, System Alerts, Voting Reminders, Waitlist Alerts, Webinar Reminders, Workshop Alerts.

- **Description of the Use Case / Summary** — Explains the types of messages being sent, the intended audience, and any relevant compliance measures. For mixed use cases, every SMS use case mentioned on the opt-in form should be present here in some way.
- **Message Content** — Add samples for each use case selected and described in the use case summary field.

**3. Opt-in Workflow Description / Opt-in Image URL**

Provide a link, a link to an image, or a link to a scanned copy of the opt-in. The opt-in process must be clearly documented in the Workflow Description explaining how the opt-in process works (e.g., "subscribers opt in on my website at https://exampleurl.com/opt-in").

There are four ways users can opt in to receive SMS:

1. **Digital**
2. **Paper**
3. **Verbal**
4. **Inbound Message**

For whichever opt-in method is selected, the subscriber must receive these disclaimers at some point before the first message (except for an inbound text opt-in, which can have the disclaimers in the first message):

> You are subscribing to [brand name] for [use case (transactional or marketing)]. Reply STOP to opt out. Reply HELP for help. Standard message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlinked].

- **Digital opt-in** — Include the URL or link to a screenshot of the branded opt-in form (as much of the form as possible) and how subscribers reach it.
- **Paper opt-in** — Include a link to the uploaded branded file and how subscribers receive it.
- **Verbal opt-in** — Include the script users hear when opting in, how they receive it, and where (e.g., what number they call if over the phone, or how they learn the address if in person), plus all the standard disclaimers.
- **Inbound message** — Provide the phone number they text into and how they learn it.

If there is no link for the opt-in image URL field (e.g., verbal consent), put a link to a publicly accessible Google Doc or Dropbox file which diagrams how the opt-in process works.

If Marketing is a selected use case, the marketing SMS opt-in must have its own compliant checkbox separate from the other use cases.

Opt-in form for both transactional and marketing use cases:

- **[Checkbox 1]** By checking this box and submitting this form, you consent to receive transactional text messages for [use case(s)] from (Company Name). Reply STOP to opt out. Reply HELP for help. Standard message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlinked].
- **[Checkbox 2]** By checking this box and submitting this form, you consent to receive text messages for marketing from (Company Name). Reply STOP to opt out. Reply HELP for help. Message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlinked].

In the privacy policy, carriers typically require verbiage to the effect of: "We will not share or sell your mobile information with third parties for promotional or marketing purposes."

Checkboxes must be optional and cannot be pre-checked. The opt-in form should be branded with the same brand being registered.

Important notes:

- The business name should be included on the opt-in form within the message content so the consumer knows who they are interacting with.
- The SMS opt-in checkbox should be unchecked by default.
- SMS consent should be separate from other communication consents (e.g., email), with distinct checkboxes for SMS and email opt-in.
- SMS opt-in and privacy policy must have separate checkboxes.

**4. ISV/Reseller Information**

If the Telnyx account username domain does not match the domain for the business website and business email address in the business contact section, the request will be put into a Waiting For Customer status until the Reseller field has been accurately filled out with the Reseller name. If the Telnyx account is for the same domain as the business being registered, leave the Reseller field blank.

**5. Additional Supporting Details**

If submitting more than 5 toll-free numbers in a single Verification Request, include a detailed valid explanation for why multiple numbers are needed. Be specific — for example, if multiple numbers are needed because there are multiple store locations, explain in depth: "The reason this VR has 6 Toll Free numbers being requested is because we have 6 locations and there will be 1 toll free number for each location so the local team can field specific customer service questions such as inventory checks. +1800XXX-XXXX will be for the Austin, Texas location on 123 Main St. +1888XXX-XXXX will be for the Houston, Texas location on 321 Broadway St."

A commonly used explanation is:

> We need multiple toll-free SMS numbers because we have several employees who regularly communicate with clients. Having enough numbers ensures that each employee can manage conversations efficiently without delays or overlap. All communication is client-initiated, and these numbers help us manage those conversations efficiently while maintaining our privacy standards.

If you run out of characters, use a publicly accessible Google Doc, paste the link into the VR, and describe the content of the Google Doc in the VR as well.

### Age Gating

The opt-in form or website needs an age gate anytime you are marketing something that is not legal to consume under a certain age in any of the 50 states (e.g., alcohol). If it is a restaurant that offers alcohol but will not promote alcohol over SMS, no age gate is needed, but the VR must state that no alcohol will be promoted via SMS. The age gate should not be a YES/NO age gate; it should be an enter-your-birthdate age gate which does not allow the user to proceed if the date is less than the required age.

### Political Use Case

- Include whether donations will be solicited in the use case summary.
- The opt-in form needs a separate checkbox from transactional or marketing consent for political consent if there is a mixed use case.
- The Privacy Policy must explicitly state that "No mobile information will be sold or shared with third parties for promotional or marketing purposes."

### Charity / Fundraising

- Select a Fundraising Use Case unless there are multiple use cases, in which case select Mixed.
- The opt-in form needs a fundraising or charity checkbox separate from the other consents, and the checkbox disclaimers should mention donations will be solicited.
- The Use Case summary of the VR should mention that donations will be solicited.

### Prohibited Content

This is not a comprehensive list:

- Loan soliciting/promotion
- CBD related
- Gambling

### Canadian Toll-Free Numbers

Canadian toll-free numbers must do all of the above plus collect double opt-in: after the initial opt-in process, a confirmation message must be sent and the subscriber must reply with an affirmative that they are subscribing to the program.

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
| Submission Editing Timed Out | 7 days from submission to carriers for Telnyx to resubmit without changes. Portal users can make a small change and save to create a new VR ID; API users face more challenges. |
| Number Not Provisioned to Your Organization | Not Eligible |
