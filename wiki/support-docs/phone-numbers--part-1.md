---
title: Phone Numbers
summary: Overview of Telnyx phone numbers (DIDs), including available types, how to
  search and buy them, ordering restrictions based on account verification, international
  regulatory requirements, bulk management features, and number lookup capabilities.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
- url: https://support.telnyx.com/en/articles/1130699-did-numbers-that-telnyx-offers
- url: https://support.telnyx.com/en/articles/1130702-where-can-i-buy-dids-in-the-us-canada
- url: https://support.telnyx.com/en/articles/1130704-what-is-a-did
- url: https://support.telnyx.com/en/articles/1458084-global-number-types
- url: https://support.telnyx.com/en/articles/2807846-bulk-edit-numbers-voice-settings
- url: https://support.telnyx.com/en/articles/2807910-bulk-edit-numbers-assigning-tags
- url: https://support.telnyx.com/en/articles/2819236-bulk-edit-numbers-delete-numbers
- url: https://support.telnyx.com/en/articles/2819238-bulk-edit-numbers-messaging-profile
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
- url: https://support.telnyx.com/en/articles/4366901-your-number-lookup-guide
- url: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
- url: https://support.telnyx.com/en/articles/4640720-what-is-an-exhausted-npa
- url: https://support.telnyx.com/en/articles/5469551-international-numbers-required-documents
- url: https://support.telnyx.com/en/articles/7003167-international-number-requirements-tool
- url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
updated_at: 2026-06-11T11:44:58Z
---

# Phone Numbers

*Part 1 of 3 — see also: [Part 2](phone-numbers--part-2.md), [Part 3](phone-numbers--part-3.md)*

Overview of Telnyx phone numbers (DIDs), including available types, how to search and buy them, ordering restrictions based on account verification, international regulatory requirements, bulk management features, and number lookup capabilities.

## What Is a DID

A Direct Inward Dial (DID) number is a virtual phone number not tied to any POTS landline. Once your account is configured, your DID becomes the phone number at which anyone can reach you.

## Number Types

### Domestic Long-Code (Local)

Typical local numbers for local businesses, with coverage in over 20,000 rate centres across the United States and Canada. Telnyx domestic long codes support instant provisioning for fax, voice, SMS, and MMS. View the domestic coverage map [here](https://telnyx.com/resources/telnyx-domestic-coverage-map).

### Domestic Toll-Free

Telnyx is a managing Responsible Organization (RespOrg QIT01), enabling acquisition, management, and routing of toll-free calls, plus the ability to quickly reroute traffic for service impairments.

**Toll-Free Voice** — Pre-provisioned voice toll-free numbers can be purchased with routing already set for instant use. Select **Quickship** on the search interface to receive numbers ready for inbound voice calls. Without Quickship, routing provisioning can take up to one hour after order completion. Quickship only applies to the voice portion of toll-free numbers.

**Toll-Free Messaging** — Toll-free SMS and MMS are available for the USA and Canada. The messaging portion is not instantly provisioned; you should submit your use case first to avoid spam blocks on non-verified toll-free numbers. See the dedicated [toll-free messaging article](https://support.telnyx.com/en/articles/5353868-toll-free-messaging) for acceptable use cases.

### International Number Types

Telnyx offers local, national, toll-free, shared cost, and mobile numbers from select countries worldwide. See the [international coverage map](https://telnyx.com/global-coverage).

When ordering international numbers, Telnyx may require documentation to comply with local regulators. The checkout UI will indicate if documentation is needed; after ordering you can upload it on the number orders page. You will also receive an email with a deadline — you have **10 days** to provide documentation or the numbers will be removed from your account.

## Searching and Buying Numbers

Access the Search & Buy Numbers page via the **Buy Number** button on the [My Numbers](https://portal.telnyx.com/#/numbers/my-numbers) page.

### Search Filters

- **Country** (required) — the only mandatory field
- **Features** — filter by capabilities (e.g., SMS, voice, MMS)
- **Type** — Local or Toll-Free
- **Search By** — Area Code, City/Region, or State/Province (local numbers only)

### Advanced Search Options

- **Vanity numbers or specific digits** — search for patterns within a phone number
- **Consecutive Numbers** — find blocks of sequential numbers
- **Results limit** — up to 100 results
- **Best Effort** — return numbers in a nearby rate centre or area code if exact matches are unavailable
- **Quickship** — return toll-free numbers with voice/fax capabilities instantly provisioned
- **Reservable Numbers** — reserve numbers for 30 minutes (extendable by another 30 minutes) without purchasing
- **Exclude Held Numbers** — exclude recently deleted numbers that Telnyx holds on your account for up to 15 days
- **Telnyx Bundles** — search for bundles containing numbers, features, and minutes (excludes premium NPA TNs)

### Cart and Ordering

Add numbers to your cart, then click the cart icon in the top-right corner. The cart shows **Upfront Cost** (one-time activation) and **Monthly Cost** (recurring) for each number. You can assign a Connection or Messaging Profile to numbers at this stage. Orders are **final** — no refunds for mistaken purchases.

It is recommended to order up to **50 numbers** at a time through the cart. Larger orders may result in purchase failures or incorrect assignment of Connections/Messaging Profiles. For bulk orders over 50, contact the sales team.

After placing an order, you are taken to the [Orders Page](https://portal.telnyx.com/#/numbers/orders) where all historical orders are listed.

## Phone Number Ordering Restrictions

Telnyx enforces ordering restrictions based on your account verification level to combat fraud and enhance security. Two verification frameworks exist:

- **Level 1 / Level 2 (Legacy)**
- **Trial-Paid-Verified-Enterprise (TPVE)**

Refer to the [Account Verification guide](https://support.telnyx.com/en/articles/1130595-account-verification) to determine your account's verification level.

### +1 Toll-Free Restrictions for Freemail Accounts

Effective September 22, 2025:

- **Freemail accounts created on or after September 22, 2025** — cannot order +1 toll-free numbers, regardless of verification level or framework.
- **Freemail accounts created before September 22, 2025** — still eligible if other account qualifications are met.
- **Non-freemail (corporate/custom domain) accounts** — still eligible if other qualifications are met.

### Level 1 / Level 2 (Legacy) Restrictions

- **Accounts created before March 24, 2025:**
  - L1: Cannot order toll-free numbers; no further restrictions
  - L2: No restrictions
- **Accounts created after March 24, 2025:**
  - L1: Can only order local numbers from their country of origin
  - L2: No restrictions

**Sub users** — ordering restrictions are based on the organization owner's signup date and verification status, not the sub-user's account.

**Managed Accounts** — restrictions are based on each individual Manager or Managed account's own signup date and verification status.

### TPVE Framework Restrictions

If your account is in the TPVE framework, see [Levels and Capabilities](https://developers.telnyx.com/docs/account-setup/levels-and-capabilities) for applicable restrictions and how to upgrade.

## International Number Requirements

International numbers may require documentation to comply with local regulators. While numbers can be purchased, inbound calling will not activate until documentation is uploaded and verified. The verification process can take several working days.

### International Number Requirements Tool

Find this tool in the portal at [Number Requirements](https://portal.telnyx.com/#/app/numbers/requirements). Filter by country to view all documents needed for Local, National, Mobile, or Toll-Free numbers. The tool only returns results for regions that require supplemental information.

### Required Document Overview

Common document categories include:

- Contact information (name, business name, phone numbers)
- Passport or ID copy
- Address (worldwide, local, or matching the DID area code)
- Utility bill (no older than 3 months)
- Company registration certificate
- Fiscal registration / VAT certificate
- Service usage description
- Letter of Intention (LOI)

Requirements vary significantly by country and number type. Some countries restrict registration to business entities only, prohibit outbound calling from the number, or require local identity documents. For the full country-by-country requirement matrix, see the [International DID Requirements collection](https://support.telnyx.com/en/collections/1511606-international-did-requirements).

### International Toll-Free Dialling

International toll-free numbers can generally only be reached from within the country. Local operators may only connect calls in a particular dialled number format (e.g., Germany: `0 800 xxxx xxxxx`, UK: `0 800 xxx xxxx`).

### Local CLI Restrictions

Due to local country regulations, voice calls bearing a local CLI (Caller Line Identification) and terminating to the same country of origin — or bearing no CLI at all — may be rejected by local operators. It is recommended to use an international or different-to-termination-country CLI. If your business requires a local CLI, contact your account manager or [sales@telnyx.com](mailto:sales@telnyx.com).
