---
title: Telnyx Voice and SIP Essentials
summary: 'A practical guide to core Telnyx voice features and policies: E911 setup
  and testing, Caller ID and CNAM, DTMF configuration, organizing SIP traffic and
  outbound controls, SIP headers for transfers and billing, short-duration call policy,
  fax over T.38/G.711, and conference calling options.'
sources:
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
- url: https://support.telnyx.com/en/articles/1130710-what-is-dtmf-and-how-to-configure-it-on-telnyx
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/1130707-what-are-short-duration-calls
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
updated_at: 2026-05-14T11:30:56Z
---

# Telnyx Voice and SIP Essentials

*Part 2 of 2 — see also: [Part 1](telnyx-voice-and-sip-essentials--part-1.md)*

A practical guide to core Telnyx voice features and policies: E911 setup and testing, Caller ID and CNAM, DTMF configuration, organizing SIP traffic and outbound controls, SIP headers for transfers and billing, short-duration call policy, fax over T.38/G.711, and conference calling options.

## Fax over SIP with T.38 or G.711

Outbound fax setup
- Create a SIP Connection, then create an Outbound Voice Profile and select that connection for fax. By default, Telnyx sends a T.38 re-INVITE once fax tone is detected. You can change “T.38 Re-invite Initiated By” to Customer or Disabled (for G.711 faxing) in the connection’s Outbound settings.

Inbound fax setup
- Create a SIP Connection, purchase/assign a number, and assign the connection to the number. By default, Telnyx expects you to send a T.38 re-INVITE on inbound fax; if none is received, the call continues with G.711. In Numbers → My Numbers → gear icon → Expert Configuration, use “Enable T.38 Fax Gateway” to allow T.38; uncheck to force no T.38.

Fax device tips
- Set baud rate to 9600 or below; disable ECM; use “normal” resolution; optionally disable dial-tone detection if outbound dialing fails. SRTP is not supported when T.38 is enabled.

## Conference calling options

Yes—Telnyx supports conferencing.
- Voice API (recommended for full control): https://developers.telnyx.com/api-reference/conference-commands
- TeXML <Conference> (simple): https://developers.telnyx.com/docs/voice/programmable-voice/texml-verbs/conference
- SIP trunking with PBX (e.g., Asterisk/3CX)
- Video API for audio/video conferencing

Getting started: use TeXML for simple rooms, the Voice API for advanced control, or follow the step-by-step demo: https://developers.telnyx.com/docs/voice/programmable-voice/conferencing-demo
