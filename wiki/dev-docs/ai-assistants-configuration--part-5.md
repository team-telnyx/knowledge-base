---
title: AI Assistants Configuration
summary: Covers advanced configuration options for Telnyx AI assistants, including
  client-side tools, custom LLM providers, dynamic variables, webhook filler messages,
  and importing assistants from third-party providers.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/client-side-tools
- url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm
- url: https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables
- url: https://developers.telnyx.com/docs/inference/ai-assistants/filler-messages
- url: https://developers.telnyx.com/docs/inference/ai-assistants/importing/index
updated_at: 2026-08-05T13:45:16Z
---

# AI Assistants Configuration

*Part 5 of 5 — see also: [Part 1](ai-assistants-configuration--part-1.md), [Part 2](ai-assistants-configuration--part-2.md), [Part 3](ai-assistants-configuration--part-3.md), [Part 4](ai-assistants-configuration--part-4.md)*

Covers advanced configuration options for Telnyx AI assistants, including client-side tools, custom LLM providers, dynamic variables, webhook filler messages, and importing assistants from third-party providers.

## Importing Assistants from another Provider

If you have voice assistants with another provider, you can import them to Telnyx in the portal or [via API](https://developers.telnyx.com/api-reference/assistants/import-assistants-from-external-provider#import-assistants-from-external-provider).

### Supported Providers

Telnyx currently supports importing assistants from:

- **Vapi** - Import your Vapi voice assistants with all configurations.
- **ElevenLabs** - Import your ElevenLabs conversational AI agents.
- **Retell** - Import your single- and multi-prompt Retell agents.

### Import Walkthrough

#### Importing from Vapi

##### Viewing your Assistants

From the [assistants page](https://portal.telnyx.com/#/ai/assistants), you can select **Import Assistants**.

![AI Assistant List Import](https://mintcdn.com/telnyx/JbAKfH7SbyeZcDpH/img/list-assistants-import-vapi.png?fit=max&auto=format&n=JbAKfH7SbyeZcDpH&q=85&s=323348a9d2c0a94c57a5185923859813)

##### Selecting your Provider

On the next page, select **Vapi** from the provider list and securely store your Vapi API Key with Telnyx to initiate the import.

*Any assistant that has already been imported will be overwritten with its latest version from Vapi.*

![Import Assistants Page](https://mintcdn.com/telnyx/tKcWw-YZ6CuwkRsC/img/import-assistants-vapi.png?fit=max&auto=format&n=tKcWw-YZ6CuwkRsC&q=85&s=c20e68ac35e7cd9fe7881314d2e255f7)

##### Selecting your Assistants

You can then select which Vapi assistants to import.

*[Trial accounts](https://developers.telnyx.com/docs/account-setup/account-upgrade) have a limit of 1 AI Assistant.*

![Import Assistants Page](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/select-vapi-ai-import.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=03f75db20ef8be5f7c8e1ec668206171)

##### Testing your imported Assistant

You should now see your new assistants listed and can click the pencil icon to edit or the telephone icon to test them in the portal. Check out the [quickstart tutorial](https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant) for more information on editing or creating our Assistants.

#### Importing from ElevenLabs

##### Viewing your Assistants

From the [assistants page](https://portal.telnyx.com/#/ai/assistants), you can select **Import Assistants**.

![AI Assistant List Import](https://mintcdn.com/telnyx/JbAKfH7SbyeZcDpH/img/list-assistants-import.png?fit=max&auto=format&n=JbAKfH7SbyeZcDpH&q=85&s=181949f2e4b92d8babd5d4559a65e964)

##### Selecting your Provider

On the next page, select **ElevenLabs** from the provider list and securely store your ElevenLabs API Key with Telnyx to initiate the import.

*Any assistant that has already been imported will be overwritten with its latest version from ElevenLabs.*

![Import Assistants Page](https://mintcdn.com/telnyx/tKcWw-YZ6CuwkRsC/img/import-ai.png?fit=max&auto=format&n=tKcWw-YZ6CuwkRsC&q=85&s=67629929117bcc087eae6d7f3697accb)

##### Selecting your Assistants

You can then select which ElevenLabs agents to import.

*[Trial accounts](https://developers.telnyx.com/docs/account-setup/account-upgrade) have a limit of 1 AI Assistant.*

![Import Assistants Page](https://mintcdn.com/telnyx/piPv--L_2q5NFR4U/img/select-ai-import.png?fit=max&auto=format&n=piPv--L_2q5NFR4U&q=85&s=8960d6181d9d9a24c1d78b6d48feacaf)

##### Testing your imported Assistant

You should now see your new assistants listed and can click the pencil icon to edit or the telephone icon to test them in the portal. Check out the [quickstart tutorial](https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant) for more information on editing or creating our Assistants.

### Supported Import Functionality

#### Instructions

Your assistant's instructions will be imported as is.

#### Greeting (a.k.a. first message)

Your assistant's greeting will be imported as is.

#### LLM

By default, the LLM assistant will be set to our flagship on-prem LLM, which provides optimal latency, cost, and intelligence. You can BYO LLM with third-party providers by storing an API Key.

#### Voice

When importing from Vapi or ElevenLabs, the voice will be imported as is. Otherwise, the LLM assistant will be set to our flagship on-prem TTS, which provides optimal latency, cost, and realism. You can BYO TTS with other third-party providers by storing an API Key.

#### Dynamic Variables

References to dynamic variables and their defaults will be imported as is. See our [guide](https://developers.telnyx.com/docs/inference/ai-assistants/dynamic-variables) on how to set these values per call.

#### Tools

Hangup, transfer, and webhook tools will be imported as is.

#### MCP Servers (a.k.a. Integrations)

Integrations with MCP Servers will be imported as is.

#### Insights (a.k.a. analysis, success criteria, structured data…)

Structured and unstructured call analysis configuration is imported as is.

#### Data Retention

If you have disabled data retention with another provider, this setting will be imported as is.

#### Knowledge Bases

Telnyx will not import your knowledge base by default. You can easily drag and drop files or import website content for your assistant in the assistant builder.

![Knowledge Base Page](https://mintcdn.com/telnyx/JbAKfH7SbyeZcDpH/img/knowledge-base-upload.png?fit=max&auto=format&n=JbAKfH7SbyeZcDpH&q=85&s=07cac08f421b818e0e1d1f5ae30e343f)

#### Secrets

Telnyx will create placeholder integration secrets for you with the same name as they are configured in the importing provider. You will need to resupply the value of the secret on the Telnyx [integration secrets page](https://portal.telnyx.com/#/integration-secrets).

![Knowledge Base Page](https://mintcdn.com/telnyx/fKocYsWR7KyFBdpc/img/edit-integration-secret.png?fit=max&auto=format&n=fKocYsWR7KyFBdpc&q=85&s=6fa31a0610378b0e8fcc67717387f9ef)
