---
title: Voice Call Router
summary: Route calls based on time of day and caller location.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/demos/voice-call-router
    content_hash: c3b07ce23f5295f02d089dce1988d47b4d26ba9c029fe21eba93c66cdd31c3b9
updated_at: 2026-04-10T00:00:00Z
---

# Voice Call Router

Route calls based on time of day and caller location.

Route incoming calls based on time of day, caller location, or custom logic.

**What you'll learn:**

* TeXML for call control
* Time-based routing logic
* Geographic routing

## Step 1: Create the Function

```bash theme={null}
telnyx-edge new-func -l=python -n=call-router
cd call-router
```

## Step 2: Add Dependencies

Create `requirements.txt`:

```txt theme={null}
pytz>=2024.1
```

## Step 3: Implement Call Routing

```python theme={null}
from datetime import datetime
import pytz

class Function:
    async def handler(self, request):
        webhook = await request.json()
        caller = webhook.get("from", "")

        # Determine routing
        destination = self.get_destination(caller)

        # Generate TeXML response
        texml = f"""<?xml version="1.0" encoding="UTF-8"?>

    Please hold while we connect your call.
    <Dial timeout="30">
        {destination}

    We're sorry, no one is available. Please try again later.

"""

        return {
            "status": 200,
            "headers": {"Content-Type": "application/xml"},
            "body": texml
        }

    def get_destination(self, caller):
        # Time-based routing
        est = pytz.timezone("America/New_York")
        now = datetime.now(est)
        hour = now.hour

        # Business hours: 9am-5pm EST
        if 9 <= hour < 17:
            # Route to main office
            return "+15551234567"
        else:
            # Route to after-hours support
            return "+15559876543"

        # Geographic routing example:
        # if caller.startswith("+44"):
        #     return "+441onal support"
        # return "+1 US support"
```

## Step 4: Deploy

```bash theme={null}
telnyx-edge ship
```

Configure your Telnyx number to use this function as the TeXML webhook.


## Related Pages

- [Voice Cloning](../runbooks/voice-cloning.md)
