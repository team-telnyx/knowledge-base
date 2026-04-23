---
title: Object Encryption
summary: 'Implementing object encryption in Telnyx Cloud Storage using SSE-C with step-by-step guide for secure AWS API requests.'
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/object-encryption/index
    content_hash: 3dbcdd11703ef68dff06f0e3307b24b131c047c242d60bebf83f3a8ad4688740
updated_at: 2026-04-10T00:00:00Z
---

# Object Encryption

Implementing object encryption in Telnyx Cloud Storage using SSE-C: Step-by-step guide for secure AWS API requests.

<Callout type="info">
  This is currently supported only for buckets located in the US.

We support [SSE-C](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html).

Here is an example on how to `PutObject` with encryption.

## PutObject with SSE-C

<Callout type="info">
  *Don't forget to update `--sse-customer-key` here.*

```bash theme={null}
user@host ~ % aws s3api put-object --body /path/to/file.png --bucket mybestbucket --key objenc --sse-customer-algorithm AES256 --sse-customer-key XXX
{
    "ETag": "\"18830c2cf6204ca111864bf967c40959\"",
    "SSECustomerAlgorithm": "AES256",
    "SSECustomerKeyMD5": "YYY"
}
```


## Related Pages

- [Object Lock & Retention](../runbooks/object-lock-retention.md)
