---
title: 10DLC Campaign Registration and Compliance
summary: A comprehensive guide to registering, configuring, and maintaining compliant
  10DLC campaigns on Telnyx, covering use cases, trust scores, opt-in methods, message
  flow, CTA requirements, keyword configuration, number assignment, shared campaigns,
  and approval best practices.
sources:
- url: https://support.telnyx.com/en/articles/10562019-guide-to-10dlc-message-flow-field
  content_hash: 52724a201fd5374074a0eb90e9410468b85a7658feedbe8a9d47840d78861363
- url: https://support.telnyx.com/en/articles/10684248-10dlc-use-cases
  content_hash: 1642b9aa15da6996121686960f14303b8ae52ce210e2da3f8d83db58714cc412
- url: https://support.telnyx.com/en/articles/10684260-10dlc-opt-in-form
  content_hash: 8ad5cdae420fd7df4a80633f0af9e3ae25b2442e724a222f7a3e1070264f0351
- url: https://support.telnyx.com/en/articles/11072276-10dlc-number-assignment-status
  content_hash: 770ca9ba38e331a0bef2ee21c47f1bcb1145a0bc5ca188b8c03c487ac05a2dab
- url: https://support.telnyx.com/en/articles/5617538-10dlc-shared-campaigns
  content_hash: e626ef28a6a0be235fefc591464a31366236db066180b4f1bf535dcad173c9c9
- url: https://support.telnyx.com/en/articles/6325734-how-to-assign-a-number-to-a-campaign
  content_hash: 2bd820c19999d71842708f2f7ec38f7c7406888e79ed9c0b45dc2eec3f465904
- url: https://support.telnyx.com/en/articles/6325747-10dlc-trust-scores-use-cases
  content_hash: d6bd1ec81d473ca63ef7c249bc414517b46feea43b2132519727076e3bfa6773
- url: https://support.telnyx.com/en/articles/6339152-how-to-create-a-10dlc-campaign
  content_hash: ba5b36e22886219329a142b32b5efc7c594b903d68df43b065b45e80b485d78b
- url: https://support.telnyx.com/en/articles/6339158-bring-campaigns-to-telnyx
  content_hash: 639b3ec94281b897babf04a81683f8dda03b1be42c8865bc196cdaffea808c7a
- url: https://support.telnyx.com/en/articles/7127078-10dlc-campaign-approval-best-practices
  content_hash: e8663aa9412e6dc56b01f487761c2cf0bce4e360dd4cf455c7b9a0d3343fdcac
- url: https://support.telnyx.com/en/articles/8269151-assigning-did-to-a-10dlc-campaign-fails
  content_hash: 5695a125b887d6ce58992c100db1af80399f925aa5b3dbf4f323ff550d0dc73a
- url: https://support.telnyx.com/en/articles/9038141-messaging-10dlc-campaign-checklist
  content_hash: 1672ce4b25969e32d5e38d4007ed007a55568633b07ad0b102d6ef139f1bcf16
- url: https://support.telnyx.com/en/articles/9940291-10dlc-campaign-compliance-requirements
  content_hash: 10cadb4c1a4e41ac2d6f453c897e739d96f4e1efe24ab346ee6fed9dd87bcd25
updated_at: 2026-06-11T11:11:29Z
---

# 10DLC Campaign Registration and Compliance

*Part 2 of 4 — see also: [Part 1](10dlc-campaign-registration-and-compliance--part-1.md), [Part 3](10dlc-campaign-registration-and-compliance--part-3.md), [Part 4](10dlc-campaign-registration-and-compliance--part-4.md)*

A comprehensive guide to registering, configuring, and maintaining compliant 10DLC campaigns on Telnyx, covering use cases, trust scores, opt-in methods, message flow, CTA requirements, keyword configuration, number assignment, shared campaigns, and approval best practices.

## Message Flow and Opt-In Methods

The Message Flow field documents how subscribers opt into your campaign. This is often the most challenging part of registration. There are four primary opt-in methods: **Digital**, **Verbal**, **Paper**, and **Inbound Message/Keyword**. Fill in the variables in the relevant template to match your brand and campaign details.

### Digital Consent (Web Form)

**Message Flow template:**

- The user navigates to [Brand Name]'s [website] and subscribes via a specific opt-in page at [URL] or [path subscriber takes if gated] and [link to screenshot].
- The opt-in form clearly states: *"By providing your phone number and clicking 'Submit,' you agree to receive SMS [update type] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. Consent is not a condition of purchase. [Privacy verbiage such as: Your mobile information will not be sold or shared with third parties for promotional or marketing purposes.] or [Link to compliant Privacy Policy]."*

For detailed digital form requirements, see [10DLC Opt-In Form](10dlc-opt-in-form.md).

### Verbal Consent (Phone or In-Person)

**General Message Flow template:**

- When a customer [calls or walks] in to [phone number or office address], published at [URL or how user learns number/address], the representative explains the consent process verbally.
- Agent states: *"By providing your phone number, you agree to receive SMS [Use Case(s)] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. We will not share mobile information with third parties for promotional or marketing purposes."*
- Once the customer verbally agrees, the phone number is recorded, and a confirmation SMS is sent: *"You have agreed to receive SMS updates from [Brand Name]. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help."*

**Marketing use case** — After verbal agreement, send a confirmation SMS that includes: *"To confirm you also want to receive marketing messages please reply YES."* If the user replies YES, they are subscribed to promotional messaging. If they do not reply YES, they will only receive informational messaging.

**Political use case** — After verbal agreement, send a confirmation SMS that includes: *"To confirm you also want to receive political messages please reply YES."* If the user replies YES, they are subscribed to political messaging. If they do not reply YES, they will only receive informational messaging. The verbal script must also state whether donations will or will not be solicited.

### Physical Consent (Paper Form)

**Message Flow template:**

- The user fills out a paper form during [appointment/onboarding/renewal/etc.] at [address], which they learn about at [website/social/etc.], providing their phone number and signing their consent.
- The form includes a disclaimer: *"By signing this form and providing your phone number, you agree to receive SMS [Use Case(s)] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. Consent is not a condition of purchase. Your mobile information will not be sold or shared with third parties for promotional or marketing purposes."*
- Once the information is entered into the system, the user receives a confirmation SMS: *"Thank you for signing up for SMS updates from [Brand Name]. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help."*
- Provide a link (e.g., Dropbox) to an image of the paper form.

### Opt-In by Keyword

**Message Flow template:**

- The [brand] provides a keyword (e.g., "START") and a number (e.g., 123456) via [a channel such as a website, flyer, or QR code].
- The keyword opt-in process includes a disclaimer: *"Text [START or similar] to [123456] to opt in to receive SMS [use case(s)] from [Brand Name]. Message frequency may vary. Standard Message and Data Rates may apply. Reply STOP to opt out. Reply HELP for help. Consent is not a condition of purchase. [Brand Privacy Policy URL or privacy policy verbiage around mobile data sharing]."*
- When the user texts the keyword, the system responds: *"Thank you for opting in to [Brand Name] SMS [update type]! Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help. Your mobile information will not be sold or shared with third parties for promotional or marketing purposes."*
- Provide a link to where the phone number/QR code is advertised or a screenshot.

### Opt-In by Inbound Message

**Message Flow template:**

- The [brand] provides a number (e.g., 123456789) via [a channel such as a website, flyer, QR code, business card, email signature, etc.].
- When the user texts the number, the system responds: *"Thank you for your message to [Brand Name]! We will be with you shortly. Msg freq may vary. Std msg & data rates apply. Reply STOP to opt out, HELP for help. We will not share or sell your mobile information for marketing/promotional purposes."*
- Provide a link to where the phone number/QR code is advertised or a screenshot.

This method relies on **implied consent** — the consumer initiates the text message exchange, and the business only responds with relevant information. No additional permission is needed beyond the initial contact.

### Use-Case-Specific Opt-In Requirements

- **Marketing use case** — The opt-in must explicitly mention marketing, e.g., "You are opting in to receive marketing SMS from [Brand Name]." If the CTA/Privacy Policy mentions marketing, the campaign's use case in TCR must include marketing, and vice versa.
- **Political or Charity use case** — If there is any fundraising (or perception of fundraising), the opt-in must state "Donations may be solicited." The program summary should include: "Donations will be secured through ___ and Accreditation listing is ___." A valid CTA and clear product description within the SMS terms of service must clearly disclose that donations will be solicited.

## Opt-In Form Requirements

If using a digital form for opt-in, it must meet the following criteria:

1. **All required disclaimers** — Include consent language, message frequency disclosure, msg & data rates notice, opt-out instructions, help instructions, and privacy policy statement or link.
2. **SMS consent checkbox is specific, explicit, and optional** — It must not be buried in terms and conditions, combined with other consents (e.g., "I agree to the terms and conditions"), or be a mandatory field. It should be unchecked by default.
3. **The subscriber knows what to expect** — Frequency, message types, and terms are clearly communicated.
4. **Phone number field is optional** — It should not be a required/mandatory field on the form, as this would be considered forced opt-in.
5. **Opt-in language must be exclusively for text messages** — It cannot include email or phone calls; those must be handled separately.
6. **For Political/Charity use cases** — Add "Donations may be solicited" to the opt-in disclaimers if applicable.
7. **For Marketing use cases** — Add explicit marketing language such as "You are opting into marketing texts" to the disclaimers.
8. **Include links to Privacy Policy and Terms & Conditions** in the CTA/registration.

If the opt-in occurs on a website but not on the main page, provide the specific URL. If a pop-up form is used, note this in the CTA field of the registration. Popups are **not** a valid method for displaying terms and conditions.
