---
title: Object Lock & Retention
summary: Object Lock & Retention is a Telnyx Cloud Storage feature that enforces write-once-read-many
  (WORM) protection on objects. It is currently supported for buckets located in the
  US and APAC (ap-southeast-1) regions and must be enabled at bucket creation time.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/lock-and-retention
updated_at: 2026-08-05T13:39:04Z
---

# Object Lock & Retention

Object Lock & Retention is a Telnyx Cloud Storage feature that enforces write-once-read-many (WORM) protection on objects. It is currently supported for buckets located in the US and APAC (ap-southeast-1) regions and must be enabled at bucket creation time.

## Overview

Object Lock & Retention enforces write-once-read-many (WORM) protection on objects stored in Telnyx Cloud Storage. This feature is currently supported for buckets located in the US and APAC (ap-southeast-1) regions. To use Object Lock, it must be enabled at the time the bucket is created — it cannot be enabled on an existing bucket.

When Object Lock is enabled, versioning is automatically enabled on the bucket as well.

## Enabling Object Lock on a New Bucket

Create a bucket with Object Lock enabled using the AWS CLI:

```
aws s3api create-bucket --bucket test-lock-v4 --object-lock-enabled-for-bucket  --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com
```

Confirm the configuration is set correctly:

```
aws s3api get-object-lock-configuration --bucket test-lock-v4 --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com              
{
    "ObjectLockConfiguration": {
        "ObjectLockEnabled": "Enabled"
    }
}
```

Verify that versioning was automatically enabled as a result:

```
aws s3api get-bucket-versioning --bucket test-lock-v4 --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com
{
    "Status": "Enabled",
    "MFADelete": "Disabled"
}
```

## Uploading an Object

Upload an object to the locked bucket:

```
aws s3api put-object --key my-object --body ~/Downloads/random-bytes --bucket test-lock-v4 --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com 
{
    "ETag": "\"21074fc6c4a7aaee18b61bb235a9d372\"",
    "VersionId": "Z.gwUKVtPQx9bqbfD4VTxv3SraZdUlF"
}
```

## Setting an Object Retention Policy

Apply a retention policy to the uploaded object. The example below uses `GOVERNANCE` mode with a `RetainUntilDate`:

```
aws s3api put-object-retention --bucket test-lock-v4 --key my-object --retention '{ "Mode": "GOVERNANCE", "RetainUntilDate": "2024-11-20T00:00:00" }' --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com
```

Confirm the retention policy is set correctly:

```
aws s3api get-object-retention --bucket test-lock-v4 --key my-object --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com 
{
    "Retention": {
        "Mode": "GOVERNANCE",
        "RetainUntilDate": "2024-11-20T00:00:00+00:00"
    }
}
```

## Verifying Lock Enforcement

Attempting to delete a locked object produces the expected error:

```
aws s3api delete-object --bucket test-lock-v4 --key my-object --version-id "Z.gwUKVtPQx9bqbfD4VTxv3SraZdUlF" --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com
An error occurred (AccessDenied) when calling the DeleteObject operation: forbidden by object lock
```

## Additional Resources

For additional information, consult the [S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_Operations.html).
