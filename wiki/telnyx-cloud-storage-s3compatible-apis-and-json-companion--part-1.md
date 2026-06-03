---
title: 'Telnyx Cloud Storage: S3‑Compatible APIs and JSON Companion'
summary: Telnyx Cloud Storage provides S3‑compatible buckets with regional endpoints
  and a JSON companion API for presigned URLs, usage, SSL, and migration. This page
  explains endpoints, authentication, supported features by region, limits, billing,
  advanced options (multipart, encryption, public access, custom domains, object lock),
  SDK/CLI tips, and migration from AWS S3.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints
  content_hash: adae17dff6274dca4b080767af3a1e030a12029460732f94084607d28ad1eeea
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/create-bucket
  content_hash: 326c06e96f637f4fcc6e16d21f6c2bf56089388fc9d219ad6c7f2ce10ecb2e5c
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket
  content_hash: ab7db45408ecd463eed7f37cdbf532758a6240dcaec649fb9d570e12bd4d4a61
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-cors
  content_hash: 777d7464c9d641ee5c0a8e5f591d92a0e1d4e07e77f62a14332fbfd5bc5c8275
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-lifecycle
  content_hash: 3a79f4d17cebfaf6ea236b2d682bf5229f7b84643d420e32262aeac42778845e
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-policy
  content_hash: c0b1b8fefce2fed46577b9ba63b3195f70605d0427695b87d58ea5f56e804a35
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-tagging
  content_hash: 6e200b58d05df83954f5ad2f7b61d4621ca9d77e92690f028789b2f27de1422d
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-acl
  content_hash: ca56825b92b6c41c73c641eec4964cf3411a71a4198f5409b799a0d38fc14ae3
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-cors
  content_hash: 594fe337415df9881f480b8b920b9279be76e9ec7865d0f7c7c5f7f8145bcde4
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-lifecycle-configuration
  content_hash: ee590c27de6f82dd5ff35aaef574ed96fccdca23b86ad652c7aa24d5b5bb8609
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-location
  content_hash: fe2628ba885f90d8954f22a05c197acf3754a4c7733e0c64293cb1e2f803c235
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy
  content_hash: 1b3ec565a514ba7e38939830177fe651a4783d8c1ec1779ce7a56a7f4face90a
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy-status
  content_hash: 3e5871c2c8ea78827c257542f4cd932c85200117750b32546e5083e37dcde36a
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-tagging
  content_hash: b3a92fdfe6e7eb56c080455f60df5756a5529d4c0b0e5ccb8b65d4e284c0e2ef
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-versioning
  content_hash: 82557fa197c5ffebe3f32e9006b5be711f9cdf72d4527535397334912006f016
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/head-bucket
  content_hash: fe528c18246d7031f8b9c75ca8d69a0c56f2e8b293935576eab066afff039ec8
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/list-bucket
  content_hash: 9837d27028df063ac73c6cdd615029f089a59d660e92e75582a81b15caac014b
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-acl
  content_hash: 97a1667010203728d9751b55be7ef727d5c897ad6bab3df855ad1d55298a5b87
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-cors
  content_hash: 64ab508bc29a34349dac69289a9b734888e98d4564367adcef355311382fb9a3
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-life-cycle-configuration
  content_hash: e2850199fdbf98dd0713691d12a275b1e2ca6a441d1e1dc970f56f6be0930ab9
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-policy
  content_hash: 7e600abd20a26051fe87fed576f9e628b4fb27fddc0c7b498d88caa1f7fbed41
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-tagging
  content_hash: f68877e56a6fcdc19a2d6b4a9a76dab74a863d0501dbea639e116fae8615597c
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/put-bucket-versioning
  content_hash: 2b83456768771f3fff43d7ab65601a56a686bfda4eb3407ff0f0da0ede18c2ac
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/abort-multipart-upload
  content_hash: 76eb089d9ce3fd93434c3048cfed4e7d8173229d9ab04e4931891d9916ded986
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/complete-multipart-upload
  content_hash: 7d6698408db0dd9aa3c32db1d92b270643d37482eb3152b4501519e78da00fea
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/create-multipart-upload
  content_hash: edbb9fe698b9dff9fe30625edf2585fc404089488f3a791bb55a2efcd4d5ea3c
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-multipart-uploads
  content_hash: 72b59313eb749f92336b450a378b4b3b9aa1433299575f9be0b62fba37b623f8
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/list-parts
  content_hash: cb6ce45c0f72d7c961dd29cac3afb4dc81cfeb48858669f0a7f4fe7c25c0949a
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/multipart-operations/upload-part
  content_hash: deb426c4d4f0e3e4985c76c64c0635da7b67fbffff48540d980177aebd75871d
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
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object
  content_hash: 0bfc4adeaa902e2dfb29e994887a4d221f8c6ae0d13231fbbb9d5ca0c8267ef7
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-acl
  content_hash: f508a116761598507bd3e05f36c50bc62225d4dee6223af81b2a8ffc059d66f2
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/object-operations/put-object-tagging
  content_hash: 9c555eb31103eb1f25324f888814aa4d3731897afe5546fe617434f56df5b35c
- url: https://developers.telnyx.com/docs/cloud-storage/authentication
  content_hash: 0c2378bd950f974fce98fdc0685e25d0c0e85ae19fd8197fce332b66e4960325
- url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility
  content_hash: fcc0774c4d890cb79a734286f2aab1831006eda8cad8042c71a2722a982ac613
- url: https://developers.telnyx.com/docs/cloud-storage/billing
  content_hash: 0bd186e7d6927124ab008d2e960f303d3fb5c821d94aafcea0d980d70d607c50
- url: https://developers.telnyx.com/docs/cloud-storage/bucket-addressing
  content_hash: bd7292bd88134619c7a41fc84bf57306e95361e202eefa6a38956dfe7163ff72
- url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket
  content_hash: 3ff90a204d01e2cbc8d5b6fd58c586d99750053b46bf46a5482d9c5ed6a69ff5
- url: https://developers.telnyx.com/docs/cloud-storage/limits
  content_hash: 98ccc21e839e533d898ac5c54bdad4a9cb0de122e00f9d333679ebac155f0e81
- url: https://developers.telnyx.com/docs/cloud-storage/lock-and-retention
  content_hash: 7a28baef0113b6e8e25cf5a44e69410a5d76201a6a16e9d8ed49e520a73f2bbd
- url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws
  content_hash: ae62d3782be3ef55eccd8afe20eee4aca02210750d98006f6b1f730c06692396
- url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload
  content_hash: b9fa94539b1ddbb7ecb2ccf77e78a3f37b45814d92e8a08def73502414df6862
- url: https://developers.telnyx.com/docs/cloud-storage/object-encryption
  content_hash: 394a6f9d2807facfd5e30150d153469fb4ce253e7e93d030f052a4e825d28894
- url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks
  content_hash: d7ca4602d6091c4b43bb9d77578e643b9f2b64d95e8531652e0b1a908ac52ed8
- url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls
  content_hash: 7fb6e1a08cc9f0a2f1aab1d364bacbe6694a5365ba15d5d9d4583d7a2e4ce266
- url: https://developers.telnyx.com/docs/cloud-storage/public-buckets
  content_hash: 2030436a585b7a67bb7cd7216bf55646be29507888b28a9946f00470a0dd866e
- url: https://developers.telnyx.com/docs/cloud-storage/quick-start
  content_hash: de7305031ad12952d43608627f9c4d35db6fb558bda02e2e0f59db3b48ba969d
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
  content_hash: 483f1695dbcb1a6fbf690730fe21b088bdcab4055a9667b5756e126152d18674
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
  content_hash: 24932b4695c9a69cfbad8addf623462a15d0ad075f39c646b0bdb8277fd907eb
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
  content_hash: fe805ed916a0851ea179ff15fd7ec63c92b811faa3c47aa9f9aefcb8323a4f2a
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
  content_hash: 3a98695238da90c2545a8747d605c4061d83f1ea855739e84c83524731f63a7a
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node
  content_hash: b7e40250309bec83e7bc2b84e5dd0c03b500a152d201dbce331d64a20516a010
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
  content_hash: 20ebc62695aa9410ab08f4d018b16b7451abe13dbbdb6afa10c8cc9bd398c6ea
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
  content_hash: 03d7506fd43baef1e03aa9fa9caafbb8fd0fcb36a8a45e7a835f5fea5ce862b0
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
  content_hash: dd89cce6b812faa2be0ad7e4d50e275e4eec7563331de9ca7c5baea10b2bdbb8
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
  content_hash: 1c24693bb1b725118ab350dedf9ae8d470da4c0fed6cb5d42fb312bf667558ed
- url: https://developers.telnyx.com/docs/cloud-storage/supported
  content_hash: 63c09b5b5bd994d394ba612e35204dd50a82e05bfa87decea5b98f10fbe60fda
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
  content_hash: ca078c865ec22ff1dbecd0fbb39a5ab49f50723fc5830a1800b0f7060af3542b
updated_at: 2026-05-08T13:06:17Z
---

# Telnyx Cloud Storage: S3‑Compatible APIs and JSON Companion

*Part 1 of 2 — see also: [Part 2](telnyx-cloud-storage-s3compatible-apis-and-json-companion--part-2.md)*

Telnyx Cloud Storage provides S3‑compatible buckets with regional endpoints and a JSON companion API for presigned URLs, usage, SSL, and migration. This page explains endpoints, authentication, supported features by region, limits, billing, advanced options (multipart, encryption, public access, custom domains, object lock), SDK/CLI tips, and migration from AWS S3.

## Regions and endpoints

Telnyx exposes regional S3‑compatible endpoints; choose the one that matches the bucket’s home region:

- us-central-1 → us-central-1.telnyxcloudstorage.com
- us-east-1 → us-east-1.telnyxcloudstorage.com
- us-west-1 → us-west-1.telnyxcloudstorage.com
- eu-central-1 → eu-central-1.telnyxcloudstorage.com

Endpoint selection rules:
- ListBuckets and GetBucketLocation: any US endpoint will list/locate all US buckets; the EU endpoint returns only EU buckets.
- All other S3 methods must target the bucket’s home region, or you’ll get an error. Best practice: call GetBucketLocation first, then direct subsequent operations to that region.

JSON companion API (for presigned URLs, usage, SSL, migration) is served from api.telnyx.com.

## Authentication (SigV4 with your Telnyx API key)

- Send an AWS Signature Version 4 Authorization header, but substitute your Telnyx API key as the access-key-id. Telnyx validates only the API key; the date/region/service/secret/signature fields are ignored (kept for S3 compatibility).
- Third‑party/CLI mapping:
  - Access Key ID → Telnyx API key
  - Secret Access Key → leave blank, reuse the API key, or use any placeholder
- When using SDKs, configure the S3 client to point to https://[region].telnyxcloudstorage.com and provide the API key via the SDK’s credentials provider.

Details: see Authentication and SDK examples for each language.

## Addressing and DNS styles

- Path‑style: https://[region].telnyxcloudstorage.com/[bucket]/[object]
- Virtual‑hosted‑style: https://[bucket].[region].telnyxcloudstorage.com/[object]

## API surface and regional compatibility

Telnyx implements a large subset of the S3 API. Unsupported methods return an S3‑compatible XML NotImplemented error. See the Compatibility Matrix for the authoritative list.

Regional highlights (summary):
- US regions: broad support including ACLs, policies, CORS, lifecycle, versioning, multipart upload, object tagging, policy status, etc.
- EU region: core bucket/object CRUD is supported (Create/Delete/List/Head Bucket; GetBucketLocation; Get/Put/Delete/List Objects; HeadObject; DeleteObjects). Many advanced features (ACLs, CORS, policies, lifecycle, versioning, multipart, tagging) are not currently supported in EU.

Always consult the matrix before relying on specific S3 features.

## Creating buckets and naming rules

- A bucket’s location is inherited from the regional endpoint you send CreateBucket to. If you include LocationConstraint in the request body, it must match that region, otherwise you’ll receive InvalidLocationConstraint.
- Bucket names must be globally unique and DNS‑compatible:
  - 3–63 characters; lowercase letters, numbers, and hyphens; no underscores or uppercase; not an IP address.
  - Must start and end with a letter or number; labels separated by dots.
  - Violations return InvalidBucketName; name conflicts return BucketAlreadyExists.

## Core operations at a glance

S3‑compatible behavior applies. Typical workflows include:
- Bucket operations: CreateBucket, DeleteBucket, HeadBucket, ListBuckets; configuration (US‑only features include ACL, CORS, policies, lifecycle, versioning, tagging).
- Object operations: PutObject, GetObject, HeadObject, ListObjects/ListObjectsV2, DeleteObject/DeleteObjects. Object ACL/tagging are US‑only.
- Versioning: Get/Put bucket versioning and ListObjectVersions (US‑only).
- Multipart upload (US‑only): CreateMultipartUpload, UploadPart, CompleteMultipartUpload, AbortMultipartUpload, ListMultipartUploads, ListParts.
  - Limits recap: min 5 MiB per part (except last), max 5 GB per part, up to 10,000 parts, up to 5 TiB per object.

See individual API reference pages for examples and supported headers.

## Multipart upload and size limits

Use multipart for large files. Platform limits:
- Requests per second: 500 per account; 200 per bucket; up to 10 concurrent PUT/COPY per object.
- Single PUT object size: up to 5 GB; multipart to 5 TiB; 10,000 parts max; min 5 MiB per part (last part exempt).
- Max buckets per account: 100; max objects per bucket: 50 million.

## Billing, usage, and suspension

You are billed for:
- Stored bytes (measured hourly; 4 KiB minimum billable object size; metadata counts):
  - US: first 10 GiB/month free; then $0.006/GiB‑month. AI embedded storage: $0.60/GiB‑month.
  - EU: no free tier; $0.025/GiB‑month. AI embedded storage: $0.60/GiB‑month.
- API operations:
  - US: Class A (PUT/COPY/POST/LIST) → first 1M free/month, then $0.50 per 1M; Class B (GET/SELECT/others) → first 10M free/month, then $0.04 per 1M.
  - EU: State‑change (PUT/COPY/POST/LIST) → $5.00 per 1M; Read (GET/SELECT/others) → $0.40 per 1M.

Account suspension:
- If available credit is negative, API calls fail with UserSuspended (data retained). Access is restored when the balance is positive. After 30 days negative, data is permanently purged.

Usage visibility (JSON companion API at api.telnyx.com):
- Bucket Snapshot: GET /v2/storage/buckets/{bucket}/usage/storage
- API Usage: GET /v2/storage/buckets/{bucket}/usage/api with time filters

## Presigned URLs (JSON companion; US‑only)

- Do NOT use AWS SDK/CLI presigners (they would expose your API key). Use the JSON companion endpoint: POST /v2/storage/buckets/{bucket}/{object}/presigned_url with a TTL.
- The response includes a presigned_url that carries an X-AMZ-Security-Token query parameter. Use it directly to PUT or GET the object anonymously within TTL.
- Long‑lived presigned URLs are privileged; non‑verified accounts are limited to TTL ≤ 5 minutes. For longer TTLs, obtain Level 2 account verification.

## Public access and custom domains (US‑only)

Public buckets (privileged):
- Making a bucket public (via bucket policy or ACL) requires Level 2 verification. Apply a policy that grants s3:GetObject to "*" for the bucket arn:aws:s3:::{bucket}/*.

HTTPS with your custom domain:
- Ensure the desired subdomain is available as a bucket name, then create the bucket with that exact name (e.g., assets.example.com).
- Make the bucket public (policy/ACL as above).
- Configure DNS for virtual‑hosted style (CNAME/ALIAS to [bucket].[region].telnyxcloudstorage.com).
- Upload the SSL certificate and matching key in the Portal under the bucket’s SSL/TLS section:
  - Bucket name must match an SNI in the cert (wildcards like *.example.com match subdomains, not the apex).
  - Include intermediate certificates (leaf first). Root may be omitted but including it is safest.
- Verify by fetching https://{bucket-domain}/{object} — you should see a valid certificate and content loads.

## Object encryption and retention (US‑only)

- Server‑Side Encryption with customer‑provided keys (SSE‑C) is supported for PutObject. Provide AES256 algorithm, the base64 key, and key MD5 per S3 semantics.
- Object Lock & Retention:
  - Must enable object lock at bucket creation time. Versioning is auto‑enabled.
  - Set/get object retention (e.g., Mode: GOVERNANCE, RetainUntilDate). Protected versions cannot be deleted; attempts return AccessDenied.

## Emptying large buckets safely

For buckets with many objects/versions, use lifecycle rules to asynchronously expire current and noncurrent versions and abort incomplete multipart uploads. Apply a lifecycle configuration (e.g., expire after 1 day) and verify it via GetBucketLifecycleConfiguration; check back after 24 hours.
