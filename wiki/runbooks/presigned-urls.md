---
title: Presigned URLs
summary: 'Information on presigned URLs in Telnyx Cloud Storage including current restrictions and guidance on safe object sharing.'
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls/index
    content_hash: f1bf80fe3b7df4ce97760e24fbb4210d83174a475c3e0bfb82962c82a56b9849
updated_at: 2026-04-10T00:00:00Z
---

# Presigned URLs

Information on presigned URLs in Telnyx Cloud Storage: Current restrictions and guidance on safe object sharing practices.

<Callout type="info">
  This is currently supported only for buckets located in the US.

<Callout type="warning">
  We do NOT follow how AWS does authentication — hence, you *MUST NOT* use the existing AWS SDK or CLI to generate presigned URLs. Otherwise, you will expose your API key to the public.

Please use the [JSON companion API](https://developers.telnyx.com/api-reference/presigned-object-urls/create-presigned-object-url) to generate ephemeral presigned URLs to allow anonymous **downloads** and **uploads** of objects to your bucket(s).

In addition, creating long-lived presigned URL is a privileged action. Non-verified accounts are limited to presigned URLs with TTL no greater than 5 minutes.

To verify your account, [request and obtain Level 2 verification](https://portal.telnyx.com/#/account/my-account/verifications) status.

## Examples

Considering `8f0nh1jk8qvf` as an example of a presigned URL token, you can perform the following actions:

### Downloading an object using a presigned URL

```
curl -o my-object.bin https://us-central-1.telnyxcloudstorage.com/my-bucket/my-object.bin\?X-AMZ-Security-Token\=8f0nh1jk8qvf
```

### Uploading an object using a presigned URL

```
curl -X PUT -F "file=@a-new-object.bin" https://us-central-1.telnyxcloudstorage.com/my-bucket/a-new-object.bin\?X-AMZ-Security-Token\=8f0nh1jk8qvf
```

where `a-new-object.bin` is the file you want to upload in `my-bucket`. If the object already exists, it will be overwritten.
