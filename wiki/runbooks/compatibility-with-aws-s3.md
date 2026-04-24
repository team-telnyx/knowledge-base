---
title: Compatibility with AWS S3
summary: Navigate AWS S3 compatibility in Telnyx Cloud Storage, focusing on supported headers and API methods.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility/index
    content_hash: 3c91b16406ed3e0324c3b1afd296e515184767dabc35ebe85c78b96be216d7a2
updated_at: 2026-04-10T00:00:00Z
---

# Compatibility with AWS S3

Navigate AWS S3 compatibility in Telnyx Cloud Storage, focusing on supported headers and API methods.

[This table](compatibility-matrix.md) documents all the supported S3 APIs. When an unsupported API method is invoked, an S3-compatible, XML-formated `NotImplemented` error response is returned.

For the ***supported*** API methods documented, not all of the AWS S3 parameters, headers, and body XML elements are supported.

## AWS S3 PutObject

For example, AWS S3 PutObject supports many headers. However, we only support what's documented under the [PutObject](https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object/index#put-object) section.

<Callout type="info">
  *They are unsupported by default unless otherwise explicitly specified.*

```json theme={null}
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


## Related Pages

- [Compatibility](../runbooks/compatibility.md)
- [Compatibility Matrix](../runbooks/compatibility-matrix.md)
