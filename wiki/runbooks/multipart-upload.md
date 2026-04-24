---
title: Multipart Upload
summary: Large objects should be uploaded to your bucket via multipart upload.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload/index
    content_hash: 9e1a09619d28f0311660d9d7888672f7feeeb0bf77654db4bc0a1a794af143d0
updated_at: 2026-04-10T00:00:00Z
---

# Multipart Upload

Large objects should be uploaded to your bucket via multipart upload.

## Using AWS CLI

Assuming you have [AWS CLI set up](quick-start.md#using-aws-cli) already:

```
user@localhost ~ % aws s3 cp ~/Projects/s3-test/testdata/10Gfile s3://target-bucket/10Gfile --profile mytelnyxprofile --endpoint-url https://us-west-1.telnyxcloudstorage.com
```

where

* `~/Projects/s3-test/testdata/10Gfile` is the path to the raw bytes stored locally
* `s3://target-bucket/10Gfile` is the target bucket name and the object key (aka object name)

Depending on your environment, you may achieve throughput between 20 MiB/s (locally on a home network) to upward of 100+ MiB/s (on a lab or production network in a data center.)

## Using AWS API/SDK

The general procedure to use the API/SDK is as follows:

1. **CreateMultipartUpload**

    Initiate the upload session with [CreateMultipartUpload](https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload/index#create-multipart-upload).

2. **UploadPart**

    Stream each chunk with [UploadPart](https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part/index#upload-part).

3. **CompleteMultipartUpload**

    Finalize the transfer by calling [CompleteMultipartUpload](https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload/index#complete-multipart-upload).
