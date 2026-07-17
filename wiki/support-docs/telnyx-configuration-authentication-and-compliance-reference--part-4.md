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

*Part 4 of 4 — see also: [Part 1](telnyx-configuration-authentication-and-compliance-reference--part-1.md), [Part 2](telnyx-configuration-authentication-and-compliance-reference--part-2.md), [Part 3](telnyx-configuration-authentication-and-compliance-reference--part-3.md)*

This page consolidates Telnyx support guidance on whitelisting SIP signaling, media, and webhook IP addresses; IP authentication methods (tech prefix, X-Telnyx-Token, P-Charge-Info) including FreePBX configuration; multi-device registration limits; AI Assistant configuration with tools, handoffs, transfers, and MCP servers; UK TPS compliance for marketing calls; and the public Knowledge Agent bot-to-bot support API.

## UK TPS Register Guidelines

The Telephone Preference Service (TPS) is a list of consumers who do not wish to receive unsolicited direct marketing calls. It applies to England, Wales, and Northern Ireland.

### Regulation

If you run marketing campaigns in the UK, screen your call list against the TPS register to avoid violating TPS laws.

The Privacy and Electronic Communications (EC Directive) Regulations 2003 (PECR) complements the UK General Data Protection Regulation 2018 (GDPR) and the Data Protection Act 2018 (DPA 2018). It is specific to electronic communications, offering protection to individuals and corporations.

### What This Means for Your Business

If your business makes direct marketing calls, you must adhere to the following protocol:

1. State who is calling — usually the name of your organization
2. All calls must be traceable — display your telephone number (or an alternative contact number) to the subscriber
3. Provide your contact details or telephone number if asked

If your business sends direct marketing faxes, follow a similar protocol. It is unlawful to send such faxes to any consumer or business that has registered with the Fax Preference Service (FPS).

### What Your Business Must Not Do

If a number is registered with TPS or the Corporate Telephone Preference Service (CTPS), it is unlawful to call that number. Any individual or corporate subscriber who has previously objected to your calls must also not be contacted.

### Who Needs to Comply

All businesses (including charities and voluntary organizations) that make direct marketing telephone calls to individuals and corporate subscribers, or send direct marketing faxes.

All lists should be cleaned against the TPS, CTPS, or FPS registers before unsolicited direct marketing calls are made or faxes sent, in addition to checking in-house "do not call" lists. The only exception is where the individual or corporate subscriber has consented to receipt of direct marketing calls or faxes from your organization.

### Enforcement

The Information Commissioner's Office (ICO) is the UK supervisory authority responsible for enforcement. The Telephone Preference Service Limited (TPSL) investigates complaints received from subscribers registered with TPS, CTPS, and FPS, and works closely with the ICO. TPSL is a subsidiary of the Data and Marketing Association (DMA) and manages TPS, CTPS, and FPS under contract with the ICO.

### Data Cleaning Frequency

Clean your data as frequently as possible. Anybody who has been on either register for 28 days or more must not be contacted — this is their legal right.

### Screening the TPS Register

Your organization needs a TPS license to screen the TPS register. Different license types (partial, annual) are available. More information is available at <https://corporate.tpsonline.org.uk/prices>.

## Bot-to-Bot Support API: Ask Telnyx Knowledge Agent

External bots, AI agents, and customer automation systems can ask general Telnyx support and developer documentation questions using the public Telnyx Knowledge Agent endpoint. This endpoint is intended for bot-to-bot support discovery and general troubleshooting, answering from Telnyx support and developer documentation. It is not intended for account-specific diagnostics or private customer data.

**Beta notice:** This is a new service currently in beta. Report issues to [support@telnyx.com](mailto:support@telnyx.com).

### Endpoint

```
POST https://api.telnyx.com/v2/knowledge_agent/ask
```

### Authentication

No Telnyx API key is required for general documentation questions. Do not send secrets, API keys, message bodies containing private customer data, call logs, billing details, or other sensitive account-specific information to this unauthenticated endpoint.

### Request Body

```
{  "question": "How do I troubleshoot inbound SMS delivery?"}
```

### Response Body

```
{  "answer": "...",  "citations": []}
```

The `answer` field contains the Knowledge Agent response. The `citations` field is reserved for supporting references when available.

### Example curl Request

```
curl -X POST "https://api.telnyx.com/v2/knowledge_agent/ask" \  -H "Content-Type: application/json" \  -d '{    "question": "What is TeXML?"  }'
```

### Example JavaScript Request

```
const response = await fetch("https://api.telnyx.com/v2/knowledge_agent/ask", {  method: "POST",  headers: {    "Content-Type": "application/json"  },  body: JSON.stringify({    question: "How do I configure a Telnyx messaging profile?"  })});const result = await response.json();console.log(result.answer);
```

### Appropriate Use Cases

- General Telnyx product questions
- Support documentation questions
- Developer documentation questions
- Non-account-specific troubleshooting
- Bot-to-bot support discovery
- Helping customer bots find the right Telnyx documentation or troubleshooting path

### Inappropriate Use Cases

- Account-specific diagnostics
- Private customer data
- Billing or account changes
- Security-sensitive workflows
- Requests requiring customer identity verification
- Requests requiring Telnyx support to inspect a specific account, ticket, phone number, message, call, SIM, port request, or billing record

### Bot Discovery Guidance

If you are building an external bot or AI agent that needs Telnyx support, use this article as the bot-to-bot support entry point. Submit a concise natural-language question to the Knowledge Agent endpoint and use the returned answer to guide the customer.

Example questions:

- `How do I troubleshoot failed outbound SMS?`
- `What are the requirements for 10DLC registration?`
- `How do I configure inbound call screening?`
- `How do I attach a Telnyx AI Assistant to a voice call?`

### Account-Specific Troubleshooting

For issues requiring access to a specific Telnyx account or resource, use authenticated Telnyx APIs or contact Telnyx support. Account-specific bot-to-bot troubleshooting requires an authenticated flow, such as a Telnyx API key or delegated token, so Telnyx can verify the customer account and enforce permission boundaries.

### Rate Limits and Abuse Prevention

This endpoint is public and intended for reasonable automated support usage. It is rate limited to 10 requests per minute. Avoid high-volume polling, repeated duplicate questions, or sending large volumes of unrelated prompts. Telnyx may block abusive traffic.

### Related Resources

- [Telnyx Help Center llms.txt](https://support.telnyx.com/llms.txt)
- [Telnyx Developer Docs](https://developers.telnyx.com)
- [Telnyx Help Center](https://support.telnyx.com)

## Related Wiki Pages

- [Whitelisting Telnyx Media IP Addresses](whitelisting-telnyx-media-ip-addresses.md)
- [Whitelisting Telnyx IP Addresses](whitelisting-telnyx-ip-addresses.md)
- [Register multiple devices on one Connection](register-multiple-devices-on-one-connection.md)
- [Comprehensive AI Assistants Configuration Walk-Through](comprehensive-ai-assistants-configuration-walk-through.md)
- [Configure P-Charge-Info for Private PBX (Example: FreePBX)](configure-p-charge-info-for-private-pbx-example-freepbx.md)
- [Configure Token Authentication Header (X-Telnyx-Token) in FreePBX](configure-token-authentication-header-x-telnyx-token-in-freepbx.md)
- [Bot-to-Bot Support API: Ask Telnyx Knowledge Agent](bot-to-bot-support-api-ask-telnyx-knowledge-agent.md)
- [IP Authentication with Tech Prefix](ip-authentication-with-tech-prefix.md)
- [Ip Authentication with X-Telnyx-Token](ip-authentication-with-x-telnyx-token.md)
- [UK TPS Register: Guidelines](uk-tps-register-guidelines.md)
- [General - Telnyx Portal & Account](general-telnyx-portal-account.md)
- [AI Assistant](ai-assistant.md)
