---
title: Performance Benchmarks
summary: 'Summary of performance tests showing aggregate throughput for Telnyx Cloud Storage operations.'
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks/index
    content_hash: 90837e687737e1d8c4f391069956943c968c55ab8214342ad68d6b42304fa9f1
updated_at: 2026-04-10T00:00:00Z
---

# Performance Benchmarks

Understand Telnyx Storage's capabilities: Summary of performance tests showing aggregate throughput for storage operations.

## Storage benchmark summary

We achieved the following throughput results given the bench test setup described in the subsequent sections.

* **PutObject Aggregate: 2.029 GiB/s**
* **GetObject Aggregate: 2.714 GiB/s**

A few disclaimers

* We did not exhaustively search the client configuration that produces the highest achievable throughputs.
* This result is only indicative of what can be achieved with the available testbed hardware specifications and arrangement.
* The test clients are not subjected to the limits outlined in the previous section.
* As we launch new sites, we will continuously update our test results and methodology. 

## Benchmark environment explained

### Client hardware 

(8) of the following bare metal machines are used as clients initiating requests to one of the regional endpoints. They are located off network with 100 Gbps uplink to the public internet.

<table>
  <tbody>
    <tr>
      <td>Type</td>
      <td>Count of nodes</td>
      <td>CPU</td>
      <td>Mem</td>
      <td>Storage</td>
      <td>Network</td>
    </tr>

    <tr>
      <td>Type 1</td>
      <td>4</td>
      <td>64</td>
      <td>2 TiB</td>
      <td>4 x 6.4TiB NVMe</td>
      <td>100 Gbps</td>
    </tr>

    <tr>
      <td>Type 2</td>
      <td>4</td>
      <td>32</td>
      <td>2 TiB</td>
      <td>1 x 960GiB NVMe</td>
      <td>100 Gbps</td>
    </tr>
  </tbody>
</table>

No special optimizations are made on the client OS. 

### Benchmark Software

[https://github.com/wasabi-tech/s3-benchmark](https://github.com/wasabi-tech/s3-benchmark)

### Client Setup

Each client bare metal reads and writes to their individual bucket.

### Results

<img alt="Put Object Aggregate Throughput" />

<img alt="Get Object Aggregate Throughput" />
