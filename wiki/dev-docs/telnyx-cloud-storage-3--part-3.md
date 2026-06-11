---
title: Telnyx Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service that supports
  standard AWS SDKs and third-party S3 tools. This page covers SDK integration, supported
  API operations, SSL certificate configuration, and third-party compatibility.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
- url: https://developers.telnyx.com/docs/cloud-storage/supported
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
updated_at: 2026-06-11T10:25:44Z
---

# Telnyx Cloud Storage

*Part 3 of 3 — see also: [Part 1](telnyx-cloud-storage-3--part-1.md), [Part 2](telnyx-cloud-storage-3--part-2.md)*

Telnyx Cloud Storage is an S3-compatible object storage service that supports standard AWS SDKs and third-party S3 tools. This page covers SDK integration, supported API operations, SSL certificate configuration, and third-party compatibility.

## Supported API Operations

The following table lists S3 API operations and their availability in US and EU regions.

### Bucket Operations

| Operation | US | EU |
|---|---|---|
| CreateBucket | Yes | Yes |
| DeleteBucket | Yes | Yes |
| HeadBucket | Yes | Yes |
| ListBuckets | Yes | Yes |
| GetBucketAcl | Yes | No |
| PutBucketAcl | Yes | No |
| DeleteBucketCors | Yes | No |
| GetBucketCors | Yes | No |
| PutBucketCors | Yes | No |
| DeleteBucketLifecycle | Yes | No |
| GetBucketLifecycleConfiguration | Yes | No |
| PutBucketLifecycleConfiguration | Yes | No |
| GetBucketLocation | Yes | Yes |
| DeleteBucketPolicy | Yes | No |
| GetBucketPolicy | Yes | No |
| PutBucketPolicy | Yes | No |
| GetBucketPolicyStatus | Yes | No |
| DeleteBucketTagging | Yes | No |
| GetBucketTagging | Yes | No |
| PutBucketTagging | Yes | No |
| GetBucketVersioning | Yes | No |
| PutBucketVersioning | Yes | No |

### Object Operations

| Operation | US | EU |
|---|---|---|
| DeleteObject | Yes | Yes |
| DeleteObjects | Yes | Yes |
| GetObject | Yes | Yes |
| HeadObject | Yes | Yes |
| ListObjects | Yes | Yes |
| ListObjectsV2 | Yes | Yes |
| ListObjectVersions | Yes | No |
| PutObject | Yes | Yes |
| GetObjectAcl | Yes | No |
| PutObjectAcl | Yes | No |
| DeleteObjectTagging | Yes | No |
| GetObjectTagging | Yes | No |
| PutObjectTagging | Yes | No |

### Multipart Upload Operations

| Operation | US | EU |
|---|---|---|
| AbortMultipartUpload | Yes | No |
| CompleteMultipartUpload | Yes | No |
| CreateMultipartUpload | Yes | No |
| ListMultipartUploads | Yes | No |
| ListParts | Yes | No |
| UploadPart | Yes | No |

### Unsupported Operations

The following S3 API operations are **not** supported in either region:

- BucketAccelerateConfiguration (Get/Put)
- BucketAnalyticsConfiguration (Delete/Get/Put/List)
- BucketEncryption (Delete/Get/Put)
- BucketIntelligentTieringConfiguration (Delete/Get/Put/List)
- BucketInventoryConfiguration (Delete/Get/Put/List)
- BucketLogging (Get/Put)
- BucketMetricsConfiguration (Delete/Get/Put/List)
- BucketNotification / BucketNotificationConfiguration (Get/Put)
- BucketOwnershipControls (Delete/Get/Put)
- BucketReplication (Delete/Get/Put)
- BucketRequestPayment (Get/Put)
- BucketWebsite (Delete/Get/Put)
- CopyObject
- ObjectAttributes (Get)
- ObjectContent / SelectObjectContent
- ObjectLegalHold (Get/Put)
- ObjectLockConfiguration (Get/Put)
- ObjectRetention (Get/Put)
- ObjectTorrent (Get)
- PublicAccessBlock (Delete/Get/Put)
- RestoreObject
- UploadPartCopy
- WriteGetObjectResponse

## Third-Party S3 Tools

All S3-compatible third-party tools, applications, clients, and libraries can be used with Telnyx Cloud Storage. This includes popular applications such as Cyberduck, S3 Browser, and Wal-G. Configuration guides for many common tools are available on the [Telnyx support page](https://support.telnyx.com/en/collections/3840515-telnyx-storage). If a guide for your specific application is not listed, you can request one through the [Telnyx contact page](https://telnyx.com/contact-us).
