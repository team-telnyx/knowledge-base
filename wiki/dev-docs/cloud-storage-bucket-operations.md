---
title: Cloud Storage Bucket Operations
summary: Reference for Telnyx Cloud Storage bucket-level API operations, which are
  S3-compatible and authenticated via AWS4-HMAC-SHA256. Covers read operations (ListBuckets,
  HeadBucket, GetBucketPolicyStatus, GetBucketTagging, GetBucketVersioning) and write
  operations (PutBucketAcl, PutBucketCors, PutBucketLifecycleConfiguration, PutBucketPolicy,
  PutBucketTagging, PutBucketVersioning).
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy-status
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-versioning
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/head-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/list-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-life-cycle-configuration
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-versioning
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
