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

*Part 4 of 4 — see also: [Part 1](cloud-storage-api-reference--part-1.md), [Part 2](cloud-storage-api-reference--part-2.md), [Part 3](cloud-storage-api-reference--part-3.md)*

Reference documentation for Telnyx Cloud Storage S3-compatible API operations, covering bucket configuration, multipart uploads, and object management endpoints with example requests and responses.

## Object operations

### DeleteObject

Removes an object from a bucket. See the [DeleteObject S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html).

**Example request:**

```http
DELETE /publicbucket/mymultiloader_1 HTTP/1.1
Host:  [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T164329Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=539be1c5c92d8b89bcc4ea79eccb1f6e8ee3e1bd5c362dbf7b5f9bb2fa5515ca
```

### DeleteObjectTagging

Removes the tag set from an object. See the [DeleteObjectTagging S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html).

**Example request:**

```http
DELETE /mybucket/myobject?tagging=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: private
X-Amz-Date: 20230927T180605Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=361bbc366be4fa4e2f770dad0130b09948383d8e2bb58540fd469be3af24bbb0
```
