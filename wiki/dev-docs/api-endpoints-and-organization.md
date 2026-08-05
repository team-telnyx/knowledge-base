---
title: API Endpoints and Organization
summary: Overview of the two suites of Telnyx Cloud Storage APIs — the S3-compatible
  API and the JSON companion API — including regional endpoint URLs and the base URL
  for the companion API.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints/index
updated_at: 2026-08-05T13:37:58Z
---

# API Endpoints and Organization

Overview of the two suites of Telnyx Cloud Storage APIs — the S3-compatible API and the JSON companion API — including regional endpoint URLs and the base URL for the companion API.

## Overview

Telnyx Cloud Storage exposes two suites of APIs:

- **S3 compatible** — an API surface compatible with AWS S3, requiring minimal changes to migrate existing integrations.
- **JSON companion** — an extension to the S3 API that adds account- and management-level functionality not covered by S3.

## S3 Compatible APIs

The S3-compatible API is region-scoped. Each region has its own endpoint hostname, and most API methods must be directed at the regional endpoint where the bucket is homed.

| Endpoint URL | Region |
| --- | --- |
| `us-central-1.telnyxcloudstorage.com` | us-central-1 |
| `us-east-1.telnyxcloudstorage.com` | us-east-1 |
| `us-west-1.telnyxcloudstorage.com` | us-west-1 |
| `eu-central-1.telnyxcloudstorage.com` | eu-central-1 |
| `ap-southeast-1.telnyxcloudstorage.com` | ap-southeast-1 |

`ListBuckets` and `GetBucketLocation` are global: any regional endpoint returns every bucket in the account regardless of the region it is homed in. All other API methods must be directed at the regional endpoint where the bucket is homed, otherwise an error is returned. As a result, it is advisable to query the location of the bucket first (via `GetBucketLocation`) before forming the correct regional endpoint for all subsequent API operations.

For the full list of supported S3 operations, see [Supported S3 APIs](supported-s3-apis.md).

## JSON Companion API

The JSON companion API is an extension to the S3 API and provides functionality that is not part of the S3 surface. It is served from a single base URL, `api.telnyx.com`, and covers:

- Querying usage — see [Billing](billing.md).
- Creating presigned URLs — see [Presigned URLs](presigned-urls.md).
- Managing SSL — see [SSL Certificates](ssl-certificates.md).
- Migrating data from AWS S3 — see [Migrating from AWS](migrating-from-aws.md).
