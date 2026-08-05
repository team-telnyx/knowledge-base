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

*Part 2 of 3 — see also: [Part 1](cloud-storage-bindings--part-1.md), [Part 3](cloud-storage-bindings--part-3.md)*

A Cloud Storage binding gives a Telnyx Edge Function a pre-authenticated handle to one of your buckets. Declared in `func.toml` and exposed as `env.<BINDING>`, the typed `CloudStorageBucket` interface lets TypeScript functions read, write, list, and delete objects without holding any S3 access keys.

## `delete(key | keys)`

Remove one object, or many in a single call. Idempotent — deleting a missing key resolves normally.

```ts
// Single key
await env.MY_BUCKET.delete("uploads/logo.png");

// Batch — up to 1000 keys per call
await env.MY_BUCKET.delete(["uploads/a.png", "uploads/b.png", "uploads/c.png"]);
```

Passing an array maps to a single S3 batch delete. Deleting more than 1000 keys splits into 1000-key batches automatically.

## `list(options?)`

Enumerate objects (metadata only — `list` does not return bodies).

```ts
interface CloudStorageListOptions {
  prefix?: string;
  limit?: number;
  cursor?: string;    // from a previous result's `cursor`
  delimiter?: string; // roll up keys sharing a prefix into `delimitedPrefixes`
  include?: Array<"httpMetadata" | "customMetadata">; // opt into per-entry metadata
}

interface CloudStorageListResult {
  objects: CloudStorageObject[];
  delimitedPrefixes: string[];   // "folders" — present when `delimiter` is set
  truncated: boolean;
  cursor?: string;               // present when truncated is true
}
```

```ts
let cursor: string | undefined;
do {
  const page = await env.MY_BUCKET.list({ prefix: "uploads/", limit: 100, cursor });
  for (const obj of page.objects) {
    // obj.key, obj.size, obj.etag, …
  }
  cursor = page.truncated ? page.cursor : undefined;
} while (cursor);
```

When `truncated` is `true`, pass the returned `cursor` back in `list({ cursor })` to fetch the next page.

By default a `list` entry carries only `key`, `size`, `etag`, and `uploaded`. Pass `include` to also populate `httpMetadata` and/or `customMetadata` on each returned object — a heavier listing, so ask for it only when you need it.

```ts
const page = await env.MY_BUCKET.list({ prefix: "uploads/", include: ["httpMetadata", "customMetadata"] });
page.objects[0].httpMetadata?.contentType;   // populated because "httpMetadata" was included
```

### Hierarchical ("folder") listing

Set `delimiter` to `/` to browse one level of a key hierarchy: keys below the current level collapse into `delimitedPrefixes`, and only keys directly at the level appear in `objects`.

```ts
const page = await env.MY_BUCKET.list({ prefix: "uploads/", delimiter: "/" });
page.delimitedPrefixes;  // e.g. ["uploads/2026/", "uploads/logos/"] — the "subfolders"
page.objects;            // keys that live directly under "uploads/"
```

## Multipart upload

Upload a large object in parts from inside a function — for objects past the Edge Compute request/response size cap, or for parallel/resumable uploads. Available on **US and APAC (`ap-southeast-1`)** region buckets.

```ts
interface CloudStorageMultipartUpload {
  key: string;
  uploadId: string;
  uploadPart(partNumber: number, body: CloudStoragePutBody, options?: CloudStoragePutOptions): Promise<CloudStorageUploadedPart>;
  complete(parts: CloudStorageUploadedPart[]): Promise<CloudStorageObject>;
  abort(): Promise<void>;
}

interface CloudStorageUploadedPart {
  partNumber: number;
  etag: string;
}
```

```ts
const upload = await env.MY_BUCKET.createMultipartUpload("videos/large.mp4", {
  httpMetadata: { contentType: "video/mp4" },
});

const parts: CloudStorageUploadedPart[] = [];
parts.push(await upload.uploadPart(1, firstChunk));   // every part except the last must be ≥ 5 MiB
parts.push(await upload.uploadPart(2, lastChunk));

const object = await upload.complete(parts);          // returns the assembled CloudStorageObject
// object.etag is the multipart form "<md5>-<partCount>", e.g. "…8a0-2"
```

- **`createMultipartUpload(key, options?)`** starts the upload and returns a handle. `options` takes the same `httpMetadata` / `customMetadata` / `ssecKey` as `put`.
- **`uploadPart(partNumber, body, options?)`** uploads one part and returns its `{ partNumber, etag }`. Parts are numbered from 1; every part except the last must be at least 5 MiB.
- **`complete(parts)`** assembles the object. You may pass the parts in any order — they are sorted by `partNumber`.
- **`abort()`** discards an in-progress upload and its parts.
- **`resumeMultipartUpload(key, uploadId, options?)`** rebuilds a handle for an existing `uploadId` (no server round-trip) so you can upload more parts or `complete()`/`abort()` from a later invocation.

```ts
// Resume an upload started elsewhere, then finish it
const resumed = env.MY_BUCKET.resumeMultipartUpload("videos/large.mp4", uploadId);
parts.push(await resumed.uploadPart(3, moreBytes));
await resumed.complete(parts);
```

## Server-side encryption (SSE-C)

Pass `ssecKey` on `get`, `put`, and multipart calls to encrypt with a customer-provided key. The key is a 256-bit (32-byte) AES key, given as an `ArrayBuffer` or a 64-character hex `string`. Supply the **same key** on read that you used on write; the object exposes `ssecKeyMd5` (hex) so you can identify which key encrypted it. SSE-C applies to **US and APAC (`ap-southeast-1`)** region buckets.

```ts
const key = crypto.getRandomValues(new Uint8Array(32)).buffer;   // keep this safe — it's not stored for you

await env.MY_BUCKET.put("secret.bin", bytes, { ssecKey: key });
const obj = await env.MY_BUCKET.get("secret.bin", { ssecKey: key });
// obj?.ssecKeyMd5 identifies the key; reading without the matching key fails
```

## Object types

```ts
interface CloudStorageObject {
  key: string;
  size?: number;
  etag?: string;                              // unquoted (e.g. "5eb63bbbe0…")
  httpEtag?: string;                          // quoted, header-ready (e.g. "\"5eb63bbbe0…\"")
  uploaded?: Date;
  version?: string;                           // object version id (when bucket versioning is enabled)
  httpMetadata?: CloudStorageHTTPMetadata;
  customMetadata?: Record<string, string>;    // keys lower-cased on read
  ssecKeyMd5?: string;                        // hex MD5 of the SSE-C key, when the object is SSE-C encrypted
  range?: CloudStorageRange;                  // the requested range, echoed on a ranged get
  writeHttpMetadata(headers: Headers): void;  // copy the stored Content-Type / Cache-Control / … onto a Headers
}

interface CloudStorageObjectBody extends CloudStorageObject {
  body: ReadableStream;
  bodyUsed: boolean;                          // true once the body has been consumed
  arrayBuffer(): Promise<ArrayBuffer>;
  text(): Promise<string>;
  json(): Promise<unknown>;
  blob(): Promise<Blob>;
}

interface CloudStorageHTTPMetadata {
  contentType?: string;
  cacheControl?: string;
  contentLanguage?: string;
  contentDisposition?: string;
  contentEncoding?: string;
  cacheExpiry?: Date;
}
```

`head` and each `list` entry populate `size` and `uploaded`; `put`'s result does not. The body readers on `CloudStorageObjectBody` consume the stream once — call a single one per `get`, and `bodyUsed` flips to `true` once you do. `writeHttpMetadata` is handy for serving an object straight back out of a function with its stored headers:

```ts
const obj = await env.MY_BUCKET.get("uploads/logo.png");
if (obj && "body" in obj) {
  const headers = new Headers();
  obj.writeHttpMetadata(headers);            // sets Content-Type, Cache-Control, …
  return new Response(obj.body, { headers });
}
```
