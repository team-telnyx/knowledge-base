---
title: Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service available
  in four regions (us-central-1, us-east-1, us-west-1, eu-central-1). It can be accessed
  via the AWS S3 API, AWS SDKs, AWS CLI, third-party S3 tools, the Telnyx Mission
  Control Portal, or directly from inside a Telnyx Edge Function via a pre-authenticated
  binding. Authentication uses your Telnyx API key as the S3 credential. The service
  supports standard S3 operations (with some US-only features like presigned URLs,
  public buckets, object lock, and SSE-C encryption), usage-based billing with a US
  free tier, and a JSON companion API for usage queries, presigned URLs, SSL management,
  and AWS S3 migration.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/create-bucket/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-lifecycle
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-policy
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-lifecycle-configuration
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-location
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy-status
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-versioning
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/head-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/list-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-life-cycle-configuration
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-versioning
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/abort-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-multipart-uploads
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-parts
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-objects
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/head-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-object-versions
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-objects
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object/index
- url: https://developers.telnyx.com/docs/cloud-storage/authentication
- url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility/index
- url: https://developers.telnyx.com/docs/cloud-storage/billing
- url: https://developers.telnyx.com/docs/cloud-storage/bindings/index
- url: https://developers.telnyx.com/docs/cloud-storage/bindings/reference
- url: https://developers.telnyx.com/docs/cloud-storage/bucket-addressing
- url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/limits/index
- url: https://developers.telnyx.com/docs/cloud-storage/lock-and-retention
- url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws
- url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/object-encryption
- url: https://developers.telnyx.com/docs/cloud-storage/overview/index
- url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks
- url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls
- url: https://developers.telnyx.com/docs/cloud-storage/public-buckets
- url: https://developers.telnyx.com/docs/cloud-storage/quick-start/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
- url: https://developers.telnyx.com/docs/cloud-storage/supported
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
updated_at: 2026-07-17T09:13:08Z
---

# Cloud Storage

*Part 1 of 5 — see also: [Part 2](cloud-storage--part-2.md), [Part 3](cloud-storage--part-3.md), [Part 4](cloud-storage--part-4.md), [Part 5](cloud-storage--part-5.md)*

Telnyx Cloud Storage is an S3-compatible object storage service available in four regions (us-central-1, us-east-1, us-west-1, eu-central-1). It can be accessed via the AWS S3 API, AWS SDKs, AWS CLI, third-party S3 tools, the Telnyx Mission Control Portal, or directly from inside a Telnyx Edge Function via a pre-authenticated binding. Authentication uses your Telnyx API key as the S3 credential. The service supports standard S3 operations (with some US-only features like presigned URLs, public buckets, object lock, and SSE-C encryption), usage-based billing with a US free tier, and a JSON companion API for usage queries, presigned URLs, SSL management, and AWS S3 migration.

## Overview

Telnyx Cloud Storage is an S3-compatible object storage service for files, media, backups, and static assets. It can be reached over the AWS S3 API you already know, or directly from inside a [Telnyx Edge Function](use-a-bucket-from-an-edge-function.md) via a pre-authenticated binding. Buckets are available in four regions: `us-central-1`, `us-east-1`, `us-west-1`, and `eu-central-1`.

With Telnyx Cloud Storage you can:

- **Use your existing S3 tooling** — the AWS SDKs, AWS CLI, and third-party S3 clients work unchanged; authenticate with your Telnyx API key.
- **Store data in the US or EU** — buckets in `us-central-1`, `us-east-1`, `us-west-1`, and `eu-central-1`.
- **Reach buckets from Edge Compute** — bind a bucket to a function and read or write objects with no S3 keys in your code.
- **Control access and lifecycle** — presigned URLs, public buckets, object lock and retention, SSE-C encryption, and lifecycle rules.
- **Pay for what you use** — a monthly free tier plus simple usage-based pricing.

## API Endpoints and Organization

There are two suites of Storage APIs:

- **S3 compatible** — minimal changes to existing integrations are needed for migration to Telnyx.
- **JSON companion** — an extension to the S3 API for usage queries, presigned URLs, SSL management, and AWS S3 migration.

### S3 Compatible Endpoints

| Endpoint URL | Region |
| --- | --- |
| us-central-1.telnyxcloudstorage.com | us-central-1 |
| us-east-1.telnyxcloudstorage.com | us-east-1 |
| us-west-1.telnyxcloudstorage.com | us-west-1 |
| eu-central-1.telnyxcloudstorage.com | eu-central-1 |

`ListBuckets` and `GetBucketLocation` are global: any regional endpoint returns every bucket in your account regardless of the region it is homed in. All other API methods must be directed at the regional endpoint that the bucket is homed in, otherwise an error is returned. Query the location of the bucket first before forming the correct regional endpoint for subsequent API operations.

### JSON Companion API

The JSON companion API extends the S3 API with:

- [Querying usage](billing.md)
- [Create presigned URL](presigned-urls.md)
- [Manage SSL](https-with-custom-domain.md)
- [Migrating data from AWS S3](migrating-from-s3.md)

The JSON companion API endpoint is `api.telnyx.com`.

## Authentication

API requests are authenticated with [API Keys](https://portal.telnyx.com/#/api-keys). Telnyx Storage requires passing an [AWS Signature Version 4 authorization header](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-auth-using-authorization-header.html) in the API request. The Telnyx API key is substituted into the authorization header as the `access-key-id`. When an API request is made, Telnyx parses the API key from the header, validates it, and authorizes the request.

The remaining components of the authorization header (`date`, `aws-region`, `aws-service`, `secret-key`) are irrelevant — they remain only to maintain S3 compatibility. As long as you pass an AWS Signature Version 4 authorization header with the Telnyx API key as the `access-key-id`, the request is authenticated.

Example:

```
Authorization: AWS4-HMAC-SHA256 
Credential={{your_telnyx_api_key_here}}/20221129/us-east-1/s3/aws4_request, 
SignedHeaders=host;range;x-amz-date,
Signature=d82d11938fe5edf39a778ec710ac79899bae1d9a46ae36607be30fb55f655a3c
```

For the AWS CLI and S3 third-party applications:

- `Access Key` → substitute in the Telnyx API token
- `Secret Access Key` → either leave blank, or type something random as a placeholder, or duplicate the Telnyx API token

## Bucket Addressing

Telnyx Cloud Storage supports both addressing styles:

- **Path-style:** `https://[region].telnyxcloudstorage.com/[bucketname]/[objectname]`
- **Virtual-hosted-style:** `https://[bucketname].[region].telnyxcloudstorage.com/[objectname]`

## Limits and Quotas

### General API Limits

| Limit | Value |
| --- | --- |
| Requests per second per account | 500 |
| Requests per second per bucket | 200 |
| Concurrent PUT or COPY requests per object | 10 |

These limits are subject to change. If you require higher throughput, [contact support](https://support.telnyx.com).

### Specific Limits

- Max count of buckets per account: 100
- Max size of single object upload via PUT request: 5 GB
- Max size of single part upload of a multi-part upload: 5 GB
- Min size of single part upload of a multi-part upload: 5 MiB, except for the final part
- Max count of parts of a multi-part upload: 10,000
- Max size of a completed multi-part upload: 5 TiB
- Max count of objects per bucket: 50 million

## Billing

You are billed on two things:

- The bytes stored
- The count of API operations invoked

### Storage Billing

The minimum billable **object** size is 4 KiB. For example, two 11-byte objects in a bucket are counted as 4 KiB each (8 KiB total). Storage consumed by each bucket is billed in multiples of 4 KiB, rounded up; metadata counts towards storage consumed.

**US Storage:**

- Every month, your **first 10 GiB is free of charge**.
- **$0.006 per GiB per month** for regular storage
- **$0.60 per GiB per month** for AI embedded storage

**EU Storage:**

- EU storage has **no free tier**.
- **$0.025 per GiB per month** for regular storage
- **$0.60 per GiB per month** for AI embedded storage

Bytes stored across all buckets are **recorded hourly**. Usage is calculated and debited from your balance at the next whole clock hour. The free tier is not available to an account if its available credit is negative.

### API Operations Billing

**US Storage:**

| Categories | Applicable API Ops | Prices |
| --- | --- | --- |
| Class A | PUT, COPY, POST, LIST requests | First 1 Million per month free, thereafter $0.50 per 1 Million |
| Class B | GET, SELECT, and all other requests | First 10 Million per month free, thereafter $0.04 per 1 Million |

**EU Storage:**

| Categories | Applicable API Ops | Prices |
| --- | --- | --- |
| State-change operations | PUT, COPY, POST, LIST requests | $5.00 per 1 Million |
| Read operations | GET, SELECT, and all other requests | $0.40 per 1 Million |

### Account Suspension and Loss of Data

When an account's available credit becomes negative:

- You will be notified via email of insufficient balance.
- Your data is **still retained** in the system but API requests will fail with error message `UserSuspended`.
- Access will be restored when available credit is made positive via payment.

If available credit remains negative for 30 days, your account will be abolished and all data will be irreversibly purged.

### Querying Usage

Two companion APIs allow querying of usage:

- [Bucket Snapshot](https://developers.telnyx.com/api-reference/bucket-usage/get-bucket-usage#get-bucket-usage) — a snapshot of the bytes your bucket is taking up at the moment of query.
- [API Usage](https://developers.telnyx.com/api-reference/bucket-usage/get-api-usage#get-api-usage) — stats of your API requests.

## Compatibility with AWS S3

The [Compatibility Matrix](compatibility-matrix.md) documents all supported S3 APIs. When an unsupported API method is invoked, an S3-compatible, XML-formatted `NotImplemented` error response is returned. For supported API methods, not all of the AWS S3 parameters, headers, and body XML elements are supported — they are unsupported by default unless explicitly specified.
