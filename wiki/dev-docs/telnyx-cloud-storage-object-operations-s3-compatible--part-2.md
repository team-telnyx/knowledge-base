---
title: Telnyx Cloud Storage Object Operations (S3-Compatible)
summary: Overview of Telnyx S3-compatible object operations with supported headers/parameters
  and minimal request/response examples for uploading, reading, listing, tagging,
  ACLs, and deleting objects.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object-tagging
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
updated_at: 2026-05-19T16:04:09Z
---

# Telnyx Cloud Storage Object Operations (S3-Compatible)

*Part 2 of 2 — see also: [Part 1](telnyx-cloud-storage-object-operations-s3-compatible--part-1.md)*

Overview of Telnyx S3-compatible object operations with supported headers/parameters and minimal request/response examples for uploading, reading, listing, tagging, ACLs, and deleting objects.

## DeleteObjectTagging

Remove all tags from an object.

Example
```
DELETE /mybucket/myobject?tagging=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: private
X-Amz-Date: 20230927T180605Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=361bbc366be4fa4e2f770dad0130b09948383d8e2bb58540fd469be3af24bbb0
```

---

## DeleteObjects

Delete multiple objects in a single request.

Example (AWS CLI)
```
aws s3api delete-objects --bucket created-in-fl-1 \
  --delete '{"Objects":[{"Key":"xxx"},{"Key":"yyy"}]}'

{
  "Deleted": [{"Key": "xxx"}, {"Key": "yyy"}]
}
```

---

## Related features

- [Multipart Upload](multipart-upload.md)
- [Presigned URLs](presigned-urls.md)
- [Object Encryption](object-encryption.md)
- [Public Buckets](public-buckets.md)
- [Data Protection & Retention](data-protection-retention.md)
