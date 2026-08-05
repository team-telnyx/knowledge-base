---
title: Telnyx Voice, Fax, and STIR/SHAKEN Configuration Reference
summary: A consolidated reference covering Cisco SPA112/122 ATA setup with Telnyx,
  fax service configuration via T.38 or G711, Fax API error codes, STUN/TURN server
  usage, STIR/SHAKEN attestation and verstat parameters, the Robocall Mitigation Database,
  and Noise Suppression configuration for SIP trunks.
sources:
- url: https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
- url: https://support.telnyx.com/en/articles/1130682-telnyx-stun-and-turn-server
- url: https://support.telnyx.com/en/articles/4967498-fax-api-error-list
- url: https://support.telnyx.com/en/articles/5402969-stir-shaken-with-telnyx
- url: https://support.telnyx.com/en/articles/5544430-robocall-mitigation-database
- url: https://support.telnyx.com/en/articles/5761463-canadian-stir-shaken-implementation-faqs
- url: https://support.telnyx.com/en/articles/7421223-shaken-stir-parameters
- url: https://support.telnyx.com/en/articles/9260287-key-configuration-notes-for-noise-suppression
- url: https://support.telnyx.com/en/collections/3968239-telnyx-fax-configuration-errors
updated_at: 2026-08-05T13:30:57Z
---

# Telnyx Voice, Fax, and STIR/SHAKEN Configuration Reference

*Part 3 of 3 — see also: [Part 1](telnyx-voice-fax-and-stir-shaken-configuration-reference--part-1.md), [Part 2](telnyx-voice-fax-and-stir-shaken-configuration-reference--part-2.md)*

A consolidated reference covering Cisco SPA112/122 ATA setup with Telnyx, fax service configuration via T.38 or G711, Fax API error codes, STUN/TURN server usage, STIR/SHAKEN attestation and verstat parameters, the Robocall Mitigation Database, and Noise Suppression configuration for SIP trunks.

## Robocall Mitigation Database

Effective September 28, 2021, the FCC prohibits intermediate providers and voice service providers from accepting traffic directly from voice service providers not listed in the Robocall Mitigation Database (RMD). Per FCC 24-73 and FCC 23-18, all carriers (including Telnyx) must block incoming calls using US Calling Line Identity (CLI) from unregistered providers, including US and foreign providers using North American Numbering Plan resources. Foreign providers were temporarily exempted but were brought into scope starting April 11, 2023.

A voice service provider is defined under 47 C.F.R. 64.1600(r)(1) as any service interconnected with the PSTN that furnishes voice communications to an end user using NANP resources.

### Registration Requirements

Before filing, obtain a Commission Registration System (CORES) account and an FCC Registration Number (FRN) at <https://apps.fcc.gov/cores/userLogin.do>.

Filings must include:

- Business name, contact information, FRN, and ownership information.
- Filing type (voice service provider, gateway provider, or non-gateway intermediate provider; select all that apply).
- US or foreign service provider status.
- Certification of full, partial, or no STIR/SHAKEN implementation.
- A robocall mitigation plan describing the "reasonable steps" taken to avoid illegal robocall traffic, per FCC 24-73.

Telnyx is registered with the RMD and is fully SHAKEN/STIR compliant. Customers should consult legal counsel to determine whether they must register.

## Noise Suppression Configuration

Noise Suppression cleans up audio on Telnyx voice traffic by removing background noise, isolating the primary speaker, or both. The result is clearer audio for human listeners, more accurate speech-to-text transcription, and better Voice AI Agent performance.

### Application Scope

Setting Noise Suppression at the connection level affects all numbers on that connection and overrides any per-number configuration. This is the recommended approach for centralized management. Noise Suppression can be applied to inbound, outbound, or both directions; charges apply per direction. See the [Voice API pricing page](https://telnyx.com/pricing/voice-api) for current rates.

### Configuration at the Connection Level

1. Log in to the [Mission Control Portal](https://portal.telnyx.com).
2. Navigate to **Voice → SIP Trunking**.
3. Select the SIP connection to configure.
4. Open the **Configuration** tab and scroll to the **Advanced** section.
5. In the **Noise Suppression** subsection, choose a model and a direction.
6. Click **Save**.

![](_images/2db4c856cae0cf2c.png)

### Configuration via API

Use the `noise_suppression` parameter in connection or number configuration requests, or call `suppression_start` on an active call and pass a `noise_suppression_engine` value with the chosen model. See the [Noise Suppression developer documentation](https://developers.telnyx.com/docs/voice/programmable-voice/noise-suppression) for details.

### Direction Options

| Setting | Behavior |
| --- | --- |
| Inbound only | Reduces noise on audio entering the Telnyx network destined for the customer. |
| Outbound only | Reduces noise on audio leaving the Telnyx network from the customer. |
| Both | Reduces noise in both directions; billed per direction. |
| Disabled | Audio passes through unprocessed. |

### Model Selection

| Use case | Recommended model |
| --- | --- |
| General-purpose, lightweight default | Denoiser |
| Standard SIP / telephony, contact centers | Krisp Viva Tel Lite |
| WebRTC and browser-based calls | Krisp Viva Pro |
| Smart speakers, conference rooms, far-field mics | Krisp Viva SS |
| Human listening with reverb / room acoustics | AIcoustics Rook Small |
| Human listening in demanding acoustic conditions | AIcoustics Rook Large |
| Voice AI Agents and STT pipelines | AIcoustics Quail Voice Focus S |

- **Denoiser:** Lightweight, general-purpose; for basic noise reduction on non-critical audio paths.
- **Krisp Viva Tel Lite:** Designed for standard SIP trunk and Call Control voice calls; handles agent-environment noise like keyboard clicks, HVAC, and nearby conversations.
- **Krisp Viva Pro:** Optimized for WebRTC and browser-based calls; isolates a single primary speaker from competing voices and handles multi-talk and echo.
- **Krisp Viva SS:** Built for smart speakers and far-field microphones; tuned to pick up speech from across the room while suppressing environmental noise.
- **AIcoustics Rook Small:** Handles noise suppression and reverberation removal for AI assistant calls; critical for AI voice where echo and room effects degrade LLM understanding.
- **AIcoustics Rook Large:** Same architecture as Rook Small, scaled for tough acoustic environments, high reverb, heavy background noise, or maximum quality.
- **AIcoustics Quail Voice Focus S:** Purpose-built for machine consumers, STT pipelines, and Voice AI agents; preserves phonetic structure for transcription while suppressing competing voices and background noise. Optimized for close-microphone input; audio may sound different to a human listener by design.

## Related Telnyx Resources

- [Configuring your Cisco SPA112/122 ATA](configuring-your-cisco-spa112-122-ata.md)
- [Fax service with Telnyx (via T.38 or G711)](fax-service-with-telnyx-via-t-38-or-g711.md)
- [Fax API - Error List](fax-api-error-list.md)
- [Telnyx STUN and TURN server](telnyx-stun-and-turn-server.md)
- [STIR/SHAKEN With Telnyx](stir-shaken-with-telnyx.md)
- [Robocall Mitigation Database](robocall-mitigation-database.md)
- [Canadian STIR/SHAKEN Implementation FAQs](canadian-stir-shaken-implementation-faqs.md)
- [SHAKEN/STIR Parameters](shaken-stir-parameters.md)
- [Key Configuration Notes for Noise Suppression](key-configuration-notes-for-noise-suppression.md)
- [Telnyx Fax Configuration & Errors](telnyx-fax-configuration-errors.md)
