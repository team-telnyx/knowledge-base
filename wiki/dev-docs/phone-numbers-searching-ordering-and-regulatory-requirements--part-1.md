---
title: 'Phone Numbers: Searching, Ordering, and Regulatory Requirements'
summary: This page covers the end-to-end workflow for purchasing phone numbers on
  Telnyx, including searching inventory, reserving numbers, placing standard, bulk,
  and advanced orders, fulfilling regulatory requirements (textual, address, document,
  and action types), uploading supporting documents, and configuring webhook notifications.
sources:
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/bulk-ordering
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/buy-phone-number
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/documents/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-search/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements
updated_at: 2026-08-05T14:00:16Z
---

# Phone Numbers: Searching, Ordering, and Regulatory Requirements

*Part 1 of 6 — see also: [Part 2](phone-numbers-searching-ordering-and-regulatory-requirements--part-2.md), [Part 3](phone-numbers-searching-ordering-and-regulatory-requirements--part-3.md), [Part 4](phone-numbers-searching-ordering-and-regulatory-requirements--part-4.md), [Part 5](phone-numbers-searching-ordering-and-regulatory-requirements--part-5.md), [Part 6](phone-numbers-searching-ordering-and-regulatory-requirements--part-6.md)*

This page covers the end-to-end workflow for purchasing phone numbers on Telnyx, including searching inventory, reserving numbers, placing standard, bulk, and advanced orders, fulfilling regulatory requirements (textual, address, document, and action types), uploading supporting documents, and configuring webhook notifications.

## Overview

Telnyx sells phone numbers in 100+ countries across multiple phone number types. To see a list of supported countries and number types, query the [Get Country Coverage API](https://developers.telnyx.com/api-reference/country-coverage/get-country-coverage). The response includes the available phone number types within each country, applicable phone number attributes, and whether the inventory coverage API is supported. If inventory coverage is supported, use the [Inventory Coverage API](https://developers.telnyx.com/api-reference/inventory-level/create-an-inventory-coverage-request) to assess how many numbers are available based on your search criteria.

The standard purchasing workflow is: search for available numbers, optionally reserve them, then create a number order. If no numbers match your search, you can submit an Advanced Order for the Number Operations team to attempt to source them, or use a Bulk Order (US/CA only) to specify search criteria and quantity. Most countries also require regulatory information to be collected before numbers can be activated.

## Searching for Phone Numbers

Use the [GET v2/available_phone_numbers endpoint](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers) to search for phone numbers that are available to purchase.

### Constraints

- To order a phone number, it must have been returned in a recent search request.
- Country code is always required in search requests. The rest of the fields are optional.
- Wildcard characters (`*`, `%`, etc.) are not supported in any of the filters. If a wildcard character is included in a filter, the search will yield 0 results.
- Depending on your [account verification level](https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/index#account-levels-and-capabilities), search results may be limited.

### Best Practices

- When supported, use the [inventory coverage API](https://developers.telnyx.com/api-reference/inventory-level/create-an-inventory-coverage-request) to list possible values for a variety of filters, including area code and city.
- Use the `features` filter (`filter[features]`) to search for phone numbers with capabilities that satisfy your use case. For example, search for `emergency` to find numbers that can place outbound calls, or `sms` to find SMS-capable numbers.
- For US toll-free phone numbers, use the `quickship` filter (`filter[quickship]=true`) to purchase a pre-provisioned number that is usable immediately. If you cannot find what you are looking for, disable the quickship filter to expand results, but be aware that non-quickship toll-free numbers can take up to 2 business days to fully activate after purchase.
- Not all phone numbers are the same price. Review the `cost_information` object in the API response to see how much each phone number will cost before purchasing.

### Filters

**Required:**

- **Country Code (`filter[country_code]`)**: Search for phone numbers in a specific country. This filter must be included in every search. Use [ISO 3166 2 letter](https://www.iban.com/country-codes) country codes.

**Standard:**

- **Feature (`filter[features]`)**: Filter for phone numbers that have the features to satisfy your use case (e.g., `sms`, `emergency`).
- **Type (`filter[phone_number_type]`)**: Filter for a specific type of phone number (e.g., `local`, `toll-free`).
- **Area Code (`filter[national_destination_code]`)**: Search for phone numbers in a given area code (e.g., `205`).
- **City / Region (`filter[locality]`)**: Search for phone numbers in a given city / region / rate center (e.g., `Boston`).
- **[US/CA only] State / Province (`filter[administrative_area]`)**: Search for phone numbers in a given state / province (e.g., `MA` for Massachusetts).

**Advanced:**

- **Starts with (`filter[starts_with]`)**: Returns numbers starting with the given digits. Never include the country code. If using the Area Code filter, do not include the area code digits in the starts with filter.
- **Ends with (`filter[ends_with]`)**: Returns numbers ending with the given digits.
- **Contains (`filter[contains]`)**: Returns numbers matching the given digits anywhere.
- **Consecutive Numbers (`filter[consecutive]`)**: Range of successive phone numbers (e.g., `3` returns three consecutive numbers).
- **Results Limit (`filter[limit]`)**: Define the maximum quantity of phone numbers in the search results.
- **[US / CA only] Best Effort (`filter[best_effort]`)**: When toggled on, Telnyx returns similar results that meet some of your criteria if no exact matches exist.
- **[US toll-free only] Quickship (`filter[quickship]`)**: When toggled on, returned toll-free numbers are pre-provisioned and ready for immediate activation. If toggled on for non-US toll-free searches, the filter is ignored.
- **Reservable Numbers (`filter[reservable]`)**: Returns phone numbers that are eligible to be reserved.
- **Exclude Held Numbers (`filter[exclude_held_numbers]`)**: Excludes phone numbers in a "hold" status (recently deleted and being recycled, or placed on hold by Number Ops).
- **Held / Reserved (`filter[only_reserved_numbers]`)**: Returns phone numbers already set aside for the requesting customer, including numbers in hold or reserved status.

## Reserving Phone Numbers

The Phone Number Reservations API lets you reserve phone numbers for 30 minutes. During this period, you have exclusive rights to search for and order the reserved phone number. After 30 minutes, the number is returned to the `available` pool.

### Constraints

- Not all phone numbers are reservable.
- Reservations expire after 30 minutes.

### Reservation Flow

1. **Search for reservable phone numbers.** Add the filters `filter[reservable]=true` and `filter[exclude_held_numbers]=true` to your search request to ensure only reservable phone numbers are included.
2. **Create a reservation.** Send a `POST https://api.telnyx.com/v2/number_reservations` request ([API reference](https://developers.telnyx.com/api-reference/phone-number-reservations/create-a-number-reservation)). Important response attributes include:
   - `id`: Unique ID associated with the overall number reservation request.
   - `status`: Status of the overall reservation request.
   - `phone_numbers[].status`: Status of the individual phone number reservation.
   - `phone_numbers[].expired_at`: Expiration timestamp for the individual phone number reservation.

   Each phone number is individually attempted for reservation. Some may fail (e.g., already purchased or reserved), in which case `phone_numbers[].status` will be `failed` and the overall request `status` will be `partial_success`.

3. **List all reservations.** Send a `GET https://api.telnyx.com/v2/number_reservations` request ([API reference](https://developers.telnyx.com/api-reference/phone-number-reservations/list-number-reservations)).
4. **Extend a reservation.** Send a `POST https://api.telnyx.com/v2/number_reservations/{{id}}/actions/extend` request ([API reference](https://developers.telnyx.com/api-reference/phone-number-reservations/extend-a-number-reservation)) to extend the reservation by another 30 minutes.
