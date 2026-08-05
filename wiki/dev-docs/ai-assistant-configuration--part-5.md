---
title: AI Assistant Configuration
summary: Telnyx AI assistants can be extended with enterprise integrations, tuned
  interruption behavior, persistent memory across conversations, and multi-participant
  call capabilities. This page covers the available integration catalog and connection
  workflow, interruption settings for turn-taking and non turn-taking transcription
  models, memory configuration via the dynamic variables webhook, and the Invite and
  Skip Turn tools used to coordinate multi-participant voice calls.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/integrations
- url: https://developers.telnyx.com/docs/inference/ai-assistants/interruption-settings
- url: https://developers.telnyx.com/docs/inference/ai-assistants/memory
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
updated_at: 2026-08-05T13:44:48Z
---

# AI Assistant Configuration

*Part 5 of 6 — see also: [Part 1](ai-assistant-configuration--part-1.md), [Part 2](ai-assistant-configuration--part-2.md), [Part 3](ai-assistant-configuration--part-3.md), [Part 4](ai-assistant-configuration--part-4.md), [Part 6](ai-assistant-configuration--part-6.md)*

Telnyx AI assistants can be extended with enterprise integrations, tuned interruption behavior, persistent memory across conversations, and multi-participant call capabilities. This page covers the available integration catalog and connection workflow, interruption settings for turn-taking and non turn-taking transcription models, memory configuration via the dynamic variables webhook, and the Invite and Skip Turn tools used to coordinate multi-participant voice calls.

## Multi-participant voice AI calls

Multi-participant Voice AI calls let an assistant bring another person into an active call, follow who is speaking, and continue using the same tools and instructions it would use in a one-to-one voice conversation. Use this pattern when your assistant needs to coordinate between people in real time, such as scheduling a meeting, connecting a customer with a specialist, or letting multiple callers complete a task together.

### How multi-participant calls work

A multi-participant Voice AI call starts like any other voice assistant call. The assistant speaks with the main caller, then uses an Invite tool when it needs to bring another participant into the conversation. Once the new participant joins, the assistant can:

- Tell whether the main user or an invited participant is speaking.
- Respond to either participant when appropriate.
- Use its configured tools, memory, dynamic variables, and integrations.
- Stay silent when the participants are talking to each other.
- Resume when someone addresses the assistant again.

By default, an assistant will respond to every turn it receives. For natural multi-participant calls, add a Skip Turn tool and describe when the assistant should remain silent.

### Requirements

Before you start, create a voice assistant by following the [Voice Assistant Quickstart](voice-assistant-quickstart.md). You also need:

- A phone number or SIP URI for the assistant.
- A phone number or SIP URI for each participant the assistant may invite.
- Any tools the assistant should use after the participant joins, such as a calendar, CRM, or booking integration.

### Step 1: Add an Invite tool

The Invite tool lets your assistant invite another participant into the current call.

1. In the [Mission Control Portal](https://portal.telnyx.com), open your assistant.
2. Go to the assistant's **Tools** section.
3. Add an **Invite** tool.
4. Configure the invite target with the participant's phone number or SIP URI.
5. Save the assistant.

You can also configure the assistant, its model, voice settings, and tools through the [Assistants API](/api-reference/assistants/create-an-assistant). When the assistant decides that another person should join, it calls the Invite tool. After the participant joins, the assistant receives the updated conversation context and can continue the call with both participants.

![Invite tool call shown in Conversation History](https://mintcdn.com/telnyx/EIZ2j7WXogC8b17s/img/ai-assistants-multi-participant/conversation-invite-tool-call.png?fit=max&auto=format&n=EIZ2j7WXogC8b17s&q=85&s=39257e7f6c35445538b2d0b15ab7d3fc)

### Step 2: Give the assistant multi-participant instructions

Your assistant should know that the conversation may include multiple people. Add instructions that tell the assistant how to behave when participants are speaking to each other.

Example instructions:

```
You are Amber, a voice assistant helping coordinate a multi-participant call.

The call may include the main user and one or more invited participants. Pay close attention to who is speaking and who they are addressing.

When the main user asks you to invite someone, use the Invite tool. After the participant joins, briefly confirm that they joined, then let the participants talk.

If the participants are talking to each other and are not addressing you, use the Skip Turn tool and remain silent.

If someone addresses you directly, respond normally. You can use any of your configured tools to help complete the task.
```

You can adapt this prompt for your use case. For example, a scheduling assistant might be instructed to listen while participants compare availability, then resume when asked to book a time.

### Step 3: Add a Skip Turn tool

In a one-to-one call, an assistant usually responds after every user turn. In a multi-participant call, that can feel unnatural because the assistant may interrupt people who are talking to each other. The Skip Turn tool lets the assistant intentionally remain silent for a turn.

Add a Skip Turn tool when you want the assistant to:

- Stay silent while invited participants talk to the main user.
- Avoid responding to side conversations.
- Wait until someone directly addresses the assistant.
- Let humans confirm details with each other before the assistant takes action.

Skip Turn does not end the call or disable the assistant. It only tells the assistant not to speak for that turn. The assistant can respond again when a participant addresses it.

If your assistant should only respond when a specific name is spoken, or you know the participant names ahead of time, add those names to **Keyterm Boost** on the assistant's **Voice** tab. Boosting the names improves transcription accuracy on those exact words, which makes name-based Skip Turn rules far more reliable. Keyterm Boost accepts a comma-separated list, for example `Telnyx,Amber,Enzo`. It also supports [Dynamic Variables](dynamic-variables.md), so you can pass participant names or other caller-specific terms at conversation start, for example `Telnyx,{{participant_names}}`. It is supported by `deepgram/flux` and `deepgram/nova-3`. See the [Transcription Settings](transcription-settings.md) guide for details.

![Keyterm Boost field on the Voice tab of the AI Assistant settings](https://mintcdn.com/telnyx/HTJFiHu9LSNOk9Fg/img/ai-assistants-multi-participant/keyterm-boost-voice-tab.png?fit=max&auto=format&n=HTJFiHu9LSNOk9Fg&q=85&s=86d4b0c5296c04877d3ac820791df67d)

### Step 4: Use other assistant tools during the call

After a participant joins, the assistant can do everything it can do in a one-to-one voice call. It can call APIs, look up information, schedule meetings, update records, send messages, and more. The assistant can continue to combine tools with turn-taking logic. For example:

1. The assistant checks availability.
2. The assistant proposes a time to both participants.
3. The main user asks the invited participant whether the time works.
4. The assistant stays silent while the invited participant answers.
5. The assistant books the meeting after the participants confirm.

![Calendar availability tool call in a multi-participant call](https://mintcdn.com/telnyx/EIZ2j7WXogC8b17s/img/ai-assistants-multi-participant/calendar-tool-call.png?fit=max&auto=format&n=EIZ2j7WXogC8b17s&q=85&s=1265d85741b54e2ecab62976eadd6412)

![Meeting booking completed in a multi-participant call](https://mintcdn.com/telnyx/EIZ2j7WXogC8b17s/img/ai-assistants-multi-participant/booking-complete.png?fit=max&auto=format&n=EIZ2j7WXogC8b17s&q=85&s=839620e0e5130f61e4aeff9593ce4598)

### Best practices

**Be explicit about when to speak** — Tell the assistant when it should respond and when it should stay silent. Multi-participant calls work best when the assistant has clear turn-taking rules.

```
If James and Enzo are speaking directly to each other, use Skip Turn and stay silent. Only respond when someone addresses you by name or asks you to take an action.
```

**Review calls in Conversation History** — Use Conversation History to inspect the transcript, audio, tool calls, and tool responses. This is especially useful when tuning Skip Turn instructions because you can see why the assistant decided to speak or remain silent.
