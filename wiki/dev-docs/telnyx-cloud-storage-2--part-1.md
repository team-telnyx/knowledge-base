---
title: Telnyx Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service with regional
  endpoints in the US and EU, supporting standard S3 operations via AWS CLI, SDKs,
  and third-party tools. It offers features such as multipart uploads, server-side
  encryption with customer keys (SSE-C), presigned URLs, public bucket policies, and
  a migration API for moving data from AWS S3 without incurring egress charges.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/limits
- url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws
- url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/object-encryption
- url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks
- url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls
- url: https://developers.telnyx.com/docs/cloud-storage/public-buckets
- url: https://developers.telnyx.com/docs/cloud-storage/quick-start/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
updated_at: 2026-06-11T10:25:05Z
---

# Telnyx Cloud Storage

*Part 1 of 3 — see also: [Part 2](telnyx-cloud-storage-2--part-2.md), [Part 3](telnyx-cloud-storage-2--part-3.md)*

Telnyx Cloud Storage is an S3-compatible object storage service with regional endpoints in the US and EU, supporting standard S3 operations via AWS CLI, SDKs, and third-party tools. It offers features such as multipart uploads, server-side encryption with customer keys (SSE-C), presigned URLs, public bucket policies, and a migration API for moving data from AWS S3 without incurring egress charges.

## Available Regions and Endpoints

| Region | Endpoint |
| --- | --- |
| us-central-1 | `us-central-1.telnyxcloudstorage.com` |
| us-east-1 | `us-east-1.telnyxcloudstorage.com` |
| us-west-1 | `us-west-1.telnyxcloudstorage.com` |
| eu-central-1 | `eu-central-1.telnyxcloudstorage.com` |

Specify the region via the `--endpoint-url` flag in the AWS CLI or the equivalent SDK configuration. Some features are currently US-only — see [Telnyx Cloud Storage Compatibility Matrix](telnyx-cloud-storage-compatibility-matrix.md) for full details.

## Getting Started

There are four ways to interact with Telnyx Cloud Storage:

1. **Telnyx Mission Control Portal** — Follow the [support article](https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide).
2. **AWS CLI** — Install the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html), then configure a profile using your Telnyx API key for both the access key and secret key, leaving the region blank (regionality is set via `--endpoint-url`).
3. **AWS SDK** — See SDK examples below for Go, Java, .NET, and Elixir.
4. **S3-compatible third-party tools** — Configuration guides are available [here](https://support.telnyx.com/en/collections/3840515-telnyx-storage).

Key differences from AWS S3 should be reviewed before production use, including API endpoint organization, supported API methods, presigned URL handling, and [Telnyx Cloud Storage Billing](telnyx-cloud-storage-billing.md).

## API Limits

### General API Limits

| Limit | Value |
| --- | --- |
| Requests per second per account | 500 |
| Requests per second per bucket | 200 |
| Concurrent PUT or COPY requests per object | 10 |

These limits are subject to change. Contact [Telnyx support](https://support.telnyx.com) if you require higher throughput.

### Specific Limits

- Max buckets per account: **100**
- Max single-object upload via PUT: **5 GB**
- Max single-part size in a multipart upload: **5 GB**
- Min single-part size in a multipart upload: **5 MiB** (except the final part)
- Max parts in a multipart upload: **10,000**
- Max completed multipart upload size: **5 TiB**
- Max objects per bucket: **50 million**

## Multipart Upload

Large objects should be uploaded via multipart upload. Throughput typically ranges from 20 MiB/s on a home network to over 100 MiB/s in a data-center environment.

### Using AWS CLI

```bash
aws s3 cp ~/path/to/largefile s3://target-bucket/largefile \
  --profile mytelnyxprofile \
  --endpoint-url https://us-west-1.telnyxcloudstorage.com
```

### Using the AWS API/SDK

The multipart upload procedure follows three steps:

1. **CreateMultipartUpload** — Initiate the upload session.
2. **UploadPart** — Stream each chunk of data.
3. **CompleteMultipartUpload** — Finalize the transfer.

## Presigned URLs

Presigned URLs are currently supported only for buckets located in the US.

**Do not use the AWS SDK or CLI to generate presigned URLs.** Telnyx does not follow AWS authentication for presigned URLs; using AWS tooling will expose your API key. Instead, use the [Presigned Object URL API](https://developers.telnyx.com/api-reference/presigned-object-urls/create-presigned-object-url) to generate ephemeral presigned URLs for anonymous downloads and uploads.

Non-verified accounts are limited to presigned URLs with a TTL of no greater than 5 minutes. To create longer-lived presigned URLs, obtain [Level 2 verification](https://portal.telnyx.com/#/account/my-account/verifications) status.

### Downloading with a Presigned URL

```bash
curl -o my-object.bin \
  "https://us-central-1.telnyxcloudstorage.com/my-bucket/my-object.bin?X-AMZ-Security-Token=8f0nh1jk8qvf"
```

### Uploading with a Presigned URL

```bash
curl -X PUT -F "file=@a-new-object.bin" \
  "https://us-central-1.telnyxcloudstorage.com/my-bucket/a-new-object.bin?X-AMZ-Security-Token=8f0nh1jk8qvf"
```

If the object already exists, it will be overwritten.

### Generating Presigned URLs via the API

All SDK examples demonstrate calling the Telnyx API directly:

```
POST /v2/storage/buckets/{bucket_name}/{object_key}/presigned_url
Authorization: Bearer <TELNYX_API_KEY>
Content-Type: application/json

{"ttl": 30}
```

The response contains a `presigned_url` field that can be used for anonymous access.

## Object Encryption

Object encryption is currently supported only for buckets located in the US. Telnyx supports [SSE-C](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html) (Server-Side Encryption with Customer-Provided Keys).

### PutObject with SSE-C

```bash
aws s3api put-object \
  --body /path/to/file.png \
  --bucket mybestbucket \
  --key objenc \
  --sse-customer-algorithm AES256 \
  --sse-customer-key XXX
```

## Public Buckets

Making a bucket public (via bucket policy or ACL) is currently supported only for buckets located in the US and is a privileged action. The procedure is:

1. **Verify your account** — Request and obtain [Level 2 verification](https://portal.telnyx.com/#/account/my-account/verifications) status.
2. **Apply bucket policy or ACL** — Use the CLI, API, or SDK to apply the desired policy.
