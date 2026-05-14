---
title: Telnyx Overview and Getting Started
summary: A concise guide to Telnyx—what it is, where it operates, how to get started
  in the Mission Control Portal, organize users and permissions, understand hardware
  compatibility and network specs, and where to find support and learning resources.
sources:
- url: https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account
  content_hash: ac1e6c38877141946be63f16593c8425ddc842d746380449f3db447a69982bd6
- url: https://support.telnyx.com/en/articles/1189141-get-started-with-organizations
  content_hash: ea43533849f06879872e23189dd1ab669f66549d900b3ad9d726461294513c8e
- url: https://support.telnyx.com/en/articles/1130637-what-is-telnyx
  content_hash: 1f313eb1a175e433fac0f7311de85bcd341a462c4a1bdc11c0f4e6ed1f35cc4f
- url: https://support.telnyx.com/en/articles/1130644-do-i-have-to-sign-a-contract
  content_hash: 558d0efd555ab8cf962ec1be40aa2939ceddc1f594bd6b08161eca7c5553af02
- url: https://support.telnyx.com/en/articles/1130638-does-telnyx-provide-any-hardware
  content_hash: 4152b7c3911e94276e65492be82a098a127da57789861097003ac30b58b4980c
- url: https://support.telnyx.com/en/articles/1130641-telnyx-recommended-hardware-configurations
  content_hash: bf7fd8f33557ad98ccc94e1aa81cd16197eaa2b8f369268639918b62203691fe
- url: https://support.telnyx.com/en/articles/1130692-does-telnyx-have-a-blog
  content_hash: 02ceb4f56650324c00578163a4c3fab75afbbef81b862d714d739698682ec262
- url: https://support.telnyx.com/en/articles/1130646-where-is-telnyx-located
  content_hash: 41c0ec2263ae243c9491da73123b8d2729176b298a82edc230deee7a65e587d3
- url: https://support.telnyx.com/en/articles/1130675-what-kind-of-equipment-do-you-use
  content_hash: d3d504fc296fc142bc9086862e27e925e07f7630a4ae4406c521ddb98607297a
- url: https://support.telnyx.com/en/articles/1130599-telnyx-tech-specs
  content_hash: b01bf96020026f0d41b2b7bab2bc6a64051e93b6bbb58e52783bdd43d985f8ac
updated_at: 2026-05-14T11:40:05Z
---

# Telnyx Overview and Getting Started

A concise guide to Telnyx—what it is, where it operates, how to get started in the Mission Control Portal, organize users and permissions, understand hardware compatibility and network specs, and where to find support and learning resources.

## What Telnyx Offers
Telnyx is a CPaaS provider delivering programmable voice, messaging, number services, WebRTC, and connectivity over a privately owned, globally distributed IP network. Key offerings include:

- Elastic SIP trunking with multi-region redundancy and configurable failover
- SMS/MMS messaging APIs for engagement, 2FA, and automation
- Real-time communications (including WebRTC SDKs)
- Number search, instant provisioning (local, toll-free, international), and streamlined porting
- AI/ML services via Inference (speech-to-text, text-to-speech, sentiment, language detection)
- Cloud media Storage integrated with voice and messaging workflows
- Flow visual builder for automated, multi-channel communication workflows
- Security and compliance features including end-to-end encryption, STIR/SHAKEN, and enhanced DDoS protections

## Company Locations
Founded in 2009, Telnyx is based in Austin, Texas, with offices in Denver, Dublin, and Amsterdam.

Address:
600 Congress Avenue
14th Floor
Austin, TX 78701

## Accounts, Pricing, and Support
- No contracts required—create a free account and pay as you go.
- Support options:
  - 24/7 AI Assistant: https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant
  - 24/7 NOC best practices: https://support.telnyx.com/en/articles/5170721-best-practices-for-contacting-support
  - Porting: 9am–7pm CT, Mon–Fri: https://support.telnyx.com/en/articles/5820338-best-practices-for-contacting-porting
  - Numbering: 9am–5pm CT, Mon–Fri: https://support.telnyx.com/en/articles/7205411-numbering-team-best-practices

## Mission Control Portal: Setup Checklist
Get your Mission Control account ready for calls and messaging:

1) Level 1 Verification
- Required to assign connections and messaging/outbound profiles.
- Portal: https://portal.telnyx.com/#/app/account/verifications
- Guide: https://support.telnyx.com/en/articles/1130595-account-verification

2) Connection Setup
- Create a SIP Connection to authenticate with sip.telnyx.com using one method: Credentials, IP Address, or FQDN.
- Portal: https://portal.telnyx.com/#/app/connections
- Auth types: https://support.telnyx.com/en/articles/4245868-sip-connection-types

3) DIDs (Inbound Calling)
- Purchase numbers and assign them to a connection to receive calls.
- My Numbers: https://portal.telnyx.com/#/app/numbers/my-numbers
- Search/Buy: https://support.telnyx.com/en/articles/4380325-search-and-buy-numbers
- Assign to connection: https://support.telnyx.com/en/articles/1177115-how-to-setup-a-did-to-sip-connection

4) Outbound Voice Profile (Outbound Calling)
- Required to place outbound calls; assign your connection to an outbound profile.
- Portal: https://portal.telnyx.com/#/app/outbound
- About profiles: https://support.telnyx.com/en/articles/4320411-more-about-outbound-voice-profiles

5) Payments
- Add a payment method and top up to purchase numbers, send messages, and make/receive calls.
- Portal: https://portal.telnyx.com/#/app/billing/payment
- Billing setup: https://support.telnyx.com/en/articles/4280500-billing-setup-billing-groups

Additional network specs (signaling/media IPs) are published at https://sip.telnyx.com/.

## Organizations: Structure, Invitations, and Permissions
- Organizations let multiple user accounts operate under one owner with group-based permissions and a single balance/payment method. For reseller-like needs, use Managed Accounts instead: https://support.telnyx.com/en/articles/4951492-managed-accounts
- Create an organization after Level 1 verification: https://portal.telnyx.com/#/app/advanced-features/organizations

Invitations
- Invite by email; the invitee must not already have a Telnyx account.
- Limits: up to 10 invites/hour (including deleted/revoked), max 10 open invites at once, resend up to 5 times at ≥5-minute intervals.
- Invites can be revoked; a revoked invitee can still sign up as an independent account.

Groups & Permissions
- Assign sub-members to groups that define their permissions (create, read, update, delete).
- Available categories include: Account Management, Connection Management, Numbers, Outbound, Reporting, Number Porting, Managed Accounts, Networking (VXC), Messaging, Organization Management, Wireless, Access Control Lists, and Call Recording.
- Technical model: users get the most permissive net result across all groups. Initially, only category-level permissions are available; entity-level will follow.

Limitations and Special Notes
- Sub-accounts don’t “own” resources (numbers, connections, outbound profiles) and can’t have separate payment methods; actions are on behalf of the owner.
- Certain sections may show limited/undesired portal results during a V2 migration; when needed, use the organization owner’s API key.
- Sub-members cannot access Verification or SSO pages.
- One organization per account; max 10 open invites. To add an existing Telnyx user, they must request account cancellation to free the email, then be invited.

## Hardware Compatibility and Recommended Configurations
- Telnyx does not sell hardware. Any SIP-capable device or platform generally works.
- Recommended audio codecs: G.729, G.711, and Opus.
- Interoperability guides for popular platforms (e.g., 3CX, Asterisk, FreePBX, Cisco, Avaya, Grandstream, Yealink, Zoiper, etc.): https://support.telnyx.com/en/collections/133118-configuration-guides
- Call forwarding to external numbers is supported for added flexibility.

## Network, Equipment, and Technical Specs
- Global PoPs with authoritative specs at:
  - https://sip.telnyx.com/
  - https://sip.telnyx.ca/
  - https://sip.telnyx.eu/
  - https://sip.telnyx.com.au/
- Core equipment: Cisco ASR (core/edge), Juniper QFX5100 (aggregation), Brocade Vyatta with virtualized routing for Cloud CE.
- Carrier partners (selection):
  - North America: AT&T, Verizon, CenturyLink, Level 3, Comcast, Inteliquent, West, Windstream, Earthlink, Peerless, Irsitel, Bandwidth
  - International: AT&T, Verizon, CenturyLink, Level 3, Comcast, Inteliquent, Tata, BT, Telefonica, IDT
- Learn more about the network: https://telnyx.com/our-network

## Numbering, Provisioning, and Porting
- Self-service number provisioning across 100+ countries; streamlined porting to minimize downtime.
- To transfer numbers/configurations between accounts: submit a port-in on the destination account and recreate configurations during a maintenance window. SIP Connections are unique—use distinct authentication on the new account or remove the old connection before recreating.

## Security and Compliance
- End-to-end encryption, secure APIs, granular access controls.
- STIR/SHAKEN support to combat spoofing; enhanced DDoS protections.

## Resources: Blog, Community, and Learning
- Blog and resources (subscribe by email): https://telnyx.com/resources
- Community forum available via the Mission Control Portal
- Interested in contributing content? Email andrewm@telnyx.com
