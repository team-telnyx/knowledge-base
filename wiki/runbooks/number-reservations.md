---
title: Number Reservations
summary: The Phone Number Reservations API lets you **reserve** phone numbers for 30 minutes.
sources:
  - url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations/index
    content_hash: 4cfc217c9c522df04f549d9b05f620044ad0435e0909f52bd942b612baa70eef
updated_at: 2026-04-10T00:00:00Z
---

# Number Reservations

## Overview

The Phone Number Reservations API lets you **reserve** phone numbers for 30 minutes. During this period, you have exclusive rights to search for and order the reserved phone number. After 30 minutes, the number is returned to the `available` pool, making it accessible for other users to search for and order.

## Constraints:

* Not all phone numbers are reservable.
* Reservations expire after 30 minutes

## Reservation Flow

### Step 1: Search for reservable phone numbers

To ensure only reservable phone numbers are included in [your search results](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers), add the filters `filter[reservable]=true` and `filter[exclude_held_numbers]=true` to your search request.

### Step 2: Create a reservation

To reserve one or more phone numbers, send a `POST  https://api.telnyx.com/v2/number_reservations` request ([API reference here](https://developers.telnyx.com/api-reference/phone-number-reservations/create-a-number-reservation)).

A couple of important attributes in the API response to consider:

* `id`: Unique ID associated with the overall number reservation request.
* `status`: Status of the overall reservation request.
* `phone_numbers[].status`: status of the individual phone number reservation.
* `phone_numbers[].expired_at`: Expiration timestamp for the individual phone number reservation. Once this timestamp is exceeded, the phone number will be returned to the `available` pool for other users to search and order.

When the request is submitted, each phone number will be individually attempted for reservation.  Some phone numbers may fail to be reserved (i.e., already purchased or reserved). In such cases, the `phone_numbers[].status` will be `failed`, and the overall request `status` will be `partial_success`.

### List all reservations

To view a list of all your number reservations, send a `GET https://api.telnyx.com/v2/number_reservations` request ([API reference here](https://developers.telnyx.com/api-reference/phone-number-reservations/list-number-reservations)).

### Extend a reservation

To extend your reservation by another 30 minutes, send a `POST https://api.telnyx.com/v2/number_reservations/{{id}}/actions/extend` request ([API reference here](https://developers.telnyx.com/api-reference/phone-number-reservations/extend-a-number-reservation)). This request will update the `phone_numbers[].expired_at` timestamp to reflect the additional 30 minutes.


## Related Pages

- [Number Reputation](../runbooks/number-reputation.md)
- [Number Orders](../runbooks/number-orders.md)
- [Phone Number Reputation](../runbooks/phone-number-reputation.md)
- [Number Reputation Settings](../runbooks/number-reputation-settings.md)
- [Number Reputation Quickstart](../tutorial/number-reputation-quickstart.md)
