---
title: Wireguard Peer Config on MacOS
summary: You come from [here](https://developers.telnyx.com/docs/network/gateways/wireguard-gateway) and have a `.conf` file ready.
sources:
  - url: https://developers.telnyx.com/docs/network/wireguard-peer-config/macos/index
    content_hash: d113feaa9f82757c8ecda14c41589007e90d8f9b85207a292cf3718f2c79071c
updated_at: 2026-04-10T00:00:00Z
---

# Wireguard Peer Config on MacOS

## Prerequisite

You come from [here](https://developers.telnyx.com/docs/network/gateways/wireguard-gateway) and have a `.conf` file ready.

## Step 1: Install Wireguard Client

From [here](https://www.wireguard.com/install/), choose and install the macOS client.

## Step 2: Create a Tunnel

"Import Tunnel(s) from File..."

<img alt="Import Tunnel(s) from File..." />

"Activate"

<img alt="&#x22;Activate&#x22;" />

At this point, it should show "Status: Active"

<img alt="&#x22;Active&#x22;" />

## Step 3: Validating and Testing

A connected peer should be pingable.

```
user@macbook-pro wireguard % ping 172.27.0.3
PING 172.27.0.3 (172.27.0.3): 56 data bytes
64 bytes from 172.27.0.3: icmp_seq=0 ttl=63 time=35.006 ms
64 bytes from 172.27.0.3: icmp_seq=1 ttl=63 time=32.528 ms
64 bytes from 172.27.0.3: icmp_seq=2 ttl=63 time=33.376 ms
^C
--- 172.27.0.3 ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 32.528/33.637/35.006/1.028 ms
```

## Next Steps

[Wireguard Gateway (WGW) Guide](https://developers.telnyx.com/docs/network/gateways/wireguard-gateway) outlines many use cases that may be valuable to you.


## Related Pages

- [Wireguard Peer Config on Windows](../runbooks/wireguard-peer-config-on-windows.md)
- [Wireguard Peer Config on Linux](../runbooks/wireguard-peer-config-on-linux.md)
