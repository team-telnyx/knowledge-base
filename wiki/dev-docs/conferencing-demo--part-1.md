---
title: Conferencing Demo
summary: A multi-language tutorial demonstrating how to build a Telnyx Voice API conferencing
  application using Python (Flask), PHP (Slim), Node.js, and Ruby (Sinatra). It covers
  webhook handling, conference creation, participant management, and exposing administrative
  endpoints for muting, holding, and pulling participants.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo
updated_at: 2026-08-05T14:03:11Z
---

# Conferencing Demo

*Part 1 of 4 — see also: [Part 2](conferencing-demo--part-2.md), [Part 3](conferencing-demo--part-3.md), [Part 4](conferencing-demo--part-4.md)*

A multi-language tutorial demonstrating how to build a Telnyx Voice API conferencing application using Python (Flask), PHP (Slim), Node.js, and Ruby (Sinatra). It covers webhook handling, conference creation, participant management, and exposing administrative endpoints for muting, holding, and pulling participants.

## Overview

The Telnyx Voice API (formerly Call Control) provides full programmatic control over a call's lifecycle, from initiation to completion, by emitting webhooks at each step. A subset of these capabilities is the [Conference API](https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks), which lets you create and manage conferences in response to inbound or outbound calls. This page walks through building a conferencing demo in four languages: Python (Flask), PHP (Slim), Node.js, and Ruby (Sinatra). Each tutorial assumes you have already [set up your developer account and environment](https://developers.telnyx.com/docs/development) and know how to [send commands](https://developers.telnyx.com/docs/voice/programmable-voice/sending-commands) and [receive webhooks](https://developers.telnyx.com/docs/voice/programmable-voice/receiving-webhooks).

Before starting any of the tutorials, configure your Voice API Application in the Mission Control Portal so that the *Webhook API Version* is **API v2** and the *Webhook URL* points at the public address of your server (use [ngrok](https://developers.telnyx.com/docs/development/development-tools/ngrok-setup/index#ngrok) to expose a local port). You will also need an [API Key](https://portal.telnyx.com/#/app/auth/v2).

## Python (Flask) Tutorial

⏱ **60 minutes build time** — [GitHub Repo](https://github.com/team-telnyx/python-conferencing-demo)

### Setup

Verify Python is installed:

```bash
$ python3 -v
```

Install Flask and the Telnyx Python SDK:

```bash
$ pip install flask
$ pip install telnyx
```

Create a Flask application that exposes a `/webhook` endpoint:

```python
import telnyx
from flask import Flask, request, Response

telnyx.api_key = "YOUR_TELNYX_API_KEY"

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def respond():
    print(request.json['data'])
    return Response(status=200)
```

Run the server:

```bash
$ export FLASK_APP=YOUR_FILE_NAME.py
$ flask run
```

Expose the local server with ngrok so Telnyx can deliver webhooks:

```bash
$ ./ngrok http 5000
```

Append `/webhook` to the ngrok URL and paste it into the *Send a webhook to the URL* field of your Voice API Application.

![URL Webhook Section](https://images.ctfassets.net/4b49ta6b3nwj/5fWNOgoZnSwcSj28O1B5Ld/f951a6c0b7118f3a27d86aa5d5035d5e/call_control_url_webhook.PNG)

### Receiving and interpreting webhooks

A typical Telnyx call webhook payload contains `record_type`, `event_type`, and a `payload` object with `call_control_id`, `call_leg_id`, `call_session_id`, `from`, `to`, `direction`, and `state`. Inspect `record_type` to confirm it is an `event`, then branch on `event_type`:

```python
def respond():
    data = request.json['data']
    if data.get('record_type') == 'event':
        event = data.get('event_type')
        if event == "call.initiated":
            print("Incoming call", flush=True)
    return Response(status=200)
```

### Creating a conference

Track active calls in a list and create a conference on the first `call.answered` event, joining subsequent callers to the existing conference:

```python
calls = []
conference = None

class call_info:
    call_control_id: ''
    call_leg_id: ''

@app.route('/webhook', methods=['POST'])
def respond():
    global calls, conference
    data = request.json.get('data')
    if data.get('record_type') == 'event':
        event = data.get('event_type')
        if event == "call.initiated":
            new_call = call_info()
            new_call.call_control_id = data.get('payload').get('call_control_id')
            new_call.call_leg_id = data.get('payload').get('call_leg_id')
            calls.append(new_call)
            print(telnyx.Call.answer(new_call), flush=True)
        elif event == "call.answered":
            call_id = data.get('payload').get('call_control_id')
            for call in calls:
                if call.call_control_id == call_id:
                    if not conference:
                        conference = telnyx.Conference.create(
                            beep_enabled="always",
                            call_control_id=call_id,
                            name="demo-conference"
                        )
                    else:
                        conference.join(call_control_id=call_id)
        elif event == "call.hangup":
            call_id = data.get('payload').get('call_leg_id')
            for call in calls:
                if call.call_leg_id == call_id:
                    calls.remove(call)
    return Response(status=200)
```

The full annotated version is available on [GitHub](https://github.com/team-telnyx/python-conferencing-demo).
