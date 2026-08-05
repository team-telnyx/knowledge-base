---
title: Programmable Voice
summary: The Telnyx Programmable Voice API enables you to integrate voice calling
  capabilities into your applications, providing flexible inbound and outbound call
  control, real-time webhooks, and advanced features such as Conversation Relay, Deepfake
  Detection, Dialogflow ES integration, and AI-driven gather flows.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conversation-relay
- url: https://developers.telnyx.com/docs/voice/programmable-voice/deepfake-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
- url: https://developers.telnyx.com/docs/voice/programmable-voice/gather-using-ai/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/get-started/index
updated_at: 2026-08-05T14:03:33Z
---

# Programmable Voice

*Part 1 of 4 — see also: [Part 2](programmable-voice--part-2.md), [Part 3](programmable-voice--part-3.md), [Part 4](programmable-voice--part-4.md)*

The Telnyx Programmable Voice API enables you to integrate voice calling capabilities into your applications, providing flexible inbound and outbound call control, real-time webhooks, and advanced features such as Conversation Relay, Deepfake Detection, Dialogflow ES integration, and AI-driven gather flows.

## Overview

The Telnyx Programmable Voice API enables you to integrate voice calling capabilities into your applications. It provides a powerful platform for managing both inbound and outbound calls through a range of commands and configurations, offering flexibility for use cases such as call routing, caller verification, conversational AI agents, fraud screening, and structured data collection.

## Prerequisites

- A Telnyx account (sign up at the [Telnyx portal](https://telnyx.com/sign-up)).
- An API key obtained from the [Telnyx Mission Control Portal](https://portal.telnyx.com/).
- A development environment prepared for API integration.
- Caller and receiver numbers in E.164 format (for example, `+1234567890`).
- An Outbound Voice Profile configured in your Telnyx account.
- A Voice API Application with a webhook URL set up.

## Core Concepts

- **Voice API Applications** act as the backbone for handling incoming and outgoing calls, providing a flexible framework for routing and verification.
- **Outbound Voice Profile** configures outbound calls, including billing and traffic destinations. It must be associated with the Voice API application. See the [Outbound Voice Profile API reference](/api-reference/outbound-voice-profiles/create-an-outbound-voice-profile).
- **Webhooks** deliver real-time notifications about call events to your server. They are integral for monitoring call progress, handling call outcomes, and integrating with external systems. See the [Receiving Webhooks](receiving-webhooks.md) guide.

## Hello World: Dial an Outbound Call

Using a simple HTTP POST request, you can dial a number from a given connection (Voice API application):

```
curl --location 'https://api.telnyx.com/v2/calls' \
--header 'Accept: application/json' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YourAPIKey' \
--data '{
   "to":"+13125790015",
   "from":"+13125790968",
   "connection_id":"234423"
}'
```
