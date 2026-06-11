---
title: Cloud Storage Bucket Operations
summary: Reference for Telnyx Cloud Storage bucket-level API operations, which are
  S3-compatible and authenticated via AWS4-HMAC-SHA256. Covers read operations (ListBuckets,
  HeadBucket, GetBucketPolicyStatus, GetBucketTagging, GetBucketVersioning) and write
  operations (PutBucketAcl, PutBucketCors, PutBucketLifecycleConfiguration, PutBucketPolicy,
  PutBucketTagging, PutBucketVersioning).
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy-status
  content_hash: e7309c8585a325a9f7646fde8b0bb6a101d716ad9920513678d37588ee7f0bb2
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-tagging
  content_hash: 36b548778be13b6ce9d0a9f78867813fdbed720b8c9a8ef9ee68617a7b3c2977
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-versioning
  content_hash: 1e9541fa7be1d5856d41ab3136c0d49215666b92f100910cfb65aff65d270932
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/head-bucket
  content_hash: b279ec592c25ea35f53ae2c1c2612acd39ed0354fd23f8d06fcdb4f1013c4f89
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/list-bucket
  content_hash: 1777780a4b3e11bad2be84703a2ad9e5ac7a268aec3dc50790e37893c449a86c
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl/index
  content_hash: 0bd5c06b4e68647c4435e152bd07e9853091e84f3ddefb09edb36c8fcd7493b5
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-cors
  content_hash: d8e86f79098416ae0aa2ba4c5d5bb8d819014bba29123431be6a00fb94a40a30
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-life-cycle-configuration
  content_hash: 324262e167065a6081c00b116b4ac42c02d8618710f716ef68346cb3923d5c61
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy/index
  content_hash: 980305a0027e7ed9806ac211c31b4c495764174ab294c1807f34ceccb98f1a31
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-tagging
  content_hash: a81fe2cdfed2ec445aff513775dc7abff8df667d9647e1c1c1d03b6a2cd0ab8a
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-versioning
  content_hash: 0601b1a7a12349604de7691cb7a14a3cbc7ed62e51c969c3cff5943a9b0560b2
updated_at: 2026-06-11T10:23:15Z
---

# Cloud Storage Bucket Operations

Reference for Telnyx Cloud Storage bucket-level API operations, which are S3-compatible and authenticated via AWS4-HMAC-SHA256. Covers read operations (ListBuckets, HeadBucket, GetBucketPolicyStatus, GetBucketTagging, GetBucketVersioning) and write operations (PutBucketAcl, PutBucketCors, PutBucketLifecycleConfiguration, PutBucketPolicy, PutBucketTagging, PutBucketVersioning).

All bucket operations target the host `[region].telnyxcloudstorage.com` and use AWS4-HMAC-SHA256 authorization with the `YOUR_TELNYX_API_KEY` credential scoped to `test/execute-api/aws4_request`. For full S3 API semantics, refer to the [Amazon S3 API Reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations_Buckets.html).

## List Buckets

Returns all buckets owned by the authenticated user.

**Request**

```
GET / HTTP/1.1
Host: [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T165213Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=...
```

**Response** — XML with `<ListAllMyBucketsResult>` containing `<Owner>` (ID and DisplayName) and `<Buckets>` listing each bucket's `<Name>` and `<CreationDate>`.

## Head Bucket

Checks whether a bucket exists and is accessible. Returns metadata in response headers.

**Request**

```
HEAD /versionedbucket HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
X-Amz-Date: 20230927T174619Z
Authorization: AWS4-HMAC-SHA256 ...
```

**Response** — `200 OK` with headers including:

- `x-rgw-bytes-used` — total bytes used in the bucket
- `x-rgw-object-count` — number of objects
- `x-rgw-quota-bucket-objects`, `x-rgw-quota-bucket-size` — per-bucket quotas (`-1` = unlimited)
- `x-rgw-quota-max-buckets`, `x-rgw-quota-user-objects`, `x-rgw-quota-user-size` — per-user quotas (`-1` = unlimited)

## Get Bucket Policy Status

Indicates whether a bucket has a public policy. Can also be invoked via the AWS CLI:

```
aws s3api get-bucket-policy-status --bucket pubreadbuc
```

**Response**

```json
{
    "PolicyStatus": {
        "IsPublic": true
    }
}
```

## Get Bucket Tagging

Returns the tag set applied to a bucket.

**Request**

```
GET /versionedbucket?tagging=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
X-Amz-Date: 20230927T182418Z
Authorization: AWS4-HMAC-SHA256 ...
```

**Response**

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

## Get Bucket Versioning

Returns the versioning state of a bucket.

**Request**

```
GET /versionedbucket?versioning=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
X-Amz-Date: 20230927T165704Z
Authorization: AWS4-HMAC-SHA256 ...
```

**Response**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Status>Enabled</Status>
    <MfaDelete>Disabled</MfaDelete>
</VersioningConfiguration>
```

## Put Bucket ACL

Sets the access control list for a bucket. Only verified users can update bucket policy — request KYC verification via [Portal Account Verifications](https://portal.telnyx.com/#/app/account/verifications).

**Supported `x-amz-acl` header values:**

- `private`
- `public-read`

**Request**

```
PUT /versionedbucket?acl=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: public-read
X-Amz-Date: 20230927T174201Z
Authorization: AWS4-HMAC-SHA256 ...
```

## Put Bucket CORS

Sets the CORS configuration for a bucket. Prepare a JSON file with `CORSRules` and apply it with the AWS CLI.

**JSON configuration file (`cors.json`)**

```json
{
  "CORSRules": [
    {
      "AllowedOrigins": ["http://www.example.com"],
      "AllowedMethods": ["PUT", "POST", "DELETE"],
      "AllowedHeaders": ["*"]
    },
    {
      "AllowedOrigins": ["*"],
      "AllowedMethods": ["GET"]
    }
  ]
}
```

**Apply via CLI**

```
aws s3api put-bucket-cors --bucket my_bucket --cors-configuration file://cors.json
```

## Put Bucket Lifecycle Configuration

Sets lifecycle rules on a bucket. Supports both non-versioned and versioned buckets.

**Supported XML elements:**

- `ID`
- `Status`
- `Prefix`
- `Expiration`
- `AbortIncompleteMultipartUpload`

**Non-versioned bucket request** — uses `Expiration` with `Days`:

```xml
<LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Rule>
        <ID>id2</ID>
        <Filter>
            <Prefix>logs/</Prefix>
        </Filter>
        <Status>Enabled</Status>
        <Expiration>
            <Days>30</Days>
        </Expiration>
    </Rule>
</LifecycleConfiguration>
```

**Versioned bucket request** — uses `NoncurrentVersionExpiration` with `NoncurrentDays`:

```xml
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

## Put Bucket Policy

Applies a bucket access policy. Only verified users can update bucket policy — request KYC verification via [Portal Account Verifications](https://portal.telnyx.com/#/app/account/verifications).

To make objects publicly readable, create a local JSON file (e.g. `public_read_policy.json`):

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::<your-bucket-name>/*"
    }
  ]
}
```

Then apply it:

```
aws s3api put-bucket-policy --bucket pubreadbuc --policy file://public_read_policy.json
```

## Put Bucket Tagging

Applies a tag set to a bucket.

**Request**

```
PUT /versionedbucket?tagging=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
Content-Type: application/xml
X-Amz-Content-Sha256: beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3
X-Amz-Date: 20230927T182056Z
Authorization: AWS4-HMAC-SHA256 ...
Content-Length: 310
```

**Body**

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

## Put Bucket Versioning

Enables or suspends versioning on a bucket.

**Supported XML element:** `Status` (set to `Enabled` or `Suspended`)

**Request**

```
PUT /versionedbucket?versioning=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
Content-Type: application/xml
X-Amz-Content-Sha256: beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3
X-Amz-Date: 20230927T165559Z
Authorization: AWS4-HMAC-SHA256 ...
Content-Length: 167
```

**Body**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<VersioningConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <Status>Enabled</Status>
</VersioningConfiguration>
```

## Verification Requirements

The following operations require a verified (KYC) account:

- [Put Bucket ACL](put-bucket-acl.md)
- [Put Bucket Policy](put-bucket-policy.md)

To request verification, go to [Portal Account Verifications](https://portal.telnyx.com/#/app/account/verifications).
