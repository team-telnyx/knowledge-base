---
title: Execution Model
summary: How edge functions are invoked, their lifecycle, and concurrency behavior.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/runtime/execution-model
    content_hash: c1cd1496aec852b47c7915d80767325c833664599254f9fc0e10cea555cab845
updated_at: 2026-04-10T00:00:00Z
---

# Execution Model

How edge functions are invoked, their lifecycle, and concurrency behavior.

Understanding how Edge Compute executes your functions helps you optimize performance and build reliable applications.

## Overview

Edge Compute runs your functions in lightweight Linux containers. When a request arrives:

1. **Routing** — Request is routed to the nearest edge location
2. **Container selection** — An existing warm container handles the request, or a new one starts (cold start)
3. **Execution** — Your function processes the request
4. **Response** — Result is returned to the caller
5. **Keep-alive** — Container stays warm for subsequent requests

## Function Lifecycle

### Cold Start Phase

When a function receives its first request or scales up, a new container initializes:

### JavaScript

    ```javascript theme={null}
    // Global initialization (runs once per container)
    const { Pool } = require('pg');

    // Expensive operations here — only run once
    const pool = new Pool({ connectionString: process.env.DATABASE_URL });
    const cache = {};

    // Function handler (runs per request)
    async function handler(req, res) {
        // Fast path — reuse initialized resources
        const result = await pool.query('SELECT * FROM users');
        res.json(result.rows);
    }

    module.exports = { handler };
    ```

### Go

    ```go theme={null}
    package main

    import (
        "database/sql"
        "encoding/json"
        "log"
        "net/http"
        "os"
    )

    // Global initialization (runs once per container)
    var db *sql.DB

    func init() {
        // Expensive operations here — only run once
        var err error
        db, err = sql.Open("postgres", os.Getenv("DATABASE_URL"))
        if err != nil {
            log.Fatal(err)
        }
    }

    // Function handler (runs per request)
    func handler(w http.ResponseWriter, r *http.Request) {
        // Fast path — reuse initialized resources
        rows, err := db.Query("SELECT * FROM users")
        if err != nil {
            http.Error(w, err.Error(), 500)
            return
        }
        defer rows.Close()

        var users []map[string]interface{}
        cols, _ := rows.Columns()
        for rows.Next() {
            vals := make([]interface{}, len(cols))
            ptrs := make([]interface{}, len(cols))
            for i := range vals {
                ptrs[i] = &vals[i]
            }
            rows.Scan(ptrs...)
            row := make(map[string]interface{})
            for i, col := range cols {
                row[col] = vals[i]
            }
            users = append(users, row)
        }
        json.NewEncoder(w).Encode(users)
    }
    ```

### Python

    ```python theme={null}
    # Global initialization (runs once per container)
    import json
    from database import create_pool

    # Expensive operations here — only run once
    db_pool = create_pool()
    cache = {}

    # Function handler (runs per request)
    async def handler(request):
        # Fast path — reuse initialized resources
        data = await request.json()
        result = await db_pool.query('SELECT * FROM users')
        return Response(json.dumps(result))
    ```

**Cold start timeline:**

1. Container image pulled (cached at edge)
2. Runtime initializes (Python/Go/Node/Java)
3. Global code executes (imports, connections)
4. First request handled

### Warm Execution

Subsequent requests reuse the same container instance:

### JavaScript

    ```javascript theme={null}
    // Global variables persist between requests
    const axios = require('axios');

    const client = axios.create({
        timeout: 10000
    });

    async function handler(req, res) {
        // Fast execution — resources already initialized
        console.log(`Request: ${req.method} ${req.path}`);

        const resp = await client.get('https://api.example.com/data');
        res.json(resp.data);
    }
    ```

### Go

    ```go theme={null}
    // Global variables persist between requests
    var (
        client *http.Client
        logger *log.Logger
    )

    func init() {
        // One-time initialization
        client = &http.Client{Timeout: 10 * time.Second}
        logger = log.New(os.Stdout, "[EDGE] ", log.LstdFlags)
    }

    func handler(w http.ResponseWriter, r *http.Request) {
        // Fast execution — resources already initialized
        logger.Printf("Request: %s %s", r.Method, r.URL.Path)

        resp, err := client.Get("https://api.example.com/data")
        // ...
    }
    ```

### Python

    ```python theme={null}
    import httpx

    # Global variables persist between requests
    client = httpx.Client(timeout=10.0)

    def handler(request):
        # Fast execution — resources already initialized
        print(f"Request: {request.method} {request.path}")

        resp = client.get("https://api.example.com/data")
        return resp.json()
    ```

### Container Recycling

Containers are recycled when:

* Idle for extended periods (to free resources)
* Memory limits approached
* New deployment shipped
* Platform scaling decisions

> **Note:** Don't rely on container persistence for critical state. Use [KV](https://developers.telnyx.com/docs/edge-compute/kv) or external storage for data that must survive restarts.

## Cold Start Optimization

Minimize cold start latency with these patterns:

### 1. Lazy Initialization

Defer expensive operations until needed:

### JavaScript

    ```javascript theme={null}
    // Bad — always initializes
    const mlModel = loadModel('large_model.pkl'); // 2 seconds

    async function handler(req, res) {
        const result = mlModel.predict(req.body);
        res.json(result);
    }
    ```

    ```javascript theme={null}
    // Good — only loads when needed
    let mlModel = null;

    function getModel() {
        if (!mlModel) {
            mlModel = loadModel('large_model.pkl');
        }
        return mlModel;
    }

    async function handler(req, res) {
        if (req.path === '/predict') {
            const result = getModel().predict(req.body);
            return res.json(result);
        }
        res.json({ status: 'ok' });
    }
    ```

### Go

    ```go theme={null}
    // Bad — always initializes
    var mlModel = loadModel("large_model.pkl") // 2 seconds

    func handler(w http.ResponseWriter, r *http.Request) {
        result := mlModel.Predict(r.Body)
        json.NewEncoder(w).Encode(result)
    }
    ```

    ```go theme={null}
    // Good — only loads when needed
    var (
        mlModel *Model
        modelOnce sync.Once
    )

    func getModel() *Model {
        modelOnce.Do(func() {
            mlModel = loadModel("large_model.pkl")
        })
        return mlModel
    }

    func handler(w http.ResponseWriter, r *http.Request) {
        if r.URL.Path == "/predict" {
            result := getModel().Predict(r.Body)
            json.NewEncoder(w).Encode(result)
            return
        }
        json.NewEncoder(w).Encode(map[string]string{"status": "ok"})
    }
    ```

### Python

    ```python theme={null}
    # Bad — always initializes
    ml_model = load_model('large_model.pkl')  # 2 seconds

    def handler(request):
        return ml_model.predict(request.data)
    ```

    ```python theme={null}
    # Good — only loads when needed
    _ml_model = None

    def get_model():
        global _ml_model
        if _ml_model is None:
            _ml_model = load_model('large_model.pkl')
        return _ml_model

    def handler(request):
        if request.path == '/predict':
            return get_model().predict(request.data)
        return {"status": "ok"}
    ```

### 2. Minimize Dependencies

### JavaScript

    ```javascript theme={null}
    // Bad — imports everything
    const _ = require('lodash');
    const moment = require('moment');

    // Good — import only what you need
    const pick = require('lodash/pick');
    // Or use native: Object.fromEntries, Date
    ```

### Go

    ```go theme={null}
    // Bad — imports everything
    import (
        "github.com/heavy/ml-library"
        "github.com/huge/data-processing"
    )

    // Good — import only what you need
    import (
        "encoding/json"
        "net/http"
    )
    ```

### Python

    ```python theme={null}
    # Bad — imports everything
    import pandas as pd
    import numpy as np
    import tensorflow as tf

    # Good — import only what you need
    from json import loads, dumps
    ```

### 3. Connection Pooling

### JavaScript

    ```javascript theme={null}
    // Initialize pool globally
    const { Pool } = require('pg');

    const pool = new Pool({
        connectionString: process.env.DATABASE_URL,
        max: 10,
        idleTimeoutMillis: 30000
    });

    async function handler(req, res) {
        const client = await pool.connect();
        try {
            const result = await client.query('SELECT * FROM users');
            res.json(result.rows);
        } finally {
            client.release();
        }
    }
    ```

### Go

    ```go theme={null}
    // Initialize pool globally
    var db *sql.DB

    func init() {
        var err error
        db, err = sql.Open("postgres", os.Getenv("DATABASE_URL"))
        if err != nil {
            log.Fatal(err)
        }
        db.SetMaxOpenConns(10)
        db.SetMaxIdleConns(5)
    }

    func handler(w http.ResponseWriter, r *http.Request) {
        rows, err := db.Query("SELECT * FROM users")
        if err != nil {
            http.Error(w, err.Error(), 500)
            return
        }
        defer rows.Close()
        // ...
    }
    ```

### Python

    ```python theme={null}
    # Initialize pool globally
    from sqlalchemy import create_engine
    from sqlalchemy.pool import QueuePool

    engine = create_engine(
        DATABASE_URL,
        poolclass=QueuePool,
        pool_size=5,
        max_overflow=10
    )

    def handler(request):
        with engine.connect() as conn:
            result = conn.execute("SELECT * FROM users")
            return list(result)
    ```

## Concurrency

Each container handles **one request at a time** by default. The platform automatically scales containers based on traffic:

```
Traffic: 100 requests/second
         ↓
Platform scales to ~100 containers
         ↓
Each container handles ~1 req/sec
```

### Scaling Behavior

| Traffic Pattern | Platform Response                         |
| --------------- | ----------------------------------------- |
| Traffic spike   | New containers start (cold starts)        |
| Sustained load  | Containers stay warm                      |
| Traffic drops   | Containers gradually recycle              |
| Zero traffic    | All containers recycle after idle timeout |

## Request Timeouts

Functions have execution time limits:

| Tier     | Timeout                   |
| -------- | ------------------------- |
| Default  | 30 seconds                |
| Extended | 60 seconds (configurable) |

Handle timeouts gracefully:

### JavaScript

    ```javascript theme={null}
    async function handler(req, res) {
        // Set timeout for 25 seconds (5 sec buffer before platform timeout)
        const timeout = new Promise((_, reject) => 
            setTimeout(() => reject(new Error('Timeout')), 25000)
        );

        try {
            const result = await Promise.race([
                longRunningOperation(),
                timeout
            ]);
            res.json(result);
        } catch (err) {
            if (err.message === 'Timeout') {
                res.json({ error: 'Operation timed out', partial: getPartialResult() });
            } else {
                throw err;
            }
        }
    }
    ```

### Go

    ```go theme={null}
    func handler(w http.ResponseWriter, r *http.Request) {
        // Create context with timeout (5 sec buffer before platform timeout)
        ctx, cancel := context.WithTimeout(r.Context(), 25*time.Second)
        defer cancel()

        resultCh := make(chan Result, 1)
        go func() {
            resultCh <- longRunningOperation(ctx)
        }()

        select {
        case result := <-resultCh:
            json.NewEncoder(w).Encode(result)
        case <-ctx.Done():
            json.NewEncoder(w).Encode(map[string]string{
                "error": "Operation timed out",
            })
        }
    }
    ```

### Python

    ```python theme={null}
    import signal

    class TimeoutError(Exception):
        pass

    def timeout_handler(signum, frame):
        raise TimeoutError("Function timeout approaching")

    def handler(request):
        # Set alarm for 25 seconds (5 sec buffer before platform timeout)
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(25)

        try:
            result = long_running_operation()
            signal.alarm(0)  # Cancel alarm
            return result
        except TimeoutError:
            return {"error": "Operation timed out", "partial": get_partial_result()}
    ```

## Triggers

Functions can be invoked by:

### HTTP Requests

```toml theme={null}
