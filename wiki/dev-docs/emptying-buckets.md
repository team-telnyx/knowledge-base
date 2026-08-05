---
title: Emptying Buckets
summary: Guidance on emptying a Telnyx cloud storage bucket that contains more than
  1000 objects by using an S3 lifecycle rule that asynchronously expires current and
  noncurrent versions and aborts incomplete multipart uploads.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket
updated_at: 2026-08-05T13:38:54Z
---

# Emptying Buckets

Guidance on emptying a Telnyx cloud storage bucket that contains more than 1000 objects by using an S3 lifecycle rule that asynchronously expires current and noncurrent versions and aborts incomplete multipart uploads.

## Overview

When a bucket has more than 1000 objects, emptying it synchronously becomes burdensome. The recommended approach is to use a lifecycle rule, which asynchronously operates on the destination bucket.

## Sample lifecycle rule

Save the following JSON as `lifecycle.json`:

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

The rule applies an empty prefix (matching every object), expires noncurrent versions after 1 day, aborts incomplete multipart uploads after 1 day, and expires current objects after 1 day.

## Applying the rule

Apply the lifecycle configuration to the target bucket using the AWS CLI:

```
aws s3api put-bucket-lifecycle-configuration --bucket mybucketname --lifecycle-configuration file://lifecycle.json --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
```

## Verifying the rule

Confirm the lifecycle configuration was applied correctly:

```
aws s3api get-bucket-lifecycle-configuration --bucket mybucketname --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
```

Check the bucket again after 24 hours to validate that it is being cleared.
