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

*Part 2 of 2 — see also: [Part 1](cloud-storage-compatibility-matrix--part-1.md)*

Reference table of S3-compatible API operations supported by Telnyx Cloud Storage across the US, EU, and APAC regions, covering bucket, multipart, and object operations.

## Regional availability summary

- **US and APAC** offer the broadest support, including bucket ACLs, CORS, lifecycle configuration, policy, tagging, versioning, multipart uploads, object ACLs, object lock configuration (read-only), object retention, and object tagging.
- **EU** supports only the core bucket operations (`CreateBucket`, `DeleteBucket`, `HeadBucket`, `ListBuckets`, `GetBucketLocation`) and core object operations (`DeleteObject`, `DeleteObjects`, `GetObject`, `HeadObject`, `ListObjects`, `ListObjectsV2`, `PutObject`). Multipart uploads and most configuration features are not available in EU.
- **Unsupported in all regions** include accelerate, analytics, encryption, intelligent tiering, inventory, logging, metrics, notifications, ownership controls, replication, request payment, website hosting, public access block, `CopyObject`, `RestoreObject`, `WriteGetObjectResponse`, `GetObjectAttributes`, `SelectObjectContent`, object legal hold, `PutObjectLockConfiguration`, and object torrent.
