---
title: Presigned URLs
summary: Presigned URLs provide time-limited, anonymous access to objects in Telnyx
  Cloud Storage buckets, enabling both downloads and uploads without exposing API
  keys. They are generated via the Telnyx JSON companion API rather than the AWS SDK
  or CLI, and are currently supported for buckets in the US and APAC (ap-southeast-1).
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls
updated_at: 2026-08-05T13:39:24Z
---

# Presigned URLs

Presigned URLs provide time-limited, anonymous access to objects in Telnyx Cloud Storage buckets, enabling both downloads and uploads without exposing API keys. They are generated via the Telnyx JSON companion API rather than the AWS SDK or CLI, and are currently supported for buckets in the US and APAC (ap-southeast-1).

## Overview

Presigned URLs grant ephemeral, anonymous access to objects stored in Telnyx Cloud Storage buckets. They allow clients to perform **downloads** and **uploads** of objects without needing to authenticate with an API key, making them useful for sharing files or accepting uploads from end users.

This feature is currently supported for buckets located in the **US** and **APAC (ap-southeast-1)** regions.

## Authentication and Security

Telnyx does **not** follow the same authentication model as AWS. As a result, you **must not** use the existing AWS SDK or CLI to generate presigned URLs — doing so would expose your API key to the public.

Instead, use the [Create Presigned Object URL](create-presigned-object-url.md) JSON companion API endpoint to generate ephemeral presigned URLs that allow anonymous downloads and uploads of objects in your bucket(s).

## Account Verification and TTL Limits

Creating long-lived presigned URLs is a privileged action. Non-verified accounts are limited to presigned URLs with a TTL no greater than **5 minutes**.

To remove this restriction, [request and obtain Level 2 verification](https://portal.telnyx.com/#/account/my-account/verifications) status.

## Examples

The following examples use `8f0nh1jk8qvf` as a sample presigned URL token.

### Downloading an object

```
curl -o my-object.bin https://us-central-1.telnyxcloudstorage.com/my-bucket/my-object.bin\?X-AMZ-Security-Token\=8f0nh1jk8qvf
```

### Uploading an object

```
curl -X PUT -T a-new-object.bin https://us-central-1.telnyxcloudstorage.com/my-bucket/a-new-object.bin\?X-AMZ-Security-Token\=8f0nh1jk8qvf
```

In the upload example, `a-new-object.bin` is the file being uploaded to `my-bucket`. If an object with the same key already exists, it will be overwritten.
