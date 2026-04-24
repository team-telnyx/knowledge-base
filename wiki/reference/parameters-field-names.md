---
title: Parameters & Field Names
summary: Comprehensive guide to Telnyx API parameter and field naming conventions, data types, and formatting standards.
sources:
  - url: https://developers.telnyx.com/development/api-fundamentals/data-standards/parameters-fields
    content_hash: a1f7d6ee015ed1aae46d7e5329a8ff77ada8360e467ef9e01d3d01d53eac5992
updated_at: 2026-04-10T00:00:00Z
---

# Parameters & Field Names

Comprehensive guide to Telnyx API parameter and field naming conventions, data types, and formatting standards.

The Parameter & Field names section provides an overview of patterns for API request and response parameters and field names.

## Data Types

### Booleans

Boolean values are presented as `true` and `false` values. They will not be `1` or `0` nor will they be strings such as "true" and "false".

### Date-times

All date-times are represented in UTC with precisely the following format: `YYYY-MM-DDThh:mm:ss.fffZ` where `fff` is the first three decimals of the fractional seconds (i.e., millisecond precision).

API V2 accepts date-times in *at least* the following 12 formats:

* `YYYY-MM-DDThh:mm:ss.fffZ`
* `YYYY-MM-DDThh:mm:ssZ`
* `YYYY-MM-DDThh:mmZ`
* The above with `-00`, `-0000`, or `-00:00` instead of the `Z` timezone identifier.

### Times (no date portion)

All times are represented in UTC with precisely the following format: `hh:mm:ss.fffZ` where `fff` is the first three decimals of the fractional seconds (i.e., millisecond precision).

### Durations

If a parameter represents a unit of time, then the unit name should be part of the field name so that the consumer knows what the value represents. For example, a retry timeout value would be named `retry_timeout_secs` or `retry_timeout_millis`.

Valid field suffixes are:

* millis
* secs
* hours
* days
* weeks
* months
* years

API V2 does not use ISO8601 time durations (e.g. `P4Y`, `PT0,42M` or `P3Y6M4DT12H30M5.423S`).

### Time zones

Time zone field names are always spelled as `timezone` and the value is always the Time Zone Database area name spelled out as `Europe/Berlin`, `America/Chicago` for example.

## Date Literals

User-friendly date ranges use this naming convention.

| Date Literal   | Range                                                                                                                                  |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| yesterday      | Starts 00:00:00 the day before and continues for 24 hours.                                                                             |
| today          | Starts 00:00:00 of the current day and continues for 24 hours.                                                                         |
| tomorrow       | Starts 00:00:00 after the current day and continues for 24 hours.                                                                      |
| last\_week     | Starts 00:00:00 on the first day of the week before the most recent first day of the week and continues for seven full days.           |
| this\_week     | Starts 00:00:00 on the most recent first day of the week before the current day and continues for seven full days.                     |
| next\_week     | Starts 00:00:00 on the most recent first day of the week after the current day and continues for seven full days.                      |
| last\_month    | Starts 00:00:00 on the first day of the month before the current day and continues for all the days of that month.                     |
| this\_month    | Starts 00:00:00 on the first day of the month that the current day is in and continues for all the days of that month.                 |
| next\_month    | Starts 00:00:00 on the first day of the month after the month that the current day is in and continues for all the days of that month. |
| last\_N\_hours | For the number n provided, starts at 00 of the last hour and continues for the past n hours.                                           |
| next\_N\_hours | For the number n provided, starts at 00 of the next hour and continues for the next n hours.                                           |
| last\_N\_days  | For the number n provided, starts 00:00:00 of the current day and continues for the past n days.                                       |
| next\_N\_days  | For the number n provided, starts 00:00:00 of the current day and continues for the next n days.                                       |
| last\_N\_weeks | For the number n provided, starts 00:00:00 of the last day of the previous week and continues for the past n weeks.                    |
| next\_N\_weeks | For the number n provided, starts 00:00:00 of the first day of the next week and continues for the next n weeks.                       |

## HTTP Headers

Date-times in HTTP headers follow [RFC-7231 §7.1.1.1](https://www.rfc-editor.org/rfc/rfc7231)'s recommended "IMF-fixdate" format.

An example of the preferred format is

Sun, 06 Nov 1994 08:49:37 GMT ; IMF-fixdate

## Naming Conventions

### Enums and string literals

Enum and string literal parameters use snake case. If there is an acronym involved, there will not be an underscore between every letter.

For example, `by_ani` instead of`ByANI`, `byAni`, or `by_a_n_i`.

### Country codes

The field name `country_code` is always used to represent a country. It will be in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format in capital letters to represent the country. For example `DE` for Germany.

### Phone numbers

Phone numbers are always specified in [e164](https://en.wikipedia.org/wiki/E.164) format. For example, `+18005550199`.

If the country calling code needs to be represented in the API, the field name will always be `country_calling_code`. If representing the actual country via its alpha 2 representation, `country_code` will be used.

Ex: `{"country_calling_code": "1", "country_code": "US"}`

### City names

City names are always called `locality` and represented in title case. For example, `New York City` instead of `NEW YORK CITY`.

## Address Format

Addresses are represented like this:

```json theme={null}
{
  "street_address": "311 W Superior St",
  "extended_address": "Suite 504",
  "locality": "Chicago",
  "administrative_area": "IL"
  "country_code": "US",
  "postal_code": "60654"
}
```

### U.S. addresses

US states are always represented in their two-digit form in capital letters. For example, `NY` for New York.

## Pagination

The parameter which contains pagination is `page`. This parameter is a map of pagination attributes.

### Example

`GET /phone_numbers?page[number]=3&page[size]=1 HTTP/1.1`

The default number of items per page is 20; however, sometimes, this may not be appropriate.

Page numbering is 1-based and omitting the `page`, or the `page[number]` parameter will return the first page.

Generally speaking, the maximum allowable results will not be more than 250, although there may be some exceptions to this rule.

The total number of results is provided in the `total_pages` field so that clients will know how many page options to display.

### Example Response

```bash theme={null}
HEADERS

Total-Pages:13
```

Response:

```json theme={null}
{
  "meta": {
    "total_pages": 13,
    "total_results": 26,
    "page_number": 3,
    "page_size": 2
  },
  "data": [
    {
      "record_type": "phone_number",
      "id": "4567890987",
      "phone_number": "+18005550100",
      "purchased_at": "2015-05-22T14:56:29.000Z",
      ...
    },
    {
      "record_type": "phone_number",
      "id": "44568890987",
      "phone_number": "+18005550199",
      "purchased_at": "2015-05-22T14:56:29.000Z",
      ...
    }
  ]
}
```

## Sorting

An endpoint may support requests to sort the primary data with a `sort` query parameter.

### Example

```bash theme={null}
GET /connections?sort=name HTTP/1.1
```

Unless not appropriate, the default sort will be `created_at DESC`

An endpoint may also support multiple sort fields using the array syntax. Sort fields will be applied in the order specified.

### Multiple Sort Fields

```bash theme={null}
GET /connections?sort[]=name&sort[]=created_at HTTP/1.1
```

The sort order for each sort field will be ascending unless it is prefixed with a minus (U+002D HYPHEN-MINUS, "-"), in which case it will be descending.

```bash theme={null}
GET /connections?sort[]=-created_at&sort[]=name HTTP/1.1
```

The above example should return the newest connections first. Any connections created on the same date will then be sorted by their name in ascending alphabetical order.

## Filtering

Filtering of a resource collection based upon associations do so by allowing query parameters that combine the filter with the association name.

For example, the following is a request for all phone\_numbers associated with a particular tag:

```bash theme={null}
GET /phone_numbers?filter[tag]=tag_one HTTP/1.1
```

Filtering to values within an array can be achieved using query parameter array syntax:

```bash theme={null}
GET /phone_numbers?filter[tag][]=tag_one&filter[tag][]=tag_two HTTP/1.1
```

Or an example using comments:

```bash theme={null}
GET /comments?filter[tag]=tag_one,tag_two HTTP/1.1
```

Use the string `null` to filter on resources that don't have a particular value set:

```bash theme={null}
GET /comments?filter[author]=null HTTP/1.1
```

### Filtering on values of nested or related objects

To denote that a filter applies to an attribute of a nested object, use the dot notation.

For example, the phone numbers endpoint returns data in this format:

```json theme={null}
{
  "id": "d460a653-8ee6-4061-ae9a-5b8a52539fb4",
  "phone_number": "18005550199",
  "record_type": "phone_number",
  ...
  "voice": {
    "e911_address_id" : "",
    "connection_name" : false,
    "inbound_call_recording_channels" : "single",
    ...
  }
}
```

To filter by the connection name the path and request would look like:

```bash theme={null}
GET /phone_numbers?filter[voice.connection_name]=conn_one HTTP/1.1
```

Similarly by connection ID:

```bash theme={null}
GET /regions?filter[voice.connection_id]=d460a653-8pp6-4061-ae9a-5b8a57339fb4 HTTP/1.1
```

However, if `name` was a top-level key as in the below example:

```json theme={null}
{
  "id": "d460a653-8pp6-4061-ae9a-5b8a57339fb4",
  "name": "conn_one",
  "record_type": "connection",
  ...
}
```

then the query would be:

```bash theme={null}
GET /connections?filter[name]=conn_one HTTP/1.1
```

### Complex filters

When filtering, you may need to specify more complex filters than `equal to`.

Options are:

* `eq`
* `ne`
* `gt`
* `gte`
* `lt`
* `lte`
* `starts_with`
* `ends_with`
* `contains`

Return phone numbers purchased before 2018-02-21:

```bash theme={null}
GET /phone_numbers?filter[purchased_at][lt]=2018-02-21 HTTP/1.1
```

If using `eq` then:

```bash theme={null}
GET /phone_numbers?filter[purchased_at][eq]=2018-02-21 HTTP/1.1
```

and:

```bash theme={null}
GET /phone_numbers?filter[purchased_at]=2018-02-21 HTTP/1.1
```

are equivalent.

To filter using string data use `starts_with`, `ends_with` or `contains`:

```bash theme={null}
GET /phone_numbers?filter[voice.connection_name][contains]=conn HTTP/1.1
```
