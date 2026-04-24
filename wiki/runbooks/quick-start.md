---
title: Quick Start
summary: There are four ways to get started on Telnyx cloud storage.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/quick-start/index
    content_hash: ec58c77d3f78dbfab4a539f1e1d8d34577f1ce75496ea42dae0f64e15eec375a
updated_at: 2026-04-10T00:00:00Z
---

# Quick Start

There are four ways to get started on Telnyx cloud storage:

* [Telnyx Mission Control Portal](https://portal.telnyx.com/#/storage/buckets)
* AWS CLI
* AWS SDK
* S3 compatible [third party tools](https://support.telnyx.com/en/collections/3840515-telnyx-storage)

## Available Regions

| Region       | Endpoint                            |
| ------------ | ----------------------------------- |
| us-central-1 | us-central-1.telnyxcloudstorage.com |
| us-east-1    | us-east-1.telnyxcloudstorage.com    |
| us-west-1    | us-west-1.telnyxcloudstorage.com    |
| eu-central-1 | eu-central-1.telnyxcloudstorage.com |

Specify the region via the `--endpoint-url` flag in the AWS CLI or the equivalent SDK configuration. See [API Endpoints & Organization](api-endpoints-and-organization.md) for details on regional behavior.

> **Note:** Some features are currently US-only, including presigned URLs, public buckets, and SSL certificates. See the [compatibility matrix](compatibility-matrix.md) for full details.

## Option 1: Using Telnyx Mission Control Portal

Follow [this support article](https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide).

<warning>
  The Mission Control Portal is not the right tool to:

1. **Handle uploads larger than 200 MiB**

      Use the `aws s3 cp` CLI command or [multipart upload API](multipart-upload.md) for more concurrency, better reliability, and bigger throughput.

2. **Move 1000+ objects efficiently**

      Use one of the S3 compatible [third party tools](https://support.telnyx.com/en/collections/3840515-telnyx-storage) when moving large object counts.

</warning>

## Option 2: Using AWS CLI

3. **Install AWS CLI locally**

    Follow the procedure [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).

    <warning>
      Due to the latest AWS update, Telnyx Cloud Storage API is currently not compatible with CLI versions later than 2.22.35.
    </warning>

4. **Configure CLI**

    * Inject your Telnyx [API key](https://portal.telnyx.com/#/api-keys) twice, once as access key and once as secret key.
    * Leave the region as blank; regionality is specified via `--endpoint-url` as shown subsequently.

    ```json theme={null}
    user@localhost ~ % aws configure --profile mytelnyxprofile 
    AWS Access Key ID [None]: XXX
    AWS Secret Access Key [None]: XXX
    Default region name [None]: 
    Default output format [None]: json
    ```

    Validate the profile has been created successfully.

    ```json theme={null}
    user@localhost ~ % aws configure list-profiles
    mytelnyxprofile
    ```

5. **Validate CLI configuration**

    Perform the following validation procedure to ensure everything is working as expected.

    **Create 2 buckets**

    Bucket names must be universally unique. Hence, `BucketAlreadyExists` error is expected on first attempt.

    ```json theme={null}
    user@localhost ~ % aws s3api create-bucket --bucket demo-bucket --profile mytelnyxprofile --endpoint-url https://us-east-1.telnyxcloudstorage.com
    An error occurred (BucketAlreadyExists) when calling the CreateBucket operation: Unknown
    user@localhost ~ % aws s3api create-bucket --bucket demo-bucket-n1 --profile mytelnyxprofile --endpoint-url https://us-east-1.telnyxcloudstorage.com
    user@localhost ~ % aws s3api create-bucket --bucket demo-bucket-n2 --profile mytelnyxprofile --endpoint-url https://us-east-1.telnyxcloudstorage.com
    ```

    **List buckets**

    Verify the buckets were created successfully.

    ```json theme={null}
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

    ```json theme={null}
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

    ```json theme={null}
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

## Option 3: AWS SDK

Refer to this [collection of examples](aws-golang-sdk-example.md)

## Option 4: S3 compatible third party tools

Many excellent tools exist to upload data at scale without any code. You can find the configuration guides [here](https://support.telnyx.com/en/collections/3840515-telnyx-storage).

## Read these documentations

Some key differences exist between Telnyx cloud storage and AWS S3. It's advisable that they are reviewed and comprehended prior to Telnyx cloud storage is put into production.

* Understand [API endpoints & organizations](api-endpoints-and-organization.md)
* Review [supported API methods](compatibility-matrix.md)
* Heed the [warning on presigned URL](presigned-urls.md)
* Pay attention to [billing](billing.md)
* Know the [restrictions on policy and ACL](making-bucket-public.md)

## Additional Resources

* All available [AWS S3 CLI Commands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/index.html)


## Related Pages

- [Quick Start](../tutorial/quick-start.md)
- [Edge Compute Quick Start](../tutorial/edge-compute-quick-start.md)
- [Start](../runbooks/start.md)
