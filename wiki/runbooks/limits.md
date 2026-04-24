---
title: Limits
summary: Safeguard Your Data with Telnyx Storage Unveiling Object Encryption Limits.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/limits/index
    content_hash: 198dfeafb716644425409c2aabcf4590b63def463a948a11bd1d1736e8cdaa49
updated_at: 2026-04-10T00:00:00Z
---

# Limits

Safeguard Your Data with Telnyx Storage Unveiling Object Encryption Limits. Learn How Telnyx's Object Encryption Feature Provides Secure Data Protection Within Defined Parameters. Explore the Perfect Balance Between Security and Convenience!

## General API limits

| Limit                                      | Value |
| ------------------------------------------ | ----- |
| Requests per second per account            | 500   |
| Requests per second per bucket             | 200   |
| Concurrent PUT or COPY requests per object | 10    |

> **Note:** These limits are subject to change. If you require higher throughput, please [contact support](https://support.telnyx.com) to discuss your use case.

## Specific limits

* Max count of buckets per account is 100
* Max size of single object upload via PUT request is 5 GB
* Max size of single part upload of a multi-part upload is 5 GB
* Min size of single part upload of a multi-part upload is 5 MiB, except for the final part
* Max count of parts of a multi-part upload is 10,000
* Max size of a completed multi-part upload is 5 TiB
* Max count of objects per bucket is 50 million


## Related Pages

- [Limits](../runbooks/limits-2.md)
- [Limits](../runbooks/limits-3.md)
