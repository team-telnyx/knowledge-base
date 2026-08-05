---
title: Cloud Storage Compatibility Matrix
summary: Reference table of S3-compatible API operations supported by Telnyx Cloud
  Storage across the US, EU, and APAC regions, covering bucket, multipart, and object
  operations.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/supported
updated_at: 2026-08-05T13:39:44Z
---

# Cloud Storage Compatibility Matrix

*Part 1 of 2 — see also: [Part 2](cloud-storage-compatibility-matrix--part-2.md)*

Reference table of S3-compatible API operations supported by Telnyx Cloud Storage across the US, EU, and APAC regions, covering bucket, multipart, and object operations.

## Overview

Telnyx Cloud Storage exposes an S3-compatible API surface. The matrix below lists every API operation grouped by data type and indicates whether it is supported in each of the three Telnyx regions: US, EU, and APAC. Use it to confirm whether a given bucket, multipart, or object call is available before integrating.

## Bucket operations

Core bucket management operations are broadly supported, while advanced configuration features (analytics, encryption, intelligent tiering, inventory, metrics, notifications, ownership controls, replication, request payment, website hosting, and accelerate) are not currently available in any region.

| API Data Type | API | US | EU | APAC |
| --- | --- | --- | --- | --- |
| Bucket | CreateBucket | Yes | Yes | Yes |
| Bucket | DeleteBucket | Yes | Yes | Yes |
| Bucket | HeadBucket | Yes | Yes | Yes |
| Bucket | ListBuckets | Yes | Yes | Yes |
| BucketAccelerateConfiguration | GetBucketAccelerateConfiguration | No | No | No |
| BucketAccelerateConfiguration | PutBucketAccelerateConfiguration | No | No | No |
| BucketAcl | GetBucketAcl | Yes | No | Yes |
| BucketAcl | PutBucketAcl | Yes | No | Yes |
| BucketAnalyticsConfiguration | DeleteBucketAnalyticsConfiguration | No | No | No |
| BucketAnalyticsConfiguration | GetBucketAnalyticsConfiguration | No | No | No |
| BucketAnalyticsConfiguration | PutBucketAnalyticsConfiguration | No | No | No |
| BucketAnalyticsConfigurations | ListBucketAnalyticsConfigurations | No | No | No |
| BucketCors | DeleteBucketCors | Yes | No | Yes |
| BucketCors | GetBucketCors | Yes | No | Yes |
| BucketCors | PutBucketCors | Yes | No | Yes |
| BucketEncryption | DeleteBucketEncryption | No | No | No |
| BucketEncryption | GetBucketEncryption | No | No | No |
| BucketEncryption | PutBucketEncryption | No | No | No |
| BucketIntelligentTieringConfiguration | DeleteBucketIntelligentTieringConfiguration | No | No | No |
| BucketIntelligentTieringConfiguration | GetBucketIntelligentTieringConfiguration | No | No | No |
| BucketIntelligentTieringConfiguration | PutBucketIntelligentTieringConfiguration | No | No | No |
| BucketIntelligentTieringConfigurations | ListBucketIntelligentTieringConfigurations | No | No | No |
| BucketInventoryConfiguration | DeleteBucketInventoryConfiguration | No | No | No |
| BucketInventoryConfiguration | GetBucketInventoryConfiguration | No | No | No |
| BucketInventoryConfiguration | PutBucketInventoryConfiguration | No | No | No |
| BucketInventoryConfigurations | ListBucketInventoryConfigurations | No | No | No |
| BucketLifecycle | DeleteBucketLifecycle | Yes | No | Yes |
| BucketLifecycle | GetBucketLifecycle | No | No | No |
| BucketLifecycle | PutBucketLifecycle | No | No | No |
| BucketLifecycleConfiguration | GetBucketLifecycleConfiguration | Yes | No | Yes |
| BucketLifecycleConfiguration | PutBucketLifecycleConfiguration | Yes | No | Yes |
| BucketLocation | GetBucketLocation | Yes | Yes | Yes |
| BucketLogging | GetBucketLogging | No | No | No |
| BucketLogging | PutBucketLogging | No | No | No |
| BucketMetricsConfiguration | DeleteBucketMetricsConfiguration | No | No | No |
| BucketMetricsConfiguration | GetBucketMetricsConfiguration | No | No | No |
| BucketMetricsConfiguration | PutBucketMetricsConfiguration | No | No | No |
| BucketMetricsConfigurations | ListBucketMetricsConfigurations | No | No | No |
| BucketNotification | GetBucketNotification | No | No | No |
| BucketNotification | PutBucketNotification | No | No | No |
| BucketNotificationConfiguration | GetBucketNotificationConfiguration | No | No | No |
| BucketNotificationConfiguration | PutBucketNotificationConfiguration | No | No | No |
| BucketOwnershipControls | DeleteBucketOwnershipControls | No | No | No |
| BucketOwnershipControls | GetBucketOwnershipControls | No | No | No |
| BucketOwnershipControls | PutBucketOwnershipControls | No | No | No |
| BucketPolicy | DeleteBucketPolicy | Yes | No | Yes |
| BucketPolicy | GetBucketPolicy | Yes | No | Yes |
| BucketPolicy | PutBucketPolicy | Yes | No | Yes |
| BucketPolicyStatus | GetBucketPolicyStatus | Yes | No | Yes |
| BucketReplication | DeleteBucketReplication | No | No | No |
| BucketReplication | GetBucketReplication | No | No | No |
| BucketReplication | PutBucketReplication | No | No | No |
| BucketRequestPayment | GetBucketRequestPayment | No | No | No |
| BucketRequestPayment | PutBucketRequestPayment | No | No | No |
| BucketTagging | DeleteBucketTagging | Yes | No | Yes |
| BucketTagging | GetBucketTagging | Yes | No | Yes |
| BucketTagging | PutBucketTagging | Yes | No | Yes |
| BucketVersioning | GetBucketVersioning | Yes | No | Yes |
| BucketVersioning | PutBucketVersioning | Yes | No | Yes |
| BucketWebsite | DeleteBucketWebsite | No | No | No |
| BucketWebsite | GetBucketWebsite | No | No | No |
| BucketWebsite | PutBucketWebsite | No | No | No |

## Multipart upload operations

Multipart uploads are supported in the US and APAC regions but not in the EU. `UploadPartCopy` is not available in any region.

| API Data Type | API | US | EU | APAC |
| --- | --- | --- | --- | --- |
| Multipart | AbortMultipartUpload | Yes | No | Yes |
| Multipart | CompleteMultipartUpload | Yes | No | Yes |
| Multipart | CreateMultipartUpload | Yes | No | Yes |
| Multipart | ListMultipartUploads | Yes | No | Yes |
| Multipart | ListParts | Yes | No | Yes |
| Multipart | UploadPart | Yes | No | Yes |
| Multipart | UploadPartCopy | No | No | No |

## Object operations

Core object read, write, list, and delete operations are supported across all three regions. Version listing, ACLs, object lock configuration, retention, and tagging are limited to US and APAC. Server-side features such as `CopyObject`, `RestoreObject`, `WriteGetObjectResponse`, `GetObjectAttributes`, `SelectObjectContent`, object legal hold, and object torrent are not supported in any region.

| API Data Type | API | US | EU | APAC |
| --- | --- | --- | --- | --- |
| Object | CopyObject | No | No | No |
| Object | DeleteObject | Yes | Yes | Yes |
| Object | DeleteObjects | Yes | Yes | Yes |
| Object | GetObject | Yes | Yes | Yes |
| Object | HeadObject | Yes | Yes | Yes |
| Object | ListObjects | Yes | Yes | Yes |
| Object | ListObjectsV2 | Yes | Yes | Yes |
| Object | ListObjectVersions | Yes | No | Yes |
| Object | PutObject | Yes | Yes | Yes |
| Object | RestoreObject | No | No | No |
| Object | WriteGetObjectResponse | No | No | No |
| ObjectAcl | GetObjectAcl | Yes | No | Yes |
| ObjectAcl | PutObjectAcl | Yes | No | Yes |
| ObjectAttributes | GetObjectAttributes | No | No | No |
| ObjectContent | SelectObjectContent | No | No | No |
| ObjectLegalHold | GetObjectLegalHold | No | No | No |
| ObjectLegalHold | PutObjectLegalHold | No | No | No |
| ObjectLockConfiguration | GetObjectLockConfiguration | Yes | No | Yes |
| ObjectLockConfiguration | PutObjectLockConfiguration | No | No | No |
| ObjectRetention | GetObjectRetention | Yes | No | Yes |
| ObjectRetention | PutObjectRetention | Yes | No | Yes |
| ObjectTagging | DeleteObjectTagging | Yes | No | Yes |
| ObjectTagging | GetObjectTagging | Yes | No | Yes |
| ObjectTagging | PutObjectTagging | Yes | No | Yes |
| ObjectTorrent | GetObjectTorrent | No | No | No |

## Public access block

Public access block operations are not supported in any region.

| API Data Type | API | US | EU | APAC |
| --- | --- | --- | --- | --- |
| PublicAccessBlock | DeletePublicAccessBlock | No | No | No |
| PublicAccessBlock | GetPublicAccessBlock | No | No | No |
| PublicAccessBlock | PutPublicAccessBlock | No | No | No |
