---
title: European Number Porting and DID Requirements
summary: This page consolidates Telnyx's documentation for number porting and DID
  acquisition across Denmark, Finland, Ireland, the United Kingdom, Sweden, Georgia,
  Latvia, Russia, Ukraine, Poland, Lithuania, and Estonia. It covers the documentation
  required to port existing numbers into Telnyx, the identity and address verification
  needed to purchase new DIDs, and country-specific operational notes such as porting
  hours, SLAs, and common rejection causes.
sources:
- url: https://support.telnyx.com/en/articles/3266720-denmark-number-porting
- url: https://support.telnyx.com/en/articles/3266934-finland-number-porting
- url: https://support.telnyx.com/en/articles/3266983-ireland-number-porting
- url: https://support.telnyx.com/en/articles/3267693-united-kingdom-number-porting
- url: https://support.telnyx.com/en/articles/3275772-sweden-number-porting
- url: https://support.telnyx.com/en/articles/3506173-georgia-did-requirements
- url: https://support.telnyx.com/en/articles/3739496-latvia-did-requirements
- url: https://support.telnyx.com/en/articles/3739559-russia-did-requirements
- url: https://support.telnyx.com/en/articles/3739745-ukraine-did-requirements
- url: https://support.telnyx.com/en/articles/5188540-latvia-number-porting
- url: https://support.telnyx.com/en/articles/5188583-poland-number-porting
- url: https://support.telnyx.com/en/articles/5190470-lithuania-number-porting
- url: https://support.telnyx.com/en/articles/5466755-lithuania-did-requirements
- url: https://support.telnyx.com/en/articles/5466967-poland-did-requirements
- url: https://support.telnyx.com/en/articles/5720521-estonia-number-porting
updated_at: 2026-07-17T09:09:57Z
---

# European Number Porting and DID Requirements

*Part 2 of 4 — see also: [Part 1](european-number-porting-and-did-requirements--part-1.md), [Part 3](european-number-porting-and-did-requirements--part-3.md), [Part 4](european-number-porting-and-did-requirements--part-4.md)*

This page consolidates Telnyx's documentation for number porting and DID acquisition across Denmark, Finland, Ireland, the United Kingdom, Sweden, Georgia, Latvia, Russia, Ukraine, Poland, Lithuania, and Estonia. It covers the documentation required to port existing numbers into Telnyx, the identity and address verification needed to purchase new DIDs, and country-specific operational notes such as porting hours, SLAs, and common rejection causes.

## United Kingdom Number Porting

### Local Numbers

1. UK template LOA — the underlying carrier's name and/or Cupid code must be mentioned, line type (single or multi) must be specified, and a local address along with a valid postcode is required.
2. Latest invoice with the current carrier.

### National / Toll-Free Numbers

1. UK template LOA — the underlying carrier's name and/or Cupid code must be mentioned, a local address along with a valid postcode is required, and a Billing Account Number must be included on the LOA.
2. Latest invoice with the current carrier.

### Mobile Numbers

1. LOA.
2. Latest invoice.

A PAC (Porting Authorization Code) is required when transferring an existing mobile phone number to a new network. Providing that all documentation is correct and there aren't any rejections, a UK mobile request submitted before 12:00 noon local can be ported within the next business day.

### Before Completing the LOA

- All pages on the LOA must be signed, dated, and include the page numbers.
- The LOA should be saved in non-editable PDF format.
- Fill in the correct details in the designated areas.
- The signature should be a valid e-signature or manually signed.

Download the UK template LOA from the [Telnyx UK CLOA 2023](https://assets.ctfassets.net/taysl255dolk/4e1xrif0j3u8PU1qrl6GY5/bc86537edcb4e1f903da88ea986bd293/TELNYX_-_UK_CLOA_2023.pdf). This document is valid for all four number types in the UK.

### Useful Information for UK Portability

When porting UK numbers, the following factors must be considered:

- **Number detail** — confirm the type of numbers (Geographic, linked to a specific area in the UK and requiring a local address, or Non-Geographic, not tied to a specific area and requiring a national address) and the line type (Single Line, terminating on a single socket with no associated numbers, or Multi-Line, terminating on equipment such as a PBX which may include associated numbers).
- **Partial porting** — whether partial porting is possible depends on the current service provider. Most UK carriers do not allow number ranges to be split, meaning the entire range of numbers (typically a range where the first number ends in 0 and the last number ends in 9) usually needs to be ported together, along with any associated DIDs. In most cases, a Main Billing Number (BTN) cannot be ported while leaving associated numbers active with the current provider; these associated numbers must either be included in the porting request or ceased with the current provider. The best way to find out if partial porting is possible is to check directly with the current provider before submitting a request to Telnyx.
- **Underlying carrier** — this is the Current Communications Provider, which may not be the company that sends the monthly bill if that company is a reseller. Resellers do not have a CUPID code (a standard identification number used within the UK telecoms industry). If the current provider is a reseller, contact them directly to obtain the name of the underlying carrier and/or their CUPID code.
- **Range holder** — this is the carrier who owns the number block originally, i.e., the assigned block from OFCOM.

### Pre-Order Validation Process

If the information currently on file with the existing carrier is uncertain, Telnyx can, depending on the carrier, initiate a Pre-Order Validation (POV) to confirm the details associated with the DID(s). The POV process typically takes between 5 to 7 business days. As there are no formal SLAs in place for this process, it cannot be escalated and is dependent on the current provider's cooperation and response time.

### Time Frame for Local / National / Toll-Free UK Numbers

| Line Type | LCP is RH | LCP is not RH |
| --- | --- | --- |
| Single line | 5 | 7 |
| Multi-Line (including associated & other numbers) | 7 | 10 |
| Multi-Line (150 lines or less) | 10 | 13 |
| Multi-Line (151 lines or more) | 17 | 20 |
| Complex DDI | 22 | 25 |

These time frames are expected SLAs between carriers. In the event of no response from the Losing Communications Provider or the Range Holder within the time frame above, an escalation will be made to the relevant party.

### Time and Date of Port

It is possible to request a specific porting date; this date must fall within the time frame outlined in the table above. If the requested porting date and time do not comply with the applicable SLAs, the team will proceed by submitting the request for the earliest available date provided by the losing carrier.

The standard activation time for local and national ports is 10:00 AM GMT. All toll-free ports, unless otherwise specified, take place between 00:00 and 04:00 AM GMT on the FOC (Firm Order Commitment) date. However, this does not mean that the number will port at that specific time on FOC; in the UK, porting can take up to six hours to complete once it has been triggered. If, on the FOC date, the losing communications provider does not release the numbers, the team will follow up with the carrier every two hours until completion.

### Port Date Changes After FOC

Once a port has reached FOC Confirmed status, it is possible to request a change to the porting date if an issue arises. Any date change requested after submission to the current carrier incurs a fee of $40 per order. If the Losing Communications Provider is the Range Holder, a minimum of 24 hours' notice prior to the FOC date is required to postpone the port. If the Losing Communications Provider is not the Range Holder, a minimum of 72 hours' notice prior to the FOC date is required.

## Sweden Number Porting

For local, national, and toll-free numbers in Sweden, the following are required:

1. LOA — a local address is mandatory, and the signature on the LOA must be a wet signature.
2. Local TAX ID / VAT (must be 12 characters long).
3. Latest invoice.

Download the Sweden LoA from the [Telnyx international LoA template](https://assets.ctfassets.net/taysl255dolk/6YYtHkPiDoOfhR8Vp3QxUz/3f7b77cf78ecdebe280c6c0226ac12ea/LoA_-_Telnyx_-_INTL.pdf).

## Georgia DID Requirements

To purchase a Georgia number, the following must be provided.

### Local Numbers in Georgia

For **personal identity** verification:

- Name, last name.
- Contact phone number.
- Contact e-mail.
- Passport or ID copy.
- Georgia registration form.

For **business identity** verification:

- Name, last name of an authorized representative.
- Company name.
- Contact phone number.
- Contact e-mail.
- Company registration certificate.
- Georgia registration form.

For **address** verification:

- Address matching the DID area code (street, building number, postal code, city, and country).
- A copy of a utility bill (less than 3 months old).

### National Numbers in Georgia

For **personal identity** verification:

- Name, last name.
- Contact phone number.
- Passport or ID copy.
- Georgia registration form.

For **business identity** verification:

- Name, last name of an authorized representative.
- Company name.
- Contact phone number.
- Company registration certificate.
- Georgia registration form.

For **address** verification:

- Address worldwide (street, building number, postal code, city, and country).

### Toll-Free Numbers in Georgia

For **personal identity** verification:

- Name, last name of an authorized representative.
- Contact phone number.
- Contact e-mail.
- Passport or ID copy.
- Georgia registration form.

For **business identity** verification:

- Name, last name.
- Company name.
- Contact phone number.
- Contact e-mail.
- Company registration certificate.
- Georgia registration form.
- Forms holding Terms & Conditions need to be signed.

For **address** verification:

- Address worldwide (street, building number, postal code, city, and country).
- Proof of address (dated within 3 months).

Once the documentation is received, it will take approximately 72 hours to validate the information and activate the number for use.
