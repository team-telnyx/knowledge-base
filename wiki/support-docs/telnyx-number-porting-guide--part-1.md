---
title: Telnyx Number Porting Guide
summary: A comprehensive guide to porting telephone numbers to and from Telnyx, covering
  port-in best practices, FastPort® activation, common porting error messages, BTN/ATN
  mismatch resolution, porting PINs and passcodes, port-out notifications and tracking,
  Port Out PIN Protection, bundle pricing and pre-configuration, and best practices
  for contacting Telnyx support and the porting team.
sources:
- url: https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error
- url: https://support.telnyx.com/en/articles/14790558-how-to-find-your-porting-pin-or-passcode
- url: https://support.telnyx.com/en/articles/1618776-porting-error-messages
- url: https://support.telnyx.com/en/articles/2021334-your-guide-to-fastport
- url: https://support.telnyx.com/en/articles/2030667-i-received-a-port-out-notification
- url: https://support.telnyx.com/en/articles/2030770-port-in-best-practices
- url: https://support.telnyx.com/en/articles/2042977-porting-in-day-of-port-foc
- url: https://support.telnyx.com/en/articles/2054704-fastport-faqs
- url: https://support.telnyx.com/en/articles/2906030-port-out-tracking
- url: https://support.telnyx.com/en/articles/3561993-using-telnyx-fastport
- url: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
- url: https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting
- url: https://support.telnyx.com/en/articles/8006189-port-out-pin-protection
- url: https://support.telnyx.com/en/articles/8340760-bundles-bundle-pricing
- url: https://support.telnyx.com/en/articles/8709331-porting-bundles
updated_at: 2026-07-17T09:02:30Z
---

# Telnyx Number Porting Guide

*Part 1 of 4 — see also: [Part 2](telnyx-number-porting-guide--part-2.md), [Part 3](telnyx-number-porting-guide--part-3.md), [Part 4](telnyx-number-porting-guide--part-4.md)*

A comprehensive guide to porting telephone numbers to and from Telnyx, covering port-in best practices, FastPort® activation, common porting error messages, BTN/ATN mismatch resolution, porting PINs and passcodes, port-out notifications and tracking, Port Out PIN Protection, bundle pricing and pre-configuration, and best practices for contacting Telnyx support and the porting team.

## Porting Overview and Best Practices

Porting is a two-way transaction between the losing carrier and the winning carrier (Telnyx). Telnyx works closely with the losing carrier to ensure that lines are not released prematurely and remain active until fully ported. If issues arise before or after the FOC (Firm Order Commitment) date, contact the Telnyx porting team immediately to investigate.

Key best practices to prevent issues:

- Once an FOC date is set, avoid changing it whenever possible. Some losing carriers still drop lines on the original FOC date. If a change is necessary, submit it well in advance.
- FOC date changes within 48 hours of FOC are considered best-effort requests, as the losing carrier may still drop the lines.
- When submitting a port request, include a Letter of Authorization (LOA), an invoice, and where possible, a Customer Service Record (CSR). A CSR can be added after the port request has been created within the Portal and helps validate end-user information if the losing carrier rejects the request for invalid information.
- When creating the port request, assign a connection to the telephone numbers so that as soon as the numbers are ported to Telnyx, they automatically route to the assigned connections.
- When Telnyx submits the port request, the losing carrier will contact the customer to confirm. Respond to the losing carrier as soon as possible to speed up the process.

### Port-In Requirements

- **Letter of Authorization (LOA):** Authorizes Telnyx to act on behalf of the client and request the port. The LOA must list all porting numbers, customer information, and include a signature via DocuSign or physical signature. Toll-free LOAs must list "Port to RespOrg QIT02."
- **Invoice:** Proves that the end user porting the numbers is the owner. If the invoice does not list the telephone numbers, the customer can provide a screenshot of the current carrier's portal showing the numbers, or a CSR from the current carrier. If neither can be provided, contact porting@telnyx.com to discuss other options.
- **Customer Service Record (CSR):** Not required, but providing a CSR helps port the number as quickly as possible. Most carriers have a record of the number, address, and billing telephone number, which is used to verify information during the porting process. Note that the information on the CSR may differ from the billing portion of the account.

## FastPort®

FastPort® is a Telnyx feature that streamlines the porting experience from start to finish. It verifies the information entered on the LOA and alerts the customer of any incorrect information in real time, eliminating the days or weeks of delays that inaccurate information can cause. Once the FOC date is confirmed and accepted by the losing carrier, FastPort® allows the customer to activate numbers at a specified date and time within an activation window.

### Activation Options

Activation is the transfer of ownership, or "handshake," of numbers from the losing carrier to Telnyx during the activation window. FastPort® offers two activation choices:

- **On Demand:** Activate the telephone numbers yourself within the given activation window. The activation window is available with the port request details.
- **Schedule:** Choose a specific time within the activation window to activate the numbers. The numbers will auto-activate at the specified date and time.

### How to Activate

- **On Demand:** Go to the port numbers page within the activation window, click *View Details* on the port request set for FOC, and click *Activate Now*. Numbers will port to Telnyx within moments.
- **Schedule:** Numbers automatically activate at the specified date and time. To change the activation time or date within the activation window, select *Reschedule Activation* on the port request.

If numbers are not activated manually within the window, they will auto-activate at the end of the activation window.

### FastPort® FAQs

- **Error at submission:** If an error is received at submission, the submitted information does not match what is on file with the losing carrier. Contact the losing carrier to verify the information, then update the port request. Requesting a CSR is highly advised, as it can be used to dispute invalid rejections.
- **Fees:** Telnyx does not charge port-in fees for US and Canadian numbers, including those eligible for FastPort®.
- **Changing scheduled time/date:** Click *Reschedule Activation* on the port request page to change to another time within the activation window. To move outside the activation window, contact the Porting Team at least 72 hours before the scheduled FOC date. Changes within 72 hours increase the likelihood that the losing carrier will drop the lines.
- **Eligibility:** Not all carriers support real-time analysis of their records, so FastPort® is not available for every port request. Ports not eligible for FastPort® are still processed as quickly as possible.

## Day of Port (FOC)

On the day numbers are set to be ported, run the following checks:

1. Ensure a connection has been assigned to all numbers set to be ported.
2. Ensure internal systems or hardware are set up and ready at the time of the port.

There may be a slight delay in porting time. Telnyx works to port numbers as close to the FOC time as possible, but high volumes may cause slight delays. If numbers must be ported as close to the FOC time as possible, inform the porting team a few days before the scheduled port.

During the port process, the Customer Portal may show "Not SMS Capable" beside pending numbers. All US numbers are SMS capable, and this status will update during activation of the port request.
