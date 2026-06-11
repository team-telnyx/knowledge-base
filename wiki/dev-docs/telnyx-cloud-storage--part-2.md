---
title: Telnyx Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service that supports
  common bucket and object operations, AWS Signature Version 4 authentication (using
  a Telnyx API key), and offers both regular and AI-embedded storage tiers with usage-based
  billing across US and EU regions.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/head-object
  content_hash: d32708769642ca1db1336fd456d711fb222b3ccbcd6b261e364456998e8ed735
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-object-versions
  content_hash: e50a907003a37fa41150d767b84940e21c27dee474798a545b134a2248924ddc
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-objects
  content_hash: 827fa038125e1b5606387d61f1f1e81417213bf8754d18e29c87d2b7b97a0a26
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-acl
  content_hash: ea4352a64e3ce6e530ebf09595811da8041d128ae46966167449f842aff19984
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-tagging
  content_hash: c92c1155cd485a78986414879f8ccc0a4db98d74023f16802df2a545cc8a8499
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object/index
  content_hash: a37f16baa6af872c0589483f913902ecb90f52a712db50f5fcc06f5637077b49
- url: https://developers.telnyx.com/docs/cloud-storage/authentication
  content_hash: ff7b6266c6fc1d6ebe4847cad651f67de9a5b26a48fea51e529e384ade5a57b4
- url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility/index
  content_hash: 56bddefa880590ca53e93c8817c90419baa5166c0f9206568b702d689cac6aaf
- url: https://developers.telnyx.com/docs/cloud-storage/billing
  content_hash: bb0357a174fedeb9ff9ed4cd1aad275b87b88214ca18647daba8dd6849dcc897
- url: https://developers.telnyx.com/docs/cloud-storage/bucket-addressing
  content_hash: 46d7fbf3e433e1bb9a4d158172f241500cf57d8aee6f69498fba113385694aad
- url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket/index
  content_hash: fa40a29da2be02c25a1d2c770fa5a8cc542eaa8dad59b425ee7beeee107ce835
updated_at: 2026-06-11T10:24:11Z
---

# Telnyx Cloud Storage

*Part 2 of 2 — see also: [Part 1](telnyx-cloud-storage--part-1.md)*

Telnyx Cloud Storage is an S3-compatible object storage service that supports common bucket and object operations, AWS Signature Version 4 authentication (using a Telnyx API key), and offers both regular and AI-embedded storage tiers with usage-based billing across US and EU regions.

## Billing

You are billed on two dimensions: bytes stored and count of API operations invoked.

### Storage Billing

The minimum billable object size is 4 KiB. Each object is rounded up to the nearest 4 KiB. Metadata counts towards storage consumed.

**US Storage:** The first 10 GiB per month is free. Beyond that:
- Regular storage: **$0.006 per GiB per month**
- AI embedded storage: **$0.60 per GiB per month**

**EU Storage:** No free tier.
- Regular storage: **$0.025 per GiB per month**
- AI embedded storage: **$0.60 per GiB per month**

Bytes stored across all buckets are recorded hourly. Usage is calculated and debited from your balance at each whole clock hour. For example, if you upload 11 GiB of objects, at the next whole hour the billable usage is (11 GiB − 10 GiB) × ($0.006 / 30 days / 24 hrs), debited from your balance.

The free tier is not available if your available credit is negative.

### API Operations Billing

**US Storage:**

| Category | Applicable API Ops | Price |
|---|---|---|
| Class A | PUT, COPY, POST, LIST | First 1 Million/month free, then $0.50 per 1 Million |
| Class B | GET, SELECT, and all other requests | First 10 Million/month free, then $0.04 per 1 Million |

**EU Storage:**

| Category | Applicable API Ops | Price |
|---|---|---|
| State-change operations | PUT, COPY, POST, LIST | $5.00 per 1 Million |
| Read operations | GET, SELECT, and all other requests | $0.40 per 1 Million |

### Account Suspension and Data Loss

When your available credit becomes negative:
- You are notified via email of insufficient balance.
- Your data is still retained but API requests fail with a `UserSuspended` error.
- Access is restored when available credit becomes positive.
- If credit remains negative for 30 days, the account is abolished and all data is irreversibly purged.

### Usage Query APIs

Two companion APIs allow querying usage:

- **Bucket Snapshot** (`GET /v2/storage/buckets/{bucket}/usage/storage`) — returns a snapshot of bytes stored, number of objects, and a timestamp.
- **API Usage** (`GET /v2/storage/buckets/{bucket}/usage/api`) — returns API request statistics with optional time-range filters (`filter[start_time]`, `filter[end_time]`), broken down by operation category including bytes sent/received, total ops, and successful ops.

Both endpoints use Bearer token authentication against `api.telnyx.com`.

## Emptying a Bucket

When a bucket has more than 1,000 objects, emptying it synchronously is impractical. The recommended approach is to apply a lifecycle rule that asynchronously deletes all objects and versions.

**Sample lifecycle rule** (`lifecycle.json`):

```json
{
    "Rules": [
        {
            "ID": "delete_all_versions_and_delete_markers",
            "Status": "Enabled",
            "Filter": {
                "Prefix": ""
            },
            "NoncurrentVersionExpiration": {
                "NoncurrentDays": 1
            },
            "AbortIncompleteMultipartUpload": {
                "DaysAfterInitiation": 1
            },
            "Expiration": {
                "Days": 1
            }
        }
    ]
}
```

**Apply the rule:**

```bash
aws s3api put-bucket-lifecycle-configuration --bucket mybucketname --lifecycle-configuration file://lifecycle.json --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
```

**Verify it was applied:**

```bash
aws s3api get-bucket-lifecycle-configuration --bucket mybucketname --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
```

Check the bucket after 24 hours to confirm it is being cleared.
