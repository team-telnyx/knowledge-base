---
title: Compatibility Matrix
summary: Review the comprehensive compatibility matrix for Telnyx Cloud Storage, covering a wide range of API functionalities.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/supported/index
    content_hash: 29fc8aa3d17197f0b09d64881725a3466f64e6417cc56c197ed8d7cf722fa3d6
updated_at: 2026-04-10T00:00:00Z
---

# Compatibility Matrix

Review the comprehensive compatibility matrix for Telnyx Cloud Storage, covering a wide range of API functionalities.

| API Data Type                          | API                                         | Supported in US | Supported in EU |
| -------------------------------------- | ------------------------------------------- | --------------- | --------------- |
| Bucket                                 | CreateBucket                                | Yes             | Yes             |
| Bucket                                 | DeleteBucket                                | Yes             | Yes             |
| Bucket                                 | HeadBucket                                  | Yes             | Yes             |
| Bucket                                 | ListBuckets                                 | Yes             | Yes             |
| BucketAccelerateConfiguration          | GetBucketAccelerateConfiguration            | No              | No              |
| BucketAccelerateConfiguration          | PutBucketAccelerateConfiguration            | No              | No              |
| BucketAcl                              | GetBucketAcl                                | Yes             | No              |
| BucketAcl                              | PutBucketAcl                                | Yes             | No              |
| BucketAnalyticsConfiguration           | DeleteBucketAnalyticsConfiguration          | No              | No              |
| BucketAnalyticsConfiguration           | GetBucketAnalyticsConfiguration             | No              | No              |
| BucketAnalyticsConfiguration           | PutBucketAnalyticsConfiguration             | No              | No              |
| BucketAnalyticsConfigurations          | ListBucketAnalyticsConfigurations           | No              | No              |
| BucketCors                             | DeleteBucketCors                            | Yes             | No              |
| BucketCors                             | GetBucketCors                               | Yes             | No              |
| BucketCors                             | PutBucketCors                               | Yes             | No              |
| BucketEncryption                       | DeleteBucketEncryption                      | No              | No              |
| BucketEncryption                       | GetBucketEncryption                         | No              | No              |
| BucketEncryption                       | PutBucketEncryption                         | No              | No              |
| BucketIntelligentTieringConfiguration  | DeleteBucketIntelligentTieringConfiguration | No              | No              |
| BucketIntelligentTieringConfiguration  | GetBucketIntelligentTieringConfiguration    | No              | No              |
| BucketIntelligentTieringConfiguration  | PutBucketIntelligentTieringConfiguration    | No              | No              |
| BucketIntelligentTieringConfigurations | ListBucketIntelligentTieringConfigurations  | No              | No              |
| BucketInventoryConfiguration           | DeleteBucketInventoryConfiguration          | No              | No              |
| BucketInventoryConfiguration           | GetBucketInventoryConfiguration             | No              | No              |
| BucketInventoryConfiguration           | PutBucketInventoryConfiguration             | No              | No              |
| BucketInventoryConfigurations          | ListBucketInventoryConfigurations           | No              | No              |
| BucketLifecycle                        | DeleteBucketLifecycle                       | Yes             | No              |
| BucketLifecycle                        | GetBucketLifecycle                          | No              | No              |
| BucketLifecycle                        | PutBucketLifecycle                          | No              | No              |
| BucketLifecycleConfiguration           | GetBucketLifecycleConfiguration             | Yes             | No              |
| BucketLifecycleConfiguration           | PutBucketLifecycleConfiguration             | Yes             | No              |
| BucketLocation                         | GetBucketLocation                           | Yes             | Yes             |
| BucketLogging                          | GetBucketLogging                            | No              | No              |
| BucketLogging                          | PutBucketLogging                            | No              | No              |
| BucketMetricsConfiguration             | DeleteBucketMetricsConfiguration            | No              | No              |
| BucketMetricsConfiguration             | GetBucketMetricsConfiguration               | No              | No              |
| BucketMetricsConfiguration             | PutBucketMetricsConfiguration               | No              | No              |
| BucketMetricsConfigurations            | ListBucketMetricsConfigurations             | No              | No              |
| BucketNotification                     | GetBucketNotification                       | No              | No              |
| BucketNotification                     | PutBucketNotification                       | No              | No              |
| BucketNotificationConfiguration        | GetBucketNotificationConfiguration          | No              | No              |
| BucketNotificationConfiguration        | PutBucketNotificationConfiguration          | No              | No              |
| BucketOwnershipControls                | DeleteBucketOwnershipControls               | No              | No              |
| BucketOwnershipControls                | GetBucketOwnershipControls                  | No              | No              |
| BucketOwnershipControls                | PutBucketOwnershipControls                  | No              | No              |
| BucketPolicy                           | DeleteBucketPolicy                          | Yes             | No              |
| BucketPolicy                           | GetBucketPolicy                             | Yes             | No              |
| BucketPolicy                           | PutBucketPolicy                             | Yes             | No              |
| BucketPolicyStatus                     | GetBucketPolicyStatus                       | Yes             | No              |
| BucketReplication                      | DeleteBucketReplication                     | No              | No              |
| BucketReplication                      | GetBucketReplication                        | No              | No              |
| BucketReplication                      | PutBucketReplication                        | No              | No              |
| BucketRequestPayment                   | GetBucketRequestPayment                     | No              | No              |
| BucketRequestPayment                   | PutBucketRequestPayment                     | No              | No              |
| BucketTagging                          | DeleteBucketTagging                         | Yes             | No              |
| BucketTagging                          | GetBucketTagging                            | Yes             | No              |
| BucketTagging                          | PutBucketTagging                            | Yes             | No              |
| BucketVersioning                       | GetBucketVersioning                         | Yes             | No              |
| BucketVersioning                       | PutBucketVersioning                         | Yes             | No              |
| BucketWebsite                          | DeleteBucketWebsite                         | No              | No              |
| BucketWebsite                          | GetBucketWebsite                            | No              | No              |
| BucketWebsite                          | PutBucketWebsite                            | No              | No              |
| Multipart                              | AbortMultipartUpload                        | Yes             | No              |
| Multipart                              | CompleteMultipartUpload                     | Yes             | No              |
| Multipart                              | CreateMultipartUpload                       | Yes             | No              |
| Multipart                              | ListMultipartUploads                        | Yes             | No              |
| Multipart                              | ListParts                                   | Yes             | No              |
| Multipart                              | UploadPart                                  | Yes             | No              |
| Multipart                              | UploadPartCopy                              | No              | No              |
| Object                                 | CopyObject                                  | No              | No              |
| Object                                 | DeleteObject                                | Yes             | Yes             |
| Object                                 | DeleteObjects                               | Yes             | Yes             |
| Object                                 | GetObject                                   | Yes             | Yes             |
| Object                                 | HeadObject                                  | Yes             | Yes             |
| Object                                 | ListObjects                                 | Yes             | Yes             |
| Object                                 | ListObjectsV2                               | Yes             | Yes             |
| Object                                 | ListObjectVersions                          | Yes             | No              |
| Object                                 | PutObject                                   | Yes             | Yes             |
| Object                                 | RestoreObject                               | No              | No              |
| Object                                 | WriteGetObjectResponse                      | No              | No              |
| ObjectAcl                              | GetObjectAcl                                | Yes             | No              |
| ObjectAcl                              | PutObjectAcl                                | Yes             | No              |
| ObjectAttributes                       | GetObjectAttributes                         | No              | No              |
| ObjectContent                          | SelectObjectContent                         | No              | No              |
| ObjectLegalHold                        | GetObjectLegalHold                          | No              | No              |
| ObjectLegalHold                        | PutObjectLegalHold                          | No              | No              |
| ObjectLockConfiguration                | GetObjectLockConfiguration                  | No              | No              |
| ObjectLockConfiguration                | PutObjectLockConfiguration                  | No              | No              |
| ObjectRetention                        | GetObjectRetention                          | No              | No              |
| ObjectRetention                        | PutObjectRetention                          | No              | No              |
| ObjectTagging                          | DeleteObjectTagging                         | Yes             | No              |
| ObjectTagging                          | GetObjectTagging                            | Yes             | No              |
| ObjectTagging                          | PutObjectTagging                            | Yes             | No              |
| ObjectTorrent                          | GetObjectTorrent                            | No              | No              |
| PublicAccessBlock                      | DeletePublicAccessBlock                     | No              | No              |
| PublicAccessBlock                      | GetPublicAccessBlock                        | No              | No              |
| PublicAccessBlock                      | PutPublicAccessBlock                        | No              | No              |


## Related Pages

- [Compatibility](../runbooks/compatibility.md)
- [Compatibility with AWS S3](../runbooks/compatibility-with-aws-s3.md)
