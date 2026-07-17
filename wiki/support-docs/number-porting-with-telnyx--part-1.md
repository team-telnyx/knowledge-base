---
title: Number Porting with Telnyx
summary: This page consolidates Telnyx's number porting policies, procedures, and
  guidance for moving telephone numbers into and out of Telnyx. It covers submitting
  port requests via the Mission Control portal and API, SLA timelines for simple and
  non-simple ports, port request statuses, exception handling, reseller instructions,
  carrier-specific port-out tips, programmatic porting, and SMS considerations for
  ported-in numbers.
sources:
- url: https://support.telnyx.com/en/articles/1130630-porting-policy-procedure
- url: https://support.telnyx.com/en/articles/1130633-checking-a-port-request-status
- url: https://support.telnyx.com/en/articles/1130634-port-numbers-to-telnyx
- url: https://support.telnyx.com/en/articles/1130635-can-i-port-out-my-telnyx-number
- url: https://support.telnyx.com/en/articles/1130643-is-there-a-cancellation-fee
- url: https://support.telnyx.com/en/articles/1130661-does-telnyx-offer-post-paid-service
- url: https://support.telnyx.com/en/articles/1782930-port-request-rejected
- url: https://support.telnyx.com/en/articles/2033789-port-numbers-away-from-telnyx
- url: https://support.telnyx.com/en/articles/2047076-carrier-refusing-to-port-your-number
- url: https://support.telnyx.com/en/articles/2086149-number-porting-rules-and-guidelines
- url: https://support.telnyx.com/en/articles/3284588-port-request-statuses
- url: https://support.telnyx.com/en/articles/3947875-porting-away-from-bandwidth
- url: https://support.telnyx.com/en/articles/5386351-automating-ports-with-programmatic-api
- url: https://support.telnyx.com/en/articles/5595770-port-away-from-voip-ms
- url: https://support.telnyx.com/en/articles/7183887-sms-for-ported-in-phone-numbers
updated_at: 2026-07-17T09:03:47Z
---

# Number Porting with Telnyx

*Part 1 of 3 — see also: [Part 2](number-porting-with-telnyx--part-2.md), [Part 3](number-porting-with-telnyx--part-3.md)*

This page consolidates Telnyx's number porting policies, procedures, and guidance for moving telephone numbers into and out of Telnyx. It covers submitting port requests via the Mission Control portal and API, SLA timelines for simple and non-simple ports, port request statuses, exception handling, reseller instructions, carrier-specific port-out tips, programmatic porting, and SMS considerations for ported-in numbers.

## Overview

Telnyx supports Local Number Portability (LNP) for moving telephone numbers between carriers. This page consolidates Telnyx's porting policies, procedures, statuses, and related guidance for porting numbers into and out of Telnyx, including carrier-specific tips, programmatic porting, and SMS considerations for ported-in numbers.

## Porting Numbers Into Telnyx

### Submitting a Port Request

To port numbers into Telnyx, create a Mission Control account and submit a request from the [Port Numbers](https://portal.telnyx.com/#/app/numbers/port-numbers) page. Enter or paste the numbers you wish to port; at least one telephone number is required. If you have multiple numbers belonging to different end-customers, submit separate port requests.

You will be required to provide:

- **Phone Service Contact details** — the service address on file with the existing carrier.
- **Authorized Person's Name** — must match the existing carrier's records. For resellers, this must be the end customer's information that matches the CSR, not the reseller's business information.
- **Letter of Authorization (LOA)** — signed by the end customer, listing all numbers porting, customer information, and either a wet signature or a valid signature through DocuSign or a similar method.
- **Most recent bill copy** from the existing carrier.
- **Default Connection** — the connection to use once the port is complete.

You may request a Firm Order Commitment (FOC) date, but it is not guaranteed. Each carrier has its own rules and may not respect the requested date. Expedited requests are handled case-by-case and require explicit Telnyx approval.

### Step-by-Step Portal Walkthrough

1. Log in to Mission Control.
2. From the left sidebar, click **REAL-TIME COMMUNICATIONS** → **NUMBERS** → **PORT NUMBERS**.
3. Click the black **New Port Request** button.
4. Choose whether the numbers are your own or your customer's (reseller/service provider).
5. Select the country for the numbers from the drop-down menu. Port requests must be split by country.
6. Enter the numbers manually or paste from a CSV/Excel file. Supported formats include `NPANXXYYYY`, `1NPANXXYYYY`, `NPA-NXX-YYYY`, and `1-NPA-NXX-YYYY`. Separate numbers with commas or line breaks.
7. Click **Check Portability**. Non-portable numbers can be removed with **Remove All Non Portable**. If an international number shows as not eligible, email [porting@telnyx.com](mailto:porting@telnyx.com) to confirm whether it can be ported manually.
8. After the portability check, the request is broken into **Sub Requests** — groups of numbers belonging to the same underlying carrier — to expedite processing.
9. Enter **Account Information**. The address must match the billing address on file with the current provider, and the **Auth Person's Name** must be the person authorized with the current provider to make account changes.
10. Upload the LOA and Invoice/CSR. You can use your own LOA or download a Word/PDF template from the portal. Country-specific documentation requirements appear automatically after the portability check.
11. Click **Save and Finish** to submit.

![A colored coded status of your port request(s).](_images/7c893d87d55b5baa.png)

### Programmatic Porting via API

Telnyx supports porting through the Mission Control API, useful for automating workflows. To port programmatically:

1. Run a [portability check](https://developers.telnyx.com/api/porting/portability-check/post-portability-check).
2. [Initiate a porting order](https://developers.telnyx.com/api/porting/porting-order/list-porting-orders) via the `v2/porting_orders` endpoint.
3. Use the [Documents API](https://developers.telnyx.com/api/documents/list-document-links) to upload the LOA and invoice. The endpoint returns a UUID.
4. [Update the porting order](https://developers.telnyx.com/api/porting/porting-order/list-porting-orders) with the document UUID, `end_user` information, `activation_settings` (FOC date), and `phone_number_configuration` settings.
5. [Confirm the porting order](https://developers.telnyx.com/api/porting/porting-order/list-porting-orders).
6. Optionally configure webhooks for port-in notifications. See the [Quickstart guide](https://developers.telnyx.com/docs/numbers/porting/quickstart) for an overview.

## Porting Policy and SLA Guidelines

Telnyx aims to process port requests as quickly as possible but cannot guarantee a specific completion date until you receive your FOC.

### Simple Ports

As defined by the FCC, simple ports:

1. Do not involve unbundled network elements.
2. Involve an account only for a single line.
3. Do not include complex switch translations (e.g., Centrex, ISDN, AIN services, remote call forwarding, or multiple services on the loop/line).
4. Do not include a reseller.

These are typically ports with fewer than 20 numbers.

- **Submission to losing carrier:** within 2 business days
- **Estimated completion:** 7 business days

### Non-Simple Ports

Any port that does not qualify as a simple port. Ports with more than 20 numbers and multi-line accounts qualify as non-simple ports and may require project management.

- **Submission to losing carrier:** within 4 business days
- **Estimated completion:** 15 business days or more

### Submission Hours and Holidays

Telnyx accepts port request submissions 24/7/365 through Mission Control, but porting requests are only processed and submitted Monday through Friday from 9 AM to 5 PM CT.

Observed US porting holidays:

- New Year's Day
- Memorial Day
- Independence Day
- Labor Day
- Thanksgiving Day
- Christmas Day

Ports around major US holidays may be slightly delayed due to other providers observing additional holidays (e.g., Day after Thanksgiving, Christmas Eve).

## Exceptions, Delays, and Rejections

### Exceptions

If an exception occurs, you will be notified by email. Depending on the nature, the port-out request may need to be resubmitted with the current carrier, which some carriers treat as an entirely new request with additional response time. If you do not respond to an exception within 14 days, Telnyx will cancel the port request. A new request can be submitted with corrected information.

### Common Causes of Porting Exceptions and Delays

- Incorrect spelling of the end customer name (e.g., "Alpha Corp" instead of "Alpha Beta Inc").
- Incorrect service address (wrong street name or zip code).
- Bundling multiple end-customer numbers under a single port request.
- One or more submitted telephone numbers is inactive.
- Not providing an account number.

### Rejected Port Requests

A port request may be rejected by the losing carrier due to an information mismatch. Carriers must verify that the telephone numbers are being ported with the consent of the actual account holder. To minimize rejections, request a Customer Service Record (CSR) from the losing carrier upfront and compare it to the information on your LOA before submitting. See [Porting Error Messages](https://support.telnyx.com/en/articles/1618776-porting-error-messages) for a full list of error messages.

### If a Carrier Refuses to Port

If a losing carrier is difficult about releasing numbers:

- **Verify your information** — incorrect account details are the most common reason for rejection. If unsure, [request a CSR from your carrier](https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier).
- **Call your provider** — phone calls typically yield faster responses than email.
- **Know the FCC regulations** — the [FCC has detailed guidelines](https://www.fcc.gov/consumers/guides/porting-keeping-your-phone-number-when-you-change-providers) on number portability.
