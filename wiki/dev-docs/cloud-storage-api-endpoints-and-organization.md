---
title: Cloud Storage API Endpoints and Organization
summary: 'Telnyx Cloud Storage exposes two API suites: an S3‑compatible API served
  from regional endpoints and a JSON companion API at api.telnyx.com. Use Signature
  V4 with your Telnyx API key, target the bucket’s home region for most S3 calls,
  and use the JSON companion for presigned URLs, usage, SSL, and migration.'
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/create-bucket
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
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-life-cycle-configuration
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-versioning
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/abort-multipart-upload
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-multipart-uploads
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-parts
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-objects
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/head-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-object-versions
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-objects
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/authentication
- url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility
- url: https://developers.telnyx.com/docs/cloud-storage/billing
- url: https://developers.telnyx.com/docs/cloud-storage/bucket-addressing
- url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/limits
- url: https://developers.telnyx.com/docs/cloud-storage/lock-and-retention
- url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws
- url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload
- url: https://developers.telnyx.com/docs/cloud-storage/object-encryption
- url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks
- url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls
- url: https://developers.telnyx.com/docs/cloud-storage/public-buckets
- url: https://developers.telnyx.com/docs/cloud-storage/quick-start
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
- url: https://developers.telnyx.com/docs/cloud-storage/supported
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
updated_at: 2026-05-14T09:45:55Z
---

# Cloud Storage API Endpoints and Organization

Telnyx Cloud Storage exposes two API suites: an S3‑compatible API served from regional endpoints and a JSON companion API at api.telnyx.com. Use Signature V4 with your Telnyx API key, target the bucket’s home region for most S3 calls, and use the JSON companion for presigned URLs, usage, SSL, and migration.

## Regional endpoints and routing

S3‑compatible endpoints by region:
- us-central-1 → us-central-1.telnyxcloudstorage.com
- us-east-1 → us-east-1.telnyxcloudstorage.com
- us-west-1 → us-west-1.telnyxcloudstorage.com
- eu-central-1 → eu-central-1.telnyxcloudstorage.com

Behavior and guidance:
- ListBuckets and GetBucketLocation requests: any US endpoint can list/locate all US buckets; the EU endpoint returns only EU buckets.
- All other S3 methods must be sent to the bucket’s home region. Always call GetBucketLocation first, then direct subsequent calls to that region.
- Bucket location is inherited from the regional endpoint used during CreateBucket. If you pass a LocationConstraint, it must match the endpoint’s region.

## Authentication and credentials

- Use AWS Signature Version 4 headers with your Telnyx API key as access-key-id. Telnyx validates the API key and ignores the other SigV4 components (date, region, service, secret‑derived signature), which remain only for S3 compatibility.
- Example header shape (single line): Authorization: AWS4-HMAC-SHA256 Credential={{your_telnyx_api_key}}/YYYYMMDD/region/s3/aws4_request, SignedHeaders=..., Signature=...
- Third‑party/S3 client mapping: set Access Key = Telnyx API key; Secret = blank, random, or duplicate of the API key.

## Bucket addressing options

- Path‑style: https://[region].telnyxcloudstorage.com/[bucket]/[object]
- Virtual‑hosted‑style: https://[bucket].[region].telnyxcloudstorage.com/[object]

## Supported APIs and compatibility

- Telnyx is S3‑compatible for a focused subset of APIs and headers. See [Compatibility Matrix](compatibility-matrix.md) for method‑by‑method support by region (US/EU).
- Not all S3 headers/XML elements are supported; only what is documented for each operation (for example, see limitations under PutObject in [AWS S3 Compatibility](aws-s3-compatibility.md)). Unsupported calls return an S3‑compatible NotImplemented XML error.
- Region highlights (see matrix): many bucket‑level features (ACL, CORS, policy, lifecycle, versioning) and multipart uploads are supported in the US; EU currently supports a subset (core bucket/object ops, no policy/ACL/CORS/multipart, etc.).

## JSON Companion API (api.telnyx.com)

Use the JSON companion for functionality that extends S3:
- Presigned URLs for anonymous uploads/downloads: see [Presigned URLs](presigned-urls.md). Do not generate with AWS SDK/CLI (would expose your API key); use the JSON companion endpoint instead.
- Usage and billing stats per bucket: see [Billing](billing.md) (Bucket Snapshot and API Usage endpoints).
- Manage custom domain TLS certificates: see [HTTPS with Custom Domain](https-with-custom-domain.md).
- Data migration from AWS S3 with minimized/avoided egress charges: see [Migrating from S3](migrating-from-s3.md).

Notes:
- Many companion features are currently US‑only (presigned URLs, public buckets, custom‑domain TLS, SSE‑C, object lock/retention).

## Verification, public access, and US‑only features

- Bucket policies (e.g., making a bucket public) are a privileged action; Level 2 account verification is required. See [Making Bucket Public](making-bucket-public.md).
- Presigned URLs: non‑verified accounts are limited to short TTLs (≤ 5 minutes). Verify your account for longer TTLs. See [Presigned URLs](presigned-urls.md).
- US‑only today: presigned URLs, public buckets, custom‑domain HTTPS, [Object Encryption](object-encryption.md) (SSE‑C), and [Object Lock & Retention](object-lock-retention.md).

## SDKs, CLI, and third‑party tools

General setup
- Always set the S3 endpoint to https://[region].telnyxcloudstorage.com.
- Provide your Telnyx API key as both access key and (optionally) secret.
- Many SDKs need small tweaks because Telnyx ignores/relaxes some S3 checksum/chunking behaviors:
  - .NET: set PutObjectRequest.UseChunkEncoding = false. See AWS .NET example in SDK docs.
  - Node.js SDK v3: set checksum calculation/validation to WHEN_REQUIRED.
  - Python (boto3 ≥1.36): set request_checksum_calculation="when_required", response_checksum_validation="when_required".
  - Java SDK v2.30+: disable/limit checksum to WHEN_REQUIRED for requests/responses.
  - Go v2, PHP, Ruby, Elixir: point the endpoint and pass your API key as credentials (examples provided in SDK pages).

AWS CLI
- Configure a profile with your Telnyx API key for both access and secret, leave “region” empty.
- Always pass --endpoint-url https://[region].telnyxcloudstorage.com.

Third‑party S3 tools
- Most S3‑compatible tools work (Cyberduck, S3 Browser, Wal‑G, etc.)—point them at the regional endpoint and use your API key as the access key. See [Third Party S3 Compatible Applications](third-party-s3-compatible-applications.md).

See [Quick Start](quick-start.md) for end‑to‑end setup examples.

## Limits and quotas

Key limits (see [Limits](limits.md) for full list):
- Requests per second: 500 per account; 200 per bucket.
- Single PUT upload max: 5 GB; multipart part size: 5 MiB–5 GB; max 10,000 parts; max multipart object size: 5 TiB.
- Max buckets per account: 100; max objects per bucket: 50 million.

## Billing and usage reporting

Overview (see [Billing](billing.md)):
- Storage billed by bytes stored, with a 4 KiB minimum object size and 4 KiB rounding per bucket (metadata counts).
- US storage: first 10 GiB/month free; then $0.006/GiB/mo (regular) and $0.60/GiB/mo (AI embedded).
- EU storage: no free tier; $0.025/GiB/mo (regular), $0.60/GiB/mo (AI embedded).
- API operations (US): Class A (PUT/COPY/POST/LIST) first 1M free, then $0.50/M; Class B (GET/SELECT/others) first 10M free, then $0.04/M. EU has separate rates.
- If available credit becomes negative, API calls fail with UserSuspended; data is retained. Accounts remaining negative for 30 days are abolished and data purged.

Usage APIs (JSON companion):
- Bucket Snapshot: on‑demand storage size and object count.
- API Usage: per‑category request counts/bytes over a time range.

## Operational best practices

- Always resolve a bucket’s region via GetBucketLocation and target the correct regional endpoint for all non‑listing calls.
- Use [Multipart Upload](multipart-upload.md) for large objects; clients and networks often achieve higher throughput this way.
- To empty large buckets, prefer lifecycle rules over synchronous deletions. See [Emptying Buckets](emptying-buckets.md).
- Public access: apply a minimal public‑read policy or ACL only after Level 2 verification. See [Making Bucket Public](making-bucket-public.md).
- Encryption with SSE‑C (US‑only): include the x‑amz-server-side-encryption-customer-* headers. See [Object Encryption](object-encryption.md).
- Governance/retention (US‑only): enable object lock at bucket creation, then configure retention on versions. See [Object Lock & Retention](object-lock-retention.md).
- Migrating from AWS: use the JSON migration API to avoid/discount egress charges and to copy in‑region via Telnyx migration engines. See [Migrating from S3](migrating-from-s3.md).
