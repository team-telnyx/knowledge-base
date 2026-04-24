---
title: Migrate from LiveKit Cloud
summary: Switch from LiveKit Cloud to Telnyx — change three environment variables, keep everything else.
sources:
  - url: https://developers.telnyx.com/docs/livekit/migration/from-livekit-cloud
    content_hash: 175c45dad808ab3835be83767d7d0843152f9d64bd703e841e9b7ffba3d12ae6
updated_at: 2026-04-10T00:00:00Z
---

# Migrate from LiveKit Cloud

Switch from LiveKit Cloud to Telnyx — change three environment variables, keep everything else.

Zero code changes. Swap your credentials, redeploy, done.

## What changes

|                      | LiveKit Cloud                        | Telnyx                            |
| -------------------- | ------------------------------------ | --------------------------------- |
| `LIVEKIT_URL`        | `https://your-project.livekit.cloud` | `https://nyc1.livekit-telnyx.com` |
| `LIVEKIT_API_KEY`    | LiveKit Cloud key                    | Telnyx API key                    |
| `LIVEKIT_API_SECRET` | LiveKit Cloud secret                 | Your LiveKit API secret           |

## What doesn't change

* Your agent code
* SDK usage
* `lk` CLI commands
* Dockerfiles
* Room management, dispatch rules

## Steps

1. **Create a Telnyx account** at [portal.telnyx.com](https://portal.telnyx.com)
2. **Generate a Telnyx API key** in the portal
3. **Register with the platform** (one-time):
   ```bash theme={null}
   curl -s -X POST "https://<region>.livekit-telnyx.com/provision" \
     -H "Content-Type: application/json" \
     -d '{
       "name": "my-project",
       "api_key": "'$TELNYX_API_KEY'",
       "api_secret": "'$LIVEKIT_API_SECRET'"
     }'
   ```
4. **Update your environment variables** with the values above
5. **Deploy to Telnyx:**
   ```bash theme={null}
   lk agent deploy . --secrets TELNYX_API_KEY=<your-key>
   ```
6. **Verify:** `lk room list` to confirm connectivity
7. **(Optional)** Install the [Telnyx plugin](build.md) for on-prem STT, TTS, and LLM
8. **(Optional)** [Buy a Telnyx number](telephony.md) for built-in telephony

## What you gain

* **Built-in telephony, no third-party SIP fees** — On other platforms, you pay third-party SIP fees on top of your usage. On Telnyx, those are gone entirely.
* **Ultra-low latency AI on Telnyx GPUs** — STT, TTS, and LLM colocated in every region \~2ms from your agents. No round-trips to external APIs.
* **One platform, one bill** — Compute, models, telephony, and phone numbers on a single Telnyx invoice. No vendor sprawl.

## Rolling back

It's just environment variables. Point them back at LiveKit Cloud and redeploy.


## Related Pages

- [Migrate from Self-Hosted](../runbooks/migrate-from-self-hosted.md)
