---
title: Edge Compute Development and CI/CD
summary: An end-to-end guide to building, running locally, configuring, and deploying
  Telnyx Edge Compute functions with the CLI and CI/CD—covering environment variables,
  secrets, routing, versioning, health checks, and known "coming soon" features.
sources:
- url: https://developers.telnyx.com/docs/edge-compute/development
- url: https://developers.telnyx.com/docs/edge-compute/deploy
- url: https://developers.telnyx.com/docs/edge-compute/quickstart/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/index
- url: https://developers.telnyx.com/docs/edge-compute/configuration/environment-variables
- url: https://developers.telnyx.com/docs/edge-compute/configuration/secrets
- url: https://developers.telnyx.com/docs/edge-compute/configuration/cron-triggers
- url: https://developers.telnyx.com/docs/edge-compute/configuration/routing
- url: https://developers.telnyx.com/docs/edge-compute/configuration/versions
- url: https://developers.telnyx.com/docs/edge-compute/testing/index
updated_at: 2026-05-20T08:17:32Z
---

# Edge Compute Development and CI/CD

*Part 1 of 2 — see also: [Part 2](edge-compute-development-and-ci-cd--part-2.md)*

An end-to-end guide to building, running locally, configuring, and deploying Telnyx Edge Compute functions with the CLI and CI/CD—covering environment variables, secrets, routing, versioning, health checks, and known "coming soon" features.

## End-to-end development workflow

- Create a function: telnyx-edge new-func
- Develop locally with your language’s native tools
- Test with your language’s test framework
- Deploy to the edge: telnyx-edge ship

See also [Edge Compute Quick Start](edge-compute-quick-start.md).

## Install and authenticate the CLI

- Install: download the latest release from the edge-compute GitHub releases and place telnyx-edge on your PATH (verify with telnyx-edge --help).
- Authenticate (recommended): telnyx-edge auth login (opens browser OAuth).
- Or with API key: telnyx-edge auth api-key set YOUR_API_KEY
- Verify: telnyx-edge auth status

Refer to [CLI Reference](cli-reference.md) for all commands.

## Scaffold a function

Create a Hello World in your preferred language:

- Go: telnyx-edge new-func --language=go --name=hello-world
- JavaScript: telnyx-edge new-func --language=js --name=hello-world
- TypeScript: telnyx-edge new-func --language=ts --name=hello-world
- Python: telnyx-edge new-func --language=python --name=hello-world
- Java (Quarkus): telnyx-edge new-func --language=quarkus --name=hello-world

Each scaffold includes func.toml plus language-specific files. See [Runtime](runtime.md) and [Execution Model](execution-model.md) for how functions run.

## Run locally (by language)

Use native servers/runtimes to iterate quickly.

- Go (temporary entrypoint):

```
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
Run: go run main.go

- Python (ASGI with uvicorn):

```
# app.py
from function import new
func = new()
app = func.handle
```
Run: pip install uvicorn && uvicorn app:app --port 8080

- Quarkus (tests/local): mvn test (or ./mvnw test)

Send requests while running:

- curl http://localhost:8080/
- curl -X POST http://localhost:8080/api/data -H "Content-Type: application/json" -d '{"key":"value"}'
- curl http://localhost:8080/api/protected -H "Authorization: Bearer test-token" -H "X-Custom-Header: value"

## Configure environment for local dev

- Use shell exports or a .env file (add .env to .gitignore).
- Popular loaders:
  - Go: github.com/joho/godotenv (godotenv.Load())
  - Python: python-dotenv (load_dotenv())
  - Quarkus: supports .env and application.properties; @ConfigProperty for injection
- Mock secrets locally with environment variables (never commit real secrets). Example: export MY_API_KEY="test-key-123"; access via os.getenv/Process.env/System.getenv.

See [Best Practices](best-practices.md) for parity tips (match language and dependency versions with production).

## Test locally

- Unit tests with standard tools work out of the box (e.g., go test, pytest/pytest-asyncio, JUnit/QuarkusTest).
- Example assertions: ensure HTTP 200 on GET; validate response body for POST.
- Dedicated testing and staging tooling is coming soon—see [Testing](testing.md).

## Function configuration (func.toml)

Manage deployment/runtime settings in func.toml, including function identity and configuration such as [env_vars]. Example:

```
[edge_compute]
func_id = "func-abc123def456"
func_name = "hello-world"

[env_vars]
LOG_LEVEL = "info"
API_BASE_URL = "https://api.example.com"
```

Learn more in [Edge Compute function configuration](edge-compute-function-configuration.md), [Environment Variables](environment-variables.md), [Edge Compute secrets management](edge-compute-secrets-management.md), [Routes & Domains](routes-domains.md), [Cron Triggers](cron-triggers.md), and [Versions & Deployments](versions-deployments.md).

## Deploy to the edge

From your function directory:

- telnyx-edge ship

The CLI validates structure, checks auth, packages files, uploads, and deploys globally. After success, the live URL is printed.

## Routes and public URLs

- Public URL pattern: https://{funcName}-{orgId}.telnyxcompute.com
- Development environment URLs use: https://{funcName}-{orgId}.dev.telnyxcompute.com
- Example: https://hello-world-abc123.telnyxcompute.com
- Custom domains and region placement are planned features.

See [Routes & Domains](routes-domains.md) for details.

## CI/CD automation

Authenticate CI with a Telnyx API key scoped for Edge Compute (create in the Telnyx Portal) and store it as a CI secret.

- GitHub Actions (deploy on main):

```
name: Deploy Edge Function
on: { push: { branches: [main] } }
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install Telnyx CLI
        run: |
          wget -qO- https://github.com/team-telnyx/edge-compute/releases/latest/download/telnyx-edge-linux-amd64.tar.gz | tar xz
          sudo mv telnyx-edge /usr/local/bin/
      - name: Deploy
        env: { TELNYX_API_KEY: ${{ secrets.TELNYX_API_KEY }} }
        run: telnyx-edge ship
```

- With tests and multi-language setups: set up your language runtime (Node, Go, Python, Java), run tests, then telnyx-edge ship.

- GitLab CI:

```
stages: [test, deploy]

test:
  stage: test
  image: python:3.11
  script:
    - pip install -r requirements.txt
    - pytest tests/

deploy:
  stage: deploy
  image: ubuntu:latest
  only: [main]
  script:
    - wget -qO- https://github.com/team-telnyx/edge-compute/releases/latest/download/telnyx-edge-linux-amd64.tar.gz | tar xz
    - sudo mv telnyx-edge /usr/local/bin/
    - telnyx-edge ship
  variables:
    TELNYX_API_KEY: $TELNYX_API_KEY
```

- CircleCI (test then deploy workflow) is similarly supported.

Environment promotion:

- Use branches/tags plus separate secrets per environment, e.g., telnyx-edge ship --env dev for staging, --env prod for production.

Health checks:

- After deploy, curl a /health endpoint and fail the job if not 200. Add a brief sleep to allow propagation.

Notifications:

- Send deployment status to Slack via a webhook. 

Monitoring after deploy: see [Edge Compute observability](edge-compute-observability.md).

## Secrets management

Use encrypted, organization-scoped secrets for sensitive data.

- Add/update/list/delete:
  - telnyx-edge secrets add NAME "value"
  - telnyx-edge secrets list (values are never shown)
  - telnyx-edge secrets delete NAME
- Access in code via environment variables (e.g., DATABASE_PASSWORD, PAYMENT_API_KEY).
- Rotate regularly: update secret, telnyx-edge ship, verify health.
- Per-environment secrets and local secret tooling are planned; until then, use naming conventions (e.g., DEV_DATABASE_PASSWORD) and mock via local env vars.

See [Edge Compute secrets management](edge-compute-secrets-management.md) for complete guidance.

## Environment variables in production

Use env vars for non-sensitive configuration and manage them in func.toml under [env_vars]. All values are strings; parse and validate in code, provide sensible defaults, and follow UPPER_SNAKE_CASE naming.

Use secrets for sensitive values; see [Environment Variables](environment-variables.md) vs [Edge Compute secrets management](edge-compute-secrets-management.md).

## Versioning and rollbacks

- Current model: telnyx-edge ship performs an atomic replacement of the previous version.
- Until built-in rollback/version history is available, use Git:
  - git revert HEAD && telnyx-edge ship
  - or deploy a specific commit (git checkout <sha> && telnyx-edge ship)

See [Versions & Deployments](versions-deployments.md).

## Cron triggers (coming soon)

Scheduling is planned. Until then, trigger your function from an external scheduler (e.g., a GitHub Actions cron that curls your endpoint).

See [Cron Triggers](cron-triggers.md).

## Differences: local vs production

- Network: localhost vs global edge network
- Secrets: local env vars vs encrypted storage/injection
- Bindings: mocked locally vs live service bindings in production
- Cold starts: typically N/A locally vs container initialization on edge
- Resource limits: your machine vs platform quotas (see [Edge Compute limits and quotas](edge-compute-limits-and-quotas.md))
