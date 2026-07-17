---
title: 'France and Neighboring Regions: DID Requirements and Number Porting'
summary: This page consolidates the documentation requirements for purchasing DID
  numbers and porting existing numbers in France, its overseas territories (French
  Guiana, Guadeloupe, Martinique, Mayotte, Reunion, Saint Barth and Saint Martin),
  Monaco, Luxembourg, and Romania, including identity, business, and address verification
  rules, port types, time slots, and common rejection reasons.
sources:
- url: https://support.telnyx.com/en/articles/1311445-france-did-requirements
- url: https://support.telnyx.com/en/articles/13194814-french-guiana-number-porting
- url: https://support.telnyx.com/en/articles/13194884-mayotte-number-porting
- url: https://support.telnyx.com/en/articles/13194922-reunion-number-porting
- url: https://support.telnyx.com/en/articles/13194951-saint-barth-and-saint-martin-number-porting
- url: https://support.telnyx.com/en/articles/13719947-french-guiana-did-requirements
- url: https://support.telnyx.com/en/articles/13719972-guadeloupe-did-requirements
- url: https://support.telnyx.com/en/articles/13719992-martinique-did-requirements
- url: https://support.telnyx.com/en/articles/13720003-mayotte-did-requirements
- url: https://support.telnyx.com/en/articles/3266956-france-number-porting
- url: https://support.telnyx.com/en/articles/3739502-luxembourg-did-requirements
- url: https://support.telnyx.com/en/articles/3739552-romania-did-requirements
- url: https://support.telnyx.com/en/articles/5466798-monaco-did-requirements
- url: https://support.telnyx.com/en/articles/5954701-guadeloupe-number-porting
- url: https://support.telnyx.com/en/articles/5954733-martinique-number-porting
updated_at: 2026-07-17T09:08:19Z
---

# France and Neighboring Regions: DID Requirements and Number Porting

*Part 1 of 2 — see also: [Part 2](france-and-neighboring-regions-did-requirements-and-number-porting--part-2.md)*

This page consolidates the documentation requirements for purchasing DID numbers and porting existing numbers in France, its overseas territories (French Guiana, Guadeloupe, Martinique, Mayotte, Reunion, Saint Barth and Saint Martin), Monaco, Luxembourg, and Romania, including identity, business, and address verification rules, port types, time slots, and common rejection reasons.

## France DID Requirements

To purchase a France number, you must provide the following documentation.

### Local Numbers in France

**Personal identity** verification:
- Name, last name
- Contact phone number
- Local copy of ID or passport

**Business identity** verification:
- Name, last name of an authorized representative
- Company name
- Contact phone number
- Local company registration certificate

**Address** verification:
- Address in France (street, building number, postal code, city, and country)
- Proof of address (dated within 3 months)

End-users must be physically present in the country when purchasing numbers from that country.

### National Numbers in France

**Personal identity** verification:
- Name, last name
- Contact phone number
- Local passport or ID copy

**Business identity** verification:
- Name, last name of an authorized representative
- Company name
- Contact phone number
- Local company registration certificate

**Address** verification:
- Address in France (street, building number, postal code, city, and country)
- Proof of address (dated within 3 months)

End-users must be physically present in the country when purchasing numbers from that country.

### Toll-Free Numbers in France

**Business identity** verification:
- Name, last name of an authorized representative
- Company name
- Contact phone number
- Local company registration certificate
- Company Registration Number (SIREN number)

**Address** verification:
- Address in France (street, building number, postal code, city, and country)
- Proof of address (dated within 3 months)

End-users must be physically present in the country when purchasing numbers from that country. Business use is required; private use is not allowed.

Once documentation is received, it takes approximately 72 hours to validate the information and activate the number for use.

### Identity Verification: What "Local" Means

For most orders, your proof of identity must be issued by the country in which you are making your purchase. As an exception, customers within the European Union may use a valid passport or national identity card from any EU member state, even if it differs from the EU country associated with the order; in these cases, the document will be treated as local.

All identification is subject to review, and Telnyx reserves the right to request additional documentation or decline any document that cannot be verified or does not meet applicable legal and regulatory requirements.

## France Number Porting

For local, national, and toll-free numbers, the following are required:

1. LOA (national address mandatory) — [Download LOA](https://assets.ctfassets.net/taysl255dolk/4pv4cqjnsUfEGbyexn1Ycy/536af1c7e37734422a9556ea38582ceb/Telnyx_LoA_-_France.pdf)
2. SIRET code (for business accounts only, must be 14 digits long)
3. RIO code (must be 12 characters long)
4. Latest invoice with the current provider
5. Proof of address (dated within 3 months of the request)

**RIO code:** To retrieve this code, the customer can dial 3179 or 0 805 92 3179. If the current carrier does not allow the customer to call special numbers, the customer needs to reach out to the current carrier directly to retrieve the RIO.

**SIRET code:** An INSEE code that allows the geographic identification of any French establishment or business. Any business registered in France will have a SIRET of 14 digits.

### Port Types

There are 4 types of ports possible in France (isolated, full, partial, and complex port). All these port types take at least 8 business days to port.

1. **Isolated** — Select this option if you are porting only one number.
2. **Full portability** — Select this option if you are migrating a main number along with all the associated numbers.
3. **Partial portability** — Select this option if you are migrating some of the associated numbers to a BTN, without porting the actual BTN.
4. **Complex portability** — Select this option if you are migrating a main phone number without the associated numbers to that number. In this case, you must inform which number will become the new BTN.

### Time of Port

There are only 2 available time slots:

1. **Morning trigger (10 AM trigger)** — The request will port from 10 AM to 1 PM.
2. **Afternoon trigger (2 PM trigger)** — The request will port from 2 PM to 5 PM.

### Information on File

It is crucial to verify the information before Telnyx submits a port request, as Telnyx needs to wait until the losing carrier rejects the initial port request before being able to create a new port. This can take up to 3 business days and therefore delay the process.

For example, if the customer confused the business address and the port request has already been sent, Telnyx will have to wait for the Losing Communications Provider to reject the request before submitting another port request for the same number with a different address; otherwise, this port request will be rejected for pending port request.

### Most Common Rejections for France Number Porting

- Business address mismatch
- SIRET code invalid
- Business name mismatch
- Pending porting request with another carrier

## French Overseas Territories DID Requirements

The following French overseas territories share a common set of requirements for acquiring local numbers: French Guiana, Guadeloupe, Martinique, Mayotte, and Reunion.

### Local Numbers in French Overseas Territories

**Personal identity** verification:
- Name, last name
- Contact phone number
- Passport or ID copy

**Business identity** verification:
- Company name
- Contact phone number
- Company registration certificate

**Address** verification:
- Address worldwide (street, building number, postal code, city, and country)

## French Overseas Territories Number Porting

For local, national, and toll-free numbers in French Guiana, Guadeloupe, Martinique, Mayotte, Reunion, and Saint Barth and Saint Martin, the following are required:

1. LOA — [Download LOA](https://assets.ctfassets.net/taysl255dolk/6YYtHkPiDoOfhR8Vp3QxUz/3f7b77cf78ecdebe280c6c0226ac12ea/LoA_-_Telnyx_-_INTL.pdf)
2. National address mandatory
3. Latest invoice

## Monaco DID Requirements

To purchase a Monaco number, the following documentation is required for toll-free numbers.

**Personal identity** verification:
- Name, last name
- Contact phone number
- Passport or ID copy

**Business identity** verification:
- Company name
- Contact phone number
- Company registration certificate

**Address** verification:
- Address worldwide (street, building number, postal code, city, and country)

For custom number pricing in Monaco, see the [number pricing](https://telnyx.com/pricing/numbers) page.
