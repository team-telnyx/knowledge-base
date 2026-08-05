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

*Part 1 of 4 — see also: [Part 2](call-tracking-with-programmable-voice--part-2.md), [Part 3](call-tracking-with-programmable-voice--part-3.md), [Part 4](call-tracking-with-programmable-voice--part-4.md)*

A tutorial for building a Call Tracking application using the Telnyx Programmable Voice API and Numbers API, available in both Python (Flask) and Node.js (Express). The app searches and orders local phone numbers, forwards inbound calls to designated destinations, and stores call metadata. The page also covers command retry best practices for handling 5XX errors, latency, and duplicate webhooks.

## Overview

Call Tracking combines the Telnyx Numbers API with Call Control (the Telnyx Voice API) to build a number ordering and call routing application. The Numbers API lets you search the phone number inventory in real time, filtering by area code, city, or state. Call Control lets you answer inbound calls, transfer them to a forwarding number, and capture post-call analytics.

A complete Call Tracking app can:

1. Search and order phone numbers by area code or city/state.
2. Receive inbound calls to the Telnyx phone number.
3. Transfer calls using Call Control to a designated forwarding number.
4. Store call metadata in a database.
5. Present the data in a front-end interface.

Two reference implementations are available:

- Python (Flask) — [GitHub repo](https://github.com/team-telnyx/demo-python-telnyx/tree/master/flask-call-tracking_call-control)
- Node.js (Express) — [GitHub repo](https://github.com/team-telnyx/demo-node-telnyx/tree/master/call-tracking)

## Prerequisites

### Create a Telnyx Mission Control account

Sign up at the [Telnyx portal](https://telnyx.com/sign-up), verify your email, and log in to the [Mission Control Portal](https://portal.telnyx.com).

### Set up a webhook tunnel with ngrok

Telnyx delivers call events as webhooks, so your local app needs a public URL. [ngrok](/development/development-tools/ngrok-setup/index#ngrok) is the easiest way to expose `localhost` over HTTPS. After installing it, run:

```
./ngrok http 8000
```

Make a note of the **HTTPS Forwarding URL** that ngrok prints.

### Create a Call Control Application

In the Portal, create a new [Call Control Application](https://portal.telnyx.com/#/app/call-control/applications). Paste the ngrok HTTPS URL into the webhook field, ensure **API v2** is selected, and save. Re-open the application and copy its **ID** — this is your `TELNYX_CONNECTION_ID`.

### Create an Outbound Voice Profile

Create a new [Outbound Voice Profile](https://portal.telnyx.com/#/app/outbound-profiles), click **Add connections/apps to profile**, and select the Call Control Application you just created. In **International Allowed Destinations**, enable the regions where your app will operate.
