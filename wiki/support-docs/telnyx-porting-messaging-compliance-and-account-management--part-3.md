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

*Part 3 of 5 — see also: [Part 1](telnyx-porting-messaging-compliance-and-account-management--part-1.md), [Part 2](telnyx-porting-messaging-compliance-and-account-management--part-2.md), [Part 4](telnyx-porting-messaging-compliance-and-account-management--part-4.md), [Part 5](telnyx-porting-messaging-compliance-and-account-management--part-5.md)*

This page consolidates Telnyx guidance on porting numbers from Skype and VoIP resellers, resolving Canadian reseller porting errors, cancelling accounts, configuring Skype for Business SIP trunks, toll-free messaging verification and opt-in workflows, SMS opt-out keywords, WhatsApp conversation windows, and handling toll-free carrier rejections.

## Toll-Free Messaging

Telnyx supports SMS on toll-free numbers, with Toll-Free MMS supported in the US and Canada only. Toll-free messaging requires use case registration and verification to ensure compliance with industry standards. Use of non-verified toll-free numbers may result in spam blocks at any time, and unblocking can only be achieved through use case verification.

### Use Case Registration

As of 23 November 2022, use case registration for toll-free numbers can be submitted from the Mission Control Portal. Registration can also be completed via API for bulk submissions and status tracking — see the developer documentation for details.

Information required for registration includes:

- Business details
- The toll-free number being used for the campaign
- A summary of the use case
- Message content examples and expected monthly volume
- The opt-in process
- Additional use case details (Terms URL, Privacy Policy)
- Reseller/ISV field — add your business name if you are a reseller or ISV; leave blank if registering for direct use

Approval times are approximately 2 weeks, with an expected improvement to 1 week. Only one unique use case can be associated with one toll-free number; multiple toll-free numbers cannot send the same messaging content, as this is considered an industry bad practice with a higher chance of spam blocking.

From 8 November 2023, any unverified toll-free numbers attempting to send messages are blocked. From 31 January 2024, unverified toll-free numbers are automatically blocked industry-wide.

After submission, track status from the Requests tab. To amend details, click the small arrow icon to access verification information, make changes, and click Save Changes. Webhook URLs can be provided to receive real-time status updates.

### Message Content Length

- UCS-2 (16 bit): 70 character maximum; 67 characters for multi-part message bodies
- Latin1 (8 bit): 140 character maximum; 134 characters for multi-part message bodies
- GSM7 (7 bit): 160 character maximum; 153 characters for multi-part message bodies

### Valid Use Cases

Acceptable use cases include: 2FA, Account Notification, Customer Care, Delivery Notification, Fraud Alert Messaging, Higher Education, Low Volume Mixed, Marketing, Mixed, Polling and Voting, and Public Service Announcements.

### Inappropriate Use Cases

The following are not permitted and may be blocked regardless of opt-in status:

- Social Marketing
- Collections
- Cryptocurrency and cryptocurrency-related language
- Financial services (high-risk/subprime lending, credit cards, auto loans, mortgages, payday loans, short-term loans, student loans, debt consolidation/reduction/forgiveness)
- Insurance (car, health)
- Gambling, Casino, and Bingo
- Gift cards
- Sweepstakes
- Free prizes
- Investment opportunities
- Lead generation
- SEO Services
- Recruiting
- Commission programs
- Credit repair
- Tax relief
- Illicit or illegal substances (including Cannabis)
- Work from home
- Get rich quick
- UGGS and RayBan campaigns
- Phishing
- Fraud or scams
- Cannabis
- Deceptive marketing
- SHAFT: Sex, Hate, Alcohol, Firearms, or Tobacco

### Additional Best Practices

- **High Frequency Messages** — Do not send more than 10 messages to a recipient in any 24-hour period unless the recipient has engaged in two-way SMS communication or has explicitly opted in to frequent messages.
- **Spoofing** — Do not represent or identify yourself as another individual or business.
- **Fraud or Phishing** — Sending fraudulent information or phishing for confidential information is explicitly prohibited.

### Consent and Opt-In

Before sending messages, obtain consent from receivers with a clear call-to-action that includes:

- The program or product description
- The phone number(s) or short code(s) from which messaging will originate
- The specific identity of the organization or individual being represented
- Clear and conspicuous language about opt-in and any associated fees or charges
- Other applicable terms and conditions (how to opt-out, customer care contact information, applicable privacy policy)

Receivers may unsubscribe by sending stop words such as STOP or UNSUBSCRIBE. Senders have up to 24 hours to remove the recipient from the list.

### Toll-Free Verification Webhook Notifications

Telnyx provides real-time status updates via webhooks to monitor the verification lifecycle. Notifications are sent to the webhook URL provided during submission. The `verification_status` field reflects one of the following values:

- `Rejected` — The verification request was rejected.
- `Waiting For Vendor` — The request is pending vendor review.
- `Waiting For Customer` — Additional information is needed from the customer.
- `Verified` — The toll-free number has been successfully verified.

Each event includes the affected phone number(s), business name, and the reason for the current status (if applicable).

## Toll-Free Opt-In Workflow Templates

Toll-free opt-in workflow descriptions must follow one of four templates: Digital, Verbal, Paper, or Inbound Message. Replace bracketed variables such as `[URL]` with actual values (e.g., `https://www.example.com/opt-in`). Where a hosted URL is required, upload screenshots to a hosting service like Dropbox or Imgur and use the publicly accessible link.

### Digital Opt-In

If the opt-in form is publicly available on the Internet:

> "Subscribers opt in digitally, they start at [URL] and navigate to [URL] where the opt in form is located."

If sign-in is required to view the opt-in form, add a public link to a hosted screenshot:

> "Subscribers opt in digitally, they sign in at [URL] and navigate to where the opt in form is located in the system, Here is a screenshot of the opt in form: [URL]."

### Verbal Opt-In

For the location variable, use a Web or social media URL, or a hosted screenshot of a Google/Bing search, advertisement, email signature, business card, flyer, poster, etc.

> "Subscribers [call/visit] the [actual phone number/actual address] which is published at [location]. If they request to receive sms then we read a script. Please see the Opt in Image URL for the full script."

### Paper Opt-In

A paper opt-in can be a contract, onboarding document, or other paper form. Upload a copy of the relevant section and host it on a service like Dropbox.

> "Subscribers opt in via paper form. Please see screenshot of paper form at [URL]."

### Inbound Message Opt-In

An inbound message means you do not initiate conversations with subscribers via outbound text; all messages are sent in response to a text received. For the location variable, use a Web or social media URL, or a hosted screenshot of a Google/Bing search, advertisement, email signature, business card, flyer, poster, etc.

> "Subscribers opt in by sending us the first text message. They find the number to text us at [location]."
