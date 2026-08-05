---
title: Call Tracking with Programmable Voice
summary: A tutorial for building a Call Tracking application using the Telnyx Programmable
  Voice API and Numbers API, available in both Python (Flask) and Node.js (Express).
  The app searches and orders local phone numbers, forwards inbound calls to designated
  destinations, and stores call metadata. The page also covers command retry best
  practices for handling 5XX errors, latency, and duplicate webhooks.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking
- url: https://developers.telnyx.com/docs/voice/programmable-voice/command-retries
updated_at: 2026-08-05T14:03:06Z
---

# Call Tracking with Programmable Voice

*Part 3 of 4 — see also: [Part 1](call-tracking-with-programmable-voice--part-1.md), [Part 2](call-tracking-with-programmable-voice--part-2.md), [Part 4](call-tracking-with-programmable-voice--part-4.md)*

A tutorial for building a Call Tracking application using the Telnyx Programmable Voice API and Numbers API, available in both Python (Flask) and Node.js (Express). The app searches and orders local phone numbers, forwards inbound calls to designated destinations, and stores call metadata. The page also covers command retry best practices for handling 5XX errors, latency, and duplicate webhooks.

## Node.js implementation

### Install dependencies

```
mkdir call-tracking
cd call-tracking
npm init
```

```
npm i dotenv
npm i express
npm i telnyx
```

### Environment variables

| Variable | Description |
| --- | --- |
| `TELNYX_API_KEY` | Your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) |
| `TELNYX_PUBLIC_KEY` | Your [Telnyx Public Key](https://portal.telnyx.com/#/app/account/public-key) |
| `TELNYX_CONNECTION_ID` | The ID from your Call Control Application |
| `PORT` | The port the app listens on (defaults to `8000`) |

Example `.env`:

```
TELNYX_PUBLIC_KEY=
TELNYX_API_KEY=
TELNYX_CONNECTION_ID=
PORT=8000
```

### Project structure

```
touch index.js
touch db.js
touch callControl.js
touch bindings.js
```

- `index.js` — Express server entry point
- `db.js` — in-memory database for bindings and calls
- `callControl.js` — inbound/outbound webhook handlers
- `bindings.js` — number search, ordering, and binding routes

### Express server

`index.js` mounts two routers — `/call-control` and `/bindings`:

```javascript
import 'dotenv/config';
import express from 'express';
import bindings from './bindings';
import callControl from './callControl';

const app = express();
app.use(express.json());
app.use(express.urlencoded({extended: true}));

app.use('/call-control', callControl);
app.use('/bindings', bindings);

app.listen(process.env.PORT);
console.log(`Server listening on port ${process.env.PORT}`);
```

### In-memory database

`db.js` exports a `bindings` array and four functions: `addPhoneNumberBinding`, `getDestinationPhoneNumber`, `saveCall`, and `getBinding`.

```javascript
export const bindings = [];

export const addPhoneNumberBinding = (telnyxPhoneNumber, destinationPhoneNumber) => {
  const index = bindings.findIndex(b => b.telnyxPhoneNumber === telnyxPhoneNumber);
  if (index > 0) {
    return {
      ok: false,
      message: `Binding of Telnyx: ${telnyxPhoneNumber} already exists`,
      binding: bindings[index],
    };
  }
  bindings.push({ telnyxPhoneNumber, destinationPhoneNumber, calls: [] });
  return { ok: true };
};

export const getDestinationPhoneNumber = telnyxPhoneNumber =>
  bindings
    .filter(b => b.telnyxPhoneNumber === telnyxPhoneNumber)
    .reduce((_, b) => b.destinationPhoneNumber, '');

export const saveCall = callWebhook => {
  const telnyxPhoneNumber = callWebhook.payload.to;
  const index = bindings.findIndex(b => b.telnyxPhoneNumber === telnyxPhoneNumber);
  bindings[index].calls.push(callWebhook);
};

export const getBinding = telnyxPhoneNumber =>
  bindings.filter(b => b.telnyxPhoneNumber === telnyxPhoneNumber);
```

### Bindings routes

`bindings.js` exposes a `POST` route that [searches available numbers](/api-reference/phone-number-search/list-available-phone-numbers) by area code, [orders the first match](/api-reference/phone-number-orders/create-a-number-order) with the configured `connection_id`, and saves the binding. A `GET` route returns all bindings, optionally filtered by `telnyxPhoneNumber`.

```javascript
import express from 'express';
import Telnyx from 'telnyx';
import db from './db';

const telnyx = new Telnyx(process.env.TELNYX_API_KEY);
export const router = express.Router();
const CONNECTION_ID = process.env.TELNYX_CONNECTION_ID;

const searchNumbers = async (req, res, next) => {
  if (!req.body.areaCode || !req.body.destinationPhoneNumber || req.body.areaCode.length !== 3) {
    res.send({
      message: 'Invalid search criteria, please send 3 digit areaCode',
      example: '{ "areaCode": "919", "destinationPhoneNumber": "+19198675309" }',
    });
    return;
  }
  try {
    const availableNumbers = await telnyx.availablePhoneNumbers.list({
      filter: {
        national_destination_code: req.body.areaCode,
        features: ['sms', 'voice', 'mms'],
        limit: 1,
      },
    });
    const phoneNumber = availableNumbers.data.reduce((_, e) => e.phone_number, '');
    if (!phoneNumber) {
      res.send({ message: 'No available phone numbers' }).status(200);
    } else {
      res.locals.phoneNumber = phoneNumber;
      next();
    }
  } catch (e) {
    console.log(e);
    res.send({ message: 'Error searching numbers' }).status(400);
  }
};

const orderNumber = async (req, res, next) => {
  try {
    const result = await telnyx.numberOrders.create({
      connection_id: CONNECTION_ID,
      phone_numbers: [{ phone_number: res.locals.phoneNumber }],
    });
    res.locals.phoneNumberOrder = result.data;
    next();
  } catch (e) {
    console.log(e);
    res.send({ message: `Error ordering number: ${res.locals.phoneNumber}` }).status(400);
  }
};

const saveBinding = async (req, res) => {
  try {
    db.addPhoneNumberBinding(res.locals.phoneNumber, req.body.destinationPhoneNumber);
    res.send(res.locals.phoneNumberOrder);
  } catch (e) {
    res.send(e).status(409);
  }
};

const getBindings = async (req, res) => {
  if (req.query.telnyxPhoneNumber) {
    res.send(db.getBinding(req.query.telnyxPhoneNumber)).status(200);
  } else {
    res.send(db.bindings);
  }
};

router.route('/')
  .post(searchNumbers, orderNumber, saveBinding)
  .get(getBindings);
```

### Call Control routes

`callControl.js` handles inbound and outbound webhook events. On `call.initiated` it [answers the call](/api-reference/call-commands/answer-call); on `call.answered` it [transfers the call](/api-reference/call-commands/transfer-call#transfer-call) to the destination stored in the database; on `call.hangup` it saves the [hangup event](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index#hangup) for post-call analytics.

```javascript
import express from 'express';
import Telnyx from 'telnyx';
import db from './db';

const telnyx = new Telnyx(process.env.TELNYX_API_KEY);
export const router = express.Router();

const outboundCallController = async (req, res) => {
  res.sendStatus(200);
  const event = req.body.data;
  console.log(`Received Call-Control event: ${event.event_type} DLR with call_session_id: ${event.payload.call_session_id}`);
};

const handleInboundAnswer = async (call, event, req) => {
  try {
    const webhook_url = new URL('/call-control/outbound', `${req.protocol}://${req.hostname}`).href;
    const destinationPhoneNumber = db.getDestinationPhoneNumber(event.payload.to);
    await call.transfer({ to: destinationPhoneNumber, webhook_url });
  } catch (e) {
    console.log(`Error transferring on call_session_id: ${call.call_session_id}`);
    console.log(e);
  }
};

const handleInboundHangup = (call, event) => {
  db.saveCall(event);
};

const inboundCallController = async (req, res) => {
  res.sendStatus(200);
  const event = req.body.data;
  const call = new telnyx.Call({
    call_control_id: event.payload.call_control_id,
    call_session_id: event.payload.call_session_id,
    call_leg_id: event.payload.call_leg_id,
  });
  switch (event.event_type) {
    case 'call.initiated':
      await call.answer();
      break;
    case 'call.answered':
      await handleInboundAnswer(call, event, req);
      break;
    case 'call.hangup':
      handleInboundHangup(call, event);
      break;
    default:
      console.log(`Received Call-Control event: ${event.event_type} DLR with call_session_id: ${call.call_session_id}`);
  }
};

router.route('/outbound').post(outboundCallController);
router.route('/inbound').post(inboundCallController);
```

### Run the Node.js app

1. Launch ngrok: `./ngrok http 8000`
2. In the Portal, edit your Call Control Application and set the webhook URL to `<ngrok-url>/call-control/inbound`.
3. Start the server: `node index.js`

### Create a binding

Send a `POST` to `/bindings` with a 3-digit `areaCode` and a `destinationPhoneNumber`:

```
POST http://ead8b6b4.ngrok.io/bindings HTTP/1.1
Content-Type: application/json; charset=utf-8

{
  "areaCode": "919",
  "destinationPhoneNumber": "+19198675309"
}
```

The app searches the inventory, orders the first match, and creates a binding so inbound calls are forwarded to the destination.

### List bindings and call history

`GET /bindings` returns all bindings. Each binding includes a `calls` array of saved `call.hangup` webhooks; the array length equals the number of calls received, and call duration is the difference between `start_time` and `end_time`.

```
GET http://ead8b6b4.ngrok.io/bindings HTTP/1.1
```

```
[
  {
    "telnyxPhoneNumber": "+19193234088",
    "destinationPhoneNumber": "+19198675309",
    "calls": [
      {
        "event_type": "call.hangup",
        "id": "cddecb2a-bb3c-4e90-8e85-e1b6d51a901b",
        "occurred_at": "2021-01-26T16:00:55.413407Z",
        "payload": {
          "call_control_id": "v2:GegDKN9TMwSPYwUALiLrqNd-TpfER6QgvvNg49reRPtz6mhrhBiTTg",
          "call_leg_id": "a704d6e6-5fef-11eb-9e5f-02420a0f7568",
          "call_session_id": "a704df56-5fef-11eb-9718-02420a0f7568",
          "connection_id": "1557657082730120568",
          "end_time": "2021-01-26T16:00:55.413407Z",
          "from": "+14154886792",
          "hangup_cause": "normal_clearing",
          "hangup_source": "caller",
          "sip_hangup_cause": "200",
          "start_time": "2021-01-26T16:00:46.873401Z",
          "to": "+19193234088"
        },
        "record_type": "event"
      }
    ]
  }
]
```
