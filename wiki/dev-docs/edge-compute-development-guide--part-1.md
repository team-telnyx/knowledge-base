---
title: Edge Compute Development Guide
summary: A comprehensive guide to building, testing, and deploying serverless functions
  on Telnyx Edge Compute — covering local development workflows, step-by-step tutorials
  for common applications, reusable code snippets across multiple languages, production-grade
  reference architectures, and CI/CD deployment pipelines.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/demos/build-a-rest-api
  content_hash: 4a1165b9c15b973912d03e68c9ad878853f5d1c1484320b5749433de86b7ece2
- url: https://developers.telnyx.com/docs/edge-compute/demos/image-resizer
  content_hash: 17c212723566d69208c1ac7e7a72f39d2f466d2caf3358c12cfda36bdc44c58c
- url: https://developers.telnyx.com/docs/edge-compute/demos/index
  content_hash: e56b0f155ab6790479826995204e40f6a392e7c882bddd0ae9b0b1c7da3e9bc4
- url: https://developers.telnyx.com/docs/edge-compute/demos/sms-webhook-handler
  content_hash: e7d1d54e84876ec01362b96b513e8fafd6280af78da4b555e21fe05ec02d6cab
- url: https://developers.telnyx.com/docs/edge-compute/demos/voice-call-router
  content_hash: 657c1832646180e3a0103aeb096ab1263058d5f4679a1fbd8566f64fd08861c2
- url: https://developers.telnyx.com/docs/edge-compute/deploy
  content_hash: cb8da54f43bf1dff1d8eecbf9ba74ea0f082418b3783a70b04cc49a58c616d05
- url: https://developers.telnyx.com/docs/edge-compute/development
  content_hash: 43d9307d3ce0be3c1656163479d4a3245dc3a332b7369a9b5d092a600a1a73dd
- url: https://developers.telnyx.com/docs/edge-compute/examples/index
  content_hash: c0bea1a073c097b2890f57ffbed24fa6d075d278858d435b783b6b07da58d2d5
- url: https://developers.telnyx.com/docs/edge-compute/frameworks-support
  content_hash: 63295d41eb8c8e328b1b5b9e7c134eb572812291ed38b35f60f3db3b9f765266
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/global-api-gateway
  content_hash: 8d771d0d30f21f84f93d5a886f0006e31bc06369abbcd7e8cafe9e0a59b785ab
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/index
  content_hash: d277e2ae0c7db30f2c4869a5abecc838ac50b904c226ffb9182133200beb3276
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/iot-data-ingestion
  content_hash: 60c36bee09e516502b4cc4e66144e9853c4c6c2bba7d130749b6b3a82dc83596
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/real-time-media-pipeline
  content_hash: 284d7c5b36a8b8665786caa506fc33582e638221746af0745529330423ad7e02
- url: https://developers.telnyx.com/docs/edge-compute/frameworks/telecom-event-processor
  content_hash: 5836ef1c324cc6d59a7e3a203e324549a39fc860065377a28e4e03a90ca2fec8
updated_at: 2026-06-11T10:26:49Z
---

# Edge Compute Development Guide

*Part 1 of 3 — see also: [Part 2](edge-compute-development-guide--part-2.md), [Part 3](edge-compute-development-guide--part-3.md)*

A comprehensive guide to building, testing, and deploying serverless functions on Telnyx Edge Compute — covering local development workflows, step-by-step tutorials for common applications, reusable code snippets across multiple languages, production-grade reference architectures, and CI/CD deployment pipelines.

## Local Development

Develop and test Edge Compute functions on your local machine before deploying. The workflow is: create a function with `telnyx-edge new-func`, develop locally using native language tools, test with your language's test framework, then deploy with `telnyx-edge ship`.

### Project Scaffolding

Create a new function and enter its directory:

```
telnyx-edge new-func -l=python -n=my-function
cd my-function
```

A typical project structure looks like:

```
my-function/
├── func.toml           # Function configuration
├── function/           # Function code (Python)
│   └── __init__.py
├── pyproject.toml      # Dependencies (Python)
├── .env                # Local env vars (gitignored)
├── .gitignore
└── tests/
    └── test_handler.py # Unit tests
```

### Running Locally by Language

**Python** — Python functions use ASGI protocol. Create an ASGI wrapper and run with `uvicorn`:

```
pip install uvicorn
```

```python
# app.py - ASGI wrapper for local testing
from function import new

func = new()
app = func.handle
```

```
uvicorn app:app --port 8080
```

Alternatively, write a test script that directly invokes the handler via the ASGI interface.

**Go** — The scaffolded Go function uses the `function` package. For local HTTP testing, create a temporary `main.go`:

```go
// +build ignore

package main

import (
    "net/http"
    "example.com/hello-world/function"
)

func main() {
    http.HandleFunc("/", function.Handle)
    http.ListenAndServe(":8080", nil)
}
```

**Java (Quarkus)** — Use Quarkus dev mode or standard Maven testing:

```
./mvnw test
```

**JavaScript** — Use `telnyx-edge dev` to run a local dev server:

```
telnyx-edge dev
```

### Environment Variables and Secrets

During local development, set environment variables in your shell or a `.env` file:

```
export LOG_LEVEL=debug
export API_URL=https://api.example.com
```

Or use a `.env` file (add it to `.gitignore`). For secrets, mock them with environment variables locally and set real values with `telnyx-edge secrets add` for production:

```
telnyx-edge secrets add TELNYX_API_KEY "your-api-key-from-portal"
telnyx-edge secrets add TELNYX_PHONE_NUMBER "+15551234567"
```

Secrets are injected as environment variables at runtime but stored encrypted.

### Unit Testing

Write unit tests using your language's test framework:

- **Go**: `go test ./...` with `net/http/httptest`
- **Python**: `pytest tests/` with `pytest-asyncio` for ASGI handlers
- **Java**: `./mvnw test` with `@QuarkusTest`
- **JavaScript**: npm test with your preferred runner

### Testing with curl

Once your local server is running:

```
curl http://localhost:8080/
curl -X POST http://localhost:8080/api/data \
  -H "Content-Type: application/json" \
  -d '{"key": "value"}'
curl http://localhost:8080/api/protected \
  -H "Authorization: Bearer test-token"
```

### Differences from Production

| Feature | Local | Production |
|---|---|---|
| **Network** | localhost | Global edge network |
| **Secrets** | Environment variables | Encrypted storage |
| **Bindings** | Mocked/simulated | Connected to services |
| **Cold starts** | N/A | Container initialization |
| **Resource limits** | Your machine | Platform limits |

Keep parity by using the same language version, matching dependency versions, and testing with production-like request payloads.

## Tutorials

Step-by-step guides that walk through complete projects from creation to deployment.

### Build a REST API

**Time:** 15 min · **Level:** Beginner

Create a JSON API with routing, validation, and error handling. Scaffolds a Python function that implements CRUD operations against in-memory storage (use KV for persistence):

```
telnyx-edge new-func -l=python -n=my-api
cd my-api
```

The handler routes by path and method (`GET /items`, `POST /items`, `GET /items/{id}`, `DELETE /items/{id}`), parses JSON bodies with validation, and returns proper HTTP status codes. Test locally with `telnyx-edge dev` and curl:

```
curl -X POST http://localhost:8787/items \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Item"}'
curl http://localhost:8787/items
curl http://localhost:8787/items/1
curl -X DELETE http://localhost:8787/items/1
```

Deploy with `telnyx-edge ship`. The API is live at `https://my-api-{orgId}.telnyxcompute.com`.

### SMS Webhook Handler

**Time:** 20 min · **Level:** Beginner

Process incoming SMS messages and respond automatically based on keywords. Requires a Telnyx account with a phone number configured for SMS.

```
telnyx-edge new-func -l=javascript -n=sms-handler
cd sms-handler
```

The handler verifies POST requests, parses Telnyx webhook payloads for `message.received` events, matches keywords (`help`, `hours`, `location`, `status`), and sends replies via the Telnyx Messaging API. After deploying, configure the webhook URL in the Telnyx Portal under **Messaging → Phone Numbers**.

### Voice Call Router

**Time:** 25 min · **Level:** Intermediate

Route incoming calls based on time of day, caller location, or custom logic. Uses `pytz` for timezone-aware routing and generates TeXML responses.

```
telnyx-edge new-func -l=python -n=call-router
cd call-router
```

Business-hours logic routes calls to the main office during 9am–5pm EST and to after-hours support otherwise. After deploying, configure the Telnyx number to use this function as the TeXML webhook.

### Image Resizer

**Time:** 20 min · **Level:** Intermediate

Resize and optimize images on-the-fly based on URL parameters. Uses `pillow` and `httpx` for fetching and processing.

```
telnyx-edge new-func -l=python -n=image-resizer
cd image-resizer
```

Accepts query parameters `url` (required), `w` (width), `h` (height), and `q` (quality, default 85). Supports aspect-ratio-preserving resize. Returns JPEG output with a `Cache-Control: public, max-age=86400` header.

Test after deploying:

```
https://image-resizer-{orgId}.telnyxcompute.com/?url=https://example.com/photo.jpg&w=400&q=80
```

### Upcoming Tutorials

- **Authentication Middleware** — Add JWT validation to protect APIs
- **Rate Limiter** — Implement rate limiting with sliding windows
- **A/B Testing** — Route traffic between experiment variants
- **Webhook Validator** — Verify signatures from third-party services
