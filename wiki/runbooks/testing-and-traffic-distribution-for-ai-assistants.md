---
title: Testing and Traffic Distribution for AI Assistants
summary: This guide walks you through testing your AI assistant before production deployment and managing live traffic distribution between different versions.
sources:
  - url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution/index
    content_hash: 8da5aaece4b9abe516f5345b8633af8bef8fbd40f94adcaeb3fb3872b0e8c781
updated_at: 2026-04-10T00:00:00Z
---

# Testing and Traffic Distribution for AI Assistants

This guide walks you through testing your AI assistant before production deployment and managing live traffic distribution between different versions. You'll learn how to create tests, iterate on your assistant, and safely roll out changes using A/B testing.

***

## Creating Your First Assistant

Start by creating a new assistant using a template to establish a baseline for testing.

1. Navigate to the [AI Assistants page](https://portal.telnyx.com/#/ai/assistants)
2. Click "Create Assistant" and select the "Weather Assistant" template
3. This template provides a good foundation with a standard greeting and weather functionality

<img alt="Create Weather Assistant" />

Take note of the default greeting message - we'll be testing and modifying this later.

***

## Setting Up Your First Test

Testing your assistant ensures it behaves correctly before going live with users.

### Creating a Test

1. Navigate to the [AI Tests page](https://portal.telnyx.com/#/ai/tests)
2. Click "Create Test" to set up your first test scenario

<img alt="Create AI Test" />

### Configuring Test Criteria

3. Configure your test with the following:
   * **Test Name**: "Weather Assistant Greeting Test"
   * **Assistant**: Select your weather assistant
   * **Success Criteria**: Add criteria to validate the greeting message content and that temperature is described by the assistant.

<img alt="Test Criteria Configuration" />

### Running Your Test

1. Click "Run Test" to execute your test scenario
2. Monitor the test progress in real-time
3. Review the detailed results once the test completes

<img alt="Test Execution Run" />

<img alt="Test Execution Results" />

<img alt="Test Execution Results" />

The results will show whether your assistant met all the defined criteria, helping you identify any issues before deployment. You can also review the conversation itself.

***

## Creating Assistant Versions

Now you'll create a new version of your assistant with modified behavior to demonstrate A/B testing.

To make it obvious that the A/B test is working, we make two visibly distinct versions of the AI Assistant using the frontend widget feature.

Versions are not limited to the frontend, though. You can make versions from any configuration on the assistant including updated tools, instructions, and more.

### Modifying the Assistant

1. Return to your weather assistant in the [AI Assistants page](https://portal.telnyx.com/#/ai/assistants)
2. Click the edit icon (pencil) next to your assistant
3. Make the following changes to create a visually distinct version:
   * **Enable the frontend widget**: Navigate to the Widget tab and click enable
   * **Widget Appearance**: Navigate back to the Widget tab and change the widget theme from dark mode to light mode in the appearance settings

<img alt="Enable Assistant Widget" />

### Creating a New Version

1. After making your changes, click "Save as New Version"
2. Give your version a descriptive name: "Light Theme with New Greeting"
3. Add version notes describing the changes made

<img alt="Edit Assistant Widget" />

You now have two versions of your assistant:

* **Version 1**: Original greeting with dark theme widget
* **Version 2**: New greeting with light theme widget

<img alt="View New Assistant Version" />

***

## Production Traffic Distribution

Once you've validated your versions through testing, you can gradually roll out changes using traffic splitting.

### Setting Up 50/50 Traffic Split

1. Navigate to your assistant's deployment settings
2. Configure traffic distribution:
   * **Version 1 (main)**: 50% traffic
   * **Version 2 (Light Theme)**: 50% traffic

<img alt="Traffic Distribution Setup" />

This setup allows you to:

* Monitor real-world performance of both versions
* Gradually increase traffic to the new version if it performs well
* Quickly rollback if issues arise
* Promote the new version to main to receive all traffic when you're ready

### Testing Live Traffic Distribution

To verify your traffic distribution is working correctly, you can test the widget behavior:

1. Copy the widget embed code from your assistant settings
2. Create a simple HTML test page in a [W3Schools editor](https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic) or similar tool
3. Click run to see the widget change between light and dark theme about half the time

```html theme={null}
<telnyx-ai-agent agent-id="REPLACE WITH YOUR ASSISTANT ID"></telnyx-ai-agent>
<script async="" src="https://unpkg.com/@telnyx/ai-agent-widget"></script>
```

<img alt="AB Test Widget" />

This real-world testing confirms your traffic distribution is working and users will experience both versions according to your specified percentages.

***

## Automated Evaluation with Coval

The manual testing and A/B traffic distribution described above work well for targeted checks and gradual rollouts. For automated evaluation at scale, Telnyx integrates with [Coval](https://www.coval.dev/) — a simulation and evaluation platform purpose-built for voice and chat agents.

### What Coval adds

| Capability                | How it complements built-in testing                                                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| **Scenario simulation**   | Generate thousands of test conversations from a few seed cases, covering edge cases that are difficult to script manually. |
| **CI/CD evaluations**     | Automatically run your scenario library on every assistant change and block deployments that introduce regressions.        |
| **Production monitoring** | Log live calls, surface performance drops in real time, and replay transcripts or audio for debugging.                     |
| **Built-in metrics**      | Measure latency, accuracy, tool-call effectiveness, and instruction compliance without custom instrumentation.             |

### Getting started with Coval

1. Set up the integration on the [Integrations tab](ai-assistant-integrations.md#coval) of your assistant.
2. Create seed scenarios in Coval that reflect your most important conversation paths.
3. Run simulations to validate assistant behavior before deploying new versions.
4. Add Coval evaluation steps to your CI/CD pipeline to catch regressions automatically.

For setup details and required credentials, see the [Coval integration guide](ai-assistant-integrations.md#coval).
