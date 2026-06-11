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
