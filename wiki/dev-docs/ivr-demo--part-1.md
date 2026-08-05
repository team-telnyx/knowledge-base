---
title: IVR Demo
summary: A multi-language walkthrough of building an Interactive Voice Response (IVR)
  application on the Telnyx Voice API, covering Python (Flask), Node.js, and Ruby
  (Sinatra) implementations. Each section demonstrates how to receive webhooks, answer
  inbound calls, present gather prompts, interpret DTMF input, and transfer or bridge
  calls based on user selection.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ivr-demo/index
updated_at: 2026-08-05T14:03:53Z
---

# IVR Demo

*Part 1 of 3 — see also: [Part 2](ivr-demo--part-2.md), [Part 3](ivr-demo--part-3.md)*

A multi-language walkthrough of building an Interactive Voice Response (IVR) application on the Telnyx Voice API, covering Python (Flask), Node.js, and Ruby (Sinatra) implementations. Each section demonstrates how to receive webhooks, answer inbound calls, present gather prompts, interpret DTMF input, and transfer or bridge calls based on user selection.

## Overview

The Telnyx Voice API lets you build Interactive Voice Response (IVR) applications that answer inbound calls, play prompts, collect DTMF input, and route the caller to a destination. This page walks through three reference implementations:

- **Python** — Flask + ngrok, ~60 minutes build time. [GitHub Repo](https://github.com/team-telnyx/ivr-demo-python)
- **Node.js** — Express + ngrok, ~60 minutes build time. [GitHub Repo](https://github.com/team-telnyx/demo-findme-ivr)
- **Ruby** — Sinatra + ngrok, ~30 minutes build time.

All three tutorials assume you have already [set up your developer account and environment](development.md) and know how to [send commands](sending-commands.md) and [receive webhooks](receiving-webhooks.md) using the Telnyx Voice API.

## Core Voice API Commands

Across all three languages, the IVR demos rely on a small subset of call control commands:

- [Bridge Calls](bridge-calls.md)
- [Dial](dial.md)
- [Speak Text](speak-text.md)
- [Gather Using Speak](gather-using-speak.md)
- [Hangup](hangup.md)
- [Recording Start](recording-start.md)

The full set of available commands is documented in the [Call Commands](call-commands.md) reference.

## Client State

Because the Telnyx Voice API is stateless and asynchronous, your application will receive several events of the same type (for example, multiple `call.answered` events when a call is bridged). The `client_state` parameter is the key to disambiguating them: it lets you tag a command with a base64-encoded payload that is echoed back on subsequent webhooks, so you can branch your logic based on where the call is in its flow.

In the Python demo, `client_state` is used to mark the inbound leg so the gather prompt is only played once. In the Node.js demo, it carries a JSON object containing the `bridgeId` of the parked call so the two legs can be joined later. In the Ruby demo, signature verification is layered on top of the same webhook flow.

## Python Implementation

### Prerequisites

Confirm Python is installed:

```bash
$ python3 -v
```

Install Flask and the Telnyx SDK:

```bash
$ pip install flask
$ pip install telnyx
```

### Environment Variables

| Variable | Description |
| --- | --- |
| `TELNYX_API_KEY` | Your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) |
| `TELNYX_PUBLIC_KEY` | Your [Telnyx Public Key](https://portal.telnyx.com/#/app/account/public-key) |

Copy `.env.sample` to `.env` in the project root and fill in the values. The app uses [python-dotenv](https://github.com/theskumar/python-dotenv) to load them:

```python
from dotenv import load_dotenv

load_dotenv()
telnyx.api_key = os.getenv('TELNYX_API_KEY')
```

### Server and Webhook Setup

Create a minimal Flask app that exposes a webhook endpoint:

```python
app = Flask(__name__)

@app.route('/Callbacks/Voice/Inbound', methods=['POST'])
def respond():
    print(request.json['data'])
    return Response(status=200)

if __name__ == '__main__':
    app.run()
```

Set the Flask entry point and start the server:

```bash
$ export FLASK_APP=YOUR_FILE_NAME.py
$ python3 app.py
```

Expose the local port with ngrok so Telnyx can deliver webhooks:

```bash
$ ./ngrok http 5000
```

Copy the ngrok URL into the **Send a webhook to the URL** field of your Call Control Application in the Telnyx Portal.

![URL Webhook Section](https://mintcdn.com/telnyx/fKocYsWR7KyFBdpc/img/diagram_ivr_demo_darkmode-.png?fit=max&auto=format&n=fKocYsWR7KyFBdpc&q=85&s=b9537dccda749a338175bbd77935ed16)

### Receiving and Interpreting Webhooks

A typical Telnyx call webhook payload looks like:

```json
{
  "data": {
    "event_type": "call.initiated",
    "id": "a2fa3fa6-4e8c-492d-a7a6-1573b62d0c56",
    "occurred_at": "2020-07-10T05:08:59.668179Z",
    "payload": {
      "call_control_id": "v2:rcSQADuW8cD1Ud1O0YVbFROiQ0_whGi3aHtpnbi_d34Hh6ELKvLZ3Q",
      "call_leg_id": "76b31010-c26b-11ea-8dd4-02420a0f6468",
      "call_session_id": "76b31ed4-c26b-11ea-a811-02420a0f6468",
      "caller_id_name": "+17578390228",
      "client_state": null,
      "connection_id": "1385617721416222081",
      "direction": "incoming",
      "from": "+14234567891",
      "start_time": "2020-07-10T05:08:59.668179Z",
      "state": "parked",
      "to": "+12624755500"
    },
    "record_type": "event"
  },
  "meta": {
    "attempt": 1,
    "delivered_to": "http://59d6dec27771.ngrok.io/webhook"
  }
}
```

Check `record_type == 'event'` and then branch on `event_type`:

```python
def respond():
    data = request.json['data']
    if data.get('record_type') == 'event':
        event = data.get('event_type')
        print(event, flush=True)
        if event == "call.initiated":
            print("Incoming call", flush=True)
    return Response(status=200)
```

### Building the IVR

The Python demo implements a "Weather Hotline" IVR with the following flow:

1. Answer the incoming call.
2. Present the menu options.
3. Transfer the caller based on their selection.

#### IVR Class

A small class generates the gather prompt from a JSON config so the spoken text can be edited without touching Python:

```python
class IVR:
    def __init__(self, intro, iterable, items, **kwargs):
        self.intro = intro
        self.iterable = iterable
        self.items = items
        self.phone_number_table = {}
        self.valid_inputs = ''
        self.prompt = self.intro
        length = len(self.items)
        for i in range(length):
            itemName = self.items[i]['itemName']
            phone_number = self.items[i]['phoneNumber']
            digit = str(i + 1)
            prompt = self.iterable % (itemName, digit)
            self.prompt = f'{self.prompt}, {prompt}'
            self.phone_number_table[digit] = phone_number
            self.valid_inputs = f'{self.valid_inputs}{digit}'

    def get_prompt(self):
        return self.prompt

    def get_valid_digits(self):
        return self.valid_inputs

    def get_phone_number_from_digit(self, digit):
        return self.phone_number_table.get(digit, False)
```

#### Configuration

`ivrConfig.json`:

```json
{
    "intro": "Thank you for calling the Weather Hotline.",
    "iterable": "For weather in %s press %s",
    "items": [
        { "itemName": "Chicago, Illinois", "phoneNumber": "+18158340675" },
        { "itemName": "Raleigh, North Carolina", "phoneNumber": "+19193261052" }
    ]
}
```

#### Answering the Incoming Call

On `call.initiated`, base64-encode the direction and use it as `client_state` so the outbound leg can be distinguished later:

```python
if event == 'call.initiated':
    direction = data.get('payload').get('direction')
    if direction == 'incoming':
        encoded_client_state = base64.b64encode(direction.encode('ascii'))
        client_state_str = str(encoded_client_state, 'utf-8')
        res = my_call.answer(client_state=client_state_str)
        print(res, flush=True)
```

#### Presenting Options

On `call.answered`, only play the gather prompt if `client_state` is present (the outbound transferred leg will also emit `call.answered` with a null `client_state`):

```python
elif event == 'call.answered':
    client_state = data.get('payload').get('client_state')
    if client_state:
        speak_str = my_ivr.get_prompt()
        res = my_call.gather_using_speak(
            payload=speak_str,
            valid_digits=my_ivr.get_valid_digits(),
            language='en-US',
            voice='male')
        print(res, flush=True)
```

#### Interpreting Button Presses

On `call.gather.ended`, look up the destination number and transfer the caller:

```python
elif event == 'call.gather.ended':
    digits_pressed = data.get('payload').get('digits')
    phone_number_lookup = my_ivr.get_phone_number_from_digit(digits_pressed)
    if phone_number_lookup:
        res = my_call.transfer(to=phone_number_lookup)
        print(res, flush=True)
```

The full commented source is available in the [GitHub Repo](https://github.com/team-telnyx/ivr-demo-python).
