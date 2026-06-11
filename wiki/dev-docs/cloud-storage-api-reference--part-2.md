---
title: Cloud Storage API Reference
summary: Reference for the Telnyx Cloud Storage S3-compatible API, covering multipart
  upload operations (create, upload part, list, complete, abort) and object operations
  (get, delete, tagging, ACL) with supported parameters, headers, and example requests
  and responses.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/abort-multipart-upload
  content_hash: dea3f1deffdd04005a68935c156addbc8cad07231094c6c9f4f24cc6cd25b546
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload/index
  content_hash: b66db916180a1f5b3de32f0d508f5a3cc4c68a1fb6282615b39ca19bb6c10246
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload/index
  content_hash: 4068d3bcc4747f054dbf6218a165d3a624989fe9e93061b5c1427593d6eb95be
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-multipart-uploads
  content_hash: ee01f643a0cfee3fd89226bcdff8b2e38f5b8b8db69e6ea112c4d3c0f8094692
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-parts
  content_hash: 3ed8eb5343215975a6bf98b45663e3c19358810e4ed1b33c59860538f93d4eff
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part/index
  content_hash: 0cfaa46874a1b59f1a4d2176fb26481ddd20777fd2ed78354627ad2d18ee69ef
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object
  content_hash: 8eda99d92c525547882b14578344e5b17f87693a439987b6b9838dff6dd3bc9f
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object-tagging
  content_hash: 622705ee5af57f4d136eed587965fc2bb60c10f7887b5ad7623cf5f6ca0d2ef5
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-objects
  content_hash: 5445b19bd980c81c8960a9e399bdcc50359e16d0afe9e05607fd4114fd229664
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object
  content_hash: 366484e0e4a80684a62bdacbebca0a838493f11af9b34ad50763dd7f537ec674
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-acl
  content_hash: 5bb9cd874e28a6d954106bbaddc015383de9c95b6fbb943c8641baaba8a32dfa
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-tagging
  content_hash: 6cde84ad935cf8c9111e196507fb1f41b1acfe0bbb977ae242f9255892c641f8
updated_at: 2026-06-11T10:24:17Z
---

# Cloud Storage API Reference

*Part 2 of 2 — see also: [Part 1](cloud-storage-api-reference--part-1.md)*

Reference for the Telnyx Cloud Storage S3-compatible API, covering multipart upload operations (create, upload part, list, complete, abort) and object operations (get, delete, tagging, ACL) with supported parameters, headers, and example requests and responses.

## Get Object

Retrieves an object. Corresponds to [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html).

**Supported headers:**

- `If-Match`
- `If-Modified-Since`
- `If-None-Match`
- `If-Unmodified-Since`
- `Range`

**Example request:**

```
GET /mybucket/myobject HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: application/octet-stream
X-Amz-Date: 20230927T152801Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=41797df5b33f76003806aeb1eba3f25e108ecdb8582e6575e3bb1aaff4ddb839
```

## Get Object ACL

Returns the access control list for an object. Corresponds to [GetObjectAcl](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html).

**Example request:**

```
GET /mybucket/myobject?acl=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
x-amz-acl: private
X-Amz-Date: 20230927T175743Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=4edb4e62f2a28e4ff8e6b317fd867b4baf382b3c87b26e2404ea7a766779be4d
```

**Example response:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Owner>
        <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
        <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
    </Owner>
    <AccessControlList>
        <Grant>
            <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
                <URI>http://acs.amazonaws.com/groups/global/AllUsers</URI>
            </Grantee>
            <Permission>READ</Permission>
        </Grant>
        <Grant>
            <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
                <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
                <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
            </Grantee>
            <Permission>FULL_CONTROL</Permission>
        </Grant>
    </AccessControlList>
</AccessControlPolicy>
```

## Get Object Tagging

Returns the tags associated with an object. Corresponds to [GetObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html).

**Example request:**

```
GET /mybucket/myobject?tagging=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
x-amz-acl: private
X-Amz-Date: 20230927T180458Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=655002dff20fc340dcfb66b4e06595ddfe950b9e091992f4c82ac0777b42ff8e
```

**Example response:**

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

## Delete Object

Removes a single object from a bucket. Corresponds to [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html).

**Example request:**

```
DELETE /publicbucket/mymultiloader_1 HTTP/1.1
Host: [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T164329Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=539be1c5c92d8b89bcc4ea79eccb1f6e8ee3e1bd5c362dbf7b5f9bb2fa5515ca
```

## Delete Objects

Removes multiple objects from a bucket in a single request. Corresponds to [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html).

**Example using the AWS S3 CLI:**

First, list the objects in the bucket:

```bash
aws s3api list-objects --bucket created-in-fl-1
```

```json
{
    "Contents": [
        { "Key": "xxx", "ETag": "\"2da8bc8e8133ec2af9268515aae59e7a\"", "Size": 22905, "StorageClass": "STANDARD" },
        { "Key": "yyy", "ETag": "\"2da8bc8e8133ec2af9268515aae59e7a\"", "Size": 22905, "StorageClass": "STANDARD" },
        { "Key": "zzz", "ETag": "\"2da8bc8e8133ec2af9268515aae59e7a\"", "Size": 22905, "StorageClass": "STANDARD" }
    ]
}
```

Then delete selected objects:

```bash
aws s3api delete-objects --delete '{"Objects":[{"Key":"xxx"},{"Key":"yyy"}]}' --bucket created-in-fl-1
```

```json
{
    "Deleted": [
        { "Key": "xxx" },
        { "Key": "yyy" }
    ]
}
```

## Delete Object Tagging

Removes the tag set from an object. Corresponds to [DeleteObjectTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjectTagging.html).

**Example request:**

```
DELETE /mybucket/myobject?tagging=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
x-amz-acl: private
X-Amz-Date: 20230927T180605Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=361bbc366be4fa4e2f770dad0130b09948383d8e2bb58540fd469be3af24bbb0
```
