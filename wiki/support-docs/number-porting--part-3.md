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

*Part 3 of 3 — see also: [Part 1](number-porting--part-1.md), [Part 2](number-porting--part-2.md)*

Telnyx supports local number portability (LNP) for moving phone numbers between carriers. This page covers the full porting lifecycle including port-in and port-out procedures, required documents, FastPort®, automated validation, auto-generated LOAs, porting bundles, SLA timelines, and reseller-specific guidance.

## LSR Submissions (Carrier-to-Carrier)

Carriers submitting Local Service Requests (LSRs) to Telnyx must follow these rules:

- All LSRs must be sent to lnp@telnyx.com.
- LSRs must be complete, legible, and accurate. Handwritten LSRs or faxes are not accepted.
- Submit a TPP (Trading Partner Profile) with your first LNP request. Email lnp@telnyx.com to obtain the Telnyx TPP.
- Required LSR fields: CCNA, PON, AN, DDD, CC, NNSP, AGAUTH, TEL NO (INIT), ZIP, LOA (attached), and a clean number list in 10-digit format.
- LSRs received after 2 PM CT are considered received on the next business day.
- Non-simple ports require all telephone numbers listed on a separate, clean sheet in 10-digit format.
- Telnyx will provide a reject notice within 48 business hours if applicable.
- FOC is issued if the LSR has no errors. Telnyx does not accept same-day FOCs. FOC is valid for 10 business days; the number must be activated in NPAC within 3 business days or the order is cancelled.
- Cancellations or reschedules must be received by 2 PM CST the day before the scheduled port date.
- Expedited LSRs are allowed at Telnyx's discretion.
- To check LSR status, email lnp@telnyx.com. Allow 48 hours before submitting a status request.

### Carrier Porting Holidays

Telnyx observes these holidays for carrier porting: New Year's Day, Memorial Day, Independence Day, Labor Day, Thanksgiving Day, Day after Thanksgiving, Christmas Eve Day, and Christmas Day. If a holiday falls on a Saturday, the preceding Friday is observed; if on a Sunday, the following Monday is observed.

### Escalation Contacts

- **1st Level:** Telnyx Porting Department — +1 (888) 980-9750 option 4, lnp@telnyx.com
- **2nd Level:** Tony Rizo, LNP Team Lead — tony@telnyx.com
- **3rd Level:** Patrick Budzinski, Global Manager, Porting and Provisioning — patrickb@telnyx.com

## Pre-Configuring Bundles on Port Orders

You can pre-configure [Bundles](bundles.md) (a Telnyx pricing option) on a porting order at any point before it completes (i.e., before it reaches `cancelled` or `ported` status). The bundle is not actually applied to the phone number until after it ports in.

### Via the Portal

1. Navigate to the **Port Numbers** page and click on an order to open its details.
2. Scroll to the bottom and click **Pre-configure Bundles**.
3. In the modal, use the **Add** tab to specify a phone number and the bundle to associate with it, then click **Create**.
4. Repeat for each number. To change a bundle, delete the existing pre-configuration and create a new one.

Ensure the bundle is eligible for the port order (e.g., a US bundle with US numbers). If the bundle is not eligible (e.g., a US bundle with Australian numbers), you cannot pre-configure it. Once the order ports, the bundles are automatically applied.

### Via the API

Follow the [developer guide for bundles and porting](https://developers.telnyx.com/docs/numbers/porting/bundles-porting) to pre-configure bundles programmatically.

## Porting API and LOA Template Download

The [Mission Control API](https://support.telnyx.com/en/articles/1130736-mission-control-api-porting) allows you to automate porting programmatically. When using the API, you can download the LOA template PDF by sending a GET request to `https://api.telnyx.com/v2/porting_orders/{porting_id}/loa_template` with your API key in the Authorization header.

## Contacting the Porting Team

- **Email:** porting@telnyx.com (customer port-in inquiries) or lnp@telnyx.com (carrier LSR/port-out inquiries)
- **Phone:** +1 (312) 270-8001 or +1 (888) 980-9750 option 4
- **Hours:** 9 AM – 5 PM Central Time, Monday–Friday
