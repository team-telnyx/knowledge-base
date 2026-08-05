---
title: Number Porting and DID Requirements by Country
summary: This page consolidates Telnyx's country-specific number porting and DID acquisition
  requirements across the Americas, Europe, and the Caribbean. It covers required
  documentation (LOA, invoices, IDs, tax IDs, company registration), porting hours,
  expected timeframes, and links to downloadable LOA templates for each supported
  country.
sources:
- url: https://support.telnyx.com/en/articles/3266425-brazil-number-porting
- url: https://support.telnyx.com/en/articles/3266430-canada-number-porting
- url: https://support.telnyx.com/en/articles/3266652-chile-number-porting
- url: https://support.telnyx.com/en/articles/3267436-peru-number-porting
- url: https://support.telnyx.com/en/articles/3267535-puerto-rico-number-porting
- url: https://support.telnyx.com/en/articles/3267566-cyprus-number-porting
- url: https://support.telnyx.com/en/articles/3267595-spain-number-porting
- url: https://support.telnyx.com/en/articles/3267816-united-states-number-porting
- url: https://support.telnyx.com/en/articles/5190458-the-dominican-republic-number-porting
- url: https://support.telnyx.com/en/articles/5464157-dominican-republic-did-requirements
- url: https://support.telnyx.com/en/articles/5856747-anguilla-did-requirements
- url: https://support.telnyx.com/en/articles/6129704-antigua-and-barbuda-did-requirements
- url: https://support.telnyx.com/en/articles/6138781-turkey-number-porting
- url: https://support.telnyx.com/en/articles/8673249-us-ca-toll-free-number-porting
- url: https://support.telnyx.com/en/articles/9271183-argentina-number-portability
updated_at: 2026-08-05T13:35:26Z
---

# Number Porting and DID Requirements by Country

*Part 1 of 2 — see also: [Part 2](number-porting-and-did-requirements-by-country--part-2.md)*

This page consolidates Telnyx's country-specific number porting and DID acquisition requirements across the Americas, Europe, and the Caribbean. It covers required documentation (LOA, invoices, IDs, tax IDs, company registration), porting hours, expected timeframes, and links to downloadable LOA templates for each supported country.

## Overview

Telnyx supports number porting and DID (Direct Inward Dialing) acquisition across a wide range of countries. Requirements vary by country and number type, but most porting requests require a signed Letter of Authorization (LOA), a recent invoice from the current carrier, and identity or business verification documents. This page consolidates the country-specific requirements, porting hours, expected timeframes, and LOA download links for each supported region.

## United States

### Local Numbers
1. LOA (BTN, Account number & Local address required)
2. Latest Invoice

### Toll-Free Numbers
1. LOA (Local address & Account Number required)
2. Latest Invoice

Download the LOA from the [Telnyx portal](https://portal.telnyx.com/downloads/other/Telnyx-LOA.pdf).

For additional guidance, see [Porting Policy Procedure](porting-policy-procedure.md), [Porting Requirements](porting-requirements.md), [Porting Error Messages](porting-error-messages.md), and [Best Practices for Contacting Porting](best-practices-for-contacting-porting.md).

## Canada

### Local / Mobile / Toll-Free Numbers
1. LOA (Local address & Account Number required)
2. Latest Invoice

Download the [Canadian LOA](https://www.dropbox.com/s/dxk8l9x73j4ufn8/Telnyx%20LOA.pdf?dl=0).

For additional guidance, see [Porting Policy Procedure](porting-policy-procedure.md), [Porting Requirements](porting-requirements.md), [Porting Error Messages](porting-error-messages.md), and [Best Practices for Contacting Porting](best-practices-for-contacting-porting.md).

## Puerto Rico

### Local / Mobile Numbers
1. LOA
2. Latest Invoice

Download the [Puerto Rico LOA](https://www.dropbox.com/s/dxk8l9x73j4ufn8/Telnyx%20LOA.pdf?dl=0).

For additional guidance, see [Porting Policy Procedure](porting-policy-procedure.md), [Porting Requirements](porting-requirements.md), [Porting Error Messages](porting-error-messages.md), and [Best Practices for Contacting Porting](best-practices-for-contacting-porting.md).

## US / CA Toll-Free Number Porting

Toll-free or "8YY" numbers (including 800, 844, 855, 866, 877, and 888 exchanges) follow a distinct porting process that differs from FCC-mandated Local Number Portability (LNP). Toll-free porting uses a centralized portal and typically completes faster than standard porting. Telnyx recommends initiating toll-free port requests at least two weeks before the desired activation date.

Toll-free numbers risk disconnection if not activated within 1–2 weeks after release by the RespOrg. To minimize rejections, customers should delay submitting port requests until they are within the 2-week window. The timeline for toll-free port requests can span 7 days, assuming no rejections and a suitable first available date is selected.

### Required Documentation
1. LOA
2. Latest Invoice

Download the [LOA](https://portal.telnyx.com/downloads/other/Telnyx-LOA.pdf). Refer to the [How to Fill Out an LOA](how-to-fill-out-an-loa.md) page for detailed procedures.

### Timeline
Toll-free number porting should take approximately 2 business days, though timelines can vary from 1 to 7 business days.

### SMS Porting Best Practices
When an order transitions to `ported` status, voice services migrate to Telnyx, but SMS migration is not guaranteed at the same time. It may take several hours after the scheduled FOC date/time before the losing carrier releases SMS to Telnyx.

To minimize SMS downtime, Telnyx recommends porting SMS prior to porting voice. To port SMS only, submit a hosted SMS request at least 5 business days prior to the desired FOC date.

Example porting process for toll-free numbers with SMS:
1. Create a hosted SMS request for the phone numbers you are attempting to port.
2. Create a porting order for the same phone numbers. Request a FOC date at least 5 business days in advance.
3. After 3–4 business days, the hosted SMS request completes. SMS migrates to Telnyx and becomes active while voice still routes through the losing carrier.
4. When the scheduled FOC date/time arrives, voice ports in and the numbers are fully activated on Telnyx. Both voice and SMS route through Telnyx with no downtime.

For more information, see [Hosted SMS Messaging Process](hosted-sms-messaging-process.md).

## Brazil

### Local / National / Toll-Free
1. LOA (CPF / CNPJ required)
2. ID / Passport copy
3. Company Registration certificate
4. Latest Invoice

Download the [Brazil LOA](https://www.dropbox.com/s/fmli59wv3wfky7w/BrazilLOA.pdf?dl=0).

### Porting Hours
Standard time after 5 PM local.

### Expected Timeframes
| Number Type | Expected Timeframe |
| --- | --- |
| National | 5+ Business days |
| Toll-Free | 5+ Business days |

> Once your port request is in status *FOC confirmed*, Telnyx requires at least 48 business hours prior to the FOC date to change the date.

See also [Brazil DID Requirements](brazil-did-requirements.md).

## Chile

### Local / Toll-Free Numbers
- E-RUT
- LOA or POA
- Latest Invoice
- Chile Power of Attorney
- Chile Certificate of Incorporation
- RUT of the individual requesting portability
- Proof of Payment (national carrier invoice, no resellers)

Reach out to [porting.intl@telnyx.com](mailto:porting.intl@telnyx.com) for the template document.

### Porting Hours
Standard time 00:00 AM to 4 AM local.

### Expected Timeframes
| Number Type | Expected Timeframe |
| --- | --- |
| Local | 5+ Business days |
| National | 5+ Business days |
| Toll-Free | 5+ Business days |

## Peru

### Local / National Numbers
1. LOA
2. Attorney's authorization for the representative (if the number belongs to a company)
3. ID / Passport copy
4. Company Registration certificate
5. Latest Invoice

Download the [Peru porting form](https://www.dropbox.com/s/0j3d2r4e5idm9o7/Peruvian_Porting_Form.pdf?dl=0).

### Porting Hours
Standard time 00:00 AM to 4 AM local.

### Expected Timeframes
| Number Type | Expected Timeframe |
| --- | --- |
| Local | 2–7 Business days |

## Argentina

### Local / National Numbers
1. LOA (contact email must be included)
2. CUIT / CUIL / VAT (if the number belongs to a company)
3. Attorney's authorization for the representative (if the number belongs to a company)
4. Copy of ID / Passport / DNI
5. Latest Invoice with the current provider

Reach out to [porting.intl@telnyx.com](mailto:porting.intl@telnyx.com) for the Argentina LOA template.

For additional guidance, see [Porting Policy Procedure](porting-policy-procedure.md), [Porting Requirements](porting-requirements.md), [Porting Error Messages](porting-error-messages.md), and [Best Practices for Contacting Porting](best-practices-for-contacting-porting.md).

## Dominican Republic

### Porting Requirements (Local / National)
1. LOA (National address required)
2. Latest Invoice with the current carrier
3. TAX ID / VAT
4. Passport / ID copy
5. Proof of address

Download the [Dominican Republic LOA](https://assets.ctfassets.net/taysl255dolk/3k7kEutWHK91DYuMoG4Xa/6fdf040bb9d9aff432133f4d72997ab2/LOA_-_TELNYX_-_DOMINICAN_REPUBLIC.pdf).

> To keep the number active during porting, contact the losing provider to retain the subscription or keep inbound services throughout the process. Otherwise, undefined service downtime (up to 7 business days) may occur. Once the porting process has started and the numbers are released by the losing carrier, an undefined (at least 2 hours) service downtime may be experienced due to local porting procedures.

### DID Acquisition Requirements

**Local and Toll-Free Numbers**

For personal identity verification:
- Name, last name
- Contact phone number
- Passport or ID copy

For business identity verification:
- Company name
- Contact phone number
- Company registration certificate

For address verification:
- Address worldwide (street, building number, postal code, city and country)

See [Dominican Republic number pricing](https://telnyx.com/pricing/numbers/do) for custom pricing.
