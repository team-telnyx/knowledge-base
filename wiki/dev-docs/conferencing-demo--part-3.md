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

*Part 3 of 4 — see also: [Part 1](conferencing-demo--part-1.md), [Part 2](conferencing-demo--part-2.md), [Part 4](conferencing-demo--part-4.md)*

A multi-language tutorial demonstrating how to build a Telnyx Voice API conferencing application using Python (Flask), PHP (Slim), Node.js, and Ruby (Sinatra). It covers webhook handling, conference creation, participant management, and exposing administrative endpoints for muting, holding, and pulling participants.

## Node.js Tutorial

⏱ **60 minutes build time** — [GitHub Repo](https://github.com/team-telnyx/demo-conference-node)

### Prerequisites

Verify Node is installed:

```bash
$ node -v
```

Install the required dependencies:

```bash
$ npm install superagent --save
$ npm install request --save
```

Add your API key, waiting audio URL, and Voice API Application ID to `telnyx-account-v2.json`:

```json
{
  "telnyx_api_auth_v2": "<your-api-v2-key-here>",
  "telnyx_waiting_url": "<your-path-to-waiting-song-here>",
  "telnyx_connection_id": "<your-call-control-application-id>"
}
```

You can find the Voice API Application ID in the Mission Portal by editing the application.

![Finding the Voice API ID for a Voice API Application](https://images.ctfassets.net/4b49ta6b3nwj/3QSrrdNoH5ar5hvnu3H2fY/fe52cb157da846063c26501647f76441/call-control-id.png)

### Voice API command helpers

Every Telnyx Voice API command follows the same pattern: a `POST` to `https://api.telnyx.com/v2/calls/{call_control_id}/actions/{action}` (or `/v2/conferences/{conf_id}/actions/{action}` for conference-level commands) with a bearer token and a JSON body. The basic set used in this demo includes:

- [Answer](https://developers.telnyx.com/docs/api-reference/call-commands/answer-call)
- [Hangup](https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/hangup/index#hangup)
- [Speak](https://developers.telnyx.com/docs/api-reference/call-commands/speak-text)
- [Dial](https://developers.telnyx.com/docs/api-reference/call-commands/dial)
- [Record start / stop](https://developers.telnyx.com/docs/api-reference/call-commands/recording-start)

The conference command set includes:

- [Join conference](https://developers.telnyx.com/docs/api-reference/conference-commands/join-a-conference)
- [Mute / Unmute participant](https://developers.telnyx.com/docs/api-reference/conference-commands/mute-conference-participants)
- [Hold / Unhold participant](https://developers.telnyx.com/docs/api-reference/conference-commands/hold-conference-participants)

A generic helper looks like:

```javascript
function call_control_COMMAND_NAME(f_call_control_id, f_INPUT) {
  const cc_action = 'COMMAND_NAME';
  const request = superagent
    .set('Content-Type', 'application/json')
    .set('Accept', 'application/json')
    .set('Authorization', `Bearer ${f_telnyx_api_auth_v2}`)
    .post(`https://api.telnyx.com/v2/calls/${f_call_control_id}/actions/${cc_action}`)
    .send({ PARAM1: f_INPUT });
  request.then((response) => { /* ... */ }).catch((error) => { console.log(error); });
}
```

`Client State` is a base64-encoded string you can attach to commands so that, when the resulting webhook arrives, you can correlate it with a specific IVR level or flow.

### Building the conference system

The Node demo exposes a webhook at `https://<webhook_domain>:8081/telnyx-conf/start` and a set of administrative `GET` endpoints. Global state is kept in memory:

```javascript
const g_appName = "telnyx-conf-v2";
const g_ivr_voice = 'female';
const g_ivr_language = 'en-GB';
const g_conf_id = 'no-conf';
const g_on_hold = 'false';
const g_participants = new Map();
```

The webhook handler reacts to events as follows:

- **`call.initiated`** — answer the call (inbound or outbound).
- **`call.answered`** — if no conference exists, speak a welcome, create the conference, and add the participant; otherwise speak a welcome and join the existing conference.
- **`conference.created`** — log the new conference ID.
- **`conference.join`** — if this is the first participant, place them on hold with the waiting audio; if it is the second, unhold the first.
- **`conference.leave`** — remove the participant; if the room is empty, reset `g_conf_id`; if only one remains, place them back on hold.
- **Other events** (`call.speak.ended`, `call.hangup`, `dtmf`, etc.) — acknowledge with `200 OK`.

### Administrative endpoints

The Node demo exposes HTTP `GET` endpoints for runtime control of the conference room:

- `GET /telnyx-conf-v2/list` — list participants and the conference ID.
- `GET /telnyx-conf-v2/mute?participant=x` — mute a participant.
- `GET /telnyx-conf-v2/unmute?participant=x` — unmute a participant.
- `GET /telnyx-conf-v2/hold?participant=x` — place a participant on hold.
- `GET /telnyx-conf-v2/unhold?participant=x` — resume a participant.
- `GET /telnyx-conf-v2/pull?number=x` — dial out to a number and add them to the conference (URL-encode `+` as `%2B` for E.164 numbers).
- `GET /telnyx-conf-v2/record-start?participant=x` — start recording a call leg.
- `GET /telnyx-conf-v2/record-stop?participant=x` — stop recording a call leg.

Start the server with:

```javascript
const server = rest.listen(8081, function () {
  const host = server.address().address;
  const port = server.address().port;
});
```

## Ruby (Sinatra) Tutorial

⏱ **60 minutes build time** — [GitHub Repo](https://github.com/team-telnyx/demo-conference-ruby)

### Setup

Install the required gems:

```bash
gem install telnyx sinatra
```

Or use a Gemfile:

```ruby
source 'https://rubygems.org'

gem 'sinatra'
gem 'telnyx'
```

Create `conference_demo_server.rb`:

```ruby
require 'sinatra'
require 'telnyx'

CONFIG = {
  telnyx_api_key: 'YOUR_API_KEY',
  phone_number: 'TELNYX_PHONE_NUMBER',
  connection_id: 'CONNECTION_ID',
}

Telnyx.api_key = CONFIG[:telnyx_api_key]
```

### Receiving webhooks and creating a conference

```ruby
calls = []
conference = nil

set :port, 9090
post "/webhook" do
  request.body.rewind
  data = JSON.parse(request.body.read)['data']

  if data['record_type'] == 'event'
    case data['event_type']
    when 'call.initiated'
      call = Telnyx::Call.new id: data['payload']['call_control_id'],
                              call_leg_id: data['payload']['call_leg_id']
      calls << call
      call.answer
    when 'call.answered'
      call = calls.find { |c| c.id == data['payload']['call_control_id'] }
      if conference.nil?
        conference = Telnyx::Conferences.create call_control_id: call.id,
                                                name: 'demo-conference'
      else
        conference.join call_control_id: call.id
      end
    when 'call.hangup'
      calls.reject! { |call| call.call_leg_id == data['payload']['call_leg_id'] }
    end
  end
end
```

### Authenticating webhooks

Protect your endpoint by verifying the Telnyx signature with your public key:

```ruby
ENV['TELNYX_PUBLIC_KEY'] = 'YOUR_PUBLIC_KEY'

post '/webhook' do
  request.body.rewind
  body = request.body.read
  data = JSON.parse(body)['data']

  Telnyx::Webhook::Signature.verify(body,
                                    request.env['HTTP_TELNYX_SIGNATURE_ED25519'],
                                    request.env['HTTP_TELNYX_TIMESTAMP'])
  # ...
end
```

`Telnyx::Webhook::Signature.verify` raises `SignatureVerificationError` if the signature does not match the payload. Fetch your public key from the [Telnyx Portal](https://portal.telnyx.com/#/app/account/public-key).

### Usage

Start the server:

```bash
bundle exec ruby conference_demo_server.rb
# or, with globally installed gems:
ruby conference_demo_server.rb
```

Expose the local port with ngrok and add the public URL plus `/webhook` to your Voice API Application's *Webhook URL* field. The [`api-v2` directory](https://github.com/team-telnyx/demo-conference-ruby/tree/master/api-v2) in the GitHub repo contains an extended version with console-based conference controls.
