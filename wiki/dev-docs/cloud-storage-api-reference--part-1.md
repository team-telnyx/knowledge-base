---
title: Cloud Storage API Reference
summary: Reference documentation for Telnyx Cloud Storage S3-compatible API operations,
  covering bucket configuration, multipart uploads, and object management endpoints
  with example requests and responses.
sources:
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
updated_at: 2026-08-05T13:38:44Z
---

# Cloud Storage API Reference

*Part 1 of 4 — see also: [Part 2](cloud-storage-api-reference--part-2.md), [Part 3](cloud-storage-api-reference--part-3.md), [Part 4](cloud-storage-api-reference--part-4.md)*

Reference documentation for Telnyx Cloud Storage S3-compatible API operations, covering bucket configuration, multipart uploads, and object management endpoints with example requests and responses.

## Overview

Telnyx Cloud Storage provides an S3-compatible object storage API. All requests are signed using AWS Signature Version 4 (AWS4-HMAC-SHA256) with your Telnyx API key as the credential. The endpoint host follows the pattern `[region].telnyxcloudstorage.com`. Each operation below links to the corresponding Amazon S3 API reference for full parameter semantics.

> **Note:** Some operations (such as updating bucket ACL or bucket policy) require a verified user account. To request KYC verification, visit [Portal Account Verifications](https://portal.telnyx.com/#/app/account/verifications).
