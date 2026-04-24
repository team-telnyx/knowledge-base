---
title: SRV Records
summary: DNS SRV (Service) records enable automatic failover and load distribution for SIP connections by resolving to multiple Telnyx signaling IPs with priority and weight parameters.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/network-configuration/srv-records/index
    content_hash: a4cd4af94676235ab9843e05c7d65f0fca9f6313d9e168be2e82dc37a0e38656
updated_at: 2026-04-10T00:00:00Z
---

# SRV Records

DNS SRV (Service) records enable automatic failover and load distribution for SIP connections by resolving to multiple Telnyx signaling IPs with priority and weight parameters.

## SRV record format

Telnyx SRV records follow RFC 2782 DNS SRV specification:

```
_service._protocol.domain TTL class SRV priority weight port target
```

**Example:**

```
_sip._udp.example.com. 3600 IN SRV 10 10 5060 sip.telnyx.com.
```

### Parameters

| Parameter | Value             | Description                                                      |
| --------- | ----------------- | ---------------------------------------------------------------- |
| Service   | `_sip`            | SIP service identifier                                           |
| Protocol  | `_udp` or `_tcp`  | Transport protocol (UDP recommended)                             |
| Domain    | User's domain     | The domain being configured                                      |
| TTL       | `3600`            | Cache duration in seconds                                        |
| Class     | `IN`              | Internet class (standard)                                        |
| Priority  | `10`              | Lower values preferred (use same value for all Telnyx entries)   |
| Weight    | `10`              | Load distribution ratio (equal weight for balanced distribution) |
| Port      | `5060` or `5061`  | 5060 for UDP/TCP, 5061 for TLS                                   |
| Target    | `sip.telnyx.com.` | Telnyx regional FQDN (note trailing dot)                         |

## Regional FQDNs

Configure SRV records to point to the Telnyx region closest to the user's infrastructure:

| Region    | FQDN                | Resolves to IPs                    |
| --------- | ------------------- | ---------------------------------- |
| US        | `sip.telnyx.com`    | `192.76.120.10`, `64.16.250.10`    |
| Europe    | `sip-eu.telnyx.com` | `5.172.39.10`, `5.172.39.25`       |
| Canada    | `sip-ca.telnyx.com` | `193.108.220.10`, `193.108.220.25` |
| Australia | `sip-au.telnyx.com` | `193.108.104.10`, `193.108.104.25` |

For the most current IP addresses and additional regions, see [sip.telnyx.com](https://sip.telnyx.com).

## Configuration examples

### Basic configuration

Single SRV record pointing to US region:

```
_sip._udp.example.com. 3600 IN SRV 10 10 5060 sip.telnyx.com.
```

### TLS transport

For encrypted SIP signaling on port 5061:

```
_sip._tcp.example.com. 3600 IN SRV 10 10 5061 sip.telnyx.com.
```

### Multi-region redundancy

Route to US as primary, EU as secondary:

```
_sip._udp.example.com. 3600 IN SRV 10 50 5060 sip.telnyx.com.
_sip._udp.example.com. 3600 IN SRV 20 50 5060 sip-eu.telnyx.com.
```

Priority `10` (US) is preferred over priority `20` (EU).

## Benefits over A records

| Feature               | SRV Records                    | A Records                          |
| --------------------- | ------------------------------ | ---------------------------------- |
| Automatic IP failover | Yes (resolves to multiple IPs) | No (manual configuration required) |
| Port specification    | Included in record             | Hardcoded in PBX config            |
| Load balancing        | Weight-based distribution      | Requires DNS round-robin           |
| Protocol awareness    | Transport specified in record  | Assumed by application             |
| Regional routing      | FQDN-based                     | IP-based                           |

## Verification

Verify the user's SRV record configuration:

```bash theme={null}
dig _sip._udp.example.com SRV
```

Expected output shows multiple A records for the target FQDN:

```
_sip._udp.example.com. 3600 IN SRV 10 10 5060 sip.telnyx.com.

;; ADDITIONAL SECTION:
sip.telnyx.com. 300 IN A 192.76.120.10
sip.telnyx.com. 300 IN A 64.16.250.10
```

Test resolution to IP addresses:

```bash theme={null}
dig sip.telnyx.com A
```

## DNS provider configuration

Most DNS providers support SRV records through their control panel or API.

**Common DNS providers:**

* Route 53 (AWS): Record type "SRV", value format `10 10 5060 sip.telnyx.com`
* Cloudflare: Record type "SRV", configure service, protocol, priority, weight, port, target separately
* Google Cloud DNS: Use `gcloud dns record-sets create` with `--type=SRV`

**API example (AWS Route 53):**

```json theme={null}
{
  "Name": "_sip._udp.example.com",
  "Type": "SRV",
  "TTL": 3600,
  "ResourceRecords": [
    {
      "Value": "10 10 5060 sip.telnyx.com."
    }
  ]
}
```

## Failover behavior

SRV records work with Telnyx automatic failover:

1. DNS query resolves `sip.telnyx.com` to both IP1 and IP2
2. SIP INVITE sent to IP1 (primary)
3. On timeout or error, retry to IP2 (secondary)
4. If all IPs fail, attempt next priority SRV target (if configured)

See [Failover and Retries](failover-and-retries.md) for complete failover logic.

## Troubleshooting

**SRV record not resolving:**

* Verify trailing dot on target FQDN (`sip.telnyx.com.`)
* Check TTL has expired if you recently updated
* Confirm DNS propagation: `dig @8.8.8.8 _sip._udp.example.com SRV`

**PBX not using SRV record:**

* Some PBX systems require explicit SRV lookup enablement
* Configure PBX to use domain (`example.com`) not IP address
* Check PBX logs for DNS query behavior

**Unbalanced load distribution:**

* Verify equal weight values for balanced distribution
* Some SIP stacks cache first resolved IP
* Consider implementing client-side round-robin
