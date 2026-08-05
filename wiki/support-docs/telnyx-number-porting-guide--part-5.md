---
title: Telnyx Number Porting Guide
summary: A consolidated reference for porting phone numbers to and from Telnyx, covering
  best practices, FastPort® activation, port request statuses, common error messages,
  SMS porting behavior, Port Out PIN protection, bundle pre-configuration, and how
  to contact the Porting team.
sources:
- url: https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error
- url: https://support.telnyx.com/en/articles/1130623-authorized-name-mismatch-error
- url: https://support.telnyx.com/en/articles/1618776-porting-error-messages
- url: https://support.telnyx.com/en/articles/2021334-your-guide-to-fastport
- url: https://support.telnyx.com/en/articles/2030770-port-in-best-practices
- url: https://support.telnyx.com/en/articles/2042977-porting-in-day-of-port-foc
- url: https://support.telnyx.com/en/articles/2054704-fastport-faqs
- url: https://support.telnyx.com/en/articles/3284588-port-request-statuses
- url: https://support.telnyx.com/en/articles/3561993-using-telnyx-fastport
- url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
- url: https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
- url: https://support.telnyx.com/en/articles/8006189-port-out-pin-protection
- url: https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing
- url: https://support.telnyx.com/en/articles/8709331-porting-bundles
updated_at: 2026-08-05T13:27:12Z
---

# Telnyx Number Porting Guide

*Part 5 of 5 — see also: [Part 1](telnyx-number-porting-guide--part-1.md), [Part 2](telnyx-number-porting-guide--part-2.md), [Part 3](telnyx-number-porting-guide--part-3.md), [Part 4](telnyx-number-porting-guide--part-4.md)*

A consolidated reference for porting phone numbers to and from Telnyx, covering best practices, FastPort® activation, port request statuses, common error messages, SMS porting behavior, Port Out PIN protection, bundle pre-configuration, and how to contact the Porting team.

## Contacting Telnyx Support (NOC)

The Telnyx Network Operation Center (NOC) is available 24/7/365 for questions about call or message failures, the API, or other account concerns.

- **Chat:** Click "chat with us" at the bottom of the left menu when signed into the Portal; the chat window appears at the bottom right of the Mission Control Portal.
- **Phone:** +1-888-980-9750 or any of the international numbers listed below.
- **Ticket:** Email [support@telnyx.com](mailto:support@telnyx.com).

At the beginning of a chat or email conversation, a ticket number is provided. Reference that ticket number when following up so the conversation can resume where it left off.

### Reporting Call or Message Failures

The NOC requires specific information to troubleshoot effectively. The best way to provide a call example is with a Call ID (SIP Call ID, Unique CDR ID, or Call UUID) or MDR ID, which can be found in a [call detail request](https://portal.telnyx.com/#/app/reporting/detail-requests) generated within the Reporting section of the Portal. Alternatively, the following information helps identify the call or message:

**Call Example:**

- **SIP Connection Name & ID:** Found in the SIP Connection settings.
- **Direction:** Inbound or Outbound.
- **CLI:** Source number.
- **CLD:** Destination number.
- **Date+Time:** Including timezone.

**Messaging Example:**

- **Messaging Profile Name & ID:** Found in the messaging profiles settings.
- **Direction:** Inbound / Outbound.
- **From number / Alphanumeric Sender ID:** The sender's number or name.
- **To number:** The receiver's number.
- **Date Timestamp:** Including timezone.
- **Error Code:** Found in the response; see the [error documentation](https://developers.telnyx.com/api/errors).

The NOC can troubleshoot most call quality or messaging issues up to 72 hours after occurrence. If escalation with carrier partners is required, examples within 48 hours are necessary. If the issue is not reproducible, examples within 24 hours are required to continue escalations.

### Reporting API Issues

To report API issues, provide as much of the following as possible:

- **Issue:** The encountered issue in a few words, and the expected behavior from the endpoint(s).
- **Endpoint(s):** The exact public URL endpoints being called.
- **Timestamp with timezone:** Preferably within the last 24 hours.
- **Request:** The payload of the request being sent.
- **Response:** The payload of the response being received.
- **Can you replicate the issue:** Yes/No.

Requests can be tested at the [developer portal](https://developers.telnyx.com). Additional context about the function being attempted is appreciated. See the [error documentation](https://developers.telnyx.com/api/errors) to help determine the source of an error.

### Reporting Portal Issues

For Portal issues such as an unfamiliar error message, a screenshot of the error is appreciated. Alternatively, access the console window using the "Inspect Element" tool in the browser (usually F12 or right-click → "Inspect Element"). Screenshots can be attached to an open Intercom chat via the paperclip icon, or emailed to [support@telnyx.com](mailto:support@telnyx.com). If a screenshot is not possible, a description of what was being attempted in the Portal and how it compares to what was experienced is helpful — including the URL of the page, error messages received, buttons clicked, and text-boxes filled in.

### International Support Numbers

The NOC can be reached by chat (via the chat icon in the bottom right of the Portal), by email at [support@telnyx.com](mailto:support@telnyx.com), or by phone at:

- Estonia: +3726991435
- Finland: +358753255300
- Ireland: +353818123457
- Israel: +972772200092
- Mexico: +525588974917
- Netherlands: +31853018256
- New Zealand: +6498844134
- Philippines: +63322346319
- Poland: +48221530079
- Singapore: +6531594436
- United Kingdom: +443301900175
- United States & Canada: +18889809750

### Notes About Contacting NOC Support

Customer emails to [support@telnyx.com](mailto:support@telnyx.com) sometimes go to spam. Email providers are becoming stricter about domains without properly configured SPF/DMARC records, which can result in messages being marked as spam. Other reasons include:

- **Email content:** Spam filters identify and block emails containing keywords, phrases, or content commonly associated with spam.
- **Sender reputation:** Many email providers consider the reputation of the sender. A history of sending spam can cause emails to be flagged.
- **User behaviour:** Spam filters consider how users interact with emails. If many users mark similar emails as spam or delete them without opening, future similar emails may be classified as spam.

Recommendations:

- Add the Telnyx email address to contacts or safe senders list.
- Avoid spammy keywords or phrases in email content.
- Send emails from a reputable domain and IP address.

Telnyx performs a daily review of emails that may have ended up in spam and pushes them to the ticketing system.
