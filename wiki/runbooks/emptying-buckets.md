---
title: Emptying Buckets
summary: When a bucket has more than 1000 objects, it's burdensome to empty it synchronously.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket/index
    content_hash: 1b957dfa6662d423f60b9d605ce5b39a8d42ef8d77122856d4da70150a3c8510
updated_at: 2026-04-10T00:00:00Z
---

# Emptying Buckets

When a bucket has more than 1000 objects, it's burdensome to empty it synchronously.

The best solution is to take advantage of lifecycle rules which asynchronously operate on destination bucket.

Here is a sample lifecycle rule

***

## Sample lifecycle rule

```json theme={null}
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

Name that file as `lifecycle.json` and you can apply that to the bucket you intend to empty ---

```json theme={null}
aws s3api put-bucket-lifecycle-configuration --bucket mybucketname --lifecycle-configuration file://lifecycle.json --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
```

You can verify that it's applied correctly the following way.

```json theme={null}
aws s3api get-bucket-lifecycle-configuration --bucket mybucketname --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
```

Check on your bucket after 24 hours to validate it's being cleared.
