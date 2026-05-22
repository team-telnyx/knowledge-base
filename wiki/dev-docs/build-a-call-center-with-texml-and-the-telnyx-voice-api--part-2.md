---
title: Build a Call Center with TeXML and the Telnyx Voice API
summary: 'Learn how to stand up a simple yet extensible call center using TeXML and
  the Telnyx Voice API: route inbound calls to multiple agents, add queueing, voicemail
  and recording, detect answering machines on outbound legs, integrate Dialogflow
  ES, and optionally enable SIPREC for compliance recording.'
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-center
  content_hash: 0bf458fbc809c2b7a36e7a6d5372c778f686c193f37d80ece921378409ca1051
- url: https://developers.telnyx.com/docs/voice/programmable-voice/call-tracking
  content_hash: fcdfe6a4af680bf3cafd547884b274231be25a03c8ae875ecbfe4b815b3255ba
- url: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo
  content_hash: bfae202034bacfe313c356c98c338a6bb32a8f8295e1df3f037bb0be3368a472
- url: https://developers.telnyx.com/docs/voice/programmable-voice/dialogflow-es
  content_hash: 337f0ca2af78bd549d75b2fcaf8b2c682a725992eff0bcf44b45b7ed32b44bcb
- url: https://developers.telnyx.com/docs/voice/programmable-voice/ivr-demo/index
  content_hash: c86d85d99b148a6fa6bd5058414352fece7f68a44b7358f4392f8b7d63bbf008
- url: https://developers.telnyx.com/docs/voice/programmable-voice/queueing-calls
  content_hash: 56ab3dd523c210a790aa9895a6a3726a1a2a66d035ba39579b51cf050df9ebb6
- url: https://developers.telnyx.com/docs/voice/programmable-voice/storing-call-recordings
  content_hash: 8e6469160e60781d5a7734d99169040762f635ef0fc99ff097cbefbf3c1370e8
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client
  content_hash: 2e0b6e278dd3a8bf90febe2abee150c72c034a62aaff8f78ed3c06a4cc9e0512
- url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-server/index
  content_hash: f87b022b285ccb562258a1f2e65487db2acd65d18a70d2f9076c39a2a38047d1
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-answering-machine
  content_hash: ba81bcb1b369f61f4cb77064548a6f7ea827d8a5be2ff283c05a9e1ce48742ac
- url: https://developers.telnyx.com/docs/voice/programmable-voice/answering-machine-detection
  content_hash: 906d83ba4b672f2646f30e3311d3727b9e3c12e59d7e8f7d3d95fcdddbf00e56
- url: https://developers.telnyx.com/docs/voice/programmable-voice/l1-accounts-restirctions
  content_hash: f06cb0df36c49852ff58e838af48e8ff0f25794c94b7674643f0b1392271d258
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
