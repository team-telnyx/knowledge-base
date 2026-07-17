---
title: Telnyx Platform Overview and Grandstream Device Setup
summary: Telnyx is a global Communications Platform as a Service (CPaaS) provider
  offering voice, messaging, WebRTC, Elastic SIP Trunking, AI Inference, Storage,
  and Flow workflow automation over a privately owned IP network. This page consolidates
  Telnyx's product suite, network and partner details, hardware compatibility, encryption
  and STUN/TURN configuration, reseller program, and step-by-step setup guides for
  Grandstream GXP16XX, GXP, GXP21XX, and HT802 devices.
sources:
- url: https://support.telnyx.com/en/articles/1130599-telnyx-tech-specs
- url: https://support.telnyx.com/en/articles/1130637-what-is-telnyx
- url: https://support.telnyx.com/en/articles/1130638-does-telnyx-provide-any-hardware
- url: https://support.telnyx.com/en/articles/1130641-telnyx-recommended-hardware-configurations
- url: https://support.telnyx.com/en/articles/1130646-where-is-telnyx-located
- url: https://support.telnyx.com/en/articles/1130655-can-i-resell-your-services
- url: https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx
- url: https://support.telnyx.com/en/articles/1130682-telnyx-stun-and-turn-server
- url: https://support.telnyx.com/en/articles/1130692-does-telnyx-have-a-blog
- url: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
- url: https://support.telnyx.com/en/articles/5725071-grandstream-ht802-telnyx-setup
- url: https://support.telnyx.com/en/articles/5815720-grandstream-gxp-telnyx-setup
- url: https://support.telnyx.com/en/articles/5819218-grandstream-gxp21xx
updated_at: 2026-07-17T09:01:55Z
---

# Telnyx Platform Overview and Grandstream Device Setup

*Part 1 of 3 — see also: [Part 2](telnyx-platform-overview-and-grandstream-device-setup--part-2.md), [Part 3](telnyx-platform-overview-and-grandstream-device-setup--part-3.md)*

Telnyx is a global Communications Platform as a Service (CPaaS) provider offering voice, messaging, WebRTC, Elastic SIP Trunking, AI Inference, Storage, and Flow workflow automation over a privately owned IP network. This page consolidates Telnyx's product suite, network and partner details, hardware compatibility, encryption and STUN/TURN configuration, reseller program, and step-by-step setup guides for Grandstream GXP16XX, GXP, GXP21XX, and HT802 devices.

## Overview

Telnyx is a Communications Platform as a Service (CPaaS) provider offering voice, messaging, connectivity, AI inference, storage, and workflow automation services over a privately owned, fully meshed global IP network. The platform is designed for businesses that need scalable, programmable communications with carrier-grade reliability and direct routing across multiple regions.

## Company and Locations

Telnyx was founded in 2009 and is headquartered in Austin, Texas, with additional offices in Denver, Dublin, and Amsterdam. The company also employs remote staff around the world.

**Headquarters address:**

600 Congress Avenue  
14th Floor  
Austin, TX 78701

## Network and Points of Presence

Telnyx operates multiple points of presence (PoPs) around the globe. For the latest authoritative information on telephony and network specifications, refer to the regional SIP portals:

- [sip.telnyx.com](https://sip.telnyx.com/)
- [sip.telnyx.ca](https://sip.telnyx.ca/)
- [sip.telnyx.eu](https://sip.telnyx.eu/)
- [sip.telnyx.com.au](https://sip.telnyx.com.au/)

### Carriers and Partners

**North America:** AT&T, Verizon, CenturyLink, Level 3 Communications, Comcast, Inteliquent, West Communications, Windstream, Earthlink, Peerless, Irsitel, Bandwidth.

**International:** AT&T, Verizon, CenturyLink, Level 3 Communications, Comcast, Inteliquent, Tata Communications, British Telecom, Telefonica, IDT.

## Product Suite

### VoIP Services

Telnyx provides VoIP solutions for businesses, supporting advanced features such as call routing, IVR (Interactive Voice Response), and number masking. The platform is suited to call centers, customer support, and unified communications deployments, with global coverage and carrier-grade reliability. Voice quality and resiliency are actively monitored and optimized across global PoPs.

### SMS and MMS Messaging

A programmable messaging API supports both SMS and MMS for customer engagement, marketing, two-factor authentication (2FA), and service automation. The platform integrates with CRMs, websites, and mobile apps, and supports high-throughput global delivery.

### Number Provisioning and Porting

Telnyx offers a self-service platform for provisioning, managing, and porting phone numbers in real time. Local, toll-free, and international numbers are available across 100+ countries, with streamlined porting designed to minimize downtime.

### Real-Time Communications and WebRTC

WebRTC SDKs allow developers to embed secure, high-quality voice and video calls directly into web and mobile applications. Common use cases include telemedicine, e-learning, and customer support.

### Global Network and Connectivity

Telnyx operates a fully meshed private IP network that serves as a global backbone for optimized traffic. The infrastructure reduces latency, improves uptime, and provides high-performance connectivity for voice, messaging, and data. Telnyx has expanded its private network with additional PoPs and enhanced Direct Routing services for Microsoft Teams and Operator Connect.

### Elastic SIP Trunking

Elastic SIP Trunking offers pay-as-you-go SIP trunking with no minimum commitments. Channels can be added or removed dynamically, with high-availability, multi-region redundancy, and enhanced voice clarity. Recent additions include advanced redundancy, failover mechanisms, and configurable call failover policies.

### Security and Compliance

Telnyx offers end-to-end encryption, secure APIs, and advanced access controls. The platform supports STIR/SHAKEN protocols to combat robocalls and call spoofing, and provides enhanced DDoS protection.

### Inference (AI and Machine Learning)

Telnyx Inference adds machine learning capabilities to communication workflows, including speech recognition, natural language processing (NLP), and ML model integration. Key features include:

- **Speech-to-text** for real-time transcription and automation.
- **Text-to-speech** for dynamic voice response generation.
- **Sentiment analysis** to detect customer sentiment during interactions.
- **Language detection** to recognize and route based on conversation language.

A typical use case is a call center automatically transcribing calls, detecting intent, and triggering real-time actions.

### Storage

Telnyx Storage provides cloud-based media storage for voice recordings, video, and SMS/MMS attachments. Key features include:

- **Secure cloud storage** for call recordings, voicemails, and message attachments.
- **Accessible APIs** for retrieval and management.
- **Compliance and audit readiness** with regulations such as GDPR and HIPAA.
- **Data encryption** for security and privacy.

### Flow (Workflow Automation)

Telnyx Flow is a visual builder for creating automated communication workflows without extensive coding. It supports drag-and-drop design, multi-channel integration (voice, SMS, MMS, email), API integration with third-party systems, event-driven triggers, and custom notifications.

## Hardware Compatibility

Telnyx is a cloud-based platform and does not provide hardware. The service is compatible with almost any SIP-enabled device or platform. As long as hardware supports SIP and uses the audio codecs G.729, G.711, or Opus, it will work with Telnyx. Call forwarding to outside numbers on existing networks is also supported for additional customizability.

### Interoperable Platforms

Telnyx maintains configuration guides for a wide range of platforms, including:

- 3CX
- Adtran
- AudioCodes
- Asterisk
- Avaya
- Broadsoft
- Cisco CallManager
- Counterpath
- Edgewater Networks
- Elastix
- Fonality
- FreePBX
- FreeSWITCH
- Grandstream
- IAUG (International Avaya Users Group)
- Mitel
- Patton
- PBX in a Flash
- Switchvox
- Thirdlane
- Vicidial
- Yealink
- Zoiper

## Encryption

By default, Telnyx does not encrypt calls. If your device supports TLS (Transport Layer Security) for signaling and SRTP for media, you can enable these settings on your connection for end-to-end encryption. Telnyx also leverages its private network to carry media across its own fiber, minimizing exposure to public hops.

- **Outbound calls:** Configure your device to use TLS and SRTP; no further configuration is required on the Telnyx portal.
- **Inbound calls:** Enable TLS and SRTP in the [Connections page](https://portal.telnyx.com/#/voice/connections) under Voice → SIP Trunking → Connection settings.

## STUN and TURN Servers

Telnyx provides STUN and TURN servers to help devices traverse NAT for reliable VoIP communications.

- **STUN server:** `stun.telnyx.com:3478`
- **TURN server:** `turn.telnyx.com:3478` (username and password available from Telnyx support)

## Reseller Program

Telnyx supports resellers through the Mission Control platform, which is designed for multi-tenant environments. Resellers can segregate traffic, implement tagging for organization, and pull reports in real time. All Mission Control functionality is built on Telnyx's public API, allowing customers to implement ordering and provisioning of services within their own platforms.
