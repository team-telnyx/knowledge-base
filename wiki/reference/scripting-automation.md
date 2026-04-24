---
title: Scripting & Automation
summary: Output formats, filtering, and scripting with the Telnyx CLI.
sources:
  - url: https://developers.telnyx.com/development/cli/general-usage/index
    content_hash: 0cba51c4718b612d6220ef7fe7db7a122ee373e2b68676ff08022d10abcf0800
updated_at: 2026-04-10T00:00:00Z
---

# Scripting & Automation

Output formats, filtering, and scripting with the Telnyx CLI

This guide covers common patterns for automating workflows with the Telnyx CLI — output formats, filtering, and integration with scripts and CI/CD pipelines.

## Output Formats

The CLI supports multiple output formats via the `--format` flag.

### Auto Format (Default)

Interactive exploration mode, best for browsing data:

```bash theme={null}
telnyx phone-numbers list
```

### JSON Format

Machine-readable output for scripting and automation:

```bash theme={null}
telnyx phone-numbers list --format json
```

### YAML Format

Human-readable structured output:

```bash theme={null}
telnyx phone-numbers list --format yaml
```

### Pretty Format

Indented, colorized JSON:

```bash theme={null}
telnyx phone-numbers list --format pretty
```

### Raw Format

Unformatted API response:

```bash theme={null}
telnyx phone-numbers list --format raw
```

### All Format Options

| Format   | Description                       | Best For                  |
| -------- | --------------------------------- | ------------------------- |
| `auto`   | Interactive exploration (default) | Browsing data             |
| `json`   | Compact JSON                      | Scripting, piping to jq   |
| `jsonl`  | JSON Lines (one object per line)  | Streaming, large datasets |
| `pretty` | Indented, colorized JSON          | Debugging                 |
| `yaml`   | YAML format                       | Human-readable configs    |
| `raw`    | Unformatted API response          | Debugging                 |

## Transforming Output with GJSON

Use `--transform` to extract specific fields using [GJSON syntax](https://github.com/tidwall/gjson/blob/master/SYNTAX.md):

```bash theme={null}
