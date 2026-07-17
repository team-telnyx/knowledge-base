---
title: Phone Numbers and Porting
summary: This page consolidates Telnyx developer documentation covering phone number
  search, ordering, reservations, bulk and advanced orders, regulatory requirements,
  requirement groups, documents, port-in and port-out workflows, and the notifications
  and events that track them. It provides an end-to-end reference for purchasing numbers,
  fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and
  monitoring the lifecycle of those operations via webhooks and events.
sources:
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/action-ordering-requirement
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/advanced-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/bulk-ordering
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/buy-phone-number
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/documents/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/getting-started/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-orders
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-search/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/regulatory-requirements/index
- url: https://developers.telnyx.com/docs/numbers/phone-numbers/requirement-groups
- url: https://developers.telnyx.com/docs/numbers/porting/allowed-foc-dates
- url: https://developers.telnyx.com/docs/numbers/porting/bundles-porting
- url: https://developers.telnyx.com/docs/numbers/porting/cancel-port-order
- url: https://developers.telnyx.com/docs/numbers/porting/extensions
- url: https://developers.telnyx.com/docs/numbers/porting/getting-started/index
- url: https://developers.telnyx.com/docs/numbers/porting/messaging-porting
- url: https://developers.telnyx.com/docs/numbers/porting/on-demand-activations
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-blocks
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-in-requirements
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-events
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-notifications
- url: https://developers.telnyx.com/docs/numbers/porting/port-out-quickstart/index
- url: https://developers.telnyx.com/docs/numbers/porting/porting-additional-steps/index
updated_at: 2026-07-17T09:16:33Z
---

# Phone Numbers and Porting

*Part 1 of 11 — see also: [Part 2](phone-numbers-and-porting--part-2.md), [Part 3](phone-numbers-and-porting--part-3.md), [Part 4](phone-numbers-and-porting--part-4.md), [Part 5](phone-numbers-and-porting--part-5.md), [Part 6](phone-numbers-and-porting--part-6.md), [Part 7](phone-numbers-and-porting--part-7.md), [Part 8](phone-numbers-and-porting--part-8.md), [Part 9](phone-numbers-and-porting--part-9.md), [Part 10](phone-numbers-and-porting--part-10.md), [Part 11](phone-numbers-and-porting--part-11.md)*

This page consolidates Telnyx developer documentation covering phone number search, ordering, reservations, bulk and advanced orders, regulatory requirements, requirement groups, documents, port-in and port-out workflows, and the notifications and events that track them. It provides an end-to-end reference for purchasing numbers, fulfilling regulatory requirements, transferring numbers in and out of Telnyx, and monitoring the lifecycle of those operations via webhooks and events.

## Overview

Telnyx provides a comprehensive set of APIs and workflows for purchasing phone numbers, porting numbers in and out, and managing the regulatory requirements that govern these operations. This page consolidates the developer guides covering number search, ordering, reservations, bulk and advanced orders, regulatory requirements, requirement groups, documents, port-in workflows, port-out workflows, and the notifications and events that track them.

## Coverage and Number Search

Telnyx sells phone numbers in 100+ countries across multiple phone number types. To see a list of supported countries and number types, query the [Get Country Coverage API](https://developers.telnyx.com/api-reference/country-coverage/get-country-coverage). The response includes the countries, available phone number types within each country, applicable phone number attributes, and whether the inventory coverage API is supported. When inventory coverage is supported, use the [Inventory Coverage API](https://developers.telnyx.com/api-reference/inventory-level/create-an-inventory-coverage-request) to assess how many numbers are available based on your search criteria.

Use the [GET v2/available_phone_numbers endpoint](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers) to search for phone numbers that are available to purchase. Country code is always required in search requests; the rest of the fields are optional. Wildcard characters (`*`, `%`, etc.) are not supported in any of the filters. Depending on your account verification level, search results may be limited.

### Best Practices

- When supported, use the inventory coverage API to list possible values for a variety of filters, including area code and city.
- Use the `features` filter (`filter[features]`) to search for phone numbers with capabilities that satisfy your use case. For example, search for `emergency` to find numbers that can place outbound calls, or `sms` to find SMS-capable numbers.
- For US toll-free phone numbers, use the `quickship` filter (`filter[quickship]=true`) to purchase a pre-provisioned number that is usable immediately. If you cannot find what you are looking for, disable the quickship filter to expand results, but be aware that non-quickship toll-free numbers can take up to 2 business days to fully activate.
- Not all phone numbers are the same price. Review the `cost_information` object in the API response to see how much each phone number will cost before purchasing.

### Search Filters

**Required filters:**

- **Country Code (`filter[country_code]`)**: Search for phone numbers in a specific country. This filter must be included in every search. Use ISO 3166 two-letter country codes.

**Standard filters:**

- **Feature (`filter[features]`)**: Filter for phone numbers with specific capabilities (e.g., `sms`, `emergency`).
- **Type (`filter[phone_number_type]`)**: Filter for a specific type of phone number (e.g., `local`, `toll-free`).
- **Area Code (`filter[national_destination_code]`)**: Search for phone numbers in a given area code.
- **City / Region (`filter[locality]`)**: Search for phone numbers in a given city, region, or rate center.
- **[US/CA only] State / Province (`filter[administrative_area]`)**: Search for phone numbers in a given state or province.

**Advanced filters:**

- **Starts with (`filter[starts_with]`)**: Returns numbers starting with the given digits. Never include the country code. If using the Area Code filter, do not include the area code digits in the starts with filter.
- **Ends with (`filter[ends_with]`)**: Returns numbers ending with the given digits.
- **Contains (`filter[contains]`)**: Returns numbers matching the given digits anywhere.
- **Consecutive Numbers (`filter[consecutive]`)**: Range of successive phone numbers.
- **Results Limit (`filter[limit]`)**: Define the maximum quantity of phone numbers in the search results.
- **[US / CA only] Best Effort (`filter[best_effort]`)**: Returns similar results that meet some of your criteria if exact matches are unavailable.
- **[US toll-free only] Quickship (`filter[quickship]`)**: Returns pre-provisioned toll-free numbers ready for immediate activation.
- **Reservable Numbers (`filter[reservable]`)**: Returns phone numbers eligible to be reserved.
- **Exclude Held Numbers (`filter[exclude_held_numbers]`)**: Excludes phone numbers in a "hold" status (recently deleted and being recycled, or placed on hold by Number Ops).
- **Held / Reserved (`filter[only_reserved_numbers]`)**: Returns phone numbers already set aside for the requesting customer, including those in hold or reserved status.

## Buying a Phone Number

### Via Mission Control Portal

1. Navigate to **Real-Time Communication** > **Numbers** > **Buy Numbers** in the left sidebar.
2. Select your search criteria: Country, Features (SMS, Voice, Fax, etc.), Number type (Local, Toll-Free, etc.), State/Region, and City/Area Code.
3. Click **Search**.
4. Choose a number from the results.
5. Click **Add to Cart** next to your chosen number.
6. Confirm the purchase by clicking **Place Order**.

### Via API

You can also purchase numbers programmatically:

```
# Search for available numbers
curl -X GET \
  --header "Authorization: Bearer your_api_key" \
  "https://api.telnyx.com/v2/available_phone_numbers?filter[country_code]=US&filter[locality]=Chicago"

# Purchase a specific number
curl -X POST \
  --header "Content-Type: application/json" \
  --header "Authorization: Bearer your_api_key" \
  --data '{
    "phone_numbers": [{"phone_number": "+13125551234"}]
  }' \
  "https://api.telnyx.com/v2/number_orders"
```

After purchasing your phone number, you will typically need to assign it to a Voice API Application or SIP Connection for voice applications, configure it with a Messaging Profile for messaging, or set up Fax Application settings for fax.

## Number Reservations

The Phone Number Reservations API lets you reserve phone numbers for 30 minutes. During this period, you have exclusive rights to search for and order the reserved phone number. After 30 minutes, the number is returned to the `available` pool. Not all phone numbers are reservable.

To ensure only reservable phone numbers are included in your search results, add the filters `filter[reservable]=true` and `filter[exclude_held_numbers]=true` to your search request.

To reserve one or more phone numbers, send a `POST https://api.telnyx.com/v2/number_reservations` request. Important attributes in the API response include:

- `id`: Unique ID associated with the overall number reservation request.
- `status`: Status of the overall reservation request.
- `phone_numbers[].status`: Status of the individual phone number reservation.
- `phone_numbers[].expired_at`: Expiration timestamp for the individual phone number reservation.

When the request is submitted, each phone number will be individually attempted for reservation. Some phone numbers may fail to be reserved (e.g., already purchased or reserved). In such cases, the `phone_numbers[].status` will be `failed`, and the overall request `status` will be `partial_success`.

To view a list of all your number reservations, send a `GET https://api.telnyx.com/v2/number_reservations` request. To extend your reservation by another 30 minutes, send a `POST https://api.telnyx.com/v2/number_reservations/{{id}}/actions/extend` request.
