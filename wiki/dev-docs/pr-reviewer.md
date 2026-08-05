---
title: PR Reviewer
summary: The PR Reviewer by Telnyx is a GitHub Action that uses open-source language
  models running on Telnyx GPUs to automatically review pull requests. This guide
  covers setup, configuration, and the core concepts behind the action.
sources:
- url: https://developers.telnyx.com/docs/inference/pr-reviewer
updated_at: 2026-08-05T13:46:29Z
---

# PR Reviewer

The PR Reviewer by Telnyx is a GitHub Action that uses open-source language models running on Telnyx GPUs to automatically review pull requests. This guide covers setup, configuration, and the core concepts behind the action.

## Introduction

The PR Reviewer by Telnyx is a GitHub Action that leverages open-source language models running on Telnyx GPUs to automatically review your pull requests. Once configured, it generates feedback and suggestions on every PR based on its content, powered by the chosen language model.

## Prerequisites

- A free Telnyx account. [Sign up here](https://telnyx.com/sign-up) if you don't already have one.

## Setup guide

### Step 1: Obtain Your Telnyx API Key

1. Log in to your [Telnyx portal](https://portal.telnyx.com/).
2. Navigate to the **API Keys** section.
3. Click **Create API Key**.
4. Copy the generated API key and store it in a secure location.

### Step 2: Add Your Telnyx API Key as a Secret on GitHub

1. In your GitHub repository, go to **Settings** > **Secrets and variables** > **Actions**.
2. Click **New repository secret**.
3. Name the secret `TELNYX_API_KEY`.
4. Paste your Telnyx API key into the **Value** field and click **Add secret**.

### Step 3: Create the GitHub workflow file

1. In your repository, create a new file at `.github/workflows/review_pr.yml`.
2. Copy and paste the following configuration into the file:

   ```
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
             model_name: "zai-org/GLM-5.2"
   ```
3. Commit the file to your repository.

### Step 4: Optional Configuration

The `model_name` parameter in the workflow file is optional. If omitted, the action uses a default language model. To specify a different model, replace the value with any model from the Telnyx [LLM Library](https://telnyx.com/products/llm-library).

## Core Concepts

### GitHub Actions

GitHub Actions automate workflows directly in your GitHub repository. The PR Reviewer is triggered by pull request events, such as when a PR is opened, synchronized, or reopened.

### Telnyx Inference API

The PR Reviewer uses the Telnyx Inference API to analyze and review the content of pull requests. This API allows interaction with large language models (LLMs) hosted on Telnyx infrastructure.

### Model Selection

Your choice of LLM affects the quality and behavior of the reviews. You can experiment with different models from the Telnyx [LLM Library](https://telnyx.com/products/llm-library) to find the best fit for your project.

### Automatic PR Reviews

Once configured, the PR Reviewer automatically generates a review for every pull request based on its content, providing suggestions or feedback powered by the chosen language model.

## Getting started

| I want to… | Relevant Tutorial |
| --- | --- |
| Learn more about GitHub Actions | [GitHub Actions Documentation](https://docs.github.com/en/actions) |
| Explore more Telnyx models | [Telnyx LLM Library](https://telnyx.com/products/llm-library) |

## Additional references

- [Telnyx Inference API documentation](https://developers.telnyx.com/docs/inference)
- [API reference](/api-reference/openai-chat/create-a-chat-completion-openai-compatible)
- [OpenAI Compatibility Matrix](/docs/inference/openai)
- [Telnyx Inference API pricing](https://telnyx.com/pricing/inference-api)
