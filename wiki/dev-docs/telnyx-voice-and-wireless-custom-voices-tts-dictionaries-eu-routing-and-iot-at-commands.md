---
title: 'Telnyx Voice and Wireless: Custom Voices, TTS Dictionaries, EU Routing, and
  IoT AT Commands'
summary: A concise guide to building and using custom voices with the Telnyx Voice
  Design Lab, managing TTS pronunciation dictionaries, optimizing Voice API usage
  in Europe, and running essential IoT SIM AT commands on Raspberry Pi cellular HATs.
sources:
- url: https://developers.telnyx.com/docs/iot-sim/at-commands/index
  content_hash: 5a67e9168384e250f9b6d80d0409144eeef803c01cca965f68e8720a41af98f9
- url: https://developers.telnyx.com/docs/voice/programmable-voice/voice-api-services-in-europe/index
  content_hash: 99e324b1534471f2546b090acd3d5d4395ee54eea801a034230a8ecca278129f
- url: https://developers.telnyx.com/docs/voice/tts/pronunciation-dictionaries/index
  content_hash: 1f242ab2cda19d8d4a8af88a813bf5f6913b109860b214a4bddcf13a5fe53247
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/concepts/index
  content_hash: 2acaa8dedb7d48f628f0069f99d895cc8ec2714fae84a658317e8407d1962b38
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/errors
  content_hash: cb3f767c69c6c55c5d95dfc43be9f981553a3542b2c69292d882193fde8c56c7
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/parameters
  content_hash: f830281f241a248c1a58078dd009c53d48efbfb4d5cdb19bab8cf6bf9910194f
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/quickstart
  content_hash: d72357abe7e838339c5d38f9af251e87abcc85dcb1769c314d3cf29a5d7f2557
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/clone-voice/responses
  content_hash: 83f961e9e984e95f098ec5514b0a3bc94c7317152e220fd8b9edcf26c5b133a3
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/api-details
  content_hash: 2808a13974ab1f9e5dd8628d3b8e6463e134df1a0d41f1ca2325485923268c01
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/concepts/index
  content_hash: 8e028d9cba6138e9cc67694d133838c577d4deb854a156fb82291f5cd60a541d
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/prompting-guide
  content_hash: d08c6b5b17591daf51fc8525f7fffa0c2db9eb40fe54f0d0ef15e2220bf48dae
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/design-voice/quickstart
  content_hash: 9565eab9f2858c4875366abe02fd2a7e0b43deeac367a3b828808a2e3e1916ab
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/index
  content_hash: b2d078054bfba95b4aee9ce724f9065fe358a6862c6040f1795131fc831896cd
- url: https://developers.telnyx.com/docs/voice/voice-design-lab/using-custom-voices/index
  content_hash: 9122e16396e0ed2238aad3df9579dda82ea73e5c4d279436aac279ab1452b37e
updated_at: 2026-05-20T10:29:04Z
---

# Telnyx Voice and Wireless: Custom Voices, TTS Dictionaries, EU Routing, and IoT AT Commands

A concise guide to building and using custom voices with the Telnyx Voice Design Lab, managing TTS pronunciation dictionaries, optimizing Voice API usage in Europe, and running essential IoT SIM AT commands on Raspberry Pi cellular HATs.

## Voice Design Lab at a glance

The Voice Design Lab lets you create production-ready voices for TTS in two ways:
- Design a Voice (from a prompt): Describe age, tone, accent, pacing; the AI generates samples. A “voice design” is a draft; save it as a clone for production use.
- Clone from Audio: Upload or record a short sample; the system learns the speaker’s timbre, cadence, and accent to synthesize new speech.

API flow:
- POST /v2/voice_designs → returns a design + sample you can preview.
- POST /v2/voice_clones → creates a usable voice from a design (or directly from audio via upload).

See also: [Voice Design Lab](voice-design-lab.md), [Design a Voice — Quickstart](design-a-voice-quickstart.md), [Clone from Audio — Quickstart](clone-from-audio-quickstart.md).

## Design a voice from a prompt

What it is: Generate a synthetic voice from a natural-language description. No source audio is required.

Prompting tips:
- Use a structured format: “<Gender>, <Age range>. <Quality/energy>. 1–2 sentences on timbre, pacing, delivery.”
- Describe dimensions: age, tone/timbre (e.g., warm, husky), pacing (measured vs rapid), emotion/energy (calm, upbeat), accent/region (be specific), and use‑case context.
- Avoid vague or contradictory traits; test the same prompt on different providers if needed.

Providers and parameters (POST /v2/voice_designs):
- provider: "telnyx" (default, Qwen3TTS) or "minimax".
- Telnyx supports generation controls; Minimax ignores them.
  - temperature (default 0.9, 0–2)
  - top_k (50, 1–1000)
  - top_p (1.0, 0–1)
  - repetition_penalty (1.05, 1–2)
  - max_new_tokens (2048, 100–4096)
- Languages: Auto, Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian.

Workflow:
1) Create a design with name, prompt, text, language, provider. 2) Preview the generated sample (GET /v2/voice_designs/{id}/sample). 3) Save as a clone (POST /v2/voice_clones) to use in TTS, Call Control, or AI Assistants.

See also: [How to Write Effective Prompts](how-to-write-effective-prompts.md).

## Clone a voice from audio

What cloning does: Learns patterns from a short sample (timbre, cadence, pronunciation) to synthesize new utterances in that voice. It is a representation, not a recording; output still passes through a TTS model.

What cloning doesn’t do: It cannot fix noisy or inconsistent recordings, and may struggle with styles far from the sample (e.g., asking an even-toned clone to shout emotionally).

Recording best practices:
- Match the delivery to your use case; the AI mirrors energy and pacing.
- Quiet room, clear speech, consistent tone; avoid long pauses and dead air.
- Target -23 to -18 dB RMS; avoid clipping; WAV ideal, MP3 ≥128 kbps is fine.
- Record in the target language.

Models and when to use them (POST /v2/voice_clones/from_upload):
- Telnyx Qwen3TTS (default): 3–15 s audio (5–10 s optimal, auto-trim to 10 s), 5 MB max, synchronous (201). Best for short, clean samples.
- Telnyx Ultra: up to 10 s, 5 MB, asynchronous (202). Higher quality, more natural; poll until active.
- Minimax speech-2.8-turbo: 10 s–5 min, 20 MB, synchronous (201). Longer recordings capture wider vocal range.

Audio and options:
- Formats: WAV, MP3, FLAC, OGG, M4A.
- Optional ref_text: transcript of the sample to improve alignment.
- Ultra async flow: POST returns 202 (pending); GET /v2/voice_clones/{id} until status=active.

Errors (highlights):
- 404 not found (clone/design), 409 duplicate provider_voice_id, 422 validation.
- Upload errors: missing audio_file, file too large (5 MB Telnyx, 20 MB Minimax), FFmpeg processing failure, invalid provider+model.
- Provider‑specific (examples): audio too short/long, poor quality/noise, unsupported format/language, rate limits (429).

See also: [Clone from Audio — Quickstart](clone-from-audio-quickstart.md), [Voice Clone API parameters](voice-clone-api-parameters.md), [Voice Clone API errors](voice-clone-api-errors.md), [Responses](responses.md).

## Voice IDs and using custom voices

Voice ID format in clone responses: {Provider}.{Model}.{provider_voice_id}
- Telnyx Qwen3TTS: provider_voice_id equals the clone UUID.
- Telnyx Ultra: Cartesia‑assigned voice ID.
- Minimax: Minimax‑assigned encoded ID.

Where to use voice IDs:
- AI Assistants: Select your clone (under Telnyx/Qwen3TTS or Minimax) in voice settings.
- Call Control: Set the speak command’s voice field to the voice ID.
- TTS WebSocket: Pass the voice ID as the voice query parameter on the connection URL.

See also: [Using Custom Voices](using-custom-voices.md).

## Pronunciation dictionaries for TTS

Purpose: Control how specific words/phrases are spoken. Dictionaries are applied before synthesis; no change to input text is required.

Item types (up to 100 items per dictionary):
- Alias (text replacement): Replace matched text before synthesis. Example: ASAP → “as soon as possible”.
- Phoneme (IPA): Specify pronunciation with IPA. Example: GIF → /ɡɪf/.

Using a dictionary:
- REST: When calling POST https://api.telnyx.com/v2/text-to-speech include pronunciation_dict_id with text and voice.
- WebSocket: Add pronunciation_dict_id as a query parameter on wss://api.telnyx.com/v2/text-to-speech/speech.

Managing dictionaries (CRUD):
- Create: POST /v2/pronunciation_dicts with name and items, or upload a PLS/XML or plain-text file (multipart/form-data). Plain-text lines: word=alias and word:/phoneme/.
- List: GET /v2/pronunciation_dicts?page[number]=...&page[size]=...
- Get one: GET /v2/pronunciation_dicts/{id}
- Update: PATCH /v2/pronunciation_dicts/{id} (optimistic locking; concurrent edits return 409 Conflict — re-fetch and retry).
- Delete: DELETE /v2/pronunciation_dicts/{id}

Limits:
- 50 dictionaries per organization; 100 items per dictionary.
- Max text (match) 200 chars; alias/phoneme 500 chars.
- File upload up to 1 MB.

File upload formats:
- PLS/XML (W3C Pronunciation Lexicon Specification; IPA supported).
- Plain text (line-based): word=alias or word:/ipa/.

See also: [Pronunciation Dictionaries](pronunciation-dictionaries.md).

## Voice API services in Europe

For lower latency on European calls:
- Use the EU endpoint: https://api.telnyx.eu
- Set your application’s AnchorSite to a European region (Frankfurt, London, Amsterdam) in the portal. All conference participants and queued-call additions must be in the same region.

Tip: When moving traffic to the EU, update your API base URL and redeploy any hard‑coded hosts.

## IoT SIM: common AT commands on Raspberry Pi HATs

Prerequisites:
- Enable Raspberry Pi serial (sudo raspi-config → Interfacing Options → Serial; disable login shell over serial, then reboot).
- Install a serial terminal (screen or minicom). Example: screen ttyUSB3 or screen ttyS0. Find the port via ls -l /dev.

Useful AT commands (examples vary by module/carrier):
- AT — sanity check; expects OK.
- AT+CCID — read SIM ID (ICCID).
- AT+CREG? — network registration status; AT+CREG=? for flag meanings.
- AT+COPS=? — list available networks compatible with the SIM.
- AT+COPS=1,0,"Carrier Name" — manual PLMN selection to a specific carrier.
- AT+COPS=(mode,format) — select network using values from AT+COPS=? response.
- AT+BANDS — inspect/set supported bands (module‑specific usage; use cautiously).

Troubleshooting on Raspberry Pi 4:
- The Pi may enumerate multiple serial interfaces (e.g., ttyUSBx vs ttyS0). If the expected port misbehaves, recheck dmesg/lsusb and try alternate ttyUSB indices. Using a Bluetooth keyboard/mouse can avoid contention on USB if you’re connected via a shared hub.

See also: [Connectivity Troubleshooting](connectivity-troubleshooting.md).
