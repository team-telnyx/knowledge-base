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

*Part 2 of 5 — see also: [Part 1](ai-assistants-configuration--part-1.md), [Part 3](ai-assistants-configuration--part-3.md), [Part 4](ai-assistants-configuration--part-4.md), [Part 5](ai-assistants-configuration--part-5.md)*

Covers advanced configuration options for Telnyx AI assistants, including client-side tools, custom LLM providers, dynamic variables, webhook filler messages, and importing assistants from third-party providers.

## Custom LLM Providers

In addition to standard third-party LLM providers like OpenAI, Gemini, and Groq, you can also power your AI Assistant with any public OpenAI-compatible chat completions endpoint. This includes models hosted using AWS Bedrock, Azure OpenAI, and Baseten or open source inference engines like vLLM and SGLang.

You must have a publicly accessible OpenAI-compatible chat completions endpoint before proceeding with deployment.

### When to use custom LLM providers

Custom LLM providers are ideal for scenarios where you need:

- **Specific model requirements** - Access to proprietary models, fine-tuned models, or the latest releases not yet available through standard providers.
- **Data residency and compliance** - Ensure your data stays within specific geographic regions or private cloud environments.
- **Cost optimization** - Leverage enterprise agreements, reserved capacity, or self-hosted infrastructure for better economics at scale.
- **Advanced model control** - Fine-tune parameters, adjust inference settings, or use specialized configurations for your use case.

### Azure

For this guide, we will deploy [gpt-4o on Azure AI Foundry](https://ai.azure.com/).

First, create or select a resource.

![Azure AI Foundry homepage showing resource selection interface](https://mintcdn.com/telnyx/4tBNWGoUCO9azKQ0/img/foundry-homepage.png?fit=max&auto=format&n=4tBNWGoUCO9azKQ0&q=85&s=cd181956c857fcd3e90736f56071520b)

Then, drill into the resource to find the API key and Azure OpenAI endpoint.

![Azure deployment details page displaying API key and endpoint URL](https://mintcdn.com/telnyx/4tBNWGoUCO9azKQ0/img/foundry-deployment.png?fit=max&auto=format&n=4tBNWGoUCO9azKQ0&q=85&s=ce3887668c59cf5544be057caad29c45)

Create or edit a Telnyx AI Assistant and in the `Agent` tab, check `Use Custom LLM`. Input the endpoint URL as the `Base URL` and append `/openai/v1` and create a new Integration Secret with your API Key.

You will see a dropdown of all possible Azure models but only ones that you have deployed will validate an LLM connection.

![Telnyx portal Agent tab with Azure custom LLM configuration and model dropdown](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/azure-in-portal.png?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=f2218f8ecd094d5c73d310a6553e4e46)

Once you save your assistant you will be able to immediately use your assistant in the Telnyx portal with the `Test Assistant` dropdown.

### Forward metadata to your custom LLM

By default, Telnyx does not include your assistant's dynamic variables in requests to a custom LLM endpoint. If your model gateway or application needs those values, enable `forward_metadata` on the assistant's `external_llm` configuration.

```
{
  "external_llm": {
    "llm_api_key_ref": "integration_secret_id",
    "base_url": "https://your-llm-gateway.example.com/openai/v1",
    "model": "your-model-name",
    "forward_metadata": true
  }
}
```

When `forward_metadata` is `true`, Telnyx adds a top-level `extra_metadata` object to the OpenAI-compatible chat completions request body sent to your custom LLM endpoint when dynamic variables are available. The field defaults to `false` when omitted.

```
{
  "model": "your-model-name",
  "messages": [
    {
      "role": "system",
      "content": "..."
    },
    {
      "role": "user",
      "content": "..."
    }
  ],
  "extra_metadata": {
    "customer_name": "Jane",
    "account_id": "acct_789",
    "telnyx_agent_target": "+13125550100",
    "telnyx_end_user_target": "+13125550123"
  }
}
```

Use this when your external LLM service needs request context for routing, logging, personalization, or retrieval. `extra_metadata` is separate from OpenAI's native `metadata` field, so your endpoint must explicitly read `extra_metadata` from the request body.

### Baseten

For this guide, we will deploy [Llama 3.3 70B on Baseten](https://www.baseten.co/library/llama-3-3-70b-instruct/).

First, click `Deploy Now`.

![Baseten model library page showing Llama 3.3 70B with Deploy Now button](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/baseten-deploy-now.png?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=e18e69c79289241404dc79791cef15f1)

Navigate to the deployment.

![Baseten deployment overview page for Llama 3.3 70B model](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/baseten-deployment.png?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=4acc536813e2c39d4a6926228d5869a8)

Click the API Endpoint button to see the endpoint and generate an API Key. Save these details.

![Baseten deployment page showing API endpoint URL and key generation button](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/baseten-api-key.png?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=d5c8b523a715a89e9b064bc777841e2b)

After about 15 minutes, the deployment should be live.

When it is complete, create or edit a Telnyx AI Assistant and in the `Agent` tab, check `Use Custom LLM`. Input the Baseten Endpoint URL for your deployment as the `Base URL` and create a new Integration Secret with your Baseten API Key.

![Telnyx portal custom LLM configuration showing Base URL input field](https://mintcdn.com/telnyx/fKocYsWR7KyFBdpc/img/custom-url.png?fit=max&auto=format&n=fKocYsWR7KyFBdpc&q=85&s=6f425937b54baa1e3ddccebf35f03a62)

If your base URL supports an OpenAI-compatible /models endpoint the Model Name dropdown will populate automatically. Baseten deployments do not support this endpoint, so you can enter any name for your model here. You can also validate the connection is live before saving your assistant.

![Telnyx portal custom LLM validation interface with connection test button](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/validate-custom-llm.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=5ab0af2d21a5ebdf549fea9400a304f1)

Once you save your assistant you will be able to immediately use your assistant in the Telnyx portal with the `Test Assistant` dropdown as well as review metrics in your Baseten deployment.

![Baseten deployment dashboard displaying usage metrics and performance data](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/baseten-metrics.png?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=bf2275e3896a6351c3e6d0a97c4f3e56)
