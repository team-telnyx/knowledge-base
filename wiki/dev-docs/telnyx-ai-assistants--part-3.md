---
title: Telnyx AI Assistants
summary: Telnyx AI Assistants are configurable voice and chat agents that combine
  large language models, text-to-speech, speech-to-text, and real-time tools into
  a single no-code or API-driven platform. Assistants can handle inbound and outbound
  calls, multi-participant conversations, scheduled outreach, structured conversation
  workflows, and integrations with enterprise systems — all managed from the Mission
  Control Portal or the Assistants API.
sources:
- url: https://developers.telnyx.com/docs/inference/ai-assistants/multi-participant-calls
  content_hash: 1ae007d98f0a079c6d9fa1acec7fd9203c2af7ca66d212171ca711e3da94d0c7
- url: https://developers.telnyx.com/docs/inference/ai-assistants/no-code-voice-assistant/index
  content_hash: d07570a4fd30575a9f261a3f4988a2208d3115a79d4b0278f337f6a791606a6b
- url: https://developers.telnyx.com/docs/inference/ai-assistants/scheduled-events
  content_hash: dc746a7ef6ef062d69a462a97a0c854a29da9576afc690ef62164b2ffecfcaf8
- url: https://developers.telnyx.com/docs/inference/ai-assistants/tools-library
  content_hash: 97d3c9a314e001171d8cdac0f6a5707f088237e0e32561470fc8a92acbfdf55c
- url: https://developers.telnyx.com/docs/inference/ai-assistants/transcription-settings
  content_hash: 155c354770eb16a9fe21e6eb194f7391f2ece82729736cef4540e5a28ee21ca4
- url: https://developers.telnyx.com/docs/inference/ai-assistants/version-testing-traffic-distribution
  content_hash: 1ea79c8dd0f948970ff36ae3e9de9dd2efaf764f85c57429bb3366a97a0eb55b
- url: https://developers.telnyx.com/docs/inference/ai-assistants/voicemail-detection-on-transfer
  content_hash: 1a351e40f03eb9e9387cc17956573eb2a3423d73dde019f2ec3879f1bcc72dd1
- url: https://developers.telnyx.com/docs/inference/ai-assistants/workflows
  content_hash: 69f833223aa236218e653b4f8fd0f4a0cd8aa0aecf5872dfe647ef741dca081f
updated_at: 2026-06-11T10:30:28Z
---

# Telnyx AI Assistants

*Part 3 of 4 — see also: [Part 1](telnyx-ai-assistants--part-1.md), [Part 2](telnyx-ai-assistants--part-2.md), [Part 4](telnyx-ai-assistants--part-4.md)*

Telnyx AI Assistants are configurable voice and chat agents that combine large language models, text-to-speech, speech-to-text, and real-time tools into a single no-code or API-driven platform. Assistants can handle inbound and outbound calls, multi-participant conversations, scheduled outreach, structured conversation workflows, and integrations with enterprise systems — all managed from the Mission Control Portal or the Assistants API.

## Scheduled Events

Scheduled events let an assistant kick off an outbound phone call or SMS at a fixed point in the future. The platform stores the event, dispatches it at the scheduled time, and reports the outcome through callbacks. For phone calls, automatic retries can be configured for recipient-side failures (busy, no-answer, failed, canceled).

### State machine

1. **`pending`** — waiting for the scheduled time.
2. **`in_progress`** — dispatched to Telnyx.
3. **`completed`** — recipient reached (call answered and ended normally, or SMS delivered).
4. **`failed`** — could not be completed and no further attempts will be made.

### Retry configuration (phone calls only)

| Field | Type | Description |
|---|---|---|
| `max_retries_client_errors` | integer, 0–10 | Additional dispatches after the initial attempt. `0` (default) disables retries. |
| `retry_interval_secs` | integer, 60–86400 | Seconds between attempts. Required when `max_retries_client_errors > 0`. |

Retry fields must be omitted for `sms_chat` events. Total attempts = initial + `max_retries_client_errors` (e.g. `max_retries_client_errors: 3` → up to 4 attempts). When a retryable failure occurs and budget remains, `scheduled_at_fixed_datetime` is advanced to **now + `retry_interval_secs`** and status returns to `pending`.

### API reference

| Method | Path | Purpose |
|---|---|---|
| `POST` | `/v2/ai/assistants/{assistant_id}/scheduled_events` | Create |
| `GET` | `/v2/ai/assistants/{assistant_id}/scheduled_events` | List (paginated) |
| `GET` | `/v2/ai/assistants/{assistant_id}/scheduled_events/{event_id}` | Fetch one |
| `DELETE` | `/v2/ai/assistants/{assistant_id}/scheduled_events/{event_id}` | Cancel a pending event |

### Create-event fields

| Field | Required | Channels | Description |
|---|---|---|---|
| `telnyx_conversation_channel` | Yes | both | `phone_call` or `sms_chat` |
| `telnyx_end_user_target` | Yes | both | Recipient (phone number or SIP URI) |
| `telnyx_agent_target` | Yes | both | Number the assistant calls/sends from |
| `scheduled_at_fixed_datetime` | Yes | both | ISO-8601 timestamp, must be in the future |
| `text` | Yes for SMS | `sms_chat` | Message body |
| `conversation_metadata` | No | both | Key/value metadata for the conversation |
| `dynamic_variables` | No | both | Variables for prompt interpolation |
| `max_retries_client_errors` | No | `phone_call` | Retry budget |
| `retry_interval_secs` | No | `phone_call` | Seconds between retries |

### Inspecting attempt history

Each phone-call event exposes a `call_attempts` array with one entry per terminal dispatch, including `attempt_number`, `attempted_at`, `call_status`, `call_duration`, and `telnyx_call_control_id`.

### Choosing a retry policy

- **Short intervals (60–300 s)**: Time-sensitive flows (verification, urgent reminders).
- **Medium intervals (5–30 min)**: General outreach campaigns.
- **Long intervals (1–24 h)**: Daily-cadence flows (missed bill reminders, callback queues).
- Total reach time = `max_retries_client_errors × retry_interval_secs` — ensure this fits within acceptable calling hours.
- Three to five retries is usually sufficient.

## Voicemail Detection on Transfer

When a transferred call reaches voicemail, the assistant can detect it and take action — keeping the caller connected throughout.

### How it works

1. The assistant initiates a transfer.
2. AMD monitors the transfer destination.
3. If voicemail is detected, the configured action triggers.
4. The assistant returns to the caller and continues the conversation.

### Configuration options

**Detection mode**:

| Value | Description |
|---|---|
| `disabled` | No voicemail detection (default) |
| `premium` | ML-based detection, recommended for production |

**Actions on detection**:

| Action | Behavior |
|---|---|
| `stop_transfer` | Cancel transfer, return assistant to caller |
| `leave_message_and_stop_transfer` | Deliver a TTS message to voicemail, then cancel transfer and return |

**Voicemail message options** (when using `leave_message_and_stop_transfer`):

| `type` | Description |
|---|---|
| `message` | Play custom TTS text (specified in `message` field) |
| `warm_transfer_instructions` | Use the warm transfer audio instructions as the voicemail message |

Configure via the Portal under the transfer tool's **Voicemail Detection** section, or via the API in the transfer tool's `voicemail_detection` object.

## Tools and Integrations

### Built-in tools

| Tool | Purpose |
|---|---|
| **Hangup** | End the call (included by default) |
| **Invite** | Bring another participant into the current call |
| **Skip Turn** | Stay silent for the current turn |
| **Webhook** | Make API requests with configurable headers, path, query, and body parameters |
| **Handoff** | Transfer the conversation to another assistant (shared or distinct voice) |
| **Transfer** / **SIP Refer** | Transfer or refer a call to named targets |
| **Send DTMF** | Interact with legacy IVR systems |

Webhook tools can be tested with sample data directly from the Portal.

### Tools Library

The Tools Library lets you create tools in a shared library and assign them to any assistant. Define a tool once and reuse it across assistants; updating a shared tool keeps behavior consistent everywhere. Existing inline (legacy) tools continue to work and can be migrated at your own pace.

1. Navigate to **AI, Storage and Compute** > **AI Tools** in the Portal.
2. Click **Create New Tool**.
3. When building or editing an assistant, assign tools from the library.

### Model Context Protocol (MCP) Servers

Configure an MCP Server in the Portal and add it to an assistant. Telnyx automatically includes a `telnyx_conversation_id` with each MCP tool call (on the `_meta` field), usable for tracking and controlling conversation flow. This ID is set by the platform and is not susceptible to prompt injection attacks.

If a server URL must be kept secret, store it as an integration secret. The conversation ID is also available via the [Start AI Assistant command](https://developers.telnyx.com/api-reference/call-commands/start-ai-assistant) or the dynamic variables webhook payload.

### Knowledge Bases

Upload files or provide URLs in the **Knowledge Bases** tab to give the assistant custom context for retrieval.

### Insights

Run structured and unstructured analysis on every conversation via the **Insights** tab. Assign an Insight Group (reusable across assistants) and optionally configure a webhook URL to receive insights after they are generated.

### Enterprise integrations

Connect assistants to external platforms to access data, create tickets, update records, and automate workflows:

- Salesforce
- ServiceNow
- Jira
- HubSpot
- Zendesk
- Intercom
- GitHub
- Greenhouse

Select the integration, enter credentials, connect it to the assistant, and choose enabled tools.

### Third-party voice providers

- **ElevenLabs**: Select ElevenLabs as the TTS provider and reference a stored API key secret. Requires a paid plan.
- **Vapi**: Select Vapi as the provider and reference a stored API key secret. For multilingual agents, set the transcription model to `deepgram/nova-3`.
- **OpenAI**: Change the assistant's model to an OpenAI model (e.g. `openai/gpt-4o`) and store your OpenAI API key as an integration secret. Requires a paid plan.

API keys are stored securely as integration secrets and cannot be retrieved after storage.
