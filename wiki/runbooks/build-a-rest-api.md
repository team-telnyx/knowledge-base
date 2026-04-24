---
title: Build a REST API
summary: Create a JSON API with routing, validation, and error handling.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/demos/build-a-rest-api
    content_hash: ed6da841abd4bb3301425092f8db1af5e9ccc754969cd4bb5a3341653f339e05
updated_at: 2026-04-10T00:00:00Z
---

# Build a REST API

Create a JSON API with routing, validation, and error handling.

Build a complete REST API with CRUD operations, input validation, and error handling.

**What you'll learn:**

* Routing requests to different handlers
* Parsing JSON request bodies
* Returning proper HTTP status codes
* Error handling patterns

## Prerequisites

* Telnyx account with Edge Compute enabled
* `telnyx-edge` CLI installed

## Step 1: Create the Function

```bash theme={null}
telnyx-edge new-func -l=python -n=my-api
cd my-api
```

## Step 2: Implement the API

Replace `src/main.py`:

```python theme={null}
import json
from urllib.parse import urlparse, parse_qs


## Related Pages

- [REST API](../runbooks/rest-api.md)
