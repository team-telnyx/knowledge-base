---
title: Telnyx CLI Quickstart
summary: Get up and running with the Telnyx CLI in 5 minutes.
sources:
  - url: https://developers.telnyx.com/development/cli/getting-started/quickstart
    content_hash: 4f15930030cd5ec544f550633bd753feb53869a4fd5da7857928cdb469a30bc7
updated_at: 2026-04-10T00:00:00Z
---

# Telnyx CLI Quickstart

Get up and running with the Telnyx CLI in 5 minutes

This quickstart guide will help you install the Telnyx CLI, configure authentication, and run your first commands.

## Prerequisites

* [Go 1.22+](https://go.dev/doc/install) installed
* A [Telnyx account](https://portal.telnyx.com/)
* A [Telnyx API key](https://portal.telnyx.com/#/app/api-keys)

## Step 1: Install the CLI

```bash theme={null}
go install github.com/team-telnyx/telnyx-cli/cmd/telnyx@latest
```

Ensure Go's bin directory is in your PATH:

```bash theme={null}
export PATH="$PATH:$(go env GOPATH)/bin"
```

Verify the installation:

```bash theme={null}
telnyx --version
```

## Step 2: Configure Authentication

Set your API key as an environment variable. You can get your API key from the [Telnyx Portal](https://portal.telnyx.com/#/app/api-keys).

```bash theme={null}
export TELNYX_API_KEY=KEY_xxxxxxxxxxxxx
```

  Add this line to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.) to persist it across sessions.

### Verify Authentication

Test that your credentials are working:

```bash theme={null}
telnyx balance retrieve
```

You should see your account balance information.

## Step 3: Run Your First Commands

### Check Your Balance

```bash theme={null}
telnyx balance retrieve
```

### List Your Phone Numbers

```bash theme={null}
telnyx phone-numbers list
```

### Search for Available Numbers

```bash theme={null}
telnyx available-phone-numbers list --filter.country-code US --filter.limit 5
```

### Send a Test Message

> **Note:** You'll need a [messaging-enabled phone number](https://portal.telnyx.com/#/app/numbers/my-numbers) and a configured [messaging profile](https://portal.telnyx.com/#/app/messaging).

```bash theme={null}
telnyx messages send \
  --from +15551234567 \
  --to +15559876543 \
  --text "Hello from the Telnyx CLI!"
```

## Step 4: Explore Commands

### Get Help

```bash theme={null}


## Related Pages

- [Inference API Quickstart](../tutorial/inference-api-quickstart.md)
- [React quickstart](../reference/react-quickstart.md)
- [Telnyx CLI](../reference/telnyx-cli.md)
