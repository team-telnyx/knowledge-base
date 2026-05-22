---
title: 'Telnyx Cloud Storage: Multipart Upload API (S3‑Compatible)'
summary: How to perform S3‑compatible multipart uploads with Telnyx Cloud Storage,
  including creating an upload, uploading parts, listing uploads and parts, completing
  the upload, and aborting it. This page summarizes supported headers/parameters and
  provides sample HTTP and XML payloads.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/abort-multipart-upload
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-multipart-uploads
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-parts
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part/index
updated_at: 2026-05-19T19:34:26Z
---

# Telnyx Cloud Storage: Multipart Upload API (S3‑Compatible)

*Part 2 of 2 — see also: [Part 1](telnyx-cloud-storage-multipart-upload-api-s3compatible--part-1.md)*

How to perform S3‑compatible multipart uploads with Telnyx Cloud Storage, including creating an upload, uploading parts, listing uploads and parts, completing the upload, and aborting it. This page summarizes supported headers/parameters and provides sample HTTP and XML payloads.

## Complete a multipart upload
Finalize the upload by providing the ordered list of parts (PartNumber and corresponding ETag) for a given UploadId.

Supported query parameters:
- uploadId

### Supported XML body
Each Part element must include:
- PartNumber
- ETag

### Example request
```
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

### Example response
```
<?xml version="1.0" encoding="UTF-8"?>
<CompleteMultipartUploadResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Location>[region].telnyxcloudstorage.com/publicbucket/mymultiloader_1</Location>
    <Bucket>publicbucket</Bucket>
    <Key>mymultiloader_1</Key>
    <ETag></ETag>
</CompleteMultipartUploadResult>
```

## Abort a multipart upload
Abort an in‑progress multipart upload to discard uploaded parts and release resources.

Supported query parameters:
- uploadId

### Example request
```
DELETE /publicbucket/mymultiloader?uploadId=2~vl8z2yj8-4JWQiQJZ1XiS-gUY9sIkcH HTTP/1.1
Host:  [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T161834Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=9f9271ad23f0d4da20bb880962c217fe6c5b56731bacf96a895da12abeb7fca4
```

## See also (S3 API references)
- CreateMultipartUpload: https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateMultipartUpload.html
- UploadPart: https://docs.aws.amazon.com/AmazonS3/latest/API/API_UploadPart.html
- ListMultipartUploads: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListMultipartUploads.html
- ListParts: https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListParts.html
- CompleteMultipartUpload: https://docs.aws.amazon.com/AmazonS3/latest/API/API_CompleteMultipartUpload.html
- AbortMultipartUpload: https://docs.aws.amazon.com/AmazonS3/latest/API/API_AbortMultipartUpload.html
