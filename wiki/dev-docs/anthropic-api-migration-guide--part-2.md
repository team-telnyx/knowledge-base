---
title: Anthropic API Migration Guide
summary: Telnyx exposes an Anthropic-compatible Messages endpoint at POST /v2/ai/anthropic/v1/messages,
  accepting the same request body and returning the same response shape as the native
  Anthropic Messages API, including streaming via Anthropic SSE event types. This
  guide covers authentication, quickstart examples, streaming, tool calling, extended
  thinking, system prompts, available models, Telnyx-specific extensions, and a parameter
  compatibility matrix.
sources:
- url: https://developers.telnyx.com/docs/inference/anthropic
updated_at: 2026-08-05T13:45:44Z
---

# Anthropic API Migration Guide

*Part 2 of 2 — see also: [Part 1](anthropic-api-migration-guide--part-1.md)*

Telnyx exposes an Anthropic-compatible Messages endpoint at POST /v2/ai/anthropic/v1/messages, accepting the same request body and returning the same response shape as the native Anthropic Messages API, including streaming via Anthropic SSE event types. This guide covers authentication, quickstart examples, streaming, tool calling, extended thinking, system prompts, available models, Telnyx-specific extensions, and a parameter compatibility matrix.

## Telnyx Extensions

The endpoint accepts several Telnyx-specific fields alongside the standard Anthropic request body:

| Field | Type | Description |
| --- | --- | --- |
| `api_key_ref` | string | Reference to an integration secret for external provider keys. |
| `mcp_servers` | array | List of MCP (Model Context Protocol) server configs to expose to the model. |
| `fallback_config` | object | Configuration for automatic model fallback when the primary model is unavailable. |
| `billing_group_id` | uuid | Billing group to associate with this request. |
| `timeout` | number | Request timeout in seconds (default: 300). |
| `max_retries` | integer | Maximum retry attempts for the request. |
| `service_tier` | string | Service tier for the request. |

These fields pass through as extra body parameters in the SDK:

```python
response = client.messages.create(
    model="zai-org/GLM-5.2",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
    extra_body={
        "billing_group_id": "6a09cdc3-8948-47f0-aa62-74ac943d6c58",
    },
)
```

## Compatibility

| Parameter | Telnyx | Anthropic |
| --- | --- | --- |
| `model` | ✅ | ✅ |
| `messages` | ✅ | ✅ |
| `max_tokens` | ✅ | ✅ |
| `system` | ✅ | ✅ |
| `stream` | ✅ | ✅ |
| `temperature` | ✅ | ✅ |
| `top_p` | ✅ | ✅ |
| `top_k` | ✅ | ✅ |
| `stop_sequences` | ✅ | ✅ |
| `metadata` | ✅ | ✅ |
| `tools` | ✅ | ✅ |
| `tool_choice` | ✅ | ✅ |
| `thinking` | ✅ | ✅ |
| `api_key_ref` | ✅ | ❌ |
| `mcp_servers` | ✅ | ❌ |
| `fallback_config` | ✅ | ❌ |
| `billing_group_id` | ✅ | ❌ |
| `timeout` | ✅ | ❌ |
| `service_tier` | ✅ | ❌ |
