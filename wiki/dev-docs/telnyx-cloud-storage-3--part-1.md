---
title: Telnyx Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service that supports
  standard AWS SDKs and third-party S3 tools. This page covers SDK integration, supported
  API operations, SSL certificate configuration, and third-party compatibility.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
- url: https://developers.telnyx.com/docs/cloud-storage/supported
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
updated_at: 2026-06-11T10:25:44Z
---

# Telnyx Cloud Storage

*Part 1 of 3 — see also: [Part 2](telnyx-cloud-storage-3--part-2.md), [Part 3](telnyx-cloud-storage-3--part-3.md)*

Telnyx Cloud Storage is an S3-compatible object storage service that supports standard AWS SDKs and third-party S3 tools. This page covers SDK integration, supported API operations, SSL certificate configuration, and third-party compatibility.

## SDK Configuration

Telnyx Cloud Storage uses the S3 API, so you can connect with any AWS SDK by pointing it at the Telnyx endpoint. The common configuration details across all SDKs are:

- **Endpoint:** `https://us-central-1.telnyxcloudstorage.com`
- **Region:** `us-central-1`
- **Credentials:** Set both `accessKeyId` and `secretAccessKey` to your Telnyx API key (from the `TELNYX_API_KEY` environment variable).
- **Path-style addressing:** Always enable path-style endpoints (e.g., `forcePathStyle: true` in Node.js, `use_path_style_endpoint: true` in PHP).

### Checksum Handling

AWS SDK v3 for Node.js and recent versions of the Python SDK (boto3/botocore 1.36+) compute checksums by default, which can cause compatibility issues. Configure them as follows:

- **Node.js (AWS SDK v3):** Set all checksum calculation and validation options to `WHEN_REQUIRED` on the `S3Client`.
- **Python (boto3 1.36+):** Pass a `botocore.config.Config` with `request_checksum_calculation="when_required"` and `response_checksum_validation="when_required"`.

### Ruby SDK Note

In the Ruby SDK, the `secret_access_key` value is required by the SDK but is not validated by Telnyx — any non-empty string works.

## Presigned URLs

Presigned URLs are generated through the Telnyx REST API rather than the S3 API. Send a `POST` request to:

```
https://api.telnyx.com/v2/storage/buckets/{bucket_name}/{object_key}/presigned_url
```

Include a JSON body with a `TTL` field (in seconds) and an `Authorization: Bearer {TELNYX_API_KEY}` header. The response contains `data.presigned_url`, which can be used for both uploads and downloads.
