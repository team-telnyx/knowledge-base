---
title: Edge Compute Quickstart
summary: 'Walks through deploying a first function on Telnyx Edge Compute end-to-end:
  installing the `telnyx-edge` CLI, authenticating, scaffolding a project in TypeScript,
  JavaScript, Go, Python, or Java, shipping it, and verifying the live URL with `curl`.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/quickstart/index
updated_at: 2026-08-05T13:41:18Z
---

# Edge Compute Quickstart

Walks through deploying a first function on Telnyx Edge Compute end-to-end: installing the `telnyx-edge` CLI, authenticating, scaffolding a project in TypeScript, JavaScript, Go, Python, or Java, shipping it, and verifying the live URL with `curl`.

## Overview

A function on Telnyx Edge Compute is a container running your own HTTP server on Telnyx infrastructure, reachable at a public URL. This quickstart covers the full path from a clean machine to a deployed, callable function: install the CLI, authenticate, scaffold, ship, and prove it with `curl`.

The code steps below are shown for every supported language — pick a tab. TypeScript is the default and the only one with the typed binding SDK today; the rest are fully supported for plain HTTP.

## Prerequisites

- A Telnyx account — [sign up](https://telnyx.com/sign-up) if you don't have one.
- The toolchain for your language: Node.js ≥ 18 (TypeScript/JavaScript), Go, Python 3, or Java with Maven.

## Install the CLI

The `telnyx-edge` CLI ships as binaries on the [GitHub releases page](https://github.com/team-telnyx/edge-compute/releases). Assets are version-stamped, and each tarball extracts into a versioned directory containing the binary.

Linux (amd64):

```
curl -fsSL https://github.com/team-telnyx/edge-compute/releases/download/v0.2.3/telnyx-edge-v0.2.3-linux-amd64.tar.gz | tar xz
sudo mv telnyx-edge-v0.2.3-linux-amd64/telnyx-edge /usr/local/bin/
```

macOS (Apple silicon):

```
curl -fsSL https://github.com/team-telnyx/edge-compute/releases/download/v0.2.3/telnyx-edge-v0.2.3-macos-arm64.tar.gz | tar xz
sudo mv telnyx-edge-v0.2.3-macos-arm64/telnyx-edge /usr/local/bin/
```

For Intel Macs use the `macos-amd64` asset; Windows zips are on the same releases page. Verify the install:

```
telnyx-edge --version
```

## Authenticate

Authenticate before creating a function — `new-func` registers the function with the platform, which requires credentials.

```
# Interactive: opens your browser for OAuth
telnyx-edge auth login

# Or headless (CI, containers): set an API key directly
telnyx-edge auth api-key set <YOUR_API_KEY>

# Confirm
telnyx-edge auth status
```

Credentials persist to `~/.telnyx-edge/config.toml`. The CLI does not read a `TELNYX_API_KEY` environment variable — in CI, run `auth api-key set` as a setup step.

## Create a function

`new-func` creates the function server-side, writes the assigned UUID into `func.toml`, and scaffolds a working project. Pass `-l` to pick the language:

TypeScript:

```
telnyx-edge new-func -l ts -n hello
cd hello
npm install
```

JavaScript:

```
telnyx-edge new-func -l js -n hello
cd hello
npm install
```

Go:

```
telnyx-edge new-func -l go -n hello
cd hello
```

Python:

```
telnyx-edge new-func -l python -n hello
cd hello
```

Java (Quarkus Funqy):

```
telnyx-edge new-func -l quarkus -n hello
cd hello
```

Every scaffold contains a `func.toml` that ties the directory to the registered function:

```
[edge_compute]
func_id = "7819cf01-39a8-400e-9bce-3d792ffa4017"  # assigned by new-func
func_name = "hello"
```

The entrypoint file and its contract differ by language — TypeScript and JavaScript run their own server; Go, Python, and Java hand you a handler and run the server for you. Here is the scaffolded entrypoint, condensed to a health check plus a default JSON response:

`index.ts` / `index.js`:

```
import * as http from "node:http";

const server = http.createServer((req, res) => {
  // Liveness/readiness probes — answer first
  if (req.url === "/health" || req.url?.startsWith("/health/")) {
    res.writeHead(200); res.end(); return;
  }
  res.writeHead(200, { "Content-Type": "application/json" });
  res.end(JSON.stringify({ message: "Hello from Telnyx Edge Compute!" }));
});

server.listen(process.env.PORT || 8080);
```

`handler.go`:

```
package function

import (
	"encoding/json"
	"net/http"
)

// The platform runs the server and calls Handle per request.
func Handle(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(map[string]string{
		"message": "Hello from Telnyx Edge Compute!",
	})
}
```

`function/func.py`:

```
import json

def new():
    return Function()

class Function:
    async def handle(self, scope, receive, send):
        body = json.dumps({"message": "Hello from Telnyx Edge Compute!"}).encode()
        await send({"type": "http.response.start", "status": 200,
                    "headers": [b"content-type", b"application/json"](b-content-type-b-application-json.md)})
        await send({"type": "http.response.body", "body": body})
```

`src/main/java/functions/Function.java`:

```
package functions;

import io.quarkus.funqy.Funq;

public class Function {
    @Funq
    public Output function(Input input) {
        return new Output("Hello from Telnyx Edge Compute!");
    }
}
```

These are trimmed for the quickstart. See [HTTP handler](http-handler.md) for the full scaffold for each language, the exact entrypoint contract, and how request bodies and health probes work.

## Ship

```
telnyx-edge ship
```

`ship` uploads the project, builds it, deploys it, and monitors the rollout (default timeout 5 minutes; `--timeout` to change). The output ends with the live URL:

```
✅ Func 'hello' is now deployed!

📡 Your function is live at:
   https://hello-<org>.telnyxcompute.com

💡 Test your function:
   curl https://hello-<org>.telnyxcompute.com
```

Every function gets a URL of the form `{func-name}-{func-id-prefix}.telnyxcompute.com` — see [Routes & Domains](routes-domains.md).

## Call it

Use the URL `ship` printed. Every scaffold answers a `GET` with the same default response:

```
curl -sS https://hello-<org>.telnyxcompute.com
# → {"message":"Hello from Telnyx Edge Compute!"}
```

Sending request bodies differs by contract — the TypeScript, JavaScript, Go, and Python scaffolds read the raw body, while the Java (Funqy) scaffold is JSON-in, JSON-out. See [HTTP handler](http-handler.md) for each.

The function is live. Iterate by editing the entrypoint and running `telnyx-edge ship` again — each successful ship creates an immutable revision you can [roll back to](versions.md).

## Next steps

- [Bindings](bindings.md) — pre-authenticated Telnyx client, secrets, and KV on `env`.
- [KV quick start](kv-quick-start.md) — persist data across requests from your function.
