---
title: Telnyx Voice, Messaging, and Billing Reference
summary: This page consolidates Telnyx documentation covering VoIP and telecommunications
  protocols (RTP, UDP, TCP, SIP, SDP), audio codecs and SDP parameters, external call
  transfers, webhooks (including WhatsApp webhooks and signing key rotation), A2P
  vs P2P traffic types and the P2P exemption process, toll-free opt-in workflow templates,
  and payment methods including ACH Direct Debit and Bitcoin.
sources:
- url: https://support.telnyx.com/en/articles/1130723-voip-telecommunications-protocols
- url: https://support.telnyx.com/en/articles/11898569-toll-free-opt-in-workflow-description
- url: https://support.telnyx.com/en/articles/13117410-how-external-call-transfers-work
- url: https://support.telnyx.com/en/articles/13986487-how-to-configure-whatsapp-webhooks
- url: https://support.telnyx.com/en/articles/3192298-audio-and-codecs
- url: https://support.telnyx.com/en/articles/3199007-guide-to-using-our-traffic-type-feature
- url: https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks
- url: https://support.telnyx.com/en/articles/7045419-ach-direct-debit-payment-method
- url: https://support.telnyx.com/en/articles/8370064-update-webhook-sign-key-guide
- url: https://support.telnyx.com/en/articles/8379618-bitcoin-payment-method
- url: https://support.telnyx.com/en/articles/8685561-p2p-definition-and-exemption-process
updated_at: 2026-07-17T09:07:29Z
---

# Telnyx Voice, Messaging, and Billing Reference

*Part 1 of 8 — see also: [Part 2](telnyx-voice-messaging-and-billing-reference--part-2.md), [Part 3](telnyx-voice-messaging-and-billing-reference--part-3.md), [Part 4](telnyx-voice-messaging-and-billing-reference--part-4.md), [Part 5](telnyx-voice-messaging-and-billing-reference--part-5.md), [Part 6](telnyx-voice-messaging-and-billing-reference--part-6.md), [Part 7](telnyx-voice-messaging-and-billing-reference--part-7.md), [Part 8](telnyx-voice-messaging-and-billing-reference--part-8.md)*

This page consolidates Telnyx documentation covering VoIP and telecommunications protocols (RTP, UDP, TCP, SIP, SDP), audio codecs and SDP parameters, external call transfers, webhooks (including WhatsApp webhooks and signing key rotation), A2P vs P2P traffic types and the P2P exemption process, toll-free opt-in workflow templates, and payment methods including ACH Direct Debit and Bitcoin.

## VoIP and Telecommunications Protocols

RTP, UDP, TCP, SIP, and SDP are the core protocols that underpin modern voice and messaging over IP. Understanding how they fit together is essential when working with Telnyx's network.

- **RTP (Real-Time Transport Protocol)** — First published in 1996 as RFC-1889 and superseded by RFC 3550 in 2003, RTP is an application-layer network protocol that delivers audio and video over IP networks. It typically runs over UDP but can also use TCP. RTP carries the media stream and works in conjunction with SIP. UDP is favored for RTP because dropping packets is preferable to waiting on delayed packets, while TCP favors reliability over reduced latency.
- **UDP (User Datagram Protocol)** — The transport-layer protocol most commonly used for RTP because it favors real-time transmission.
- **TCP (Transmission Control Protocol)** — An alternative transport for RTP that prioritizes reliability over latency.
- **SIP (Session Initiation Protocol)** — Used to establish and control multimedia sessions. Works in conjunction with RTP and SDP.
- **SDP (Session Description Protocol)** — Describes the parameters of a multimedia session, including codecs, ports, and connection information. SDP does not deliver any media itself; it is used in conjunction with RTP.

An RTP session is established for each multimedia stream and includes a port and an IP address. Because audio and video use separate media streams, the receiver can deselect one or the other. RTP typically uses UDP ports between 1024 and 65535, with ports negotiated through SIP and SDP. Profiles and payloads are also defined; the profiles specify the codecs used to encode the payload data. Audio payload formats commonly offered include G.711U, G.711A, G.722, G.729, and OPUS, while typical video payload formats are H.263, H.264, and MPEG-4.
