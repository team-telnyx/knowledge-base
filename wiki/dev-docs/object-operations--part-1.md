---
title: Object Operations
summary: Reference documentation for the S3-compatible object operations supported
  by Telnyx Cloud Storage, covering read, write, listing, tagging, ACL, and versioning
  endpoints with example requests and responses.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-objects
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/head-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-object-versions
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-objects
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object/index
updated_at: 2026-08-05T13:38:58Z
---

# Object Operations

*Part 1 of 2 — see also: [Part 2](object-operations--part-2.md)*

Reference documentation for the S3-compatible object operations supported by Telnyx Cloud Storage, covering read, write, listing, tagging, ACL, and versioning endpoints with example requests and responses.

## Overview

Telnyx Cloud Storage exposes an S3-compatible object API. Each operation below maps to the equivalent Amazon S3 API and is invoked against the regional endpoint `[region].telnyxcloudstorage.com` using AWS Signature Version 4 (`AWS4-HMAC-SHA256`) with your Telnyx API key as the credential. For the upstream S3 specification of any operation, follow the linked AWS reference.

## PutObject

Creates or replaces an object in a bucket. See the [AWS PutObject reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html) for the full specification.

**Supported headers:**

- `x-amz-acl` — `private` or `public-read`
- `x-amz-storage-class` — `STANDARD`
- `x-amz-meta-*`
- `x-amz-server-side-encryption-customer-algorithm`
- `x-amz-server-side-encryption-customer-key`
- `x-amz-server-side-encryption-customer-key-MD5`

Example request:

```
PUT /mybucket/myobject HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-storage-class: STANDARD
x-amz-acl: private
x-amz-meta-author: john
Content-Type: image/png
X-Amz-Date: 20230927T152352Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature=f1a15846adc6247727c0dcfbb738d8ee4463527023e7818bf128866944981dea
Content-Length: 22

"<file contents here>"
```

## GetObject

Retrieves an object's contents and metadata. See the [AWS GetObject reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html) for the full specification.

**Supported headers:**

- `If-Match`
- `If-Modified-Since`
- `If-None-Match`
- `If-Unmodified-Since`
- `Range`

Example request:

```
GET /mybucket/myobject HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: application/octet-stream
X-Amz-Date: 20230927T152801Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=41797df5b33f76003806aeb1eba3f25e108ecdb8582e6575e3bb1aaff4ddb839
```

## HeadObject

Returns object metadata without the body. See the [AWS HeadObject reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html) for the full specification.

**Supported headers:**

- `If-Match`
- `If-Modified-Since`
- `If-None-Match`
- `If-Unmodified-Since`
- `Range`

Example request:

```
HEAD /mybucket/myobject HTTP/1.1
Host:  [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T164456Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=d198d5440102737bd0dc5753ce6e5a843a673779ece724acd84ae08aedfe8297
```

Example response:

```
HTTP/1.1 200 OK
accept-ranges: bytes
content-length: 22905
content-type: image/png
date: Wed, 27 Sep 2023 16:47:00 GMT
etag: "2da8bc8e8133ec2af9268515aae59e7a"
last-modified: Wed, 27 Sep 2023 15:23:52 GMT
x-amz-meta-author: john
x-amz-request-id: tx00000b6702bae22c9729e-0065145c84-e3bf-fl1
x-amz-storage-class: STANDARD
x-rgw-object-type: Normal
server: Telnyx API
```

## DeleteObjects

Removes multiple objects from a bucket in a single request. See the [AWS DeleteObjects reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObjects.html) for the full specification.

Example using the AWS S3 CLI. The bucket `created-in-fl-1` initially contains three objects (`xxx`, `yyy`, `zzz`):

```
user@host ~ % aws s3api list-objects --bucket created-in-fl-1

{
    "Contents": [
        {
            "Key": "xxx",
            "LastModified": "2023-10-02T19:11:54.788000+00:00",
            "ETag": "\"2da8bc8e8133ec2af9268515aae59e7a\"",
            "Size": 22905,
            "StorageClass": "STANDARD",
            "Owner": {
                "DisplayName": "xd",
                "ID": "xd"
            }
        },
        {
            "Key": "yyy",
            "LastModified": "2023-10-02T19:11:38.436000+00:00",
            "ETag": "\"2da8bc8e8133ec2af9268515aae59e7a\"",
            "Size": 22905,
            "StorageClass": "STANDARD",
            "Owner": {
                "DisplayName": "xd",
                "ID": "xd"
            }
        },
        {
            "Key": "zzz",
            "LastModified": "2023-10-02T19:11:25.551000+00:00",
            "ETag": "\"2da8bc8e8133ec2af9268515aae59e7a\"",
            "Size": 22905,
            "StorageClass": "STANDARD",
            "Owner": {
                "DisplayName": "xd",
                "ID": "xd"
            }
        }
    ],
    "RequestCharged": null
}
```

Deleting `xxx` and `yyy`:

```
user@host ~ % aws s3api delete-objects --delete '{"Objects":[{"Key":"xxx"},{"Key":"yyy"}]}' --bucket created-in-fl-1

{
    "Deleted": [
        {
            "Key": "xxx"
        },
        {
            "Key": "yyy"
        }
    ]
}
```

## ListObjects

Returns some or all (up to 1,000) of the objects in a bucket. See the [AWS ListObjects reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html) for the full specification.

**Supported parameters:**

- `prefix`
- `delimiter`
- `marker`
- `max-keys`

Example request:

```
GET /mybucket?prefix=myobject HTTP/1.1
Host:  [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T154626Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=b77c8c94d8f0bd0913708ae7da0fbac552d14a6f2b8853b6e297a12127156e38
```

Example response:

```
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Name>mybucket</Name>
    <Prefix>myobject</Prefix>
    <MaxKeys>1000</MaxKeys>
    <IsTruncated>false</IsTruncated>
    <Contents>
        <Key>myobject</Key>
        <LastModified>2023-09-27T15:23:52.668Z</LastModified>
        <ETag>&quot;2da8bc8e8133ec2af9268515aae59e7a&quot;</ETag>
        <Size>22905</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
            <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
            <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
        </Owner>
        <Type>Normal</Type>
    </Contents>
    <Contents>
        <Key>myobject_2</Key>
        <LastModified>2023-09-27T15:44:06.670Z</LastModified>
        <ETag>&quot;0e43168b1e60136a3d4292c54763d449&quot;</ETag>
        <Size>27761</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
            <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
            <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
        </Owner>
        <Type>Normal</Type>
    </Contents>
    <Marker></Marker>
</ListBucketResult>
```
