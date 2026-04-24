---
title: Configure custom LLM providers for AI assistants
summary: Configure Azure OpenAI, AWS Bedrock, Baseten, or any OpenAI-compatible endpoint as a custom LLM provider for your Telnyx AI assistants.
sources:
  - url: https://developers.telnyx.com/docs/inference/ai-assistants/custom-llm/index
    content_hash: 180b44fe76a1328f32eb21d366ef239fa393d623f37b7c55d1ce8618bc3e32f8
updated_at: 2026-04-10T00:00:00Z
---

# Configure custom LLM providers for AI assistants

Configure Azure OpenAI, AWS Bedrock, Baseten, or any OpenAI-compatible endpoint as a custom LLM provider for your Telnyx AI assistants.

In addition to standard third-party LLM providers like OpenAI, Gemini, and Groq, you can also power your AI Assistant with any public OpenAI-compatible chat completions endpoint. This includes models hosted using AWS Bedrock, Azure OpenAI, and Baseten or open source inference engines like vLLM and SGLang.

> **Note:** You must have a publicly accessible OpenAI-compatible chat completions endpoint before proceeding with deployment.

***

## When to use custom LLM providers

Custom LLM providers are ideal for scenarios where you need:

* **Specific model requirements** - Access to proprietary models, fine-tuned models, or the latest releases not yet available through standard providers.
* **Data residency and compliance** - Ensure your data stays within specific geographic regions or private cloud environments.
* **Cost optimization** - Leverage enterprise agreements, reserved capacity, or self-hosted infrastructure for better economics at scale.
* **Advanced model control** - Fine-tune parameters, adjust inference settings, or use specialized configurations for your use case.

***

## Azure

For this guide, we will deploy [gpt-4o on Azure AI Foundry](https://ai.azure.com/).

First, create or select a resource.

<img alt="Azure AI Foundry homepage showing resource selection interface" />

Then, drill into the resource to find the API key and Azure OpenAI endpoint.

<img alt="Azure deployment details page displaying API key and endpoint URL" />

Create or edit a Telnyx AI Assistant and in the `Agent` tab, check `Use Custom LLM`.

Input the endpoint URL as the `Base URL` and append `/openai/v1` and create a new Integration Secret with your API Key.

You will see a dropdown of all possible Azure models but only ones that you have deployed will validate an LLM connection.

<img alt="Telnyx portal Agent tab with Azure custom LLM configuration and model dropdown" />

Once you save your assistant you will be able to immediately use your assistant in the Telnyx portal with the `Test Assistant` dropdown.

## Baseten

For this guide, we will deploy [Llama 3.3 70B on Baseten](https://www.baseten.co/library/llama-3-3-70b-instruct/).

First, click `Deploy Now`.

<img alt="Baseten model library page showing Llama 3.3 70B with Deploy Now button" />

Navigate to the deployment.

<img alt="Baseten deployment overview page for Llama 3.3 70B model" />

Click the API Endpoint button to see the endpoint and generate an API Key. Save these details.

<img alt="Baseten deployment page showing API endpoint URL and key generation button" />

After about 15 minutes, the deployment should be live.

When it is complete, create or edit a Telnyx AI Assistant and in the `Agent` tab, check `Use Custom LLM`.

Input the Baseten Endpoint URL for your deployment as the `Base URL` and create a new Integration Secret with your Baseten API Key.

<img alt="Telnyx portal custom LLM configuration showing Base URL input field" />

If your base URL supports an OpenAI-compatible /models endpoint the Model Name dropdown will populate automatically.

Baseten deployments do not support this endpoint, so you can enter any name for your model here. You can also validate the connection is live before saving your assistant.

<img alt="Telnyx portal custom LLM validation interface with connection test button" />

Once you save your assistant you will be able to immediately use your assistant in the Telnyx portal with the `Test Assistant` dropdown as well as review metrics in your Baseten deployment.

<img alt="Baseten deployment dashboard displaying usage metrics and performance data" />
