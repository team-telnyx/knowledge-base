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

*Part 2 of 3 — see also: [Part 1](number-porting-with-telnyx--part-1.md), [Part 3](number-porting-with-telnyx--part-3.md)*

This page consolidates Telnyx's number porting policies, procedures, and guidance for moving telephone numbers into and out of Telnyx. It covers submitting port requests via the Mission Control portal and API, SLA timelines for simple and non-simple ports, port request statuses, exception handling, reseller instructions, carrier-specific port-out tips, programmatic porting, and SMS considerations for ported-in numbers.

## Special Instructions for Resellers

If your company name and service address are not listed on the CSR with the current carrier, Telnyx considers you a reseller. Resellers must:

- Be authorized to act on behalf of the end customer. Submit an LOA signed by the end customer whenever possible. Telnyx may request a copy of the Master Services Agreement that grants the right to change carriers.
- Be prepared to provide a signed LOA from the customer at any time upon request.
- Create separate port requests for each customer and each service address when porting multiple numbers.

## Port Request Statuses

Port requests move through the following statuses (also visible in the Mission Control portal):

- **draft** — the port request has been created but not yet submitted. Draft orders are deleted after 30 calendar days.
- **in-process** — the port request has been submitted to Telnyx and is awaiting submission to the losing provider. Generally changes within a few hours during business hours.
- **submitted** — the port request has been submitted to the losing provider and Telnyx is awaiting their response. Generally updated within 36–48 business hours of the losing provider's response.
- **exception** — the losing provider has rejected the request, typically due to a mismatch between submitted information and their records. See [Porting Error Messages](https://support.telnyx.com/en/articles/1618776-porting-error-messages).
- **foc-date-confirmed** — the losing provider has confirmed a port date. The port will activate at the specified date/time per the `foc_date` field.
- **activation-in-progress** (V2 API only) — the FOC date/time has arrived and the port and internal activation are occurring.
- **ported** — the port is complete and calls now route via Telnyx.
- **cancel-pending** — Telnyx has received a cancellation request and is informing the losing carrier. Can take up to 48 hours depending on the losing carrier.
- **cancelled** — Telnyx has received confirmation from the losing carrier that the port is cancelled.

## Checking Port Request Status

View the status of any port request in real time from the [Mission Control portal](https://portal.telnyx.com/#/login/sign-in). The Port Numbers page lists all requests with color-coded status indicators. Click **View Details** on any request to:

- Search for a particular number to view its status.
- View Sub-Requests, including status and FOC date for each.
- View and add Comments (associated with a specific Sub Request ID).

All communication regarding port requests, including supplementary document uploads, must go through the comments feature in Mission Control. Do not email for status updates or supplemental documents.

For additional help, contact the porting team at [porting@telnyx.com](mailto:porting@telnyx.com) or call [+1 312 270 8001](tel:+13122708001), available 9 AM – 5 PM Central time.

## Porting Numbers Out of Telnyx

### For Customers

To port out, initiate a port-in with your new (winning) carrier. The winning carrier will contact Telnyx to process the request.

### For Carriers

- All port-out requests must be submitted to [lnp@telnyx.com](mailto:lnp@telnyx.com). Telnyx does not accept port-outs over the phone.
- Telnyx does not provide CSRs.
- Acknowledgement for a port-out request: 3 business days.
- Simple port-out requests: typically completed in 2 business days.
- Non-simple port-out requests: considered projects; a Telnyx representative will provide an estimated completion date.

### Account Information for Port-Out

Telnyx does not hold or provide specific CSR information. To port out, use the following:

- **End-user Name** — your client's business name (or personal name for residential clients).
- **Address** — any address within the US (or specific country where the number is based).
- **BTN** — use one of the telephone numbers being ported out as the account number.
- **Account number** — Telnyx does not use account numbers; use one of the telephone numbers being ported out.
- **Always request Full Port** — Telnyx never cancels or disconnects other services on the account based on a port request from a gaining carrier.

To export a list of your DIDs, go to the [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) page and click **Export to CSV**.

Once the new carrier contacts Telnyx, you will receive an email notification with a link to view the port-out under the **Port Out** tab in your Telnyx account. See [Port Out Tracking](port-out-tracking.md) for details on approving or rejecting a port-out request.

## Number Porting Rules and Guidelines (Carrier-to-Carrier)

Telnyx LLC ports telephone numbers in accordance with applicable Regulatory Rules and Industry Guidelines (SPID: 073H). Submit a Trading Partner Profile (TPP) when submitting your first LNP request by emailing [lnp@telnyx.com](mailto:lnp@telnyx.com).

### Submitting an LSR

All LSR requests must be sent to [lnp@telnyx.com](mailto:lnp@telnyx.com). The LSR must be complete, legible, and accurate. Telnyx does not support handwritten LSRs or LSRs sent via fax.

Required LSR fields:

- Customer Carrier Name Abbreviation (CCNA)
- Purchase Order Number (PON)
- Account Number (AN)
- Desired Due Date (DDD)
- Company Code (CC)
- New Network Service Provider (NNSP)
- Agency Authority Status (AGAUTH)
- Telephone Number (Initiator) (TEL NO (INIT))
- Zip Code (ZIP)
- LOA (attached to email)
- Numbers to port (include a clean Number List alongside the LSR)

To check the status of an LSR, email Telnyx. Allow 48 hours before submitting a status request; status requests within 48 hours of receipt will not be responded to and may push the request to the back of the queue. Expedited LSRs are allowed at Telnyx's discretion. Email [lnp@telnyx.com](mailto:lnp@telnyx.com) for any changes to the LSR.

### Rejected LSRs

Telnyx provides a reject notice within 48 business hours. LSRs received after 2 PM CT are considered received on the following business day. Multi-line accounts may require project management and a longer interval.

### Firm Order Confirmation (FOC)

FOC is issued if Telnyx determines, based on LSOR standards, that the LSR has no errors or discrepancies. Telnyx does not accept same-day FOCs. FOC is valid for 10 business days; the order is canceled if the number is not activated in NPAC by the end of the third business day.

### Cancellations or Reschedules

Cancellation or reschedule requests must be received by 2 PM CST the day before the scheduled port date.

### Port Order Hours

Monday – Friday, 9:00 AM to 5:00 PM CT.

Telnyx observes the following holidays:

- New Year's Day
- Memorial Day
- Independence Day
- Labor Day
- Thanksgiving Day
- Day after Thanksgiving
- Christmas Eve Day
- Christmas Day

If a holiday falls on a Saturday, the preceding Friday is observed; if on a Sunday, the following Monday is observed. No porting is allowed on observed holidays.

### Customer Service Records (CSRs)

Telnyx does not provide CSRs.

### Escalation Contacts

- **1st Level** — Telnyx Porting Department: +1 (888) 980 9750 option 4, [lnp@telnyx.com](mailto:lnp@telnyx.com)
- **2nd Level** — Tony Rizo, LNP Team Lead: [tony@telnyx.com](mailto:tony@telnyx.com)
- **3rd Level** — Patrick Budzinski, Global Manager, Porting and Provisioning: [patrickb@telnyx.com](mailto:patrickb@telnyx.com)
