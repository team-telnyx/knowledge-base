---
title: Telnyx Platform Overview and SIP Technical Reference
summary: Telnyx is a global Communications Platform as a Service (CPaaS) provider
  offering voice, messaging, real-time communications, AI inference, storage, and
  workflow automation over a privately-owned IP network. This page consolidates Telnyx's
  network specifications, supported SIP protocols and methods, interoperability partners,
  and configuration guidance for common PBX and softphone integrations.
sources:
- url: https://support.telnyx.com/en/articles/1130599-telnyx-tech-specs
- url: https://support.telnyx.com/en/articles/1130637-what-is-telnyx
- url: https://support.telnyx.com/en/articles/1130705-sip-protocols-that-telnyx-uses
- url: https://support.telnyx.com/en/articles/4304898-sip-trunking-methods-requests-responses
- url: https://support.telnyx.com/en/articles/5138185-bicom-pbxware-setup
- url: https://support.telnyx.com/en/articles/6128008-sipxecs-pbx-setup-config
- url: https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx
- url: https://support.telnyx.com/en/articles/6902981-understanding-sip-prack-protocol
updated_at: 2026-08-05T13:27:04Z
---

# Telnyx Platform Overview and SIP Technical Reference

*Part 1 of 4 — see also: [Part 2](telnyx-platform-overview-and-sip-technical-reference--part-2.md), [Part 3](telnyx-platform-overview-and-sip-technical-reference--part-3.md), [Part 4](telnyx-platform-overview-and-sip-technical-reference--part-4.md)*

Telnyx is a global Communications Platform as a Service (CPaaS) provider offering voice, messaging, real-time communications, AI inference, storage, and workflow automation over a privately-owned IP network. This page consolidates Telnyx's network specifications, supported SIP protocols and methods, interoperability partners, and configuration guidance for common PBX and softphone integrations.

## Telnyx Platform Overview

Telnyx is a Communications Platform as a Service (CPaaS) provider offering a broad suite of real-time communication services through a globally distributed, cloud-based platform. Telnyx enables seamless integration of voice, messaging, and connectivity into applications, systems, or workflows, with a focus on high-performance, secure, and scalable communication solutions.

Telnyx distinguishes itself with its privately-owned IP network, delivering industry-leading quality, reduced latency, and enhanced reliability, as well as offering comprehensive security and flexibility for global communications.

### Core Service Areas

- **VoIP Services** — High-quality internet-based voice communications with advanced call routing, IVR, and number masking, with global coverage and carrier-grade reliability. Telnyx has focused on improving voice quality and resiliency through active monitoring and leveraging its global points of presence (PoPs).
- **SMS/MMS Messaging** — Programmable messaging API supporting SMS and MMS for customer engagement, marketing, two-factor authentication (2FA), and customer service automation, with high-throughput and global delivery.
- **Number Provisioning and Porting** — Self-service platform for provisioning, managing, and porting phone numbers in real time, offering local, toll-free, and international numbers across 100+ countries.
- **Real-Time Communications and WebRTC** — WebRTC SDKs for integrating secure, high-quality video and audio calls directly into web and mobile applications, ideal for telemedicine, e-learning, and customer support.
- **Global Network and Connectivity** — A fully-meshed private IP network offering a global backbone for optimized communication traffic, with reduced latency, improved service uptime, and high-performance connectivity. Telnyx has expanded its private network by adding more PoPs and enhancing its Direct Routing services for Microsoft Teams and Operator Connect.
- **Elastic SIP Trunking** — Pay-as-you-go SIP trunking with no minimum commitments, dynamic scaling, high-availability, multi-region redundancy, and enhanced voice clarity. Advanced redundancy and failover mechanisms are available, and businesses can configure call failover policies.
- **Security and Compliance** — End-to-end encryption, secure APIs, and advanced access controls. Telnyx supports STIR/SHAKEN protocols to combat robocalls and call spoofing, and provides enhanced DDoS protection.
- **Flexibility and Scalability** — Granular billing options and API customization for managing usage efficiently.

### Extended Product Suite

- **Inference** — AI-powered service for embedding speech recognition, natural language processing (NLP), and machine learning models into voice and messaging applications. Key features include speech-to-text, text-to-speech, sentiment analysis, and language detection.
- **Storage** — Cloud-based media storage for voice recordings, video, and SMS/MMS attachments, with secure cloud storage, accessible APIs, compliance and audit readiness (GDPR, HIPAA), and data encryption.
- **Flow** — Visual drag-and-drop builder for creating automated communication workflows without extensive coding, with multi-channel support (voice, SMS, MMS, email), API integration, event-driven triggers, and custom notifications.

## Network and Points of Presence

Telnyx has several points of presence around the globe. Depending on your location, the following regional SIP endpoints provide the latest and most authoritative information on Telnyx's telephony and network specifications:

- [sip.telnyx.com](https://sip.telnyx.com/)
- [sip.telnyx.ca](https://sip.telnyx.ca/)
- [sip.telnyx.eu](https://sip.telnyx.eu/)
- [sip.telnyx.com.au](https://sip.telnyx.com.au/)

### Carrier Partners

- **North America:** AT&T, Verizon, CenturyLink, Level 3 Communications, Comcast, Inteliquent, West Communications, Windstream, Earthlink, Peerless, Irsitel, Bandwidth
- **International:** AT&T, Verizon, CenturyLink, Level 3 Communications, Comcast, Inteliquent, Tata Communications, British Telecom, Telefonica, IDT

## Supported SIP Transport Protocols

Telnyx Mission Control supports the following SIP transport protocols:

- UDP
- TCP
- TLS

Refer to [sip.telnyx.com](https://sip.telnyx.com/) for more detail.

![Telnyx SIP transport protocols](_images/d423060fe62f5b84.png)

## SIP Methods and Requests

SIP Trunking is a popular form of voice and fax communications over the Internet. The SIP specification is defined in [RFC 3261](https://tools.ietf.org/html/rfc3261), which describes Session Initiation Protocol (SIP) as an application-layer control (signalling) protocol for creating, modifying, and terminating sessions with one or more participants, including Internet telephone calls, multimedia distribution, and multimedia conferences.

There are fourteen SIP request methods, of which the first six are the most basic:

- **INVITE** — Establishes a session.
- **ACK** — Confirms an INVITE request.
- **BYE** — Ends a session.
- **CANCEL** — Cancels establishing of a session.
- **REGISTER** — Communicates user location (host name, IP).
- **OPTIONS** — Communicates information about the capabilities of the calling and receiving SIP phones.
- **PRACK** — Provisional Acknowledgement.
- **SUBSCRIBE** — Subscribes for Notification from the notifier.
- **NOTIFY** — Notifies the subscriber of a new event.
- **PUBLISH** — Publishes an event to the Server.
- **INFO** — Sends mid session information.
- **MESSAGE** — Transports Instant Messages.
- **UPDATE** — Modifies the state of a session.

### SIP Options Behaviour

SIP Options are used to determine if a user agent (e.g., a SIP phone or server) is available or reachable, and to query the capabilities of the user agent, such as which methods it supports. Telnyx's systems do not send SIP Options to customer SIP Connections, but Telnyx does accept and respond to SIP Options requests to its SIP Proxies from customer user agents.
