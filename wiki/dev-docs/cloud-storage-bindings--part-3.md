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

*Part 3 of 3 — see also: [Part 1](cloud-storage-bindings--part-1.md), [Part 2](cloud-storage-bindings--part-2.md)*

A Cloud Storage binding gives a Telnyx Edge Function a pre-authenticated handle to one of your buckets. Declared in `func.toml` and exposed as `env.<BINDING>`, the typed `CloudStorageBucket` interface lets TypeScript functions read, write, list, and delete objects without holding any S3 access keys.

## End-to-end example: a file API

The following TypeScript function exposes a small file API backed by a Cloud Storage bucket binding (`env.ASSETS`): `PUT`, `GET`, and `DELETE` an object by key, and list objects by prefix.

```ts
// index.ts
import * as http from "node:http";
import { env } from "@telnyx/edge-runtime";

// A small file API backed by a Cloud Storage bucket binding (env.ASSETS):
//   PUT    /files/<key>   store the request body as an object
//   GET    /files/<key>   download an object
//   GET    /files         list objects (optional ?prefix=)
//   DELETE /files/<key>   delete an object
const bucket = env.ASSETS;

function sendJson(res: http.ServerResponse, status: number, body: unknown) {
  res.writeHead(status, { "content-type": "application/json" });
  res.end(JSON.stringify(body));
}

async function readBody(req: http.IncomingMessage): Promise<Buffer> {
  const chunks: Buffer[] = [];
  for await (const chunk of req) chunks.push(chunk as Buffer);
  return Buffer.concat(chunks);
}

const server = http.createServer(async (req, res) => {
  // Health probes must stay unauthenticated
  if (req.url === "/health" || req.url?.startsWith("/health/")) {
    res.writeHead(200);
    res.end();
    return;
  }

  const url = new URL(req.url ?? "/", "http://localhost");
  const isCollection = url.pathname === "/files" || url.pathname === "/files/";
  const key = decodeURIComponent(url.pathname.replace(/^\/files\//, ""));

  try {
    // List: GET /files?prefix=
    if (req.method === "GET" && isCollection) {
      const { objects, truncated, cursor } = await bucket.list({
        prefix: url.searchParams.get("prefix") ?? undefined,
        limit: 100,
      });
      return sendJson(res, 200, {
        objects: objects.map((o) => ({ key: o.key, size: o.size, uploaded: o.uploaded })),
        truncated,
        cursor,
      });
    }

    // Upload: PUT /files/<key>
    if (req.method === "PUT" && key) {
      const body = await readBody(req);
      const put = await bucket.put(key, new Uint8Array(body), {
        httpMetadata: { contentType: req.headers["content-type"] ?? "application/octet-stream" },
      });
      return sendJson(res, 200, { key: put?.key, etag: put?.etag });
    }

    // Download: GET /files/<key>
    if (req.method === "GET" && key) {
      const obj = await bucket.get(key);
      if (obj === null) return sendJson(res, 404, { error: "not found" });
      const bytes = Buffer.from(await obj.arrayBuffer());
      res.writeHead(200, {
        "content-type": obj.httpMetadata?.contentType ?? "application/octet-stream",
        "content-length": String(bytes.byteLength),
      });
      res.end(bytes);
      return;
    }

    // Delete: DELETE /files/<key>  (idempotent)
    if (req.method === "DELETE" && key) {
      await bucket.delete(key);
      res.writeHead(204);
      res.end();
      return;
    }

    sendJson(res, 405, { error: "method not allowed" });
  } catch (err: any) {
    sendJson(res, 500, { error: err?.message ?? "internal error" });
  }
});

server.listen(Number(process.env.PORT ?? 8080), () => console.log("file-api up"));
```

Scaffold and ship the function:

```bash
telnyx-edge new-func --language ts --name file-api
cd file-api
telnyx-edge ship
```

When the deploy finishes, get the function's invoke URL:

```bash
telnyx-edge list   # shows STATUS and the INVOKE URL for file-api
```

Try it (with `URL` set to your function's invoke URL):

```bash
# Upload an object
curl -X PUT "$URL/files/hello.txt" -H "content-type: text/plain" --data "hello from the edge"
# → {"key":"hello.txt","etag":"11c9dad6fdb6ae2efe36b9c7aef39031"}

# Download it back
curl "$URL/files/hello.txt"
# → hello from the edge

# List objects
curl "$URL/files"
# → {"objects":[{"key":"hello.txt","size":19,"uploaded":"2026-07-04T…Z"}],"truncated":false}

# Delete it (idempotent — 204 whether or not it existed)
curl -i -X DELETE "$URL/files/hello.txt"
# → HTTP/1.1 204 No Content
```

## Beyond the basics

The same binding also supports **ranged and conditional reads**, **batch delete**, **hierarchical (folder) listing**, **multipart uploads** for objects past the request/response size cap, and **SSE-C** customer-key encryption — all on `env.<BINDING>`. Ranged and conditional reads, batch delete, hierarchical listing, SSE-C, and the `version` / `writeHttpMetadata` object fields need **≥ 0.4.0**; multipart uploads need **≥ 0.5.0**.

## Related

- [Bindings overview](bindings-overview.md) — how bindings work across Telnyx API, Secrets, KV, and Cloud Storage
- [S3-compatible quick start](s3-compatible-quick-start.md) — the same buckets over HTTP
- [S3-compatible API reference](https://developers.telnyx.com/docs/cloud-storage/api-endpoints) — the same buckets over HTTP
