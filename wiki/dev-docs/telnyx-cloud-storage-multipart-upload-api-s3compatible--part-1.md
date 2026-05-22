---
title: 'Telnyx Cloud Storage: Multipart Upload API (S3‑Compatible)'
summary: How to perform S3‑compatible multipart uploads with Telnyx Cloud Storage,
  including creating an upload, uploading parts, listing uploads and parts, completing
  the upload, and aborting it. This page summarizes supported headers/parameters and
  provides sample HTTP and XML payloads.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/abort-multipart-upload
  content_hash: 76eb089d9ce3fd93434c3048cfed4e7d8173229d9ab04e4931891d9916ded986
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload/index
  content_hash: 7d6698408db0dd9aa3c32db1d92b270643d37482eb3152b4501519e78da00fea
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload/index
  content_hash: edbb9fe698b9dff9fe30625edf2585fc404089488f3a791bb55a2efcd4d5ea3c
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-multipart-uploads
  content_hash: 72b59313eb749f92336b450a378b4b3b9aa1433299575f9be0b62fba37b623f8
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-parts
  content_hash: cb6ce45c0f72d7c961dd29cac3afb4dc81cfeb48858669f0a7f4fe7c25c0949a
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part/index
  content_hash: deb426c4d4f0e3e4985c76c64c0635da7b67fbffff48540d980177aebd75871d
updated_at: 2026-05-19T19:34:26Z
---

# Telnyx Cloud Storage: Multipart Upload API (S3‑Compatible)

*Part 1 of 2 — see also: [Part 2](telnyx-cloud-storage-multipart-upload-api-s3compatible--part-2.md)*

How to perform S3‑compatible multipart uploads with Telnyx Cloud Storage, including creating an upload, uploading parts, listing uploads and parts, completing the upload, and aborting it. This page summarizes supported headers/parameters and provides sample HTTP and XML payloads.

## Overview
Telnyx Cloud Storage implements S3‑compatible multipart upload operations so you can upload large objects as independent parts and then assemble them server‑side. The core flow is: Create a multipart upload → Upload one or more parts (in parallel or sequence) → Optionally list uploads/parts → Complete the upload to finalize the object (or abort to discard it).

## Endpoint and authentication
- Endpoint host pattern: [region].telnyxcloudstorage.com
- Addressing: Path‑style with bucket and key in the URL path (e.g., /{bucket}/{key}).
- Authentication: AWS Signature Version 4 using your Telnyx credentials in the Authorization header.

## Create a multipart upload
Initiate an upload session for a bucket/key and receive an UploadId.

Supported headers:
- x-amz-acl: private, public-read
- x-amz-storage-class: STANDARD

### Example request
```
POST /publicbucket/mymultiloader?uploads=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: public-read
x-amz-storage-class: STANDARD
X-Amz-Date: 20230927T155204Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date;x-amz-storage-class, Signature=c4b61aa3aa192e1e569c5c6c458138b11f098cbbaaac9f7c88afeb37aa7500ef
Content-Type: text/plain
Content-Length: 22

"<file contents here>"
```

### Example response
```
<?xml version="1.0" encoding="UTF-8"?>
<InitiateMultipartUploadResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Bucket>publicbucket</Bucket>
    <Key>mymultiloader</Key>
    <UploadId>2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH</UploadId>
</InitiateMultipartUploadResult>
```

## Upload a part
Upload a single part for an existing multipart upload.

Supported query parameters:
- partNumber
- uploadId

### Example request
```
PUT /publicbucket/mymultiloader?partNumber=1&uploadId=2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Content-Type: image/png
X-Amz-Date: 20230927T155504Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature=7c96230e5ac9b1a3d9fdf95349c5eaadc78157b16321dcc5355727faf8aa1132
Content-Length: 22

"<file contents here>"
```

## List multipart uploads
Enumerate in‑progress multipart uploads within a bucket.

Supported query parameters:
- prefix
- delimiter
- key-marker
- max-keys
- max-uploads
- upload-id-marker

### Example request
```
GET /publicbucket?uploads=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: public-read
x-amz-storage-class: STANDARD
X-Amz-Date: 20230927T162150Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date;x-amz-storage-class, Signature=3475df7d1f022226a816241819edc7a152691dc99f018f49a3a5023aed6da467
```

### Example response
```
<?xml version="1.0" encoding="UTF-8"?>
<ListMultipartUploadsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Bucket>publicbucket</Bucket>
    <NextKeyMarker>mymultiloader_2</NextKeyMarker>
    <NextUploadIdMarker>2~xbDHpXAq1dlmdGM7Kuj7mL9gPDCYuZx</NextUploadIdMarker>
    <MaxUploads>1000</MaxUploads>
    <IsTruncated>false</IsTruncated>
    <Upload>
        <Key>mymultiloader_1</Key>
        <UploadId>2~3Y81uRI7FdyjpBLwnWlT_twccOWO5BB</UploadId>
        <Initiator>
            <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
            <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
        </Initiator>
        <Owner>
            <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
            <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
        </Owner>
        <StorageClass>STANDARD</StorageClass>
        <Initiated>2023-09-27T16:21:50.208Z</Initiated>
    </Upload>
    <Upload>
        <Key>mymultiloader_2</Key>
        <UploadId>2~xbDHpXAq1dlmdGM7Kuj7mL9gPDCYuZx</UploadId>
        <Initiator>
            <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
            <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
        </Initiator>
        <Owner>
            <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
            <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
        </Owner>
        <StorageClass>STANDARD</StorageClass>
        <Initiated>2023-09-27T16:21:50.208Z</Initiated>
    </Upload>
</ListMultipartUploadsResult>
```

## List parts for an upload
List the parts that have been successfully uploaded for a specific UploadId.

Supported query parameters:
- uploadId
- max-parts
- part-number-marker

### Example request
```
GET /publicbucket/mymultiloader?uploadId=2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH HTTP/1.1
Host:  [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T160734Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=c2224c5a6a794e0e41f6aa962ab72f0fc2ccb9156b946d22fdb106dd1f95586b
```

### Example response
```
<?xml version="1.0" encoding="UTF-8"?>
<ListPartsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Bucket>publicbucket</Bucket>
    <Key>mymultiloader</Key>
    <UploadId>2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH</UploadId>
    <StorageClass>STANDARD</StorageClass>
    <PartNumberMarker>0</PartNumberMarker>
    <NextPartNumberMarker>4</NextPartNumberMarker>
    <MaxParts>1000</MaxParts>
    <IsTruncated>false</IsTruncated>
    <Owner>
        <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
        <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
    </Owner>
    <Part>
        <LastModified>2023-09-27T15:55:04.138Z</LastModified>
        <PartNumber>1</PartNumber>
        <ETag>&quot;2da8bc8e8133ec2af9268515aae59e7a&quot;</ETag>
        <Size>22905</Size>
    </Part>
    <Part>
        <LastModified>2023-09-27T15:55:30.828Z</LastModified>
        <PartNumber>2</PartNumber>
        <ETag>&quot;2da8bc8e8133ec2af9268515aae59e7a&quot;</ETag>
        <Size>22905</Size>
    </Part>
    <Part>
        <LastModified>2023-09-27T15:55:35.044Z</LastModified>
        <PartNumber>3</PartNumber>
        <ETag>&quot;2da8bc8e8133ec2af9268515aae59e7a&quot;</ETag>
        <Size>22905</Size>
    </Part>
    <Part>
        <LastModified>2023-09-27T15:55:38.630Z</LastModified>
        <PartNumber>4</PartNumber>
        <ETag>&quot;2da8bc8e8133ec2af9268515aae59e7a&quot;</ETag>
        <Size>22905</Size>
    </Part>
</ListPartsResult>
```
