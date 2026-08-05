---
title: Cloud Storage API Reference
summary: Reference documentation for Telnyx Cloud Storage S3-compatible API operations,
  covering bucket configuration, multipart uploads, and object management endpoints
  with example requests and responses.
sources:
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
updated_at: 2026-08-05T13:38:44Z
---

# Cloud Storage API Reference

*Part 3 of 4 — see also: [Part 1](cloud-storage-api-reference--part-1.md), [Part 2](cloud-storage-api-reference--part-2.md), [Part 4](cloud-storage-api-reference--part-4.md)*

Reference documentation for Telnyx Cloud Storage S3-compatible API operations, covering bucket configuration, multipart uploads, and object management endpoints with example requests and responses.

## Multipart upload operations

Multipart upload lets you upload large objects in parts and complete them as a single object.

### CreateMultipartUpload

Initiates a multipart upload and returns an `UploadId` used by subsequent part operations. See the [CreateMultipartUpload S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html).

**Supported headers:**

- `x-amz-acl` — `private` or `public-read`
- `x-amz-storage-class` — `STANDARD`

**Example request:**

```http
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

**Example response:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<InitiateMultipartUploadResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Bucket>publicbucket</Bucket>
    <Key>mymultiloader</Key>
    <UploadId>2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH</UploadId>
</InitiateMultipartUploadResult>
```

### UploadPart

Uploads a single part of a multipart upload. See the [UploadPart S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html).

**Supported parameters:**

- `partNumber`
- `uploadId`

**Example request:**

```http
PUT /publicbucket/mymultiloader?partNumber=1&uploadId=2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Content-Type: image/png
X-Amz-Date: 20230927T155504Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature=7c96230e5ac9b1a3d9fdf95349c5eaadc78157b16321dcc5355727faf8aa1132
Content-Length: 22

"<file contents here>"
```

### ListParts

Lists the parts that have been uploaded for a specific multipart upload. See the [ListParts S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html).

**Supported parameters:**

- `uploadId`
- `max-parts`
- `part-number-marker`

**Example request:**

```http
GET /publicbucket/mymultiloader?uploadId=2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH HTTP/1.1
Host:  [region].telnyxcloudstorage.com
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

### CompleteMultipartUpload

Assembles the previously uploaded parts into a final object. See the [CompleteMultipartUpload S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html).

**Supported parameters:**

- `uploadId`

**Supported XML elements:**

- `ETag`
- `PartNumber`

**Example request:**

```http
POST /publicbucket/mymultiloader_1?uploadId=2~3Y81uRI7FdyjpBLwnWlT_twccOWO5BB HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Content-Type: application/xml
X-Amz-Content-Sha256: beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3
X-Amz-Date: 20230927T162813Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-content-sha256;x-amz-date, Signature=b2cdd3c55ecfddc4f9f8773984b8ce2754672f8c3740fcc65feadae8d8905b94
Content-Length: 348

<CompleteMultipartUpload xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Part>
        <PartNumber>1</PartNumber>
        <ETag>&quot;df38b7a75236d2b16ce24c6f770b2615&quot;</ETag>
    </Part>
    <Part>
        <PartNumber>2</PartNumber>
        <ETag>&quot;df38b7a75236d2b16ce24c6f770b2615&quot;</ETag>
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

### AbortMultipartUpload

Cancels an in-progress multipart upload and frees the storage occupied by any uploaded parts. See the [AbortMultipartUpload S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html).

**Supported parameters:**

- `uploadId`

**Example request:**

```http
DELETE /publicbucket/mymultiloader?uploadId=2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH HTTP/1.1
Host:  [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T161834Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=9f9271ad23f0d4da20bb880962c217fe6c5b56731bacf96a895da12abeb7fca4
```

### ListMultipartUploads

Lists in-progress multipart uploads for a bucket. See the [ListMultipartUploads S3 API reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html).

**Supported parameters:**

- `prefix`
- `delimiter`
- `key-marker`
- `max-keys`
- `max-uploads`
- `upload-id-marker`

**Example request:**

```http
GET /publicbucket?uploads=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: public-read
x-amz-storage-class: STANDARD
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
