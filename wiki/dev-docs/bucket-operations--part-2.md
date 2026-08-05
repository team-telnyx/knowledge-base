---
title: Bucket operations
summary: Reference for the S3-compatible bucket operations supported by Telnyx Cloud
  Storage, covering create, delete, head, and various get/delete subresource operations
  (ACL, CORS, lifecycle, location, policy, tagging, versioning).
sources:
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
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy-status
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-versioning
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/head-bucket
updated_at: 2026-08-05T13:38:25Z
---

# Bucket operations

*Part 2 of 2 — see also: [Part 1](bucket-operations--part-1.md)*

Reference for the S3-compatible bucket operations supported by Telnyx Cloud Storage, covering create, delete, head, and various get/delete subresource operations (ACL, CORS, lifecycle, location, policy, tagging, versioning).

## GetBucketLifecycleConfiguration

Returns the lifecycle rules configured on a bucket.

**Example request**

```http
GET /versionedbucket?lifecycle=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
X-Amz-Date: 20230927T172450Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=c8e6ec2d0c5c34ea061e4dd47d2e7103fde5a885c25d9dca3ac743d8b6ab3330
```

**Example response**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Rule>
        <ID>DeleteAfterBecomingNonCurrent</ID>
        <Filter>
            <Prefix>logs/</Prefix>
        </Filter>
        <Status>Enabled</Status>
        <NoncurrentVersionExpiration>
            <NoncurrentDays>100</NoncurrentDays>
        </NoncurrentVersionExpiration>
    </Rule>
</LifecycleConfiguration>
```

See the upstream [GetBucketLifecycleConfiguration](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLifecycleConfiguration.html) reference.

## DeleteBucketLifecycle

Removes the lifecycle configuration from a bucket.

**Example request**

```http
DELETE /versionedbucket?lifecycle=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
X-Amz-Date: 20230927T173847Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=63c7e3d367d62488f9eba08ec8fdbe5bf89ef4484772b5fee952a4ac2dcd3362
```

See the upstream [DeleteBucketLifecycle](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketLifecycle.html) reference.

## GetBucketPolicy

Returns the bucket policy as JSON.

**Example request**

```bash
aws s3api get-bucket-policy --bucket pubreadbuc
```

**Example response**

```json
{
    "Policy": "{\n        \"Version\": \"2012-10-17\",\n        \"Statement\": [\n            {\n                \"Sid\": \"PublicReadGetObject\",\n                \"Effect\": \"Allow\",\n                \"Principal\": \"*\",\n                \"Action\": \"s3:GetObject\",\n                \"Resource\": \"arn:aws:s3:::pubreadbuc *\"\n            }\n        ]\n    }\n\n"
}
```

See the upstream [GetBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicy.html) reference.

## GetBucketPolicyStatus

Indicates whether the bucket's policy currently makes the bucket public.

**Example request**

```bash
aws s3api get-bucket-policy-status --bucket pubreadbuc
```

**Example response**

```json
{
    "PolicyStatus": {
        "IsPublic": true
    }
}
```

See the upstream [GetBucketPolicyStatus](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html) reference.

## DeleteBucketPolicy

Removes the policy from a bucket.

**Example request**

```bash
aws s3api delete-bucket-policy --bucket pubreadbuc
```

See the upstream [DeleteBucketPolicy](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketPolicy.html) reference.

## GetBucketTagging

Returns the tag set associated with a bucket.

**Example request**

```http
GET /versionedbucket?tagging=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
X-Amz-Date: 20230927T182418Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=94c986f7bf15c5ce04a1cdd83c0ee058d78eabfb8d0bab35caac92b965490b96
```

**Example response**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Tagging xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <TagSet>
        <Tag>
            <Key>dimention_1</Key>
            <Value>value_1</Value>
        </Tag>
        <Tag>
            <Key>dimention_2</Key>
            <Value>value_2</Value>
        </Tag>
    </TagSet>
</Tagging>
```

See the upstream [GetBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html) reference.

## DeleteBucketTagging

Removes the tag set from a bucket.

**Example request**

```http
DELETE /versionedbucket?tagging=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
X-Amz-Date: 20230927T182455Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=8bad860d937751e40011d5953da3f2463f57e30b1f00d9f25707d393f68f582b
```

See the upstream [DeleteBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html) reference.

## GetBucketVersioning

Returns the versioning state of a bucket.

**Example request**

```http
GET /versionedbucket?versioning=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
X-Amz-Date: 20230927T165704Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=8d8723b48a60f1fef06b43a2f34ca9f4426efa5ae01f9dce8fcc49cba893b69e
```

**Example response**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Status>Enabled</Status>
    <MfaDelete>Disabled</MfaDelete>
</VersioningConfiguration>
```

See the upstream [GetBucketVersioning](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html) reference.
