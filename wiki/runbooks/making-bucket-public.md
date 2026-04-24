---
title: Making Bucket Public
summary: This is currently supported only for buckets located in the US.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/public-buckets/index
    content_hash: 9da916799999cc6a30eda8a373ed00ae1faccfe3718daffd49a13ece79613da5
updated_at: 2026-04-10T00:00:00Z
---

# Making Bucket Public

<Callout type="info">
  This is currently supported only for buckets located in the US.

Making a bucket public (via [policy](https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy/index#put-bucket-policy) or [ACL](https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl/index#put-bucket-acl)) is a privileged action.

Follow the following procedure:

1. **Verify your account**

    Request and obtain [Level 2 verification](https://portal.telnyx.com/#/account/my-account/verifications) status.

2. **Apply bucket policy or ACL**

    Use the [CLI](https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy/index#put-bucket-policy), API, or SDK to apply the desired policy to your bucket.
