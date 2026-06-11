---
title: AI Assistants
summary: Telnyx AI Assistants are configurable voice and text agents that support
  multi-agent handoff, dynamic variables, persistent memory, async tool execution,
  enterprise integrations, custom LLM providers, Langfuse observability, and migration
  from other providers — all orchestrated through the Mission Control Portal or API.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-handoff
  content_hash: 70a4981634a6392849db64eb9505dc98ed11f2c816e1a5a90809b02d509e14b1
- url: https://developers.telnyx.com/docs/inference/ai-assistants/agent-observability
  content_hash: fef9a26ab4abb9421515d4444216948ad9d6348ed5eebc66c50729e9ab27e71a
- url: https://developers.telnyx.com/docs/inference/ai-assistants/async-tools/index
  content_hash: 4305d6ceba22801446c835423e7dad2029e48c5d186c3358bde90d33d9cf2d90
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
  content_hash: 26757cd4f78fd56c2320d158d13becea98fbb06936445b505a2075cdd609a686
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
  content_hash: 3d2eeb67ed78ad9cf2e5fd0a52e0b6b017bf273d08335395bf9df845a2f4bacf
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
  content_hash: c1af4766c041fd4740d0e4a329bb36fb52a550bc0e8b28684ba40e1aa0274ac4
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
  content_hash: 4441f80ea6c53c4f58838df0f99b66bd3cc4779b2c8415f970c5a4d17dab9d77
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
  content_hash: c7ecb160d4f9b143af3c70bcb729def8e69d59ff8b3f872b15654bf3b3971030
updated_at: 2026-06-11T10:29:30Z
---

# AI Assistants

*Part 3 of 4 — see also: [Part 1](ai-assistants--part-1.md), [Part 2](ai-assistants--part-2.md), [Part 4](ai-assistants--part-4.md)*

Telnyx AI Assistants are configurable voice and text agents that support multi-agent handoff, dynamic variables, persistent memory, async tool execution, enterprise integrations, custom LLM providers, Langfuse observability, and migration from other providers — all orchestrated through the Mission Control Portal or API.

## Enterprise Integrations

Telnyx AI assistants can integrate with leading enterprise platforms to access data, create tickets, update records, and automate workflows directly during conversations.

### Available integrations

| Integration | Key capabilities |
|---|---|
| **Salesforce** | Search/create/update records, run SOQL queries |
| **ServiceNow** | Create incidents, update tickets, search knowledge base, query CMDB |
| **Jira** | Create/update/search issues, add comments, transition issues |
| **HubSpot** | Manage contacts, deal tracking, ticket management, engagement logging |
| **Zendesk** | Create tickets, search customer history, update ticket status, search KB |
| **Intercom** | Access conversation history, create notes, update customer attributes, search users |
| **GitHub** | Create issues, search repositories, manage pull requests, access code |
| **Greenhouse** | Candidate lookup, interview scheduling, application management, scorecard review |
| **Coval** | Automated scenario simulation, CI/CD regression testing, production monitoring, built-in evaluation metrics |

Coval is a testing and evaluation tool rather than a conversation-time tool — it tests and monitors the assistant itself.

### Connection workflow

1. Open your assistant in the [Mission Control Portal](https://portal.telnyx.com/#/ai/assistants).
2. Select the **Integrations** tab.
3. Click **Add Integration**, choose a provider, and enter credentials.
4. Enable the tools you need and save.

### Credential requirements

Each integration requires platform-specific credentials:

- **Salesforce** — Instance domain, username, password, security token, organisation ID.
- **ServiceNow** — Instance URL, username, password.
- **Jira** — Account email, API token, site URL.
- **HubSpot** — Private app token.
- **Zendesk** — Subdomain, email, API token.
- **Intercom** — Access token.
- **GitHub** — Personal access token.
- **Greenhouse** — Harvest API key.
- **Coval** — Coval API key.

Credentials are stored securely and can be managed on the [Integration Secrets](https://portal.telnyx.com/#/integration-secrets) page.

### Managing integrations

- **Disconnect** — Removes the integration from the current assistant (tools are disabled); the integration remains in your account and can be reconnected.
- **Delete** — Permanently removes the integration and all stored credentials from your account.

### Security best practices

- Use dedicated service accounts with minimal permissions.
- Rotate credentials regularly.
- Start with read-only tools before enabling write actions.
- Test integrations in sandbox environments first.

## Custom LLM Providers

In addition to standard providers (OpenAI, Gemini, Groq), you can power an assistant with any publicly accessible OpenAI-compatible chat completions endpoint — including models hosted on AWS Bedrock, Azure OpenAI, Baseten, or open-source inference engines like vLLM and SGLang.

### When to use custom LLM providers

- **Specific model requirements** — Access proprietary or fine-tuned models not available through standard providers.
- **Data residency and compliance** — Keep data within specific regions or private cloud environments.
- **Cost optimisation** — Leverage enterprise agreements or self-hosted infrastructure.
- **Advanced model control** — Fine-tune parameters or use specialised configurations.

### Azure OpenAI

1. Deploy a model (e.g., GPT-4o) on Azure AI Foundry.
2. Note the API key and Azure OpenAI endpoint.
3. In the assistant's **Agent** tab, check **Use Custom LLM**.
4. Set the Base URL to the Azure endpoint appended with `/openai/v1`.
5. Create an Integration Secret with your API key.
6. Select the deployed model from the dropdown and save.

### Baseten

1. Deploy a model (e.g., Llama 3.3 70B) on Baseten.
2. Copy the API endpoint URL and generate an API key.
3. In the assistant's **Agent** tab, check **Use Custom LLM**.
4. Set the Base URL to the Baseten endpoint URL.
5. Create an Integration Secret with your Baseten API key.
6. Enter a model name (Baseten does not support the `/models` endpoint) and validate the connection.

### Forwarding metadata to your custom LLM

By default, Telnyx does not include dynamic variables in requests to custom LLM endpoints. Enable `forward_metadata` in the `external_llm` configuration to add an `extra_metadata` object to the request body:

```json
{
  "external_llm": {
    "llm_api_key_ref": "integration_secret_id",
    "base_url": "https://your-llm-gateway.example.com/openai/v1",
    "model": "your-model-name",
    "forward_metadata": true
  }
}
```

When enabled and dynamic variables are available, Telnyx adds `extra_metadata` containing the resolved variable values (including `telnyx_agent_target` and `telnyx_end_user_target`) to the chat completions request. `extra_metadata` is separate from OpenAI's native `metadata` field.
