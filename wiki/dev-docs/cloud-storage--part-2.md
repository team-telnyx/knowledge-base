---
title: Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service available
  in four regions (us-central-1, us-east-1, us-west-1, eu-central-1). It can be accessed
  via the AWS S3 API, AWS SDKs, AWS CLI, third-party S3 tools, the Telnyx Mission
  Control Portal, or directly from inside a Telnyx Edge Function via a pre-authenticated
  binding. Authentication uses your Telnyx API key as the S3 credential. The service
  supports standard S3 operations (with some US-only features like presigned URLs,
  public buckets, object lock, and SSE-C encryption), usage-based billing with a US
  free tier, and a JSON companion API for usage queries, presigned URLs, SSL management,
  and AWS S3 migration.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints/index
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
- url: https://developers.telnyx.com/docs/cloud-storage/authentication
- url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility/index
- url: https://developers.telnyx.com/docs/cloud-storage/billing
- url: https://developers.telnyx.com/docs/cloud-storage/bindings/index
- url: https://developers.telnyx.com/docs/cloud-storage/bindings/reference
- url: https://developers.telnyx.com/docs/cloud-storage/bucket-addressing
- url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/limits/index
- url: https://developers.telnyx.com/docs/cloud-storage/lock-and-retention
- url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws
- url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/object-encryption
- url: https://developers.telnyx.com/docs/cloud-storage/overview/index
- url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks
- url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls
- url: https://developers.telnyx.com/docs/cloud-storage/public-buckets
- url: https://developers.telnyx.com/docs/cloud-storage/quick-start/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
- url: https://developers.telnyx.com/docs/cloud-storage/supported
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
updated_at: 2026-07-17T09:13:08Z
---

# Cloud Storage

*Part 2 of 5 — see also: [Part 1](cloud-storage--part-1.md), [Part 3](cloud-storage--part-3.md), [Part 4](cloud-storage--part-4.md), [Part 5](cloud-storage--part-5.md)*

Telnyx Cloud Storage is an S3-compatible object storage service available in four regions (us-central-1, us-east-1, us-west-1, eu-central-1). It can be accessed via the AWS S3 API, AWS SDKs, AWS CLI, third-party S3 tools, the Telnyx Mission Control Portal, or directly from inside a Telnyx Edge Function via a pre-authenticated binding. Authentication uses your Telnyx API key as the S3 credential. The service supports standard S3 operations (with some US-only features like presigned URLs, public buckets, object lock, and SSE-C encryption), usage-based billing with a US free tier, and a JSON companion API for usage queries, presigned URLs, SSL management, and AWS S3 migration.

## S3 API Reference

### Bucket Operations

#### CreateBucket

Supported headers: `x-amz-acl` (`private`, `public-read`). Supported XML element: `LocationConstraint`.

A bucket's location is inherited from the regional endpoint to which the `CreateBucket` request is sent. If `LocationConstraint` is specified in the request body, its value must match the location of the regional endpoint, otherwise an `InvalidLocationConstraint` error is returned.

Bucket names must follow domain name constraints:

- Must be unique
- Cannot be formatted as an IP address
- Can be between 3 and 63 characters long
- Must not contain uppercase characters or underscores
- Must start with a lowercase letter or number
- Can contain a dash (-)
- Must be a series of one or more labels separated by single periods; each label must start and end with a lowercase letter or number

Violations return an `InvalidBucketName` error.

#### DeleteBucket

```
DELETE /[bucket_name] HTTP/1.1
Host: [region].telnyxcloudstorage.com
```

#### DeleteBucketCors

Removes the CORS configuration from a bucket.

#### DeleteBucketLifecycle

```
DELETE /[bucket]?lifecycle=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
```

#### DeleteBucketPolicy

Removes the policy from a bucket.

#### DeleteBucketTagging

```
DELETE /[bucket]?tagging=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
```

#### GetBucketAcl

Returns the access control list for a bucket. Supported `x-amz-acl` values are `private` and `public-read`.

#### GetBucketCors

Returns the CORS configuration for a bucket.

#### GetBucketLifecycleConfiguration

Returns the lifecycle configuration for a bucket. Supported XML elements include `ID`, `Status`, `Prefix`, `Expiration`, `AbortIncompleteMultipartUpload`, and `NoncurrentVersionExpiration`.

#### GetBucketLocation

Returns the region in which the bucket is located.

#### GetBucketPolicy

Returns the policy of a bucket.

#### GetBucketPolicyStatus

Returns whether the bucket policy is public.

#### GetBucketTagging

Returns the tag set associated with a bucket.

#### GetBucketVersioning

Returns the versioning configuration for a bucket.

#### HeadBucket

Verifies that a bucket exists and is accessible. The response includes `x-rgw-bytes-used`, `x-rgw-object-count`, and quota headers.

#### ListBuckets

Returns a list of all buckets in the account.

#### PutBucketAcl

> **Warning:** Only verified users can update bucket policy. To request KYC on your account, go to [Portal Account Verifications](https://portal.telnyx.com/#/app/account/verifications).

Supported `x-amz-acl` values: `private`, `public-read`.

#### PutBucketCors

Sets the CORS configuration for a bucket.

#### PutBucketLifecycleConfiguration

Supported XML elements: `ID`, `Status`, `Prefix`, `Expiration`, `AbortIncompleteMultipartUpload`. Supports both non-versioned and versioned buckets (with `NoncurrentVersionExpiration`).

#### PutBucketPolicy

> **Warning:** Only verified users can update bucket policy. To request KYC on your account, go to [Portal Account Verifications](https://portal.telnyx.com/#/app/account/verifications).

#### PutBucketTagging

Sets tags on a bucket.

#### PutBucketVersioning

Supported XML element: `Status`.

### Object Operations

#### DeleteObject

```
DELETE /[bucket]/[object] HTTP/1.1
Host: [region].telnyxcloudstorage.com
```

#### DeleteObjects

Batch delete up to 1000 objects in a single call.

#### DeleteObjectTagging

Removes tags from an object.

#### GetObject

Supported headers: `If-Match`, `If-Modified-Since`, `If-None-Match`, `If-Unmodified-Since`, `Range`.

#### GetObjectAcl

Returns the access control list for an object.

#### GetObjectTagging

Returns the tag set associated with an object.

#### HeadObject

Supported headers: `If-Match`, `If-Modified-Since`, `If-None-Match`, `If-Unmodified-Since`, `Range`. Returns object metadata without the body.

#### ListObjects

Supported parameters: `prefix`, `delimiter`, `marker`, `max-keys`.

#### ListObjectVersions

Supported parameters: `prefix`, `delimiter`, `marker`, `max-keys`.

#### PutObject

Supported headers: `x-amz-acl` (`private`, `public-read`), `x-amz-storage-class` (`STANDARD`), `x-amz-meta-*`, `x-amz-server-side-encryption-customer-algorithm`, `x-amz-server-side-encryption-customer-key`, `x-amz-server-side-encryption-customer-key-MD5`.

#### PutObjectAcl

> **Warning:** Only verified users can update bucket policy. To request KYC on your account, go to [Portal Account Verifications](https://portal.telnyx.com/#/app/account/verifications).

Supported headers: `x-amz-acl` (`private`, `public-read`), `versionId`.

#### PutObjectTagging

Supported headers: `versionId`.

### Multipart Operations

#### AbortMultipartUpload

Supported parameters: `uploadId`.

#### CompleteMultipartUpload

Supported parameters: `uploadId`. Supported XML elements: `ETag`, `PartNumber`.

#### CreateMultipartUpload

Supported headers: `x-amz-acl` (`private`, `public-read`), `x-amz-storage-class` (`STANDARD`).

#### ListMultipartUploads

Supported parameters: `prefix`, `delimiter`, `key-marker`, `max-keys`, `max-uploads`, `upload-id-marker`.

#### ListParts

Supported parameters: `uploadId`, `max-parts`, `part-number-marker`.

#### UploadPart

Supported parameters: `partNumber`, `uploadId`.

## Multipart Upload

Large objects should be uploaded to your bucket via multipart upload.

### Using AWS CLI

```
aws s3 cp ~/Projects/s3-test/testdata/10Gfile s3://target-bucket/10Gfile --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
```

Depending on your environment, you may achieve throughput between 20 MiB/s (locally on a home network) to upward of 100+ MiB/s (on a lab or production network in a data center).

### Using AWS API/SDK

1. **CreateMultipartUpload** — initiate the upload session.
2. **UploadPart** — stream each chunk.
3. **CompleteMultipartUpload** — finalize the transfer.

## Presigned URLs

> This is currently supported only for buckets located in the US.

Telnyx does **not** follow how AWS does authentication — you **must not** use the existing AWS SDK or CLI to generate presigned URLs, otherwise you will expose your API key to the public. Use the [JSON companion API](/api-reference/presigned-object-urls/create-presigned-object-url) to generate ephemeral presigned URLs for anonymous **downloads** and **uploads** of objects.

Creating long-lived presigned URLs is a privileged action. Non-verified accounts are limited to presigned URLs with TTL no greater than 5 minutes. To verify your account, [request and obtain Level 2 verification](https://portal.telnyx.com/#/account/my-account/verifications) status.

### Examples

**Downloading an object:**

```
curl -o my-object.bin https://us-central-1.telnyxcloudstorage.com/my-bucket/my-object.bin\?X-AMZ-Security-Token\=8f0nh1jk8qvf
```

**Uploading an object:**

```
curl -X PUT -T a-new-object.bin https://us-central-1.telnyxcloudstorage.com/my-bucket/a-new-object.bin\?X-AMZ-Security-Token\=8f0nh1jk8qvf
```

If the object already exists, it will be overwritten.

## Object Encryption (SSE-C)

> This is currently supported only for buckets located in the US. On non-US buckets the SSE-C headers are silently ignored: the object is stored **unencrypted** and can be retrieved without the key.

Telnyx supports [SSE-C](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html).

```
aws s3api put-object --body /path/to/file.png --bucket mybestbucket --key objenc --sse-customer-algorithm AES256 --sse-customer-key XXX
```
