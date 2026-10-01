---
title: "How to use Telnyx AI Inference with OpenClaw"
summary: "The Telnyx provider is an external, Telnyx-maintained OpenClaw plugin. It uses the OpenAI-compatible Telnyx Chat Completions API, supports streaming, and can retrieve model information from the Telnyx model catalog."
sources:
- url: "https://support.telnyx.com/en/articles/16220836-how-to-use-telnyx-ai-inference-with-openclaw"
updated_at: 2026-09-15T00:00:00Z
tags: [support-docs]
source_path: "support-docs/16220836-how-to-use-telnyx-ai-inference-with-openclaw.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/16220836-how-to-use-telnyx-ai-inference-with-openclaw.md -->

# How to use Telnyx AI Inference with OpenClaw

The Telnyx provider is an external, Telnyx-maintained OpenClaw plugin. It uses the OpenAI-compatible Telnyx Chat Completions API, supports streaming, and can retrieve model information from the Telnyx model catalog.

**Primary references:**

- [Telnyx OpenClaw provider repository](https://github.com/team-telnyx/openclaw-telnyx-provider)
- [Telnyx Inference API quickstart](https://developers.telnyx.com/docs/inference/getting-started)
- [Telnyx available models](https://developers.telnyx.com/docs/inference/models)

## What you will configure

By the end of this guide, you will have:

- A compatible OpenClaw installation.
- The Telnyx inference-provider plugin installed.
- A Telnyx API key available to OpenClaw.
- A Telnyx model selected as the default OpenClaw model.
- A working OpenClaw agent that can respond from the terminal and Control UI.

## Integration status

The provider runtime is maintained in the public [`team-telnyx/openclaw-telnyx-provider`](https://github.com/team-telnyx/openclaw-telnyx-provider) repository.

The current repository package manifest declares:

```
@team-telnyx/openclaw-provider
```

It also declares:

```
OpenClaw >= 2026.7.2-beta.7
```

An [upstream OpenClaw pull request](https://github.com/openclaw/openclaw/pull/116016) is seeking to add Telnyx to OpenClaw’s official external-provider catalog, onboarding flow, and provider documentation.

The direct installation path documented below does not require that catalog PR to be merged.

## Prerequisites

You need:

- A [Telnyx account](https://portal.telnyx.com/).
- A Telnyx API key.
- A machine supported by OpenClaw.
- OpenClaw `2026.7.2-beta.7` or newer.
- A supported Node.js version when installing OpenClaw manually through npm.
- Internet access from the machine running the OpenClaw Gateway.

OpenClaw currently supports Node.js `22.22.3+`, `24.15+`, and `25.9+`, including Node 26.

References:

- [OpenClaw Node.js requirements](https://docs.openclaw.ai/install/node)
- [Telnyx provider compatibility declaration](https://github.com/team-telnyx/openclaw-telnyx-provider/blob/main/package.json)

Install the provider on the same machine that runs the OpenClaw Gateway. OpenClaw plugins are loaded by the Gateway runtime.

References:

- [OpenClaw plugin management](https://docs.openclaw.ai/plugins/manage-plugins)
- [OpenClaw Gateway documentation](https://docs.openclaw.ai/gateway)

## Step 1: Create a Telnyx API key

Sign in to the [Telnyx Mission Control Portal](https://portal.telnyx.com/).

Then:

1. Select your account name in the upper-right corner.
2. Open **API Keys**.
3. Select **Create API Key**.
4. Add a descriptive name for the key.
5. Choose the appropriate expiration settings.
6. Create and securely copy the key.

Telnyx displays the full value only when the key is created. Store it in a password manager or secrets vault.

Reference: [Create and manage Telnyx API keys](https://developers.telnyx.com/development/api-fundamentals/create-api-keys)

Do not:

- Commit the key to Git.
- Put it in client-side browser code.
- Include it in screenshots, documentation, or logs.
- Share it through an unsecured messaging channel.

Telnyx recommends environment variables, regular rotation, and separate keys for development and production.

Reference: [Telnyx API authentication and security practices](https://developers.telnyx.com/development/api-fundamentals/authentication)

## Step 2: Install a compatible OpenClaw version

The current Telnyx package requires OpenClaw `2026.7.2-beta.7` or newer.

Reference: [Telnyx provider compatibility declaration](https://github.com/team-telnyx/openclaw-telnyx-provider/blob/main/package.json)

### macOS, Linux, or WSL

Use the official installer and pin the tested version:

```
curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh \   | bash -s -- \       --version 2026.7.2-beta.7 \       --no-onboard
```

The `--version` option accepts an npm version, distribution tag, or package specification. The `--no-onboard` option installs OpenClaw without immediately starting the onboarding wizard.

References:

- [OpenClaw installation overview](https://docs.openclaw.ai/install)
- [OpenClaw installer flags](https://docs.openclaw.ai/install/installer)

### Windows PowerShell

Use the official PowerShell installer and pin the same version:

```
& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) `   -Tag 2026.7.2-beta.7 `   -NoOnboard
```

The PowerShell installer’s `-Tag` option accepts an npm tag, version, or package specification.

Reference: [OpenClaw Windows installer options](https://docs.openclaw.ai/install/installer#installps1)

### npm alternative

When Node.js and npm are already installed:

```
npm install -g openclaw@2026.7.2-beta.7
```

For npm 12, allow the OpenClaw lifecycle scripts explicitly:

```
npm install -g openclaw@2026.7.2-beta.7 \   --allow-scripts openclaw
```

Reference: [Install OpenClaw using npm](https://docs.openclaw.ai/install#npm-pnpm-or-bun)

### Verify the installation

```
openclaw --version
```

Confirm that the result is `2026.7.2-beta.7` or a newer compatible version.

## Step 3: Create the baseline OpenClaw configuration

Create the standard OpenClaw state, configuration, workspace, and session directories without running the complete onboarding wizard:

```
openclaw setup --baseline
```

Baseline setup creates the initial configuration and workspace and then exits. It does not run provider selection, Gateway setup, or channel onboarding.

References:

- [OpenClaw baseline setup command](https://docs.openclaw.ai/cli/setup)
- [OpenClaw advanced setup](https://docs.openclaw.ai/start/setup)

The default configuration path is:

```
~/.openclaw/openclaw.json
```

The default workspace path is:

```
~/.openclaw/workspace
```

Reference: [OpenClaw setup and workspace paths](https://docs.openclaw.ai/start/setup)

## Step 4: Install the Telnyx provider

Install the version declared by the current Telnyx-owned repository:

```
openclaw plugins install @team-telnyx/openclaw-provider@0.1.0
```

Restart the Gateway after installation:

```
openclaw gateway restart
```

References:

- [Telnyx provider installation instructions](https://github.com/team-telnyx/openclaw-telnyx-provider#install)
- [Telnyx provider package name and version](https://github.com/team-telnyx/openclaw-telnyx-provider/blob/main/package.json)
- [OpenClaw plugins CLI](https://docs.openclaw.ai/cli/plugins)
- [OpenClaw Gateway CLI](https://docs.openclaw.ai/cli/gateway)

If you are replacing an earlier local or test installation, use:

```
openclaw plugins install \   @team-telnyx/openclaw-provider@0.1.0 \   --force
```

The `--force` flag is supported by the OpenClaw plugin installer.

Reference: [OpenClaw plugin-install command](https://docs.openclaw.ai/cli/plugins)

## Step 5: Verify the plugin installation

List the installed plugins:

```
openclaw plugins list
```

Inspect the Telnyx plugin:

```
openclaw plugins inspect telnyx --json
```

Verify its runtime registration:

```
openclaw plugins inspect telnyx --runtime --json
```

The runtime inspection should identify the `telnyx` provider and show that the plugin loaded successfully.

The `--runtime` option loads the plugin module and reports its registered runtime capabilities.

References:

- [OpenClaw plugin inspection](https://docs.openclaw.ai/cli/plugins#inspect)
- [OpenClaw plugin runtime verification](https://docs.openclaw.ai/tools/plugin)
- [Telnyx OpenClaw plugin manifest](https://github.com/team-telnyx/openclaw-telnyx-provider/blob/main/openclaw.plugin.json)

## Step 6: Authenticate OpenClaw with Telnyx

There are two supported approaches:

1. Store the API key through OpenClaw’s provider-authentication flow.
2. Expose the key to the Gateway through the `TELNYX_API_KEY` environment variable.

### Option A: Interactive provider authentication

Run:

```
openclaw models auth login \   --provider telnyx \   --method api-key \   --set-default
```

Paste your Telnyx API key when prompted.

The upstream provider contribution documents this authentication flow and uses `telnyx` as the provider ID.

References:

- [OpenClaw Telnyx provider PR](https://github.com/openclaw/openclaw/pull/116016)
- [OpenClaw model-authentication commands](https://docs.openclaw.ai/cli/models#auth-profiles)
- [OpenClaw model-provider selection](https://docs.openclaw.ai/concepts/model-providers)

### Option B: Environment variable

Set the key in the shell that starts OpenClaw:

```
export TELNYX_API_KEY="KEY_your_api_key_here"
```

The Telnyx provider repository documents `TELNYX_API_KEY` as its environment-variable authentication method.

References:

- [Telnyx provider configuration](https://github.com/team-telnyx/openclaw-telnyx-provider#install)
- [Telnyx API-key storage guidance](https://developers.telnyx.com/development/api-fundamentals/create-api-keys)
- [Telnyx API authentication](https://developers.telnyx.com/development/api-fundamentals/authentication)

After setting the variable, restart the Gateway from the same user environment:

```
openclaw gateway restart
```

For a managed Gateway service, make sure the environment variable is available to the service rather than only to an interactive terminal.

Reference: [OpenClaw Gateway operations](https://docs.openclaw.ai/gateway)

## Step 7: Discover the available Telnyx models

Refresh the model metadata exposed by installed providers:

```
openclaw models refresh
```

List the Telnyx models:

```
openclaw models list \   --all \   --provider telnyx
```

For JSON output:

```
openclaw models list \   --all \   --provider telnyx \   --json
```

References:

- [OpenClaw models CLI](https://docs.openclaw.ai/cli/models)
- [OpenClaw hosted model catalogs](https://docs.openclaw.ai/concepts/models)
- [Telnyx provider discovery implementation](https://github.com/team-telnyx/openclaw-telnyx-provider)
- [Telnyx available-models API](https://developers.telnyx.com/api-reference/openai-chat/get-available-models-openai-compatible)

The provider includes an offline model catalog and can augment that information using authenticated live discovery from Telnyx.

The exact live model catalog can change. Retrieve the current list rather than permanently hardcoding every model into your application.

Reference: [Current Telnyx inference models](https://developers.telnyx.com/docs/inference/models)

## Step 8: Select a Telnyx model

The current provider manifest declares Kimi K3 as its default model:

```
telnyx/moonshotai/Kimi-K3
```

Set it as the OpenClaw default:

```
openclaw models set telnyx/moonshotai/Kimi-K3
```

Confirm the result:

```
openclaw models status
```

References:

- [OpenClaw model-selection commands](https://docs.openclaw.ai/cli/models)
- [OpenClaw provider/model reference format](https://docs.openclaw.ai/concepts/model-providers)

You can select any model returned by the Telnyx provider using:

```
telnyx/<Telnyx model ID>
```

For example:

```
openclaw models set telnyx/moonshotai/Kimi-K2.6
```

Or:

```
openclaw models set telnyx/zai-org/GLM-5.2
```

The current Telnyx model guide describes:

- `moonshotai/Kimi-K3` as a recommended general model for coding, reasoning, and multimodal work.
- `moonshotai/Kimi-K2.6` as suitable for Voice AI when thinking is disabled.
- `zai-org/GLM-5.2` as suitable for coding, reasoning, and long-context workloads.
- `MiniMaxAI/MiniMax-M3-MXFP8` as a cost-efficient model that maintains strong intelligence.

Reference: [Telnyx available models](https://developers.telnyx.com/docs/inference/models)

## Step 9: Complete OpenClaw onboarding

Run OpenClaw’s onboarding wizard and install its managed Gateway service:

```
openclaw onboard --install-daemon
```

The onboarding process configures the Gateway, workspace, channels, skills, and health checks.

References:

- [OpenClaw onboarding guide](https://docs.openclaw.ai/start/wizard)
- [OpenClaw CLI setup reference](https://docs.openclaw.ai/start/wizard-cli-reference)
- [OpenClaw getting started](https://docs.openclaw.ai/start/getting-started)

Because Telnyx authentication and the default model were configured in the earlier steps, retain the existing Telnyx model when the wizard asks about model configuration.

Restart the managed Gateway after onboarding:

```
openclaw gateway restart
```

Check its status:

```
openclaw gateway status
```

For a more detailed service scan:

```
openclaw gateway status --deep
```

References:

- [OpenClaw Gateway CLI](https://docs.openclaw.ai/cli/gateway)
- [OpenClaw Gateway runbook](https://docs.openclaw.ai/gateway)

## Step 10: Test the Telnyx provider from the command line

First, confirm the selected model:

```
openclaw models status
```

Then run an isolated agent turn:

```
openclaw agent exec \   "Reply with exactly: TELNYX_OPENCLAW_OK"
```

Expected response:

```
TELNYX_OPENCLAW_OK
```

`openclaw agent exec` runs an embedded agent turn using the normal OpenClaw configuration and configured provider credentials.

Reference: [OpenClaw `agent exec` command](https://docs.openclaw.ai/cli/agent#agent-exec)

For a more general test:

```
openclaw agent exec \   "Explain what Telnyx does in two sentences."
```

## Step 11: Open the OpenClaw Control UI

Launch the dashboard:

```
openclaw dashboard
```

The command opens the OpenClaw dashboard using the active Gateway configuration.

References:

- [OpenClaw dashboard CLI](https://docs.openclaw.ai/cli/dashboard)
- [OpenClaw Control UI](https://docs.openclaw.ai/web/control-ui)

Send a test message such as:

```
Which model provider are you using? Then summarize Telnyx in two sentences.
```

## How the integration works

The plugin registers `telnyx` as an OpenClaw model-provider ID.

A complete model reference has the following form:

```
telnyx/moonshotai/Kimi-K3
```

It consists of:

- OpenClaw provider ID: `telnyx`
- Telnyx model ID: `moonshotai/Kimi-K3`

Reference: [OpenClaw model-provider reference format](https://docs.openclaw.ai/concepts/model-providers)

The plugin manifest configures the following OpenAI-compatible base URL:

```
https://api.telnyx.com/v2/ai/openai
```

Telnyx documents its Inference API as OpenAI-compatible, allowing integrations to use OpenAI SDK and Chat Completions conventions with a different base URL and API key.

References:

- [Telnyx Inference API quickstart](https://developers.telnyx.com/docs/inference/getting-started)
- [Telnyx framework integrations](https://developers.telnyx.com/docs/inference/integrations)
- [Telnyx OpenAI migration guide](https://developers.telnyx.com/docs/inference/openai)

The provider supports streaming through OpenClaw’s OpenAI-compatible completions transport.

References:

- [Telnyx provider manifest](https://github.com/team-telnyx/openclaw-telnyx-provider/blob/main/openclaw.plugin.json)
- [Telnyx streaming and function calling](https://developers.telnyx.com/docs/inference/streaming-functions)
- [Telnyx OpenClaw provider test evidence](https://github.com/openclaw/openclaw/pull/116016)

## Troubleshooting

### OpenClaw reports that the plugin is incompatible

Check the installed OpenClaw version:

```
openclaw --version
```

The provider currently requires:

```
OpenClaw >= 2026.7.2-beta.7
```

Reference: [Telnyx provider `peerDependencies`](https://github.com/team-telnyx/openclaw-telnyx-provider/blob/main/package.json)

Install the tested version:

```
npm install -g openclaw@2026.7.2-beta.7
```

Then restart the Gateway:

```
openclaw gateway restart
```

### The plugin is installed but not loaded

Inspect both its cold configuration and active runtime:

```
openclaw plugins inspect telnyx --json openclaw plugins inspect telnyx --runtime --json
```

References:

- [OpenClaw plugin inspection](https://docs.openclaw.ai/cli/plugins#inspect)
- [OpenClaw runtime plugin verification](https://docs.openclaw.ai/tools/plugin)

Run the plugin diagnostics:

```
openclaw plugins doctor
```

Then run the complete OpenClaw diagnostic tool:

```
openclaw doctor
```

For automated repair of supported issues:

```
openclaw doctor --fix
```

References:

- [OpenClaw plugins CLI](https://docs.openclaw.ai/cli/plugins)
- [OpenClaw Doctor](https://docs.openclaw.ai/cli/doctor)

### OpenClaw cannot find a Telnyx API key

Repeat the interactive authentication flow:

```
openclaw models auth login \   --provider telnyx \   --method api-key \   --set-default
```

Then inspect the model and authentication state:

```
openclaw models status openclaw models auth list --provider telnyx
```

Reference: [OpenClaw models and authentication CLI](https://docs.openclaw.ai/cli/models)

For environment-variable authentication, verify only whether the variable exists without printing its value:

```
test -n "$TELNYX_API_KEY" \   && echo "TELNYX_API_KEY is set" \   || echo "TELNYX_API_KEY is not set"
```

Restart the Gateway after setting or changing the variable:

```
openclaw gateway restart
```

### The Telnyx API returns `401 Unauthorized`

A `401` response normally means that the API key is missing or invalid.

Check that:

- The full key was copied.
- It has not expired or been revoked.
- It contains no leading or trailing spaces.
- It is available to the Gateway process.
- The correct Telnyx account and environment are being used.

Reference: [Telnyx authentication errors](https://developers.telnyx.com/development/api-fundamentals/authentication#error-handling)

### Telnyx models do not appear

Refresh and list the provider catalog:

```
openclaw models refresh openclaw models list --all --provider telnyx
```

Then restart the Gateway:

```
openclaw gateway restart
```

References:

- [OpenClaw models CLI](https://docs.openclaw.ai/cli/models)
- [OpenClaw hosted catalog updates](https://docs.openclaw.ai/concepts/models)

### OpenClaw is still using another provider

Set the Telnyx model explicitly:

```
openclaw models set telnyx/moonshotai/Kimi-K3
```

Then confirm the resolved default:

```
openclaw models status
```

Reference: [OpenClaw model-provider selection](https://docs.openclaw.ai/concepts/model-providers)

### Agent requests fail or time out

Run the standard diagnostic sequence:

```
openclaw status openclaw gateway status openclaw logs --follow openclaw doctor
```

Look for:

- Authentication failures.
- Plugin compatibility errors.
- Provider-loading failures.
- Network or DNS problems.
- Model-not-found responses.
- Rate-limit responses.
- Gateway startup errors.

References:

- [OpenClaw Gateway troubleshooting](https://docs.openclaw.ai/gateway/troubleshooting)
- [OpenClaw help center](https://docs.openclaw.ai/help)
- [OpenClaw Doctor](https://docs.openclaw.ai/cli/doctor)

## Updating the provider

Inspect the currently installed provider:

```
openclaw plugins inspect telnyx --json
```

Check for a newer version:

```
openclaw plugins update telnyx --dry-run
```

Install an explicitly reviewed version:

```
openclaw plugins update \   @team-telnyx/openclaw-provider@<VERSION>
```

Restart and verify:

```
openclaw gateway restart openclaw plugins inspect telnyx --runtime --json openclaw models refresh openclaw models status
```

Reference: [OpenClaw plugin update commands](https://docs.openclaw.ai/cli/plugins)

For production environments, pin an explicitly reviewed provider version rather than automatically installing an unknown future version.

## Uninstalling the provider

Before removing Telnyx, configure another usable OpenClaw model provider.

Preview the removal:

```
openclaw plugins uninstall telnyx --dry-run
```

Remove the plugin:

```
openclaw plugins uninstall telnyx
```

Restart the Gateway:

```
openclaw gateway restart
```

Confirm the remaining model configuration:

```
openclaw models status
```

Reference: [OpenClaw plugin uninstall command](https://docs.openclaw.ai/cli/plugins)

## Next steps

After Telnyx inference is working, you can:

- Connect OpenClaw to a supported messaging channel.
- Use Telnyx-hosted models for scripted agent runs and scheduled automations.
- Add inbound and outbound Telnyx voice calling through OpenClaw’s voice-call plugin.
- Connect OpenClaw to Telnyx APIs through the official [Telnyx MCP server.](https://developers.telnyx.com/development/mcp/remote-mcp)
- Assign a lower-cost Telnyx model to sub-agents or specialist agents.
- Run separate OpenClaw profiles, agents, or Gateways for development and production.
- Evaluate the Telnyx speech-to-text and text-to-speech provider projects as their distribution paths stabilize.

OpenClaw does not use Hermes’s main-model and auxiliary-slot architecture.

Instead, OpenClaw supports a primary model, per-agent model configuration, and a separate model override for sub-agents. This lets you retain a higher-capability Telnyx model for the primary agent while assigning a faster or lower-cost model to repetitive delegated work.

OpenClaw’s [voice-call plugin](https://docs.openclaw.ai/plugins/voice-call) already supports Telnyx for inbound and outbound calls, including realtime voice capabilities and transcription-related call workflows.

The public Telnyx OpenClaw STT and TTS repositories should currently be treated as preview integrations rather than established production next steps: t

---

Related Articles

- [Use Syncovery with Telnyx Storage](https://support.telnyx.com/en/articles/8047874-use-syncovery-with-telnyx-storage)
- [Use Cloudmounter with Telnyx Storage](https://support.telnyx.com/en/articles/8047914-use-cloudmounter-with-telnyx-storage)
- [Use ODrive with Telnyx Storage](https://support.telnyx.com/en/articles/8047956-use-odrive-with-telnyx-storage)
- [Get Started with Telnyx Storage & Inference Guide](https://support.telnyx.com/en/articles/8344129-get-started-with-telnyx-storage-inference-guide)
- [How to use Telnyx AI Inference with Hermes Agent](https://support.telnyx.com/en/articles/16221027-how-to-use-telnyx-ai-inference-with-hermes-agent)
