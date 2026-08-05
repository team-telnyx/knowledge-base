---
title: Cloud Storage Bindings
summary: A Cloud Storage binding gives a Telnyx Edge Function a pre-authenticated
  handle to one of your buckets. Declared in `func.toml` and exposed as `env.<BINDING>`,
  the typed `CloudStorageBucket` interface lets TypeScript functions read, write,
  list, and delete objects without holding any S3 access keys.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/bindings/index
- url: https://developers.telnyx.com/docs/cloud-storage/bindings/reference
updated_at: 2026-08-05T13:39:28Z
---

# Cloud Storage Bindings

*Part 1 of 3 — see also: [Part 2](cloud-storage-bindings--part-2.md), [Part 3](cloud-storage-bindings--part-3.md)*

A Cloud Storage binding gives a Telnyx Edge Function a pre-authenticated handle to one of your buckets. Declared in `func.toml` and exposed as `env.<BINDING>`, the typed `CloudStorageBucket` interface lets TypeScript functions read, write, list, and delete objects without holding any S3 access keys.

## Overview

A **Cloud Storage binding** gives a [Telnyx Edge Function](telnyx-edge-function.md) a pre-authenticated handle to one of your buckets. You declare the binding in `func.toml`; the runtime resolves it to `env.<BINDING>` and injects the credential — your code holds **no access key or secret key**, and nothing sensitive appears in your bundle or logs.

The handle is a small, focused surface — `get`, `put`, `head`, `delete`, `list`, plus multipart upload helpers. It is the in-function counterpart of the [S3-compatible API](s3-compatible-api.md): same buckets, same objects, reached from inside a function instead of over HTTP.

Cloud Storage bindings are **TypeScript-only** — the typed `env` handle comes from the `@telnyx/edge-runtime` SDK (**≥ 0.5.0**). Other runtimes (JS, Go, Python) do not get a typed binding.

## Declaring a binding

Add a `[storage.cloudstorage.<name>]` block to the generated `func.toml`. The block key is a name you choose — it becomes the property on `env`. Declare more than one bucket by adding more blocks; each `[storage.cloudstorage.<name>]` becomes `env.<name>`.

```toml
[edge_compute]
func_id   = "…"           # filled in by new-func
func_name = "file-api"

[storage.cloudstorage.ASSETS]
bucket_name = "my-assets"   # an existing bucket
region      = "us-east-1"   # us-central-1 | us-east-1 | us-west-1 | eu-central-1 | ap-southeast-1
```

The binding points at a bucket, it does not create one. If you do not have one, create it first via the Mission Control portal, the AWS CLI, or an S3 SDK.

## Installing and generating types

`new-func` already lists `@telnyx/edge-runtime` and `@aws-sdk/client-s3` in `package.json`. Install them, then generate the typed `env`:

```bash
npm install
telnyx-edge types
```

`telnyx-edge types` writes `telnyx-env.d.ts`, which types `env.ASSETS` as `CloudStorageBucket` so the calls below type-check.

## The `CloudStorageBucket` interface

`env.<BINDING>` (a `CloudStorageBucket`) is the in-function handle to a Cloud Storage bucket. It is a pre-authenticated wrapper over the bucket — the runtime injects the credential, so your code holds no S3 access key or secret key.

```ts
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

- **Missing keys read as `null`** — `get` and `head` resolve to `null` for a key that does not exist, not an error.
- **A failed conditional read returns a body-less object** — when a `get` `onlyIf` precondition is not met, `get` resolves to a plain `CloudStorageObject` (metadata only, no `body` and no readers) so you can reuse your cached copy. Check for a body before reading it.
- **`delete` is idempotent** — deleting a missing key (single or in a batch) succeeds and resolves to `void`.
- **`put` returns partial metadata** — the resolved object carries `key`, `etag`, `httpEtag`, `version`, and any metadata you set, but not `size` or `uploaded`. Use `head` to read those after a write.
- **Custom metadata keys are lower-cased on read** — `x-amz-meta-*` header names are stored lower-cased, so `customMetadata` keys come back lower-cased (`uploadedBy` → `uploadedby`).
- **SSE-C applies to US and APAC (`ap-southeast-1`) region buckets** — `ssecKey` is honored for buckets in US regions.

## `get(key, options?)`

Read an object and its body. Returns `null` if the key does not exist.

```ts
const obj = await env.MY_BUCKET.get("uploads/logo.png");
if (obj === null) {
  // not found
} else {
  const bytes = await obj.arrayBuffer();   // consume the body once
  // obj.key, obj.size, obj.etag, obj.httpMetadata, obj.customMetadata, …
}
```

A successful read returns a `CloudStorageObjectBody` — a `CloudStorageObject` plus the `body` stream and one-shot readers `arrayBuffer()`, `text()`, `json()`, and `blob()`.

```ts
type CloudStorageGetOptions = CloudStorageOnlyIf & {
  range?: CloudStorageRange;
  ssecKey?: ArrayBuffer | string;
};
```

### Ranged reads

Pass `range` to fetch part of an object instead of the whole thing — byte-range streaming, reading a header, or resuming a download. The resolved object echoes the requested `range`.

```ts
interface CloudStorageRange {
  offset?: number;   // start byte
  length?: number;   // number of bytes from offset
  suffix?: number;   // final N bytes (mutually exclusive with offset/length)
}
```

```ts
const head = await env.MY_BUCKET.get("videos/clip.mp4", { range: { offset: 0, length: 1024 } });
const tail = await env.MY_BUCKET.get("videos/clip.mp4", { range: { suffix: 512 } });
```

### Conditional reads

Pass `onlyIf` to read only when a precondition holds — cache revalidation and "only fetch if changed." A `CloudStorageConditional` maps to `If-Match` / `If-None-Match` / `If-Unmodified-Since` / `If-Modified-Since`; you can also pass a `Headers` object directly.

```ts
interface CloudStorageConditional {
  etagMatches?: string;        // read only if the current etag matches      (If-Match)
  etagDoesNotMatch?: string;   // read only if the current etag differs       (If-None-Match)
  uploadedBefore?: Date;       // read only if unchanged since this time      (If-Unmodified-Since)
  uploadedAfter?: Date;        // read only if changed since this time        (If-Modified-Since)
}

interface CloudStorageOnlyIf {
  onlyIf?: CloudStorageConditional | Headers;
}
```

```ts
// Revalidate a cached copy: fetch the body only if the object changed.
const obj = await env.MY_BUCKET.get("data.json", { onlyIf: { etagDoesNotMatch: cachedEtag } });
if (obj !== null && !("body" in obj)) {
  // precondition failed → not modified; keep using the cached copy
} else if (obj) {
  const fresh = await obj.json();
}
```

Conditional **writes** are not supported — `onlyIf` applies to `get`/`head` only.

## `put(key, body, options?)`

Write an object. Resolves to a `CloudStorageObject` describing the write.

```ts
type CloudStoragePutBody = ReadableStream | ArrayBuffer | ArrayBufferView | Blob | string;

interface CloudStoragePutOptions {
  httpMetadata?: CloudStorageHTTPMetadata;    // Content-Type, Cache-Control, …
  customMetadata?: Record<string, string>;    // x-amz-meta-* — keys lower-cased on read
  ssecKey?: ArrayBuffer | string;             // SSE-C key (US and APAC region buckets)
}
```

```ts
await env.MY_BUCKET.put("uploads/logo.png", bytes, {
  httpMetadata: { contentType: "image/png", cacheControl: "max-age=3600" },
  customMetadata: { uploadedby: "alice" },
});

// Strings, ArrayBuffers, typed arrays, Blobs, and streams all work
await env.MY_BUCKET.put("notes/today.txt", "hello world");
```

The resolved object carries `key`, `etag` (unquoted MD5 for a single-part write), `httpEtag` (the quoted, header-ready form), `version` (when bucket versioning is enabled), and the metadata you set. `size` and `uploaded` are **not** populated on the `put` result — read them back with `head` if you need them.

## `head(key, options?)`

Read an object's metadata without its body. Returns `null` if the key does not exist. Accepts the same `onlyIf` preconditions as `get`.

```ts
const meta = await env.MY_BUCKET.head("uploads/logo.png");
// meta?.size, meta?.uploaded (Date), meta?.version, meta?.httpMetadata, meta?.customMetadata
```

Unlike `put`, `head` returns the full `CloudStorageObject` including `size` and `uploaded`.
