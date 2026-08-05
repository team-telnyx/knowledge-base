---
title: Cloud Storage Limits and Quotas
summary: Reference page describing the general API rate limits and specific object/bucket
  quotas that apply to Telnyx Cloud Storage.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/limits/index
updated_at: 2026-08-05T13:38:56Z
---

# Cloud Storage Limits and Quotas

Reference page describing the general API rate limits and specific object/bucket quotas that apply to Telnyx Cloud Storage.

## General API limits

| Limit | Value |
| --- | --- |
| Requests per second per account | 500 |
| Requests per second per bucket | 200 |
| Concurrent PUT or COPY requests per object | 10 |

These limits are subject to change. If you require higher throughput, please [contact support](https://support.telnyx.com) to discuss your use case.

## Specific limits

- Max count of buckets per account is 100
- Max size of single object upload via PUT request is 5 GB
- Max size of single part upload of a multi-part upload is 5 GB
- Min size of single part upload of a multi-part upload is 5 MiB, except for the final part
- Max count of parts of a multi-part upload is 10,000
- Max size of a completed multi-part upload is 5 TiB
- Max count of objects per bucket is 50 million
