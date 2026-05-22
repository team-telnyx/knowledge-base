---
title: TeXML Fundamentals
summary: TeXML is Telnyx’s XML-based markup language for building programmable voice
  call flows with simple, sequential “verbs” and “nouns.” This page explains what
  TeXML is, how TeXML Applications fetch and run your instructions, quick ways to
  host XML with TeXML Bin, using dynamic templates and HTTP requests, and how TeXML
  aligns with Twilio’s TwiML for fast migration.
sources:
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-fundamentals/index
  content_hash: 44926f6fe1cdd9db555df44e6663d8d682b8d0d09aa667c7871761f5298f3597
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-setup
  content_hash: cdc8eea33def935c1c4adf405b8ca4050bd9daee2cab77e9a2ed7d982f3c7cae
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-quickstart
  content_hash: 423683bc710e343878daf7cb12062097ff9dcc03f94be8ef93398906030dee8a
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-bin-dynamic
  content_hash: bdd4ecaf617ffeb47b5e20f2858f95e8b338f0f50dd6d1f1dd74c6901aa61ce0
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-instruction-fetching
  content_hash: 30586d67aef7fbe6013710694cba378084f7f5c77c095e5911d8fb45555ffe1c
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-interpreter
  content_hash: 95b262ca75a1f895956d5675895bcd12649dab5a80c5a39bc6ae5545e10d49e5
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-sending-http-requests
  content_hash: ef808de2ca1772907239fbb75f9d7e2387cb79e2087b640b617a0f3117cd2612
- url: https://developers.telnyx.com/docs/voice/programmable-voice/texml-twiml-compatibility
  content_hash: 0fbd8134313bac0367ec56e73c772504a60d4fa08cae006714ed5bc52de178d7
updated_at: 2026-05-20T09:36:55Z
---

# TeXML Fundamentals

*Part 2 of 2 — see also: [Part 1](texml-fundamentals--part-1.md)*

TeXML is Telnyx’s XML-based markup language for building programmable voice call flows with simple, sequential “verbs” and “nouns.” This page explains what TeXML is, how TeXML Applications fetch and run your instructions, quick ways to host XML with TeXML Bin, using dynamic templates and HTTP requests, and how TeXML aligns with Twilio’s TwiML for fast migration.

## Best practices
- Keep instruction fetch latency low; consider AnchorSite latency routing for optimal data center selection.
- Validate CallSid and expected parameters; implement webhook error handling and use a Failover URL.
- Return HTTP 200 with well‑formed XML (<Response> root) and keep responses small.
- Use Telnyx-provided parameters (for example, From, To) to personalize flows.
- For outbound: prefer TeXML Calls API when you want application‑level control; use parked outbound on SIP trunking for trunk‑level control.
- Use TeXML Secrets for credentials; never hardcode keys in XML.
- Test with varied parameter combinations and edge cases (timeouts, unavailable URLs, invalid inputs).

## See also
- [TeXML Quickstart: Simple Text-to-Speech Demo](texml-quickstart-simple-text-to-speech-demo.md)
- [TeXML Bin Simple Voicemail and Call Forwarding](texml-bin-simple-voicemail-and-call-forwarding.md)
- [TeXML Bin Dynamic Content](texml-bin-dynamic-content.md)
- [Sending HTTP requests in TeXML - tutorial](sending-http-requests-in-texml-tutorial.md)
- [TeXML Instruction Fetching](texml-instruction-fetching.md)
- [TeXML Interpreter](texml-interpreter.md)
- [TeXML and TwiML Compatibility](texml-and-twiml-compatibility.md)
