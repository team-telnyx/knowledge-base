---
title: Object Lock & Retention
summary: This is currently supported only for buckets located in the US.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/lock-and-retention/index
    content_hash: a339d1c8088ade9e130f66091b60cabcf9c6ff4af38d49b964c09779003a4453
updated_at: 2026-04-10T00:00:00Z
---

# Object Lock & Retention

<Callout type="info">
  This is currently supported only for buckets located in the US.

To enable this feature, object lock MUST be enabled at bucket creation time.

```bash theme={null}
aws s3api create-bucket --bucket test-lock-v4 --object-lock-enabled-for-bucket  --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com
```

Confirm this is set properly.

```bash theme={null}
aws s3api get-object-lock-configuration --bucket test-lock-v4 --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com              
{
    "ObjectLockConfiguration": {
        "ObjectLockEnabled": "Enabled"
    }
}
```

Versioning is automatically enabled as a result.

```bash theme={null}
s3-test % aws s3api get-bucket-versioning --bucket test-lock-v4 --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com
{
    "Status": "Enabled",
    "MFADelete": "Disabled"
}
```

Upload an object.

```bash theme={null}
aws s3api put-object --key my-object --body ~/Downloads/random-bytes --bucket test-lock-v4 --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com 
{
    "ETag": "\"21074fc6c4a7aaee18b61bb235a9d372\"",
    "VersionId": "Z.gwUKVtPQx9bqbfD4VTxv3SraZdUlF"
}
```

Now set the object retention policy.

```bash theme={null}
aws s3api put-object-retention --bucket test-lock-v4 --key my-object --retention '{ "Mode": "GOVERNANCE", "RetainUntilDate": "2024-11-20T00:00:00" }' --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com
```

And confirm it's set properly.

```bash theme={null}
aws s3api get-object-retention --bucket test-lock-v4 --key my-object --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com 
{
    "Retention": {
        "Mode": "GOVERNANCE",
        "RetainUntilDate": "2024-11-20T00:00:00+00:00"
    }
}
```

Deleting the object produces an expected error.

```bash theme={null}
aws s3api delete-object --bucket test-lock-v4 --key my-object --version-id "Z.gwUKVtPQx9bqbfD4VTxv3SraZdUlF" --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com
An error occurred (AccessDenied) when calling the DeleteObject operation: forbidden by object lock
```

For additional information, please consult S3's API reference.


## Related Pages

- [Object Encryption](../runbooks/object-encryption.md)
