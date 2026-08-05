---
title: Compatibility with AWS S3
summary: Telnyx Cloud Storage implements a subset of the AWS S3 API. Unsupported API
  methods return an S3-compatible XML `NotImplemented` error, and even supported methods
  only honor a documented subset of AWS S3 parameters, headers, and body XML elements.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility/index
updated_at: 2026-08-05T13:38:37Z
---

# Compatibility with AWS S3

Telnyx Cloud Storage implements a subset of the AWS S3 API. Unsupported API methods return an S3-compatible XML `NotImplemented` error, and even supported methods only honor a documented subset of AWS S3 parameters, headers, and body XML elements.

## Overview

Telnyx Cloud Storage is designed to be compatible with a subset of the AWS S3 API. The full list of supported API methods is documented in the [Supported S3 APIs](/docs/cloud-storage/supported) table. When an unsupported API method is invoked, the service returns an S3-compatible, XML-formatted `NotImplemented` error response.

For the API methods that are supported, not all of the AWS S3 parameters, headers, and body XML elements are honored. Any parameter, header, or body element that is not explicitly documented for a given operation is unsupported by default.

## Example: AWS S3 PutObject

The AWS S3 `PutObject` operation supports many request headers, but Telnyx Cloud Storage only supports the headers documented under the [PutObject](https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object/index#put-object) reference. The full set of headers that AWS S3 defines for `PutObject` — and which Telnyx therefore does not support unless explicitly listed in the Telnyx reference — is shown below.

```
PUT /Key+ HTTP/1.1
Host: Bucket.s3.amazonaws.com
x-amz-acl: ACL
Cache-Control: CacheControl
Content-Disposition: ContentDisposition
Content-Encoding: ContentEncoding
Content-Language: ContentLanguage
Content-Length: ContentLength
Content-MD5: ContentMD5
Content-Type: ContentType
x-amz-sdk-checksum-algorithm: ChecksumAlgorithm
x-amz-checksum-crc32: ChecksumCRC32
x-amz-checksum-crc32c: ChecksumCRC32C
x-amz-checksum-sha1: ChecksumSHA1
x-amz-checksum-sha256: ChecksumSHA256
Expires: Expires
x-amz-grant-full-control: GrantFullControl
x-amz-grant-read: GrantRead
x-amz-grant-read-acp: GrantReadACP
x-amz-grant-write-acp: GrantWriteACP
x-amz-server-side-encryption: ServerSideEncryption
x-amz-storage-class: StorageClass
x-amz-website-redirect-location: WebsiteRedirectLocation
x-amz-server-side-encryption-customer-algorithm: SSECustomerAlgorithm
x-amz-server-side-encryption-customer-key: SSECustomerKey
x-amz-server-side-encryption-customer-key-MD5: SSECustomerKeyMD5
x-amz-server-side-encryption-aws-kms-key-id: SSEKMSKeyId
x-amz-server-side-encryption-context: SSEKMSEncryptionContext
x-amz-server-side-encryption-bucket-key-enabled: BucketKeyEnabled
x-amz-request-payer: RequestPayer
x-amz-tagging: Tagging
x-amz-object-lock-mode: ObjectLockMode
x-amz-object-lock-retain-until-date: ObjectLockRetainUntilDate
x-amz-object-lock-legal-hold: ObjectLockLegalHoldStatus
x-amz-expected-bucket-owner: ExpectedBucketOwner

Body
```

## See also

- [Supported S3 APIs](supported-s3-apis.md)
- [PutObject API reference](https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object/index#put-object)
