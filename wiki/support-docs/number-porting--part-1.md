---
title: Number Porting
summary: Telnyx supports local number portability (LNP) for moving phone numbers between
  carriers. This page covers the full porting lifecycle including port-in and port-out
  procedures, required documents, FastPort®, automated validation, auto-generated
  LOAs, porting bundles, SLA timelines, and reseller-specific guidance.
sources:
- url: https://support.telnyx.com/en/articles/1130626-international-number-porting-required-documents
  content_hash: 2666e6590c5d40d75f1ca3eba692352425ee125f962d0e8704bc42e3837e351d
- url: https://support.telnyx.com/en/articles/1130630-porting-policy-procedure
  content_hash: 1559ee59b372c1825d8b182149f94199bc4207c8a09ea6b4254f7b64cc03f15c
- url: https://support.telnyx.com/en/articles/1130633-checking-a-port-request-status
  content_hash: 9dbefe941d4494e56466917c4ca28ab3864025c9ca6319757bc4e78ddd6d77c3
- url: https://support.telnyx.com/en/articles/1130634-port-numbers-to-telnyx
  content_hash: 62926b63aa966025bd5f1ccb686353afa90661682a86bafe61e56e2a6f0c18e9
- url: https://support.telnyx.com/en/articles/1130635-can-i-port-out-my-telnyx-number
  content_hash: cc008d87e7ed790c82632a18b886b72a756e40ff8f3711920edfa2e5e67c8149
- url: https://support.telnyx.com/en/articles/1516776-automated-port-request-validation
  content_hash: d59a61b7640448b28cdb9b9eb2b701361e83a81537626eaa08dc4c43dca7490d
- url: https://support.telnyx.com/en/articles/2021334-your-guide-to-fastport
  content_hash: 918ed88ee13342fb94f0ef6bbc9cf8971615dff902b12a3733553504ad17cd9b
- url: https://support.telnyx.com/en/articles/2030770-port-in-best-practices
  content_hash: 9a8b473b36868a7005e7827e320412f1bc2eb04fdb3d363846e71f60e543c3d8
- url: https://support.telnyx.com/en/articles/2033789-port-numbers-away-from-telnyx
  content_hash: 6a6ca78dcaa26dae4cccdc17cba37614daa205c479f156464f9a0d72e9346574
- url: https://support.telnyx.com/en/articles/2034326-how-to-fill-out-an-loa
  content_hash: 7bbc168fc36305967bb39144216f2eb01c12dd5ed54627b09891dbfac865b753
- url: https://support.telnyx.com/en/articles/2042977-porting-in-day-of-port-foc
  content_hash: 16603c67b6daa5ccff477ca0794847ea9475d9817fc0c850b6eaabc58d3fe5b1
- url: https://support.telnyx.com/en/articles/2054704-fastport-faqs
  content_hash: 786bfde32aa7d2444f38ee8b58556645da4bff79f945b10e3f84fdb0c5764890
- url: https://support.telnyx.com/en/articles/2086149-number-porting-rules-and-guidelines
  content_hash: 42f4ac8958e5fbfdd923cc926a7f51efe3285d1bbf59ca3b8d0aae5195fba72a
- url: https://support.telnyx.com/en/articles/3284588-port-request-statuses
  content_hash: b334b6b275900e7b374df31481407b799a9ac60ba6a1992283b6bf35de66c042
- url: https://support.telnyx.com/en/articles/3561993-using-telnyx-fastport
  content_hash: a3d4279678968caab57b3c7c09b5184b9b5f8f02b921df71904b8ea5e7a27acb
- url: https://support.telnyx.com/en/articles/6460777-porting-requirements
  content_hash: 9ff006df65edfc3e01a4b24443a52c56ce8a709c47fbc2405671bbf8f18ed2f0
- url: https://support.telnyx.com/en/articles/8268276-loa-template-download
  content_hash: 0e4af1cc265cc42fc51d52dee93761e896ae05e912e7cc1e1fd96e0e02b5fbd7
- url: https://support.telnyx.com/en/articles/8588086-auto-generated-letter-of-authorization-loa
  content_hash: 096805d248af306e95444a3b7eb8ae808ad6e8ca7d42a343bb985ccca77203e6
- url: https://support.telnyx.com/en/articles/8709331-porting-bundles
  content_hash: 1ce9997e7910b8c2a7daf4e10607c8fd5854b33daa312a2b1e8caf881dc0c252
updated_at: 2026-06-11T11:12:38Z
---

# Number Porting

*Part 1 of 3 — see also: [Part 2](number-porting--part-2.md), [Part 3](number-porting--part-3.md)*

Telnyx supports local number portability (LNP) for moving phone numbers between carriers. This page covers the full porting lifecycle including port-in and port-out procedures, required documents, FastPort®, automated validation, auto-generated LOAs, porting bundles, SLA timelines, and reseller-specific guidance.

## Porting Numbers Into Telnyx

To port numbers from another carrier into Telnyx, use the Mission Control Portal or the [Mission Control API](https://support.telnyx.com/en/articles/1130736-mission-control-api-porting). Port requests can be submitted 24/7/365 through the portal, but are only processed Monday through Friday, 9 AM – 5 PM CT.

### Step-by-Step Port-In

1. Log in to Mission Control and navigate to **Real-Time Communications → Numbers → Port Numbers**.
2. Click **New Port Request**.
3. Choose whether the numbers are your own or your customer's (if you are a reseller).
4. Select the country. Port requests must be split into separate requests per country.
5. Enter the numbers to port, separated by commas or line breaks. Accepted formats: NPANXXYYYY, 1NPANXXYYYY, NPA-NXX-YYYY, 1-NPA-NXX-YYYY.
6. Click **Check Portability**. Non-portable numbers are flagged and can be removed. The request is broken into sub-requests grouped by the underlying losing carrier. If an international number shows as not eligible, email porting@telnyx.com — it may still be portable outside the automated process.
7. Input account information that matches the billing/service address on file with the current carrier, and provide the authorized person's name.
8. Upload supporting documents (LOA and Invoice/CSR).
9. Choose a default connection so numbers are immediately routed once ported.
10. You may request a FOC (Firm Order Commitment) date, but it is not guaranteed by the losing carrier. Expedited requests are handled on a case-by-case basis and require explicit Telnyx approval.

### Checking Port Request Status

View real-time status from the **Port Numbers** tab in Mission Control. Requests are color-coded by status. Click **View Details** to search for specific numbers, view sub-requests and FOC dates, and read or add comments. All communication about port requests — including supplementary document uploads — must go through the comments feature; do not email for status updates.

See [Port Request Statuses](port-request-statuses.md) for the full list of statuses and their meanings.

## Required Documents

Every port request requires the following documentation:

### Letter of Authorization (LOA)

The LOA is a legal document authorizing Telnyx to request a port on behalf of the end user. Requirements:

- **Signature:** Wet signature or valid electronic signature (DocuSign, Adobe Sign, etc.).
- **Signer:** Must match the authorized person on file with the losing carrier.
- **Numbers:** All numbers being ported must be listed in NPA-NXX-XXXX format, separated by commas (or attached as a spreadsheet for large lists).
- **Information:** End-user name, service address (not billing address unless they are the same), carrier name, and Billing Telephone Number (BTN).
- **Date:** Must be signed within the last 90 days.
- **Toll-free LOA:** Must include the phrase "Port to RespOrg QIT02."

Download the [LOA template](https://drive.google.com/file/d/1yxrQSkEIFA5dPzlmRJAtB7QN3iYDzh0z/view) or use the auto-generated LOA feature described below.

### Invoice or Bill

An invoice from the current (losing) carrier proves ownership of the numbers. Requirements:

- Must be from the losing carrier.
- Must be within the last 30 days.
- Should show the telephone numbers being ported if possible.

If the invoice does not list the numbers, provide one of these alternatives:

- A screenshot from the current carrier's portal showing the numbers on the account.
- A Customer Service Record (CSR) from the current carrier listing the numbers.
- Contact porting@telnyx.com to discuss other proof-of-ownership options.

### Customer Service Record (CSR) — Optional but Recommended

A CSR is an official record from the current carrier containing account holder name, service address, BTN, list of telephone numbers, and carrier information. Although not required, providing a CSR helps validate your information and prevents rejections due to mismatched data.

### Document Validity Periods

| Document | Maximum Age |
|---|---|
| LOA (signature date) | 90 days |
| Invoice/Bill | 30 days |
| CSR | No strict limit, but recent is preferred |

For details on filling out the LOA, see [How to Fill Out an LOA](how-to-fill-out-an-loa.md).

## Auto-Generated LOA

On select port orders, Telnyx can auto-generate a pre-populated LOA based on the information entered on the porting order form. This feature is currently available for US local and CA local phone numbers only.

### Using Auto-Generate LOA

After running the portability check and filling in order details, navigate to the **Additional Requirements** page and click **Auto-generate LOA**. A modal appears where you can:

- Select an LOA template (if you have multiple branded templates).
- Enter the print name and date.
- Draw a signature.
- **Modify** to save changes, **Download** to save locally, or **Submit** to attach the LOA to the order.

A preview of the LOA is shown on the right side of the modal.

### Share LOA

If the authorized signer is someone else, click **Share LOA** to generate a shareable link. The authorized user can visit the link to sign and attach the LOA without needing a Telnyx account. Key notes:

- The link expires after 48 hours. If it expires, generate a new link or manually upload a signed LOA.
- Save the port order as a draft ("Save and Close") while waiting for the signer.
- Email notifications are sent when the LOA is signed or when the link expires.
- You cannot submit the porting order until an LOA is attached.

### Custom LOA Branding

By default, auto-generated LOAs use Telnyx branding. To customize with your own company logo and information, go to the [Customize LOA page](https://portal.telnyx.com/#/numbers/port-numbers/customize-loa) in the portal and click **New LOA Template**. Fill in your company name, email, phone, and address, then preview and save. Multiple templates can be created; the most recently created is used by default, and you can switch templates from the LOA Template dropdown.

## International Number Porting

To check the portability of international numbers, submit a port request via the Mission Control Portal with the required documentation. You must provide an LOA and invoice; after portability is confirmed, the Telnyx porting team will contact you with next steps and any additional country-specific documentation requirements.

Requirements vary by country and may include country-specific LOA forms, VAT/Tax ID, and other documentation. See the [International Number Porting Required Documents](https://support.telnyx.com/en/articles/1130626-international-number-porting-required-documents) article or the International Number Requirements Tool in the portal for country-specific details. Some countries do not support porting at all.

## FastPort®

FastPort® is a feature that verifies your LOA information against the losing carrier's records in real time, alerting you to any incorrect information before submission. This prevents days or weeks of delays caused by data mismatches.

Once the FOC date is confirmed, FastPort® gives you two activation options:

1. **On Demand:** You manually activate the numbers by clicking **Activate Now** on the port request details page at any time within the activation window.
2. **Schedule:** Choose a specific date and time within the activation window. The numbers auto-activate at that time.

If you forget to activate during the window, numbers auto-activate at the end of the window. You can reschedule the activation time within the window by clicking **Reschedule Activation**. To change the FOC date itself, contact the porting team at least 72 hours before the scheduled date; changing within 72 hours increases the risk that the losing carrier will drop the lines.

Not all carriers support the real-time validation needed for FastPort®. There is no additional fee for FastPort® on US and Canadian numbers.
