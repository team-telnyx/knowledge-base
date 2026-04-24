---
title: Storing call recordings
summary: Telnyx's Programmable Voice gives customers the ability to store the recordings on storage owned by them (AWS, GCS).
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/storing-call-recordings/index
    content_hash: e67e0e5326b682b22afa1dbfcdacd8a22de89d5de6faadbb7cf3b3e54ab256f7
updated_at: 2026-04-10T00:00:00Z
---

# Storing call recordings

Telnyx's Programmable Voice gives customers the ability to store the recordings on storage owned by them (AWS, GCS)

## Overview

This tutorial covers how to store your Telnyx call recordings in Amazon S3 or Google Cloud Storage.

Call recordings are automatically stored in S3 buckets owned by Telnyx, but users can opt to store recordings in their own S3 or GCS buckets instead.

## Telnyx’s S3 storage

The recordings for the calls are stored in the S3 buckets owned by Telnyx.

The link to them is shared in the webhook “call.recording.saved” when they are ready to download.

```json theme={null}
{
  "created_at": "2022-02-04T11:36:13.612978Z",
  "event_type": "recording_saved",
  "payload": {
    "call_control_id": "9977677e-85ae-11ec-826d-02420a0d7e70",
    "call_leg_id": "9977677e-85ae-11ec-826d-02420a0d7e70",
    "call_session_id": "99706bb8-85ae-11ec-885c-02420a0d7e70",
    "channels": "single",
    "client_state": null,
    "connection_id": "1684641123236054244",
    "end_time": "2022-02-04T11:36:12.788447Z",
    "format": "wav",
    "occurred_at": "2022-02-04T11:36:13.508869Z",
    "public_recording_urls": {},
    "recording_ended_at": "2022-02-04T11:36:12.788447Z",
    "recording_id": "10cd86ac-fef8-4765-b203-0f7511f9fc75",
    "recording_started_at": "2022-02-04T11:36:08.148619Z",
    "recording_urls": {
      "wav": "https://s3.amazonaws.com/telephony-recorder-prod/047e057e-cb46-4b11-bb31-37987e753ed7/2022-02-04/9977677e-85ae-11ec-826d-02420a0d7e70-1643974566.wav?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=xxx%2Faws4_request&X-Amz-Date=20220204T113613Z&X-Amz-Expires=600&X-Amz-SignedHeaders=host&X-Amz-Signature=xxx"
    },
    "start_time": "2022-02-04T11:36:08.148619Z"
  },
  "record_type": "event",
  "webhook_id": "a6854826-41ae-4781-b299-415a760663a0"
}
```

The link to the recording is active for 10 minutes.

## Using custom GCS storage

As an alternative, the recordings can be stored in a GCS bucket owned by the customer. To set this up, the following requests with user credentials to the storage need to be sent for every particular application:

```bash theme={null}
curl --location --request POST 'https://api.telnyx.com/v2/custom_storage_credentials/{call_control_application_id}' \
--header 'Authorization: Bearer xxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
	"backend": "gcs",
	"configuration": {
		"credentials": "JSON_WITH_CREDENTIALS",
		"bucket": "BUCKET_NAME"
	}
}'
```

The provided user must have permission to store the files in the bucket. The information on how to generate the credentials can be found in the GCS docs <a href="https://cloud.google.com/iam/docs/keys-create-delete#creating">here</a>.

The information on where the recording is stored will be sent in the webhook “call.recording.saved” as well.

```json theme={null}
{
  "call_control_id": "d9d877c6-8424-11ec-b0b1-02420a0d7e68",
  "call_leg_id": "d9d877c6-8424-11ec-b0b1-02420a0d7e68",
  "call_session_id": "d9d3ba60-8424-11ec-a0c2-02420a0d7e68",
  "channels": "single",
  "client_state": null,
  "connection_id": "1684641123236054244",
  "end_time": "2022-02-02T12:37:48.670332Z",
  "format": "wav",
  "public_recording_urls": {},
  "recording_ended_at": "2022-02-02T12:37:48.670332Z",
  "recording_id": "505f7da3-c50a-4e05-8234-758196993ee3",
  "recording_started_at": "2022-02-02T12:37:41.996407Z",
  "recording_urls": {
    "wav": "gs://tacrde12904/047e057e-cb46-4b11-bb31-37987e753ed7/2022-02-02/d9d877c6-8424-11ec-b0b1-02420a0d7e68-1643805460"
  },
  "start_time": "2022-02-02T12:37:41.996407Z"
}
```

## Using custom S3 storage

It is possible to use AWS S3 storage owned by the customer. In that case, the storage configuration can be provided in the following way:

```bash theme={null}
curl --location --request POST 'https://api.telnyx.com/v2/custom_storage_credentials/{call_control_application_id}' \
--header 'Authorization: Bearer xxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
	"backend": "s3",
	"configuration": {
		"bucket": "BUCKET_NAME",
    "region" : "REGION_NAME",
    "aws_access_key_id" :  "AWS_ACCESS_KEY_ID",
    "aws_secret_access_key" : "AWS_SECRET_ACCESS_KEY"
	}
}'
```

In that case, the webhook “call.recording.saved” will look like this:

```json theme={null}
{
  "call_control_id": "d9d877c6-8424-11ec-b0b1-02420a0d7e68",
  "call_leg_id": "d9d877c6-8424-11ec-b0b1-02420a0d7e68",
  "call_session_id": "d9d3ba60-8424-11ec-a0c2-02420a0d7e68",
  "channels": "single",
  "client_state": null,
  "connection_id": "1684641123236054244",
  "end_time": "2022-02-02T12:37:48.670332Z",
  "format": "wav",
  "public_recording_urls": {},
  "recording_ended_at": "2022-02-02T12:37:48.670332Z",
  "recording_id": "505f7da3-c50a-4e05-8234-758196993ee3",
  "recording_started_at": "2022-02-02T12:37:41.996407Z",
  "recording_urls": {
    "wav": "s3://tacrde12904/047e057e-cb46-4b11-bb31-37987e753ed7/2022-02-02/d9d877c6-8424-11ec-b0b1-02420a0d7e68-1643805460"
  },
  "start_time": "2022-02-02T12:37:41.996407Z"
}
```

## Using custom Microsoft Azure Blob Storage storage

The Microsoft Azure Blob Storage can be used for storing recordings too. In that case, the storage configuration can be provided in the following way:

```bash theme={null}
curl --location --request POST 'https://api.telnyx.com/v2/custom_storage_credentials/{call_control_application_id}' \
--header 'Authorization: Bearer xxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
	"backend": "azure",
	"configuration": {
		"bucket": "BUCKET_NAME",
    "account_name" :  "AZURE_ACCOUNT_NAME",
    "account_key" : "AZURE_ACCOUNT_KEY"
	}
}'
```

In that case, the webhook “call.recording.saved” will look like this:

```json theme={null}
{
  "call_control_id": "d9d877c6-8424-11ec-b0b1-02420a0d7e68",
  "call_leg_id": "d9d877c6-8424-11ec-b0b1-02420a0d7e68",
  "call_session_id": "d9d3ba60-8424-11ec-a0c2-02420a0d7e68",
  "channels": "single",
  "client_state": null,
  "connection_id": "1684641123236054244",
  "end_time": "2022-02-02T12:37:48.670332Z",
  "format": "wav",
  "public_recording_urls": {},
  "recording_ended_at": "2022-02-02T12:37:48.670332Z",
  "recording_id": "505f7da3-c50a-4e05-8234-758196993ee3",
  "recording_started_at": "2022-02-02T12:37:41.996407Z",
  "recording_urls": {
    "wav": "https://my-account.blob.core.windows.net/my-bucket/7ab0a016-479f-4ab1-beaf-87b1a7430a01/2023-12-05/d9d877c6-8424-11ec-b0b1-02420a0d7e68-1643805461"
  },
  "start_time": "2022-02-02T12:37:41.996407Z"
}
```

Please find more details see our [call recording API reference](https://developers.telnyx.com/api-reference/call-recordings/retrieve-a-call-recording).


## Related Pages

- [Recordings](../runbooks/recordings.md)
