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

*Part 1 of 5 — see also: [Part 2](telnyx-number-porting-guide--part-2.md), [Part 3](telnyx-number-porting-guide--part-3.md), [Part 4](telnyx-number-porting-guide--part-4.md), [Part 5](telnyx-number-porting-guide--part-5.md)*

A consolidated reference for porting phone numbers to and from Telnyx, covering best practices, FastPort® activation, port request statuses, common error messages, SMS porting behavior, Port Out PIN protection, bundle pre-configuration, and how to contact the Porting team.

## Overview of Porting with Telnyx

Porting is a two-way transaction between the losing carrier and the winning carrier (Telnyx). Telnyx works closely with the losing carrier to ensure that lines are not released prematurely and that numbers remain active right up until they are fully ported. If issues arise before or after the FOC (Firm Order Commitment) date and time, customers should contact the Telnyx porting team immediately so the source of the issue can be identified.

A few general practices help prevent most porting issues:

- Avoid changing the FOC date once it is set. Changes are a common source of issues because some losing carriers still drop lines on the original FOC date. If a specific FOC time is desired, enter it when submitting the port request, though the losing carrier may not always accept the requested time.
- FOC date changes within 48 hours of FOC are considered best-effort requests, as the losing carrier may still drop the lines.
- Submit a Letter of Authorization (LOA), an invoice, and where possible a Customer Service Record (CSR) with the port request. A CSR can be added after the request is created in the Portal and helps validate end-user information if the losing carrier rejects the request.
- When creating the port request, assign a connection to the telephone numbers so that as soon as the numbers port to Telnyx they automatically route to the assigned connections.

When Telnyx submits the port request, the losing carrier will contact the customer to confirm. Confirming promptly speeds up the overall process.

## Port-In Requirements

Three documents are central to a port-in:

- **Letter of Authorization (LOA):** Gives Telnyx permission to request the port on behalf of the customer and end user. The LOA must list all porting numbers, customer information, and include a signature via DocuSign or physical signature. Toll-free LOAs must list "Port to RespOrg QIT02."
- **Invoice:** Proves that the end user porting the numbers is the owner. If the invoice does not list the telephone numbers, the customer can provide a screenshot of the current carrier's portal showing the numbers, or a CSR from the current carrier. If neither can be provided, contact [porting@telnyx.com](mailto:porting@telnyx.com) to discuss other ownership-proof options.
- **Customer Service Record (CSR):** Not required, but providing one helps port the number as quickly as possible. Most carriers have a record of the number, address, and billing telephone number, which is used to verify information during the porting process. Information on the CSR may differ from the billing portion of the account.

## FastPort®

FastPort® is a Telnyx feature that streamlines the porting experience from start to finish. It verifies the information entered on the LOA and alerts the customer of any incorrect information in real time, eliminating the days or weeks of back-and-forth that inaccurate information can cause with the losing carrier. Once the FOC date is confirmed and accepted by the losing carrier, FastPort® allows the customer to activate numbers at a specified date and time within an activation window.

### Activation Options

Activation is the transfer of ownership — the "handshake" — of the numbers from the losing carrier to Telnyx during the activation window. FastPort® offers two activation choices:

- **On Demand:** Activate the telephone numbers yourself within the given activation window. The activation window is available with the port request details.
- **Schedule:** Choose a specific time within the activation window by moving the scroll along the line. The numbers will auto-activate at the specified date and time.

### Activating a Port Request

- For **On Demand**, go to the port numbers page within the activation window, click *View Details* on the port request set for FOC, and click *Activate Now*. The numbers port to Telnyx within a few moments.
- For **Schedule**, numbers automatically activate at the selected date and time. To change the activation time or date within the activation window, click *Reschedule Activation* on the port request.

If the numbers are not activated manually within the window, they will auto-activate at the end of the activation window.

### FastPort® Eligibility and Fees

Telnyx does not charge port-in fees for US and Canadian numbers, and there is no change in cost for ports eligible for FastPort®. Not all carriers support real-time analysis of their records, so FastPort® is not available for every port request. Ports not eligible for FastPort® are still processed as quickly as possible.

### Changing the Scheduled Time or FOC Date

The scheduled time and date can be changed to another time within the activation window by clicking *Reschedule Activation* on the port request page. To move the date outside the activation window, contact the Porting Team to change the FOC date. The Porting Team must be contacted at least 72 hours before the scheduled FOC date. Changing the FOC date within 72 hours increases the likelihood that the losing carrier will drop the lines, resulting in the numbers being out of service.

### Correcting Information Errors

If an error is received at submission, the submitted information does not match what is on file with the losing carrier. Contact the losing carrier to verify the information, then update the port request with the corrected details. Where possible, request a CSR from the losing carrier — it is a record of all account information that can be used to dispute invalid rejections.

## Port Request Statuses

Port requests move through a defined set of statuses:

- **draft:** The port request has been created but not yet submitted. Draft orders are retained for 30 calendar days; after that they are deleted and a new order must be created.
- **in-process:** The port request has been successfully submitted to Telnyx and is waiting to be submitted to the losing provider. This status generally changes within a few hours during business hours.
- **submitted:** The port request has been successfully submitted to the losing provider and Telnyx is awaiting their response. Updates generally occur within 36–48 business hours of the losing provider's response.
- **exception:** The losing provider has rejected the port request. Something submitted differs from what is on record with the losing carrier. See [Porting Error Messages](porting-error-messages.md) for the full list of rejection reasons.
- **foc-date-confirmed:** The losing provider has provided a port confirmation date. The port will occur at the specified date/time per the `foc_date` field.
- **activation-in-progress (V2 API only):** The transition between `foc-date-confirmed` and `ported`. The FOC date/time has arrived and the port and internal activation are occurring.
- **ported:** The port request has been confirmed as ported away from the losing provider and is now with Telnyx. Calls should now route via Telnyx.
- **cancel-pending:** Telnyx has received a cancellation request and needs to inform the losing carrier. Confirmation can take up to 48 hours depending on the losing carrier.
- **cancelled:** Telnyx has received confirmation from the losing carrier that the port request has been cancelled. The losing carrier will not remove the number(s) from routing on or after the requested/confirmed porting date.

Full information on porting via API is available in the [Telnyx developer docs](https://developers.telnyx.com/docs/numbers/porting).
