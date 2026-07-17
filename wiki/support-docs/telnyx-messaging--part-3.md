---
title: Telnyx Messaging
summary: A consolidated reference for Telnyx programmable messaging covering messaging
  profiles, opt-in/opt-out keywords and auto responses, 10DLC and toll-free verification,
  hosted SMS, SMPP setup, and third-party integrations.
sources:
- url: https://support.telnyx.com/en/articles/10645338-10dlc-keywords-and-confirmation-messages
- url: https://support.telnyx.com/en/articles/12650709-how-to-pick-a-toll-free-use-case
- url: https://support.telnyx.com/en/articles/1270091-sms-opt-out-keywords-and-stop-words
- url: https://support.telnyx.com/en/articles/15138019-toll-free-carrier-rejections
- url: https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide
- url: https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile
- url: https://support.telnyx.com/en/articles/4348981-receiving-sms-on-your-telnyx-number
- url: https://support.telnyx.com/en/articles/5336668-hosted-sms-messaging-process
- url: https://support.telnyx.com/en/articles/5353868-toll-free-messaging
- url: https://support.telnyx.com/en/articles/6986625-easy-text-marketing-and-telnyx-integration
- url: https://support.telnyx.com/en/articles/6989758-toll-free-opt-out-words
updated_at: 2026-07-17T09:00:31Z
---

# Telnyx Messaging

*Part 3 of 4 — see also: [Part 1](telnyx-messaging--part-1.md), [Part 2](telnyx-messaging--part-2.md), [Part 4](telnyx-messaging--part-4.md)*

A consolidated reference for Telnyx programmable messaging covering messaging profiles, opt-in/opt-out keywords and auto responses, 10DLC and toll-free verification, hosted SMS, SMPP setup, and third-party integrations.

## Toll-Free Carrier Rejections

Common carrier rejection reasons and resolutions for toll-free submissions include:

- **Agreeing to receive messages must be optional** — The SMS opt-in is forced by submitting a form with a phone number. Make the phone number field optional or add a checkbox to SMS disclosures, then resubmit.
- **Additional information requested — justification for more than 5 numbers per business** — Provide a valid explanation in the additional use case details field for 6+ numbers, then resubmit.
- **Business email address must use an official domain** — The email domain does not match the website domain. Update the email and resubmit.
- **Business information could not be verified** — Business details do not match the website. Ensure website details match the submission, then resubmit.
- **Business registration number is missing or invalid** — Wrong business name or company less than 6 months old. Email [tfverification@telnyx.com](mailto:tfverification@telnyx.com) with the business registration document. Do not resubmit.
- **Consent for messaging cannot be part of other agreements** — SMS opt-in is grouped with product/service terms. Provide a separate SMS-only opt-in or remove terms and conditions, then resubmit.
- **Contact name must belong to a business representative** — Name is unintelligible. Update and resubmit.
- **Disallowed content — cannabis, CBD, or other illegal substances** — Remove cannabis content from the website. Exceptions may apply for 2FA, Employee Alerts, or HR/Staffing use cases.
- **Disallowed content — third-party lead generation or multi-level marketing** — Remove lead generation language. Lead alerts and lead management are allowed.
- **End business details must be accurate and complete** — Brand name or DBA does not match. Correct the brand name in the submission or opt-in disclosure, then resubmit.
- **Entity misclassification** — Business entity type does not match official records. Update and resubmit.
- **High risk — known spam campaign** — Business flagged by carrier prior to joining Telnyx. Email [tfverification@telnyx.com](mailto:tfverification@telnyx.com) to request a carrier-level appeal.
- **High risk — submission flagged for high-risk domain issues** — Domain similar to a flagged business or very new. Email [tfverification@telnyx.com](mailto:tfverification@telnyx.com) for appeal. Do not resubmit.
- **Invalid or inaccessible website URL** — Website is inaccessible. Ensure the site is live and public, or email [tfverification@telnyx.com](mailto:tfverification@telnyx.com).
- **Marketing messages require express written consent** — Marketing/promotional SMS cannot be combined with other use cases in the same opt-in. Add a separate opt-in for marketing SMS. Note: opt-ins stating "receive promotional or marketing and informational SMS" will be rejected; "informational" must be defined and is typically a separate transactional opt-in.
- **Opt-in — consent for messaging is a requirement for service** — SMS is not optional. Add a checkbox to make it optional, then resubmit.
- **Opt-in does not match the use case** — Opt-in mentions a use case that does not align with the submission. Update the opt-in or use case to match, then resubmit.
- **Opt-in example must be complete, branded, and legible** — Image is not branded, missing details, or blurry. Provide a new screenshot and resubmit.
- **Opt-ins must clearly reflect the end business** — Opt-in is branded with something other than what was submitted. Update and resubmit.
- **Opt-in URL not accessible** — Link is inaccessible or returns 404. Update and verify, then resubmit.
- **SHAFT violation — alcohol message content without a 21+ robust age gate** — Website lacks age verification. Add an age gate and resubmit.
- **Social platform must be established and active** — Social media link is missing business contact details. Update the page and resubmit.
- **Submission editing timed out** — Resubmission did not occur within 7 days. Email [tfverification@telnyx.com](mailto:tfverification@telnyx.com) for details. Do not resubmit until feedback is received.
- **Website is password protected or requires login** — Make the website public, then resubmit.
- **Website must be established and active** — Website is missing a Home Page, Contact Information, Products/Services, About page, Contact Us page, or Privacy and Terms page. Update and resubmit.

## Hosted SMS Messaging

Hosted SMS messaging allows a customer to port and enable messaging with Telnyx for a number while leaving the voice portion with the current voice provider. This requires the expressed consent of the authorized end user, a Letter of Authorization (LOA), and an invoice from the current messaging provider.

The account must be Level 2 Verified to submit hosted messaging orders. In the portal, navigate to **Real-Time Communications > Messaging > Hosted Messaging** and click **Create new order**. Up to 200 numbers can be added per order, along with the messaging profile to assign them to. The LOA must be signed and dated by the end user within the last 30 calendar days, and the invoice must match.

Upload requirements:

- Files must be PDF, max 5MB each.
- Two files required: LOA and Bill.
- File names cannot contain special characters (#, $, %, &, @, etc).

Orders are processed within 24–48 business hours, Monday through Friday, 9am–5pm CT. Telnyx accepts submissions 24/7/365 but observes New Year's Day, Memorial Day, Independence Day, Labor Day, Thanksgiving, Day after Thanksgiving, Christmas Eve, and Christmas Day.

Hosted messaging is only available for local numbers in the US and Canada. It is not available for international numbers or for transfers between Telnyx accounts. If voice and messaging currently live with a wireless provider (including Google Voice), voice must be ported to a non-wireless provider first. Zoom Phone does allow hosted messaging away from their network. Toll-free hosted messaging is supported but takes a minimum of 72 hours.

Providers known to block hosted messaging transfers include Bandwidth, Aerialink, and Callfire. Manual intervention is required for these providers, and the direct customer may need to approve the release.

## SMPP (Short Message Peer-to-Peer)

SMPP is a widely used protocol for SMS delivery and receipt, best suited for customers requiring high throughput. This feature is reserved for contracted Telnyx customers committing to a $5,000 minimum monthly spend for 12 months.

### Connection details

- **Host:** smpp.telnyx.com
- **Port:** 2775
- **SSL/TLS:** Required
- **Username and password:** Provided by the Telnyx account manager (request by providing the Messaging Profile ID)

### Throughput

- Long Code: 10 messages per number per minute
- Toll-Free: 1,200 messages per number per minute

### Supported PDUs

- bind_transmitter
- bind_transceiver
- bind_receiver
- unbind
- submit_sm
- deliver_sm
- enquire_link

### Required bind parameters

- system_id = Telnyx provided
- password = Telnyx provided
- addr_ton = 1 (International)
- addr_npi = 1 (ISDN/telephone numbering plan, E163/E164)
