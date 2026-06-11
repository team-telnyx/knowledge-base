---
title: Telnyx Cloud Storage API Endpoints and Bucket Operations
summary: Telnyx Cloud Storage exposes two API suites—S3-compatible and JSON companion—across
  regional endpoints, supporting standard bucket operations such as create, delete,
  and read/manage configuration for ACLs, CORS, lifecycle, location, policies, and
  tagging.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints
  content_hash: 98f1fa942fcaccc32b04c3177e42a4380bc1193c71cc43b44e778ce07385ec73
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/create-bucket/index
  content_hash: e2ae6f80201ebc985e167de32e9432cf35490def75af1771e36fbe2e7226ec47
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket
  content_hash: 50e58fea2ce528d133348d2c55833192d9a9d2b11836843ab84dc56d6ddb61df
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-cors
  content_hash: 53d998f51997d9709ff7495cb1d7b2d0e74f528698af38f653fa421e94aadd96
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-lifecycle
  content_hash: 60413968890156256ba3bb8875490eca55062fbdc360b30f2413678ad42b8ca6
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-policy
  content_hash: 370cee6ec16fd81ab858d9ee781ee4462799150fc094d17332b9830853760098
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-tagging
  content_hash: 4333b762f66823aec97427f0e10622e7c6448e092060d6a0fdddbcea995c4a9d
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-acl
  content_hash: 2c4fdb338a1582bf6eb236385dd3e5bd7723472cfd3f08c31168596201b7a2b1
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-cors
  content_hash: 071f50de22efcd21410d12535d7fa98280c720586aee4becf607bf0ae7387d10
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-lifecycle-configuration
  content_hash: 2aac1b025f1dadc5914c689bfd7f8cc277208638d18c085bded70d7ae5717760
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-location
  content_hash: 14284665f58cb846e491872b0a2e650e02683a5622072d55661ab8f58c9e0e50
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy
  content_hash: 863e1881922140eee15011926cd102b12b4aecd6be50a7d6d3ef172d71529344
updated_at: 2026-06-11T10:23:43Z
---

# Telnyx Cloud Storage API Endpoints and Bucket Operations

*Part 1 of 2 — see also: [Part 2](telnyx-cloud-storage-api-endpoints-and-bucket-operations--part-2.md)*

Telnyx Cloud Storage exposes two API suites—S3-compatible and JSON companion—across regional endpoints, supporting standard bucket operations such as create, delete, and read/manage configuration for ACLs, CORS, lifecycle, location, policies, and tagging.

## API Suites

Telnyx Cloud Storage provides two suites of APIs:

- **S3 Compatible APIs** — Compatible with AWS S3, requiring minimal changes for migration from existing S3 integrations.
- **JSON Companion API** — An extension to S3, supporting querying usage, creating presigned URLs, managing SSL, and migrating data from AWS S3. The endpoint for the JSON Companion API is `api.telnyx.com`.

## S3-Compatible Regional Endpoints

| Endpoint URL | Region |
|---|---|
| `us-central-1.telnyxcloudstorage.com` | us-central-1 |
| `us-east-1.telnyxcloudstorage.com` | us-east-1 |
| `us-west-1.telnyxcloudstorage.com` | us-west-1 |
| `eu-central-1.telnyxcloudstorage.com` | eu-central-1 |

Any US endpoint can be used for `ListBuckets` and `GetBucketLocation` across all US buckets. The European endpoint (`eu-central-1`) returns only buckets located in Europe. All other API methods must be directed at the regional endpoint where the bucket is homed; otherwise an error is returned. It is advisable to query the bucket's location first, then form the correct regional endpoint for subsequent operations.

## CreateBucket

Creates a new bucket. The request is a `PUT` to `/<bucket_name>` on the regional endpoint. The bucket's location is inherited from the regional endpoint to which the request is sent.

### Supported Headers and XML Elements

- **Supported Header:** `x-amz-acl` — accepts `private` or `public-read`
- **Supported XML Element:** `LocationConstraint` — if specified, its value must match the location of the regional endpoint, otherwise an `InvalidLocationConstraint` error is returned.

### Bucket Naming Rules

- Must be unique.
- Cannot be formatted as an IP address.
- Between 3 and 63 characters long.
- Must not contain uppercase characters or underscores.
- Must start with a lowercase letter or number.
- Can contain a dash (`-`).
- Must be a series of one or more labels separated by a single period (`.`). Labels can contain lowercase letters, numbers, and hyphens. Each label must start and end with a lowercase letter or number.

Violating naming rules returns an `InvalidBucketName` error.

### Example Request

```http
PUT /mybucket HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
Content-Type: application/xml
X-Amz-Content-Sha256: beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3
X-Amz-Date: 20230927T152207Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;content-length;content-type;host;x-amz-acl;x-amz-content-sha256;x-amz-date, Signature=eb67629c5cd507c56c5c5447323cc0190c605ab87c2b2fd3046825ca09a28425
Content-Length: 197

<?xml version="1.0" encoding="UTF-8"?>
<CreateBucketConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
   <LocationConstraint>us-east-1</LocationConstraint>
</CreateBucketConfiguration>
```

## DeleteBucket

Deletes an empty bucket. Sends a `DELETE` request to the bucket's regional endpoint.

### Example Request

```bash
curl --location --request DELETE 'https://[region].telnyxcloudstorage.com/[bucket_name]' \
--header 'X-Amz-Date: 20230927T175031Z' \
--header 'Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=host;x-amz-date, Signature=06c306e4a75de6aa98a875cfe76ee3977a1c99d60aee86b6db1f53a47539d464'
```

## DeleteBucketCors

Removes the CORS configuration from a bucket.

### Example Request

```bash
aws s3api delete-bucket-cors --bucket chatgpt-bucket-1696358562 --profile us-east-1.telnyxcloudstorage.com --endpoint-url https://us-east-1.telnyxcloudstorage.com
```

## DeleteBucketLifecycle

Removes the lifecycle configuration from a bucket. Sends a `DELETE` request to `/<bucket_name>?lifecycle=null` on the regional endpoint.

### Example Request

```http
DELETE /versionedbucket?lifecycle=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
X-Amz-Date: 20230927T173847Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=63c7e3d367d62488f9eba08ec8fdbe5bf89ef4484772b5fee952a4ac2dcd3362
```

## DeleteBucketPolicy

Removes the bucket policy from a bucket.

### Example Request

```bash
aws s3api delete-bucket-policy --bucket pubreadbuc
```

## DeleteBucketTagging

Removes the tagging configuration from a bucket. Sends a `DELETE` request to `/<bucket_name>?tagging=null` on the regional endpoint.

### Example Request

```http
DELETE /versionedbucket?tagging=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: private
X-Amz-Date: 20230927T182455Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=8bad860d937751e40011d5953da3f2463f57e30b1f00d9f25707d393f68f582b
```

## GetBucketAcl

Retrieves the access control list (ACL) for a bucket. Sends a `GET` request to `/<bucket_name>?acl=null`.

### Example Request

```http
GET /versionedbucket?acl=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
x-amz-acl: public-read
X-Amz-Date: 20230927T174306Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-acl;x-amz-date, Signature=050c7795578015f9b3f51bc6d3785d90f7394e5ef7e611ebb6ede54802faa996
```

### Example Response

```xml
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

## GetBucketCors

Retrieves the CORS configuration for a bucket.

### Example Request and Response

```bash
aws s3api get-bucket-cors --bucket my_bucket
```

```json
{
    "CORSRules": [
        {
            "AllowedHeaders": ["*"],
            "AllowedMethods": ["PUT", "DELETE", "POST"],
            "AllowedOrigins": ["http://www.example.com"]
        },
        {
            "AllowedMethods": ["GET"],
            "AllowedOrigins": ["*"]
        }
    ]
}
```

## GetBucketLifecycleConfiguration

Retrieves the lifecycle configuration for a bucket. Sends a `GET` request to `/<bucket_name>?lifecycle=null`.

### Example Request

```http
GET /versionedbucket?lifecycle=null HTTP/1.1
Host: [region].telnyxcloudstorage.com
Accept: text/xml
X-Amz-Date: 20230927T172450Z
Authorization: AWS4-HMAC-SHA256 Credential=YOUR_TELNYX_API_KEY/20230927/test/execute-api/aws4_request, SignedHeaders=accept;host;x-amz-date, Signature=c8e6ec2d0c5c34ea061e4dd47d2e7103fde5a885c25d9dca3ac743d8b6ab3330
```

### Example Response

```xml
<?xml version="1.0" encoding="UTF-8"?>
<LifecycleConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
    <Rule>
        <ID>DeleteAfterBecomingNonCurrent</ID>
        <Filter>
            <Prefix>logs/</Prefix>
        </Filter>
        <Status>Enabled</Status>
        <NoncurrentVersionExpiration>
            <NoncurrentDays>100</NoncurrentDays>
        </NoncurrentVersionExpiration>
    </Rule>
</LifecycleConfiguration>
```
