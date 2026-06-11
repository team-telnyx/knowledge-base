---
title: Toll-Free Verification and Messaging
summary: Toll-Free numbers on Telnyx require verification before sending outbound
  messages. This page covers the full verification process, form requirements, use
  case selection, opt-in workflows, prohibited content, carrier rejections, and related
  topics such as opt-out handling, webhook notifications, and number porting.
sources:
- url: https://support.telnyx.com/en/articles/10729979-toll-free-verification-request-guide
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/13765655-compliance-catch-up-why-toll-free-verification-now-mirrors-10dlc
- url: https://support.telnyx.com/en/articles/14286763-forbidden-messaging-use-cases-in-the-us-and-canada-10dlc-toll-free-and-short-code
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
- url: https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status
- url: https://support.telnyx.com/en/articles/8673249-us-ca-toll-free-number-porting
updated_at: 2026-06-11T11:12:33Z
---

# Toll-Free Verification and Messaging

*Part 2 of 4 — see also: [Part 1](toll-free-verification-and-messaging--part-1.md), [Part 3](toll-free-verification-and-messaging--part-3.md), [Part 4](toll-free-verification-and-messaging--part-4.md)*

Toll-Free numbers on Telnyx require verification before sending outbound messages. This page covers the full verification process, form requirements, use case selection, opt-in workflows, prohibited content, carrier rejections, and related topics such as opt-out handling, webhook notifications, and number porting.

## Opt-In Workflow and Consent

Ensuring proper SMS consent is critical for verification. There are four opt-in methods, each with a specific workflow description template.

### Digital Opt-In

If the form is publicly available:

> "Subscribers opt in digitally, they start at [URL] and navigate to [URL] where the opt in form is located."

If a login is required to see the form, include a publicly accessible hosted screenshot:

> "Subscribers opt in digitally, they sign in at [URL] and navigate to where the opt in form is located in the system. Here is a screenshot of the opt in form: [URL]."

### Verbal Opt-In

> "Subscribers [call/visit] the [actual phone number/actual address] which is published at [location]. If they request to receive sms then we read a script. Please see the Opt in Image URL for the full script."

The location variable should be a web or social media URL, or a hosted screenshot of a Google/Bing search, advertisement, email signature, business card, flyer, poster, etc.

### Paper Opt-In

> "Subscribers opt in via paper form. Please see screenshot of paper form at [URL]."

Upload a copy of the relevant section of the paper form, host it (e.g., Dropbox), and share the publicly accessible link.

### Inbound Message Opt-In

> "Subscribers opt in by sending us the first text message. They find the number to text us at [location]."

The location variable should be a web or social media URL, or a hosted screenshot showing how subscribers discover the number.

### Required Consent Disclaimers

Before the first message (except for inbound text opt-in, where disclaimers can be in the first message), the subscriber must receive:

> You are subscribing to [brand name] for [use case (transactional or marketing)]. Reply STOP to opt out. Reply HELP for help. Standard message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlink].

### Checkbox Requirements

- The SMS opt-in checkbox must be **unchecked by default** (not pre-checked).
- SMS consent must be **separate from other communication consents** (e.g., email) with distinct checkboxes.
- SMS opt-in and privacy policy acceptance must have **separate checkboxes**.
- The opt-in form must be **branded** with the same brand being registered.
- The business name must appear within the message content on the opt-in form.
- Marketing SMS must have its **own compliant checkbox**, separate from transactional consent.

Example for a form covering both transactional and marketing use cases:

- **[Checkbox 1]** By checking this box and submitting this form, you consent to receive transactional text messages for [use case(s)] from (Company Name). Reply STOP to opt out. Reply HELP for help. Standard message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlink].
- **[Checkbox 2]** By checking this box and submitting this form, you consent to receive text messages for marketing from (Company Name). Reply STOP to opt out. Reply HELP for help. Message and data rates may apply. Message frequency may vary. View our Terms and Condition [hyperlink]. View our Privacy Policy [hyperlink].

### Special Consent Rules

**One-to-one consent:** Per FCC-backed rules, consent must be specific to your business. You cannot use lead lists where the user agreed to be contacted by "partners."

**Political use case:** The opt-in form needs a separate checkbox for political consent (in addition to transactional/marketing). The privacy policy must explicitly state: "No mobile information will be sold or shared with third parties for promotional or marketing purposes." Indicate in the use case summary whether donations will be solicited.

**Charity/Fundraising:** Select the Fundraising use case (or Mixed if there are multiple use cases). A separate fundraising/charity checkbox is required on the opt-in form, and its disclaimers must mention that donations will be solicited. The use case summary must also mention donation solicitation.

**Canadian toll-free numbers:** Must collect **double opt-in** — after the initial opt-in, a confirmation message must be sent, and the subscriber must reply with an affirmative to confirm subscription.

## Age Gating Requirements

The opt-in form or website must include an age gate anytime you market something not legal for minors in any of the 50 states (e.g., alcohol). The age gate must require the user to **enter their birthdate** — YES/NO age gates are not acceptable. If a business sells alcohol but will not promote it via SMS, no age gate is needed, but this must be stated in the verification request.

## Prohibited Content and Use Cases

The following message categories are not permitted across US and Canada messaging channels (10DLC, Toll-Free, and Short Code):

**SHAFT categories:**
- **Sex:** Adult content or services
- **Hate:** Hate speech or discriminatory content
- **Alcohol:** Subject to regional/carrier-specific rules; may be allowed with appropriate age verification
- **Firearms:** Weapons and related products — not permitted
- **Tobacco/Vape:** Including e-cigarettes — not permitted

**Other prohibited categories:**
- Loan soliciting/promotion, payday loans, short-term loans, debt consolidation/reduction/forgiveness, credit repair
- CBD, cannabis, and other illegal/federally illegal substances
- Gambling, casino, bingo, sports betting
- Cryptocurrency and related content
- Sweepstakes, free prizes, gift cards, get-rich-quick schemes
- Third-party lead generation, multi-level marketing
- Phishing, fraud, scams, deceptive marketing
- Spoofing (representing yourself as another individual or business)
- Third-party debt collection
- Stock alerts, risk investment
- High-risk/subprime lending, auto loans, mortgages, student loans
- Car insurance, health insurance
- UGGS and RayBan campaigns
- Social marketing, SEO services, recruiting, commission programs, work from home

Violations can result in carrier filtering, increased error rates, blocking of individual messages, blocking of phone numbers, or account termination.

**Additional compliance notes:**
- Avoid generic or public URL shorteners; use branded, recognizable domains with HTTPS.
- Do not send more than 10 messages to a recipient in any 24-hour period unless the recipient has engaged in two-way communication or explicitly opted in to frequent messages.
- One unique use case should be associated with one toll-free number. Multiple toll-free numbers sending identical messaging content is considered an industry bad practice.
