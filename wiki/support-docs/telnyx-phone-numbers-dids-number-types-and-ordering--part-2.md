---
title: 'Telnyx Phone Numbers: DIDs, Number Types, and Ordering'
summary: A consolidated reference covering what DIDs are, the global number types
  Telnyx offers, how to search and buy numbers, how to request numbers that are unavailable,
  country-specific documentation requirements for international numbers, and best
  practices for working with the Telnyx numbering team.
sources:
- url: https://support.telnyx.com/en/articles/1130626-international-number-porting-required-documents
- url: https://support.telnyx.com/en/articles/1130699-did-numbers-that-telnyx-offers
- url: https://support.telnyx.com/en/articles/1130702-where-can-i-buy-dids-in-the-us-canada
- url: https://support.telnyx.com/en/articles/1130703-can-i-call-toll-free-with-my-telnyx-number
- url: https://support.telnyx.com/en/articles/1130704-what-is-a-did
- url: https://support.telnyx.com/en/articles/1458084-global-number-types
- url: https://support.telnyx.com/en/articles/3562148-requesting-numbers
- url: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
- url: https://support.telnyx.com/en/articles/5469551-international-numbers-required-documents
- url: https://support.telnyx.com/en/articles/5820047-find-gb-numbers-on-telnyx-portal
- url: https://support.telnyx.com/en/articles/7003167-international-number-requirements-tool
- url: https://support.telnyx.com/en/articles/7205411-numbering-team-best-practices
updated_at: 2026-08-05T13:28:46Z
---

# Telnyx Phone Numbers: DIDs, Number Types, and Ordering

*Part 2 of 5 — see also: [Part 1](telnyx-phone-numbers-dids-number-types-and-ordering--part-1.md), [Part 3](telnyx-phone-numbers-dids-number-types-and-ordering--part-3.md), [Part 4](telnyx-phone-numbers-dids-number-types-and-ordering--part-4.md), [Part 5](telnyx-phone-numbers-dids-number-types-and-ordering--part-5.md)*

A consolidated reference covering what DIDs are, the global number types Telnyx offers, how to search and buy numbers, how to request numbers that are unavailable, country-specific documentation requirements for international numbers, and best practices for working with the Telnyx numbering team.

## Searching and Buying Numbers

The [My Numbers](my-numbers.md) section of Mission Control houses all of the phone numbers you have purchased or ported to Telnyx. From there, click **Buy Number** in the top right or **Search Numbers** to begin.

### Number Search Options

The Search & Buy Numbers page provides five search types:

- **Country** (required)
- **Features**
- **Type**
- **Search By**
- **Area Code**

**Country:** Choose the country in the dropdown where you want to find a phone number. This is the only required field.

**Features:** Choose one or multiple features to ensure the number aligns with your use case.

**Number Type:** Choose the number type you are looking to purchase.

### Local Numbers

Choosing Local Numbers enables you to search by Area Code, City/Region, or State/Province.

- **Search by Area Code:** Search via the Area Code dropdown or type the area code directly.
- **Search by City/Region:** Type the City, Region, or Rate Center; the portal will autogenerate options as you type.
- **Search by State/Province:** Search for the state or province you are interested in (US only for now).

### Toll-Free Numbers

Choose a country, select Toll-free as the Type, and specify patterns the toll-free numbers should contain under the **Advanced Search** feature.

### Advanced Search

The Advanced Search feature works for both Toll-free and Local number types and enables you to:

- Search for vanity numbers or specific digits within a phone number
- Specify how many **Consecutive Numbers** you would like (e.g., 555-7345, 555-7346, 555-7347)
- Specify your **Results limit** (currently 100 results max)
- Toggle **Best Effort** searches to return numbers in a rate center or area code close to your chosen one if no exact match is found
- Enable **Quickship** to return toll-free numbers with voice/fax capabilities instantly provisioned
- Toggle **Reservable Numbers** to reserve numbers for future purchase. With the Telnyx Number Reservations service, you can reserve numbers for 30 minutes and extend reservations for another 30 minutes at no cost
- **Exclude Held Numbers** to return searches for numbers that have not been previously owned. By default, recently deleted numbers may appear in results; Telnyx holds deleted numbers on your account for up to 15 days before they are vetted and released back into general inventory
- **Telnyx Bundles** to search for a bundle that contains numbers, features, and minutes included. Search results will exclude premium NPA TNs

### Cart and Ordering

When satisfied with your search results, click **Add to Cart** to add numbers for purchase. When ready, click your **cart** in the top right-hand corner. Your cart shows the numbers you have chosen, and you can empty the cart or delete individual numbers. You can also select a Connection or Messaging Profile to assign numbers to automatically once the order is processed.

The cart displays the **Upfront Cost** (one-time activation) and **Monthly Cost** (recurring) for each number. The **Order Summary** on the right shows the order total and the **Place Order** button. The order total will be deducted from your balance.

Orders are final, and Telnyx does not provide refunds if a number is purchased by mistake. Review the order summary completely before proceeding.

It is recommended to order no more than **50 numbers** at a time through the cart. Orders over this amount may result in purchase failures (which you are not charged for) or Connections/Messaging Profiles not being assigned correctly. For bulk orders of more than 50 phone numbers, contact the sales team.

### Orders Page

After placing an order, you will be brought to the [Orders Page](https://portal.telnyx.com/#/numbers/orders). Each order you have ever processed will be listed there with the order date, time, and quantity of numbers purchased. Click the order ID or "details" to re-check your order and verify what numbers were purchased.

### Deleting and Restoring Numbers

Visit the [My Numbers Page](my-numbers-page.md) and use the search filters to find the number you want to delete. Click the trash icon on the right. Once deleted, monthly recurring charges will no longer apply.

You have **15 days** to repurchase numbers you may have accidentally deleted. Numbers deleted will reincur charges, and resubmission of documentation will be required if they are international numbers. A prorated monthly recurring charge will be applied depending on your repurchase date.

To restore deleted numbers, use **Advanced Search** on the Search & Buy Numbers Page:

1. Specify the **Country**
2. Search by **Area Code**
3. Under **Advanced Search**, set **Phone Number** to **Contains**
4. Input the number you are looking to purchase
5. Click **Search Numbers**

You may have to wait a couple of minutes after deleting a number for it to return as a search result. If you cannot see the deleted numbers in search results and it has been less than 15 days, email [numbering@telnyx.com](mailto:numbering@telnyx.com) for assistance. For bulk deletes, consider using the [API](https://developers.telnyx.com/api-reference/phone-number-configurations/delete-a-phone-number) or follow the bulk edit guide.

### International Requirements During Ordering

When ordering numbers outside of North America, you may be prompted to provide more information to comply with local regulatory requirements by a set deadline. Numbers that require further documentation will be displayed with a warning note on your portal.

Once purchased, head to the [Orders Page](https://portal.telnyx.com/#/numbers/orders) and click on the phone number with the Pending status. Clicking on that phone number takes you to the **Orders Requirement** page specific to that number where you can add the required documentation. Requirements can generally include, but are not limited to:

- Contact Information
- Address matching the phone number purchased
- Proof of identification
- Company registration certificate
- Business Use Case
- Company Website

You may also start a conversation with the numbering team for any inquiries about documentation requirements using the **Communications** functionality on the same page.

**Please note:** Any number without proper documentation uploaded may not be activated, and inbound call capabilities may not work as expected.
