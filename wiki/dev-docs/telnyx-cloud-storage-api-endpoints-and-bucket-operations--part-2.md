---
title: Telnyx Cloud Storage API Endpoints and Bucket Operations
summary: Telnyx Cloud Storage exposes two API suites—S3-compatible and JSON companion—across
  regional endpoints, supporting standard bucket operations such as create, delete,
  and read/manage configuration for ACLs, CORS, lifecycle, location, policies, and
  tagging.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/create-bucket/index
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
updated_at: 2026-06-11T10:23:43Z
---

# Telnyx Cloud Storage API Endpoints and Bucket Operations

*Part 2 of 2 — see also: [Part 1](telnyx-cloud-storage-api-endpoints-and-bucket-operations--part-1.md)*

Telnyx Cloud Storage exposes two API suites—S3-compatible and JSON companion—across regional endpoints, supporting standard bucket operations such as create, delete, and read/manage configuration for ACLs, CORS, lifecycle, location, policies, and tagging.

## GetBucketLocation

Retrieves the region/location constraint for a bucket. Sends a `GET` request to `/<bucket_name>?location=null`.

### Example Request

```http
GET /versionedbucket?location=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
X-Amz-Date: 20230927T170849Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=107fa2b75c0af7f1982923de787b767f407718c4f1eb19937ff3445f2c0be332
```

### Example Response

```xml
<?xml version="1.0" encoding="UTF-8"?>
<LocationConstraint xmlns="http://s3.amazonaws.com/doc/2006-03-01/">us-east-1</LocationConstraint>
```

## GetBucketPolicy

Retrieves the bucket policy for a bucket.

### Example Request and Response

```bash
aws s3api get-bucket-policy --bucket pubreadbuc
```

```json
{
    "Policy": "{\n  \"Version\": \"2012-10-17\",\n  \"Statement\": [\n    {\n      \"Sid\": \"PublicReadGetObject\",\n      \"Effect\": \"Allow\",\n      \"Principal\": \"*\",\n      \"Action\": \"s3:GetObject\",\n      \"Resource\": \"arn:aws:s3:::pubreadbuc *\"\n    }\n  ]\n}"
}
```

## Authentication

All S3-compatible API requests use AWS Signature Version 4 (AWS4-HMAC-SHA256) for authentication. The `Authorization` header includes the Telnyx API key as the credential, along with a timestamp (`X-Amz-Date`) and a computed signature over signed headers. For details on authentication, see [Cloud Storage Authentication](cloud-storage-authentication.md).

## Further Reference

For the full list of supported S3 APIs, see [Cloud Storage Supported APIs](cloud-storage-supported-apis.md). For information on usage billing, presigned URLs, SSL management, and AWS S3 migration, see the JSON Companion API documentation at `api.telnyx.com`.
