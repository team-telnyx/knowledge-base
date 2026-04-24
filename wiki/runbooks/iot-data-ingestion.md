---
title: IoT Data Ingestion
summary: Collect and process IoT sensor data globally.
sources:
  - url: https://developers.telnyx.com/docs/edge-compute/frameworks/iot-data-ingestion
    content_hash: c2da5477398ac11ee31a692177b2405c34b62dfd6d39888f825c01664cada19d
updated_at: 2026-04-10T00:00:00Z
---

# IoT Data Ingestion

Collect and process IoT sensor data globally.

Collect sensor data from IoT devices globally with edge processing and aggregation.

## Architecture Diagram

```
┌──────────────────────────────────────────────────────────────────┐
│                       IoT Devices (Global)                        │
│  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐  ┌───────┐          │
│  │Sensor │  │Sensor │  │Sensor │  │Sensor │  │Sensor │          │
│  │  A    │  │  B    │  │  C    │  │  D    │  │  E    │          │
│  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘  └───┬───┘          │
└──────┼──────────┼──────────┼──────────┼──────────┼───────────────┘
       │          │          │          │          │
       └──────────┴────┬─────┴──────────┴──────────┘
                       ▼
         ┌──────────────────────────────┐
         │     Telnyx Edge (Per-PoP)    │
         │  ┌─────────┐  ┌───────────┐  │
         │  │Validate │→ │ Aggregate │  │
         │  │ + Parse │  │ + Buffer  │  │
         │  └─────────┘  └───────────┘  │
         └──────────────────────────────┘
                       │
                       ▼
         ┌──────────────────────────────┐
         │      Central Data Lake       │
         └──────────────────────────────┘
```

## Implementation

```javascript theme={null}
// IoT data ingestion with edge processing
// Note: For production, use a persistent queue (e.g., Kafka, Redis)
// to avoid data loss. This example shows the processing pattern.

export async function handler(request) {
    // Parse sensor data
    const data = await request.json();

    // Validate
    if (!isValidSensorData(data)) {
        return new Response(JSON.stringify({ error: "Invalid data" }), {
            status: 400
        });
    }

    // Enrich with edge metadata
    const enriched = {
        ...data,
        edge_pop: process.env.TELNYX_POP,
        received_at: Date.now(),
        device_id: request.headers.get("X-Device-ID")
    };

    // Send directly to data lake (no in-memory buffering to avoid data loss)
    const response = await fetch(process.env.DATA_LAKE_URL, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            reading: enriched,
            edge_pop: process.env.TELNYX_POP
        })
    });

    if (!response.ok) {
        // Return error so client can retry
        return new Response(JSON.stringify({ error: "Failed to store" }), {
            status: 502
        });
    }

    return new Response(JSON.stringify({ received: true }));
}

function isValidSensorData(data) {
    return data.sensor_type && 
           typeof data.value === "number" &&
           data.timestamp;
}
```

> **Note:** For high-volume ingestion with batching, use an external queue (Kafka, Redis Streams) to buffer data reliably. In-memory buffers in serverless functions risk data loss on cold starts or process recycling.

## Use Cases

* **Fleet management** — Vehicle telemetry processing
* **Smart buildings** — Sensor data aggregation
* **Industrial IoT** — Edge preprocessing for manufacturing
