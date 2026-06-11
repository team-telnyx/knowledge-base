---
title: Telnyx Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service that supports
  standard AWS SDKs and third-party S3 tools. This page covers SDK integration, supported
  API operations, SSL certificate configuration, and third-party compatibility.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
  content_hash: 557f66728d24bc407e8e5a23df3fb036191a9547a66935915e658730f22b1943
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
  content_hash: a03b4e1572b7b695ac821993afc55add9dbbb3eb679c19c085d9a2fc9da4ab4c
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
  content_hash: 6da5801c698f795bde27af7770adc427d7f496ed6eda5853b5afdec508302d58
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
  content_hash: 1b2ff4d4d7fd27ad2f7fb2d016d22a8d20d482a161670708923cde4ee797f05f
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
  content_hash: bef5c483f31f5b02559d529398af82e64b310db6369c65644f435be2b5561e91
- url: https://developers.telnyx.com/docs/cloud-storage/supported
  content_hash: fc00383afc647bc1000db8bb56c40a035c44dfbe0983aa9667aa26ae4afe69f4
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
  content_hash: f13747eb826c99839d3a3c677d09530be46a09b92f4b842a952fc180a8d0a78a
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
