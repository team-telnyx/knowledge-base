---
title: AIAssistant
summary: The `` verb allows you to start a voice assistant on the call.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/aiassistant/index
    content_hash: dc53ac37cbc74fcab97cd3ea202072d0b9393377c20563ff1e8b3c047d40a0a1
updated_at: 2026-04-10T00:00:00Z
---

# AIAssistant

The `` verb allows you to start a voice assistant on the call.

## Attributes

<table>
  <thead>
    <tr>
      <th>ATTRIBUTE</th>
      <th>DESCRIPTION</th>
      <th>OPTIONS</th>
      <th>DEFAULT</th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td><code>id</code></td>
      <td> The identifier of the AI assistant. The AI assistant can be created using the [AI Assistant API](https://developers.telnyx.com/api-reference/assistants/create-an-assistant). </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>join</code></td>
      <td> The ID of an existing AI assistant conversation to join. When set, the call leg is added as a participant to the specified conversation instead of starting a new one. Use `participantName` and `participantRole` to configure the joining participant. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>participantName</code></td>
      <td> The display name of the participant joining the conversation. Only used when `join` is set. </td>

      <td />

      <td>-</td>
    </tr>

    <tr>
      <td><code>participantRole</code></td>
      <td> The role of the participant joining the conversation. Only used when `join` is set. </td>
      <td><code>user</code>, <code>assistant</code></td>
      <td><code>user</code></td>
    </tr>
  </tbody>
</table>

## Examples

```xml theme={null}

        <AIAssistant id=\"assistant-776d0d6f-716d-4d8f-b6da-b95181636838\">

```

```xml theme={null}
<!-- Join an existing AI assistant conversation -->

        <AIAssistant join=\"v3:abc123def456\" participantName=\"John\" participantRole=\"user\">

```
