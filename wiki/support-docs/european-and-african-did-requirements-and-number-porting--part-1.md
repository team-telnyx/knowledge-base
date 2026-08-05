---
title: European and African DID Requirements and Number Porting
summary: This page consolidates Telnyx documentation covering DID (Direct Inward Dialing)
  number requirements and number porting procedures for several European and African
  countries, including Italy, Sweden, Switzerland, Denmark, Norway, Portugal, Mozambique,
  and Angola. It also explains the Requirement Groups feature, which became mandatory
  for ordering numbers in six European countries on September 16, 2024.
sources:
- url: https://support.telnyx.com/en/articles/11843417-mozambique-did-requirements
- url: https://support.telnyx.com/en/articles/1311462-italy-did-requirements
- url: https://support.telnyx.com/en/articles/1311477-sweden-did-requirements
- url: https://support.telnyx.com/en/articles/3266720-denmark-number-porting
- url: https://support.telnyx.com/en/articles/3266934-finland-number-porting
- url: https://support.telnyx.com/en/articles/3266983-ireland-number-porting
- url: https://support.telnyx.com/en/articles/3275772-sweden-number-porting
- url: https://support.telnyx.com/en/articles/3739580-switzerland-did-requirements
- url: https://support.telnyx.com/en/articles/5120062-portugal-number-porting
- url: https://support.telnyx.com/en/articles/5464149-denmark-did-requirements
- url: https://support.telnyx.com/en/articles/5466855-norway-did-requirements
- url: https://support.telnyx.com/en/articles/5466980-portugal-did-requirements
- url: https://support.telnyx.com/en/articles/5720521-estonia-number-porting
- url: https://support.telnyx.com/en/articles/6129696-angola-did-requirements
- url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
updated_at: 2026-08-05T13:32:26Z
---

# European and African DID Requirements and Number Porting

*Part 1 of 3 — see also: [Part 2](european-and-african-did-requirements-and-number-porting--part-2.md), [Part 3](european-and-african-did-requirements-and-number-porting--part-3.md)*

This page consolidates Telnyx documentation covering DID (Direct Inward Dialing) number requirements and number porting procedures for several European and African countries, including Italy, Sweden, Switzerland, Denmark, Norway, Portugal, Mozambique, and Angola. It also explains the Requirement Groups feature, which became mandatory for ordering numbers in six European countries on September 16, 2024.

## Overview

Telnyx provides local, national, mobile, and toll-free phone numbers across many countries. Each country has its own regulatory requirements for purchasing new DIDs and for porting existing numbers from another carrier. This page consolidates the per-country requirements for several European and African markets, along with the cross-country Requirement Groups workflow.

## Requirement Groups for Ordering Phone Numbers

Requirement Groups let you view, manage, and fulfill regulatory requirements in advance for a particular order type. By creating a Requirement Group, you can pre-fill all necessary information and documentation once and then reuse the group across multiple orders, eliminating the need to re-upload the same requirements for each order.

Requirement Groups are optional in most countries. However, starting **September 16, 2024**, they became mandatory for ordering phone numbers in the following countries:

- CH (Switzerland)
- DK (Denmark)
- IT (Italy)
- NO (Norway)
- PT (Portugal)
- SE (Sweden)

### How Requirement Groups work

1. Navigate to the [Requirement Groups page in the portal](https://portal.telnyx.com/#/numbers/requirements/requirement-groups).
2. Click `New Requirement Group` to open the creation form.
3. Each Requirement Group is valid only for a specific combination of `Country`, `phone_number_type`, and `type of order`. For example, a `Portugal` `local` `ordering` requirement group can only be associated with Portugal local number orders.
4. Once created, the Requirement Group displays the expected requirements for the relevant order.
5. Fill out all of the requirements and click `Submit`.
6. Go to the [Buy Numbers page](https://portal.telnyx.com/#/numbers/buy-numbers) and add the phone numbers that match the Requirement Group to your cart.
7. In the cart, use the `Requirement Groups` column to select the appropriate Requirement Group for each phone number.
8. Place your order.
9. The requirements from the Requirement Group are automatically attached to your order, which is then reviewed by the Operations team.

A developer guide is also available for integrating with Requirement Groups via the API.

## Italy DID Requirements

Italy requires the use of Requirement Groups for all number orders.

### Customer types

- **Natural Person (Persona Fisica):** Individual using the service for personal, non-commercial purposes at their residence. No VAT number or business registration required.
- **Legal Entity (Persona Giuridica):** Public or private entities with legal capacity independent from their members (e.g., SpA, Srl, Ltd, Inc, foundations, municipalities, universities). Has a VAT number and is a legally registered entity.
- **Sole Proprietorship (Ditta Individuale):** Business owned and operated by one individual who is personally responsible for all aspects (e.g., freelancers, small traders, artisans, consultants). Has a VAT number.

### Local Numbers in Italy

**Personal identity verification:**
- Name, last name
- Date of birth
- Place of birth
- Gender
- Nationality
- Personal Tax Code (natural persons and sole proprietorships only)
- Local copy of ID or passport (front and back)
- Identity document type, issuer, number, issuance date, and expiration date
- Contact e-mail

**Business identity verification:**
- Name, last name of an authorized representative (legal entities and sole proprietorships only)
- Authorized representative's date of birth, place of birth, gender, nationality
- Local copy of ID or passport of an authorized representative (front and back)
- Identity document type, issuer, number, issuance date, and expiration date
- Authorized representative contact e-mail
- Company name
- Local company registration certificate (legal entities and sole proprietorships only)
- VAT number (legal entities and sole proprietorships only)
- Supplemental address of legal representative's residence in Italy (legal entities only)

**Address verification:**
- Address in Italy (street, building number, postal code, city, country)
- Proof of address (dated within 3 months)

**Additional details:**
- End-users must be physically present in the country when purchasing numbers from that country.
- All documents must be submitted in `.pdf` format.
- Upon regulatory review, additional validating details may be requested.

### Toll-Free Numbers in Italy

**Business identity verification:**
- Business registration certificate
- VAT number
- Local passport or ID copy of an authorized representative (front and back)
- Company representative's Tax ID

**Address verification:**
- Address in Italy (street, building number, postal code, city, country)
- Proof of address (dated within 3 months)

**Additional details:**
- End-users must be physically present in the country when purchasing numbers from that country.
- Upon regulatory review, additional validating details may be requested.

## Sweden DID Requirements

Sweden requires the use of Requirement Groups for all number orders.

### Local Numbers in Sweden

**Business identity verification:**
- Name, last name of an authorized representative
- Contact phone number
- Contact e-mail
- Company name
- Passport or ID copy of an authorized representative
- Business registration certificate
- Business registration number

**Address verification:**
- Address matching the DID area code (street, building number, postal code, city, country)
- Proof of address (dated within 3 months)

**Additional details:**
- End-users must be physically present in the country when purchasing numbers from that country.
- Business use is required; private use is not allowed.

### National Numbers in Sweden

**Business identity verification:**
- Name, last name of an authorized representative
- Contact phone number
- Contact e-mail
- Company name
- Passport or ID copy of an authorized representative
- Business registration certificate
- Business registration number

**Address verification:**
- Address in Sweden (street, building number, postal code, city, country)
- Proof of address (dated within 3 months)

**Additional details:**
- End-users must be physically present in the country when purchasing numbers from that country.
- Business use is required; private use is not allowed.

### Mobile Numbers in Sweden

**Personal identity verification:**
- Name, last name
- Contact phone number
- Local passport or ID copy

**Business identity verification:**
- Name, last name of an authorized representative
- Company name
- Contact phone number
- Local company incorporation certificate

**Address verification:**
- Address in Sweden (street, building number, postal code, city, country)
- Proof of address (dated within 3 months)

**Additional details:**
- End-users must be physically present in the country when purchasing numbers from that country.

### Toll-Free Numbers in Sweden

**Personal identity verification:**
- Name, last name
- Contact phone number
- Local passport or ID copy

**Business identity verification:**
- Name, last name
- Contact phone number
- Company name
- Local company incorporation certificate

**Address verification:**
- Address in Sweden (street, building number, postal code, city, country)
- Proof of address (dated within 3 months)

**Additional details:**
- End-users must be physically present in the country when purchasing numbers from that country.
