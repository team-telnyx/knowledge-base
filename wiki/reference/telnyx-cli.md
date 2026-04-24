---
title: Telnyx CLI
summary: Command-line interface for Telnyx APIs.
sources:
  - url: https://developers.telnyx.com/development/cli/index
    content_hash: ad76fdd7273c443c141294aa4aec988a752fbd57ebe7c250b8bb48cf3ae9855c
updated_at: 2026-04-10T00:00:00Z
---

# Telnyx CLI

Command-line interface for Telnyx APIs

The Telnyx CLI is the official command-line interface for managing Telnyx resources directly from your terminal. Send messages, manage phone numbers, control calls, and more — all without leaving the command line.

## When to Use the CLI vs the API

| Use Case                | CLI                    | API                        |
| ----------------------- | ---------------------- | -------------------------- |
| Quick manual tasks      | ✅ Best choice          | Overkill                   |
| Scripting & automation  | ✅ Great for bash/shell | ✅ Better for complex logic |
| CI/CD pipelines         | ✅ Simple integrations  | ✅ Full control             |
| Production applications | ❌ Not recommended      | ✅ Use SDKs or direct API   |
| Exploring the API       | ✅ Fast iteration       | Slower feedback loop       |

The CLI is ideal for operators, developers exploring the API, and simple automation. For production applications, use the [Telnyx SDKs](https://developers.telnyx.com/development/sdks) or call the [REST API](https://developers.telnyx.com/api-reference/overview) directly.

## Features

  - [Full API Coverage](#) — Access all Telnyx APIs — messaging, voice, numbers, 10DLC, AI, verification, storage, and more

  - [Multiple Output Formats](#) — JSON, YAML, pretty-print, and raw output for scripting and human readability

  - [Auto-generated from OpenAPI](#) — Always in sync with the latest Telnyx API endpoints

  - [Debug Mode](#) — Inspect HTTP requests and responses for troubleshooting

## Quick Example

```bash theme={null}


## Related Pages

- [Telnyx](../runbooks/telnyx.md)
- [Telnyx CLI Quickstart](../reference/telnyx-cli-quickstart.md)
- [Install the Telnyx CLI](../reference/install-the-telnyx-cli.md)
