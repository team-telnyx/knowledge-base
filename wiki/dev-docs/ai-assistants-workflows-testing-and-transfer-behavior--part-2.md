---
title: 'AI Assistants: Workflows, Testing, and Transfer Behavior'
summary: 'This page covers three core capabilities for Telnyx AI Assistants: conversation
  workflows for guided multi-step interactions, version testing and traffic distribution
  for safe rollouts, and voicemail detection on transfer for handling calls that reach
  voicemail.'
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
updated_at: 2026-08-05T13:45:23Z
---

# AI Assistants: Workflows, Testing, and Transfer Behavior

*Part 2 of 3 — see also: [Part 1](ai-assistants-workflows-testing-and-transfer-behavior--part-1.md), [Part 3](ai-assistants-workflows-testing-and-transfer-behavior--part-3.md)*

This page covers three core capabilities for Telnyx AI Assistants: conversation workflows for guided multi-step interactions, version testing and traffic distribution for safe rollouts, and voicemail detection on transfer for handling calls that reach voicemail.

## Version Testing and Traffic Distribution

This section walks you through testing your AI assistant before production deployment and managing live traffic distribution between different versions. You'll learn how to create tests, iterate on your assistant, and safely roll out changes using A/B testing.

### Creating your first assistant

Start by creating a new assistant using a template to establish a baseline for testing.

1. Navigate to the [AI Assistants page](https://portal.telnyx.com/#/ai/assistants)
2. Click "Create Assistant" and select the "Weather Assistant" template
3. This template provides a good foundation with a standard greeting and weather functionality

![Create Weather Assistant](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/create-weather-assistant-template.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=a0e198b1b16f6fea7ef6597e71dd9026)

Take note of the default greeting message — you'll be testing and modifying this later.

### Setting up your first test

Testing your assistant ensures it behaves correctly before going live with users.

#### Creating a test

1. Navigate to the [AI Tests page](https://portal.telnyx.com/#/ai/tests)
2. Click "Create Test" to set up your first test scenario

![Create AI Test](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/create-ai-test-setup.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=02087226ea0fefa9db162707ab107035)

#### Configuring test criteria

3. Configure your test with the following:
   - **Test Name**: "Weather Assistant Greeting Test"
   - **Assistant**: Select your weather assistant
   - **Success Criteria**: Add criteria to validate the greeting message content and that temperature is described by the assistant.

![Test Criteria Configuration](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/test-criteria-setup.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=6491fddc6c99c3aa1588355c87f8badf)

#### Running your test

1. Click "Run Test" to execute your test scenario
2. Monitor the test progress in real-time
3. Review the detailed results once the test completes

![Test Execution Run](https://mintcdn.com/telnyx/33ANQJ-HKUTIlR5u/img/ai-test-run.png?fit=max&auto=format&n=33ANQJ-HKUTIlR5u&q=85&s=cc4ba4e305c333e9d89bf6ee4d916dca)
![Test Execution Results](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/test-execution-results.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=f12809fa3d065f48220caea49e18b60a)
![Test Execution Results](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/test-conversation-history.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=4e61105016c72d2f0f7f40ff3ea626ec)

The results will show whether your assistant met all the defined criteria, helping you identify any issues before deployment. You can also review the conversation itself.

### Creating assistant versions

Now you'll create a new version of your assistant with modified behavior to demonstrate A/B testing. To make it obvious that the A/B test is working, we make two visibly distinct versions of the AI Assistant using the frontend widget feature. Versions are not limited to the frontend, though. You can make versions from any configuration on the assistant including updated tools, instructions, and more.

#### Modifying the assistant

1. Return to your weather assistant in the [AI Assistants page](https://portal.telnyx.com/#/ai/assistants)
2. Click the edit icon (pencil) next to your assistant
3. Make the following changes to create a visually distinct version:
   - **Enable the frontend widget**: Navigate to the Widget tab and click enable
   - **Widget Appearance**: Navigate back to the Widget tab and change the widget theme from dark mode to light mode in the appearance settings

![Enable Assistant Widget](https://mintcdn.com/telnyx/fKocYsWR7KyFBdpc/img/enable-assistant-widget.png?fit=max&auto=format&n=fKocYsWR7KyFBdpc&q=85&s=6f9ae8dc0784b11b1d4a81d54f30ee7b)

#### Creating a new version

1. After making your changes, click "Save as New Version"
2. Give your version a descriptive name: "Light Theme with New Greeting"
3. Add version notes describing the changes made

![Edit Assistant Widget](https://mintcdn.com/telnyx/fKocYsWR7KyFBdpc/img/edit-assistant-widget.png?fit=max&auto=format&n=fKocYsWR7KyFBdpc&q=85&s=5d669b13f880cfd5c7b8960e22f5bb07)

You now have two versions of your assistant:

- **Version 1**: Original greeting with dark theme widget
- **Version 2**: New greeting with light theme widget

![View New Assistant Version](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/view-assistant-versions.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=dd9d839a698c6b5914a08b37ac1f5e08)

### Production traffic distribution

Once you've validated a new version, use version routing to control which live calls receive it. Traffic routing now uses ordered rules, similar to feature-flag targeting. Each rule has:

- **If** conditions that match the end user target for the conversation
- **Serve** behavior that sends matching calls to one version, or splits them across several versions

Rules are evaluated from top to bottom. The first matching rule wins. If no target rule matches, the assistant serves the main version unless you configure a default rule.

#### Open the traffic routing editor

1. Open your assistant from the [AI Assistants page](https://portal.telnyx.com/#/ai/assistants).
2. Go to the assistant's version or deployment controls.
3. Open **Traffic distribution** to configure routing rules.

#### Add a target rule

Use target rules when you want a specific end user, customer, or test endpoint to receive a version. The target value is the same value exposed to assistants as `{{telnyx_end_user_target}}`: the phone number, SIP URI, or other identifier associated with the end user. This works for both call directions:

- **Inbound calls**: the end user target is the caller's phone number, SIP URI, or identifier.
- **Outbound calls**: the end user target is the destination the assistant calls. For example, you can route calls to your own number to a test version.

1. Click **Add rule**.
2. In the **If** section, choose **End user target**.
3. Select an operator:
   - **is one of** for exact targets, such as `+13125550123` or `sip:customer@example.com`
   - **is not one of** to exclude specific targets
   - **starts with** for prefixes, such as `+1312` or `sip:qa-`

![AI Assistant traffic routing new end user target rule](https://mintcdn.com/telnyx/fqsuoz6tioAwo703/img/ai-assistant-routing-new-target-rule.png?fit=max&auto=format&n=fqsuoz6tioAwo703&q=85&s=fe53726042a6925275eb5bed4cd58159)

If your Traffic distribution editor still shows **Origination number**, treat it as the end user target. The field is being renamed because the same routing behavior applies to inbound callers and outbound call destinations.

4. Enter one or more target values. You can separate values with commas or new lines.
5. In the **Serve** section, choose **Send all matched calls to one version** and select the version that matching calls should receive.

![AI Assistant single-version end user target rule](https://mintcdn.com/telnyx/fqsuoz6tioAwo703/img/ai-assistant-routing-single-version-rule.png?fit=max&auto=format&n=fqsuoz6tioAwo703&q=85&s=94cad6f10edec112622b82341c359d02)

Target rules can contain multiple conditions. Conditions in the same rule are AND-joined, so every condition must match for the rule to apply. If multiple rules could match, only the first matching rule is used.

![AI Assistant end user target rule with multiple conditions](https://mintcdn.com/telnyx/fqsuoz6tioAwo703/img/ai-assistant-routing-multiple-conditions.png?fit=max&auto&n=fqsuoz6tioAwo703&q=85&s=a2c970520768d6aad9a1cebecff1483e)

#### Split matching traffic by percentage

For gradual rollouts, set a rule's **Serve** behavior to **Split by percentage**. Add version slots and assign each one a percentage. The allocation bar shows how matching traffic is split. Percentages must add up to less than 100. Any remaining percentage routes to the main version, which gives you a built-in safety fallback during canary releases.

![AI Assistant weighted rollout configuration](https://mintcdn.com/telnyx/fqsuoz6tioAwo703/img/ai-assistant-routing-weighted-rollout.png?fit=max&auto&n=fqsuoz6tioAwo703&q=85&s=ba0193eb7446a6f1794803a7846e25c2)

For example, if a target rule sends 25% of matching calls to Version 2 and 25% to Version 3, the remaining 50% of matching calls continue to use the main version.

#### Configure the default rule

The default rule handles calls that do not match any target rule. By default, unmatched calls serve the main version. Use **Configure default** when you want unmatched calls to receive another version or a percentage split. Use **Reset to main** to remove the custom default and return all unmatched traffic to the main version.

#### Save, reorder, or rollback

- Drag target rules to change their priority. Rule order matters because the first match wins.
- Click **Save** to apply the routing configuration.
- Click **Rollback** to clear all routing rules and send traffic back to the main version.

This setup allows you to:

- Test new versions with internal phone numbers or SIP URIs before a broad rollout
- Run percentage-based canaries for matching call segments
- Keep the main version as the fallback for unmatched calls and remaining rollout percentage
- Quickly rollback if issues arise
- Promote a validated version to main when you're ready

#### Testing live traffic distribution

To verify your routing is working correctly, make repeated test calls with end user targets that should match each rule:

1. For inbound testing, call the assistant from a phone number or SIP URI listed in a target rule and confirm the routed version answers.
2. For outbound testing, have the assistant call a target listed in a rule, such as your own phone number, and confirm you receive the test version.
3. Call from or to a target that should not match the target rules and confirm the default behavior applies.
4. For weighted rollouts, make enough calls to confirm that matching traffic is distributed according to your configured percentages.

### Automated evaluation with Coval

The manual testing and A/B traffic distribution described above work well for targeted checks and gradual rollouts. For automated evaluation at scale, Telnyx integrates with [Coval](https://www.coval.dev/) — a simulation and evaluation platform purpose-built for voice and chat agents.

| Capability | How it complements built-in testing |
| --- | --- |
| **Scenario simulation** | Generate thousands of test conversations from a few seed cases, covering edge cases that are difficult to script manually. |
| **CI/CD evaluations** | Automatically run your scenario library on every assistant change and block deployments that introduce regressions. |
| **Production monitoring** | Log live calls, surface performance drops in real time, and replay transcripts or audio for debugging. |
| **Built-in metrics** | Measure latency, accuracy, tool-call effectiveness, and instruction compliance without custom instrumentation. |

To get started with Coval:

1. Set up the integration on the Integrations tab of your assistant.
2. Create seed scenarios in Coval that reflect your most important conversation paths.
3. Run simulations to validate assistant behavior before deploying new versions.
4. Add Coval evaluation steps to your CI/CD pipeline to catch regressions automatically.

For setup details and required credentials, see the Coval integration guide in [Integrations](integrations.md).
