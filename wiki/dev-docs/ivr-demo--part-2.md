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

*Part 2 of 3 — see also: [Part 1](ivr-demo--part-1.md), [Part 3](ivr-demo--part-3.md)*

A multi-language walkthrough of building an Interactive Voice Response (IVR) application on the Telnyx Voice API, covering Python (Flask), Node.js, and Ruby (Sinatra) implementations. Each section demonstrates how to receive webhooks, answer inbound calls, present gather prompts, interpret DTMF input, and transfer or bridge calls based on user selection.

## Node.js Implementation

### Prerequisites

Confirm Node is installed:

```bash
$ node -v
```

Install the Telnyx SDK and Express:

```bash
$ npm install telnyx --save
$ npm install express --save
```

### Configuration

Store credentials and connection details in a `telnyx-config` module:

```javascript
export const telnyx_config = {
  api: "YOURAPIV2KEYgoeshere",
  connection_id: "1110011011",
  telnyx_did: "+18888675309",
  c_fwd_number: "+13128675309"
};
```

Instantiate the SDK:

```javascript
import Telnyx from 'telnyx';
import telnyxAuth from "./telnyx-config";

const telnyx = new Telnyx(telnyxAuth.apiKey);
```

### Voice API Command Patterns

Every command follows the same pattern: instantiate a `telnyx.Call` with the `call_control_id`, then call the command method with its parameters.

**Bridge:**

```javascript
const bridge_call = new telnyx.Call({ call_control_id: l_call_control_id });
bridge_call.bridge({ call_control_id: l_client_state_o.bridgeId });
```

**Dial:**

```javascript
const { data: call } = await telnyx.calls.create({
  connection_id: g_connection_id,
  to: g_forwarding_did,
  from: req.body.data.payload.from,
  client_state: Buffer.from(JSON.stringify(l_client_state)).toString("base64"),
  timeout_secs: "30",
});
```

**Gather Using Speak:**

```javascript
const gather = new telnyx.Call({ call_control_id: l_call_control_id });
gather.gather_using_speak({
  payload: "Call Forwarded press 1 to accept or 2 to reject",
  voice: g_ivr_voice,
  language: g_ivr_language,
  valid_digits: "123",
  client_state: Buffer.from(JSON.stringify(l_client_state)).toString("base64"),
});
```

**Speak:**

```javascript
const speak = new telnyx.Call({ call_control_id: l_call_control_id });
speak.speak({
  payload: "Please Leave a Message After the Tone",
  voice: g_ivr_voice,
  language: g_ivr_language,
  client_state: Buffer.from(JSON.stringify(l_client_state)).toString("base64"),
});
```

**Hangup:**

```javascript
const hangup_call = new telnyx.Call({ call_control_id: l_call_control_id });
hangup_call.hangup();
```

**Recording Start:**

```javascript
const record_call = new telnyx.Call({ call_control_id: l_call_control_id });
record_call.record_start({
  format: "mp3",
  channels: "single",
  play_beep: true,
  client_state: Buffer.from(JSON.stringify(l_client_state)).toString("base64"),
});
```

**SMS Notification:**

```javascript
telnyx.messages.create({
  from: g_call_control_did,
  to: g_forwarding_did,
  text: `You have a new Voicemail ${req.body.data.payload.recording_urls.mp3}`,
});
```

### Building the Find Me / Follow Me IVR

The Node demo implements a richer flow:

1. Park the incoming call.
2. Dial the user's PSTN number.
3. Present an IVR (Accept / Reject) with a 20-second timeout.
4. On accept, bridge the parked call with the dialed call. On reject, send the parked call to voicemail.
5. At any time, `*9` triggers on-demand call recording.
6. Send an SMS (and optionally an email) when a recording is saved.

![IVR Demo Diagram](https://images.ctfassets.net/4b49ta6b3nwj/5B6v9Bygi4iVGH8N42C1Hw/a663b0e9619b95e3b4d1df4c8749e611/Diagram_IVR_Demo_DarkMode.png)

#### Webhook Endpoint

```javascript
rest.post(`/${g_appName}/followme`, async (req, res) => {
  // APP CODE GOES HERE
});
```

This exposes a URL like `http://MY_DOMAIN_URL/telnyx-findme/followme`.

#### Global Variables

```javascript
const g_appName = "telnyx-findme";
const g_ivr_voice = "female";
const g_ivr_language = "en-GB";
```

#### Event Handlers

**`call.initiated` → Dial the user:**

```javascript
if (l_hook_event_type == "call.initiated") {
  if (req.body.data.payload.direction == "incoming") {
    let l_client_state = {
      clientState: "stage-bridge",
      bridgeId: l_call_control_id,
    };
    const { data: call } = await telnyx.calls.create({
      connection_id: g_connection_id,
      to: g_forwarding_did,
      from: req.body.data.payload.from,
      client_state: Buffer.from(JSON.stringify(l_client_state)).toString("base64"),
      timeout_secs: "30",
    });
    res.end();
  }
}
```

**`call.answered` → Gather Using Speak:**

```javascript
else if (l_hook_event_type == "call.answered") {
  if (l_client_state_o.clientState == "stage-bridge") {
    let l_client_state = {
      clientState: "stage-dial",
      bridgeId: l_client_state_o.bridgeId,
    };
    const gather = new telnyx.Call({ call_control_id: l_call_control_id });
    gather.gather_using_speak({
      payload: "Call Forwarded press 1 to accept or 2 to reject",
      voice: g_ivr_voice,
      language: g_ivr_language,
      valid_digits: "123",
      client_state: Buffer.from(JSON.stringify(l_client_state)).toString("base64"),
    });
    res.end();
  }
}
```

> Every webhook must be acknowledged with `200 OK`, otherwise Telnyx will retry delivery.

**`call.bridged` → No-op:**

```javascript
else if (l_hook_event_type == "call.bridged") {
  res.end();
}
```

**`*` DTMF or `call.speak.ended` → Start recording:**

```javascript
else if (
  req.body.data.payload.digit === "*" ||
  l_hook_event_type == "call.speak.ended"
) {
  let l_client_state = {
    clientState: "stage-voicemail-greeting",
    bridgeId: null,
  };
  const record_call = new telnyx.Call({ call_control_id: l_call_control_id });
  record_call.record_start({
    format: "mp3",
    channels: "single",
    play_beep: true,
    client_state: Buffer.from(JSON.stringify(l_client_state)).toString("base64"),
  });
  res.end();
}
```

> DTMF appears in both `call.gather.ended` (key `digits`) and `call.dtmf.received` (key `digit`).

**`call.gather.ended` → Bridge or send to voicemail:**

```javascript
else if (l_hook_event_type == "call.gather.ended") {
  const l_dtmf_number = req.body.data.payload.digits;
  if (l_client_state_o.clientState == "stage-dial" && l_dtmf_number) {
    if (l_dtmf_number == "1") {
      const bridge_call = new telnyx.Call({ call_control_id: l_call_control_id });
      bridge_call.bridge({ call_control_id: l_client_state_o.bridgeId });
    } else if (l_dtmf_number == "2") {
      let l_client_state = {
        clientState: "stage-voicemail-greeting",
        bridgeId: null,
      };
      const answer_bridge_call = new telnyx.Call({
        call_control_id: l_client_state_o.bridgeId,
      });
      answer_bridge_call.answer({
        client_state: Buffer.from(JSON.stringify(l_client_state)).toString("base64"),
      });
      const hangup_call = new telnyx.Call({ call_control_id: l_call_control_id });
      hangup_call.hangup();
    }
  }
  res.end();
}
```

**`call.recording.saved` → SMS notification:**

```javascript
else if (l_hook_event_type == "call.recording.saved") {
  telnyx.messages.create({
    from: g_call_control_did,
    to: g_forwarding_did,
    text: `You have a new Recording ${req.body.data.payload.recording_urls.mp3}`,
  });
  res.end();
}
```

#### Running the App

```javascript
const PORT = 8081;
rest.listen(PORT, () => {
  console.log(`app listening at http://localhost:${PORT}/${g_appName}`);
});
```

```bash
$ npm run dev
```
