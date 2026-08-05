---
title: Runtime APIs
summary: 'Edge Compute functions are real Linux containers running native language
  runtimes (Node.js, Go, Python, Java/Quarkus). The platform adds a small, explicit
  layer on top: an execution environment with cold starts, warm reuse, and a request
  budget; a per-language entrypoint contract for handling HTTP requests; and bindings
  that inject credentials for the Telnyx API, secrets, KV, object storage, SQL databases,
  and stateful actors.'
sources:
- url: https://developers.telnyx.com/docs/edge-compute/runtime/bindings
- url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
- url: https://developers.telnyx.com/docs/edge-compute/runtime/http-handler
- url: https://developers.telnyx.com/docs/edge-compute/runtime/index
updated_at: 2026-08-05T13:41:58Z
---

# Runtime APIs

*Part 2 of 3 — see also: [Part 1](runtime-apis--part-1.md), [Part 3](runtime-apis--part-3.md)*

Edge Compute functions are real Linux containers running native language runtimes (Node.js, Go, Python, Java/Quarkus). The platform adds a small, explicit layer on top: an execution environment with cold starts, warm reuse, and a request budget; a per-language entrypoint contract for handling HTTP requests; and bindings that inject credentials for the Telnyx API, secrets, KV, object storage, SQL databases, and stateful actors.

## HTTP handler

HTTP is the only way a function is invoked. Requests arrive at `https://<func-name>-<func-id-prefix>.telnyxcompute.com` (see [Routing](routing.md)) and are handed to your entrypoint — but what "your entrypoint" means differs by language. In TypeScript and JavaScript you own and run the HTTP server (the CLI scaffolds a working one); in Go, Python, and Java the server is run for you and your code is called per request.

`telnyx-edge new-func -l <language>` generates a working entrypoint for each language. The code below is that scaffold — start from it rather than a blank file.

### The contract at a glance

| Language | File | You implement | Server owned by | Health probes |
| --- | --- | --- | --- | --- |
| TypeScript / JavaScript | `index.ts` / `index.js` (project root) | An HTTP server on `process.env.PORT \|\| 8080` | You | You — return `200` for `/health` and paths under it |
| Go | `handler.go` | `func Handle(w http.ResponseWriter, r *http.Request)` in `package function` | Platform | Handled for you — no health route in your code |
| Python | `function/func.py` | `new()` factory returning an object with `async def handle(self, scope, receive, send)` | Platform | Platform — probes never reach `handle()` |
| Java | `src/main/java/functions/Function.java` | A method annotated `@Funq` (Quarkus Funqy) | Quarkus | SmallRye Health at `/health/*`, pre-configured |

### TypeScript / JavaScript

You own the server. There is no framework-provided `handler(request)` entrypoint and no `Response` object to return — your function is a container running a plain `node:http` server (or any server framework you install). Two things are contractual:

- **Listen on `process.env.PORT`**, falling back to `8080`.
- **Answer `/health`** (and paths under it) with a `200`. The platform's liveness and readiness probes hit it — a function that doesn't answer isn't routed traffic and can be restarted. Keep the probe path fast: respond before any other work.

`index.ts` lives at the project root, next to `func.toml` — not in `src/`. The scaffold, lightly condensed:

```ts
import * as http from 'node:http';

interface ResponseData {
  message: string;
  data?: any;
}

const server = http.createServer(async (req: http.IncomingMessage, res: http.ServerResponse) => {
  // Liveness/readiness probes — answer before any other work
  if (req.url === '/health' || req.url?.startsWith('/health/')) { res.writeHead(200); res.end(); return; }

  const responseData: ResponseData = {
    message: 'Hello from Telnyx Edge Compute!'
  };

  // POST: read and echo the request body
  if (req.method === 'POST') {
    let body = '';

    req.on('data', (chunk: Buffer) => {
      body += chunk.toString();
    });

    req.on('end', () => {
      if (body) {
        try {
          responseData.data = JSON.parse(body);
        } catch (error) {
          responseData.data = body;   // not JSON — echo as text
        }
      }

      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(responseData));
    });
  } else {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(responseData));
  }
});

const port = process.env.PORT || 8080;
server.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
```

The JavaScript scaffold (`-l js`) is the same file minus type annotations, at `index.js` (same project-root location). Request bodies arrive as `data` events carrying `Buffer` chunks. The scaffold accumulates them as a string, which is fine for text and JSON — for binary bodies collect the buffers instead (`chunks.push(chunk)` then `Buffer.concat(chunks)`), because `toString()` corrupts non-UTF-8 bytes.

### Go

The platform owns the server. You write an ordinary `net/http` handler — exported as `Handle`, in `package function`, with no `main()`. The platform binds the port and routes requests to `Handle`; the scaffold defines no health route and doesn't need one. `handler.go` — the scaffold, lightly condensed:

```go
package function

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
)

// Response represents the function response structure
type Response struct {
	Message string      `json:"message"`
	Data    interface{} `json:"data,omitempty"`
}

// Handle answers every HTTP request routed to the function.
func Handle(w http.ResponseWriter, r *http.Request) {
	log.Printf("Serving a new request: %v > %v @ %v", r.Host, r.Method, r.URL.Path)

	w.Header().Set("Content-Type", "application/json")

	response := Response{
		Message: "Hello from Telnyx Edge Compute!",
	}

	// POST: read and echo the request body
	if r.Method == "POST" {
		body, err := io.ReadAll(r.Body)
		if err != nil {
			log.Printf("Error reading request body: %v", err)
		} else if len(body) > 0 {
			var jsonData interface{}
			if err := json.Unmarshal(body, &jsonData); err == nil {
				response.Data = jsonData
			} else {
				response.Data = string(body) // not JSON — echo as text
			}
		}
	}

	responseBytes, err := json.Marshal(response)
	if err != nil {
		http.Error(w, "Internal Server Error", http.StatusInternalServerError)
		return
	}

	w.Write(responseBytes)
}
```

`go.mod` declares `module function` (Go 1.24). Standard `net/http` semantics apply: read the body from `r.Body`, set headers with `w.Header().Set(...)` before the first write.

### Python

The contract is ASGI. Your project is a `function/` package whose `func.py` exposes a module-level `new()` factory; the runtime calls it when an instance starts, keeps the returned object, and dispatches every HTTP request — except liveness and readiness probes, which the platform answers itself — to its `handle` coroutine. There is no `handler(request)` returning a dict, and no `requirements.txt` — dependencies go in `pyproject.toml` (the scaffold uses hatchling). `function/func.py` — the scaffold, trimmed:

```python
import json

def new():
    """Required. Called when an instance starts; the returned object
    receives all requests via its handle() coroutine."""
    return Function()

class Function:
    async def handle(self, scope, receive, send):
        """Called for every HTTP request except liveness/readiness probes."""
        method = scope.get('method', 'GET')

        response_data = {"message": "Hello from Telnyx Edge Compute!"}

        # POST: the body arrives in chunks over the ASGI receive channel
        if method == 'POST':
            body = b''
            while True:
                message = await receive()
                if message['type'] == 'http.request':
                    body += message.get('body', b'')
                    if not message.get('more_body', False):
                        break

            if body:
                try:
                    response_data["data"] = json.loads(body)
                except (json.JSONDecodeError, UnicodeDecodeError):
                    response_data["data"] = body.decode('utf-8', errors='replace')

        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'application/json'],
            ],
        })
        await send({
            'type': 'http.response.body',
            'body': json.dumps(response_data).encode(),
        })

    def start(self, cfg):
        """Optional. Called when an instance starts (scale-up, update).
        cfg is a dict of all environmental configuration."""

    def stop(self):
        """Optional. Called when an instance stops (scale-down, update,
        manual cancel)."""
```

`function/__init__.py` re-exports the factory: `from .func import new`.

| Hook | Required | Called when |
| --- | --- | --- |
| `new()` | Yes | Instance start — returns the object that handles requests |
| `handle(self, scope, receive, send)` | Yes | Every request (async, ASGI) |
| `start(cfg)` | No | Instance start — `cfg` is a dict of all environmental configuration |
| `stop()` | No | Instance stop — scale-down, update, or manual cancel |

### Java

Functions are Quarkus Funqy functions: a plain class with a method annotated `@Funq` that takes a bean and returns a bean. Quarkus owns the server, deserializes the JSON request body into your input bean, and serializes your return value back to JSON. `src/main/java/functions/Function.java` — the scaffold:

```java
package functions;

import io.quarkus.funqy.Funq;

public class Function {

    @Funq
    public Output function(Input input) {

        String defaultMessage = "Hello from Telnyx Edge Compute!";

        // Null or empty input — return the default message
        if (input == null || input.getMessage() == null || input.getMessage().trim().isEmpty()) {
            return new Output(defaultMessage);
        }

        // Echo back the input message
        return new Output(input.getMessage());
    }

}
```

`Input` and `Output` are plain beans in the same package — a `message` field with a no-arg constructor, getter, and setter. Invocation is JSON in, JSON out:

```bash
curl -s https://demo-quarkus-<func-id-prefix>.telnyxcompute.com \
  -H "Content-Type: application/json" \
  -d '{"message": "hello"}'
# → {"message":"hello"}
```

Two scaffold defaults worth knowing:

- `application.properties` selects the exported method by name: `quarkus.funqy.export=function`. Rename the method, update the property.
- Health endpoints come from SmallRye Health, pre-configured at `/health/liveness` and `/health/readiness` — leave them in place.

Funqy is a typed JSON model: your method sees the deserialized bean, not raw bytes, URL paths, or headers. For raw HTTP semantics — routing on paths, custom headers, binary bodies — use the TypeScript, JavaScript, Go, or Python contract instead.

### Bodies, headers, and binary data

These apply to the raw-HTTP contracts — TypeScript, JavaScript, Go, and Python. Java/Funqy is the exception: it's typed JSON in/out, so raw bodies, binary responses, and custom headers aren't available from a `@Funq` method.

- **Bodies pass through raw, both directions.** There is no base64 envelope and no JSON wrapping between the caller and your code. To serve binary, set the `Content-Type` and write the bytes:

  ```ts
  res.writeHead(200, { "Content-Type": "image/png" });
  res.end(pngBuffer);   // raw bytes — no base64
  ```

- **Headers are yours.** Whatever your server (or `Handle`, or `http.response.start`) sets is what the caller receives. There is no platform header rewriting to work around.
- **Bodies are size-capped.** Request and response body limits are listed in [Limits](limits.md).

### The request budget

A function has **30 seconds** by default to respond, and **60 seconds** at most. Past the budget the request is terminated and the caller gets a `504`. This is a platform limit, not a `func.toml` field — there is no `timeout_seconds` setting. For work that can run long, set your own internal timeout a few seconds under the platform's and return an error or partial result instead of being cut off mid-response. Exact numbers and the other caps — memory, body size, deploy rate — are in [Limits](limits.md).
