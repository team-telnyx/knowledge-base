---
title: Edge Compute Configuration
summary: Covers all aspects of configuring Telnyx Edge Compute functions, including
  the func.toml file, environment variables, secrets management, routing, cron triggers,
  deployment versions, and best practices for performance, reliability, security,
  and observability.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/best-practices
- url: https://developers.telnyx.com/docs/edge-compute/configuration/cron-triggers
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
updated_at: 2026-06-11T10:26:17Z
---

# Edge Compute Configuration

*Part 1 of 3 — see also: [Part 2](edge-compute-configuration--part-2.md), [Part 3](edge-compute-configuration--part-3.md)*

Covers all aspects of configuring Telnyx Edge Compute functions, including the func.toml file, environment variables, secrets management, routing, cron triggers, deployment versions, and best practices for performance, reliability, security, and observability.

Function configuration is managed through a `func.toml` file, which defines your project settings, bindings, and deployment options. The `telnyx-edge` CLI is the command-line tool used to develop, test, and deploy functions.

## Environment Variables

Environment variables allow you to configure your Edge Compute functions without modifying code. They are ideal for non-sensitive configuration values like API endpoints, feature flags, and performance settings.

Environment variables in Edge Compute are:

- **Declared in configuration** — Defined in your function's `func.toml`
- **Injected at deployment** — Available when your function starts
- **Function-scoped** — Specific to each function
- **Version controlled** — Part of your function's configuration

### Defining Environment Variables

Define environment variables in your `func.toml` under the `[env_vars]` section:

```toml
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

### Accessing Environment Variables

In Python:

```python
import os

class Function:
    def __init__(self):
        self.service_name = os.getenv("SERVICE_NAME", "unknown-service")
        self.api_url = os.environ.get("API_BASE_URL")
        self.debug = os.environ.get("DEBUG", "false").lower() == "true"
        self.cache_ttl = int(os.environ.get("CACHE_TTL", "300"))

    async def handler(self, request):
        return {
            "service": self.service_name,
            "api_configured": bool(self.api_url),
            "cache_ttl": self.cache_ttl,
            "debug": self.debug
        }
```

In Go:

```go
package function

import (
    "encoding/json"
    "net/http"
    "os"
    "strconv"
)

func Handle(w http.ResponseWriter, r *http.Request) {
    apiURL := os.Getenv("API_BASE_URL")
    serviceName := os.Getenv("SERVICE_NAME")
    debug, _ := strconv.ParseBool(os.Getenv("DEBUG"))
    cacheTTL, _ := strconv.Atoi(os.Getenv("CACHE_TTL"))

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

In Java (Quarkus):

```java
import java.util.Map;

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

    public Map<String, Object> getConfig() {
        return Map.of(
            "service", serviceName,
            "api_configured", apiUrl != null,
            "cache_ttl", cacheTtl,
            "debug", debug
        );
    }
}
```

### Environment Variable Best Practices

- **Naming conventions**: Use `UPPER_SNAKE_CASE` for consistency with standard environment variable conventions. Include descriptive names like `MAX_FILE_SIZE` rather than vague ones like `maxsize`.
- **Type safety**: Store all values as strings and parse them in your code.
- **Validation and defaults**: Always validate environment variables and provide sensible defaults.
- **Environment-specific values**: Use descriptive variable names and document expected values, e.g. `ENVIRONMENT = "production"` with a comment listing valid options.

### Common Environment Variable Patterns

**Feature flags:**

```toml
[env_vars]
ENABLE_NEW_PROCESSING = "true"
ENABLE_BULK_OPERATIONS = "false"
BETA_FEATURES_ENABLED = "false"
```

**Service configuration:**

```toml
[env_vars]
SERVICE_NAME = "user-auth-service"
SERVICE_VERSION = "2.1.0"
API_BASE_URL = "https://api.telnyx.com"
```

**Performance tuning:**

```toml
[env_vars]
MAX_CONNECTIONS = "100"
CONNECTION_TIMEOUT = "30"
BATCH_SIZE = "50"
MAX_RETRIES = "3"
```

### Debugging Environment Variables

Print environment variables for debugging during development. Remove debug logging before deploying to production to avoid exposing configuration details.

### Environment Variable Limits

- Variable names must contain only letters, numbers, and underscores
- Variable names are case-sensitive
- All values are stored and retrieved as strings

For specific size limits on variable names and values, refer to the Edge Compute limits documentation.

### CLI Management

Manage environment variables by editing your `func.toml` file directly, then redeploy. Changes take effect on the next deployment.

```bash
# Edit func.toml to add/update env_vars
vim func.toml

# Deploy function with updated environment variables
telnyx-edge ship
```
