---
title: Environment Variables
summary: Define and access environment variables in Edge Compute functions.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
    content_hash: 58fdc4f9839447c54961237b4023527882f12fb2382f09fd1fa1251b7a6153f6
updated_at: 2026-04-10T00:00:00Z
---

# Environment Variables

Define and access environment variables in Edge Compute functions.

Environment variables allow you to configure your Edge Compute functions without modifying code. They're ideal for non-sensitive configuration values like API endpoints, feature flags, and performance settings that you want to manage alongside your function code.

## Overview

Environment variables in Edge Compute are:

* **Declared in configuration** — Defined in your function's `func.toml`
* **Injected at deployment** — Available when your function starts
* **Function-scoped** — Specific to each function
* **Version controlled** — Part of your function's configuration

## Defining Environment Variables

Define environment variables in your `func.toml` under the `[env_vars]` section:

```toml theme={null}
[edge_compute]
func_id = "your-function-id"
func_name = "my-function"

[env_vars]
SERVICE_NAME = "data-processor"
VERSION = "1.0.0"
LOG_LEVEL = "info"
DEBUG = "false"
MAX_FILE_SIZE = "10485760"
CACHE_TTL = "3600"
API_BASE_URL = "https://api.example.com"
```

All values are stored as strings. Parse them to the appropriate type in your code.

## Accessing Environment Variables

### JavaScript

    ```javascript theme={null}
    class Config {
        constructor() {
            this.serviceName = process.env.SERVICE_NAME || 'unknown-service';
            this.apiUrl = process.env.API_BASE_URL;
            this.debug = process.env.DEBUG === 'true';
            this.cacheTtl = parseInt(process.env.CACHE_TTL || '300', 10);
            this.maxFileSize = parseInt(process.env.MAX_FILE_SIZE || '10485760', 10);
        }
    }

    const config = new Config();

    export async function handler(request) {
        return new Response(JSON.stringify({
            service: config.serviceName,
            api_configured: !!config.apiUrl,
            cache_ttl: config.cacheTtl,
            debug: config.debug
        }), {
            headers: { 'Content-Type': 'application/json' }
        });
    }
    ```

### Go

    ```go theme={null}
    package main

    import (
        "encoding/json"
        "net/http"
        "os"
        "strconv"
    )

    func handler(w http.ResponseWriter, r *http.Request) {
        // Access environment variables
        apiURL := os.Getenv("API_BASE_URL")
        serviceName := os.Getenv("SERVICE_NAME")
        debug, _ := strconv.ParseBool(os.Getenv("DEBUG"))
        cacheTTL, _ := strconv.Atoi(os.Getenv("CACHE_TTL"))

        // Provide defaults for optional values
        if cacheTTL == 0 {
            cacheTTL = 300
        }

        response := map[string]interface{}{
            "service":        serviceName,
            "api_configured": apiURL != "",
            "cache_ttl":      cacheTTL,
            "debug":          debug,
        }

        json.NewEncoder(w).Encode(response)
    }
    ```

### Python

    ```python theme={null}
    import os

    class Function:
        def __init__(self):
            # Access environment variables
            self.service_name = os.getenv("SERVICE_NAME", "unknown-service")
            self.api_url = os.environ.get("API_BASE_URL")
            self.debug = os.environ.get("DEBUG", "false").lower() == "true"
            self.cache_ttl = int(os.environ.get("CACHE_TTL", "300"))
            self.max_file_size = int(os.getenv("MAX_FILE_SIZE", "10485760"))

        async def handler(self, request):
            return {
                "service": self.service_name,
                "api_configured": bool(self.api_url),
                "cache_ttl": self.cache_ttl,
                "debug": self.debug
            }
    ```

### Java

    ```java theme={null}
    import java.util.Map;
    import java.util.Optional;

    public class ConfigHandler {

        private final String serviceName;
        private final String apiUrl;
        private final boolean debug;
        private final int cacheTtl;

        public ConfigHandler() {
            this.serviceName = getEnv("SERVICE_NAME", "unknown-service");
            this.apiUrl = System.getenv("API_BASE_URL");
            this.debug = Boolean.parseBoolean(getEnv("DEBUG", "false"));
            this.cacheTtl = Integer.parseInt(getEnv("CACHE_TTL", "300"));
        }

        private String getEnv(String key, String defaultValue) {
            String value = System.getenv(key);
            return value != null ? value : defaultValue;
        }

        public Map<String, Object> handle() {
            return Map.of(
                "service", serviceName,
                "api_configured", apiUrl != null,
                "cache_ttl", cacheTtl,
                "debug", debug
            );
        }
    }
    ```

## Environment Variables vs Secrets

Use environment variables for non-sensitive configuration. For sensitive data like API keys and passwords, use [Secrets](secrets.md) instead.

| Feature             | Environment Variables        | Secrets                            |
| ------------------- | ---------------------------- | ---------------------------------- |
| **Storage**         | Plain text in `func.toml`    | Encrypted in Telnyx infrastructure |
| **Scope**           | Function-specific            | Organization-wide                  |
| **Version Control** | ✅ Yes (in git)               | ❌ No (separate secure storage)     |
| **Use Case**        | Configuration, feature flags | API keys, passwords, tokens        |

### When to Use Each

### Environment Variables ✅

    Perfect for non-sensitive configuration:

    * **Application settings** — `LOG_LEVEL`, `DEBUG_MODE`, `PORT`
    * **Feature flags** — `ENABLE_CACHING`, `MAINTENANCE_MODE`
    * **Performance tuning** — `MAX_FILE_SIZE`, `BATCH_SIZE`, `TIMEOUT`
    * **Public endpoints** — `API_BASE_URL`, `CDN_URL`, `WEBHOOK_URL`
    * **Environment identifiers** — `ENVIRONMENT`, `VERSION`, `SERVICE_NAME`

### Secrets 🔒

    Use secrets for sensitive data:

    * **API keys** — `STRIPE_API_KEY`, `TWILIO_API_KEY`
    * **Database credentials** — `DATABASE_PASSWORD`, `REDIS_PASSWORD`
    * **Authentication tokens** — `JWT_SECRET`, `OAUTH_TOKEN`
    * **Encryption keys** — `ENCRYPTION_KEY`, `SIGNING_KEY`

## CLI Management

Manage environment variables by editing your `func.toml` file directly, then redeploy:

```bash theme={null}


## Related Pages

- [Dynamic Variables](../runbooks/dynamic-variables.md)
