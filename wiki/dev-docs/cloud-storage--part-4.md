---
title: Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service available
  in four regions (us-central-1, us-east-1, us-west-1, eu-central-1). It can be accessed
  via the AWS S3 API, AWS SDKs, AWS CLI, third-party S3 tools, the Telnyx Mission
  Control Portal, or directly from inside a Telnyx Edge Function via a pre-authenticated
  binding. Authentication uses your Telnyx API key as the S3 credential. The service
  supports standard S3 operations (with some US-only features like presigned URLs,
  public buckets, object lock, and SSE-C encryption), usage-based billing with a US
  free tier, and a JSON companion API for usage queries, presigned URLs, SSL management,
  and AWS S3 migration.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/api-endpoints/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/create-bucket/index
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-lifecycle
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-policy
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/delete-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-acl
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-cors
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-lifecycle-configuration
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-location
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-policy-status
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-tagging
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/get-bucket-versioning
- url: https://developers.telnyx.com/docs/cloud-storage/api-reference/bucket-operations/head-bucket
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
- url: https://developers.telnyx.com/docs/cloud-storage/authentication
- url: https://developers.telnyx.com/docs/cloud-storage/aws-s3-compatibility/index
- url: https://developers.telnyx.com/docs/cloud-storage/billing
- url: https://developers.telnyx.com/docs/cloud-storage/bindings/index
- url: https://developers.telnyx.com/docs/cloud-storage/bindings/reference
- url: https://developers.telnyx.com/docs/cloud-storage/bucket-addressing
- url: https://developers.telnyx.com/docs/cloud-storage/emptying-bucket
- url: https://developers.telnyx.com/docs/cloud-storage/limits/index
- url: https://developers.telnyx.com/docs/cloud-storage/lock-and-retention
- url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws
- url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/object-encryption
- url: https://developers.telnyx.com/docs/cloud-storage/overview/index
- url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks
- url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls
- url: https://developers.telnyx.com/docs/cloud-storage/public-buckets
- url: https://developers.telnyx.com/docs/cloud-storage/quick-start/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
- url: https://developers.telnyx.com/docs/cloud-storage/ssl-certificates
- url: https://developers.telnyx.com/docs/cloud-storage/supported
- url: https://developers.telnyx.com/docs/cloud-storage/third-party
updated_at: 2026-07-17T09:13:08Z
---

# Cloud Storage

*Part 4 of 5 — see also: [Part 1](cloud-storage--part-1.md), [Part 2](cloud-storage--part-2.md), [Part 3](cloud-storage--part-3.md), [Part 5](cloud-storage--part-5.md)*

Telnyx Cloud Storage is an S3-compatible object storage service available in four regions (us-central-1, us-east-1, us-west-1, eu-central-1). It can be accessed via the AWS S3 API, AWS SDKs, AWS CLI, third-party S3 tools, the Telnyx Mission Control Portal, or directly from inside a Telnyx Edge Function via a pre-authenticated binding. Authentication uses your Telnyx API key as the S3 credential. The service supports standard S3 operations (with some US-only features like presigned URLs, public buckets, object lock, and SSE-C encryption), usage-based billing with a US free tier, and a JSON companion API for usage queries, presigned URLs, SSL management, and AWS S3 migration.

## Cloud Storage Bindings (Edge Functions)

A **Cloud Storage binding** gives a [Telnyx Edge Function](use-a-bucket-from-an-edge-function.md) a pre-authenticated handle to one of your buckets. You declare the binding in `func.toml`; the runtime resolves it to `env.<BINDING>` and injects the credential — your code holds **no access key or secret key**, and nothing sensitive appears in your bundle or logs.

The handle is a small, focused surface — `get`, `put`, `head`, `delete`, `list`. It is the in-function counterpart of the S3-compatible API: same buckets, same objects, reached from inside a function instead of over HTTP.

Cloud Storage bindings are **TypeScript-only** — the typed `env` handle comes from the `@telnyx/edge-runtime` SDK (≥ 0.5.0). Other runtimes (JS, Go, Python) don't get a typed binding.

### Declaring a Binding

Add a `[storage.cloudstorage.<name>]` block to `func.toml`. The block key is a name you choose — it becomes the property on `env`:

```
[edge_compute]
func_id   = "…"
func_name = "file-api"

[storage.cloudstorage.ASSETS]
bucket_name = "my-assets"
region      = "us-east-1"
```

Declare more than one bucket by adding more blocks — each becomes `env.<name>`.

### CloudStorageBucket API

```
interface CloudStorageBucket {
  get(key: string, options?: CloudStorageGetOptions): Promise<CloudStorageObjectBody | CloudStorageObject | null>;
  put(key: string, body: CloudStoragePutBody, options?: CloudStoragePutOptions): Promise<CloudStorageObject | null>;
  head(key: string, options?: CloudStorageOnlyIf): Promise<CloudStorageObject | null>;
  delete(key: string | string[]): Promise<void>;
  list(options?: CloudStorageListOptions): Promise<CloudStorageListResult>;
  createMultipartUpload(key: string, options?: CloudStoragePutOptions): Promise<CloudStorageMultipartUpload>;
  resumeMultipartUpload(key: string, uploadId: string, options?: CloudStoragePutOptions): CloudStorageMultipartUpload;
}
```

Key behaviors:

- **Missing keys read as `null`** — `get` and `head` resolve to `null` for a key that doesn't exist.
- **A failed conditional read returns a body-less object** — when a `get` precondition isn't met, `get` resolves to a plain `CloudStorageObject` (metadata only, no `body` and no readers).
- **`delete` is idempotent** — deleting a missing key (single or in a batch) succeeds and resolves to `void`.
- **`put` returns partial metadata** — the resolved object carries `key`, `etag`, `httpEtag`, `version`, and any metadata you set, but not `size` or `uploaded`. Use `head` to read those after a write.
- **Custom metadata keys are lower-cased on read** — `x-amz-meta-*` header names are stored lower-cased.
- **SSE-C applies to US-region buckets** — `ssecKey` is honored for buckets in US regions.

### `get(key, options?)`

Read an object and its body. Returns `null` if the key does not exist. Supports ranged reads (`offset`/`length`/`suffix`) and conditional reads (`etagMatches`, `etagDoesNotMatch`, `uploadedBefore`, `uploadedAfter`).

### `put(key, body, options?)`

Write an object. `body` can be a `ReadableStream`, `ArrayBuffer`, `ArrayBufferView`, `Blob`, or `string`. Options include `httpMetadata`, `customMetadata`, and `ssecKey`.

### `head(key, options?)`

Read an object's metadata without its body. Returns `null` if the key does not exist. Accepts the same `onlyIf` preconditions as `get`.

### `delete(key | keys)`

Remove one object, or many in a single call (up to 1000 keys per call). Idempotent.

### `list(options?)`

Enumerate objects (metadata only). Options include `prefix`, `limit`, `cursor`, `delimiter`, and `include` (for `httpMetadata` and/or `customMetadata`). When `truncated` is `true`, pass the returned `cursor` back to fetch the next page. Set `delimiter` to `/` for hierarchical ("folder") listing.

### Multipart Upload

Upload a large object in parts from inside a function. Available on **US-region** buckets. Use `createMultipartUpload`, `uploadPart` (parts numbered from 1; every part except the last must be at least 5 MiB), `complete`, and `abort`. Use `resumeMultipartUpload` to rebuild a handle for an existing `uploadId`.

### Server-Side Encryption (SSE-C)

Pass `ssecKey` on `get`, `put`, and multipart calls to encrypt with a customer-provided key. The key is a 256-bit (32-byte) AES key, given as an `ArrayBuffer` or a 64-character hex `string`. Supply the same key on read that you used on write. SSE-C applies to **US-region** buckets.
