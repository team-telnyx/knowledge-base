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

*Part 5 of 5 — see also: [Part 1](cloud-storage--part-1.md), [Part 2](cloud-storage--part-2.md), [Part 3](cloud-storage--part-3.md), [Part 4](cloud-storage--part-4.md)*

Telnyx Cloud Storage is an S3-compatible object storage service available in four regions (us-central-1, us-east-1, us-west-1, eu-central-1). It can be accessed via the AWS S3 API, AWS SDKs, AWS CLI, third-party S3 tools, the Telnyx Mission Control Portal, or directly from inside a Telnyx Edge Function via a pre-authenticated binding. Authentication uses your Telnyx API key as the S3 credential. The service supports standard S3 operations (with some US-only features like presigned URLs, public buckets, object lock, and SSE-C encryption), usage-based billing with a US free tier, and a JSON companion API for usage queries, presigned URLs, SSL management, and AWS S3 migration.

## SDK Examples

Telnyx Cloud Storage is S3-compatible, so the AWS SDKs work against it. The Telnyx API key is used as both the access key and secret key (the secret key can be left blank or duplicated).

### Node.js

Recent AWS SDK v3 versions work against Cloud Storage with default checksum settings. If you hit a checksum error on an older v3 release, set all checksum calculation and validation options to `WHEN_REQUIRED`.

```
const { S3Client, CreateBucketCommand, PutObjectCommand, ListObjectsCommand, GetObjectCommand } = require("@aws-sdk/client-s3");

const s3Client = new S3Client({
  endpoint: "https://us-central-1.telnyxcloudstorage.com",
  region: "us-central-1",
  credentials: {
    accessKeyId: telnyxApiKey,
    secretAccessKey: telnyxApiKey
  },
  forcePathStyle: true,
  requestChecksumCalculation: 'WHEN_REQUIRED',
  requestChecksumValidation: 'WHEN_REQUIRED',
  responseChecksumCalculation: 'WHEN_REQUIRED',
  responseChecksumValidation: 'WHEN_REQUIRED'
});
```

### Python

Recent boto3 versions (1.36+) work against Cloud Storage with default checksum settings. If you hit a checksum error, disable checksum calculation and verification:

```
from botocore.config import Config
import boto3

config = Config(
    request_checksum_calculation="when_required",
    response_checksum_validation="when_required",
)

client = boto3.client(
    "s3",
    endpoint_url="https://us-central-1.telnyxcloudstorage.com",
    aws_access_key_id=telnyx_api_key,
    aws_secret_access_key=telnyx_api_key,
    config=config
)
```

### Java

If you hit a checksum error with AWS SDK for Java v2 (2.30+), set request checksum calculation and response checksum validation to `WHEN_REQUIRED`:

```
S3Client s3 = S3Client.builder()
    .region(region)
    .endpointOverride(URI.create(telnyxUrl))
    .requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)
    .responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)
    .credentialsProvider(
        StaticCredentialsProvider.create(AwsBasicCredentials.create(telnyxApiKey, "does not matter")))
    .build();
```

### Go

```
cfg, err := config.LoadDefaultConfig(ctx,
    config.WithRegion(region),
    config.WithCredentialsProvider(aws.CredentialsProviderFunc(
        func(context.Context) (aws.Credentials, error) {
            return aws.Credentials{
                AccessKeyID:     telnyxAPIKey,
                SecretAccessKey: telnyxAPIKey,
            }, nil
        })),
    config.WithS3UseARNRegion(true),
    config.WithS3DisableExpressAuth(true),
    config.WithS3DisableMultiRegionAccessPoints(true),
)
cfg.BaseEndpoint = aws.String(endpoint)
```

### Ruby

```
resource = Aws::S3::Resource.new(
  region: "us-central-1",
  endpoint: "https://us-central-1.telnyxcloudstorage.com",
  access_key_id: telnyx_api_key,
  secret_access_key: "doesn't matter"
)
```

### PHP

```
$s3Client = new S3Client([
    'region'  => $region,
    'version' => 'latest',
    'endpoint' => $endpoint,
    'credentials' => [
        'key'    => $telnyxAPIKey,
        'secret' => $telnyxAPIKey,
    ],
    'use_path_style_endpoint' => true
]);
```

### .NET

> Chunk encoding is not supported by the Cloud Storage API. Set `putObjectRequest.UseChunkEncoding = false`.

```
var s3Config = new AmazonS3Config
{
   ServiceURL = $"https://{region}.telnyxcloudstorage.com",
   ForcePathStyle = true,
   SignatureVersion = "4",
};

var telnyxClient = new AmazonS3Client(
   new BasicAWSCredentials(apiKeyTelnyx, apiKeyTelnyx),
   s3Config
);
```

### Elixir

```
telnyx_storage_client =
    AWS.Client.create(
        System.fetch_env!("TELNYX_V2_API_KEY"),
        "",
        System.get_env("TELNYX_STORAGE_REGION", "us-east-1")
    )
    |> AWS.Client.put_endpoint(fn options -> "#{options.region}.telnyxcloudstorage.com" end)
```

## Third-Party S3 Compatible Applications

All S3 third-party tools, applications, clients, and libraries can be used to interact with Telnyx Cloud Storage, including popular applications like Cyberduck, S3 Browser, Wal-G, and many others. Visit the [Telnyx support page](https://support.telnyx.com/en/collections/3840515-telnyx-storage) for configuration guides.

## Quick Start

There are five ways to get started:

1. [Cloud Storage binding](use-a-bucket-from-an-edge-function.md) — from inside a Telnyx Edge Function
2. AWS SDK
3. AWS CLI
4. S3-compatible third-party tools
5. Telnyx Mission Control Portal

### Using the AWS CLI

1. **Install AWS CLI locally** — use a recent AWS CLI v2. The Cloud Storage endpoint accepts the AWS CLI's default checksums (CRC64NVME) on both `put-object` and `aws s3 cp` multipart uploads.
2. **Configure CLI** — inject your Telnyx API key twice (once as access key and once as secret key). Leave the region blank; regionality is specified via `--endpoint-url`.
3. **Validate CLI configuration** — create buckets, list buckets, add objects, and list objects to verify everything works.

### Key Differences from AWS S3

Before going to production, review:

- [Compatibility Matrix](compatibility-matrix.md) — which S3 operations are supported, by region
- [Authentication](authentication.md) — your Telnyx API key as the S3 credential
- [Presigned URLs](presigned-urls.md) — the Telnyx-specific way to generate them safely
- [Billing](billing.md) — storage and request pricing
- [Making a Bucket Public](making-a-bucket-public.md) — restrictions on policy and ACL
