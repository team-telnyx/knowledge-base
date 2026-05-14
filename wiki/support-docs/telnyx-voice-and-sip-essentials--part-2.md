---
title: Telnyx Voice and SIP Essentials
summary: 'A practical guide to core Telnyx voice features and policies: E911 setup
  and testing, Caller ID and CNAM, DTMF configuration, organizing SIP traffic and
  outbound controls, SIP headers for transfers and billing, short-duration call policy,
  fax over T.38/G.711, and conference calling options.'
sources:
- url: https://support.telnyx.com/en/articles/1130683-e911-setup-guide
  content_hash: 1fdde1d3b7a07125725e6beff707bea2c34994ecf73ad25dfc6cbcacec5fc76e
- url: https://support.telnyx.com/en/articles/1130647-register-e911-addresses
  content_hash: e7aa8f7df17ce21043032611a61b110b20558c20d9a323e747cb7b656d94c18e
- url: https://support.telnyx.com/en/articles/1130709-how-do-i-test-e911-service
  content_hash: ea536e75afa53eec60880712f4611f065b894a31097eb57bbeb71c291f241f1c
- url: https://support.telnyx.com/en/articles/1130710-what-is-dtmf-and-how-to-configure-it-on-telnyx
  content_hash: 15af5a30be29b9f76f2827eb63a370a0bef4b816d3ddbc994c55ecb1c6211aa0
- url: https://support.telnyx.com/en/articles/1130720-caller-id-outbound-vs-cnam
  content_hash: a5c4bcf279708062c83ddf570095efee456e808f675b2e05e3f82f1fad4de176
- url: https://support.telnyx.com/en/articles/1130721-distinguish-your-outbound-profiles-dids
  content_hash: cc44abb155d2979d4f425127ccbce05eca945af332f1f7dc7853abfba8f1e6a2
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
  content_hash: ec0fc8534c339a1648f07649f7cd4cae8995cfcb3c1991d55d6aa1b5b6fd4910
- url: https://support.telnyx.com/en/articles/12580667-configure-repeat-call-guard-on-outbound-voice-profiles-beta
  content_hash: 522a0582d43c80a2d6bc6efec747326b65a11e7bd9d99e5b2cffe73f99be2baa
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
  content_hash: 67a3e25a960125ae76f36108f3cfc724252403c88ed3a037543de70d69f74624
- url: https://support.telnyx.com/en/articles/1130707-what-are-short-duration-calls
  content_hash: 6ddcc43284cda8b1d723284af01eb440b59cdbd647ac2514cacc177adf4301d6
- url: https://support.telnyx.com/en/articles/1130656-set-up-inbound-caller-id-name-incoming
  content_hash: 5a0bdc9ef6f264292392de0682c348ff96ae464f87eb2dcc1cd63e7670b55431
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
  content_hash: 8a6b2171a1e87c496f2a31689703fa77bc5672d771c10e5867bd53f77433e33e
- url: https://support.telnyx.com/en/articles/1130677-does-telnyx-support-conference-calls
  content_hash: afc57bf4cdcea3daf5b4d5065ca963e7114f3b9e4d5bba6cfdf8cb4441760b8f
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
