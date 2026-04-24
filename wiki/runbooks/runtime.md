---
title: Runtime
summary: The runtime environment and platform APIs available to your edge functions.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/runtime/index
    content_hash: 66351f9ccd85ce0a690fdded3b254fcdd54380e72efcde054c9fd02d8ee40571
updated_at: 2026-04-10T00:00:00Z
---

# Runtime

The runtime environment and platform APIs available to your edge functions.

Edge Compute runs your functions in real Linux containers, giving you access to standard runtime APIs and system calls. Unlike V8 isolate-based platforms, you have a full POSIX environment with native language runtimes.

## Runtime Environment

Your functions run in lightweight containers with:

* **Full language runtimes** — Python 3.11+, Node.js 18+, Go 1.25+, Java 17+ (Quarkus)
* **Standard libraries** — Use native packages and dependencies
* **POSIX APIs** — File I/O, environment variables, process control
* **Network access** — HTTP clients, TCP sockets, DNS resolution

## Platform APIs

Edge Compute provides platform bindings for accessing Telnyx services:

* [Bindings](bindings.md) — Connect to Telnyx APIs (Voice, Messaging, Storage) with auto-injected credentials
* [Execution Model](execution-model.md) — Function lifecycle, cold starts, concurrency

## Accessing Environment

Configuration is injected via environment variables:

### JavaScript

    ```javascript theme={null}
    // Environment variables from func.toml
    const logLevel = process.env.LOG_LEVEL || 'info';
    const apiEndpoint = process.env.API_ENDPOINT;

    // Binding credentials (auto-injected)
    const telnyxKey = process.env.TELNYX_API_KEY;
    ```

### Go

    ```go theme={null}
    package main

    import "os"

    func main() {
        // Environment variables from func.toml
        logLevel := os.Getenv("LOG_LEVEL")
        apiEndpoint := os.Getenv("API_ENDPOINT")

        // Binding credentials (auto-injected)
        telnyxKey := os.Getenv("TELNYX_API_KEY")
    }
    ```

### Python

    ```python theme={null}
    import os

    # Environment variables from func.toml
    log_level = os.environ.get('LOG_LEVEL', 'info')
    api_endpoint = os.environ.get('API_ENDPOINT')

    # Binding credentials (auto-injected)
    telnyx_key = os.environ.get('TELNYX_API_KEY')
    ```

### Java

    ```java theme={null}
    public class Handler {
        // Environment variables from func.toml
        private static final String LOG_LEVEL = System.getenv("LOG_LEVEL");
        private static final String API_ENDPOINT = System.getenv("API_ENDPOINT");

        // Binding credentials (auto-injected)
        private static final String TELNYX_KEY = System.getenv("TELNYX_API_KEY");
    }
    ```

## HTTP Handling

Functions receive HTTP requests and return responses:

### JavaScript

    ```javascript theme={null}
    const express = require('express');
    const app = express();

    app.use(express.json());

    app.all('/', (req, res) => {
        if (req.method === 'POST') {
            return res.json({ received: req.body });
        }

        res.json({ status: 'ok' });
    });

    app.listen(8080);
    ```

### Go

    ```go theme={null}
    package main

    import (
        "encoding/json"
        "net/http"
    )

    func handler(w http.ResponseWriter, r *http.Request) {
        w.Header().Set("Content-Type", "application/json")

        if r.Method == "POST" {
            var data map[string]interface{}
            json.NewDecoder(r.Body).Decode(&data)
            json.NewEncoder(w).Encode(map[string]interface{}{
                "received": data,
            })
            return
        }

        json.NewEncoder(w).Encode(map[string]string{
            "status": "ok",
        })
    }

    func main() {
        http.HandleFunc("/", handler)
        http.ListenAndServe(":8080", nil)
    }
    ```

### Python

    ```python theme={null}
    from flask import Flask, request, jsonify

    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def handler():
        if request.method == 'POST':
            data = request.get_json()
            return jsonify({"received": data})

        return jsonify({"status": "ok"})
    ```

## Networking

Functions can make outbound HTTP requests:

### JavaScript

    ```javascript theme={null}
    async function fetchData() {
        const response = await fetch('https://api.example.com/data');
        return response.json();
    }

    async function postData(payload) {
        const response = await fetch('https://api.example.com/submit', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload)
        });
        return response.status;
    }
    ```

### Go

    ```go theme={null}
    package main

    import (
        "bytes"
        "encoding/json"
        "net/http"
        "time"
    )

    var client = &http.Client{Timeout: 10 * time.Second}

    func fetchData() (map[string]interface{}, error) {
        resp, err := client.Get("https://api.example.com/data")
        if err != nil {
            return nil, err
        }
        defer resp.Body.Close()

        var data map[string]interface{}
        json.NewDecoder(resp.Body).Decode(&data)
        return data, nil
    }
    ```

### Python

    ```python theme={null}
    import requests

    def fetch_data():
        response = requests.get('https://api.example.com/data')
        return response.json()

    def post_data(payload):
        response = requests.post(
            'https://api.example.com/submit',
            json=payload,
            timeout=10
        )
        return response.status_code
    ```

## Next Steps

* [Bindings](bindings.md) — Access Telnyx services from your functions
* [Execution Model](execution-model.md) — Understand lifecycle and performance
* [Configuration](configuration.md) — Set environment variables and secrets
