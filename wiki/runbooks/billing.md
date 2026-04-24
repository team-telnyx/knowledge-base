---
title: Billing
summary: Understand Telnyx Cloud Storage billing—Details on charges for storage bytes and API operation counts.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/billing/index
    content_hash: b87c24631ac21d47431c5336ad8d32d75ac8c274587cfecbef6dbde2128f217c
updated_at: 2026-04-10T00:00:00Z
---

# Billing

Understand Telnyx Cloud Storage billing—Details on charges for storage bytes and API operation counts.

You are billed on two things

* The bytes stored
* The count of API operations invoked

## Storage billing explained

The minimum billable **object** size is 4 KiB. Here is an example — if you have two 11-byte objects in a bucket, they will be counted as 4 KiB each, i.e. 8 KiB in total. 

Storage consumed by each bucket is billed in multiples of 4 KiB, rounded up; Metadata counts towards storage consumed.

### US Storage

Every month, your **first 10 GiB is free of charge**. Any bytes beyond that are billed at:

* **\$0.006 per GiB per month** for regular storage
* **\$0.60 per GiB per month** for AI embedded storage

### EU Storage

EU storage has **no free tier** and is billed at:

* **\$0.025 per GiB per month** for regular storage
* **\$0.60 per GiB per month** for AI embedded storage

Bytes stored across all buckets are **recorded hourly**. Usage is subsequently calculated and debited from your balance. 

Here is a hypothetical example:

* You have a \$10 balance in your account.
* At time `t`, you uploaded 11 GiB of objects into various buckets in your account.
* At the next whole clock hour after time `t`
  * a snapshot of your total storage is recorded as 11 GiB
  * your usage is calculated as (11 GiB - 10 GiB) x (\$ 0.006 / 30 days / 24 hrs)
  * that usage is then debited from your \$10 balance

Lastly, free tier is not available to an account if its available credit is negative.

Here is a hypothetical example:

* You have a \$10 balance in your account
* Through usage of Voice and Messaging API, you've depleted your balance and resulted in a negative available credit of -0.1 USD.
* You will not be able to create a bucket and upload objects until your available credit is restored.

## API operations billing explained

API operations are classified and billed the following way —

### US Storage

<table>
  <tbody>
    <tr>
      <td>Categories</td>
      <td>Applicable API Ops</td>
      <td>Prices</td>
    </tr>

    <tr>
      <td>Class A</td>
      <td>PUT, COPY, POST, LIST requests</td>
      <td>Every month, the first 1 Million is free of charge, thereafter \$0.50 per 1 Million</td>
    </tr>

    <tr>
      <td>Class B</td>
      <td>GET, SELECT, and all other request</td>
      <td>Every month, the first 10 Million is free of charge, thereafter \$0.04 per 1  Million</td>
    </tr>
  </tbody>
</table>

### EU Storage

<table>
  <tbody>
    <tr>
      <td>Categories</td>
      <td>Applicable API Ops</td>
      <td>Prices</td>
    </tr>

    <tr>
      <td>State-change operations</td>
      <td>PUT, COPY, POST, LIST requests</td>
      <td>\$5.00 per 1 Million</td>
    </tr>

    <tr>
      <td>Read operations</td>
      <td>GET, SELECT, and all other requests</td>
      <td>\$0.40 per 1 Million</td>
    </tr>
  </tbody>
</table>

## Account suspension and loss of data

<Callout type="warning">
  When an account's available credit becomes negative:

  * You will be notified via email of insufficient balance.
  * Your data is ***still retained*** in the system but API requests will fail with error message `UserSuspended`.
  * Access will be restored when available credit is made positive via payment.

  If available credit remains negative for 30 days, your account will be abolished. As a consequence, all data will be irreversibly purged.

## Relevant companion APIs

Two companion APIs exist to allow for querying of usage:

* [Bucket Snapshot](https://developers.telnyx.com/api-reference/bucket-usage/get-bucket-usage#get-bucket-usage) is a snapshot of the bytes your bucket is taking up at the moment of query.
* [API Usage](https://developers.telnyx.com/api-reference/bucket-usage/get-api-usage#get-api-usage) shows the stats of your API requests.

### Query bucket snapshot

**Example Request**

```json theme={null}
GET /v2/storage/buckets/mybucket/usage/storage HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

**Example Response**

```json theme={null}
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

```json theme={null}
GET /v2/storage/buckets/mybucket/usage/api?filter[start_time]=2024-07-01T00:00:00.000Z&filter[end_time]=2024-07-31T00:00:00.000Z HTTP/1.1
Host: api.telnyx.com
Authorization: Bearer XXX
```

**Example Response**

```json theme={null}
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
