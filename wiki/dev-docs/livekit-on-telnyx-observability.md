---
title: LiveKit on Telnyx observability
summary: Overview of observability features available for LiveKit agents on Telnyx,
  including current agent log streaming and upcoming tracing, metrics, and session
  debugging capabilities.
sources:
- url: https://developers.telnyx.com/docs/livekit/observability/index
updated_at: 2026-08-05T13:47:36Z
---

# LiveKit on Telnyx observability

Overview of observability features available for LiveKit agents on Telnyx, including current agent log streaming and upcoming tracing, metrics, and session debugging capabilities.

## Agent logs

Stream logs from your running agent via the Telnyx CLI:

```
lk agent logs <agent-id>
```

This command provides real-time stdout/stderr output from your agent, matching the log access experience available on LiveKit Cloud.

## Coming very soon

Traces, metrics, and session debugging are on the [LiveKit on Telnyx compatibility](livekit-on-telnyx-compatibility.md) roadmap. These capabilities will extend the current log streaming with deeper insight into agent execution, performance metrics, and interactive session debugging.
