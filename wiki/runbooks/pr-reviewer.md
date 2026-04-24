---
title: PR Reviewer
summary: Telnyx Inference tool for automatically reviewing Pull Requests at GitHub.
sources:
  - url: https://developers.telnyx.com/docs/inference/pr-reviewer/index
    content_hash: b0c8bc1da601f9591e1d38a2a54210047cc5aa7c31a5103f82ecc559c9b14a7d
updated_at: 2026-04-10T00:00:00Z
---

# PR Reviewer

Telnyx Inference tool for automatically reviewing Pull Requests at GitHub

## Introduction

Welcome to the PR Reviewer by Telnyx GitHub Action! This guide will teach you how to set up and use the PR Reviewer By Telnyx, which leverages open-source language models running on Telnyx GPUs to automatically review your pull requests.

## Prerequisites

* [Sign up for a free Telnyx account](https://telnyx.com/sign-up) if you haven't already.

## Setup guide

### Step 1: Obtain Your Telnyx API Key

1. Log in to your [Telnyx account](https://portal.telnyx.com/).
2. Navigate to the **API Keys** section in the Telnyx portal.
3. Click on **Create API Key**.
4. Copy the generated API key and store it in a secure location.

### Step 2: Add Your Telnyx API Key as a Secret on GitHub

1. In your GitHub repository, go to **Settings** > **Secrets and variables** > **Actions**.
2. Click on **New repository secret**.
3. Name the secret `TELNYX_API_KEY`.
4. Paste your Telnyx API key in the **Value** field and click **Add secret**.

### Step 3: Create the GitHub workflow file

To integrate the Telnyx PR Reviewer into your project, follow these steps:

1. In your repository, create a new file at `.github/workflows/review_pr.yml`.

2. Copy and paste the following configuration into the file:

   ```yaml theme={null}
   name: PR Review

   on:
     pull_request:
       types: [opened, synchronize, reopened]

   permissions:
     pull-requests: write

   jobs:
     review:
       runs-on: ubuntu-latest

       steps:
         - name: PR Review
           uses: team-telnyx/reviewpr@main
           with:
             telnyx_api_key: ${{ secrets.TELNYX_API_KEY }}
             model_name: "meta-llama/Meta-Llama-3.1-8B-Instruct"
   ```

3. Commit the file to your repository.

### Step 4: Optional Configuration

The `model_name` parameter in the workflow file is optional. If omitted, the action will use a default language model. If you wish to specify a different model, replace `'meta-llama/Meta-Llama-3.1-8B-Instruct'` with your desired model from the Telnyx [LLM Library](https://telnyx.com/products/llm-library).

## Core Concepts

### GitHub Actions

GitHub Actions automate workflows directly in your GitHub repository. In this case, the PR Reviewer By Telnyx is triggered by pull request events, such as when a PR is opened or updated.

### Telnyx Inference API

The PR Reviewer By Telnyx uses the Telnyx Inference API to analyze and review the content of pull requests. This API allows interaction with large language models (LLMs) hosted on Telnyx infrastructure.

### Model Selection

Your choice of LLM will affect the quality and behavior of the reviews. You can experiment with different models from the Telnyx [LLM Library](https://telnyx.com/products/llm-library) to find the best fit for your project.

### Automatic PR Reviews

Once configured, the PR Reviewer By Telnyx automatically generates a review for every pull request based on the content, providing suggestions or feedback powered by the chosen language model.

## Not sure how to get started?

| I want to...                    | Relevant Tutorial                                                  |
| :------------------------------ | :----------------------------------------------------------------- |
| Learn more about GitHub Actions | [GitHub Actions Documentation](https://docs.github.com/en/actions) |
| Explore more Telnyx models      | [Telnyx LLM Library](https://telnyx.com/products/llm-library)      |

## Additional references

* Dive into our [Telnyx Inference API documentation](https://developers.telnyx.com/docs/inference)
* Explore our full [API reference](https://developers.telnyx.com/api-reference/chat/create-a-chat-completion)
* Review our [OpenAI Compatibility Matrix](openai-api-migration-guide.md)
* Check out our [pricing page](https://telnyx.com/pricing/inference-api)
