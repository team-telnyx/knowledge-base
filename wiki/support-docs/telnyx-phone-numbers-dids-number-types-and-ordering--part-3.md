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

*Part 3 of 5 — see also: [Part 1](telnyx-phone-numbers-dids-number-types-and-ordering--part-1.md), [Part 2](telnyx-phone-numbers-dids-number-types-and-ordering--part-2.md), [Part 4](telnyx-phone-numbers-dids-number-types-and-ordering--part-4.md), [Part 5](telnyx-phone-numbers-dids-number-types-and-ordering--part-5.md)*

A consolidated reference covering what DIDs are, the global number types Telnyx offers, how to search and buy numbers, how to request numbers that are unavailable, country-specific documentation requirements for international numbers, and best practices for working with the Telnyx numbering team.

## Requesting Numbers (Advanced Orders)

If no phone number results are returned from your search request, you have the option to submit a direct DID request from your account. When you click **Request Number**, a form will pop up. Fill out the form and specify the phone numbers you would like to purchase. The Number Operations team will use these details as they try to acquire the phone numbers on your behalf.

By submitting this form, you create an **Advanced Order**. Each Advanced Order has its own unique ID for tracking. You can view your account's Advanced Orders [via the portal](https://portal.telnyx.com/#/numbers/advanced-orders) or via the [Advanced Order API](https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders).

The Number Operations team will review your request within 3-5 business days. They will attempt to acquire the phone number(s) you requested. These requests are best effort, and Telnyx cannot guarantee fulfillment.

If the Number Operations team can fulfill your request, they will place a number order for the requested phone numbers on your account. If regulatory requirements apply, the order will remain in a "pending" state until you provide the required information. A successful advanced order confirms that the order was placed, but it will not be completed until all regulatory requirements are met.

Telnyx also offers contiguous blocks, typically sold in increments of 10, 25, 50, or 100.

### Advanced Order FAQ

**Q: I want to receive notifications for my advanced orders. Is that possible?**

A: Yes. You can set up webhook and/or email notifications for advanced order events. See the [Notifications section of the developer guide](https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders#notifications) and the [Notification Settings](notification-settings.md) article for more details.

**Q: Why am I being asked for regulatory requirements? How do I provide those?**

A: In some cases, the Number Operations team needs your regulatory requirements in advance to secure the phone numbers you have requested. To provide regulatory requirements: (1) create a [requirement group](https://portal.telnyx.com/#/numbers/requirements/requirement-groups) for the phone numbers you are requesting, (2) fill in the requirement group, and (3) update your Advanced Order with that requirement group.

## International Number Requirements Tool

The International Number Requirements Tool is available in your portal account [here](https://portal.telnyx.com/#/app/numbers/requirements?enableAlerts=true).

As a global carrier, Telnyx offers customers the ability to purchase or port a wide variety of phone numbers across the globe. Depending on the country and number type, you may be required to provide additional information or documentation for orders to successfully process and phone numbers to activate.

This tool allows Telnyx users to view the supplemental information or documentation required to activate numbers ahead of time, helping customers better plan number ports and orders to avoid unforeseen wait times.

Filter by the country or countries you want to buy a number in, click **Apply Filters**, then click on the returned result. You will see a list of all relevant documents needed to acquire or port a Local, National, Mobile, or Toll-Free number relating to that country.

**Please note:**

- This tool only retrieves information on numbers in regions that require supplemental information for number porting and ordering. Countries with no requirements will return as null in this table.
- For questions about country coverage, [reach out](https://telnyx.com/contact-us) to a member of the sales team.
