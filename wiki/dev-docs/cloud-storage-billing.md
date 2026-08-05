---
title: Cloud Storage Billing
summary: Telnyx Cloud Storage charges customers based on the bytes stored and the
  count of API operations invoked. This page explains storage and API operation pricing
  for both US and EU regions, account suspension rules, and the companion APIs available
  for querying usage.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/billing
updated_at: 2026-08-05T13:38:48Z
---

# Cloud Storage Billing

Telnyx Cloud Storage charges customers based on the bytes stored and the count of API operations invoked. This page explains storage and API operation pricing for both US and EU regions, account suspension rules, and the companion APIs available for querying usage.

## Overview

Telnyx Cloud Storage bills customers on two dimensions:

- The bytes stored
- The count of API operations invoked

## Storage billing

The minimum billable **object** size is 4 KiB. For example, two 11-byte objects in a bucket are counted as 4 KiB each, totalling 8 KiB. Storage consumed by each bucket is billed in multiples of 4 KiB, rounded up, and metadata counts towards storage consumed.

### US Storage

Every month, the **first 10 GiB is free of charge**. Bytes beyond that are billed at:

- **$0.006 per GiB per month** for regular storage
- **$0.60 per GiB per month** for AI embedded storage

### EU Storage

EU storage has **no free tier** and is billed at:

- **$0.025 per GiB per month** for regular storage
- **$0.60 per GiB per month** for AI embedded storage

### How storage usage is recorded

Bytes stored across all buckets are **recorded hourly**. Usage is subsequently calculated and debited from your balance.

Example scenario:

- You have a $10 balance in your account.
- At time `t`, you upload 11 GiB of objects into various buckets in your account.
- At the next whole clock hour after time `t`:
  - A snapshot of your total storage is recorded as 11 GiB.
  - Your usage is calculated as `(11 GiB - 10 GiB) × ($0.006 / 30 days / 24 hrs)`.
  - That usage is then debited from your $10 balance.

The free tier is not available to an account if its available credit is negative. For example, if you have a $10 balance but your usage of Voice and Messaging API depletes your balance to a negative available credit of -0.1 USD, you will not be able to create a bucket and upload objects until your available credit is restored.

## API operations billing

API operations are classified and billed according to the region in which the bucket resides.

### US Storage

| Categories | Applicable API Ops | Prices |
| --- | --- | --- |
| Class A | PUT, COPY, POST, LIST requests | Every month, the first 1 Million is free of charge, thereafter $0.50 per 1 Million |
| Class B | GET, SELECT, and all other requests | Every month, the first 10 Million is free of charge, thereafter $0.04 per 1 Million |

### EU Storage

| Categories | Applicable API Ops | Prices |
| --- | --- | --- |
| State-change operations | PUT, COPY, POST, LIST requests | $5.00 per 1 Million |
| Read operations | GET, SELECT, and all other requests | $0.40 per 1 Million |

## Account suspension and loss of data

When an account's available credit becomes negative:

- You will be notified via email of insufficient balance.
- Your data is **still retained** in the system, but API requests will fail with the error message `UserSuspended`.
- Access will be restored when available credit is made positive via payment.

If available credit remains negative for 30 days, your account will be abolished. As a consequence, all data will be irreversibly purged.

## Relevant companion APIs

Two companion APIs exist to allow for querying of usage:

- [Bucket Snapshot](https://developers.telnyx.com/api-reference/bucket-usage/get-bucket-usage#get-bucket-usage) is a snapshot of the bytes your bucket is taking up at the moment of query.
- [API Usage](https://developers.telnyx.com/api-reference/bucket-usage/get-api-usage#get-api-usage) shows the stats of your API requests.

### Query bucket snapshot

**Example Request**

```
GET /v2/storage/buckets/mybucket/usage/storage HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

**Example Response**

```json
{
    "data": [
        {
            "size": 1078984704,
            "size_kb": 1053696,
            "num_objects": 2,
            "timestamp": "2024-07-30T14:26:43Z"
        }
    ],
    "meta": {
        "page_number": 1,
        "page_size": 1,
        "total_pages": 1,
        "total_results": 1
    }
}
```

### Query API usage

**Example Request**

```
GET /v2/storage/buckets/mybucket/usage/api?filter[start_time]=2024-07-01T00:00:00.000Z&filter[end_time]=2024-07-31T00:00:00.000Z HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

**Example Response**

```json
{
    "data": [
        {
            "categories": [
                {
                    "bytes_sent": 1768,
                    "bytes_received": 0,
                    "ops": 13,
                    "successful_ops": 13,
                    "category": "get_bucket_location"
                },
                {
                    "bytes_sent": 141,
                    "bytes_received": 0,
                    "ops": 1,
                    "successful_ops": 1,
                    "category": "get_bucket_policy_status"
                },
                {
                    "bytes_sent": 137,
                    "bytes_received": 0,
                    "ops": 1,
                    "successful_ops": 1,
                    "category": "get_bucket_versioning"
                },
                {
                    "bytes_sent": 2022703104,
                    "bytes_received": 0,
                    "ops": 2,
                    "successful_ops": 2,
                    "category": "get_obj"
                },
                {
                    "bytes_sent": 1623,
                    "bytes_received": 0,
                    "ops": 3,
                    "successful_ops": 3,
                    "category": "list_bucket"
                }
            ],
            "total": {
                "bytes_sent": 2022706773,
                "bytes_received": 0,
                "ops": 20,
                "successful_ops": 20
            },
            "timestamp": "2024-07-02T17:00:00.000Z"
        }
    ]
}
```
