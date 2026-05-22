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

*Part 1 of 2 — see also: [Part 2](telnyx-cloud-storage-object-operations-s3-compatible--part-2.md)*

Overview of Telnyx S3-compatible object operations with supported headers/parameters and minimal request/response examples for uploading, reading, listing, tagging, ACLs, and deleting objects.

## Endpoint and authentication

All requests target your regional endpoint and are signed with AWS Signature Version 4.

- Host pattern: [region].telnyxcloudstorage.com
- Common headers: X-Amz-Date, Authorization (AWS4-HMAC-SHA256 …)
- See also: [Authentication](authentication.md), [API Endpoints & Organization](api-endpoints-organization.md), [Bucket Addressing](bucket-addressing.md), [AWS S3 Compatibility](aws-s3-compatibility.md)

---

## PutObject

Upload an object.

Supported headers
- x-amz-acl: private, public-read
- x-amz-storage-class: STANDARD
- x-amz-meta-*
- x-amz-server-side-encryption-customer-algorithm
- x-amz-server-side-encryption-customer-key
- x-amz-server-side-encryption-customer-key-MD5

Example
```
PUT /mybucket/myobject HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-storage-class: STANDARD
x-amz-acl: private
x-amz-meta-author: john
Content-Type: image/png
X-Amz-Date: 20230927T152352Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-date, Signature=f1a15846adc6247727c0dcfbb738d8ee4463527023e7818bf128866944981dea
Content-Length: 22

"<file contents here>"
```

---

## GetObject

Download an object (optionally with conditional and range requests).

Supported headers
- If-Match
- If-Modified-Since
- If-None-Match
- If-Unmodified-Since
- Range

Example
```
GET /mybucket/myobject HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: application/octet-stream
X-Amz-Date: 20230927T152801Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=41797df5b33f76003806aeb1eba3f25e108ecdb8582e6575e3bb1aaff4ddb839
```

---

## HeadObject

Retrieve object metadata without returning the object body.

Supported headers
- If-Match
- If-Modified-Since
- If-None-Match
- If-Unmodified-Since
- Range

Example request
```
HEAD /mybucket/myobject HTTP/1.1
Host:  [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T164456Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=d198d5440102737bd0dc5753ce6e5a843a673779ece724acd84ae08aedfe8297
```

Example response (truncated)
```
HTTP/1.1 200 OK
accept-ranges: bytes
content-length: 22905
content-type: image/png
etag: "2da8bc8e8133ec2af9268515aae59e7a"
last-modified: Wed, 27 Sep 2023 15:23:52 GMT
x-amz-meta-author: john
x-amz-storage-class: STANDARD
server: Telnyx API
```

---

## ListObjects

List objects within a bucket.

Supported parameters
- prefix, delimiter, marker, max-keys

Example
```
GET /mybucket?prefix=myobject HTTP/1.1
Host:  [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T154626Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=b77c8c94d8f0bd0913708ae7da0fbac552d14a6f2b8853b6e297a12127156e38
```

Example response (truncated)
```
<?xml version="1.0" encoding="UTF-8"?>
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Name>mybucket</Name>
  <Prefix>myobject</Prefix>
  <MaxKeys>1000</MaxKeys>
  <IsTruncated>false</IsTruncated>
  <Contents>
    <Key>myobject</Key>
    <ETag>&quot;2da8...e7a&quot;</ETag>
    <Size>22905</Size>
    <StorageClass>STANDARD</StorageClass>
  </Contents>
</ListBucketResult>
```

---

## ListObjectVersions

List versions in a versioned bucket.

Supported parameters
- prefix, delimiter, marker, max-keys

Example
```
GET /versionedbucket?versions=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: application/octet-stream
X-Amz-Date: 20230927T170348Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=15c5f0d8404b4e43153138818ca4cd0895c6a0bd4b94173bb6080a71f41bc49f
```

Example response (truncated)
```
<?xml version="1.0" encoding="UTF-8"?>
<ListVersionsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Name>versionedbucket</Name>
  <Version>
    <Key>versionedobject</Key>
    <VersionId>X04kXxTyoh1YjplIl647teiNbL0foEN</VersionId>
    <IsLatest>true</IsLatest>
    <Size>279010</Size>
    <StorageClass>STANDARD</StorageClass>
  </Version>
</ListVersionsResult>
```

---

## PutObjectACL

Set an object's canned ACL.

Supported headers/parameters
- x-amz-acl: private, public-read
- versionId

Example
```
PUT /mybucket/myobject?acl=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: public-read
X-Amz-Date: 20230927T175633Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=71b70f25be863194c5d573fdf09ea02139af3cbcaa5e16dc53a0f30d41f7311a
```

---

## GetObjectAcl

Retrieve an object's ACL.

Example request
```
GET /mybucket/myobject?acl=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: private
X-Amz-Date: 20230927T175743Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=4edb4e62f2a28e4ff8e6b317fd867b4baf382b3c87b26e2404ea7a766779be4d
```

Example response (truncated)
```
<?xml version="1.0" encoding="UTF-8"?>
<AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <Owner>
    <ID>27784a49-...</ID>
  </Owner>
  <AccessControlList>
    <Grant>
      <Grantee xsi:type="Group" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
        <URI>http://acs.amazonaws.com/groups/global/AllUsers</URI>
      </Grantee>
      <Permission>READ</Permission>
    </Grant>
  </AccessControlList>
</AccessControlPolicy>
```

---

## PutObjectTagging

Create or replace the tag set on an object.

Supported parameters
- versionId

Example
```
PUT /mybucket/myobject?tagging=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: private
Content-Type: application/xml
X-Amz-Content-Sha256: beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3
X-Amz-Date: 20230927T180401Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=content-length;content-type;host;x-amz-acl;x-amz-content-sha256;x-amz-date, Signature=cd6f3a0350f531a0bc89cfc145463f963fc967bcaeef2ae9d68490cee01ed8af
Content-Length: 271

<Tagging xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <TagSet>
    <Tag><Key>dimention_1</Key><Value>value_1</Value></Tag>
    <Tag><Key>dimention_2</Key><Value>value_2</Value></Tag>
  </TagSet>
</Tagging>
```

---

## GetObjectTagging

Retrieve an object's tag set.

Example request
```
GET /mybucket/myobject?tagging=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: private
X-Amz-Date: 20230927T180458Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=655002dff20fc340dcfb66b4e06595ddfe950b9e091992f4c82ac0777b42ff8e
```

Example response
```
<?xml version="1.0" encoding="UTF-8"?>
<Tagging xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <TagSet>
    <Tag><Key>dimention_1</Key><Value>value_1</Value></Tag>
    <Tag><Key>dimention_2</Key><Value>value_2</Value></Tag>
  </TagSet>
</Tagging>
```

---

## DeleteObject

Delete a single object.

Example
```
DELETE /publicbucket/mymultiloader_1 HTTP/1.1
Host:  [region].telnyxcloudstorage.com
X-Amz-Date: 20230927T164329Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=539be1c5c92d8b89bcc4ea79eccb1f6e8ee3e1bd5c362dbf7b5f9bb2fa5515ca
```

---
