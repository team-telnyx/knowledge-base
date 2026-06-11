---
title: 'Telnyx Number Management: Search, Ordering, Assignment, and Compliance'
summary: A practical guide to finding, purchasing, assigning, and managing Telnyx
  phone numbers worldwide—including number types and coverage, account-based ordering
  restrictions, international regulatory requirements, advanced (backorder) requests,
  portal management tools, and how to get help.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
- url: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection
- url: https://support.telnyx.com/en/articles/1424680-international-coverage
- url: https://support.telnyx.com/en/articles/1458084-global-number-types
- url: https://support.telnyx.com/en/articles/3562148-requesting-numbers
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
- url: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
- url: https://support.telnyx.com/en/articles/4640720-what-is-an-exhausted-npa
- url: https://support.telnyx.com/en/articles/5820047-find-gb-numbers-on-telnyx-portal
- url: https://support.telnyx.com/en/articles/7003167-international-number-requirements-tool
- url: https://support.telnyx.com/en/articles/7205411-numbering-team-best-practices
- url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
- url: https://support.telnyx.com/en/articles/13795700-accessing-canadian-lrn-data
- url: https://support.telnyx.com/en/collections/3968222-telnyx-number-management-guide
updated_at: 2026-05-20T15:36:51Z
---

# Telnyx Number Management: Search, Ordering, Assignment, and Compliance

*Part 1 of 2 — see also: [Part 2](telnyx-number-management-search-ordering-assignment-and-compliance--part-2.md)*

A practical guide to finding, purchasing, assigning, and managing Telnyx phone numbers worldwide—including number types and coverage, account-based ordering restrictions, international regulatory requirements, advanced (backorder) requests, portal management tools, and how to get help.

## Number types and global coverage
- Domestic long-code (local) numbers for voice, fax, SMS, and MMS across 20k+ US/CA rate centers. See the domestic coverage map at https://telnyx.com/resources/telnyx-domestic-coverage-map.
- Domestic toll-free: Telnyx is a RespOrg (QIT01). Quickship toll-free numbers can be instantly provisioned for voice/fax inbound; if not using quickship, routing can take up to ~1 hour post-order. Quickship is voice-only; test before production. Learn about quickship via API: https://developers.telnyx.com/api/numbers/list-available-phone-number-blocks.
- Toll-free messaging (US/CA): Supported for SMS and MMS but not instantly provisioned. Submit your use case for verification first to avoid filtering/spam blocks. Details: https://support.telnyx.com/en/articles/5353868-toll-free-messaging.
- International number types: Local, national, toll-free, shared-cost, and mobile in many countries. Coverage continues to expand; see https://telnyx.com/global-coverage and the high-level country list at https://support.telnyx.com/en/articles/1424680-international-coverage. Some countries require documentation to activate; you’ll have 10 days to provide required docs after ordering or numbers may be removed.
- Contiguous blocks are available (typically 10, 25, 50, 100).

## Searching and buying numbers in the portal
Access Search & Buy at https://portal.telnyx.com/#/numbers/buy-numbers or via “Buy Number” on My Numbers.

Search inputs
- Country (required)
- Features (e.g., voice, messaging, fax)
- Type (local, toll-free, national, mobile, etc.)
- Search By (area code, city/region, state/province)
- Area Code (for local searches)

Advanced Search options
- Vanity/pattern search and specific digit matching
- Consecutive numbers quantity
- Results limit (up to 100)
- Best Effort (return nearby rate centers/area codes if exact criteria unavailable)
- Quickship (toll-free voice/fax instant provisioning)
- Reservable Numbers (hold results free for 30 minutes; can extend once for another 30 minutes)
- Exclude Held Numbers (omit numbers recently held/deleted on your account)
- Telnyx Bundles (search bundles with numbers, features, minutes; excludes premium NPA)

Cart and order placement
- Assign a SIP Connection and/or Messaging Profile to be auto-applied on fulfillment.
- Upfront (activation) and Monthly (recurring) costs are shown. Orders are final; no refunds for mistakes—review carefully before placing.
- Recommendation: place up to 50 numbers per cart order for best reliability.
- After purchase, track at Orders: https://portal.telnyx.com/#/numbers/orders.

International requirements during/after order
- Some countries require documentation; affected numbers show a warning in the portal.
- Provide required info on the per-number “Order Requirements” page after purchase. Typical items include contact info, matching address, ID, business registration, website, and use case.
- Tooling to discover requirements in advance is covered below.

Deleting and restoring numbers
- Delete from My Numbers to stop monthly charges.
- You have 15 days to repurchase deleted numbers (pro-rated MRC applies; international docs may need re-submission). Use Advanced Search to locate by “Contains” and repurchase. If you don’t see it within a few minutes (and it’s been <15 days), email numbering@telnyx.com for help.

## Ordering restrictions and account verification
Frameworks
- Legacy L1/L2 framework (based on signup date):
  - Accounts created before Mar 24, 2025:
    - L1: Cannot order toll-free; otherwise unrestricted.
    - L2: No restrictions.
  - Accounts created on/after Mar 24, 2025:
    - L1: Can only order local numbers from the account’s country of origin.
    - L2: No restrictions.
- Subusers inherit ordering restrictions from the org owner’s signup date and verification status. Managed Accounts apply restrictions per individual managed/manager account.
- TPVE (Trial–Paid–Verified–Enterprise) framework: see levels, capabilities, and upgrade paths at https://developers.telnyx.com/docs/account-setup/levels-and-capabilities.

+1 toll-free restriction for freemail domains
- Freemail accounts created on/after Sep 22, 2025 (e.g., gmail.com, yahoo.com, outlook.com): cannot order +1 toll-free, regardless of verification/framework.
- Freemail accounts created before Sep 22, 2025 and non-freemail (corporate/custom) domains remain eligible subject to other qualifications.

Account verification reference: https://support.telnyx.com/en/articles/1130595-account-verification.

## International requirements: tools and reusable Requirement Groups
International Number Requirements Tool
- Find country-specific ordering/porting documentation needs ahead of time: https://portal.telnyx.com/#/app/numbers/requirements?enableAlerts=true.
- Collection of requirements by country: https://support.telnyx.com/en/collections/1511606-international-did-requirements.

Requirement Groups (pre-fill once, reuse many orders)
- Create at https://portal.telnyx.com/#/numbers/requirements/requirement-groups.
- A Requirement Group is scoped to a Country + phone_number_type + order_type (e.g., Portugal | local | ordering). Fill required fields/docs once, then select the group for each matching number in your cart.
- Required since Sep 16, 2024 for: Switzerland (CH), Denmark (DK), Italy (IT), Norway (NO), Portugal (PT), Sweden (SE). Optional in most other countries.
- Developer guide: https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups.

## Requesting numbers when inventory is unavailable (Advanced Orders)
- If a search returns no results, click “Request Number” to submit your DID request directly from the portal. This creates an Advanced Order with a unique ID visible at https://portal.telnyx.com/#/numbers/advanced-orders (API: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders).
- Telnyx Number Operations reviews within ~3–5 business days on a best-effort basis; fulfillment is not guaranteed.
- If requirements apply, orders remain pending until you provide the required info. You can pre-create a Requirement Group and associate it with the Advanced Order for faster processing.
- Notifications: configure webhooks and/or emails for Advanced Order events per https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders#notifications and https://support.telnyx.com/en/articles/4277896-notification-settings.

## Assigning DIDs to SIP Connections
- You must assign a registered connection to a DID to receive inbound calls.
- Single DID: on the Numbers page, under the “SIP Connection/App” column, click the pencil icon and choose your connection.
- Multiple DIDs: select checkboxes, click Bulk update, paste numbers (if prompted), choose Edit Voice Settings, select the desired SIP Connection, and Save.
