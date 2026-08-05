---
title: WebRTC Voice SDKs
summary: The Telnyx WebRTC Voice SDKs enable client-side applications to instantiate
  and control Telnyx call legs from browsers and mobile devices. They translate between
  the WebRTC standard and Telnyx's SIP platform, providing worldwide PSTN coverage
  under the Programmable Voice API umbrella. This page covers SDK architecture, authentication
  options, the JS SDK client and call lifecycle, demo app setup, configuration interfaces,
  and Android push notifications.
sources:
- url: https://developers.telnyx.com/docs/voice/webrtc/architecture
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/credential-connections/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/jwt/index
- url: https://developers.telnyx.com/docs/voice/webrtc/auth/telephony-credentials/index
- url: https://developers.telnyx.com/docs/voice/webrtc/fundamentals
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/anatomy
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/demo-app/index
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/icalloptions
- url: https://developers.telnyx.com/docs/voice/webrtc/js-sdk/interfaces/iclientoptions
- url: https://developers.telnyx.com/docs/voice/webrtc/push-notifications/android
updated_at: 2026-08-05T14:08:20Z
---

# WebRTC Voice SDKs

*Part 1 of 7 — see also: [Part 2](webrtc-voice-sdks--part-2.md), [Part 3](webrtc-voice-sdks--part-3.md), [Part 4](webrtc-voice-sdks--part-4.md), [Part 5](webrtc-voice-sdks--part-5.md), [Part 6](webrtc-voice-sdks--part-6.md), [Part 7](webrtc-voice-sdks--part-7.md)*

The Telnyx WebRTC Voice SDKs enable client-side applications to instantiate and control Telnyx call legs from browsers and mobile devices. They translate between the WebRTC standard and Telnyx's SIP platform, providing worldwide PSTN coverage under the Programmable Voice API umbrella. This page covers SDK architecture, authentication options, the JS SDK client and call lifecycle, demo app setup, configuration interfaces, and Android push notifications.

## Overview

The Telnyx WebRTC Voice SDKs enable client-side applications to instantiate and control a Telnyx call leg. Developers integrating with the Telnyx voice platform are no longer constrained to inflexible SIP UAs such as PBX, Asterisk, or Zoiper. Instead, they can embed native voice capabilities client-side to work seamlessly with their voice application and achieve end-to-end visibility and control of the user experience.

The SDKs:

- Utilize the native client-end (browser or device) WebRTC API for cross browser/device compatibility.
- Adhere to the WebRTC standardization where media is transported via RTP over DTLS (SRTP / DTLS-SRTP).
- Implement WebRTC session negotiation (signaling) via JSON-RPC messages over Secure WebSocket (WSS).

Available SDKs:

- [JavaScript SDK](https://github.com/team-telnyx/webrtc)
- [Native iOS SDK](https://github.com/team-telnyx/telnyx-webrtc-ios)
- [Native Android SDK](https://github.com/team-telnyx/telnyx-webrtc-android)
- [Flutter SDK](https://github.com/team-telnyx/flutter-voice-sdk)

## Architecture

To properly architect solutions and troubleshoot issues, it is important to understand how the WebRTC Voice SDK fits among Telnyx's product portfolio.

![WebRTC Voice SDK architecture diagram](_images/webrtc-voicesdk-architecture.png)

### SDKs cannot be used on their own for calling

The WebRTC Voice SDKs merely lower the barriers for users to incorporate voice functionalities in their applications, i.e. instantiate a call leg. `rtc.telnyx.com` acts as the translation layer where on the SDK-facing side it adheres to the WebRTC standard and on the SIP-facing side it speaks SIP protocol. To the core SIP platform, `rtc.telnyx.com` is merely another SIP UA. All methods of authenticating an SDK client are based on [SIP connection](sip-connection.md) authentication.

This setup:

- Avails the WebRTC Voice SDKs the worldwide PSTN calling coverage.
- Puts those calls under the umbrella of the Programmable Voice API.

### SDKs cannot be used on their own to orchestrate call flow

The SDKs allow only local control, e.g. un/hold, un/mute, sending DTMF digits. To orchestrate call flow or manipulate audio, TeXML or the Call Control API must be used.

Consider a prepaid calling app where the user is told the remaining number of minutes before the call is placed. In the case of inadequate balance, they are told to top up before the call is hung up gracefully. The Voice SDKs are insufficient to achieve this on their own. Instead, the call control API must be incorporated:

- The call leg instantiated by the SDK must be parked via a setting on the SIP connection.
- The user's backend must respond to Telnyx webhooks, inject the necessary custom Text-To-Speech audio, place another outbound leg to the intended PSTN destination (or hang up due to insufficient balance), and finally bridge the WebRTC call leg with the PSTN leg.

### Role in the Telnyx Voice Product Suite

The WebRTC SDKs' role in the Telnyx voice product suite is to:

- Bring the Telnyx voice infrastructure closer to the ultimate end users. Developers do not need to maintain their own voice infrastructure; they can focus on building user-facing applications and business logic.
- Lower the barrier to access Telnyx's worldwide PSTN coverage. Developers do not need to know SIP; they can work with the widely adopted WebRTC standardization and API.
- Unify all the crucial building blocks of a CPaaS platform under the Telnyx umbrella. Developers do not need to manage multiple integrations and vendors in their stack.
