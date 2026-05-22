---
title: Using AWS SDKs with Telnyx Cloud Storage (S3-Compatible)
summary: How to connect popular AWS SDKs (Node.js, Python, Java, Go, PHP, .NET, Ruby,
  Elixir) to Telnyx Cloud Storage. This guide highlights the required endpoint, credentials,
  path-style addressing, checksum and chunked-encoding settings, and how to generate
  and use Telnyx presigned URLs.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
updated_at: 2026-05-19T19:35:40Z
---

# Using AWS SDKs with Telnyx Cloud Storage (S3-Compatible)

How to connect popular AWS SDKs (Node.js, Python, Java, Go, PHP, .NET, Ruby, Elixir) to Telnyx Cloud Storage. This guide highlights the required endpoint, credentials, path-style addressing, checksum and chunked-encoding settings, and how to generate and use Telnyx presigned URLs.

## Overview and prerequisites
Telnyx Cloud Storage is S3-compatible. You can use AWS SDKs by pointing them at the Telnyx storage endpoint and authenticating with your Telnyx API key.

- Telnyx API key: use your Telnyx v2 API key.
- Region and endpoint: choose a Telnyx storage region (examples use us-central-1) and set the S3 endpoint to https://{region}.telnyxcloudstorage.com.
- Credentials: supply the Telnyx API key as the AWS access key; most SDKs either accept the same key as the secret or allow an empty/placeholder secret.
- Addressing: use path-style bucket addressing (not virtual-hosted style) in SDKs that expose this option.

## Required SDK settings across languages
To avoid incompatibilities, apply these settings where supported by your SDK/version:

- Endpoint and region
  - Set endpoint to https://{region}.telnyxcloudstorage.com and pick the same region in the client config.
- Authentication
  - Use Signature Version 4 (SigV4). Provide your Telnyx API key as the access key; the secret can be the same key or left blank depending on SDK.
- Path-style addressing
  - Enable “force path style” (a.k.a. use_path_style_endpoint) to avoid virtual-host routing issues.
- Checksums
  - Newer AWS SDKs may compute/validate checksums by default. Set checksum calculation/validation to WHEN_REQUIRED (or disable, per SDK) to prevent mismatches:
    - Node.js AWS SDK v3: set request/response checksum calculation and validation to WHEN_REQUIRED.
    - Python botocore/boto3 (v1.36+): set request_checksum_calculation and response_checksum_validation to "when_required" in botocore Config.
    - Java v2 (2.30+): set RequestChecksumCalculation/ResponseChecksumValidation to WHEN_REQUIRED.
- Chunked transfer encoding
  - Chunked (streaming) encoding is not supported by the Telnyx Cloud Storage API. For SDKs that can emit chunked uploads, disable it (for example, in .NET set PutObjectRequest.UseChunkEncoding = false).
- AWS-specific features
  - Disable Amazon-only features that aren’t applicable (e.g., express auth, multi-region access points) if your SDK exposes them.

## Language-specific notes
- Node.js (AWS SDK v3)
  - endpoint: https://us-central-1.telnyxcloudstorage.com
  - region: us-central-1
  - credentials: accessKeyId = telnyxApiKey, secretAccessKey = telnyxApiKey
  - forcePathStyle: true
  - checksum options: set all request/response calculation and validation to WHEN_REQUIRED.
- Python (boto3)
  - endpoint_url: https://us-central-1.telnyxcloudstorage.com
  - aws_access_key_id/aws_secret_access_key: use your Telnyx API key for both
  - botocore Config: request_checksum_calculation = "when_required", response_checksum_validation = "when_required"
- Java (AWS SDK v2)
  - endpointOverride: https://us-central-1.telnyxcloudstorage.com
  - credentialsProvider: StaticCredentialsProvider with AwsBasicCredentials(telnyxApiKey, "ignored")
  - For SDK 2.30+: set request/response checksum handling to WHEN_REQUIRED.
- Go (aws-sdk-go-v2)
  - cfg.BaseEndpoint = https://us-central-1.telnyxcloudstorage.com
  - Credentials provider returns access key = telnyxApiKey (secret can also be telnyxApiKey)
  - Common S3 options in examples: WithS3UseARNRegion(true), WithS3DisableExpressAuth(true), WithS3DisableMultiRegionAccessPoints(true)
- PHP (aws/aws-sdk-php)
  - endpoint: https://us-central-1.telnyxcloudstorage.com
  - credentials: key = telnyxApiKey, secret = telnyxApiKey
  - use_path_style_endpoint: true
- .NET (AWSSDK.S3)
  - ServiceURL: https://{region}.telnyxcloudstorage.com
  - ForcePathStyle: true, SignatureVersion: "4"
  - IMPORTANT: disable chunked encoding for uploads (PutObjectRequest.UseChunkEncoding = false)
- Ruby (aws-sdk-s3)
  - endpoint: https://us-central-1.telnyxcloudstorage.com
  - access_key_id = telnyxApiKey, secret_access_key can be a placeholder
  - Examples show creating buckets, uploading/downloading objects, and using Telnyx presigned URLs for both upload (PUT) and download (GET)
- Elixir (:aws)
  - Dependencies: :aws, :hackney
  - AWS.Client.create(telnyxApiKey, "", region) |> put_endpoint(fn o -> "#{o.region}.telnyxcloudstorage.com" end)
  - Use AWS.S3.* operations to create buckets, put/get/list objects

## Typical object storage workflow
- Create a bucket.
- Put objects into the bucket (single-part put or multipart as needed).
- List objects in a bucket (and optionally list buckets).
- Get/download objects by key.
- Optionally generate a presigned URL to allow time-limited access without exposing your API key.
- Clean up by deleting objects and buckets when finished.

## Presigned URLs via the Telnyx API
Use the Telnyx REST API to generate presigned URLs for a specific object key:

- Endpoint: POST https://api.telnyx.com/v2/storage/buckets/{bucket_name}/{object_key}/presigned_url
- Authorization: Bearer <your Telnyx v2 API key>
- Body: JSON with a TTL field (seconds), for example: { "ttl": 30 } (examples also use "TTL": 30). 
- Response: data.presigned_url (and may include token and expires_at). Use the presigned_url directly in HTTP clients.
- Usage:
  - Download with HTTP GET to the presigned URL.
  - Some examples demonstrate uploading with HTTP PUT to the presigned URL.

See [Presigned URLs](presigned-urls.md) for more details.

## Endpoint and region pattern
- Base endpoint pattern: https://{region}.telnyxcloudstorage.com
- Example region: us-central-1
- Ensure your SDK’s region matches the region in the endpoint you set.

## Troubleshooting checklist
- Signature or auth errors: confirm SigV4 is used and the Telnyx API key is provided as credentials.
- Checksum/CRC errors: set checksum calculation/validation to WHEN_REQUIRED (or disable per SDK guidance above).
- 400/411 upload errors: disable chunked transfer encoding on uploads (not supported by Telnyx Cloud Storage).
- Bucket/host resolution issues: enable path-style addressing (force path style / use_path_style_endpoint).
- Presigned URL fails: ensure you POST to the Telnyx API with a valid Bearer token and a TTL in seconds, then use the returned presigned URL directly with GET/PUT.

## Security considerations
- Never expose your Telnyx API key in client-side code. Use presigned URLs to delegate time-limited access.
- Keep TTLs short and scope presigned URLs to the minimal object and operation you need.
- Rotate API keys and remove unused buckets/objects regularly.
