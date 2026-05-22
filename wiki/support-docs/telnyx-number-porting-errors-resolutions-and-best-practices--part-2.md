---
title: 'Telnyx Number Porting: Errors, Resolutions, and Best Practices'
summary: A consolidated guide to Telnyx number porting that explains common rejection
  reasons, how to resolve them, key documents and identifiers (LOA, CSR, BTN/ATN),
  day‑of‑port readiness, port request statuses, and how to manage port‑outs from Telnyx.
sources:
- url: https://support.telnyx.com/en/articles/1130610-btn-or-atn-mismatch-error
- url: https://support.telnyx.com/en/articles/1130616-number-not-portable-tn-not-portable-error
- url: https://support.telnyx.com/en/articles/1130619-invalid-reseller-error
- url: https://support.telnyx.com/en/articles/1130623-authorized-name-mismatch-error
- url: https://support.telnyx.com/en/articles/1618776-porting-error-messages
- url: https://support.telnyx.com/en/articles/1782930-port-request-rejected
- url: https://support.telnyx.com/en/articles/2042977-porting-in-day-of-port-foc
- url: https://support.telnyx.com/en/articles/2030667-i-received-a-port-out-notification
- url: https://support.telnyx.com/en/articles/2030770-port-in-best-practices
- url: https://support.telnyx.com/en/articles/2033789-port-numbers-away-from-telnyx
- url: https://support.telnyx.com/en/articles/2047076-carrier-refusing-to-port-your-number
- url: https://support.telnyx.com/en/articles/2906030-port-out-tracking
- url: https://support.telnyx.com/en/articles/3284588-port-request-statuses
- url: https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa
updated_at: 2026-05-20T15:45:05Z
---

# Telnyx Number Porting: Errors, Resolutions, and Best Practices

*Part 2 of 2 — see also: [Part 1](telnyx-number-porting-errors-resolutions-and-best-practices--part-1.md)*

A consolidated guide to Telnyx number porting that explains common rejection reasons, how to resolve them, key documents and identifiers (LOA, CSR, BTN/ATN), day‑of‑port readiness, port request statuses, and how to manage port‑outs from Telnyx.

## Port request lifecycle and statuses
- draft: Order created, not yet submitted to Telnyx. Drafts older than 30 calendar days are auto‑deleted.
- in‑process: Submitted to Telnyx and pending submission to the losing carrier.
- submitted: Delivered to the losing carrier; awaiting their response (updates typically within ~36–48 business hours after carrier reply).
- exception: Losing carrier rejected the request (mismatch or other error). Correct data per the rejection reason list and resubmit.
- foc‑date‑confirmed: Losing carrier confirmed the activation date/time.
- activation‑in‑progress (V2 API): The FOC window has arrived and activation/port cutover is underway.
- ported: Activation confirmed; calls should now route via Telnyx.
- cancel‑pending: Telnyx received your cancellation; awaiting losing‑carrier confirmation (can take up to 48 hours depending on carrier).
- cancelled: Losing carrier confirmed cancellation; the port will not occur.

## When a carrier resists or delays your port
- Verify everything against the CSR: Most rejections trace back to simple mismatches. Correcting data up front saves weeks.
- Call instead of only emailing: Many carriers provide faster updates over the phone for porting cases.
- Know your rights: The FCC provides detailed guidance on number portability; understanding it can help resolve disputes. See https://www.fcc.gov/consumers/guides/porting-keeping-your-phone-number-when-you-change-providers

## Managing port‑outs from Telnyx
- Information to give your new (gaining) carrier:
  - End‑user name: Business or residential name.
  - Address: Any valid address within the TN’s country (for US numbers, any US address).
  - BTN / Account number: Telnyx doesn’t use separate account numbers—use one of the TNs being ported as the BTN/account number.
  - Request a Full Port: Telnyx will not cancel or disconnect other services based solely on a gaining‑carrier port request.
- CSR note: Telnyx does not hold or provide CSR data. If the new carrier requires CSR info, they must proceed without it or the end user must provide alternate proof.
- Exporting your numbers: In the portal under My Numbers, you can export your DIDs to CSV for reference.
- Notifications and timing:
  - Telnyx creates a Port‑Out request upon receipt from the gaining carrier and notifies the account owner by email (webhooks available). You can adjust notification recipients/permissions in the portal.
  - Please acknowledge within 24–48 hours. If you approve, status moves to Authorized and Telnyx notifies the gaining carrier. If you reject, you must provide a valid reason; withholding numbers for non‑regulatory reasons (e.g., billing disputes) is not allowed. Invalid rejections may be overridden and FOC provided.
  - No acknowledgment auto‑approves the port‑out.
  - FOC changes from the gaining carrier trigger a webhook. The gaining carrier has a 10‑day grace window after the listed FOC date to complete the port‑out.
- Completion and fees:
  - Once port‑out is confirmed, numbers are removed from your account immediately.
  - Port‑out fees apply as per your pricing; see your account’s Pricing section or contact sales if you have questions.

## Support and escalation
- Telnyx Porting team: porting@telnyx.com
- Telnyx LNP (port‑out inquiries): lnp@telnyx.com
- Use your Mission Control Portal to: create/track port‑ins, assign connections, monitor port‑outs, manage permissions for who can view/act on porting requests.
