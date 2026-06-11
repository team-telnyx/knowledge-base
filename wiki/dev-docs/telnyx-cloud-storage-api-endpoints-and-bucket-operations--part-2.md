---
title: Telnyx Cloud Storage API Endpoints and Bucket Operations
summary: Telnyx Cloud Storage exposes two API suites—S3-compatible and JSON companion—across
  regional endpoints, supporting standard bucket operations such as create, delete,
  and read/manage configuration for ACLs, CORS, lifecycle, location, policies, and
  tagging.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints
  content_hash: 98f1fa942fcaccc32b04c3177e42a4380bc1193c71cc43b44e778ce07385ec73
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/create-bucket/index
  content_hash: e2ae6f80201ebc985e167de32e9432cf35490def75af1771e36fbe2e7226ec47
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket
  content_hash: 50e58fea2ce528d133348d2c55833192d9a9d2b11836843ab84dc56d6ddb61df
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-cors
  content_hash: 53d998f51997d9709ff7495cb1d7b2d0e74f528698af38f653fa421e94aadd96
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-lifecycle
  content_hash: 60413968890156256ba3bb8875490eca55062fbdc360b30f2413678ad42b8ca6
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-policy
  content_hash: 370cee6ec16fd81ab858d9ee781ee4462799150fc094d17332b9830853760098
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-tagging
  content_hash: 4333b762f66823aec97427f0e10622e7c6448e092060d6a0fdddbcea995c4a9d
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-acl
  content_hash: 2c4fdb338a1582bf6eb236385dd3e5bd7723472cfd3f08c31168596201b7a2b1
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-cors
  content_hash: 071f50de22efcd21410d12535d7fa98280c720586aee4becf607bf0ae7387d10
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-lifecycle-configuration
  content_hash: 2aac1b025f1dadc5914c689bfd7f8cc277208638d18c085bded70d7ae5717760
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-location
  content_hash: 14284665f58cb846e491872b0a2e650e02683a5622072d55661ab8f58c9e0e50
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy
  content_hash: 863e1881922140eee15011926cd102b12b4aecd6be50a7d6d3ef172d71529344
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
