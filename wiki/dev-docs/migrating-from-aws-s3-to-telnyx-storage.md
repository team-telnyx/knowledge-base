---
title: Migrating from AWS S3 to Telnyx Storage
summary: The Telnyx migration API moves all data from a source AWS S3 bucket to a
  destination Telnyx Storage bucket without the user incurring AWS data egress charges.
  It is currently supported for buckets located in the US and APAC (ap-southeast-1)
  regions.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws
updated_at: 2026-08-05T13:39:15Z
---

# Migrating from AWS S3 to Telnyx Storage

The Telnyx migration API moves all data from a source AWS S3 bucket to a destination Telnyx Storage bucket without the user incurring AWS data egress charges. It is currently supported for buckets located in the US and APAC (ap-southeast-1) regions.

## Overview

The [migration API](https://developers.telnyx.com/api-reference/data-migration/create-a-migration) moves all data from a source AWS S3 bucket to a destination Telnyx Storage bucket without the user incurring a data egress charge by AWS. This is currently supported for buckets located in the US and APAC (ap-southeast-1).

## Feature

The owner of the AWS account does not get charged by AWS on data transfer to Telnyx when this migration API is employed.

## Achieving Minimal Costs

There are three components to this data pipeline:

1. **Source bucket** — the user's AWS S3 bucket in AWS Region X.
2. **Migration engine** — Telnyx's migration engine in the same AWS Region X.
3. **Direct connect links** — Telnyx's direct connects with AWS used to transfer the data.

Cost minimization is achieved via the following AWS billing practices:

- Intra-region data transfer between S3 and EC2, within the same account or across different accounts, is free of charge. See [AWS S3 Pricing](https://aws.amazon.com/s3/pricing/?nc=sn&loc=4) and the [AWS S3 FAQ](https://aws.amazon.com/s3/faqs/?nc=sn&loc=7) for details.
- Data Transfer Out (DTO) over AWS Direct Connect within the same geopolitical region is heavily discounted in comparison to DTO over the internet. See [AWS Direct Connect pricing](https://aws.amazon.com/directconnect/pricing/?nc=sn&loc=3).

Depending on the region of the source AWS S3 bucket, the API selects the co-located migration engines to best take advantage of these billing practices. Telnyx's infrastructure is multi-cloud and multi-region with PoPs in multiple geopolitical regions, and AWS Direct Connect is one of the components of that architecture. As a result, the migration API takes advantage of the discounted rate of DTO within the same geopolitical region to move data off AWS into Telnyx.

## AWS S3 vs Telnyx Storage Costs Revisited

Assuming a user has a typical storage pattern in `us-east-2` (Ohio), the cost breakdown (ignoring marginal API operation costs) shows the on-AWS expense. With the migration API, data can be moved to Telnyx without an egress charge from AWS, and the post-migration costs are reduced accordingly.

The migration API is offered free of charge to users during its beta stage. In the future, a minimum storage duration will be required to offset the costs Telnyx incurs with AWS for DTO over Direct Connect.

## API Concepts and Procedure

### Coverage

Before using the API for migration, ensure the AWS S3 bucket you want to migrate is among the supported regions. Query the coverage endpoint to list them:

```
curl --location 'https://api.telnyx.com/v2/storage/migration_source_coverage' \
--header 'Authorization: Bearer XXX'
```

Example response:

```
{
    "data": [
        {
            "provider": "aws",
            "source_region": "us-west-1"
        },
        {
            "provider": "aws",
            "source_region": "us-east-1"
        },
        {
            "provider": "aws",
            "source_region": "us-east-2"
        }
    ]
}
```

### Migration Sources

Only the standard storage class is supported. Restore data in Glacier before attempting migration.

This endpoint defines the source bucket in AWS. You must provide a pair of AWS access key and secret access key. It is recommended to create an IAM role with a Read Only user for this purpose.

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

Example response:

```
{
    "data": {
        "id": "48f215e7-8f16-4e65-aa31-9340d4a18745",
        "provider": "aws",
        "provider_auth": {
            "access_key": "XXX",
            "secret_access_key": "XXXXXX"
        },
        "bucket_name": "source-west-bucket-demo",
        "source_region": "us-west-1"
    }
}
```

Possible errors include:

- **Bucket doesn't exist**

```
{
    "errors": [
        {
            "code": "15005",
            "title": "Bucket does not exist",
            "detail": "Bucket does not exist."
        }
    ]
}
```

- **Bucket you don't own**

```
{
    "errors": [
        {
            "code": "15025",
            "title": "Access denied",
            "detail": "Access denied reading migration source bucket."
        }
    ]
}
```

- **Bucket region not supported**

```
{
    "errors": [
        {
            "code": "15003",
            "title": "Bucket region invalid",
            "detail": "You have provided an invalid bucket region."
        }
    ]
}
```

### Migrations

Create a migration by referencing the source ID returned from the previous step. If the target bucket doesn't exist, the API will attempt to create it for you. If the desired bucket name is not available or invalid, you will receive an error right away.

You do not have to match the source bucket region to the target bucket region — for example, you can migrate data from an AWS source bucket in `us-west-1` to a Telnyx target bucket in `us-east-1`. You will not be charged for DTO by AWS because the API will use a migration engine in `us-west-1`.

When the `refresh` parameter is set to `false`, a one-time migration is created. Otherwise, the API will periodically synchronize the source and destination bucket.

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

Example response:

```
{
    "data": {
        "id": "04532400-7d40-4862-8437-17937d48b405",
        "source_id": "1c73c8d9-d65a-4f61-ab41-afa095324c5d",
        "target_bucket_name": "target-bucket-test-account",
        "target_region": "us-west-1",
        "refresh": false,
        "last_copy": "0001-01-01T00:00:00Z",
        "status": "pending",
        "bytes_to_migrate": 0,
        "bytes_migrated": 0,
        "speed": 0,
        "eta": "2024-05-10T20:47:33.821604511Z",
        "created_at": "2024-05-10T20:47:33.756241Z"
    }
}
```

### Checking Migration Progress

You can periodically poll the migration endpoint to see its status:

```
curl --location 'https://api.telnyx.com/v2/storage/migrations/04532400-7d40-4862-8437-17937d48b405' \
--header 'Authorization: Bearer XXX'
```

Example response:

```
{
    "data": {
        "id": "04532400-7d40-4862-8437-17937d48b405",
        "source_id": "1c73c8d9-d65a-4f61-ab41-afa095324c5d",
        "target_bucket_name": "target-bucket-test-account",
        "target_region": "us-west-1",
        "refresh": false,
        "last_copy": "2024-05-10T21:07:27.43006Z",
        "status": "complete",
        "bytes_to_migrate": 10485760000,
        "bytes_migrated": 10485760000,
        "speed": 7226700,
        "eta": "0001-01-01T00:00:00Z",
        "created_at": "2024-05-10T20:47:33.756241Z"
    }
}
```

Alternatively, check the metric of the target bucket. When it has reached the expected size or all the objects appear in there, the migration is complete.
