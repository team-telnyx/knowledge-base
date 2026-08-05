---
title: Configuration
summary: Every Telnyx Edge Compute project is configured by a single TOML manifest
  at its root — `func.toml` for classic single-function projects or `telnyx.toml`
  for umbrella TypeScript projects. The manifest declares the function's identity,
  environment variables, secret bindings, storage bindings, and (for umbrella projects)
  actors; configuration changes take effect on the next `telnyx-edge ship`.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
updated_at: 2026-08-05T13:40:37Z
---

# Configuration

*Part 2 of 4 — see also: [Part 1](configuration--part-1.md), [Part 3](configuration--part-3.md), [Part 4](configuration--part-4.md)*

Every Telnyx Edge Compute project is configured by a single TOML manifest at its root — `func.toml` for classic single-function projects or `telnyx.toml` for umbrella TypeScript projects. The manifest declares the function's identity, environment variables, secret bindings, storage bindings, and (for umbrella projects) actors; configuration changes take effect on the next `telnyx-edge ship`.

## telnyx.toml

The umbrella manifest replaces `[edge_compute]` with top-level keys and adds `[actors](actors.md)`. On `ship`, the module graph rooted at `main` is bundled into a single file with esbuild (TypeScript/JavaScript only) and the manifest ships with it.

```toml
name = "account-svc"           # function name
main = "src/index.ts"          # entry module — exports the fetch handler (and the actor class)
compatibility_date = "2026-05-01"

[actors](actors.md)
binding = "ACCOUNT"            # the property on env — your handle
type    = "Account"            # the class to instantiate per name

[telnyx]                       # same binding blocks as func.toml
binding = "MY_TELNYX"

[secrets](secrets.md)
binding = "GREETING"
name    = "DEMO_GREETING"
```

| Key | Value |
| --- | --- |
| `name` | Function name, used by the platform to register the function. |
| `main` | Entry module — the root of the client-side esbuild bundle. |
| `compatibility_date` | Runtime compatibility pin. |
| `[actors](actors.md)` | Actor bindings — `binding` is the `env` property, `type` the class to instantiate per name. Ship-time constraints (identifier rules, uniqueness, the 32-character type cap) are specified in the [Stateful Actors configuration reference](stateful-actors-configuration-reference.md). |

The project shape — one module exporting both the actor class and a `fetch` handler — is covered in [Project Structure](project-structure.md). `telnyx-edge new-func --actor` scaffolds it. See [Stateful Actors](stateful-actors--part-1.md) for the full documentation.

## Environment variables

Functions run as real containers, so configuration reaches your code as ordinary process environment variables — `process.env`, `os.environ`, `os.Getenv`, `System.getenv`. There is no separate configuration API to learn.

### What's in the environment

| Variable | Where it comes from |
| --- | --- |
| `PORT` | Set by the platform. Your HTTP server must listen on it. |
| Every `[env_vars]` key | Declared in `func.toml`; injected verbatim on each deploy. |
| Every secret key | `telnyx-edge secrets add <key> <value>` injects the key into **all** functions in your organization. See [Secrets](secrets.md). |
| `TELNYX_API_KEY` | Injected when the function declares a `[telnyx]` binding. This is how non-TypeScript runtimes call the [Telnyx API](telnyx-api.md). |

### Declaring variables

Define non-sensitive configuration under `[env_vars]` in `func.toml`:

```toml
[edge_compute]
func_id   = "7819cf01-39a8-400e-9bce-3d792ffa4017"
func_name = "demo-ts"

[env_vars]
LOG_LEVEL   = "info"
MAX_RETRIES = "3"
DEBUG       = "false"
```

Three behavioral contracts:

- **All values are strings.** Parse numbers and booleans in your code.
- **Changes take effect on the next `telnyx-edge ship`** — there is no live update.
- **Names share the `env` namespace with bindings.** If an `[env_vars]` entry has the same name as a declared binding — or is named `SECRETS` while a `[secrets](secrets.md)` block is declared — `ship` **warns** that one shadows the other on `env` and still proceeds; rename one. (A *binding* named `SECRETS`, or a duplicate `[secrets](secrets.md)` handle, is a hard error.)

`[env_vars]` values are plaintext in `func.toml` and end up in version control. Put credentials in [Secrets](secrets.md) instead.

### Reading variables

**TypeScript / JavaScript**

```ts
const port = Number(process.env.PORT ?? 8080);         // set by the platform
const logLevel = process.env.LOG_LEVEL ?? "info";      // from [env_vars]
const maxRetries = Number(process.env.MAX_RETRIES ?? "3");
const debug = process.env.DEBUG === "true";
```

**Python**

```python
import os

log_level = os.environ.get("LOG_LEVEL", "info")
max_retries = int(os.environ.get("MAX_RETRIES", "3"))
debug = os.environ.get("DEBUG", "false").lower() == "true"
```

**Go**

```go
package function

import (
    "os"
    "strconv"
)

func loadConfig() (logLevel string, maxRetries int, debug bool) {
    logLevel = os.Getenv("LOG_LEVEL")
    if logLevel == "" {
        logLevel = "info"
    }
    maxRetries, _ = strconv.Atoi(os.Getenv("MAX_RETRIES"))
    debug, _ = strconv.ParseBool(os.Getenv("DEBUG"))
    return
}
```

**Quarkus (Java)**

```java
String logLevel = System.getenv().getOrDefault("LOG_LEVEL", "info");
int maxRetries = Integer.parseInt(System.getenv().getOrDefault("MAX_RETRIES", "3"));
boolean debug = Boolean.parseBoolean(System.getenv("DEBUG"));
```

### Environment variables vs secrets

|  | `[env_vars]` | Secrets |
| --- | --- | --- |
| Stored | Plaintext in `func.toml`, committed to git | Server-side; the CLI never prints values |
| Scope | One function | Every function in the organization |
| Changed by | Editing `func.toml`, then `ship` | `telnyx-edge secrets add`, then `ship` |
| Use for | Log levels, feature flags, public URLs, tuning knobs | API keys, passwords, signing keys |
