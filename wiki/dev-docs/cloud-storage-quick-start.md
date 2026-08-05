---
title: Cloud Storage Quick Start
summary: Telnyx Cloud Storage is an S3-compatible object storage service that can
  be accessed through Edge Function bindings, the AWS SDK, the AWS CLI, S3-compatible
  third-party tools, or the Telnyx Mission Control Portal. This page covers the available
  regions, the five onboarding paths, and a step-by-step AWS CLI walkthrough for creating
  buckets and uploading objects.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/quick-start/index
updated_at: 2026-08-05T13:39:37Z
---

# Cloud Storage Quick Start

Telnyx Cloud Storage is an S3-compatible object storage service that can be accessed through Edge Function bindings, the AWS SDK, the AWS CLI, S3-compatible third-party tools, or the Telnyx Mission Control Portal. This page covers the available regions, the five onboarding paths, and a step-by-step AWS CLI walkthrough for creating buckets and uploading objects.

## Overview

There are five ways to get started with Telnyx Cloud Storage:

1. [Cloud Storage Bindings](cloud-storage-bindings--part-1.md) — from inside a Telnyx Edge Function
2. AWS SDK
3. AWS CLI
4. S3-compatible third-party tools
5. Telnyx Mission Control Portal

## Available Regions

| Region | Endpoint |
| --- | --- |
| us-central-1 | us-central-1.telnyxcloudstorage.com |
| us-east-1 | us-east-1.telnyxcloudstorage.com |
| us-west-1 | us-west-1.telnyxcloudstorage.com |
| eu-central-1 | eu-central-1.telnyxcloudstorage.com |
| ap-southeast-1 | ap-southeast-1.telnyxcloudstorage.com |

Specify the region via the `--endpoint-url` flag in the AWS CLI or the equivalent SDK configuration. See [API Endpoints & Organization](api-endpoints-organization.md) for details on regional behavior.

Some features are currently available only in US and APAC regions, including presigned URLs, public buckets, and SSL certificates. EU buckets do not support these features. See the [compatibility matrix](supported-api-methods.md) for full details.

## Use a Cloud Storage Binding

Bind an existing bucket to a [Telnyx Edge Function](telnyx-edge-functions-overview.md) and read, write, and list objects through a pre-authenticated `env` binding — the runtime injects the credential, so your code holds no S3 keys. This is the fastest path if your code already runs on Telnyx Edge Compute. See [Use a bucket from an Edge Function](cloud-storage-bindings--part-1.md) to declare the binding and call `env.MY_BUCKET.get/put/head/delete/list`.

## Use the AWS SDK

Telnyx Cloud Storage is S3-compatible, so the AWS SDKs work against it. See the ready-to-run examples for [Node](https://developers.telnyx.com/docs/cloud-storage/sdk/node), [Python](https://developers.telnyx.com/docs/cloud-storage/sdk/python), [Java](https://developers.telnyx.com/docs/cloud-storage/sdk/java), [Go](https://developers.telnyx.com/docs/cloud-storage/sdk/golang), [Ruby](https://developers.telnyx.com/docs/cloud-storage/sdk/ruby), [PHP](https://developers.telnyx.com/docs/cloud-storage/sdk/php), [.NET](https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet), and [Elixir](https://developers.telnyx.com/docs/cloud-storage/sdk/elixir).

## Use the AWS CLI

### 1. Install AWS CLI locally

Follow the procedure in the [AWS CLI installation guide](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

Use a recent AWS CLI v2. The Cloud Storage endpoint accepts the AWS CLI's default checksums (CRC64NVME) on both `put-object` and `aws s3 cp` multipart uploads.

### 2. Configure CLI

- Inject your Telnyx [API key](https://portal.telnyx.com/#/api-keys) twice, once as access key and once as secret key.
- Leave the region as blank; regionality is specified via `--endpoint-url` as shown subsequently.

```
user@localhost ~ % aws configure --profile mytelnyxprofile 
AWS Access Key ID [None]: XXX
AWS Secret Access Key [None]: XXX
Default region name [None]: 
Default output format [None]: json
```

Validate the profile has been created successfully.

```
user@localhost ~ % aws configure list-profiles
mytelnyxprofile
```

### 3. Validate CLI configuration

Perform the following validation procedure to ensure everything is working as expected.

**Create 2 buckets**

Bucket names must be universally unique. Hence, a `BucketAlreadyExists` error is expected on first attempt.

```
user@localhost ~ % aws s3api create-bucket --bucket demo-bucket --profile mytelnyxprofile --endpoint-url https://us-east-1.telnyxcloudstorage.com
An error occurred (BucketAlreadyExists) when calling the CreateBucket operation: Unknown
user@localhost ~ % aws s3api create-bucket --bucket demo-bucket-n1 --profile mytelnyxprofile --endpoint-url https://us-east-1.telnyxcloudstorage.com
user@localhost ~ % aws s3api create-bucket --bucket demo-bucket-n2 --profile mytelnyxprofile --endpoint-url https://us-east-1.telnyxcloudstorage.com
```

**List buckets**

Verify the buckets were created successfully.

```
user@localhost ~ % aws s3api list-buckets --profile mytelnyxprofile --endpoint-url https://us-east-1.telnyxcloudstorage.com
{
    "Buckets": [
        {
            "Name": "demo-bucket-n1",
            "CreationDate": "2024-07-26T17:31:14.888000+00:00"
        },
        {
            "Name": "demo-bucket-n2",
            "CreationDate": "2024-07-26T17:31:25.225000+00:00"
        }
    ],
    "Owner": {
        "DisplayName": "XXX",
        "ID": "XXX"
    }
}
```

**Add objects to a bucket**

Upload some random objects.

```
user@localhost ~ % aws s3api put-object --key demo-obj-101 --body ~/Downloads/IMG_1752.mov --bucket demo-bucket-n1 --profile mytelnyxprofile --endpoint-url https://us-east-1.telnyxcloudstorage.com
{
    "ETag": "\"bc864c2bc4549d72abadb0a5d44ee788\""
}

user@localhost ~ % aws s3api put-object --key demo-obj-202 --body ~/Downloads/IMG_1753.mov --bucket demo-bucket-n1 --profile mytelnyxprofile --endpoint-url https://us-east-1.telnyxcloudstorage.com
{
    "ETag": "\"bc864c2bc4549d72babdb0a5d44ee988\""
}
```

**List objects**

Verify the objects were uploaded successfully.

```
user@localhost ~ % aws s3api list-objects-v2 --bucket demo-bucket-n1 --profile mytelnyxprofile --endpoint-url https://us-east-1.telnyxcloudstorage.com 
{
    "Contents": [
        {
            "Key": "demo-obj-101",
            "LastModified": "2024-07-26T17:34:52.428000+00:00",
            "ETag": "\"bc864c2bc4549d72abadb0a5d44ee788\"",
            "Size": 136994934,
            "StorageClass": "STANDARD"
        },
        {
            "Key": "demo-obj-202",
            "LastModified": "2024-07-26T17:36:31.799000+00:00",
            "ETag": "\"bc864c2bc4549d72babdb0a5d44ee988\"",
            "Size": 136994934,
            "StorageClass": "STANDARD"
        }
    ],
    "RequestCharged": null
}
```

## Use S3-Compatible Third-Party Tools

Many excellent tools exist to upload data at scale without any code. Configuration guides are available in the [Telnyx Storage support collection](https://support.telnyx.com/en/collections/3840515-telnyx-storage).

## Use the Telnyx Mission Control Portal

Follow the [Get started with Telnyx Storage inference guide](https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide).

## Read These Documentations

Some key differences exist between Telnyx Cloud Storage and AWS S3. It is advisable that they are reviewed and comprehended prior to putting Telnyx Cloud Storage into production.

- Understand [API Endpoints & Organization](api-endpoints-organization.md)
- Review [Supported API Methods](supported-api-methods.md)
- Heed the warning on [Presigned URLs](presigned-urls.md)
- Pay attention to [Billing](billing.md)
- Know the restrictions on policy and ACL in [Public Buckets](public-buckets.md)

## Additional Resources

- All available [AWS S3 CLI Commands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html)
