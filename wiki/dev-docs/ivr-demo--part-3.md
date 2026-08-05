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

*Part 3 of 3 — see also: [Part 1](ivr-demo--part-1.md), [Part 2](ivr-demo--part-2.md)*

A multi-language walkthrough of building an Interactive Voice Response (IVR) application on the Telnyx Voice API, covering Python (Flask), Node.js, and Ruby (Sinatra) implementations. Each section demonstrates how to receive webhooks, answer inbound calls, present gather prompts, interpret DTMF input, and transfer or bridge calls based on user selection.

## Ruby Implementation

### Setup

Install the required gems:

```bash
gem install telnyx sinatra dotenv
```

Or via a `Gemfile`:

```ruby
source 'https://rubygems.org'

gem 'sinatra'
gem 'telnyx'
gem 'dotenv'
```

### Environment Variables

| Variable | Description |
| --- | --- |
| `TELNYX_API_KEY` | Your [Telnyx API Key](https://portal.telnyx.com/#/app/api-keys) |
| `TELNYX_PUBLIC_KEY` | Your [Telnyx Public Key](https://portal.telnyx.com/#/app/account/public-key) |
| `TELNYX_APP_PORT` | Defaults to `8000`. The port the app will be served on. |

`.env`:

```
TELNYX_API_KEY=
TELNYX_PUBLIC_KEY=
TELNYX_APP_PORT=8000
```

In the Portal, ensure the Call Control Application's **Webhook API Version** is set to **API v2** and the **Webhook URL** points at your server (use [ngrok](https://ngrok.com/) for local development).

### Server Skeleton

```ruby
# frozen_string_literal: true

require 'sinatra'
require 'telnyx'
require 'dotenv/load'

Telnyx.api_key = ENV.fetch('TELNYX_API_KEY')
```

### Receiving Webhooks and Answering a Call

```ruby
set :port, ENV.fetch('TELNYX_APP_PORT')
post '/webhook' do
  request.body.rewind
  body = request.body.read
  data = JSON.parse(body)['data']

  if data['record_type'] == 'event'
    call = Telnyx::Call.new id: data['payload']['call_control_id'],
                            call_leg_id: data['payload']['call_leg_id']
    case data['event_type']
    when 'call.initiated'
      call.answer
      puts('Answered Call')

    when 'call.answered'
      call.gather_using_speak(voice: 'female',
                              language: 'en-US',
                              payload: 'Press some digits! The only valid options are 1 2 3',
                              valid_digits: '123',
                              invalid_payload: 'Invalid Entry Please try again')
      puts('Gather sent')

    when 'call.gather.ended'
      if data['payload']['status'] != 'call_hangup'
        call.speak(voice: 'female',
                   language: 'en-US',
                   payload: "You pressed: #{data['payload']['digits']}, You can now hangup")
        puts('DTMF spoke')
      end
    end
  end
end
```

The `valid_digits` parameter restricts caller input, and `invalid_payload` is replayed before the main prompt if the caller presses an invalid digit. The `call_hangup` status indicates the caller hung up before the gather completed — `speak` cannot be issued on an ended call.

### Authenticating Webhooks

Verify the Ed25519 signature on every incoming webhook to prevent spoofing:

```ruby
post '/webhook' do
  request.body.rewind
  body = request.body.read
  data = JSON.parse(body)['data']
  begin
    Telnyx::Webhook::Signature.verify(body,
                                      request.env['HTTP_TELNYX_SIGNATURE_ED25519'],
                                      request.env['HTTP_TELNYX_TIMESTAMP'])
  rescue Exception => e
    puts e
    halt 400, 'Webhook signature not valid'
  end
  # ...
end
```

Your public key is read from the environment and can be looked up in the [Telnyx Portal](https://portal.telnyx.com/#/app/account/public-key).

### Running the Server

```bash
$ bundle exec ruby ivr_demo_server.rb
```

Or, with globally installed gems:

```bash
$ ruby ivr_demo_server.rb
```

Expose the local port with ngrok and configure the Call Control Application's webhook URL as `{ngrok-url}/webhook`.

| Callback Type | URL |
| --- | --- |
| Inbound Calls Callback | `{ngrok-url}/webhook` |

## Conclusion

You now have three reference implementations of an IVR on the Telnyx Voice API. From here you can extend the flow with additional [Call Commands](call-commands.md) — for example, conferencing, recording, transcription, or branching into sub-menus — to build a production call experience. See the [Call Commands](call-commands.md) reference for the full set of available operations.
