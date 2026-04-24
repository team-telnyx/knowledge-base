---
title: Migrate from Self-Hosted
summary: Stop running LiveKit infrastructure.
sources:
  - url: https://developers.telnyx.com/docs/livekit/migration/from-self-hosted
    content_hash: 8ffde58a5ad2ced58b45ebf48e51695a650b85e6a5a3b532426e5d8a60efbf15
updated_at: 2026-04-10T00:00:00Z
---

# Migrate from Self-Hosted

Stop running LiveKit infrastructure. Deploy your agents to Telnyx.

Keep your agents, ditch the infrastructure. No more managing Kubernetes clusters, TURN servers, SIP services, or autoscaling.

## What Telnyx replaces

* LiveKit SFU server
* SIP service / Otel SIP
* TURN/STUN servers
* Container orchestration / autoscaling
* TLS termination and load balancing
* Monitoring infrastructure

## What stays the same

* Your agent code
* SDK calls
* Room management logic
* Dispatch rules

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
4. **Update your agent** to point at `https://nyc1.livekit-telnyx.com` (or your [preferred region](connect-to-telnyx.md#available-regions))
5. **Move secrets** to the platform:
   ```bash theme={null}
   lk agent deploy . --secrets TELNYX_API_KEY=<your-key>,OTHER_SECRET=<value>
   ```
6. **Re-create dispatch rules** on the Telnyx platform
7. **Update SIP configuration** to point at Telnyx [SIP endpoints](telephony.md)
8. **Verify** your agent is running: `lk room list`
9. **Decommission** your self-hosted infrastructure

## What you gain

* **No infra management** — No Kubernetes, no TURN, no Redis for multi-region.
* **Built-in SIP, no third-party SIP fees** — On other platforms, you pay third-party SIP fees on top of your usage. On Telnyx, those are gone entirely.
* **Managed autoscaling** — Platform handles container lifecycle.
* **Ultra-low latency AI on Telnyx GPUs** — STT, TTS, and LLM colocated in every region \~2ms from your agents. No round-trips to external APIs.


## Related Pages

- [Migrate from LiveKit Cloud](../runbooks/migrate-from-livekit-cloud.md)
- [Migrating from S3](../runbooks/migrating-from-s3.md)
