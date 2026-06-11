---
title: Number Porting
summary: Telnyx supports local number portability (LNP) for moving phone numbers between
  carriers. This page covers the full porting lifecycle including port-in and port-out
  procedures, required documents, FastPort®, automated validation, auto-generated
  LOAs, porting bundles, SLA timelines, and reseller-specific guidance.
sources:
- url: https://support.telnyx.com/en/articles/1130626-international-number-porting-required-documents
- url: https://support.telnyx.com/en/articles/1130630-porting-policy-procedure
- url: https://support.telnyx.com/en/articles/1130633-checking-a-port-request-status
- url: https://support.telnyx.com/en/articles/1130634-port-numbers-to-telnyx
- url: https://support.telnyx.com/en/articles/1130635-can-i-port-out-my-telnyx-number
- url: https://support.telnyx.com/en/articles/1516776-automated-port-request-validation
- url: https://support.telnyx.com/en/articles/2021334-your-guide-to-fastport
- url: https://support.telnyx.com/en/articles/2030770-port-in-best-practices
- url: https://support.telnyx.com/en/articles/2033789-port-numbers-away-from-telnyx
- url: https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa
- url: https://support.telnyx.com/en/articles/2042977-porting-in-day-of-port-foc
- url: https://support.telnyx.com/en/articles/2054704-fastport-faqs
- url: https://support.telnyx.com/en/articles/2086149-number-porting-rules-and-guidelines
- url: https://support.telnyx.com/en/articles/3284588-port-request-statuses
- url: https://support.telnyx.com/en/articles/3561993-using-telnyx-fastport
- url: https://support.telnyx.com/en/articles/6460777-porting-requirements
- url: https://support.telnyx.com/en/articles/8268276-loa-template-download
- url: https://support.telnyx.com/en/articles/8588086-auto-generated-letter-of-authorization-loa
- url: https://support.telnyx.com/en/articles/8709331-porting-bundles
updated_at: 2026-06-11T11:12:38Z
---

# Number Porting

*Part 2 of 3 — see also: [Part 1](number-porting--part-1.md), [Part 3](number-porting--part-3.md)*

Telnyx supports local number portability (LNP) for moving phone numbers between carriers. This page covers the full porting lifecycle including port-in and port-out procedures, required documents, FastPort®, automated validation, auto-generated LOAs, porting bundles, SLA timelines, and reseller-specific guidance.

## Automated Port Request Validation

Telnyx can automatically validate port request information with the losing carrier:

1. When a port request is submitted, Telnyx checks if the losing carrier supports automated CSR validation.
2. If supported, Telnyx requests a CSR using the BTN, account number, end customer name, and service address. This can take up to 30 minutes.
3. If the information matches, Telnyx proceeds with the final port submission.
4. If the information does not match, the request enters **Exception** status and you are notified of the errors. You can correct the fields through the comments feature, and Telnyx will resubmit.

Key notes:

- Only major carriers (such as Level 3, AT&T, and CenturyLink) currently support automated validation; Telnyx regularly adds more.
- If the submitted data is materially different from what is on file, the carrier may not return any data at all (typically due to incorrect BTN, account number, or service address).
- For privacy reasons, Telnyx cannot share the corrected data — it can only confirm whether the data matched.
- Even if validation fails, Telnyx continues working on the port request and will notify you if further action is needed.

## SLA Guidelines and Timelines

### Simple Ports

As defined by the FCC, a simple port: (1) does not involve unbundled network elements, (2) involves a single-line account only, (3) does not include complex switch translations (Centrex, ISDN, AIN, remote call forwarding, or multiple services on the loop/line), and (4) does not include a reseller. These are typically ports with fewer than 20 numbers.

- Submission to losing carrier: within 2 business days
- Estimated completion: 7 business days

### Non-Simple Ports

Any port that does not qualify as a simple port — including ports with more than 20 numbers and multi-line accounts — may require project management.

- Submission to losing carrier: within 4 business days
- Estimated completion: 15 business days or more

Telnyx cannot guarantee completion on a specific date until you receive a FOC. Porting requests are only processed Monday through Friday, 9 AM – 5 PM CT.

### US Porting Holidays

- New Year's Day
- Memorial Day
- Independence Day
- Labor Day
- Thanksgiving Day
- Christmas Day

Other providers may observe additional holidays (e.g., day after Thanksgiving, Christmas Eve), which can cause slight delays around major US holidays.

## Common Causes of Porting Exceptions and Delays

- Incorrect spelling of the end customer name (e.g., submitted "Alpha Corp" instead of "Alpha Beta Inc").
- Incorrect service address (wrong street name or zip code).
- Bundling multiple end-customer numbers under a single port request.
- One or more of the telephone numbers is inactive.
- Not providing an account number.
- LOA not signed, signature older than 90 days, or missing information.
- Name or address mismatch with carrier records.

If an exception occurs, you will be notified by email. If you do not respond within 14 days, the port request will be cancelled. Depending on the nature of the exception, resubmission to the losing carrier may be required, and some carriers treat this as an entirely new request.

## Reseller Instructions

If your company name and service address are not listed on the CSR with the current carrier, Telnyx considers you a reseller. Resellers must follow these rules:

- You must be authorized to act on behalf of your end customer. Submit an LOA signed by the end customer whenever possible.
- Telnyx may request a copy of your Master Services Agreement with the customer stipulating your right to change carriers.
- Telnyx has the right to request a signed LOA from the customer at any time.
- You must create separate port requests for each customer and each service address.
- Use your end customer's information on the LOA and port request — not your business information.

## Day of Port (FOC)

On the FOC date, take these steps to ensure readiness:

1. Ensure a connection has been assigned to all numbers being ported.
2. Ensure your internal systems or hardware are configured and ready.

There may be slight delays during unusually high volumes. If timing is critical, inform the porting team a few days before the FOC date.

It is best not to change the FOC date once set. FOC date changes within 48 hours of the port are considered best-effort requests, as the losing carrier may still drop the lines.

US ports generally allow 24/5 activations (Monday–Friday). In rare cases, Telnyx must manually activate numbers during business hours.

A note that may appear during the port process: numbers may show "Not SMS Capable" before activation. All US numbers are SMS capable, and this status will update once the port activates.

## Porting Numbers Away from Telnyx

### For Customers

Simply initiate a port-in request with your new carrier. The new carrier will contact Telnyx to process the request.

### For Carriers

- All port-out requests must be submitted to lnp@telnyx.com. Telnyx does not accept port-outs over the phone.
- Telnyx does not provide CSRs.
- Acknowledgement for a port-out request is 3 business days.
- Simple port-out requests can typically be completed in 2 business days.
- Non-simple port-outs are considered projects; a Telnyx representative will provide an estimated completion date.

### Account Information for Porting Out

When submitting a port-out to a new carrier, use the following:

- **End-user Name:** Your client's business name (or personal name for residential clients).
- **Address:** Any address within the US (or the number's country).
- **BTN:** One of the telephone numbers being ported out.
- **Account Number:** Telnyx does not use account numbers — use one of the telephone numbers being ported out as the account number.
- Always request a full port; Telnyx never cancels or disconnects other services based on a port-out request.

You can export a list of your DIDs from the **My Numbers** page using the **Export to CSV** button. When a new carrier contacts Telnyx about your port-out, you will be notified via email with a link to view the port-out under the **Port Out** tab.
