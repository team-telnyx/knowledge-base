---
title: Telnyx Network, Webhook, and Push Notification Configuration
summary: This page consolidates Telnyx guidance on whitelisting SIP signaling, media,
  and webhook IP addresses; configuring and verifying webhooks (including signature
  rotation); setting up iOS and Android push notifications for the WebRTC SDK; and
  accessing support resources such as the status page, bug reporting, and the Bot-to-Bot
  Knowledge Agent API.
sources:
- url: https://support.telnyx.com/en/articles/10007243-whitelisting-telnyx-media-ip-addresses
- url: https://support.telnyx.com/en/articles/1130687-whitelisting-telnyx-ip-addresses
- url: https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent
- url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
- url: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
- url: https://support.telnyx.com/en/articles/6707731-telnyx-status-page
- url: https://support.telnyx.com/en/articles/8268140-android-push-notification-setup
- url: https://support.telnyx.com/en/articles/8268170-how-to-setup-ios-push-notifications
- url: https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide
- url: https://support.telnyx.com/en/collections/133094-general-telnyx-portal-account
- url: https://support.telnyx.com/en/collections/5782829-webrtc-voice-sdk
updated_at: 2026-08-05T13:24:23Z
---

# Telnyx Network, Webhook, and Push Notification Configuration

*Part 5 of 5 — see also: [Part 1](telnyx-network-webhook-and-push-notification-configuration--part-1.md), [Part 2](telnyx-network-webhook-and-push-notification-configuration--part-2.md), [Part 3](telnyx-network-webhook-and-push-notification-configuration--part-3.md), [Part 4](telnyx-network-webhook-and-push-notification-configuration--part-4.md)*

This page consolidates Telnyx guidance on whitelisting SIP signaling, media, and webhook IP addresses; configuring and verifying webhooks (including signature rotation); setting up iOS and Android push notifications for the WebRTC SDK; and accessing support resources such as the status page, bug reporting, and the Bot-to-Bot Knowledge Agent API.

## Bug Reports and Security Disclosure

### Submitting Bug Reports

Telnyx is engineering-focused and iterates quickly, shipping improvements and new features regularly. Customers are encouraged to report bugs and improvements by contacting [support@telnyx.com](mailto:support@telnyx.com). A detailed description of the bug, along with screenshots or videos, is always appreciated.

The Mission Control Portal UI is built on top of the Telnyx API, so browser console logs (for front-end issues) and network logs (for back-end issues) can significantly help reproduce concerns.

Step-by-step guide:

1. Note the browser and version you are using.
2. Open the developer tools (typically F12, or right-click → **Inspect** / **Inspect element**).
3. Navigate to the page where you have an issue.
4. Open the **Network** or **Console** tab.
5. For back-end issues, use the **Network** tab to inspect traffic. You can save a HAR file by right-clicking the failing request and selecting **Save HAR file**.
6. For front-end issues, use the **Console** tab to inspect console logs. You can filter by type (Errors, Warnings). If you see red logs, right-click the whitespace and save the console logs.
7. These files are very useful for determining the cause.

If the bug is mission critical (service affecting), open a chat with support for immediate investigation.

### Security Vulnerability Disclosure

If you believe you have found a security vulnerability, report it to **security@telnyx.com** rather than general support. Telnyx welcomes responsible security research on its products and infrastructure.

**Scope:** Telnyx-owned web applications, APIs, and infrastructure, including `portal.telnyx.com`, `api.telnyx.com`, and other `*.telnyx.com` properties.

**Out of scope:** Third-party services and integrations, physical security, social engineering against employees, and denial-of-service testing.

**What Telnyx is looking for:** Vulnerabilities with demonstrated, real-world security impact, such as remote code execution, injection flaws, authentication or authorization bypass, access to other users' data, and significant data exposure.

**What does not qualify:** Configuration hardening suggestions or best-practice recommendations without a working exploit; informational findings with no demonstrated security impact (version disclosure, missing headers, cookie attributes); issues requiring unlikely user interaction or only affecting the reporter's own session; automated scanner output without manual validation and a clear proof of concept; and telecom service abuse, carrier routing, or call quality issues.

**Report requirements:** A description of the vulnerability and affected component; step-by-step reproduction instructions; proof of concept (screenshots, requests and responses, video, or exploit code); and demonstrated impact.

**Rules:** Do not access or modify other users' data; do not degrade service availability; test only against your own accounts; do not disclose the issue publicly before Telnyx has had reasonable time to remediate; stop and report immediately if you encounter customer data.

**Rewards:** Telnyx may offer rewards for qualifying reports at its sole discretion, based on severity, exploitability, and impact. Informational findings and out-of-scope reports are not eligible.

**Submission:** Send security reports to **security@telnyx.com** with the subject `[Vulnerability Report] <Brief Description>`.

**Safe Harbor:** Telnyx will not pursue legal action against researchers who act in good faith, follow this policy, and report findings to Telnyx before any public disclosure.

## Bot-to-Bot Support API: Ask Telnyx Knowledge Agent

External bots, AI agents, and customer automation systems can ask general Telnyx support and developer documentation questions using the public Telnyx Knowledge Agent endpoint. This endpoint is intended for bot-to-bot support discovery and general troubleshooting. It answers from Telnyx support and developer documentation and is not intended for account-specific diagnostics or private customer data.

**Beta notice:** This is a new service currently in beta. If you run into issues, unexpected answers, or problems using the endpoint, report them to [support@telnyx.com](mailto:support@telnyx.com).

### Endpoint

```
POST https://api.telnyx.com/v2/knowledge_agent/ask
```

### Authentication

No Telnyx API key is required for general documentation questions. Do not send secrets, API keys, message bodies containing private customer data, call logs, billing details, or other sensitive account-specific information to this unauthenticated endpoint.

### Request Body

```
{ "question": "How do I troubleshoot inbound SMS delivery?" }
```

### Response Body

```
{ "answer": "...", "citations": [] }
```

The `answer` field contains the Knowledge Agent response. The `citations` field is reserved for supporting references when available.

### Example curl Request

```
curl -X POST "https://api.telnyx.com/v2/knowledge_agent/ask" \
  -H "Content-Type: application/json" \
  -d '{ "question": "What is TeXML?" }'
```

### Example JavaScript Request

```
const response = await fetch("https://api.telnyx.com/v2/knowledge_agent/ask", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ question: "How do I configure a Telnyx messaging profile?" })
});
const result = await response.json();
console.log(result.answer);
```

### When to Use This Endpoint

Use it for general Telnyx product questions, support documentation questions, developer documentation questions, non-account-specific troubleshooting, bot-to-bot support discovery, and helping customer bots find the right Telnyx documentation or troubleshooting path.

Do not use it for account-specific diagnostics, private customer data, billing or account changes, security-sensitive workflows, requests that require customer identity verification, or requests that require Telnyx support to inspect a specific account, ticket, phone number, message, call, SIM, port request, or billing record.

### Bot Discovery Guidance

If you are building an external bot or AI agent that needs Telnyx support, use this article as the bot-to-bot support entry point. Submit a concise natural-language question to the Knowledge Agent endpoint and use the returned answer to guide the customer. Example questions include:

- `How do I troubleshoot failed outbound SMS?`
- `What are the requirements for 10DLC registration?`
- `How do I configure inbound call screening?`
- `How do I attach a Telnyx AI Assistant to a voice call?`

### Account-Specific Troubleshooting

For issues that require access to a specific Telnyx account or resource, use authenticated Telnyx APIs or contact Telnyx support. Account-specific bot-to-bot troubleshooting requires an authenticated flow, such as a Telnyx API key or delegated token, so Telnyx can safely verify the customer account and enforce permission boundaries.

### Rate Limits and Abuse Prevention

This endpoint is public and intended for reasonable automated support usage. It is rate limited to 10 requests per minute. Clients should avoid high-volume polling, repeated duplicate questions, or sending large volumes of unrelated prompts. Telnyx may block abusive traffic.

### Related Resources

- [Telnyx Help Center llms.txt](https://support.telnyx.com/llms.txt)
- [Telnyx Developer Docs](https://developers.telnyx.com)
- [Telnyx Help Center](https://support.telnyx.com)
