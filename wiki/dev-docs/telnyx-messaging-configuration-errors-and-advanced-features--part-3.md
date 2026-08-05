---
title: Telnyx Messaging Configuration, Errors, and Advanced Features
summary: This page consolidates Telnyx messaging configuration guidance, including
  messaging profile setup, configurable spend limits, error code handling, the Vercel
  Chat SDK adapter, and Geomatch for area-code-based sender selection. It covers prerequisites,
  environment variables, webhook setup, capability matrices, and best practices for
  production SMS/MMS workloads.
sources:
- url: https://developers.telnyx.com/docs/messaging/messages/chat-sdk-adapter
- url: https://developers.telnyx.com/docs/messaging/messages/configurable-spend-limits/index
- url: https://developers.telnyx.com/docs/messaging/messages/configuration-and-usage/index
- url: https://developers.telnyx.com/docs/messaging/messages/error-codes/index
- url: https://developers.telnyx.com/docs/messaging/messages/geomatch
updated_at: 2026-08-05T13:55:16Z
---

# Telnyx Messaging Configuration, Errors, and Advanced Features

*Part 3 of 4 — see also: [Part 1](telnyx-messaging-configuration-errors-and-advanced-features--part-1.md), [Part 2](telnyx-messaging-configuration-errors-and-advanced-features--part-2.md), [Part 4](telnyx-messaging-configuration-errors-and-advanced-features--part-4.md)*

This page consolidates Telnyx messaging configuration guidance, including messaging profile setup, configurable spend limits, error code handling, the Vercel Chat SDK adapter, and Geomatch for area-code-based sender selection. It covers prerequisites, environment variables, webhook setup, capability matrices, and best practices for production SMS/MMS workloads.

## Vercel Chat SDK Adapter

`@telnyx/chat-sdk-adapter` is the official Telnyx adapter for the Vercel Chat SDK — Vercel's TypeScript framework for building chatbots that work across Slack, Microsoft Teams, Discord, Telegram, WhatsApp, email, and SMS/MMS through Telnyx. Write bot logic once and route messages through any supported channel.

The adapter is maintained by Telnyx at `team-telnyx/telnyx-chat-sdk-adapter` and listed as a **vendor-official** adapter on chat-sdk.dev.

**When to use this adapter:** building an AI- or rules-driven SMS bot inside a Next.js app and wanting the same handler API you already use for other chat platforms. For general-purpose, high-volume messaging outside a Chat SDK app, use the Telnyx Messaging API directly.

### Prerequisites

- A Telnyx account with a messaging-enabled phone number (E.164 format)
- A Messaging Profile with a webhook URL configured
- Your Telnyx v2 API key
- The Ed25519 **Public Key** from the messaging profile (for webhook signature verification)
- Node.js `>=18`

### Install

```
pnpm add @telnyx/chat-sdk-adapter chat
```

Also install a state adapter — `@chat-adapter/state-memory` for development, `@chat-adapter/state-redis` for production:

```
pnpm add @chat-adapter/state-memory
```

### Quick Start

```
import { createTelnyxAdapter } from "@telnyx/chat-sdk-adapter";
import { createMemoryState } from "@chat-adapter/state-memory";
import { Chat } from "chat";

const telnyx = createTelnyxAdapter({
  messagingProfileId: "40017a7b-...", // recommended — see "Dedicated messaging profile"
  // apiKey:      "KEY..."              // or set TELNYX_API_KEY
  // phoneNumber: "+15551234567"        // or set TELNYX_FROM_NUMBER
  // publicKey:   "vFo7Hk..."           // or set TELNYX_PUBLIC_KEY
});

const chat = new Chat({
  userName: "sms-bot",
  adapters: { telnyx },
  state: createMemoryState(),
});

chat.onNewMention(async (thread, message) => {
  await thread.subscribe();
  await thread.post(`Got your text: ${message.text}`);
});

chat.onSubscribedMessage(async (thread, message) => {
  await thread.post(`Reply: ${message.text}`);
});

await chat.initialize();
```

In your webhook route handler, forward the request to `chat.webhooks.telnyx`:

```
// app/api/webhooks/telnyx/route.ts (Next.js App Router)
export async function POST(request: Request) {
  return chat.webhooks.telnyx(request);
}
```

Point your messaging profile's webhook URL at `https://<your-domain>/api/webhooks/telnyx`.

### Configuration

#### Environment Variables

| Variable | Required | Description |
| --- | --- | --- |
| `TELNYX_API_KEY` | Yes | Your v2 API key |
| `TELNYX_FROM_NUMBER` | Yes | E.164 phone number the bot sends from |
| `TELNYX_PUBLIC_KEY` | Recommended | Ed25519 public key from the messaging profile. Base64 or hex — auto-detected. If unset, webhook signatures are not verified — never run without it in production. |
| `BOT_USERNAME` | No | Bot display name. Defaults to `"bot"`. |

#### TelnyxAdapterConfig

```
interface TelnyxAdapterConfig {
  apiKey?: string;
  phoneNumber?: string;            // E.164
  publicKey?: string;              // base64 or hex, auto-detected
  messagingProfileId?: string;     // strongly recommended (see below)
  userName?: string;
  extraTags?: string[];            // merged into outbound `tags` array
  disableAttributionTags?: boolean;
  logger?: Logger;
}
```

### Recommended: Dedicated Messaging Profile

Create a dedicated Messaging Profile for each bot and pass its ID as `messagingProfileId`. We recommend prefixing the profile name with `[Chat SDK]` (for example, `[Chat SDK] support-bot-prod`) so it's easy to find in Mission Control and in usage reports.

A dedicated profile gives you:

- Per-profile usage analytics, so bot traffic is separated from the rest of your account
- Per-profile spend limits, which cap bot spend without affecting other workloads
- An isolated webhook URL and failover URL
- An isolated Ed25519 public key — the one you pass as `publicKey` belongs to the profile, not the account

### Webhook Setup

1. **Open your messaging profile** in the Telnyx Mission Control portal.
2. **Set the webhook URL** under **Inbound Settings** to your server's endpoint (for example, `https://bot.example.com/api/webhooks/telnyx`). Set **Webhook API version** to `2`.
3. **Copy the Public Key** under **Messaging** → **Security**. Pass it as `publicKey` (or set `TELNYX_PUBLIC_KEY`). Telnyx shows this key in base64; the adapter accepts it as-is.
4. **Assign a phone number** to the profile. The number you set as `TELNYX_FROM_NUMBER` must belong to this profile.

Incoming webhooks are validated against the `telnyx-signature-ed25519` and `telnyx-timestamp` headers. Requests with a timestamp older than 300 seconds, or with an invalid signature, are rejected with `401`.

### Capabilities

| Capability | Supported | Notes |
| --- | --- | --- |
| Inbound SMS / MMS | Yes | via Ed25519-verified webhooks |
| Outbound SMS | Yes | via `POST /v2/messages` |
| Outbound MMS | Yes | automatic upgrade when a posted message has attachments with public URLs |
| Rate-limit handling | Yes | `429` responses surface as `AdapterRateLimitError` with `Retry-After` |
| Structured errors | Yes | Telnyx error codes, titles, and details are parsed into `AuthenticationError` / `NetworkError` messages |
| Direct messages | Yes | a thread is one pair of phone numbers; `isDM()` returns `true` |
| Typing indicators | No | no-op; SMS has no typing concept |
| Reactions | No | SMS has no reactions |
| Edit / delete | No | SMS messages are final once sent |
| Message history API | No | Telnyx does not expose a thread-scoped history API — use a persistent Chat SDK state adapter |

### Thread Model

A thread is a pair of E.164 phone numbers. The thread ID format is `telnyx:<bot-number>:<user-number>`, for example `telnyx:+15551234567:+15559876543`. `openDM(phoneNumber)` returns the thread ID for a given recipient so you can post proactively.

### Attribution

Outbound messages carry two ecosystem-observability signals:

1. **`User-Agent` header** on every outbound API call: `@telnyx/chat-sdk-adapter/<version> (vercel-chat-sdk)`.
2. **`tags` on every outbound message**: `["vercel-chat-sdk", "vercel-chat-sdk:<version>"]`, merged with any user-supplied tags.

These tags appear in Telnyx webhook event payloads (`message.sent`, `message.finalized`, `message.received`) in the `data.payload.tags` field. User-supplied `extraTags` are merged after the attribution tags. Set `disableAttributionTags: true` to opt out; `extraTags` is unaffected.

```
const telnyx = createTelnyxAdapter({
  extraTags: ["env:prod", "team:support"],
  // disableAttributionTags: true,
});
```

### Pair with the Telnyx AI SDK Provider

Use this adapter alongside `@telnyx/ai-sdk-provider` — the Telnyx provider for the Vercel AI SDK — to build a full AI-powered SMS agent on Telnyx inference. The Chat SDK handles message I/O; the AI SDK handles LLM, embeddings, and speech. One account, one API key, two packages.
