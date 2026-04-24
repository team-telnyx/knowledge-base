---
title: Fundamentals - Searching + Ordering Phone Numbers
summary: The following concepts must be understood to purchase phone numbers.
sources:
  - url: https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started/index
    content_hash: a60801bda322705a126c4dca336df072ed7ea15a181d9667901d1136e0fa167a
updated_at: 2026-04-10T00:00:00Z
---

# Fundamentals - Searching + Ordering Phone Numbers

The following concepts must be understood to purchase phone numbers.

### Overview:

The following concepts must be understood to purchase phone numbers.

### Coverage

Telnyx sells phone numbers in **100+ countries** across multiple phone number types.

To see a list of supported countries and number types, query the [Get Country Coverage API](https://developers.telnyx.com/api-reference/country-coverage/get-country-coverage). The response includes:

* Countries
* Available phone number types within each country
* Applicable phone number attributes
* If the inventory coverage API (inventory\_coverage=true) is supported

If inventory coverage is supported, use the [Inventory Coverage API](https://developers.telnyx.com/api-reference/inventory-level/create-an-inventory-coverage-request) to assess how many numbers are available based on your search criteria.

### Regulatory Requirements

Prior to number activation, some phone numbers need additional information to satisfy regulatory requirements. 

**Requirement Resources**

| Feature                                                                                           | Description                                                                               |
| :------------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------- |
| [Compliance Page](https://portal.telnyx.com/#/numbers/requirements)                               | View regulatory requirements for all countries in the Telnyx Portal                       |
| [Developer Guide](https://developers.telnyx.com/api-reference/requirements/list-all-requirements) | Guide discussing regulatory requirements in more detail, including relevant API requests. |
| [Requirement Groups](https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups) | Stores pre-filled regulatory information to be assigned to orders.                        |

### Search

Search for available phone numbers using the [List Available Phone Numbers API](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers) . 

For a deeper dive into search strategies, check out the [Search Guide](https://developers.telnyx.com/docs/numbers/phone-numbers/portal-search-guide).

### Reserve

[Reserve phone numbers](https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations) to block other users from purchasing them. Reservations expire after 30 minutes. Not all phone numbers are reservable. 

### Order

Purchase phone numbers using the [Create Number Order API](https://developers.telnyx.com/api-reference/phone-number-orders/create-a-number-order) . Numbers in the order must come from a prior search for the order to be accepted.

### Advanced Order

Advanced Orders are a fallback mechanism for inventory not found in standard search. These requests are routed to the Number Operations team for manual sourcing and are added to the account upon acquisition.

Submit an [Advanced Order](https://developers.telnyx.com/api-reference/advanced-number-orders/create-advanced-order)  and our Number Operations team will attempt to acquire the numbers you need. Once sourced, they’ll be added directly to your account for activation.

These requests are best effort. Telnyx cannot guarantee that every advanced order will be fulfilled.
