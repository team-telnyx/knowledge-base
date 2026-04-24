---
title: Number Search
summary: Tutorial to search for available numbers to purchase.
sources:
  - url: https://developers.telnyx.com/docs/numbers/phone-numbers/number-search/index
    content_hash: e30f608f84cdd651d9ccf25d288edf72dd010fa70ed1dbd2a7e1bf426cf665c4
updated_at: 2026-04-10T00:00:00Z
---

# Number Search

Tutorial to search for available numbers to purchase

Use the [GET v2/available\_phone\_numbers endpoint](https://developers.telnyx.com/api-reference/phone-number-search/list-available-phone-numbers) to search for phone numbers that are available to purchase.

## Constraints

* To order a phone number, it must have been returned in a recent search request
* Country code is always required in search requests. The rest of the fields are optional
* Wildcard characters (\*, %, etc.) are not supported in any of the filters. If a wildcard character is included in a filter, the search will yield 0 results.
* Depending on your [account verification level](https://developers.telnyx.com/docs/account-setup/levels-and-capabilities/index#account-levels-and-capabilities), search results may be limited.

## Best Practices

* When supported, use the [inventory coverage API](https://developers.telnyx.com/api-reference/inventory-level/create-an-inventory-coverage-request#create-an-inventory-coverage-request) to list possible values for a variety of filters, including area code and city.
* Use the `features` filter (filter\[features]) to search for phone numbers with capabilities that satisfy your use case
  * If you need phone numbers that are able to place outbound calls, search for phone numbers with `emergency` as a feature
  * If you need phone numbers that are SMS capable, search for phone numbers with `sms` as a feature. Any phone number with `sms` as a feature should be capable and ready to immediately leverage SMS.
* For US toll-free phone numbers, we recommend using the `quickship` filter (filter\[quickship]=true) in your search request. In doing so, you will be purchasing a phone number that is pre-provisioned and usable immediately. If you can’t find what you are looking for, you can disable the quickship filter to expand the possible search results. Just be aware that it could take up to 2 business days for a non-quickship toll-free phone number to be fully active after purchase.
* Not all phone numbers are the same price. Review the `cost_information` object  in the API response to see how much each phone number will cost before purchasing.

## Filter for specific phone numbers

There are a variety of filters to narrow down your search and find your desired number.

### Required Filters

* **Country Code (**`filter[country_code]`**)**: Search for phone numbers in a specific country. This filter must be included in every search. Use [ISO 3166 2 letter](https://www.iban.com/country-codes) country codes.

### Standard Filters

* **Feature (**`filter[features]`**)**: Phone numbers have varying capabilities. Filter for phone numbers that have the features to satisfy your use case. I.e. “sms” will return phone numbers that support SMS, “emergency” will return phone numbers capable of placing emergency calls, etc.
* **Type (**`filter[phone_number_type]`**)**: Filter for a specific type of phone number. I.e. “local” will return local/geographic phone numbers, “toll-free” will return toll-free phone numbers only, etc.
* **Area Code (**`filter[national_destination_code]`**)**: Search for phone numbers in a given area code. I.e. “205” will return phone numbers with a “205” area code
* **City / Region (**`filter[locality]`**)**: Search for phone numbers in a given city / region / rate center. I.e. “Boston” would return phone numbers in or near Boston, MA.
* **\[US/CA only] State / Province (**`filter[administrative_area]`**)**: Search for phone numbers in a given state / province. I.e. filtering for “MA” will return phone numbers in Massachusetts.

### Advanced Filters

* **Starts with (**`filter[starts_with]`**)**: “56” will return numbers starting with “56”, i.e. +1-312-562-0011. Couple of things to note:
  * Never include the country code (i.e. “+1”) in the search filter.
  * If you are using the Area Code filter in conjunction with the Starts with filter, do not include the area code digits in the starts with filter. I.e. if you wanted to find +1-312-562-0011, you would use Area Code = 312 and Starts With = 562.
  * If you are not using the Area Code filter, include the area code digits in the starts with filter. I.e. if you wanted to find +1-312-562-0011, you would use Starts With = 312562.
* **Ends with (**`filter[ends_with]`**)**: “356” will return numbers ending with “356”, i.e. +1-312-562-0356.
* **Contains (**`filter[contains]`**)**: “56” will return numbers matching “5” and ”6” anywhere, i.e. +1-312-622-0533.
* **Consecutive Numbers (**`filter[consecutive]`**)**: Range of successive phone numbers. I.e. entering “3” will return +1-312-562-0011, +1-312-562-0012, and +1-312-562-0013 in the search results
* **Results Limit (**`filter[limit]`**)**: Define the maximum quantity of phone numbers in the search results. I.e. “2” will return a maximum of 2 phone numbers in your search results
* **\[US / CA only] Best Effort (**`filter[best_effort]`**)**: Telnyx may not have phone numbers that meet your exact search criteria. If that’s the case and “Best Effort” is toggled on, Telnyx will return similar results that meet some of your criteria.
* **\[US toll-free only] Quickship (**`filter[quickship]`**)**: When “Quickship” is toggled on, the toll-free phone numbers returned in search are pre-provisioned and ready for immediate activation. When “Quickship” is toggled off, a phone number may be returned that is not pre-provisioned. If that phone number is purchased, it can take up to 2 business days for provisioning to complete and the phone number to be usable. If the filter is toggled on and you are searching for something that isn’t a US toll-free phone number, then the filter will be ignored.
* **Reservable Numbers (**`filter[reservable]`**)**: Returns phone numbers that are eligible to be reserved. When a phone number is reserved, you will have exclusive rights to search and order the phone number for a period of 30 minutes. More details [here](https://developers.telnyx.com/docs/numbers/phone-numbers/number-reservations).
* **Exclude Held Numbers (**`filter[exclude_held_numbers]`**)**: A phone number can be on "hold" in two instances. Either the phone number was recently deleted and is in the process of being recycled. Or the phone number was placed on hold by Telnyx's Number Ops team for you to search and purchase. Enabling this filter will exclude any phone numbers in a "hold" status from the search results.
* **Held / Reserved (**`filter[only_reserved_numbers]`**)**: Returns phone numbers that are already set aside for the requesting customer, meaning numbers currently in either hold status (e.g., recently deleted numbers still in the recovery/grace period, or numbers placed on hold by Number Ops) or reserved status. Use this filter to surface numbers you can reclaim or repurchase before they return to general availability.


## Related Pages

- [Number Reservations](../runbooks/number-reservations.md)
- [Number Orders](../runbooks/number-orders.md)
- [Number Reputation](../runbooks/number-reputation.md)
