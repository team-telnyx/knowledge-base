---
title: 'Telnyx Phone Numbers: Ordering, E911, and Number Management'
summary: This page consolidates Telnyx guidance on phone number ordering, including
  account verification restrictions, searching and buying numbers, requirement groups,
  working with the numbering team, E911 address registration and setup, testing E911
  with 933, handling spam/scam-likely flags, and managing numbers through the My Numbers
  Page.
sources:
- url: https://support.telnyx.com/en/articles/10715715-phone-number-ordering-restrictions
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- url: https://support.telnyx.com/en/articles/4088988-telnyx-how-to-handle-spam-scam-likely
- url: https://support.telnyx.com/en/articles/4294429-addresses-overview
- url: https://support.telnyx.com/en/articles/4349113-my-numbers-page
- url: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
- url: https://support.telnyx.com/en/articles/7205411-numbering-team-best-practices
- url: https://support.telnyx.com/en/articles/9801714-requirement-groups-for-ordering-phone-numbers
updated_at: 2026-07-17T09:01:25Z
---

# Telnyx Phone Numbers: Ordering, E911, and Number Management

*Part 1 of 6 — see also: [Part 2](telnyx-phone-numbers-ordering-e911-and-number-management--part-2.md), [Part 3](telnyx-phone-numbers-ordering-e911-and-number-management--part-3.md), [Part 4](telnyx-phone-numbers-ordering-e911-and-number-management--part-4.md), [Part 5](telnyx-phone-numbers-ordering-e911-and-number-management--part-5.md), [Part 6](telnyx-phone-numbers-ordering-e911-and-number-management--part-6.md)*

This page consolidates Telnyx guidance on phone number ordering, including account verification restrictions, searching and buying numbers, requirement groups, working with the numbering team, E911 address registration and setup, testing E911 with 933, handling spam/scam-likely flags, and managing numbers through the My Numbers Page.

## Phone Number Ordering Restrictions

Telnyx has introduced phone number ordering restrictions to combat fraudulent activity and enhance platform security. Restrictions are enforced based on your account verification level, which falls under one of two frameworks:

- The Level 1 / Level 2 framework (Legacy)
- The Trial-Paid-Verified-Enterprise (TPVE) framework

Refer to [Account Verification](account-verification.md) to determine your account's verification level.

### +1 Toll-Free Ordering Restrictions

Effective September 22, 2025, accounts created with a freemail domain (e.g., gmail.com, yahoo.com, outlook.com) face restrictions when ordering +1 toll-free phone numbers:

- **Freemail accounts created on or after September 22, 2025** cannot order +1 toll-free phone numbers, regardless of verification level or framework.
- **Freemail accounts created before September 22, 2025** remain eligible if they meet other account qualifications.
- **Non-freemail accounts (corporate or custom domains)** remain eligible if they meet other account qualifications.

### Level 1 / Level 2 (Legacy) Ordering Restrictions

- **Accounts created after March 24, 2025 with Level 1 (L1) status** can only order local phone numbers in their account's country of origin.
- **Pre-existing L1 accounts (created before March 24, 2025)** cannot order toll-free phone numbers. Telnyx reserves the right to update these restrictions.
- **All Level 2 (L2) accounts** have no ordering restrictions.

**Sub users:** Ordering restrictions are based on the organization owner's account signup date and verification status, not the sub user's account.

**Managed Accounts:** Restrictions are based on the signup date and verification status of each individual ManagER or ManagED account.

### TPVE Ordering Restrictions

If your account is part of the Trial-Paid-Verified-Enterprise (TPVE) framework, refer to the [TPVE levels and capabilities documentation](https://developers.telnyx.com/docs/account-setup/levels-and-capabilities) for details on applicable restrictions and how to upgrade.

## Searching and Buying Phone Numbers

The [My Numbers Page](my-numbers-page.md) in Mission Control lists all procured numbers. From there, click **Buy Number** or **Search Numbers** to open the Search & Buy Numbers page.

### Search Options

The Search & Buy Numbers page provides five search types:

- **Country** (required)
- **Features**
- **Type**
- **Search By**
- **Area Code**

**Local Numbers** can be searched by Area Code, City/Region, or State/Province (US only).

**Toll-Free Numbers** can be searched by country and pattern using the Advanced Search feature.

### Advanced Search

The Advanced Search feature works for both toll-free and local number types and enables you to:

- Search for vanity numbers or specific digits within a phone number
- Specify consecutive numbers (e.g., 555-7345, 555-7346, 555-7347)
- Set a results limit (currently 100 results max)
- Toggle **Best Effort** searches to return numbers in a nearby rate center or area code if no exact match is found
- Enable **Quickship** to return toll-free numbers with voice/fax capabilities instantly provisioned
- Toggle **Reservable Numbers** to hold numbers for 30 minutes (extendable by another 30 minutes) before purchasing
- **Exclude Held Numbers** to avoid recently deleted numbers that are held on your account for up to 15 days
- Search **Telnyx Bundles** for bundles containing numbers, features, and minutes (excludes premium NPA TNs)

### Cart and Ordering

Add numbers to your cart using the **Add to Cart** button. In the cart, you can:

- Empty the cart or delete individual numbers
- Select a Connection or Messaging Profile to auto-assign to the numbers
- Review the **Upfront Cost** (one-time activation) and **Monthly Cost** (recurring)
- View the **Order Summary** and click **Place Order**

Orders are final and non-refundable. Telnyx recommends ordering no more than 50 numbers at a time through the cart; larger orders may result in purchase failures or incorrect assignment of Connections/Messaging Profiles. For bulk orders beyond 50 numbers, contact the sales team.

### Orders Page

After placing an order, you are taken to the [Orders Page](https://portal.telnyx.com/#/numbers/orders), which lists every order ever processed, including order date, time, quantity, and order ID. Click an order ID or "details" to verify which numbers were purchased.

### Deleting and Restoring Numbers

To delete a number, visit the [My Numbers Page](my-numbers-page.md), filter for the number, and click the trash icon. Deleted numbers no longer incur monthly recurring charges.

You have **15 days** to repurchase accidentally deleted numbers. Restored numbers will incur charges again, and international numbers require resubmission of documentation. A prorated monthly recurring charge applies based on the repurchase date.

To restore deleted numbers, use Advanced Search on the Search & Buy Numbers page:

1. Specify the Country
2. Search by Area Code
3. Under Advanced Search, set Phone Number to **Contains**
4. Input the number you're looking for
5. Click **Search Numbers**

It may take a few minutes after deletion for the number to reappear in search results. If the number does not appear within 15 days, email [numbering@telnyx.com](mailto:numbering@telnyx.com) for assistance. For bulk deletes, use the [API](https://developers.telnyx.com/api-reference/phone-number-configurations/delete-a-phone-number) or the bulk edit guide.

### International Requirements

When ordering numbers outside North America, you may be prompted to provide additional information to comply with local regulatory requirements by a set deadline. See the [International DID Requirements collection](https://support.telnyx.com/en/collections/1511606-international-did-requirements) for country-specific requirements.

Numbers requiring further documentation display a warning note in the portal. After purchase, go to the Orders Page, click the phone number with Pending status, and add the required documentation on the Orders Requirement page. Requirements may include:

- Contact Information
- Address matching the phone number purchased
- Proof of identification
- Company registration certificate
- Business Use Case
- Company Website

You can also start a conversation with the numbering team using the Communications functionality on the same page. Numbers without proper documentation may not be activated, and inbound call capabilities may not work as expected.
