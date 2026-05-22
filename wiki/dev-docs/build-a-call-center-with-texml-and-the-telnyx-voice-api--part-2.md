---
title: Build a Call Center with TeXML and the Telnyx Voice API
summary: 'Learn how to stand up a simple yet extensible call center using TeXML and
  the Telnyx Voice API: route inbound calls to multiple agents, add queueing, voicemail
  and recording, detect answering machines on outbound legs, integrate Dialogflow
  ES, and optionally enable SIPREC for compliance recording.'
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-center
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ivr-demo/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/queueing-calls
- url: https://developers.telnyx.com/docs/voice/programmable-voice/storing-call-recordings
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-server/index
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-answering-machine
- url: https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection
- url: https://developers.telnyx.com/docs/voice/programmable-voice/l1-accounts-restirctions
updated_at: 2026-05-20T09:32:42Z
---

# Build a Call Center with TeXML and the Telnyx Voice API

*Part 2 of 2 — see also: [Part 1](build-a-call-center-with-texml-and-the-telnyx-voice-api--part-1.md)*

Learn how to stand up a simple yet extensible call center using TeXML and the Telnyx Voice API: route inbound calls to multiple agents, add queueing, voicemail and recording, detect answering machines on outbound legs, integrate Dialogflow ES, and optionally enable SIPREC for compliance recording.

## Security, webhooks, and local development
- Webhooks: set Webhook API Version to v2 and always return 200 OK. Consider verifying Telnyx webhook signatures with the account public key in your server (supported in official SDKs).
- Local tunneling: use ngrok to expose your local server; append your route paths (e.g., /TeXML/inbound) to the forwarding URL in the portal/app settings.
- SDK options and full flows are demonstrated in [IVR Demo](ivr-demo.md), [Call Tracking Demo](call-tracking-demo.md), and [Conferencing Demo](conferencing-demo.md).

## Limits on L1-verified accounts
If your account is only L1-verified, the following apply until you upgrade:
- An automated disclaimer is prepended to machine-generated speech (Speak/Play/Gather, AI-related actions, and TeXML Say/Play/AIGather).
- Outbound concurrency limits: max 100 calls/day and 10 calls/hour.
See [Programmable Voice restrictions for L1 verified accounts](programmable-voice-restrictions-for-l1-verified-accounts.md).

## Related tutorials and next steps
- Explore the full TeXML verb set and compatibility to extend flows.
- Build richer IVRs (Find-Me/Follow-Me, transfers, recording) with the Voice API examples.
- Add reporting by saving webhook payloads (call/queue/AMD/recording) to your datastore.
- Try conferencing and agent whisper/barge features: [Conferencing Demo](conferencing-demo.md).
- For number procurement + dynamic forwarding + analytics dashboards, see [Call Tracking Demo](call-tracking-demo.md).
