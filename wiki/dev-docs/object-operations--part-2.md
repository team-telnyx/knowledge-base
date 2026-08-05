---
title: Object Operations
summary: Reference documentation for the S3-compatible object operations supported
  by Telnyx Cloud Storage, covering read, write, listing, tagging, ACL, and versioning
  endpoints with example requests and responses.
sources:
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
updated_at: 2026-08-05T13:38:58Z
---

# Object Operations

*Part 2 of 2 — see also: [Part 1](object-operations--part-1.md)*

Reference documentation for the S3-compatible object operations supported by Telnyx Cloud Storage, covering read, write, listing, tagging, ACL, and versioning endpoints with example requests and responses.

## ListObjectVersions

Enumerates all versions of objects in a versioning-enabled bucket. See the [AWS ListObjectVersions reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectVersions.html) for the full specification.

**Supported parameters:**

- `prefix`
- `delimiter`
- `marker`
- `max-keys`

Example request:

```
GET /versionedbucket?versions=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
Accept: application/octet-stream
X-Amz-Date: 20230927T170348Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=15c5f0d8404b4e43153138818ca4cd0895c6a0bd4b94173bb6080a71f41bc49f
```

Example response:

```
<?xml version="1.0" encoding="UTF-8"?>
<ListVersionsResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Name>versionedbucket</Name>
    <Prefix></Prefix>
    <MaxKeys>1000</MaxKeys>
    <IsTruncated>false</IsTruncated>
    <KeyMarker></KeyMarker>
    <VersionIdMarker></VersionIdMarker>
    <Version>
        <Key>versionedobject</Key>
        <VersionId>X04kXxTyoh1YjplIl647teiNbL0foEN</VersionId>
        <IsLatest>true</IsLatest>
        <LastModified>2023-09-27T17:01:09.522Z</LastModified>
        <ETag>&quot;22472751e76c3a57583d89785e2330e4&quot;</ETag>
        <Size>279010</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
            <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
            <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
        </Owner>
        <Type>Normal</Type>
    </Version>
    <Version>
        <Key>versionedobject</Key>
        <VersionId>IWv2xkiXwOQvN1RClOuCeJZKKFIjjc7</VersionId>
        <IsLatest>false</IsLatest>
        <LastModified>2023-09-27T17:00:51.542Z</LastModified>
        <ETag>&quot;2da8bc8e8133ec2af9268515aae59e7a&quot;</ETag>
        <Size>22905</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
            <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
            <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
        </Owner>
        <Type>Normal</Type>
    </Version>
    <Version>
        <Key>versionedobject</Key>
        <VersionId>Hmvl0sI98e-m9fyFZW23gC2vz2hODKC</VersionId>
        <IsLatest>false</IsLatest>
        <LastModified>2023-09-27T17:00:22.591Z</LastModified>
        <ETag>&quot;0e43168b1e60136a3d4292c54763d449&quot;</ETag>
        <Size>27761</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
            <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
            <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
        </Owner>
        <Type>Normal</Type>
    </Version>
    <Version>
        <Key>versionedobject_xxx</Key>
        <VersionId>TUKc1O3XHubZcxH9Wo.MPaddPsJY7Wi</VersionId>
        <IsLatest>true</IsLatest>
        <LastModified>2023-09-27T17:03:44.249Z</LastModified>
        <ETag>&quot;22472751e76c3a57583d89785e2330e4&quot;</ETag>
        <Size>279010</Size>
        <StorageClass>STANDARD</StorageClass>
        <Owner>
            <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
            <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
        </Owner>
        <Type>Normal</Type>
    </Version>
</ListVersionsResult>
```

## GetObjectAcl

Returns the access control list (ACL) for an object. See the [AWS GetObjectAcl reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAcl.html) for the full specification.

Example request:

```
GET /mybucket/myobject?acl=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: private
X-Amz-Date: 20230927T175743Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=4edb4e62f2a28e4ff8e6b317fd867b4baf382b3c87b26e2404ea7a766779be4d
```

Example response:

```
<?xml version="1.0" encoding="UTF-8"?>
<AccessControlPolicy xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Owner>
        <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
        <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
    </Owner>
    <AccessControlList>
        <Grant>
            <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group">
                <URI>http://acs.amazonaws.com/groups/global/AllUsers</URI>
            </Grantee>
            <Permission>READ</Permission>
        </Grant>
        <Grant>
            <Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser">
                <ID>27784a49-1f14-4209-a58d-27fe905efe58</ID>
                <DisplayName>27784a49-1f14-4209-a58d-27fe905efe58</DisplayName>
            </Grantee>
            <Permission>FULL_CONTROL</Permission>
        </Grant>
    </AccessControlList>
</AccessControlPolicy>
```

## PutObjectAcl

Sets the access control list (ACL) for an object. See the [AWS PutObjectAcl reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectAcl.html) for the full specification.

> **Warning:** Only verified users can update bucket policy. To request KYC on your account, go to [Portal Account Verifications](https://portal.telnyx.com/#/app/account/verifications).

**Supported headers:**

- `x-amz-acl` — `private` or `public-read`
- `versionId`

Example request:

```
PUT /mybucket/myobject?acl=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: public-read
X-Amz-Date: 20230927T175633Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=71b70f25be863194c5d573fdf09ea02139af3cbcaa5e16dc53a0f30d41f7311a
```

## GetObjectTagging

Returns the tag set associated with an object. See the [AWS GetObjectTagging reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectTagging.html) for the full specification.

Example request:

```
GET /mybucket/myobject?tagging=null HTTP/1.1
Host:  [region].telnyxcloudstorage.com
x-amz-acl: private
X-Amz-Date: 20230927T180458Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-acl;x-amz-date, Signature=655002dff20fc340dcfb66b4e06595ddfe950b9e091992f4c82ac0777b42ff8e
```

Example response:

```
<?xml version="1.0" encoding="UTF-8"?>
<Tagging xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <TagSet>
        <Tag>
            <Key>dimention_1</Key>
            <Value>value_1</Value>
        </Tag>
        <Tag>
            <Key>dimention_2</Key>
            <Value>value_2</Value>
        </Tag>
    </TagSet>
</Tagging>
```

## PutObjectTagging

Sets the tag set for an object. See the [AWS PutObjectTagging reference](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObjectTagging.html) for the full specification.

**Supported headers:**

- `versionId`

Example request:

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
      <Tag>
         <Key>dimention_1</Key>
         <Value>value_1</Value>
      </Tag>
      <Tag>
         <Key>dimention_2</Key>
         <Value>value_2</Value>
      </Tag>
   </TagSet>
</Tagging>
```
