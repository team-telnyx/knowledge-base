---
title: Multipart Upload
summary: Large objects should be uploaded to your Telnyx Cloud Storage bucket via
  multipart upload. This page describes how to perform multipart uploads using the
  AWS CLI and the AWS API/SDK.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload/index
updated_at: 2026-08-05T13:39:08Z
---

# Multipart Upload

Large objects should be uploaded to your Telnyx Cloud Storage bucket via multipart upload. This page describes how to perform multipart uploads using the AWS CLI and the AWS API/SDK.

## Using AWS CLI

Assuming you have the AWS CLI set up already, you can copy a large file directly to a Telnyx Cloud Storage bucket:

```
user@localhost ~ % aws s3 cp ~/Projects/s3-test/testdata/10Gfile s3://target-bucket/10Gfile --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
```

where:

- `~/Projects/s3-test/testdata/10Gfile` is the path to the raw bytes stored locally
- `s3://target-bucket/10Gfile` is the target bucket name and the object key (aka object name)

Depending on your environment, you may achieve throughput between 20 MiB/s (locally on a home network) to upward of 100+ MiB/s (on a lab or production network in a data center).

## Using AWS API/SDK

The general procedure to use the API/SDK is as follows:

1. **CreateMultipartUpload** — Initiate the upload session with [CreateMultipartUpload](https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload/index#create-multipart-upload).
2. **UploadPart** — Stream each chunk with [UploadPart](https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part/index#upload-part).
3. **CompleteMultipartUpload** — Finalize the transfer by calling [CompleteMultipartUpload](https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload/index#complete-multipart-upload).
