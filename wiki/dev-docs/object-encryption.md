---
title: Object Encryption
summary: Telnyx Cloud Storage supports server-side encryption with customer-provided
  keys (SSE-C) for buckets in the US and APAC (ap-southeast-1) regions. On EU buckets,
  SSE-C headers are silently ignored and objects are stored unencrypted.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/object-encryption
updated_at: 2026-08-05T13:39:13Z
---

# Object Encryption

Telnyx Cloud Storage supports server-side encryption with customer-provided keys (SSE-C) for buckets in the US and APAC (ap-southeast-1) regions. On EU buckets, SSE-C headers are silently ignored and objects are stored unencrypted.

## Overview

Telnyx Cloud Storage supports [SSE-C](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html) (Server-Side Encryption with Customer-Provided Keys) for object encryption.

SSE-C is supported for buckets located in the **US** and **APAC (ap-southeast-1)** regions. On **EU** buckets, the SSE-C headers are silently ignored: the object is stored **unencrypted** and can be retrieved without the key.

## PutObject with SSE-C

When uploading an object with SSE-C, you must provide the customer key via the appropriate headers. Replace the placeholder value with your own key in the `--sse-customer-key` parameter.

```
user@host ~ % aws s3api put-object --body /path/to/file.png --bucket mybestbucket --key objenc --sse-customer-algorithm AES256 --sse-customer-key XXX
{
    "ETag": "\"18830c2cf6204ca111864bf967c40959\"",
    "SSECustomerAlgorithm": "AES256",
    "SSECustomerKeyMD5": "YYY"
}
```

The response includes the object's ETag along with the `SSECustomerAlgorithm` (AES256) and the `SSECustomerKeyMD5` fingerprint of the key that was used to encrypt the object.

## Regional Availability

| Region | SSE-C Support |
| --- | --- |
| US | Supported |
| APAC (ap-southeast-1) | Supported |
| EU | Not supported (headers ignored, objects stored unencrypted) |

> **Note:** Because EU buckets ignore SSE-C headers, do not rely on SSE-C to protect data stored in EU buckets. Choose a US or APAC bucket if you require server-side encryption with customer-provided keys.
