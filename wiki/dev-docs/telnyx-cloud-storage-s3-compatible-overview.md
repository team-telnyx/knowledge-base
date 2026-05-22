---
title: Telnyx Cloud Storage (S3-Compatible) Overview
summary: A high-level guide to Telnyx Cloud Storage covering regional endpoints, authentication,
  AWS S3 compatibility, companion JSON APIs, pricing, limits, migration from AWS S3,
  performance, and recommended tooling.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints
  content_hash: cbe99d23c10206ee6ebb9ec99e2c645c2674216bf1e1a948b73be208e2f0b1d3
- url: https://developers.telnyx.com/docs/cloud-storage/authentication
  content_hash: 833a3abfb25019d891e22dda4d1b92e69ca7aa90af2151ab2ccbcd58e5735ac1
- url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility/index
  content_hash: fcc0774c4d890cb79a734286f2aab1831006eda8cad8042c71a2722a982ac613
- url: https://developers.telnyx.com/docs/cloud-storage/billing
  content_hash: a1a3a337bb3a3807ab2311fb30cf9c06325bb97576a6a8b5c31a86b0c7414184
- url: https://developers.telnyx.com/docs/cloud-storage/limits
  content_hash: 7bbdb4c025eec2273739a1b3fa93f002b1b2ecaf950965213b61a9b413b9ddc7
- url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws
  content_hash: ae62d3782be3ef55eccd8afe20eee4aca02210750d98006f6b1f730c06692396
- url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks
  content_hash: d7ca4602d6091c4b43bb9d77578e643b9f2b64d95e8531652e0b1a908ac52ed8
- url: https://developers.telnyx.com/docs/cloud-storage/quick-start/index
  content_hash: f00aabc3a24affea53693e7b2c36976b8485dcd5c5acd8bd08a4a083cbc2f62e
- url: https://developers.telnyx.com/docs/cloud-storage/supported
  content_hash: 63c09b5b5bd994d394ba612e35204dd50a82e05bfa87decea5b98f10fbe60fda
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
  content_hash: ca078c865ec22ff1dbecd0fbb39a5ab49f50723fc5830a1800b0f7060af3542b
updated_at: 2026-05-19T15:55:59Z
---

# Telnyx Cloud Storage (S3-Compatible) Overview

A high-level guide to Telnyx Cloud Storage covering regional endpoints, authentication, AWS S3 compatibility, companion JSON APIs, pricing, limits, migration from AWS S3, performance, and recommended tooling.

## Service layout and endpoints
Telnyx Storage exposes two API suites:

- S3-compatible APIs for buckets and objects
- A JSON Companion API for management and usage features

Regional S3 endpoints (use the bucket’s home region for most operations):
- us-central-1 → us-central-1.telnyxcloudstorage.com
- us-east-1 → us-east-1.telnyxcloudstorage.com
- us-west-1 → us-west-1.telnyxcloudstorage.com
- eu-central-1 → eu-central-1.telnyxcloudstorage.com

Notes on regional behavior:
- Any US endpoint can be used for ListBuckets and GetBucketLocation across all US buckets
- The EU endpoint returns only EU buckets for those two calls
- All other S3 API methods must target the bucket’s regional endpoint; query location first, then direct subsequent calls accordingly

JSON Companion API endpoint: api.telnyx.com

See [API Endpoints and Organization](api-endpoints-and-organization.md) and [Cloud Storage quick start](cloud-storage-quick-start.md).

## Authentication model
S3-compatible requests use an AWS Signature Version 4 Authorization header, but with your Telnyx API key substituted as access-key-id. Telnyx validates only the API key; date/region/service/secret/signature fields are ignored and included solely for S3 compatibility.

Third‑party/AWS CLI guidance:
- Access Key → Telnyx API token
- Secret Access Key → blank, random placeholder, or duplicate of the API token

JSON Companion API requests use standard Telnyx Bearer auth against api.telnyx.com.

Details: [Cloud Storage authentication](cloud-storage-authentication.md).

## S3 compatibility and supported features
- Telnyx implements a large subset of S3; unsupported methods return S3‑compatible XML NotImplemented
- For supported APIs, not all S3 headers/parameters/elements are accepted. Only what’s documented for each operation is guaranteed. For example, PutObject supports a limited set of headers; others are unsupported by default unless explicitly specified
- Some capabilities are currently US‑only (e.g., presigned URLs, public buckets, SSL certificates). Verify per‑region availability in the matrix

Reference: [Compatibility with AWS S3](compatibility-with-aws-s3.md) and [Compatibility Matrix](compatibility-matrix.md).

## Getting started with AWS CLI/SDKs
- Configure AWS CLI with your Telnyx API key as both Access Key and Secret (placeholder is fine)
- Omit the AWS region in the profile; specify the Telnyx regional endpoint via --endpoint-url
- Point SDKs to the same regional endpoints as above

Step‑by‑step examples: [Cloud Storage quick start](cloud-storage-quick-start.md).

## JSON Companion API capabilities
Use api.telnyx.com for extended features:
- Usage queries (bucket storage snapshots and API operation stats)
- Presigned URL creation
- SSL certificate management for buckets
- Data migration from AWS S3

Auth: Authorization: Bearer <your Telnyx API key>

See: [Billing](billing.md) (usage queries), [Presigned URLs](presigned-urls.md), [HTTPS with Custom Domain](https-with-custom-domain.md), and [Migrating from S3](migrating-from-s3.md).

## Billing and free tiers
You are billed for:
- Bytes stored (measured hourly; metadata counts; minimum billable object size is 4 KiB, billed in 4 KiB increments per bucket)
- API operations (classified pricing)

Storage pricing:
- US: first 10 GiB/month free; then $0.006 per GiB/month (regular), $0.60 per GiB/month (AI embedded)
- EU: no free tier; $0.025 per GiB/month (regular), $0.60 per GiB/month (AI embedded)

API operations pricing:
- US: Class A (PUT/COPY/POST/LIST) → first 1M/month free, then $0.50 per 1M; Class B (GET/SELECT/other) → first 10M/month free, then $0.04 per 1M
- EU: State‑change (PUT/COPY/POST/LIST) → $5.00 per 1M; Read (GET/SELECT/other) → $0.40 per 1M

Account states:
- If available credit is negative, API requests fail with UserSuspended; data is retained and access is restored when credit is positive
- If negative for 30 days, the account is abolished and data is irreversibly purged

Companion usage APIs (high level):
- GET /v2/storage/buckets/{bucket}/usage/storage → current size and object count
- GET /v2/storage/buckets/{bucket}/usage/api?filter[start_time]=...&filter[end_time]=... → categorized API stats

Details: [Billing](billing.md).

## Service quotas and limits
General API limits (subject to change):
- 500 requests/second per account
- 200 requests/second per bucket
- 10 concurrent PUT or COPY requests per object

Object and multipart limits:
- Max single‑PUT object size: 5 GB
- Multipart upload part size: 5 MiB min (except final), 5 GB max per part
- Max parts per multipart upload: 10,000
- Max object size via multipart: 5 TiB

Resource limits:
- Up to 100 buckets per account
- Up to 50 million objects per bucket

See [Cloud Storage limits and quotas](cloud-storage-limits-and-quotas.md).

## Migrating data from AWS S3
The Migration API moves data from an AWS S3 source bucket to a Telnyx bucket without AWS internet egress charges by leveraging intra‑region transfer and AWS Direct Connect. Key points:
- Currently supported for US buckets only
- Only Standard storage class is supported; restore Glacier objects before migration
- You can migrate across regions (e.g., AWS us-west-1 → Telnyx us-east-1); the engine co‑locates in the AWS source region to avoid egress
- The API can create the target Telnyx bucket if it doesn’t exist; invalid/unavailable names error immediately
- Supports one‑time migrations or periodic sync via a refresh flag
- Typical flow: check coverage → create migration source (read‑only AWS creds) → create migration → poll status or verify target bucket size/objects

Errors you may encounter include “Bucket does not exist,” “Access denied,” and “Bucket region invalid.”

Learn more: [Migrating from S3](migrating-from-s3.md).

## Performance at a glance
Aggregate benchmarks (indicative, hardware/testbed dependent):
- PutObject: ~2.03 GiB/s
- GetObject: ~2.71 GiB/s

See environment, methodology, and charts in [Performance Benchmarks](performance-benchmarks.md).

## Third‑party tools and applications
Any S3‑compatible client can be used (e.g., Cyberduck, S3 Browser, Wal‑G). Configure the endpoint to the Telnyx regional URL and use your Telnyx API key for access credentials as described above.

Guides: [Third Party S3 Compatible Applications](third-party-s3-compatible-applications.md).

## Practical tips and gotchas
- Always discover a bucket’s location and use that region’s endpoint for all non‑listing operations
- In the US, ListBuckets/GetBucketLocation can hit any US endpoint; EU listings must use the EU endpoint
- Verify feature availability per region in [Compatibility Matrix](compatibility-matrix.md) (e.g., multipart and many bucket/object sub‑features are US‑only today)
- Keep single‑PUT uploads ≤ 5 GB; use multipart for larger objects
- Only documented headers/parameters are honored for each API; others are ignored or cause NotImplemented
- For public access, presigned URLs, and custom domains/SSL, consult [Presigned URLs](presigned-urls.md), [Public Buckets](public-buckets.md), and [HTTPS with Custom Domain](https-with-custom-domain.md)
- Review addressing patterns in [Bucket Addressing](bucket-addressing.md) before production use
