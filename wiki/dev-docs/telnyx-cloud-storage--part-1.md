---
title: Telnyx Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service that supports
  common bucket and object operations, AWS Signature Version 4 authentication (using
  a Telnyx API key), and offers both regular and AI-embedded storage tiers with usage-based
  billing across US and EU regions.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/head-object
  content_hash: d32708769642ca1db1336fd456d711fb222b3ccbcd6b261e364456998e8ed735
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-object-versions
  content_hash: e50a907003a37fa41150d767b84940e21c27dee474798a545b134a2248924ddc
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-objects
  content_hash: 827fa038125e1b5606387d61f1f1e81417213bf8754d18e29c87d2b7b97a0a26
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-acl
  content_hash: ea4352a64e3ce6e530ebf09595811da8041d128ae46966167449f842aff19984
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-tagging
  content_hash: c92c1155cd485a78986414879f8ccc0a4db98d74023f16802df2a545cc8a8499
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object/index
  content_hash: a37f16baa6af872c0589483f913902ecb90f52a712db50f5fcc06f5637077b49
- url: https://developers.telnyx.com/docs/cloud-storage/authentication
  content_hash: ff7b6266c6fc1d6ebe4847cad651f67de9a5b26a48fea51e529e384ade5a57b4
- url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility/index
  content_hash: 56bddefa880590ca53e93c8817c90419baa5166c0f9206568b702d689cac6aaf
- url: https://developers.telnyx.com/docs/cloud-storage/billing
  content_hash: bb0357a174fedeb9ff9ed4cd1aad275b87b88214ca18647daba8dd6849dcc897
- url: https://developers.telnyx.com/docs/cloud-storage/bucket-addressing
  content_hash: 46d7fbf3e433e1bb9a4d158172f241500cf57d8aee6f69498fba113385694aad
- url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket/index
  content_hash: fa40a29da2be02c25a1d2c770fa5a8cc542eaa8dad59b425ee7beeee107ce835
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
