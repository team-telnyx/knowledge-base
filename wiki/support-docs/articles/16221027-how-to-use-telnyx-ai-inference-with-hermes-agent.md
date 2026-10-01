---
title: "How to use Telnyx AI Inference with Hermes Agent"
summary: "The Telnyx integration is a vendor-maintained external Hermes model-provider plugin. It connects Hermes to the OpenAI-compatible Telnyx Chat Completions API, supports streaming and tool calling, and retrieves the models available to your Telnyx account."
sources:
- url: "https://support.telnyx.com/en/articles/16221027-how-to-use-telnyx-ai-inference-with-hermes-agent"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/16221027-how-to-use-telnyx-ai-inference-with-hermes-agent.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/16221027-how-to-use-telnyx-ai-inference-with-hermes-agent.md -->

# How to use Telnyx AI Inference with Hermes Agent

The Telnyx integration is a vendor-maintained external Hermes model-provider plugin. It connects Hermes to the OpenAI-compatible Telnyx Chat Completions API, supports streaming and tool calling, and retrieves the models available to your Telnyx account.

**Primary references**

- [Telnyx Hermes inference-provider repository](https://github.com/team-telnyx/hermes-inference-provider)
- [Telnyx Hermes provider README](https://github.com/team-telnyx/hermes-inference-provider/blob/main/README.md)
- [Telnyx Hermes provider manifest](https://github.com/team-telnyx/hermes-inference-provider/blob/main/plugin.yaml)
- [Telnyx Hermes provider release `v0.1.0-rc.1`](https://github.com/team-telnyx/hermes-inference-provider/releases/tag/v0.1.0-rc.1)
- [Hermes model-provider plugin architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin)
- [Telnyx Inference API quickstart](https://developers.telnyx.com/docs/inference/getting-started)
- [Telnyx available inference models](https://developers.telnyx.com/docs/inference/models)

## What you will configure

By the end of this guide, you will have:

- Hermes Agent installed.
- The Telnyx model-provider plugin installed in Hermes’s provider-discovery directory.
- A Telnyx API key available to Hermes.
- A Telnyx model selected for interactive and scripted tasks.
- A working Hermes conversation using Telnyx AI Inference.
- A documented path for updating, troubleshooting, and removing the integration.

## Integration status

The Telnyx provider is currently available as the prerelease:

```
v0.1.0-rc.1
```

The release was published from commit:

```
5ce06f2
```

It was validated against:

```
NousResearch/hermes-agent@ae6c2e57e12b2f320175e3b9bb1bc13c3402255e
```

The release supports Python 3.11–3.13. Release candidates currently track the Hermes main branch. Stable `v0.1.0` is expected to pin the first released Hermes version that automatically routes plugins declared as `kind: model-provider` into the correct discovery directory.

References:

- [Telnyx provider release `v0.1.0-rc.1`](https://github.com/team-telnyx/hermes-inference-provider/releases/tag/v0.1.0-rc.1)
- [Telnyx provider compatibility notes](https://github.com/team-telnyx/hermes-inference-provider#compatibility)

## Current installation limitation

Hermes discovers external model providers under:

```
$HERMES_HOME/plugins/model-providers/
```

The default location is:

```
~/.hermes/plugins/model-providers/
```

The current generic plugin installer initially clones plugins into:

```
~/.hermes/plugins/
```

For this release, you must therefore move the installed Telnyx plugin into the `model-providers` subdirectory. This manual step should become unnecessary after Hermes ships provider-aware installation routing.

References:

- [Telnyx provider installation instructions](https://github.com/team-telnyx/hermes-inference-provider#install)
- [Telnyx post-install instructions](https://github.com/team-telnyx/hermes-inference-provider/blob/main/after-install.md)
- [Hermes model-provider discovery](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin#how-discovery-works)

## Prerequisites

You need:

- A [Telnyx account](https://portal.telnyx.com/).
- A Telnyx API key.
- Git.
- A Hermes-supported operating system.
- Internet access from the machine running Hermes.
- Python 3.11–3.13 for the currently validated provider path.

Hermes supports command-line installation on Linux, macOS, WSL2, native Windows, and Android through Termux. The standard installer manages Python, Node.js, the Hermes virtual environment, and other application dependencies.

References:

- [Hermes installation guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation/)
- [Hermes platform support](https://hermes-agent.nousresearch.com/docs/getting-started/platform-support)
- [Telnyx provider compatibility](https://github.com/team-telnyx/hermes-inference-provider#compatibility)

## Step 1: Install Hermes Agent

Skip this step when Hermes is already installed and `hermes doctor` completes successfully.

### Linux, macOS, WSL2, or Termux

Run the official installer:

```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Reload the shell after installation:

```
source ~/.bashrc
```

For Zsh:

```
source ~/.zshrc
```

References:

- [Hermes installation guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation/)
- [Hermes quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart/)

For a headless environment that does not need browser automation:

```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh \   | bash -s -- --skip-browser
```

Reference: [Hermes headless installation options](https://hermes-agent.nousresearch.com/docs/getting-started/installation/#non-sudo--system-service-user-installs)

### Native Windows

Open PowerShell and run:

```
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

References:

- [Hermes installation guide](https://hermes-agent.nousresearch.com/docs/getting-started/installation/)
- [Hermes native Windows guide](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native)

### Verify the installation

Run:

```
hermes doctor
```

You can also check the installed CLI:

```
hermes --version
```

The normal per-user installation stores Hermes under:

```
~/.hermes/
```

The standard per-user layout includes:

```
~/.hermes/hermes-agent/    Hermes source and runtime ~/.hermes/config.yaml      Main configuration ~/.hermes/.env             API keys and environment values ~/.hermes/plugins/         User-installed plugins
```

References:

- [Hermes installation layout](https://hermes-agent.nousresearch.com/docs/getting-started/installation/#install-layout)
- [Hermes configuration](https://hermes-agent.nousresearch.com/docs/user-guide/configuration/)

## Step 2: Create a Telnyx API key

Sign in to the [Telnyx Mission Control Portal](https://portal.telnyx.com/).

Open the API Keys section:

<https://portal.telnyx.com/#/app/api-keys>

Then:

1. Select **Create API Key**.
2. Give the key a descriptive name, such as `Hermes development`.
3. Configure its expiration and access settings.
4. Create the key.
5. Copy it immediately and store it securely.

Telnyx only displays the complete key at creation time.

References:

- [Create and manage Telnyx API keys](https://developers.telnyx.com/development/api-fundamentals/create-api-keys)
- [Telnyx API authentication](https://developers.telnyx.com/development/api-fundamentals/authentication)

Do not:

- Commit the key to Git.
- Put it in a public configuration file.
- Add it to client-side browser code.
- Include it in screenshots or application logs.
- Reuse a production key in development.

Telnyx recommends storing API keys in environment variables or a secrets manager, separating development and production credentials, and rotating keys periodically.

Reference: [Telnyx authentication security practices](https://developers.telnyx.com/development/api-fundamentals/authentication)

## Step 3: Install the Telnyx provider

Two installation paths are available.

### Option A: Install through the Hermes plugin command

This is the simplest path and follows the plugin repository’s primary instructions.

Run:

```
hermes plugins install team-telnyx/hermes-inference-provider
```

The installer reads the plugin manifest, detects the required `TELNYX_API_KEY`, prompts for it using a masked input, and saves the value to:

```
~/.hermes/.env
```

The installer may also ask:

```
Enable 'telnyx-provider' now? [y/N]
```

That general plugin toggle does not activate or deactivate a model-provider plugin. Model providers are activated by selecting them through `hermes model` or by passing `--provider telnyx` when launching a session.

References:

- [Telnyx provider installation](https://github.com/team-telnyx/hermes-inference-provider#option-a--hermes-installer--one-move)
- [Telnyx plugin manifest](https://github.com/team-telnyx/hermes-inference-provider/blob/main/plugin.yaml)
- [Hermes plugin installation](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins/#managing-plugins)
- [Hermes model-provider activation](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins/#what-the-allow-list-does-not-gate)

### Move the provider into the discovery directory

On Linux, macOS, or WSL2:

```
mkdir -p ~/.hermes/plugins/model-providers  mv ~/.hermes/plugins/telnyx-provider \   ~/.hermes/plugins/model-providers/
```

The resulting location should be:

```
~/.hermes/plugins/model-providers/telnyx-provider/
```

References:

- [Telnyx provider README](https://github.com/team-telnyx/hermes-inference-provider#option-a--hermes-installer--one-move)
- [Telnyx post-install instructions](https://github.com/team-telnyx/hermes-inference-provider/blob/main/after-install.md)
- [Hermes model-provider discovery directory](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin#how-discovery-works)

On native Windows PowerShell, use the equivalent directory move:

```
New-Item `   -ItemType Directory `   -Force `   "$HOME\.hermes\plugins\model-providers" | Out-Null  Move-Item `   "$HOME\.hermes\plugins\telnyx-provider" `   "$HOME\.hermes\plugins\model-providers\telnyx-provider"
```

The Windows command uses the same Hermes home and provider-discovery paths described by the plugin and Hermes documentation.

References:

- [Hermes native Windows data layout](https://hermes-agent.nousresearch.com/docs/user-guide/windows-native)
- [Hermes model-provider plugin directory](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin)

### Option B: Install the exact release candidate with Git

This option pins the installation to `v0.1.0-rc.1` instead of cloning the changing main branch.

On Linux, macOS, or WSL2:

```
mkdir -p ~/.hermes/plugins/model-providers  git clone \   --branch v0.1.0-rc.1 \   --depth 1 \   https://github.com/team-telnyx/hermes-inference-provider \   ~/.hermes/plugins/model-providers/telnyx
```

The provider will be installed at:

```
~/.hermes/plugins/model-providers/telnyx/
```

References:

- [Telnyx provider Git installation](https://github.com/team-telnyx/hermes-inference-provider#option-b--plain-git-clone)
- [Telnyx release `v0.1.0-rc.1`](https://github.com/team-telnyx/hermes-inference-provider/releases/tag/v0.1.0-rc.1)
- [Hermes external provider directory](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin)

On native Windows PowerShell:

```
New-Item `   -ItemType Directory `   -Force `   "$HOME\.hermes\plugins\model-providers" | Out-Null  git clone `   --branch v0.1.0-rc.1 `   --depth 1 `   https://github.com/team-telnyx/hermes-inference-provider `   "$HOME\.hermes\plugins\model-providers\telnyx"
```

## Step 4: Verify the provider files

List the provider directories:

```
find ~/.hermes/plugins/model-providers \   -maxdepth 2 \   -name plugin.yaml \   -print
```

You should see either:

```
~/.hermes/plugins/model-providers/telnyx-provider/plugin.yaml
```

or:

```
~/.hermes/plugins/model-providers/telnyx/plugin.yaml
```

depending on the installation method.

Inspect the plugin manifest:

```
cat ~/.hermes/plugins/model-providers/telnyx-provider/plugin.yaml
```

For the pinned Git path:

```
cat ~/.hermes/plugins/model-providers/telnyx/plugin.yaml
```

The manifest should declare:

```
manifest_version: 1 name: telnyx-provider kind: model-provider version: 0.1.0-rc.1 author: Telnyx
```

It should also declare `TELNYX_API_KEY` as a required secret.

Reference: [Telnyx provider manifest](https://github.com/team-telnyx/hermes-inference-provider/blob/main/plugin.yaml)

## Step 5: Configure the Telnyx API key

Skip this step if the plugin installer already prompted for and saved the key.

The provider reads:

```
TELNYX_API_KEY
```

The normal Hermes environment file is:

```
~/.hermes/.env
```

Add the following entry:

```
TELNYX_API_KEY=KEY_your_api_key_here
```

References:

- [Telnyx provider configuration](https://github.com/team-telnyx/hermes-inference-provider#install)
- [Telnyx provider manifest](https://github.com/team-telnyx/hermes-inference-provider/blob/main/plugin.yaml)
- [Telnyx API authentication](https://developers.telnyx.com/development/api-fundamentals/authentication)

Alternatively, expose the key to the current process as an environment variable:

```
export TELNYX_API_KEY="KEY_your_api_key_here"
```

An environment variable set only in an interactive shell will not automatically be visible to a separately managed gateway service. For a persistent Hermes setup, storing the key through the plugin installer or in the active profile’s `.env` file is the preferred current path.

Hermes profiles have separate home directories and separate `.env` files. Install the provider and configure the key in the same profile that will use Telnyx.

Reference: [Hermes profiles and isolated configuration](https://hermes-agent.nousresearch.com/docs/user-guide/profiles/)

### Protect the environment file

On Linux, macOS, or WSL2:

```
chmod 600 ~/.hermes/.env
```

Do not print the complete key in diagnostics or commit `.env` to source control.

Reference: [Telnyx API-key security practices](https://developers.telnyx.com/development/api-fundamentals/authentication)

## Step 6: Restart any running Hermes Gateway

Hermes discovers and registers model providers once per running process. Restart a long-running gateway after installing or updating the provider:

```
hermes gateway restart
```

Check its state:

```
hermes gateway status
```

References:

- [Telnyx provider restart requirement](https://github.com/team-telnyx/hermes-inference-provider#install)
- [Telnyx post-install instructions](https://github.com/team-telnyx/hermes-inference-provider/blob/main/after-install.md)
- [Hermes Gateway CLI](https://hermes-agent.nousresearch.com/docs/reference/cli-commands/#hermes-gateway)

A restart is not required before starting a new short-lived CLI process because that new process performs fresh provider discovery.

Reference: [Hermes model-provider discovery lifecycle](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin#how-discovery-works)

## Step 7: Select Telnyx as the model provider

Run the full provider-selection wizard from your terminal:

```
hermes model
```

Do not run this command inside an active Hermes chat session.

In the picker:

1. Select **Telnyx**.
2. Enter the Telnyx API key if Hermes prompts for it.
3. Select a model from the Telnyx catalog.
4. Save the selection as the main model.

`hermes model` is the complete provider setup command. It can discover providers, prompt for API keys, retrieve provider-specific model lists, and save the selected provider and model into Hermes configuration.

References:

- [Hermes `model` command](https://hermes-agent.nousresearch.com/docs/reference/cli-commands/#hermes-model)
- [Hermes AI-provider management](https://hermes-agent.nousresearch.com/docs/integrations/providers/#two-commands-for-model-management)
- [Telnyx provider usage](https://github.com/team-telnyx/hermes-inference-provider#use)

The Telnyx provider retrieves the live model catalog from:

```
GET https://api.telnyx.com/v2/ai/openai/models
```

The endpoint requires bearer authentication and returns the models available to the authenticated Telnyx account.

References:

- [Telnyx available-models API](https://developers.telnyx.com/api-reference/openai-chat/get-available-models-openai-compatible)
- [Telnyx provider model discovery](https://github.com/team-telnyx/hermes-inference-provider#models)

## Step 8: Choose a Telnyx model

The current curated fallback models are:

|  |  |
| --- | --- |
| Model | Suggested use |
| `moonshotai/Kimi-K3` | General coding, reasoning, multimodal, and long-context work |
| `moonshotai/Kimi-K2.6` | Voice-oriented workloads when thinking is disabled |
| `zai-org/GLM-5.2` | Coding, reasoning, and long-context workflows |
| `MiniMaxAI/MiniMax-M3-MXFP8` | Cost-efficient general intelligence |

References:

- [Telnyx available models](https://developers.telnyx.com/docs/inference/models)
- [Telnyx Hermes provider fallback catalog](https://github.com/team-telnyx/hermes-inference-provider#models)

The provider’s recommended default starting point is:

```
moonshotai/Kimi-K3
```

The complete launch combination is:

```
Provider: telnyx Model: moonshotai/Kimi-K3
```

Hermes keeps provider and model as separate command-line values, so the model is not prefixed with `telnyx/` when passed through `-m` or `--model`.

Reference: [Telnyx provider usage examples](https://github.com/team-telnyx/hermes-inference-provider#use)

## Step 9: Run a one-shot test

Run a noninteractive test that explicitly selects Telnyx:

```
hermes -z \   "Reply with exactly: TELNYX_HERMES_OK" \   --provider telnyx \   --model moonshotai/Kimi-K3
```

Expected response:

```
TELNYX_HERMES_OK
```

The `-z` or `--oneshot` mode accepts one prompt and prints only the final response. The `--provider` and `--model` flags override the configured provider and model for that invocation without changing the global configuration.

References:

- [Hermes one-shot mode](https://hermes-agent.nousresearch.com/docs/reference/cli-commands/#hermes--z-prompt--scripted-one-shot)
- [Telnyx provider one-shot example](https://github.com/team-telnyx/hermes-inference-provider#use)

You can test a different Telnyx model:

```
hermes -z \   "Summarize Telnyx in two sentences." \   --provider telnyx \   --model zai-org/GLM-5.2
```

## Step 10: Start an interactive Telnyx conversation

Launch a new Hermes chat that explicitly uses Telnyx:

```
hermes chat \   --provider telnyx \   --model moonshotai/Kimi-K3
```

You can also start Hermes using its shorter default command after selecting Telnyx through `hermes model`:

```
hermes
```

References:

- [Hermes chat command](https://hermes-agent.nousresearch.com/docs/reference/cli-commands/#hermes-chat)
- [Hermes CLI interface](https://hermes-agent.nousresearch.com/docs/user-guide/cli/)
- [Telnyx provider usage](https://github.com/team-telnyx/hermes-inference-provider#use)

A useful first prompt is:

```
Identify the model provider and model used for this conversation, then explain what Telnyx does in two sentences.
```

## Step 11: Verify tool calling

The Telnyx Chat Completions API supports tool and function calling, and the provider’s curated fallback models were verified with tool-using conversations.

References:

- [Telnyx function calling](https://developers.telnyx.com/docs/inference/functions)
- [Telnyx streaming function calling](https://developers.telnyx.com/docs/inference/streaming-functions)
- [Telnyx Hermes provider implementation](https://github.com/team-telnyx/hermes-inference-provider/blob/main/__init__.py)
- [Telnyx provider test and implementation notes](https://github.com/NousResearch/hermes-agent/pull/74880)

Inside a Hermes session, ask the model to perform a low-risk tool task, such as:

```
Use the terminal tool to print the current working directory, then explain the result.
```

Review the proposed tool call before approving any operation that changes files, sends messages, accesses credentials, or modifies external systems.

## Step 12: Configure a messaging Gateway

Complete this step only when Hermes will run through Telegram, Discord, Slack, or another persistent channel.

First, confirm that ordinary CLI chat works. Hermes recommends establishing one clean conversation before adding gateway, cron, voice, or routing features.

Reference: [Hermes quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart/)

Configure the Gateway:

```
hermes gateway setup
```

Restart it after configuration:

```
hermes gateway restart
```

Check its status:

```
hermes gateway status
```

References:

- [Hermes messaging Gateway](https://hermes-agent.nousresearch.com/docs/user-guide/messaging/)
- [Hermes Gateway CLI](https://hermes-agent.nousresearch.com/docs/reference/cli-commands/#hermes-gateway)

The Gateway must run under the same Hermes profile in which the Telnyx provider and API key were installed.

Reference: [Hermes profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles/)

## How the integration works

Hermes model-provider plugins describe an inference backend that Hermes can use for its main and auxiliary model calls. Third parties can add providers by placing a plugin directory under:

```
$HERMES_HOME/plugins/model-providers/
```

The Telnyx package registers a provider profile through Hermes’s documented `providers.register_provider` interface.

References:

- [Hermes model-provider architecture](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin)
- [Telnyx provider source](https://github.com/team-telnyx/hermes-inference-provider/blob/main/__init__.py)

The provider uses the OpenAI-compatible Telnyx base URL:

```
https://api.telnyx.com/v2/ai/openai
```

Telnyx’s Inference API supports OpenAI-compatible chat completions, streaming responses, model listing, and function calling.

References:

- [Telnyx Inference API quickstart](https://developers.telnyx.com/docs/inference/getting-started)
- [Telnyx chat-completions API](https://developers.telnyx.com/api-reference/openai-chat/create-a-chat-completion-openai-compatible)
- [Telnyx available-models API](https://developers.telnyx.com/api-reference/openai-chat/get-available-models-openai-compatible)
- [Telnyx function calling](https://developers.telnyx.com/docs/inference/functions)

## Live and fallback model discovery

The provider uses two catalog sources:

1. **Authenticated live catalog:** The provider requests the current model list from the Telnyx `/models` endpoint.
2. **Curated offline fallback:** If authentication, networking, or live discovery fails, Hermes can still display a small verified set of Telnyx text-generation models.

The live catalog is filtered to text-generation workloads. It accepts both `text-generation` and `text generation` task labels because both forms have appeared in the Telnyx catalog.

Reference: [Telnyx provider model-discovery implementation](https://github.com/team-telnyx/hermes-inference-provider/blob/main/__init__.py)

## Current release-candidate limitations

## Manual provider-directory move

The current Hermes plugin installer places the repository in the generic plugins directory. Model-provider discovery scans the `model-providers` subdirectory, so the manual move is currently required.

Reference: [Telnyx provider installation limitation](https://github.com/team-telnyx/hermes-inference-provider#option-a--hermes-installer--one-move)

## In-session model switching

The following in-session path may currently report that `telnyx` is an unknown provider:

```
/model <model> --provider telnyx
```

Until Hermes’s generic external-provider resolver is updated, use one of these supported paths:

```
hermes model
```

or:

```
hermes chat \   --provider telnyx \   --model moonshotai/Kimi-K3
```

or:

```
hermes -z \   "Your prompt" \   --provider telnyx \   --model moonshotai/Kimi-K3
```

References:

- [Telnyx provider known constraints](https://github.com/team-telnyx/hermes-inference-provider#known-constraints)
- [Hermes PR discussion of external-provider resolution](https://github.com/NousResearch/hermes-agent/pull/74880)

## Cost reporting

Telnyx catalog prices are expressed per one million tokens using:

```
pricing.unit = "1M_tokens"
```

Until Hermes ships generic handling for this tagged pricing unit, treat Hermes’s displayed or exported cost estimate for Telnyx as unavailable or non-authoritative.

Use current Telnyx pricing sources for billing decisions.

References:

- [Telnyx provider pricing limitation](https://github.com/team-telnyx/hermes-inference-provider#known-constraints)
- [Telnyx model metadata and pricing units](https://developers.telnyx.com/api-reference/openai-chat/get-available-models-openai-compatible)

## Maximum-output settings

The provider does not volunteer a default output-token cap. The plugin repository reports that combining explicit `max_tokens` or `max_completion_tokens` values with function tools can cause Telnyx error `10015` on some hosted models.

Leave Hermes’s explicit maximum-token setting unset unless the workflow requires it and the selected model has been tested with tools.

Reference: [Telnyx provider output-cap constraint](https://github.com/team-telnyx/hermes-inference-provider#known-constraints)

## Troubleshooting

### Telnyx does not appear in `hermes model`

Confirm that the plugin is inside the model-provider directory:

```
find ~/.hermes/plugins/model-providers \   -maxdepth 2 \   -name plugin.yaml \   -print
```

The provider must not remain only at:

```
~/.hermes/plugins/telnyx-provider/
```

It must be under:

```
~/.hermes/plugins/model-providers/
```

Restart any running Gateway:

```
hermes gateway restart
```

Then rerun:

```
hermes model
```

References:

- [Telnyx provider troubleshooting](https://github.com/team-telnyx/hermes-inference-provider#troubleshooting)
- [Hermes external-provider discovery](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin#how-discovery-works)

### The API returns `401 Unauthorized`

Check that `TELNYX_API_KEY` exists in the active Hermes profile:

```
grep '^TELNYX_API_KEY=' ~/.hermes/.env \   | sed 's/=.*/=<redacted>/'
```

Do not print the complete value.

A `401` response normally means that bearer authentication is missing or invalid.

Verify that:

- The complete API key was copied.
- The key has not expired or been revoked.
- The key contains no leading or trailing spaces.
- The key is stored in the active profile’s `.env` file.
- A running Gateway was restarted after the key changed.

References:

- [Telnyx provider troubleshooting](https://github.com/team-telnyx/hermes-inference-provider#troubleshooting)
- [Telnyx API authentication](https://developers.telnyx.com/development/api-fundamentals/authentication)
- [Telnyx available-models authorization](https://developers.telnyx.com/api-reference/openai-chat/get-available-models-openai-compatible#authorizations)

### Only a few models appear

The provider is probably displaying its curated fallback catalog because the authenticated live model request failed.

Check:

- `TELNYX_API_KEY`
- Internet connectivity
- DNS resolution
- Access to `api.telnyx.com`
- Whether the key belongs to the expected Telnyx account

The fallback catalog currently includes:

```
moonshotai/Kimi-K3 moonshotai/Kimi-K2.6 zai-org/GLM-5.2 MiniMaxAI/MiniMax-M3-MXFP8
```

References:

- [Telnyx provider fallback models](https://github.com/team-telnyx/hermes-inference-provider#models)
- [Telnyx available models](https://developers.telnyx.com/docs/inference/models)

### The Gateway does not see the provider

Restart it:

```
hermes gateway restart
```

Then check:

```
hermes gateway status
```

Provider registration happens once per process, so a Gateway started before installation will not see the newly added provider until it restarts.

References:

- [Telnyx provider restart requirement](https://github.com/team-telnyx/hermes-inference-provider#install)
- [Hermes provider discovery](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin#how-discovery-works)

### `/model` reports an unknown Telnyx provider

Exit the active session:

```
/quit
```

Then run:

```
hermes model
```

Alternatively, launch a new session with explicit flags:

```
hermes chat \   --provider telnyx \   --model moonshotai/Kimi-K3
```

Reference: [Telnyx provider known constraints](https://github.com/team-telnyx/hermes-inference-provider#known-constraints)

### Hermes still uses another provider

Launch a Telnyx session explicitly:

```
hermes chat \   --provider telnyx \   --model moonshotai/Kimi-K3
```

To change the saved default, exit the session and run:

```
hermes model
```

`hermes model` is the complete provider setup wizard. The `/model` command inside a conversation is intended only for switching among providers Hermes can already resolve.

References:

- [Hermes model command](https://hermes-agent.nousresearch.com/docs/reference/cli-commands/#hermes-model)
- [Hermes provider management](https://hermes-agent.nousresearch.com/docs/integrations/providers/#two-commands-for-model-management)

### Requests fail or time out

Run Hermes diagnostics:

```
hermes doctor
```

Then test a direct one-shot conversation:

```
hermes -z \   "Reply with exactly: CONNECTION_OK" \   --provider telnyx \   --model moonshotai/Kimi-K3
```

For a Gateway deployment, also run:

```
hermes gateway status
```

Hermes recommends the following recovery sequence:

1. `hermes doctor`
2. `hermes model`
3. `hermes setup`
4. `hermes sessions list`
5. `hermes --continue`
6. `hermes gateway status`

Reference: [Hermes recovery toolkit](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart/#recovery-toolkit)

### Explicit maximum-token requests fail during tool use

Remove any custom `agent.max_tokens` configuration and retry.

The current provider deliberately does not set a default output cap because some Telnyx-hosted models reject explicit output-token parameters when tools are included.

Reference: [Telnyx provider known constraints](https://github.com/team-telnyx/hermes-inference-provider#known-constraints)

## Updating the provider

The current repository recommends updating the provider through Git.

For an installation at `telnyx-provider`:

```
git -C ~/.hermes/plugins/model-providers/telnyx-provider pull
```

For an installation at `telnyx`:

```
git -C ~/.hermes/plugins/model-providers/telnyx pull
```

Restart the Gateway after updating:

```
hermes gateway restart
```

Then run:

```
hermes model
```

and complete a one-shot verification:

```
hermes -z \   "Reply with exactly: TELNYX_PROVIDER_UPDATED" \   --provider telnyx \   --model moonshotai/Kimi-K3
```

Reference: [Telnyx provider update instructions](https://github.com/team-telnyx/hermes-inference-provider#update--remove)

For production use, review the target release and pin an explicit tag rather than automatically tracking a changing main branch.

## Removing the provider

First, use `hermes model` to select another provider so Hermes retains a working default:

```
hermes model
```

Remove the provider directory.

For the installer-and-move path:

```
rm -rf ~/.hermes/plugins/model-providers/telnyx-provider
```

For the Git-clone path:

```
rm -rf ~/.hermes/plugins/model-providers/telnyx
```

Restart the Gateway:

```
hermes gateway restart
```

Remove the Telnyx API key from:

```
~/.hermes/.env
```

when it is no longer required by another Telnyx integration.

References:

- [Telnyx provider removal instructions](https://github.com/team-telnyx/hermes-inference-provider#update--remove)
- [Hermes model selection](https://hermes-agent.nousresearch.com/docs/reference/cli-commands/#hermes-model)

## Security considerations

The Telnyx provider executes inside the Hermes process. Install it only from the official Telnyx-owned repository and review its release before upgrading.

The plugin repository is:

<https://github.com/team-telnyx/hermes-inference-provider>

The current release is:

<https://github.com/team-telnyx/hermes-inference-provider/releases/tag/v0.1.0-rc.1>

The package is distributed under the MIT License:

<https://github.com/team-telnyx/hermes-inference-provider/blob/main/LICENSE>

Report security issues through the repository’s private GitHub Security Advisory flow rather than opening a public issue.

Reference: [Telnyx provider security guidance](https://github.com/team-telnyx/hermes-inference-provider#security)

## Next steps

After Telnyx inference is working, you can:

- Connect Hermes to a supported messaging platform.
- Use Telnyx-hosted models in one-shot scripts and scheduled cron workflows.
- Connect Hermes to Telnyx APIs through the official [Telnyx MCP server.](https://developers.telnyx.com/development/mcp/remote-mcp)
- Configure separate Hermes profiles for development, testing, and production.
- Evaluate the Telnyx speech-to-text and text-to-speech integrations as they progress toward upstream Hermes support.
- After Hermes ships the generic external-provider resolver improvements, assign lower-cost Telnyx models to selected auxiliary tasks.

Hermes distinguishes between a main model and auxiliary model slots. The main model handles user messages, streamed responses, and tool-call loops. Auxiliary slots handle smaller tasks such as context compression, image analysis, webpage summarization, approval scoring, MCP tool routing, title generation, and skill search. Each auxiliary slot can be configured independently.

The current Telnyx STT and TTS repositories contain tested provider implementations intended for contribution to Hermes core; they are not currently distributed as standalone end-user plugins but coming soon.

The current Telnyx inference-provider release also documents an outstanding external-provider resolver limitation. Until the related provider-neutral Hermes changes land, use Telnyx as the main provider through `hermes model` or the `--provider telnyx` launch option rather than promising task-specific auxiliary-provider selection.

---

Related Articles

- [Get Started with Telnyx Storage & Inference Guide](https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide)
- [How to use Telnyx AI Inference with OpenClaw](https://support.telnyx.com/en/articles/16220836-how-to-use-telnyx-ai-inference-with-openclaw)
