---
title: Install the Telnyx CLI
summary: Install the Telnyx CLI on macOS, Windows, or Linux.
sources:
  - url: https://developers.telnyx.com/development/cli/getting-started/install
    content_hash: 854430f7f48afd3949b8e150e72556c956eb246f2010500d707b3e3f31ca8e99
updated_at: 2026-04-10T00:00:00Z
---

# Install the Telnyx CLI

Install the Telnyx CLI on macOS, Windows, or Linux

The Telnyx CLI is supported on macOS, Windows, and Linux.

  The Telnyx CLI requires **Go 1.22 or later**. If you don't have Go installed, follow the [official installation guide](https://go.dev/doc/install).

## Installation

Install the CLI using Go:

```bash theme={null}
go install github.com/team-telnyx/telnyx-cli/cmd/telnyx@latest
```

This downloads, compiles, and installs the `telnyx` binary to your Go bin directory.

## Add to PATH

After installation, ensure the Go bin directory is in your PATH:

```bash theme={null}


## Related Pages

- [Install Legacy CLI](../reference/install-legacy-cli.md)
- [Telnyx CLI](../reference/telnyx-cli.md)
- [Getting Started with Telnyx Voice API](../runbooks/getting-started-with-telnyx-voice-api.md)
