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

*Part 2 of 3 — see also: [Part 1](number-porting-with-telnyx--part-1.md), [Part 3](number-porting-with-telnyx--part-3.md)*

A consolidated reference for porting phone numbers into and out of Telnyx, covering port-in procedures, SLA timelines, automated validation, status tracking, port-out handling, reseller and carrier-specific guidance, and programmatic API automation.

## Porting Numbers Into Telnyx

### Submitting a Port-In Request

Port-in requests are submitted through the [Port Numbers](https://portal.telnyx.com/#/app/numbers/port-numbers) page in Mission Control. To begin, log in, navigate to **REAL-TIME COMMUNICATIONS → NUMBERS → PORT NUMBERS**, and click **New Port Request**.

1. Choose whether the numbers are your own or belong to a customer (reseller/service provider).
2. Select the country for the numbers. Port requests must be split by country.
3. Enter the numbers manually or paste from a CSV/Excel file. Supported formats include `NPANXXYYYY`, `1NPANXXYYYY`, `NPA-NXX-YYYY`, and `1-NPA-NXX-YYYY`.
4. Click **Check Portability**. Non-portable numbers can be removed with **Remove All Non Portable**. If an international number is flagged as not eligible, email [porting@telnyx.com](mailto:porting@telnyx.com) to confirm whether it can be ported manually.
5. Enter account information. The service address must match the billing address on file with the current provider, and the Authorized Person's Name must match the carrier's records.
6. Upload supporting documents: a signed Letter of Authorization (LOA) and the most recent bill/CSR from the existing carrier. The LOA must list all numbers porting, the customer information, and either a wet signature or a valid e-signature (e.g., DocuSign).
7. Choose a default Connection to use once the port completes.
8. Optionally request a Firm Order Commitment (FOC) date. The Portal will display available activation date/time options; in rare cases Telnyx must manually activate numbers during business hours.

After submission, the request is broken into **Sub Requests** grouped by underlying carrier to expedite processing. Expedited requests are handled case-by-case and require explicit Telnyx approval.

### Required Documents

For each port request, Telnyx requires:

- An LOA signed by the end customer, with the signer matching the existing carrier's records.
- The most recent bill copy (or CSR) from the existing carrier.

Country-specific documentation requirements are automatically displayed in the Portal after portability is checked.

### Automated Port Request Validation

Telnyx can automatically validate port request data with the losing carrier when supported (e.g., Level 3, AT&T, CenturyLink). The flow is:

1. Telnyx requests a CSR using the Billing Telephone Number (BTN), account number, end customer name, and service address. This can take up to 30 minutes.
2. Submitted data is matched against the returned CSR.
3. If data matches, the Porting Team proceeds with final submission to the losing carrier.
4. If data does not match, the request moves to **Exception** status and the customer is notified. Customers can correct fields via the comments feature and Telnyx will resubmit.

Telnyx cannot share the corrected CSR data for privacy reasons; only whether the data matched. If validation fails, Telnyx continues working on the request and will reach out if customer action is needed.

### SLA Guidelines and Timelines

Telnyx aims to process port requests quickly but cannot guarantee a specific completion date until FOC is received.

- **Simple ports** (per FCC definition: no unbundled network elements, single-line account, no complex switch translations, no reseller; typically fewer than 20 numbers):
  - Submission to losing carrier: within 2 business days
  - Estimated completion: 7 business days
- **Non-simple ports** (more than 20 numbers, multi-line accounts, or anything not meeting the simple-port criteria):
  - Submission to losing carrier: within 4 business days
  - Estimated completion: 15 business days or more

Port requests are accepted 24/7/365 but processed Monday–Friday, 9 AM–5 PM CT. Telnyx observes the following US porting holidays: New Year's Day, Memorial Day, Independence Day, Labor Day, Thanksgiving Day, and Christmas Day. Ports around major US holidays may be slightly delayed.

### Common Causes of Porting Exceptions and Delays

- Incorrect spelling of the end customer name (e.g., "Alpha Corp" instead of "Alpha Beta Inc").
- Incorrect service address (wrong street name or zip code).
- Bundling multiple end-customer numbers under a single port request.
- One or more submitted telephone numbers is inactive.
- Missing account number.

If an exception occurs, the customer is notified by email. Some exceptions require resubmission to the losing carrier, which may restart the response clock. If Telnyx does not receive a response within 14 days, the port request is canceled and a new request can be submitted with corrected information.

### Special Instructions for Resellers

If the requesting company name and service address are not on the CSR with the current carrier, Telnyx treats the requester as a reseller. Resellers must:

- Be authorized to act on behalf of the end customer and submit an LOA signed by the end customer whenever possible. Telnyx may request the Master Services Agreement that grants the right to change carriers.
- Be prepared to provide a signed LOA from the customer at any time upon request.
- Create separate port requests for each customer and each service address when porting multiple numbers.

### Porting From Specific Carriers and Resellers

**Bandwidth:** Raise a support ticket with Bandwidth porting support to request CSR information. Bandwidth does not use BTNs or account numbers; any of the numbers being ported can be used as the BTN and account number. For large ports, write "*Numbers provided in spreadsheet*" in the LOA's "Numbers to be ported" field and use your own company information on the LOA.

**Aircall:** Aircall is a reseller (typically backed by Twilio), so authorization must come from the underlying carrier. Contact Aircall support to obtain the underlying carrier, the carrier-level account number, and the carrier-level PIN/passcode (not the Aircall login password). Use the exact legal name and service address on the Aircall account. Common rejection reasons include `PASSCODE_PIN_INVALID`, `ACCOUNT_NUMBER_MISMATCH`, `BUSINESS_NAME_MISMATCH`, and `SERVICE_ADDRESS_MISMATCH`. Do not cancel Aircall before the port completes.

**Intercom:** Intercom's calling product is also typically backed by a carrier such as Twilio. Contact Intercom support for the underlying carrier, carrier-level account number, and port-out PIN. For Twilio-backed numbers, the account number is the Twilio Account SID (starting with "AC...") and the PIN is the Twilio auth token or a dedicated port-out passcode configured under Console → Phone Numbers → Port Out Settings. If a PIN is rejected, ask Intercom specifically for the current port-out passcode or auth token.

### Automating Ports With the API

Port-in can be automated using the Telnyx Porting API and Documents API:

1. Run a [portability check](https://developers.telnyx.com/api/porting/portability-check/post-portability-check).
2. [Upload supporting documents](https://developers.telnyx.com/api/documents/list-document-links) via the Documents API to receive a UUID.
3. [Initiate a porting order](https://developers.telnyx.com/api/porting/porting-order/list-porting-orders) using the v2/porting_orders endpoint.
4. Update the porting order with the document UUID, end_user information, activation_settings (FOC date), and phone_number_configuration settings.
5. [Confirm the porting order](https://developers.telnyx.com/api/porting/porting-order/list-porting-orders).
6. Optionally configure webhooks for port-in notifications. See the [Quickstart guide](https://developers.telnyx.com/docs/numbers/porting/quickstart) for an overview.
