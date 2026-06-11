---
title: Cloud Storage API Reference
summary: Reference for the Telnyx Cloud Storage S3-compatible API, covering multipart
  upload operations (create, upload part, list, complete, abort) and object operations
  (get, delete, tagging, ACL) with supported parameters, headers, and example requests
  and responses.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/abort-multipart-upload
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-multipart-uploads
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-parts
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-objects
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-tagging
updated_at: 2026-06-11T10:24:17Z
---

# Cloud Storage API Reference

*Part 1 of 2 — see also: [Part 2](cloud-storage-api-reference--part-2.md)*

Reference for the Telnyx Cloud Storage S3-compatible API, covering multipart upload operations (create, upload part, list, complete, abort) and object operations (get, delete, tagging, ACL) with supported parameters, headers, and example requests and responses.

Telnyx Cloud Storage provides an S3-compatible API. All requests are made to `[region].telnyxcloudstorage.com` and authenticated using AWS4-HMAC-SHA256 with your Telnyx API key. See the [Amazon S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html) for full semantic details of each operation.

## Create Multipart Upload

Initiates a multipart upload. Corresponds to [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html).

**Supported headers:**

- `x-amz-acl` — `private` or `public-read`
- `x-amz-storage-class` — `STANDARD`

**Example request:**

```
POST /publicbucket/mymultiloader?uploads=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
x-amz-acl: public-read
x-amz-storage-class: STANDARD
X-Amz-Date: 20230927T155204Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date;x-amz-storage-class, Signature=c4b61aa3aa192e1e569c5c6c458138b11f098cbbaaac9f7c88afeb37aa7500ef
Content-Type: text/plain
Content-Length: 22

"<file contents here>"
```

**Example response:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<InitiateMultipartUploadResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Bucket>publicbucket</Bucket>
    <Key>mymultiloader</Key>
    <UploadId>2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH</UploadId>
</InitiateMultipartUploadResult>
```

The returned `UploadId` is used in subsequent part upload, listing, completion, and abort operations.

## Upload Part

Uploads a single part of a multipart upload. Corresponds to [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html).

**Supported parameters:**

- `partNumber`
- `uploadId`

**Example request:**

```
PUT /publicbucket/mymultiloader?partNumber=1&uploadId=2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH HTTP/1.1
Host: [region].telnyxcloudstorage.com
Content-Type: image/png
X-Amz-Date: 20230927T155504Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature=7c96230e5ac9b1a3d9fdf95349c5eaadc78157b16321dcc5355727faf8aa1132
Content-Length: 22

"<file contents here>"
```

## List Parts

Lists the parts that have been uploaded for a specific multipart upload. Corresponds to [ListParts](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html).

**Supported parameters:**

- `uploadId`
- `max-parts`
- `part-number-marker`

**Example request:**

```
GET /publicbucket/mymultiloader?uploadId=2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH HTTP/1.1
Host: [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T160734Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=c2224c5a6a794e0e41f6aa962ab72f0fc2ccb9156b946d22fdb106dd1f95586b
```

**Example response:**

```xml
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
        <ETag>"2da8bc8e8133ec2af9268515aae59e7a"</ETag>
        <Size>22905</Size>
    </Part>
    <!-- additional Part elements omitted for brevity -->
</ListPartsResult>
```

## Complete Multipart Upload

Finalises a multipart upload by assembling previously uploaded parts. Corresponds to [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html).

**Supported parameters:**

- `uploadId`

**Supported XML elements in the request body:**

- `ETag` and `PartNumber` within `<Part>` elements

**Example request:**

```
POST /publicbucket/mymultiloader_1?uploadId=2~3Y81uRI7FdyjpBLwnWlT_twccOWO5BB HTTP/1.1
Host: [region].telnyxcloudstorage.com
Content-Type: application/xml
X-Amz-Content-Sha256: beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3
X-Amz-Date: 20230927T162813Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-content-sha256;x-amz-date, Signature=b2cdd3c55ecfddc4f9f8773984b8ce2754672f8c3740fcc65feadae8d8905b94
Content-Length: 348

<CompleteMultipartUpload xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Part>
        <PartNumber>1</PartNumber>
        <ETag>"df38b7a75236d2b16ce24c6f770b2615"</ETag>
    </Part>
    <Part>
        <PartNumber>2</PartNumber>
        <ETag>"df38b7a75236d2b16ce24c6f770b2615"</ETag>
    </Part>
</CompleteMultipartUpload>
```

**Example response:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CompleteMultipartUploadResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Location>[region].telnyxcloudstorage.com/publicbucket/mymultiloader_1</Location>
    <Bucket>publicbucket</Bucket>
    <Key>mymultiloader_1</Key>
    <ETag></ETag>
</CompleteMultipartUploadResult>
```

## List Multipart Uploads

Lists in-progress multipart uploads for a bucket. Corresponds to [ListMultipartUploads](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html).

**Supported parameters:**

- `prefix`
- `delimiter`
- `key-marker`
- `max-keys`
- `max-uploads`
- `upload-id-marker`

**Example request:**

```
GET /publicbucket?uploads=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T162150Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date;x-amz-storage-class, Signature=3475df7d1f022226a816241819edc7a152691dc99f018f49a3a5023aed6da467
```

**Example response:**

```xml
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
    <!-- additional Upload elements omitted for brevity -->
</ListMultipartUploadsResult>
```

## Abort Multipart Upload

Aborts an in-progress multipart upload. Corresponds to [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html).

**Supported parameters:**

- `uploadId`

**Example request:**

```
DELETE /publicbucket/mymultiloader?uploadId=2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH HTTP/1.1
Host: [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T161834Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=9f9271ad23f0d4da20bb880962c217fe6c5b56731bacf96a895da12abeb7fca4
```
