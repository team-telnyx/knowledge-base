---
title: Workflow
summary: Manage AI assistant workflows with visual flowcharts.
sources:
  - url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows/index
    content_hash: 8a85238a15d1e83e9877b1cec98a2748f1f841fec9c4bd9f1faf03134fd86f36
updated_at: 2026-04-10T00:00:00Z
---

# Workflow

Manage AI assistant workflows with visual flowcharts. Configure tools, design conversation flows, and optimize call routing for your voice AI assistant.

The Workflow feature provides a visual interface for managing your AI assistant's conversation flow and tool configuration. Use the interactive flowchart to understand how your assistant routes calls, transfers to specialists, and executes actions throughout a conversation.

## Overview

Workflow helps you:

* **Visualize conversation flow** - See how your assistant connects tools and actions.
* **Manage assistant tools** - Add, edit, and configure tools like Transfer and Hang Up.
* **Understand call routing** - Track how calls move through your system.
* **Optimize assistant behavior** - Identify and improve conversation paths.

## Accessing Workflow

You can access the Workflow feature in two ways:

### Quick access to Flowchart

From the AI Assistants dashboard, click the **View Flowchart** icon next to any assistant to directly view its conversation flow.

<img alt="AI Assistants dashboard showing the View Flowchart button highlighted next to each assistant" />

### Full Workflow editor

To access the complete Workflow interface with tool management:

1. Navigate to **AI Assistants** in the portal.
2. Select your assistant from the list.
3. Click the **Workflow** tab in the assistant editor.

The Workflow tab displays:

* **Tools section** - List of configured tools with edit/delete options.
* **View Flowchart button** - Opens the visual flowchart interface.

<img alt="Workflow tab showing Tools section with configured tools and View Flowchart button" />

## Managing tools

The Tools section shows all tools configured for your assistant. Each tool can perform specific actions during conversations.

### Adding a tool

1. Click **Add tool** in the Workflow tab.
2. Select a tool type:
   * **Webhook** - Connect to external services.
   * **Hang Up** - End the call.
   * **Handoff** - Transfer to another AI assistant.
   * **Transfer** - Transfer call to a phone number.
   * **SIP Refer** - Transfer using SIP protocol.
   * **Send DTMF** - Send touch-tone signals.
3. Configure the tool's settings.
4. Save your changes.

<img alt="Add tool dropdown menu showing all available tool options including Webhook, Hang Up, Handoff, Transfer, SIP Refer, and Send DTMF" />

### Editing a tool

1. Locate the tool in the Tools list.
2. Click the **edit icon** (pencil).
3. Update the tool configuration.
4. Save your changes.

<img alt="Tool edit icon highlighted in the tools list" />

### Deleting a tool

1. Locate the tool in the Tools list.
2. Click the **delete icon** (trash).
3. Confirm the deletion.

<img alt="Tools list showing configured tools with edit and delete action icons" />

> **Warning:** Deleting a tool removes it from your assistant's capabilities. Ensure the tool is not critical to your conversation flow before removing it.

## Understanding the flowchart

The flowchart view provides a visual representation of your assistant's conversation flow.

<img alt="Workflow flowchart showing assistant node connected to multiple tool nodes with colored connection arrows and control panel" />

### Flowchart components

**Assistant node** (top of diagram)

* Represents your main AI assistant.
* Shows the assistant name.
* All conversation flows start from this node.

**Tool nodes** (connected nodes)

* Represent configured tools.
* Color-coded by tool type.
* Display tool name and configuration details.

**Connection arrows**

* Show how tools connect.
* Color-coded to indicate relationships:
  * **Purple** - Transfer connections.
  * **Red** - Hang Up connections.
  * **Blue** - Other actions.

**Control panel** (right side)

* **Zoom In (+)** - Enlarge the flowchart.
* **Zoom Out (-)** - Shrink the flowchart.
* **Fit View** - Auto-fit the entire flowchart to your screen.

<img alt="Flowchart control panel showing Zoom In, Zoom Out, and Fit View controls" />

### Interacting with the flowchart

* **Zoom** - Use the control panel or mouse wheel.
* **Pan** - Click and drag the canvas.
* **Inspect nodes** - Hover over nodes to see details.
* **Navigate back** - Click "Back to Assistant" to return to the Workflow tab.

## Use cases

### Multi-department routing

Create workflows that route callers to different departments based on their needs:

```
Main Assistant
├── Sales Department Transfer
├── Support Department Transfer
├── Billing Department Transfer
└── Hang Up
```

### Emergency handling

Design workflows that prioritize urgent situations:

```
Emergency Hotline Assistant
├── Critical Emergency Transfer (Immediate)
├── Non-Critical Transfer (Queue)
├── Information Only (Continue conversation)
└── Hang Up
```

### Appointment scheduling

Build workflows for scheduling and confirmation:

```
Scheduling Assistant
├── Check Availability (Webhook)
├── Book Appointment (Webhook)
├── Send Confirmation (Webhook)
├── Transfer to Human Agent
└── Hang Up
```

## Best practices

### Design clear flow paths

* **Keep flows simple** - Avoid overly complex routing.
* **Limit transfer targets** - Too many options confuse callers.
* **Test thoroughly** - Verify all paths work as expected.

### Use descriptive names

* **Name tools clearly** - Use descriptive labels (e.g., "Emergency Veterinary Services" instead of "Transfer 1").
* **Add descriptions** - Provide context for when each tool should be used.

### Monitor and optimize

* **Review flowcharts regularly** - Ensure flows match business needs.
* **Analyze call patterns** - Identify frequently used paths.
* **Update as needed** - Adjust tools based on caller behavior.

### Consider caller experience

* **Minimize transfers** - Reduce how often callers are transferred.
* **Provide context** - Ensure transferred calls include relevant information.
* **Always offer exit** - Include Hang Up option when assistance is complete.

## Common workflow patterns

### Simple routing workflow

Basic pattern for routing to departments:

1. Assistant greets caller.
2. Assistant determines caller's need.
3. Assistant transfers to appropriate department or continues conversation.
4. Caller receives assistance or hangs up.

### Multi-tier support workflow

Escalation pattern for complex issues:

1. Assistant attempts to resolve issue.
2. If unresolved, transfer to Level 1 support.
3. If still unresolved, transfer to Level 2 specialist.
4. Issue resolved or callback scheduled.

### Information gathering workflow

Pattern for collecting data before routing:

1. Assistant greets and identifies purpose.
2. Assistant gathers required information.
3. Assistant uses webhook to validate/process data.
4. Assistant routes to appropriate destination or confirms completion.

## Related resources

* **[Integrations](ai-assistant-integrations.md)** - Learn how to connect external services that appear in your workflow.
* **[Agent Handoff](agent-handoff.md)** - Understand how to transfer between multiple AI assistants.
* **[Dynamic Variables](dynamic-variables.md)** - Pass data between workflow steps.
* **[Testing Assistants](testing-and-traffic-distribution-for-ai-assistants.md)** - Test your workflows before deploying to production.
