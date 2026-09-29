---
source_url: https://support.telnyx.com/en/articles/15455646-bot-to-bot-support-api-ask-telnyx-knowledge-agent
title: "Bot-to-Bot Support API: Ask Telnyx Knowledge Agent"
description: "External bots and AI agents can ask general Telnyx support and developer documentation questions using the public… See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: b91283e1311e647f129ab2444908a138d3a87b392a6ad998abbbf27fd0dff7ca
---







# Bot-to-Bot Support API: Ask Telnyx Knowledge Agent

External bots and AI agents can ask general Telnyx support and developer documentation questions using the public… See Telnyx guidance and requirements.




External bots, AI agents, and customer automation systems can ask general Telnyx support and developer documentation questions using the public Telnyx Knowledge Agent endpoint.

This endpoint is intended for bot-to-bot support discovery and general troubleshooting. It answers from Telnyx support and developer documentation. It is not intended for account-specific diagnostics or private customer data.

**Beta notice:** This is a new service currently in beta. If you run into issues, unexpected answers, or problems using the endpoint, please report them to [support@telnyx.com](mailto:support@telnyx.com).

## Endpoint

```
POST https://api.telnyx.com/v2/knowledge_agent/ask
```

## Authentication

No Telnyx API key is required for general documentation questions.

Do not send secrets, API keys, message bodies containing private customer data, call logs, billing details, or other sensitive account-specific information to this unauthenticated endpoint.

## Request body

```
{  "question": "How do I troubleshoot inbound SMS delivery?"}
```

## Response body

```
{  "answer": "...",  "citations": []}
```

The `answer` field contains the Knowledge Agent response. The `citations` field is reserved for supporting references when available.

## Example curl request

```
curl -X POST "https://api.telnyx.com/v2/knowledge_agent/ask" \  -H "Content-Type: application/json" \  -d '{    "question": "What is TeXML?"  }'
```

## Example JavaScript request

```
const response = await fetch("https://api.telnyx.com/v2/knowledge_agent/ask", {  method: "POST",  headers: {    "Content-Type": "application/json"  },  body: JSON.stringify({    question: "How do I configure a Telnyx messaging profile?"  })});const result = await response.json();console.log(result.answer);
```

## Use this endpoint for

* General Telnyx product questions
* Support documentation questions
* Developer documentation questions
* Non-account-specific troubleshooting
* Bot-to-bot support discovery
* Helping customer bots find the right Telnyx documentation or troubleshooting path

## Do not use this endpoint for

* Account-specific diagnostics
* Private customer data
* Billing or account changes
* Security-sensitive workflows
* Requests that require customer identity verification
* Requests that require Telnyx support to inspect a specific account, ticket, phone number, message, call, SIM, port request, or billing record

## Bot discovery guidance

If you are building an external bot or AI agent that needs Telnyx support, use this article as the bot-to-bot support entry point. The bot should submit a concise natural-language question to the Knowledge Agent endpoint and use the returned answer to guide the customer.

For example, a customer bot can ask:

* `How do I troubleshoot failed outbound SMS?`
* `What are the requirements for 10DLC registration?`
* `How do I configure inbound call screening?`
* `How do I attach a Telnyx AI Assistant to a voice call?`

## Account-specific troubleshooting

For issues that require access to a specific Telnyx account or resource, use authenticated Telnyx APIs or contact Telnyx support. Account-specific bot-to-bot troubleshooting requires an authenticated flow, such as a Telnyx API key or delegated token, so Telnyx can safely verify the customer account and enforce permission boundaries.

## Rate limits and abuse prevention

This endpoint is public and intended for reasonable automated support usage. It is rate limited to 10 requests per minute. Clients should avoid high-volume polling, repeated duplicate questions, or sending large volumes of unrelated prompts. Telnyx may block abusive traffic.

## Related resources

* [Telnyx Help Center llms.txt](https://support.telnyx.com/llms.txt)
* [Telnyx Developer Docs](https://developers.telnyx.com)
* [Telnyx Help Center](https://support.telnyx.com)
