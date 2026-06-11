---
title: 'Telnyx Cloud Storage: Addressing, Uploads, Security, and Public Access'
summary: How to address Telnyx S3-compatible buckets, upload large objects, share
  time-limited access, encrypt with customer keys, lock objects, make buckets public,
  serve over custom domains, and empty large buckets efficiently — with important
  regional availability notes.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/bucket-addressing
- url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket/index
- url: https://developers.telnyx.com/docs/cloud-storage/lock-and-retention
- url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/object-encryption
- url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls
- url: https://developers.telnyx.com/docs/cloud-storage/public-buckets
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
updated_at: 2026-05-19T15:58:39Z
---

# Telnyx Cloud Storage: Addressing, Uploads, Security, and Public Access

How to address Telnyx S3-compatible buckets, upload large objects, share time-limited access, encrypt with customer keys, lock objects, make buckets public, serve over custom domains, and empty large buckets efficiently — with important regional availability notes.

## Addressing buckets and objects
Use either addressing style (replace placeholders in brackets):

- Path-style: https://[region].telnyxcloudstorage.com/[bucket]/[object]
- Virtual-hosted-style: https://[bucket].[region].telnyxcloudstorage.com/[object]

Virtual-hosted-style is required when you front a bucket with your own domain (see HTTPS with a custom domain below).

## Presigned URLs (JSON companion API)
- Supported only for US buckets.
- Do not generate presigned URLs with AWS SDK/CLI — Telnyx authentication differs and doing so can leak your API key.
- Use the JSON companion API to mint short-lived tokens for anonymous downloads and uploads. Non-verified accounts are limited to presigned URLs with TTL ≤ 5 minutes; request Level 2 verification to extend limits.
- Examples (token shown as 8f0nh1jk8qvf):
  - Download:
    curl -o my-object.bin "https://us-central-1.telnyxcloudstorage.com/my-bucket/my-object.bin?X-AMZ-Security-Token=8f0nh1jk8qvf"
  - Upload (overwrites if the object exists):
    curl -X PUT -F "file=@a-new-object.bin" "https://us-central-1.telnyxcloudstorage.com/my-bucket/a-new-object.bin?X-AMZ-Security-Token=8f0nh1jk8qvf"
- API reference: https://developers.telnyx.com/api-reference/presigned-object-urls/create-presigned-object-url

## Multipart uploads for large objects
Large objects should be uploaded with multipart upload.

- Using AWS CLI (after you’ve configured it for Telnyx):
  aws s3 cp ~/path/to/largefile s3://target-bucket/largefile --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
- Typical throughput ranges from ~20 MiB/s on home networks to 100+ MiB/s in data-center environments.
- Using APIs/SDKs, follow the standard sequence:
  1) CreateMultipartUpload → 2) UploadPart (repeat per chunk) → 3) CompleteMultipartUpload
  - References:
    - CreateMultipartUpload: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload
    - UploadPart: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part
    - CompleteMultipartUpload: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload

## Customer-provided encryption keys (SSE-C)
- Supported only for US buckets.
- Telnyx supports S3 Server-Side Encryption with customer-provided keys (SSE-C, AES256) on PutObject.
- Example:
  aws s3api put-object --body /path/to/file.png --bucket mybestbucket --key objenc --sse-customer-algorithm AES256 --sse-customer-key <base64-key>
- Learn more (AWS docs): https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html

## Making a bucket public
- Supported only for US buckets.
- Public access (via bucket policy or ACL) is a privileged action and requires Level 2 verification: https://portal.telnyx.com/#/account/my-account/verifications
- After verification, apply a public-read policy or appropriate ACL using the CLI, API, or SDK.
  - Policy API reference: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy
  - ACL API reference: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl

## HTTPS with a custom domain
- Supported only for US buckets.
- End-to-end workflow:
  1) Validate the hostname you want to use is an available bucket name, then create the bucket with that exact name (e.g., asset.example.com).
  2) Make the bucket public (policy or ACL) so objects are readable.
  3) Configure DNS to alias your hostname to the bucket using virtual-hosted-style addressing.
  4) In the bucket’s SSL/TLS settings, upload the certificate and matching private key. Requirements:
     - The bucket name must exactly match one certificate SNI. A wildcard like *.example.com matches help.example.com but not example.com.
     - Include intermediate certificates in the file, with the leaf cert first. Root is optional but including it can improve acceptance.
  5) Test: load https://your-hostname/object.jpg and verify the object is served and the browser reports a valid, secure certificate.

## Object lock and retention
- Supported only for US buckets.
- Must be enabled when creating the bucket; it cannot be turned on later:
  aws s3api create-bucket --bucket my-locked-bucket --object-lock-enabled-for-bucket --profile mytelnyxprofile --endpoint-url https://us-central-1.telnyxcloudstorage.com
- Verify object lock is enabled (get-object-lock-configuration). Bucket versioning is automatically enabled as a result (get-bucket-versioning shows Status: Enabled).
- After uploading an object, set a retention policy. Example:
  aws s3api put-object-retention --bucket my-locked-bucket --key my-object --retention '{ "Mode": "GOVERNANCE", "RetainUntilDate": "2026-11-20T00:00:00" }' --profile mytelnyxprofile --endpoint-url https://us-central-1.telnyxcloudstorage.com
- Attempts to delete a retained version will fail with AccessDenied (forbidden by object lock).

## Emptying large buckets efficiently (lifecycle rules)
When a bucket holds more than ~1,000 objects, synchronous deletion is cumbersome. Use a lifecycle configuration to clear the bucket asynchronously:

- Configure rules that apply to all keys (Prefix "") and:
  - Expire current objects after 1 day
  - Delete noncurrent versions after 1 day
  - Abort incomplete multipart uploads after 1 day
- Apply and verify:
  - Put config:
    aws s3api put-bucket-lifecycle-configuration --bucket mybucket --lifecycle-configuration file://lifecycle.json --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
  - Get config:
    aws s3api get-bucket-lifecycle-configuration --bucket mybucket --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
- Allow about 24 hours for the lifecycle to clear the bucket.

## Regional availability notes
The following features are currently available only for buckets located in the US:
- Presigned URLs (JSON companion API)
- SSE-C object encryption
- Public buckets (policy/ACL)
- HTTPS with custom domain (SSL/TLS on buckets)
- Object lock & retention

## Related references
- [Cloud Storage Quick Start](cloud-storage-quick-start.md)
- [Cloud Storage authentication](cloud-storage-authentication.md)
- [Cloud Storage limits and quotas](cloud-storage-limits-and-quotas.md)
- [Compatibility with AWS S3](compatibility-with-aws-s3.md)
