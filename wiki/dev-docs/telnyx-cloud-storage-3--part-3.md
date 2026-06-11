---
title: Telnyx Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service that supports
  standard AWS SDKs and third-party S3 tools. This page covers SDK integration, supported
  API operations, SSL certificate configuration, and third-party compatibility.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
  content_hash: 557f66728d24bc407e8e5a23df3fb036191a9547a66935915e658730f22b1943
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
  content_hash: a03b4e1572b7b695ac821993afc55add9dbbb3eb679c19c085d9a2fc9da4ab4c
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
  content_hash: 6da5801c698f795bde27af7770adc427d7f496ed6eda5853b5afdec508302d58
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
  content_hash: 1b2ff4d4d7fd27ad2f7fb2d016d22a8d20d482a161670708923cde4ee797f05f
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
  content_hash: bef5c483f31f5b02559d529398af82e64b310db6369c65644f435be2b5561e91
- url: https://developers.telnyx.com/docs/cloud-storage/supported
  content_hash: fc00383afc647bc1000db8bb56c40a035c44dfbe0983aa9667aa26ae4afe69f4
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
  content_hash: f13747eb826c99839d3a3c677d09530be46a09b92f4b842a952fc180a8d0a78a
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
