---
title: Number Porting with Telnyx
summary: A consolidated reference for porting phone numbers into and out of Telnyx,
  covering port-in procedures, SLA timelines, automated validation, status tracking,
  port-out handling, reseller and carrier-specific guidance, and programmatic API
  automation.
sources:
- url: https://support.telnyx.com/en/articles/1130630-porting-policy-procedure
- url: https://support.telnyx.com/en/articles/1130633-checking-a-port-request-status
- url: https://support.telnyx.com/en/articles/1130634-port-numbers-to-telnyx
- url: https://support.telnyx.com/en/articles/1130635-can-i-port-out-my-telnyx-number
- url: https://support.telnyx.com/en/articles/14708128-porting-numbers-away-from-aircall-to-telnyx
- url: https://support.telnyx.com/en/articles/14708129-porting-numbers-away-from-intercom-to-telnyx
- url: https://support.telnyx.com/en/articles/1516776-automated-port-request-validation
- url: https://support.telnyx.com/en/articles/1782930-port-request-rejected
- url: https://support.telnyx.com/en/articles/2030667-i-received-a-port-out-notification
- url: https://support.telnyx.com/en/articles/2033789-port-numbers-away-from-telnyx
- url: https://support.telnyx.com/en/articles/2047076-carrier-refusing-to-port-your-number
- url: https://support.telnyx.com/en/articles/2086149-number-porting-rules-and-guidelines
- url: https://support.telnyx.com/en/articles/2906030-port-out-tracking
- url: https://support.telnyx.com/en/articles/3947875-porting-away-from-bandwidth
- url: https://support.telnyx.com/en/articles/5386351-automating-ports-with-programmatic-api
updated_at: 2026-08-05T13:28:43Z
---

# Number Porting with Telnyx

*Part 3 of 3 — see also: [Part 1](number-porting-with-telnyx--part-1.md), [Part 2](number-porting-with-telnyx--part-2.md)*

A consolidated reference for porting phone numbers into and out of Telnyx, covering port-in procedures, SLA timelines, automated validation, status tracking, port-out handling, reseller and carrier-specific guidance, and programmatic API automation.

## Checking Port Request Status

Port request status is visible in real time in the [Mission Control portal](https://portal.telnyx.com/#/login/sign-in) under the **PORT NUMBERS** tab. Numbers are color-coded by status. Clicking **View Details** on a request opens the **Porting Request Details** page, where you can:

- Search for a particular number to view its status.
- View Sub Requests, including each sub-request's status and FOC date.
- View and add Comments (associated with a specific Sub Request ID).

Automated update emails are sent as the request is processed. All communication regarding port requests, including supplemental document uploads, must go through the comments feature in Mission Control rather than email. The Porting Experts can be reached at [porting@telnyx.com](mailto:porting@telnyx.com) or +1 312 270 8001, 9 AM–5 PM Central time.

## Port Request Rejections

A port request may be rejected by the losing carrier due to information mismatch. To minimize rejections, request a CSR from the losing carrier upfront and compare it to the LOA before submitting. If a rejection occurs, Telnyx can use the CSR to dispute the rejection with the losing carrier. See [Porting Error Messages](porting-error-messages.md) for a full list of error messages. Questions about a specific rejection can be raised by commenting on the port request in the Portal or emailing [porting@telnyx.com](mailto:porting@telnyx.com).

If a carrier is refusing to port a number, common remedies include verifying that all submitted information is correct, calling the provider directly for faster responses, and familiarizing yourself with the [FCC's number porting guidelines](https://www.fcc.gov/consumers/guides/porting-keeping-your-phone-number-when-you-change-providers).

## Porting Numbers Away From Telnyx

### For Customers

To port out, initiate a port-in with the new (gaining) carrier. The gaining carrier will contact Telnyx to process the request. Telnyx does not hold or provide Customer Service Record (CSR) information.

The following information can be used when submitting to the new carrier (available on the [Account information](https://portal.telnyx.com/#/app/account/general) page):

- **End-user Name:** The client's business name (or personal name for residential clients).
- **Address:** Any address within the US (or the country where the number is based).
- **BTN / Account Number:** Telnyx does not use account numbers; use one of the telephone numbers being ported out as the account number.
- **Always request Full Port:** Telnyx never cancels or disconnects other services on the account based on a port request.

To export a list of DIDs for the new carrier, go to [My Numbers](https://portal.telnyx.com/#/app/numbers/my-numbers) and click **Export to CSV**.

### For Carriers

All port-out requests must be submitted to [lnp@telnyx.com](mailto:lnp@telnyx.com). Telnyx does not accept port-outs over the phone and does not provide CSRs. Acknowledgement of a port-out request is provided within 3 business days. Simple port-out requests typically complete in 2 business days; non-simple port-outs are treated as projects and a Telnyx representative will provide an estimated completion date.

### Port-Out Notifications and Tracking

When Telnyx receives a port-out request, an email notification (and webhook, if configured) is sent to the account owner. Customers should respond within 24–48 hours. If the numbers should not be ported out, the request must be rejected with a valid reason within the given timeframe. Resellers and service providers are responsible for confirming with their end user before responding.

The **Port Out** tab in Mission Control lists all port-out requests with status, FOC date, total TNs, request details, and winning carrier name. Requests can be filtered by status (`complete` or `incomplete`) and searched by telephone number or Request # (e.g., `PO_a24719`).

![Port out details in the port out tab.](_images/df4a98516a294783.png)

Clicking a request shows the submitted information, status, winning carrier, requested FOC date, and TNs in the request.

![Port out details in the port out tab.](_images/5144cd31f51fadf1.png)

- **Accepting:** Status moves from `Pending` to `Authorized` and Telnyx notifies the gaining carrier.
- **Rejecting:** A valid and reasonable reason is required. If the reason is deemed invalid, the number will be ported out. Numbers cannot be withheld without proper authority or for billing/payment issues.
- **No acknowledgment:** If neither approved nor rejected, the port is automatically approved and the gaining carrier is notified.
- **FOC date changes:** A webhook notification is sent if the gaining carrier requests a FOC date change. The gaining carrier has a 10-day grace period after the FOC date to complete the port.
- **Completed port-outs:** Once confirmed, the request shows `Ported Out` and the number is removed from the account immediately. The port-out fee is billed at that time and can be reviewed in the [Pricing](https://portal.telnyx.com/#/app/pricing) section. Questions about port-out fees can be sent to [sales@telnyx.com](mailto:sales@telnyx.com).

## LSR Submissions (Carrier-to-Carrier)

Carriers submitting Local Service Requests (LSRs) to Telnyx must email [lnp@telnyx.com](mailto:lnp@telnyx.com). A Trading Partner Profile (TPP) should be submitted with the first LNP request. LSRs must be complete, legible, and accurate; handwritten LSRs and LSRs sent via fax are not supported.

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
- Numbers to port (include a clean number list alongside the LSR)

Status requests should be emailed and will be responded to within 48 hours; please allow 48 hours before submitting a status request. Telnyx will not respond to status updates within 48 hours of receiving the LSR, and status requests may push the request to the back of the queue. Expedited LSRs are allowed at Telnyx's discretion.

For non-simple ports, all telephone numbers must be listed on a separate, clean sheet of the LSR in 10-digit format. Telnyx provides a reject notice within 48 business hours; LSRs received after 2 PM CT are considered received the following business day. FOC is issued if the LSR has no errors or discrepancies per LSOR standards. Telnyx does not accept same-day FOCs. FOC is valid for 10 business days; the order is canceled if the number is not activated in NPAC by the end of the third business day. Cancellation or reschedule requests must be received by 2 PM CST the day before the scheduled port date.

Port order hours are Monday–Friday, 9:00 AM–5:00 PM CT. Telnyx observes New Year's Day, Memorial Day, Independence Day, Labor Day, Thanksgiving Day, the day after Thanksgiving, Christmas Eve Day, and Christmas Day. If a holiday falls on a Saturday, the preceding Friday is observed; if on a Sunday, the following Monday is observed. No porting is allowed on observed holidays.

## Escalation Contacts

- **1st Level:** Telnyx Porting Department — +1 (888) 980 9750 option 4, [lnp@telnyx.com](mailto:lnp@telnyx.com)
- **2nd Level:** Tony Rizo, LNP Team Lead — [tony@telnyx.com](mailto:tony@telnyx.com)
- **3rd Level:** Patrick Budzinski, Global Manager, Porting and Provisioning — [patrickb@telnyx.com](mailto:patrickb@telnyx.com)
