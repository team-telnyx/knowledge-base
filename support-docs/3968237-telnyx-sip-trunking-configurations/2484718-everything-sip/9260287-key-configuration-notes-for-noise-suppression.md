---
source_url: https://support.telnyx.com/en/articles/9260287-key-configuration-notes-for-noise-suppression
scraped: 2026-06-11
---

Key Configuration Notes for Noise Suppression | Telnyx Help Center

[Skip to main content](#main-content)

# Key Configuration Notes for Noise Suppression

Learn how to implement and manage Noise Suppression with a guide on key configuration options.

Written by Telnyx Engineering

May 5, 2026

Table of contents

Noise Suppression cleans up audio on your Telnyx voice traffic by removing background noise, isolating the primary speaker, or both.

The result is clearer audio for human listeners, more accurate speech-to-text transcription, and better Voice AI Agent performance.

This article covers how to configure the feature, what each direction setting does, and how to choose the right model for your use case.  
​

## **Application Scope**

Setting Noise Suppression at the connection level affects all numbers associated with that connection and overrides any configuration set on individual numbers. This is the recommended approach for centralized management and consistent audio quality across all calls on a trunk.

You can apply noise suppression to specific call directions — inbound, outbound, or both. **Charges apply per direction**, so selecting "both" incurs charges for each direction separately. See the [Voice API pricing page](https://telnyx.com/pricing/voice-api) for current rates.

---

## How to configure

## At the Connection level (recommended)

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Navigate to **Voice → SIP Trunking**.
3. Select the SIP connection you want to configure.
4. Open the **Configuration** tab and scroll to the **Advanced** section.
5. In the **Noise Suppression** subsection, choose a model and a direction.
6. Click **Save**.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329617740/37a42073a462bc78d73fbb870cb5/Screenshot+2026-04-28+at+3_45_42%E2%80%AFPM.png?expires=1781168400&signature=250a26705ecdcd05d29728f163bb02815bd43948d974e632322e0eeabe3d62f0&req=diMlH89%2FmoZbWfMW1HO4zTeXmrMLhxvPVnskYcRh3nFPXgHjwxk8fDSfk%2FH5%0A%2FjdeRIRL%2BtU2rEqL3xk%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2329617740/37a42073a462bc78d73fbb870cb5/Screenshot+2026-04-28+at+3_45_42%E2%80%AFPM.png?expires=1781168400&signature=250a26705ecdcd05d29728f163bb02815bd43948d974e632322e0eeabe3d62f0&req=diMlH89%2FmoZbWfMW1HO4zTeXmrMLhxvPVnskYcRh3nFPXgHjwxk8fDSfk%2FH5%0A%2FjdeRIRL%2BtU2rEqL3xk%3D%0A)

## Via API

You can also configure noise suppression programmatically. Use the `noise_suppression` parameter in connection or number configuration requests, or call `suppression_start` on an active call and pass a `noise_suppression_engine` value with your chosen model. See the [Noise Suppression developer documentation](https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression) for details.

## Direction options

|  |  |
| --- | --- |
| Setting | What it does |
| **Inbound only** | Applies noise reduction to audio entering the Telnyx network and destined for the customer. Cleans up audio you receive. |
| **Outbound only** | Applies noise reduction to audio leaving the Telnyx network from the customer. Cleans up audio you send. |
| **Both** | Applies noise reduction in both directions. Highest impact on call clarity, but billed per direction. |
| **Disabled** | Turns the feature off. Audio passes through unprocessed. |

## Choosing a model

Telnyx supports five noise suppression engines. Each is tuned for a different point in the audio pipeline, so the right choice depends on what's downstream — a human listener, an STT engine, or a voice AI agent — and where the speaker sits relative to the microphone.

## Quick guide

|  |  |
| --- | --- |
| Use case | Recommended model |
| General-purpose, lightweight default | Denoiser |
| Standard SIP / telephony, contact centers | Krisp Viva Tel Lite |
| WebRTC and browser-based calls | Krisp Viva Pro |
| Smart speakers, conference rooms, far-field mics | Krisp Viva SS |
| Human listening with reverb / room acoustics | AIcoustics Rook Small |
| Human listening in demanding acoustic conditions | AIcoustics Rook Large |
| Voice AI Agents and STT pipelines | AIcoustics Quail Voice Focus S |

## Model details

## Denoiser

A lightweight, general-purpose noise suppression model, not specialized for any particular use case.

**Use when:** basic noise reduction, non-critical audio paths.

## Krisp Viva Tel Lite

Designed for standard SIP trunk and Call Control voice calls. The right choice for the vast majority of human-to-human voice calls, handles typical agent-environment noise like keyboard clicks, HVAC, and nearby conversations.

**Use when:** standard VoIP calls, IVR systems, contact centers.

## Krisp Viva Pro

Optimized for WebRTC and browser-based calls where you need to isolate a single primary speaker from competing voices. Handles multi-talk scenarios and echo well.

**Use when:** browser-based softphones, video calls, scenarios with multiple nearby speakers.

## Krisp Viva SS

Built for smart-speaker and far-field microphone setups where the speaker is at a distance from the mic. Handles ambient noise differently than close-talk models, tuned to pick up speech from across the room while suppressing environmental noise.

**Use when:** smart speakers, conference-room hardware, and far-field microphones.

## AIcoustics Rook Small

The go-to model for AI assistant calls. Handles both noise suppression and reverberation removal, which is critical for AI voice where echo and room effects degrade LLM understanding.

**Use when:** Telnyx AI Assistants, conversational AI, agent-handoff flows.

## AIcoustics Rook Large

Same architecture as AIcoustics Rook Small but scaled up for tough acoustic environments, high reverb rooms, heavy background noise, or when you need maximum quality.

**Use when:** demanding acoustic conditions, high-value AI calls where quality is critical.

## AIcoustics Quail Voice Focus S

Purpose-built for machine consumers, STT pipelines and Voice AI agents. Preserves the phonetic structure that transcription engines and voice agents depend on while suppressing competing voices and background noise. Optimized for close-microphone input. Audio may sound different to a human listener, that's by design.

**Use when:** Telnyx Voice AI Assistants, conversational AI, transcription pipelines, voice analytics, close-mic setups.

## Related articles

* [Telnyx SIP Trunking Configurations](https://support.telnyx.com/en/collections/3968237-telnyx-sip-trunking-configurations)
* [Voice API: Noise Suppression](https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression)

---

Related Articles

[Configuring a Cisco CUBE/CUCM IP Trunk](https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk)[Configuring a Cisco CME Credentials Trunk](https://support.telnyx.com/en/articles/1130668-configuring-a-cisco-cme-credentials-trunk)[Fanvil A32i: Telnyx Setup](https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup)[Fanvil H3: Hotel IP](https://support.telnyx.com/en/articles/6202965-fanvil-h3-hotel-ip)[How to configure Yeastar P-series](https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series)

Did this answer your question?

😞😐😃

Table of contents
