---
title: Migrating from S3
summary: The migration API moves all data from a source AWS S3 bucket to a destination Telnyx Storage bucket without the user incurring a data egress charge by AWS.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws/index
    content_hash: 95c6dcf0f7c97b6428d8b864dc60c7db2c4558b022bb4c1b6fce2067d8fdc126
updated_at: 2026-04-10T00:00:00Z
---

# Migrating from S3

The migration API moves all data from a source AWS S3 bucket to a destination Telnyx Storage bucket without the user incurring a data egress charge by AWS.

The [migration API](https://developers.telnyx.com/api-reference/data-migration/create-a-migration) moves all data from a source AWS S3 bucket to a destination Telnyx Storage bucket without the user incurring a data egress charge by AWS.

<Callout type="warning" title="Regional Availability">
  This is currently supported only for buckets located in the US.

## Feature

The owner of the AWS account does not get charged by AWS on data transfer to Telnyx when this API is employed.

## Achieving minimal costs

There are 3 components to this data pipeline:

1. **Source bucket**

    User’s AWS S3 bucket in AWS Region X.

2. **Migration engine**

    Telnyx’s migration engine in the same AWS Region X.

3. **Direct connect links**

    Telnyx’s direct connects with AWS used to transfer the data.

Cost minimization is achieved via the following billing practices by AWS.

<Callout type="warning" title="Intra-region data transfer">
  Intra-region data transfer between S3 and EC2, within the same account, or across different accounts, is free of charge.

<img alt="Intra-region-Data-Transfer-1" />

Source: [AWS S3 Pricing](https://aws.amazon.com/s3/pricing/?nc=sn\&loc=4)

<img alt="Intra-region-Data-Transfer-2" />

Source: [AWS S3 FAQ](https://aws.amazon.com/s3/faqs/?nc=sn\&loc=7)

Hence, depending on the region of the source AWS S3 bucket, the API will select the co-located migration engines to best take advantage of this billing practice.

<Callout type="warning" title="Transfer via AWS Direct Connect">
  Data Transfer Out (DTO) over AWS Direct Connect within the same geopolitical region is heavily discounted in comparison to DTO over the internet.

<img alt="Intra-region-Data-Transfer-3" />

Source: [AWS Direct Connect](https://aws.amazon.com/directconnect/pricing/?nc=sn\&loc=3)

Telnyx’s infrastructure is multi-cloud and multi-region with PoPs in multiple geopolitical regions. AWS Direct Connect is one of the components of that architecture. As a result, the migration API takes advantage of the discounted rate of DTO within the same geopolitical region to move data off AWS into Telnyx.

## AWS S3 vs Telnyx Storage Costs Revisited

Assume a user has the following pattern in us-east-2 Ohio.

<img alt="Intra-region-Data-Transfer-4" />

Ignoring API operations since those costs are marginal, this is their costs breakdown. In the Appendix, you can see these costs are corroborated by AWS Cost Calculator.

<img alt="Intra-region-Data-Transfer-5" />

With the migration API, data can be moved to Telnyx without egress charge from AWS. The post migration costs are as follows.

<img alt="Intra-region-Data-Transfer-6" />

<Callout type="warning" title="Important">
  We are offering this API free of charge to users in its beta stage.

  In the future, we will require minimum storage duration to offset the costs we incur with AWS for DTO over Direct Connect.

## API Concepts and Procedure

### Coverage

This API shows you the supported AWS S3 regions. Prior to using the API for migration,  ensure the AWS S3 bucket you want to migrate is among the supported regions.

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/storage/migration_source_coverage' \
--header 'Authorization: Bearer XXX'

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

<Callout type="warning" title="Important">
  Only standard class is supported. Restore data in glacier before attempting migration.

This API allows you to define the source bucket in AWS. In order to use this API, you need to provide it with a pair of AWS access key and secret access key. We advise you to create an IAM role with a Read Only user for this purpose.

```bash theme={null}
curl --location ‘https://api.telnyx.com/v2/storage/migration_sources’ \
--header ‘Content-Type: application/json’ \
--header ‘Authorization: Bearer XXX’ \
--data ‘{
  “provider”: “aws”,
  “provider_auth”: {
    “access_key”: “XXX”,
    “secret_access_key”: “XXX”
  },
  “bucket_name”: “source-west-bucket-demo”
}’

{
    “data”: {
        “id”: “48f215e7-8f16-4e65-aa31-9340d4a18745”,
        “provider”: “aws”,
        “provider_auth”: {
            “access_key”: “XXX”,
            “secret_access_key”: “XXXXXX”
        },
        “bucket_name”: “source-west-bucket-demo”,
        “source_region”: “us-west-1"
    }
}
```

The following errors might be possible —

4. **Bucket doesn’t exist**

    ```json theme={null}
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

5. **Bucket you don’t own**

    ```json theme={null}
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

6. **Bucket region not supported**

    ```json theme={null}
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

Lastly, you can create a migration. If the target bucket doesn’t exist, the API will attempt to create it for you. If the desired bucket name is not available or invalid, you will receive an error right away.

In addition, you do not have to match source bucket region to target bucket region; in other words, you can migrate data from an AWS source bucket in us-west-1 to Telnyx target bucket in us-east-1. You will not be charged for DTO by AWS as the API will use a migration engine in us-west-1.

When the refresh parameter is set to false, a one time migration will be created. Otherwise, the API will periodically synchronize the source and destination bucket.

```bash theme={null}
curl --location 'https://api.telnyx.com/v2/storage/migrations' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer XXX' \
--data '{
  "source_id": "1c73c8d9-d65a-4f61-ab41-afa095324c5d",
  "target_bucket_name": "target-bucket-test-account",
  "target_region": "us-west-1",
  "refresh": false
}'

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

You can periodically poll the API to see its status.

```bash theme={null}

curl --location 'https://api.telnyx.com/v2/storage/migrations/04532400-7d40-4862-8437-17937d48b405' \
--header 'Authorization: Bearer XXX'

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

Alternatively, check in on the metric of the target bucket. When it’s reached the expected size or all the objects appear in there, the migration is complete.

<img alt="Intra-region-Data-Transfer-7" />


## Related Pages

- [Migrate from Self-Hosted](../runbooks/migrate-from-self-hosted.md)
