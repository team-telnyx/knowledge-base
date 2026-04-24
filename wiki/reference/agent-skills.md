---
title: Agent Skills
summary: Agent Skills enable Claude Code and other AI coding agents to build Telnyx integrations using natural language.
sources:
  - url: https://developers.telnyx.com/development/agent-skills/index
    content_hash: 33ad6b9c87622cb885b4a5fd4eadeff2601df273cd1d1c40916d4d860996392b
updated_at: 2026-04-10T00:00:00Z
---

# Agent Skills

Agent Skills enable Claude Code and other AI coding agents to build Telnyx integrations using natural language. They support all 36 Telnyx products including Messaging, Voice, Numbers, IoT, and AI.

## Installation Quickstart

Choose your setup method:

### Skills CLI

    The Skills CLI works with Codex, Cursor, OpenClaw, Gemini CLI, GitHub Copilot, and more.

    ```bash theme={null}
    npx skills add team-telnyx/skills --skill  --agent 
    ```

    **Example:**

    ```bash theme={null}
    npx skills add team-telnyx/skills --skill telnyx-voice-python --agent codex
    ```

    ### Agent-specific commands

**Codex**

        ```bash theme={null}
        npx skills add team-telnyx/skills --skill  --agent codex
        ```

---

**Claude Code**

        ```bash theme={null}
        npx skills add team-telnyx/skills --skill  --agent claude-code
        ```

---

**Cursor**

        ```bash theme={null}
        npx skills add team-telnyx/skills --skill  --agent cursor
        ```

---

**OpenClaw**

        ```bash theme={null}
        npx skills add team-telnyx/skills --skill  --agent openclaw
        ```

---

**Gemini CLI**

        ```bash theme={null}
        npx skills add team-telnyx/skills --skill  --agent gemini-cli
        ```

---

**GitHub Copilot**

        ```bash theme={null}
        npx skills add team-telnyx/skills --skill  --agent github-copilot
        ```

---

    See the [full list of supported agents](https://github.com/vercel-labs/skills#supported-agents).

    > **Note:** Use only the skills your project actually needs. Loading too many skills wastes tokens and dilutes context.

### Claude Code Plugins

    Plugins are curated bundles of related Telnyx Agent skills.

    **Step 1.** Add the Telnyx skills marketplace (one-time):

    ```bash theme={null}
    /plugin marketplace add team-telnyx/skills
    ```

    **Step 2.** Install a plugin:

    ```bash theme={null}
    /plugin install @skills
    ```

    | Plugin                    | Language                                                     |
    | ------------------------- | ------------------------------------------------------------ |
    | `telnyx-python`           | Python                                                       |
    | `telnyx-javascript`       | JavaScript / Node.js                                         |
    | `telnyx-go`               | Go                                                           |
    | `telnyx-java`             | Java                                                         |
    | `telnyx-ruby`             | Ruby                                                         |
    | `telnyx-curl`             | curl (REST API)                                              |
    | `telnyx-webrtc-client`    | WebRTC client SDKs (JS, iOS, Android, Flutter, React Native) |
    | `telnyx-twilio-migration` | Migrate from Twilio to Telnyx                                |
    | `telnyx-cli`              | Telnyx CLI                                                   |

    **Examples:**

    ```bash theme={null}
    /plugin install telnyx-python@skills
    /plugin install telnyx-twilio-migration@skills
    ```

    Each language plugin includes all 36 Telnyx products.

### Manual Setup

    For Cursor, Windsurf, or agents without native skill support.

    **Cursor:**

    1. Open **Settings > Rules > Project Rules**.
    2. Create a rule file (e.g., `.cursor/rules/telnyx.mdc`).
    3. Paste the contents of the relevant `SKILL.md` from the [skills repository](https://github.com/team-telnyx/skills).

    **Windsurf:**

    1. Create a `.windsurfrules` file in your project root.
    2. Paste the contents of the relevant `SKILL.md`.

    **Direct URL:**

    ```
    https://raw.githubusercontent.com/team-telnyx/skills/main/telnyx-python/skills/telnyx-messaging-python/SKILL.md
    ```

    Replace `telnyx-python` and `telnyx-messaging-python` with your desired language and product.

> **Note:** You'll need a [Telnyx API key](https://portal.telnyx.com/#/api-keys) when you're ready to make API calls.

## Available Skills

Skills are organized by product and language. Each product skill is available in **curl**, **JavaScript**, **Python**, **Go**, **Java**, and **Ruby**.

Replace `*` with your language suffix (e.g., `telnyx-voice-python`, `telnyx-messaging-go`).

### Messaging

| Skill                         | Description                                                     |
| ----------------------------- | --------------------------------------------------------------- |
| `telnyx-messaging-*`          | Send/receive SMS/MMS, manage messaging numbers, handle opt-outs |
| `telnyx-messaging-profiles-*` | Messaging profiles, number pools, short codes                   |
| `telnyx-messaging-hosted-*`   | Hosted SMS numbers, toll-free verification, RCS                 |
| `telnyx-10dlc-*`              | 10DLC brand/campaign registration for A2P compliance            |

### Voice & Communications

| Skill                         | Description                                                  |
| ----------------------------- | ------------------------------------------------------------ |
| `telnyx-voice-*`              | Call control: dial, answer, hangup, transfer, bridge         |
| `telnyx-voice-media-*`        | Audio playback, text-to-speech, call recording               |
| `telnyx-voice-gather-*`       | DTMF/speech input collection, AI-powered gather              |
| `telnyx-voice-streaming-*`    | Real-time audio streaming, forking, transcription            |
| `telnyx-voice-conferencing-*` | Conference calls, queues, multi-party sessions               |
| `telnyx-voice-advanced-*`     | DTMF sending, SIPREC, noise suppression, supervisor          |
| `telnyx-texml-*`              | TeXML (TwiML-compatible) voice applications                  |
| `telnyx-sip-*`                | SIP trunking connections, outbound voice profiles            |
| `telnyx-sip-integrations-*`   | Call recordings, media storage, Dialogflow integration       |
| `telnyx-webrtc-*`             | WebRTC credentials and push notification setup (server-side) |

### Numbers

| Skill                         | Description                                 |
| ----------------------------- | ------------------------------------------- |
| `telnyx-numbers-*`            | Search, order, and manage phone numbers     |
| `telnyx-numbers-config-*`     | Phone number configuration and settings     |
| `telnyx-numbers-compliance-*` | Regulatory requirements, bundles, documents |
| `telnyx-numbers-services-*`   | Voicemail, voice channels, E911             |
| `telnyx-porting-in-*`         | Port numbers into Telnyx                    |
| `telnyx-porting-out-*`        | Manage port-out requests                    |
| `telnyx-verify-*`             | Phone verification, number lookup, 2FA      |

### AI

| Skill                    | Description                              |
| ------------------------ | ---------------------------------------- |
| `telnyx-ai-assistants-*` | AI voice assistants with knowledge bases |
| `telnyx-ai-inference-*`  | LLM inference, embeddings, AI analytics  |
| `telnyx-missions-*`      | Automated AI-driven workflows and tasks  |

### IoT & Networking

| Skill                 | Description                      |
| --------------------- | -------------------------------- |
| `telnyx-iot-*`        | IoT SIM cards, eSIMs, data plans |
| `telnyx-networking-*` | Private networks, VPN gateways   |

### Other Products

| Skill              | Description                    |
| ------------------ | ------------------------------ |
| `telnyx-storage-*` | S3-compatible cloud storage    |
| `telnyx-video-*`   | Video rooms and conferencing   |
| `telnyx-fax-*`     | Programmable fax               |
| `telnyx-oauth-*`   | OAuth 2.0 authentication flows |

### Account Management

| Skill                            | Description                                          |
| -------------------------------- | ---------------------------------------------------- |
| `telnyx-account-*`               | Balance, payments, invoices, webhooks, audit logs    |
| `telnyx-account-access-*`        | Addresses, auth providers, IP access, billing groups |
| `telnyx-account-management-*`    | Sub-account management (resellers)                   |
| `telnyx-account-notifications-*` | Notification channels and settings                   |
| `telnyx-account-reports-*`       | Usage reports for billing and analytics              |

## WebRTC Client SDKs

The skills above cover **server-side** Telnyx APIs. For building **calling apps** where users make/receive VoIP calls, you need client-side WebRTC SDKs:

| Skill                               | Platform     | Language   |
| ----------------------------------- | ------------ | ---------- |
| `telnyx-webrtc-client-js`           | Browser      | JavaScript |
| `telnyx-webrtc-client-ios`          | iOS          | Swift      |
| `telnyx-webrtc-client-android`      | Android      | Kotlin     |
| `telnyx-webrtc-client-flutter`      | Flutter      | Dart       |
| `telnyx-webrtc-client-react-native` | React Native | TypeScript |

Each covers authentication, making/receiving calls, call controls, push notifications, and AI Agent integration.

> **Note:** Building a calling app typically requires **two skills**: a server-side plugin (e.g. `telnyx-voice-python`) for credentials/tokens, and a client-side WebRTC skill for the UI.

## Twilio Migration

A comprehensive 6-phase orchestrated workflow for migrating from Twilio to Telnyx.

```bash theme={null}
npx skills add team-telnyx/skills --skill telnyx-twilio-migration --agent 
```

**What's covered:**

| Area           | Description                                                        |
| -------------- | ------------------------------------------------------------------ |
| Voice          | TwiML → TeXML compatibility (15 verbs, 8 nouns) + Call Control API |
| Messaging      | Parameter mapping, messaging profiles, 10DLC registration          |
| WebRTC         | Architecture differences, endpoint migration, mobile SDK guides    |
| Number Porting | FastPort API for same-day US/Canada activation                     |
| Verify (2FA)   | SMS, voice, flash calling, PSD2 verification                       |
| SIP Trunking   | Connection setup, credential auth, FQDN migration                  |
| Auth Changes   | Basic → Bearer, webhook signatures (HMAC-SHA1 → Ed25519)           |

Includes automated scripts for pre-flight checks, usage scanning, linting, validation, and smoke tests.

## Example Prompts

Once installed, try asking your agent:

| Prompt                                                     | What it builds                            |
| ---------------------------------------------------------- | ----------------------------------------- |
| "Send an SMS to +15551234567 saying 'Your order shipped'." | Messaging integration with error handling |
| "Create a webhook server to receive inbound calls."        | Express/Flask server with Call Control    |
| "Search for toll-free numbers in the US."                  | Number search and provisioning code       |
| "Build an IVR that routes calls based on keypad input."    | TeXML application with DTMF handling      |
| "Create a Voice AI agent for appointment scheduling."      | AI Assistant with custom tools            |
| "Port my number from Twilio to Telnyx."                    | Porting request with required fields      |

## How It Works

1. Describe what you want to build in natural language.
2. The agent reads Telnyx SDK documentation through the installed skill.
3. The agent writes production-ready code with proper auth, error handling, and best practices.
4. Review and iterate until complete.

Skills provide:

* Complete SDK reference documentation
* Code examples and patterns
* Error handling best practices
* Authentication setup guides
* Webhook configuration examples

## Resources

* [Agent Skills Repository](https://github.com/team-telnyx/skills)
* [Agent Skills Specification](https://agentskills.io/specification)
* [GitHub: Telnyx SDKs](https://github.com/team-telnyx)
* [API Reference](/api-reference)
* [Get API Keys](https://portal.telnyx.com/#/api-keys)

## Contributing

See the [Agent Skills Repository](https://github.com/team-telnyx/skills) for contribution guidelines and to report issues.
