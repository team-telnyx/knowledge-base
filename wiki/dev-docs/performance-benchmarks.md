---
title: Performance Benchmarks
summary: Indicative throughput results for Telnyx Cloud Storage, including aggregate
  PutObject and GetObject performance measured against a regional endpoint using a
  multi-client benchmark setup.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks
updated_at: 2026-08-05T13:39:20Z
---

# Performance Benchmarks

Indicative throughput results for Telnyx Cloud Storage, including aggregate PutObject and GetObject performance measured against a regional endpoint using a multi-client benchmark setup.

## Storage benchmark summary

Telnyx achieved the following throughput results given the bench test setup described in the subsequent sections:

- **PutObject Aggregate: 2.029 GiB/s**
- **GetObject Aggregate: 2.714 GiB/s**

A few disclaimers apply to these numbers:

- The client configuration that produces the highest achievable throughputs was not exhaustively searched.
- The result is only indicative of what can be achieved with the available testbed hardware specifications and arrangement.
- The test clients are not subjected to the limits outlined in the previous section.
- As new sites are launched, test results and methodology will be continuously updated.

## Benchmark environment explained

### Client hardware

Eight bare metal machines are used as clients initiating requests to one of the regional endpoints. They are located off network with a 100 Gbps uplink to the public internet.

| Type | Count of nodes | CPU | Mem | Storage | Network |
| --- | --- | --- | --- | --- | --- |
| Type 1 | 4 | 64 | 2 TiB | 4 x 6.4 TiB NVMe | 100 Gbps |
| Type 2 | 4 | 32 | 2 TiB | 1 x 960 GiB NVMe | 100 Gbps |

No special optimizations are made on the client OS.

### Benchmark software

The benchmark tool used is [wasabi-tech/s3-benchmark](https://github.com/wasabi-tech/s3-benchmark).

### Client setup

Each client bare metal reads and writes to its individual bucket.

### Results

![Put Object Aggregate Throughput](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/storage-PutObjectThroughput.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=01d6d95cac82dc2b3287dfd7c9ae4044)

![Get Object Aggregate Throughput](https://mintcdn.com/telnyx/M104dP2YWeqFiyN4/img/storage-GetObjectThroughput.png?fit=max&auto=format&n=M104dP2YWeqFiyN4&q=85&s=2afbf1963e40489ca3e7ecc97c8b7c0d)
