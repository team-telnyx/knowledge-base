---
title: End-of-Turn Detection
summary: Flux end-of-turn detection parameters for voice agent turn-taking.
sources:
  - url: https://developers.telnyx.com/docs/voice/stt/websocket-streaming/parameters/end-of-turn
    content_hash: 38296367a619b9a7b4b8edeca248d00753d46aa8ce209eb396a1f2e6230bc304
updated_at: 2026-04-10T00:00:00Z
---

# End-of-Turn Detection

Flux end-of-turn detection parameters for voice agent turn-taking.

**Deepgram Flux only.** These parameters return a 400 error on non-Flux models.

Flux uses a confidence-based system to decide when a speaker has finished their turn.

<ParamField type="float">
  Confidence threshold (`0.5`–`0.9`) for triggering an `EndOfTurn` event. Higher values require more certainty the speaker is done — fewer false positives but slightly more latency. Lower values respond faster but may cut speakers off mid-thought.

<ParamField type="float">
  Confidence threshold (`0.3`–`0.9`) for triggering an early `EagerEndOfTurn` event. Not set by default — setting it enables eager mode. When fired, your agent can start generating a response speculatively. If the speaker resumes, a `TurnResumed` event cancels it. Must be ≤ `eot_threshold`. Lower values = earlier triggers, more false starts. Typical range: `0.3`–`0.5` for \~150–250 ms latency savings at the cost of \~50–70% more LLM calls.

<ParamField type="integer">
  Maximum silence in ms (`500`–`10000`) before forcing `EndOfTurn` regardless of confidence. Resets when speech resumes. Increase for speakers who pause frequently; decrease for rapid-fire Q\&A.

## Event Flow

Without eager mode (`eot_threshold` only):

```
Speech → silence → confidence ≥ eot_threshold → EndOfTurn
Speech → silence → timeout (eot_timeout_ms) → EndOfTurn
```

With eager mode (`eager_eot_threshold` set):

```
Speech → silence → confidence ≥ eager_eot_threshold → EagerEndOfTurn
  → speaker stays silent → confidence ≥ eot_threshold → EndOfTurn
  → speaker resumes → TurnResumed (cancel speculative work)
```

## Configuration Profiles

**Default** — balanced for general use:

```
?eot_threshold=0.7&eot_timeout_ms=5000
```

**Low-latency** — fast response, more false starts:

```
?eager_eot_threshold=0.4&eot_threshold=0.7&eot_timeout_ms=6000
```

**High-reliability** — fewer interruptions, more latency:

```
?eot_threshold=0.85&eot_timeout_ms=8000
```
