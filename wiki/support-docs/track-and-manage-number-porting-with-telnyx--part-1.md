---
title: Track and Manage Number Porting with Telnyx
summary: Learn how to check the real-time status of your port requests in Mission
  Control, submit ports with the right documents, use automated validation and FastPort,
  follow best practices, understand timelines, handle port-outs, and know when PINs/CSRs
  are needed.
sources:
- url: https://support.telnyx.com/en/articles/1130633-checking-a-port-request-status
- url: https://support.telnyx.com/en/articles/1130634-port-numbers-to-telnyx
- url: https://support.telnyx.com/en/articles/1130635-can-i-port-out-my-telnyx-number
- url: https://support.telnyx.com/en/articles/1130630-porting-policy-procedure
- url: https://support.telnyx.com/en/articles/1130626-international-number-porting-required-documents
- url: https://support.telnyx.com/en/articles/1516776-automated-port-request-validation
- url: https://support.telnyx.com/en/articles/2021334-your-guide-to-fastport
- url: https://support.telnyx.com/en/articles/2030770-port-in-best-practices
- url: https://support.telnyx.com/en/articles/2033789-port-numbers-away-from-telnyx
- url: https://support.telnyx.com/en/articles/14790558-how-to-find-your-porting-pin-or-passcode
- url: https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier
updated_at: 2026-05-14T11:31:37Z
---

# Track and Manage Number Porting with Telnyx

*Part 1 of 2 — see also: [Part 2](track-and-manage-number-porting-with-telnyx--part-2.md)*

Learn how to check the real-time status of your port requests in Mission Control, submit ports with the right documents, use automated validation and FastPort, follow best practices, understand timelines, handle port-outs, and know when PINs/CSRs are needed.

## Porting overview and where to track status
Number porting lets you keep existing phone numbers when switching providers. You can submit and manage ports in the Mission Control portal and see real-time status updates for every request. Use the Port Numbers area to start a new request, check portability, and monitor progress. If a number isn’t in Telnyx inventory, you can request it separately. For API-based workflows, the Mission Control API also supports porting.

- Mission Control login: https://portal.telnyx.com/#/login/sign-in
- Start a new port request / portability check: https://portal.telnyx.com/#/app/numbers/port-numbers/new
- View all port requests: https://portal.telnyx.com/#/app/numbers/port-numbers?status=both

## Checking porting status in Mission Control
From REAL-TIME COMMUNICATIONS → NUMBERS → PORT NUMBERS you can:
- See color-coded port statuses at a glance.
- Click View Details to open Porting Request Details, where you can:
  - Search specific numbers and see their status.
  - Review sub-requests (grouped by underlying carrier), each with its own status and FOC date.
  - Read and post Comments (threaded per sub-request) to provide updates or respond to Telnyx.

Tip: Use the Comments in Mission Control for all request-related communication and supplemental uploads so everything is tracked alongside your ticket.

## Status lifecycle, FOC, and timelines
- Automated updates: You’ll receive email notifications as your request progresses. Real-time status is always in Mission Control.
- FOC (Firm Order Commitment): Telnyx notifies you when the losing carrier approves. Numbers activate on the assigned FOC date/time. Most US ports allow 24/5 activations (Mon–Fri). In rare cases, activation must occur during business hours.
- SLA guidelines (estimates, not guarantees until FOC):
  - Simple ports (generally single-line accounts, <20 numbers, no complex translations, no reseller): submitted to losing carrier within 2 business days; typical completion ~7 business days.
  - Non-simple ports (>20 numbers, multi-line, complex features): submitted within 4 business days; typical completion ~15 business days or more; may require project management.
- Processing window: Telnyx accepts submissions 24/7/365, but processing/submission occurs Mon–Fri, 9am–5pm CT. US porting holidays observed: New Year’s Day, Memorial Day, Independence Day, Labor Day, Thanksgiving Day, Christmas Day. Around major holidays, other carriers’ schedules may extend timelines.

## Submitting a port-in request (portal flow)
- Navigate to REAL-TIME COMMUNICATIONS → NUMBERS → PORT NUMBERS → New Port Request.
- Specify whether the numbers are yours or your customer’s and select the country. Split requests by country.
- Enter numbers (comma- or line-separated). Supported formats include NPANXXYYYY, 1NPANXXYYYY, NPA-NXX-YYYY, and 1-NPA-NXX-YYYY.
- Click Check Portability. Non-portable numbers can be removed in bulk. For some international cases flagged as ineligible, email porting@telnyx.com to confirm manual options.
- Provide Account Information matching the losing carrier’s service address and the Authorized Person’s Name on file (for resellers, use the end customer details from the CSR).
- Upload required documents: a signed LOA listing all numbers and customer info (wet or e-signature accepted) and a recent bill/invoice from the current carrier. Country-specific requirements will appear automatically when applicable.
- Assign a default Connection so numbers route immediately upon activation.
- You may request a FOC date/time; carriers may not always honor it. Expedites are case-by-case and must be approved by Telnyx.

## Automated validation and CSRs
Telnyx can automatically validate your request against the losing carrier when supported:
- If the carrier supports automated CSR validation, Telnyx requests data using your BTN, account number, end-customer name, and service address. Responses can take up to ~30 minutes.
- If submitted data matches, Telnyx proceeds to final submission. If not, the request moves to Exception status and you’ll be notified. Update fields via the request’s Comments and Telnyx will re-check and proceed.
- Only major carriers currently support this automation (e.g., Level 3, AT&T, CenturyLink), with more added over time. For privacy reasons, Telnyx can’t disclose corrected data—only whether it matches.

About CSRs:
- A CSR shows how your account appears in the carrier’s database and is the best way to ensure your data matches for porting. Uploading a CSR can significantly reduce delays.
- How to obtain a CSR: Call your current carrier and request it via email; then upload to Mission Control. US-focused; many Canadian carriers won’t provide CSRs to other carriers. Learn more: https://support.telnyx.com/en/articles/1130614-obtaining-a-csr-from-your-carrier

## International porting documentation
When submitting international ports in the portal, provide an LOA and invoice initially. After Telnyx confirms coverage and portability with the carrier, the team will advise next steps and any country-specific documents required. See country lists and required document types: https://support.telnyx.com/en/articles/1130626-international-number-porting-required-documents

## FastPort and activation options
FastPort streamlines porting by verifying LOA details in real time and, once FOC is set, lets you choose how to activate:
- On Demand: You manually trigger activation within the allowed activation window.
- Schedule: You pre-select a specific date/time within the activation window and numbers auto-activate then.
More details: https://support.telnyx.com/en/articles/2054704-fastport-faqs

## Port-in best practices
- Avoid changing the FOC date once set. Changes—especially within 48 hours of FOC—are best-effort and can cause the losing carrier to drop lines on the original date.
- Always upload a complete, correctly signed LOA and a recent invoice. Add a CSR when available to validate end-user details.
- Assign your Connection during request creation so numbers route immediately at cutover.
- If the losing carrier contacts you to confirm the port, respond promptly to speed up processing.
- If issues arise before or after FOC, contact Telnyx porting support immediately.

## Porting PIN or passcode requirements
Some carriers require a porting PIN/passcode. If the PIN is wrong, ports are rejected with PASSCODE_PIN_INVALID.
- Get the correct PIN from your carrier (often via account portal or by calling 611 for mobile). Some carriers generate time-limited transfer PINs.
- Don’t reuse old PINs; verify the one on file if rejections persist.
- Tips and carrier-specific steps: https://support.telnyx.com/en/articles/14790558-how-to-find-your-porting-pin-or-passcode

## Porting numbers away from Telnyx (port-out)
- Customers: Initiate a port with your new (winning) carrier. They’ll contact Telnyx to process the port-out.
- Account info for the new carrier (find in Mission Control → Account information):
  - End-user Name: Your client’s business/personal name
  - Address: Any valid address within the number’s country (US for US numbers)
  - BTN/Account number: Use one of the numbers being ported out (Telnyx doesn’t use separate account numbers)
  - Always request a Full Port. Telnyx doesn’t cancel other services based on a port-out request.
- Export your DIDs if needed: My Numbers → Export to CSV.
- Carriers: Submit port-out requests to lnp@telnyx.com (not by phone). Telnyx doesn’t provide CSRs. Acknowledgement in ~3 business days. Simple port-outs typically complete in ~2 business days; non-simple become projects with an ETA provided.
- You’ll receive an email when Telnyx is notified of your port-out. Manage approvals in the Port Out tab. Learn more: https://support.telnyx.com/en/articles/2906030-port-out-tracking
