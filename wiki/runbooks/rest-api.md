---
title: REST API
summary: Single-request text-to-speech with HTTP chunked streaming — start playing before synthesis finishes.
sources:
  - url: https://developers.telnyx.com/docs/voice/tts/rest-api/index
    content_hash: a8423cf816c43e1b07f45886c06d0fbb7955a9909cab8f4fb519ec6d726e5b77
updated_at: 2026-04-10T00:00:00Z
---

# REST API

Single-request text-to-speech with HTTP chunked streaming — start playing before synthesis finishes.

## How It Works

You send text in, audio streams back over the same HTTP connection. No polling, no callbacks.

The response uses HTTP chunked transfer encoding — audio chunks arrive as they're synthesized. Your client can begin playback immediately without waiting for the full file. The connection stays open until synthesis completes or 30 seconds pass with no new chunks.

This makes REST suitable for real-time playback, not just batch file generation. For multi-turn conversational use cases where you're continuously feeding text, use [WebSocket Streaming](lifecycle-2.md) instead.

***

## Text Preprocessing

Before synthesis, text passes through two stages:

1. **Markdown stripping** — headers, bold, italics, code blocks, links, lists, emoji are converted to plain text.
2. **Pronunciation dictionary** — if `pronunciation_dict_id` is set, custom word replacements are applied.

***

## API Reference

The full OpenAPI spec for these endpoints is available in the auto-generated [API Reference](https://developers.telnyx.com/docs/voice/tts/rest-api/api-reference). Note: the OAS is currently being cleaned up — some fields and provider-specific schemas may be incomplete.


## Related Pages

- [Build a REST API](../runbooks/build-a-rest-api.md)
