---
title: Telnyx Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service that supports
  common bucket and object operations, AWS Signature Version 4 authentication (using
  a Telnyx API key), and offers both regular and AI-embedded storage tiers with usage-based
  billing across US and EU regions.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/head-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-object-versions
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-objects
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object/index
- url: https://developers.telnyx.com/docs/cloud-storage/authentication
- url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility/index
- url: https://developers.telnyx.com/docs/cloud-storage/billing
- url: https://developers.telnyx.com/docs/cloud-storage/bucket-addressing
- url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket/index
updated_at: 2026-06-11T10:24:11Z
---

# Telnyx Cloud Storage

*Part 1 of 2 — see also: [Part 2](telnyx-cloud-storage--part-2.md)*

Telnyx Cloud Storage is an S3-compatible object storage service that supports common bucket and object operations, AWS Signature Version 4 authentication (using a Telnyx API key), and offers both regular and AI-embedded storage tiers with usage-based billing across US and EU regions.

## Authentication

API requests are authenticated using a Telnyx API key passed inside an [AWS Signature Version 4 authorization header](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-auth-using-authorization-header.html). The Telnyx API key is substituted as the `access-key-id` within the `Credential` component. All other components of the authorization header (`date`, `aws-region`, `aws-service`, `secret-key`) and the generated signature are ignored — they exist only to maintain S3 compatibility. As long as the header is a valid AWS Signature Version 4 header and the Telnyx API key is in the `access-key-id` position, the request will be authenticated.

```
Authorization: AWS4-HMAC-SHA256 Credential={{your_telnyx_api_key_here}}/20221129/us-east-1/s3/aws4_request, SignedHeaders=host;range;x-amz-date, Signature=d82d11938fe5edf39a778ec710ac79899bae1d9a46ae36607be30fb55f655a3c
```

When using the AWS CLI or third-party S3 applications:
- **Access Key** → your Telnyx API token
- **Secret Access Key** → leave blank, enter a random placeholder, or duplicate the Telnyx API token

## Bucket Addressing

Two addressing styles are supported:

- **Path-style:** `https://[region].telnyxcloudstorage.com/[bucketname]/[objectname]`
- **Virtual-hosted-style:** `https://[bucketname].[region].telnyxcloudstorage.com/[objectname]`

## AWS S3 Compatibility

Telnyx Cloud Storage implements a subset of the AWS S3 API. When an unsupported API method is invoked, an S3-compatible, XML-formatted `NotImplemented` error response is returned. For supported API methods, not all AWS S3 parameters, headers, and body XML elements are supported — only those explicitly documented are available. Unsupported headers are ignored by default.

## Object Operations

### HeadObject

Retrieves metadata for an object without returning the object body. Reference: [HeadObject — Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html)

**Supported headers:** `If-Match`, `If-Modified-Since`, `If-None-Match`, `If-Unmodified-Since`, `Range`

**Example request:**

```
HEAD /mybucket/myobject HTTP/1.1
Host: [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T164456Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=d198d5440102737bd0dc5753ce6e5a843a673779ece724acd84ae08aedfe8297
```

**Example response:**

```
HTTP/1.1 200 OK
accept-ranges: bytes
content-length: 22905
content-type: image/png
etag: "2da8bc8e8133ec2af9268515aae59e7a"
last-modified: Wed, 27 Sep 2023 15:23:52 GMT
x-amz-meta-author: john
x-amz-storage-class: STANDARD
```

### ListObjects

Lists objects within a bucket. Reference: [ListObjects — Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html)

**Supported parameters:** `prefix`, `delimiter`, `marker`, `max-keys`

**Example request:**

```
GET /mybucket?prefix=myobject HTTP/1.1
Host: [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T154626Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=b77c8c94d8f0bd0913708ae7da0fbac552d14a6f2b8853b6e297a12127156e38
```

**Example response** returns a `<ListBucketResult>` XML document containing `<Contents>` entries with `Key`, `LastModified`, `ETag`, `Size`, `StorageClass`, and `Owner` details.

### ListObjectVersions

Lists all versions of objects in a version-enabled bucket. Reference: [ListObjectVersions — Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html)

**Supported parameters:** `prefix`, `delimiter`, `marker`, `max-keys`

**Example request:**

```
GET /versionedbucket?versions=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T170348Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=15c5f0d8404b4e43153138818ca4cd0895c6a0bd4b94173bb6080a71f41bc49f
```

**Example response** returns a `<ListVersionsResult>` XML document containing `<Version>` entries with `Key`, `VersionId`, `IsLatest`, `LastModified`, `ETag`, `Size`, `StorageClass`, `Owner`, and `Type` details.

### PutObject

Uploads an object to a bucket. Reference: [PutObject — Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)

**Supported headers:**
- `x-amz-acl`: `private`, `public-read`
- `x-amz-storage-class`: `STANDARD`
- `x-amz-meta-*` (custom metadata)
- `x-amz-server-side-encryption-customer-algorithm`
- `x-amz-server-side-encryption-customer-key`
- `x-amz-server-side-encryption-customer-key-MD5`

**Example request:**

```
PUT /mybucket/myobject HTTP/1.1
Host: [region].telnyxcloudstorage.com
x-amz-storage-class: STANDARD
x-amz-acl: private
x-amz-meta-author: john
Content-Type: image/png
X-Amz-Date: 20230927T152352Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature=f1a15846adc6247727c0dcfbb738d8ee4463527023e7818bf128866944981dea
Content-Length: 22

"<file contents here>"
```

### PutObjectACL

Sets the access control list for an object. Only verified users can update bucket policy — request KYC verification at [Portal Account Verifications](https://portal.telnyx.com/#/app/account/verifications). Reference: [PutObjectAcl — Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html)

**Supported headers:**
- `x-amz-acl`: `private`, `public-read`
- `versionId`

**Example request:**

```
PUT /mybucket/myobject?acl=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
x-amz-acl: public-read
X-Amz-Date: 20230927T175633Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=71b70f25be863194c5d573fdf09ea02139af3cbcaa5e16dc53a0f30d41f7311a
```

### PutObjectTagging

Sets tags on an object. Reference: [PutObjectTagging — Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html)

**Supported headers:** `versionId`

**Example request:**

```
PUT /mybucket/myobject?tagging=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
x-amz-acl: private
Content-Type: application/xml
X-Amz-Date: 20230927T180401Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-acl;x-amz-content-sha256;x-amz-date, Signature=cd6f3a0350f531a0bc89cfc145463f963fc967bcaeef2ae9d68490cee01ed8af
Content-Length: 271

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
