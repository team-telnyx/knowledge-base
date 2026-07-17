---
title: Telnyx Configuration, Authentication, and Compliance Reference
summary: This page consolidates Telnyx support guidance on whitelisting SIP signaling,
  media, and webhook IP addresses; IP authentication methods (tech prefix, X-Telnyx-Token,
  P-Charge-Info) including FreePBX configuration; multi-device registration limits;
  AI Assistant configuration with tools, handoffs, transfers, and MCP servers; UK
  TPS compliance for marketing calls; and the public Knowledge Agent bot-to-bot support
  API.
sources:
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
- url: https://support.telnyx.com/en/articles/12232444-comprehensive-ai-assistants-configuration-walk-through
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
- url: https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
- url: https://support.telnyx.com/en/articles/6136385-uk-tps-register-guidelines
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
- url: https://support.telnyx.com/en/collections/19623087-ai-assistant
updated_at: 2026-07-17T08:59:35Z
---

# Telnyx Configuration, Authentication, and Compliance Reference

*Part 3 of 4 — see also: [Part 1](telnyx-configuration-authentication-and-compliance-reference--part-1.md), [Part 2](telnyx-configuration-authentication-and-compliance-reference--part-2.md), [Part 4](telnyx-configuration-authentication-and-compliance-reference--part-4.md)*

This page consolidates Telnyx support guidance on whitelisting SIP signaling, media, and webhook IP addresses; IP authentication methods (tech prefix, X-Telnyx-Token, P-Charge-Info) including FreePBX configuration; multi-device registration limits; AI Assistant configuration with tools, handoffs, transfers, and MCP servers; UK TPS compliance for marketing calls; and the public Knowledge Agent bot-to-bot support API.

## AI Assistants Configuration

AI Assistants provide a way to manage inbound and outbound calling and messaging within the Telnyx interface, without additional software. The AI Assistants tab is located under the AI, Storage and Compute tab on the home screen of the Mission Control Portal.

![AI assistants tab location on the mission control telnyx portal](_images/d30ba41121383e26.png)

### Creating an AI Assistant

![This is a screenshot of the AI Assistants 'Get Started' Page](_images/a98efff6956ead1f.png)

Popular templates are available for a quick start, such as Lead Qualification, Survey and Feedback Specialist, or Customer Service Representative. You can also build from a blank canvas.

![This is a screenshot of the AI Assistant blank canvas configuration page](_images/47bce7fd97f38290.png)

### Choosing a Model

You can use an open source model such as Qwen, or a model like OpenAI's, ensuring to add the API key in the relevant API key input field. The key can also be saved as an integration secret, hiding it from other org members.

![This is a screenshot of the 'integration secret' pop up which allows Telnyx users to hide their API keys](_images/1eb10803f619658a.png)

### Fallback Model

If your primary model experiences issues, you can choose a fallback model that can step in even mid-call.

### Instructions and Greeting

Use the Instructions field to specify any instructions, greetings, and mannerisms the LLM should use. Dynamic variables can be used to insert real-time call data. The Greeting field specifies the greeting the agent should follow, and also supports dynamic variables.

### Dynamic Variables Webhook URL

If populated, dynamic variables will be fetched from the specified webhook and provided to the assistant in real time.

### Tools

By default, every AI assistant can hang up the call when appropriate. Additional tools can be added via the "add tool" dropdown.

#### Webhook Tool

![This is a screenshot of the "add webhook tool" on the telnyx mission control portal](_images/4fbee1897541f537.png)

- **Name** — descriptive, no spaces (e.g., `call_status_webhook`)
- **Description** — clear explanation of what the webhook does
- **Timeout (ms)** — recommended 1–5 seconds (1000–5000 ms)
- **Method** — Telnyx requires an HTTP 2xx response (e.g., `200 OK`) to confirm successful delivery
- **URL** — the webhook URL where events will be sent (e.g., `https://example.com/webhooks/call-status`)

**Advanced settings (optional):**

- **Headers** — custom headers for authentication or specifying formats (e.g., `Authorization: Bearer your_api_key_here`, `Content-Type: application/json`)
- **Path Parameters** — dynamic values injected into the URL path (e.g., `https://example.com/webhooks/{assistant_id}/status` with `assistant_id=12345`)
- **Query Parameters** — optional key-value pairs appended to the URL (e.g., `?version=1.0&token=secureToken123`)
- **Body Parameters** — custom fields sent in the request body, usually JSON

Example body payload:

```
{ "assistant_id": "12345", "event_type": "call.ended", "timestamp": "2025-09-09T10:45:00Z", "custom_metadata": { "customer_id": "abc-789", "session_id": "xyz-456" } }
```

#### Handoff Tool

![](_images/d27bd3f4ccd23b88.png)

The Handoff tool allows you to add an additional voice AI agent that can help your current agent complete tasks. For example, an accommodation booking agent can hand off to a travel arrangements agent, allowing specialization while working as a team.

- **Unified voice mode** — all agents share the same voice, making the handoff transparent to the user
- **Distinct voice mode** — all assistants retain their voice config, providing a conference-call-like experience

Give your handoff agent a descriptive display name and select the AI assistant to include via the dropdown.

#### Transfer Tool

![](_images/57e1cc56852cd4e0.png)

The Transfer tool moves the call from your AI assistant to a real person who can tackle a challenging aspect of the conversation.

- **From number / SIP URI** — the number the call should be transferred from. When using a phone number, it must be owned by the user or organization and have a connection with an attached outbound voice profile
- **Targets** — name of the target (e.g., Live agent 1)
- **To number / SIP URI** — the destination number or SIP URI (e.g., `sip:user@domain`)
- **Custom headers** — custom headers added to the SIP INVITE during transfer (e.g., Name: AI transfer, Value: Front Desk)

#### Add SIP Refer Tool

![](_images/71726d1391efbb3a.png)

- **Targets** — name of the target (e.g., Live agent 2)
- **Name** — descriptive, aligned with your use case
- **SIP Address** — the SIP sub-domain to refer (e.g., `sip:+14085551234@sip.example.com`)
- **SIP Auth Username / SIP Auth Password**
- **SIP Headers (optional)** — User-User or Diversion
- **Custom headers** — name/value pairs passed on SIP messages (e.g., `X-Campaign-ID: 12345`)

#### Transfer Tool vs SIP Refer Tool

- **Transfer** — used to move a call from one endpoint to another within the same system or application. Example: redirecting a call to a different department within the same organization.
- **SIP Refer** — used to transfer a phone call to another SIP infrastructure during a TeXML call. Example: transferring a call to an external partner's SIP system for further handling.

#### Send DTMF

This tool sends DTMF tones during a call and comes pre-configured. Your AI assistant can send DTMF tones on call to complete IVR options on outbound calls.

#### Add MCP Server

![](_images/c5661ce2e6d94755.png)

MCP (Model Context Protocol) is a protocol for connecting AI models with external tools, data sources, or services. It standardizes how models send requests and receive context/data from outside systems.

- **Name** — descriptive and easy to remember
- **Type** — HTTP or SSE
- **URL**

**SSE (Server-Sent Events)** — provides real-time streaming connections where a server pushes updates to a client over a single, long-lived HTTP connection. It is lightweight, uses plain HTTP, and streams text/event data. Unlike webhooks (new request per event) or WebSockets (bidirectional), SSE is one-way (server → client).

**HTTP** — uses standard HTTP methods (GET, POST, etc.) for structured exchange of context, instructions, and data. Each request is independent and stateless.
