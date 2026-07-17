---
title: Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service available
  in four regions (us-central-1, us-east-1, us-west-1, eu-central-1). It can be accessed
  via the AWS S3 API, AWS SDKs, AWS CLI, third-party S3 tools, the Telnyx Mission
  Control Portal, or directly from inside a Telnyx Edge Function via a pre-authenticated
  binding. Authentication uses your Telnyx API key as the S3 credential. The service
  supports standard S3 operations (with some US-only features like presigned URLs,
  public buckets, object lock, and SSE-C encryption), usage-based billing with a US
  free tier, and a JSON companion API for usage queries, presigned URLs, SSL management,
  and AWS S3 migration.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/create-bucket/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-lifecycle
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-policy
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-lifecycle-configuration
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-location
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy-status
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-versioning
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/head-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/list-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-life-cycle-configuration
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-versioning
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/abort-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-multipart-uploads
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-parts
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-objects
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/head-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-object-versions
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-objects
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object/index
- url: https://developers.telnyx.com/docs/cloud-storage/authentication
- url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility/index
- url: https://developers.telnyx.com/docs/cloud-storage/billing
- url: https://developers.telnyx.com/docs/cloud-storage/bindings/index
- url: https://developers.telnyx.com/docs/cloud-storage/bindings/reference
- url: https://developers.telnyx.com/docs/cloud-storage/bucket-addressing
- url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/limits/index
- url: https://developers.telnyx.com/docs/cloud-storage/lock-and-retention
- url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws
- url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/object-encryption
- url: https://developers.telnyx.com/docs/cloud-storage/overview/index
- url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks
- url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls
- url: https://developers.telnyx.com/docs/cloud-storage/public-buckets
- url: https://developers.telnyx.com/docs/cloud-storage/quick-start/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
- url: https://developers.telnyx.com/docs/cloud-storage/supported
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
updated_at: 2026-07-17T09:13:08Z
---

# Cloud Storage

*Part 3 of 5 — see also: [Part 1](cloud-storage--part-1.md), [Part 2](cloud-storage--part-2.md), [Part 4](cloud-storage--part-4.md), [Part 5](cloud-storage--part-5.md)*

Telnyx Cloud Storage is an S3-compatible object storage service available in four regions (us-central-1, us-east-1, us-west-1, eu-central-1). It can be accessed via the AWS S3 API, AWS SDKs, AWS CLI, third-party S3 tools, the Telnyx Mission Control Portal, or directly from inside a Telnyx Edge Function via a pre-authenticated binding. Authentication uses your Telnyx API key as the S3 credential. The service supports standard S3 operations (with some US-only features like presigned URLs, public buckets, object lock, and SSE-C encryption), usage-based billing with a US free tier, and a JSON companion API for usage queries, presigned URLs, SSL management, and AWS S3 migration.

## Making a Bucket Public

> This is currently supported only for buckets located in the US.

Making a bucket public (via [policy](https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy/index#put-bucket-policy) or [ACL](https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl/index#put-bucket-acl)) is a privileged action:

1. **Verify your account** — request and obtain [Level 2 verification](https://portal.telnyx.com/#/account/my-account/verifications) status.
2. **Apply bucket policy or ACL** — use the CLI, API, or SDK to apply the desired policy to your bucket.

## HTTPS with Custom Domain

> This is currently supported only for buckets located in the US.

1. **Validate availability of bucket** — ensure the subdomain is available as a bucket name, then create the bucket.
2. **Make the bucket public** — apply a public read policy.
3. **Configure DNS** — set up an alias to the bucket with virtual addressing style.
4. **Upload certificate and matching key** — under SSL/TLS, upload the certificate and matching key. The bucket name must match one of the certificate SNIs exactly. If you have intermediate certificates, include them in the certificate file with the leaf certificate at the top. You may omit the root certificate.
5. **Test** — verify the image loads and the browser shows "Connection is secure" and "Certificate is valid".

## Object Lock & Retention

> This is currently supported only for buckets located in the US.

To enable this feature, object lock **must** be enabled at bucket creation time:

```
aws s3api create-bucket --bucket test-lock-v4 --object-lock-enabled-for-bucket --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com
```

Versioning is automatically enabled as a result. Upload an object, then set the object retention policy:

```
aws s3api put-object-retention --bucket test-lock-v4 --key my-object --retention '{ "Mode": "GOVERNANCE", "RetainUntilDate": "2024-11-20T00:00:00" }' --profile "*.telnyxcloudstorage.com" --endpoint-url https://us-central-1.telnyxcloudstorage.com
```

Deleting a locked object produces an `AccessDenied` error: `forbidden by object lock`.

## Emptying Buckets

When a bucket has more than 1000 objects, it's burdensome to empty it synchronously. The best solution is to use lifecycle rules which asynchronously operate on the destination bucket.

Sample lifecycle rule:

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

Apply it to the bucket:

```
aws s3api put-bucket-lifecycle-configuration --bucket mybucketname --lifecycle-configuration file://lifecycle.json --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
```

Check on your bucket after 24 hours to validate it's being cleared.

## Migrating from S3

> This is currently supported only for buckets located in the US.

The [migration API](/api-reference/data-migration/create-a-migration) moves all data from a source AWS S3 bucket to a destination Telnyx Storage bucket without the user incurring a data egress charge by AWS.

### Cost Minimization

The data pipeline has three components:

1. **Source bucket** — user's AWS S3 bucket in AWS Region X.
2. **Migration engine** — Telnyx's migration engine in the same AWS Region X.
3. **Direct connect links** — Telnyx's direct connects with AWS used to transfer the data.

Intra-region data transfer between S3 and EC2 (within the same account or across different accounts) is free of charge. Data Transfer Out (DTO) over AWS Direct Connect within the same geopolitical region is heavily discounted compared to DTO over the internet. The migration API takes advantage of these billing practices.

The migration API is offered free of charge during its beta stage. In the future, a minimum storage duration will be required to offset the costs incurred with AWS for DTO over Direct Connect.

### API Procedure

**Coverage** — check supported AWS S3 regions:

```
curl --location 'https://api.telnyx.com/v2/storage/migration_source_coverage' \
--header 'Authorization: Bearer XXX'
```

**Migration Sources** — define the source bucket in AWS. Only standard class is supported; restore data in glacier before attempting migration. Provide an AWS access key and secret access key (preferably from an IAM role with Read Only access):

```
curl --location 'https://api.telnyx.com/v2/storage/migration_sources' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer XXX' \
--data '{
  "provider": "aws",
  "provider_auth": {
    "access_key": "XXX",
    "secret_access_key": "XXX"
  },
  "bucket_name": "source-west-bucket-demo"
}'
```

**Migrations** — create a migration. If the target bucket doesn't exist, the API will attempt to create it. Source and target regions do not need to match. When `refresh` is `false`, a one-time migration is created; otherwise the API periodically synchronizes the source and destination bucket:

```
curl --location 'https://api.telnyx.com/v2/storage/migrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer XXX' \
--data '{
  "source_id": "1c73c8d9-d65a-4f61-ab41-afa095324c5d",
  "target_bucket_name": "target-bucket-test-account",
  "target_region": "us-west-1",
  "refresh": false
}'
```

**Checking Migration Progress** — periodically poll the API to see its status, or check the metric of the target bucket.

## Performance Benchmarks

Indicative throughput results from the benchmark test setup:

- **PutObject Aggregate: 2.029 GiB/s**
- **GetObject Aggregate: 2.714 GiB/s**

The benchmark used 8 bare metal client machines (4 with 64 CPUs / 2 TiB RAM / 4 × 6.4 TiB NVMe, and 4 with 32 CPUs / 2 TiB RAM / 1 × 960 GiB NVMe), each with 100 Gbps uplink, using the [wasabi-tech/s3-benchmark](https://github.com/wasabi-tech/s3-benchmark) tool. Each client reads and writes to its individual bucket.
