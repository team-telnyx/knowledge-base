---
title: Telnyx Cloud Storage Object Operations (S3-Compatible)
summary: Overview of Telnyx S3-compatible object operations with supported headers/parameters
  and minimal request/response examples for uploading, reading, listing, tagging,
  ACLs, and deleting objects.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object
  content_hash: 5cf75cb0fca04d93e6fbcbc0df0c075c7581125e9ae70f3905ef7156bada7b6b
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-object-tagging
  content_hash: 317295025ab08a9ae7eedd02caedea9f792ca52b9acfa3c0309ad51867e8e264
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/delete-objects
  content_hash: e37a466ef51bd039350b0e97fdc76a7e84959dad44901a2a6db29bc82be003e6
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object
  content_hash: ce34771a46aef4a3e91a812dcbed8faa7761f7d3c148595eb422332a03b17da5
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-acl
  content_hash: 6dfe9c219e4ec6b8d57f15b7c256e457c955763741e70ca120d76399e7cd9dc5
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/get-object-tagging
  content_hash: 5bdaa7a14a5862b6233562121bf0a71bea93db601fdd3c021958db025fa0c06d
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/head-object
  content_hash: 5bbed520faea3f6f968c4c8e9bf05cd32da211c281b4e33956f3db3259394d4e
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-object-versions
  content_hash: d87757c29f7d6c331ce916b030185592a9f327e6ba299f414713cb2e3e94b3da
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/list-objects
  content_hash: 2f6948138634d5fab9c00cbfb23d0449f180f7e554f7a83edc01c9149e1c1d27
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-acl
  content_hash: f508a116761598507bd3e05f36c50bc62225d4dee6223af81b2a8ffc059d66f2
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-tagging
  content_hash: 9c555eb31103eb1f25324f888814aa4d3731897afe5546fe617434f56df5b35c
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object/index
  content_hash: 0bfc4adeaa902e2dfb29e994887a4d221f8c6ae0d13231fbbb9d5ca0c8267ef7
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
