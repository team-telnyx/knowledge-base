---
title: Telnyx Platform Overview
summary: Telnyx is a Communications Platform as a Service (CPaaS) provider founded
  in 2009 and based in Austin, Texas, offering voice, messaging, networking, AI inference,
  storage, and workflow automation through a globally distributed private IP network
  and robust APIs.
sources:
- url: https://support.telnyx.com/en/articles/1130637-what-is-telnyx
- url: https://support.telnyx.com/en/articles/1130638-does-telnyx-provide-any-hardware
- url: https://support.telnyx.com/en/articles/1130641-telnyx-recommended-hardware-configurations
- url: https://support.telnyx.com/en/articles/1130646-where-is-telnyx-located
- url: https://support.telnyx.com/en/articles/1130664-countries-that-telnyx-offers-termination-in
- url: https://support.telnyx.com/en/articles/1130667-do-you-offer-service-to-call-centers
- url: https://support.telnyx.com/en/articles/1130675-what-kind-of-equipment-do-you-use
- url: https://support.telnyx.com/en/articles/1130692-does-telnyx-have-a-blog
- url: https://support.telnyx.com/en/articles/1130710-what-is-dtmf-and-how-to-configure-it-on-telnyx
- url: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
- url: https://support.telnyx.com/en/articles/1130713-what-is-my-sip-account-connection-password
- url: https://support.telnyx.com/en/articles/1130723-voip-telecommunications-protocols
- url: https://support.telnyx.com/en/articles/1424680-international-coverage
- url: https://support.telnyx.com/en/articles/3610162-prevent-telnyx-account-fraud
- url: https://support.telnyx.com/en/articles/4283783-feature-requests
- url: https://support.telnyx.com/en/articles/4283906-bug-reports-guide
- url: https://support.telnyx.com/en/articles/4400326-south-africa-number-porting
- url: https://support.telnyx.com/en/articles/4567969-united-states-n11-codes
- url: https://support.telnyx.com/en/articles/5721953-linksys-dialplan-for-linksys-atas
- url: https://support.telnyx.com/en/articles/5724344-cisco-linksys-star-codes
- url: https://support.telnyx.com/en/articles/5941652-google-verified-calls-faq
- url: https://support.telnyx.com/en/articles/6228388-aca-feedback-process
- url: https://support.telnyx.com/en/articles/7020727-account-compromise-what-to-do
- url: https://support.telnyx.com/en/articles/7205411-numbering-team-best-practices
- url: https://support.telnyx.com/en/articles/7915224-blocked-account-guidelines
- url: https://support.telnyx.com/en/articles/8020222-mission-control-portal-ai-chat-support-assistant
- url: https://support.telnyx.com/en/articles/8428806-channel-billing
- url: https://support.telnyx.com/en/collections/5782829-webrtc-voice-sdk
updated_at: 2026-06-11T11:45:24Z
---

# Telnyx Platform Overview

*Part 2 of 3 — see also: [Part 1](telnyx-platform-overview--part-1.md), [Part 3](telnyx-platform-overview--part-3.md)*

Telnyx is a Communications Platform as a Service (CPaaS) provider founded in 2009 and based in Austin, Texas, offering voice, messaging, networking, AI inference, storage, and workflow automation through a globally distributed private IP network and robust APIs.

## Voice Protocols and Configuration

### VoIP Protocols

Telnyx voice services rely on several key protocols:

- **RTP (Real Time Transport Protocol):** Delivers audio and video over IP networks, typically over UDP. RTP carries the media stream and works alongside SIP.
- **UDP (User Datagram Protocol):** The favored transport for RTP, prioritizing real-time delivery over reliability.
- **TCP (Transmission Control Protocol):** Can also carry RTP but favors reliability over reduced latency.
- **SIP (Session Initiation Protocol):** Establishes and manages communication sessions.
- **SDP (Session Description Protocol):** Negotiates ports, IP addresses, and payload formats (including codecs) within SIP signaling.

RTP typically uses UDP ports between 1024–65535, negotiated via SIP and SDP. Supported audio payload formats include G.711U, G.711A, G.7229, and OPUS.

### DTMF Configuration

DTMF (Dual-Tone Multi-Frequency) transmits keypad inputs over phone systems using paired audio frequencies. Telnyx supports three DTMF methods over VoIP:

| Method | Best For | Notes |
|---|---|---|
| **RFC 2833** (recommended default) | Most deployments; compressed codecs (G.729, Opus) | Codec-agnostic; widely supported; sent as special RTP packets |
| **Inband** | Legacy analog devices/ATAs | Tones sent within audio stream; degraded by compressed codecs |
| **SIP INFO** | When far end requires it | Sent as SIP signaling messages; immune to codec issues; possible timing inconsistencies |

To configure DTMF in the portal: navigate to **Real Time Communications → Voice → SIP Trunking**, edit the connection, open the **Configuration** tab, select the DTMF type, and save.

### SIP Connection Credentials

When creating a SIP connection with credentials authentication, Telnyx generates a random username and password that you can change. To find or update credentials: navigate to **Voice → SIP Trunking**, edit the connection, and open the **Authentication and routing** tab. Using a random password generator is recommended for additional security.

### Device Dial Plans and Star Codes

For Linksys ATAs, a dial plan string determines how entered digits are interpreted and transmitted. Key digit sequences include `x` (any digit), `[sequence]` (allow-list), `.` (zero or more repeats), `<dialed:substituted>` (substitution), `,` (outside line dial tone), `!` (prohibit), and timer overrides (`S0`, `L0`).

Cisco/Linksys star codes provide quick feature access, including:

- `*69` — Call Return
- `*72` / `*73` — Call Forwarding All Activate / Deactivate
- `*78` / `*79` — Do Not Disturb Activate / Deactivate
- `*67` / `*68` — Block Caller ID Activate / Deactivate
- `*98` — Blind Transfer
- `*66` / `*86` — Call Back Activate / Deactivate
- `*77` / `*87` — Block Anonymous Calls Activate / Deactivate

## Channel Billing

Channel Billing allows customers to pay a flat per-channel fee for unlimited inbound minutes instead of per-minute billing. Each channel supports one concurrent inbound call. Channels are managed at the number level by setting the Voice Billing Method to "Channel" in the number's Voice tab.

Channels are pooled within geographic zones—multiple numbers in the same zone share the total reserved channels. If all channels are in use, new inbound calls are rejected with a "User Busy" hangup cause.

Pricing is tiered (per channel per month, decreasing with volume):

| Zone | 0–10 Ch. | 10–50 Ch. | 50–250 Ch. | 250+ Ch. |
|---|---|---|---|---|
| **US** | $12 | $11 | $9 | $8 |
| **Zone A** (Europe+) | $15 | $14 | $12 | $10 |
| **Zone B** (AU, CA, BR, MX+) | $20 | $19 | $15 | $14 |
| **Zone C** (IL, JP, NZ, SI) | $25 | $23 | $19 | $17 |

Zone A includes countries such as the UK, Germany, France, Spain, Italy, Netherlands, and most of Europe. Zone B includes Australia, Canada, Brazil, Mexico, Singapore, South Africa, and others. Zone C covers Israel, Japan, New Zealand, and Slovenia.

## Security and Encryption

### Encryption

By default, Telnyx does not encrypt calls. End-to-end encryption can be enabled using TLS (Transport Layer Security) for signaling and SRTP (Secure RTP) for media. For outbound calls, configure your device to use TLS and SRTP. For inbound calls, enable TLS and SRTP in the connection settings under **Voice → SIP Trunking** in the portal. Additionally, Telnyx's private network carries media across its own fiber, minimizing exposure to public hops.

### STIR/SHAKEN and Anti-Fraud

Telnyx supports STIR/SHAKEN protocols to combat robocalls and call spoofing, and provides enhanced DDoS protection. The platform includes anti-fraud and anti-spam systems to protect customers and the global community.

### Fraud Prevention Best Practices

To prevent fraud on your account:

- **Secure passwords:** Update account passwords regularly (every 30–90 days).
- **Rotate API keys:** Delete old keys and generate new ones periodically.
- **Update SIP credentials:** Change credential-based connection passwords regularly (can be automated via API).
- **Set channel limits:** Apply inbound and outbound channel limits on connections and outbound profiles.
- **Configure outbound profiles:** Set max daily spend limits, max destination rate limits, country blacklists, and concurrent call limits.
- **Enable notifications:** Configure alerts for suspicious outbound voice traffic (e.g., multiple calls to the same high-cost destination, long-lived concurrent calls).
- **Enable 2FA:** Two-factor authentication is available at [portal.telnyx.com](https://portal.telnyx.com/#/account/my-account/security).
- **Use Tech Prefix:** Segment traffic on shared IP addresses.
- **Restrict PBX/VoIP web access** and review access logs regularly.

### Account Compromise Response

If your account is compromised, take these steps immediately:

1. Change the login password for the compromised user.
2. Change credentials for all credential-based SIP connections and update your phone system.
3. Check IP authentication connections for unauthorized IPs.
4. Regenerate messaging profile secrets (v1 API).
5. Delete all active API keys and generate new ones.
6. Check call forwarding on all numbers for unauthorized forwarding.
7. Review Programmable Voice API and TeXML applications for unauthorized configurations.

Enabling 2FA is the single most effective preventive measure.

### Blocked Account Guidelines

If your account is blocked by Telnyx's anti-fraud systems:

- Contact [support@telnyx.com](mailto:support@telnyx.com) for a manual case review.
- Cooperate with the review process and address any identified issues.
- If permanently blocked, you may request temporary access to port numbers away (waived port-out fee) via [porting@telnyx.com](mailto:porting@telnyx.com).
- Refund requests for unused funds can be sent to [billing@telnyx.com](mailto:billing@telnyx.com).
- Feedback on the blocking process can be sent to [community@telnyx.com](mailto:community@telnyx.com).

Report abuse of Telnyx numbers via [telnyx.com/report-abuse](https://telnyx.com/report-abuse), [abuse@telnyx.com](mailto:abuse@telnyx.com), or the chat widget.

## Emergency Services and N11 Codes

In the United States, N11 codes provide three-digit dialing access to special services. Telnyx supports the following for outbound dialing:

| N11 Code | Description | Supported |
|---|---|---|
| 711 | Telecommunications Relay Service (TRS) | Yes |
| 811 | One Call Services (pipeline/utility protection) | Yes |
| 911 | Emergency | Yes |
| 988 | National Suicide Prevention Lifeline (call and text) | Yes |

For 911 calls, using an invalid Caller ID or one without an emergency address results in a $100 per call unregistered call charge. Ensure you send valid Caller IDs from numbers with emergency services enabled.
