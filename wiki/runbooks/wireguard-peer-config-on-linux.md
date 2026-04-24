---
title: Wireguard Peer Config on Linux
summary: You come from [here](https://developers.telnyx.com/docs/network/gateways/wireguard-gateway) and have a `.conf` file ready.
sources:
  - url: https://developers.telnyx.com/docs/network/wireguard-peer-config/linux/index
    content_hash: f150e25a3395961e106439108768b2480b9a7143d97131e8155037a67785c0ca
updated_at: 2026-04-10T00:00:00Z
---

# Wireguard Peer Config on Linux

## Prerequisite

You come from [here](https://developers.telnyx.com/docs/network/gateways/wireguard-gateway) and have a `.conf` file ready.

## Step 1: Install Wireguard

`ubuntu@ip-10-10-11-10:~$ sudo apt install wireguard`

## Step 2: Bring up the Interface

Assuming the correct config file is located at `/etc/wireguard/peer1.conf`

```
ubuntu@ip-10-10-11-10:~$ sudo wg-quick up peer1
[#] ip link add peer1 type wireguard
[#] wg setconf peer1 /dev/fd/63
[#] ip -4 address add 172.27.0.2/32 dev peer1
[#] ip link set mtu 8921 up dev peer1
[#] ip -4 route add 172.27.0.0/24 dev peer1
```

## Step 3: Validating and Testing

```
ubuntu@ip-10-10-11-10:~$ sudo wg show
interface: peer1
  public key: Jt1zAJD6W2BZgOwtUsNY2KrMO0oRfUmfAEZGNEUZKiQ=
  private key: (hidden)
  listening port: 43548

peer: XYy8e5EKtE1F0fwwMgr792/9noYs53uRZBX5O3XJ4Eg=
  endpoint: 64.16.243.3:5107
  allowed ips: 172.27.0.0/24
  latest handshake: 1 minute, 28 seconds ago
  transfer: 92 B received, 2.86 KiB sent
  persistent keepalive: every 1 second
```

If another peer is connected to the network, it should be pingable.

```
ubuntu@ip-10-10-11-10:~$ ping 172.27.0.3
PING 172.27.0.3 (172.27.0.3) 56(84) bytes of data.
64 bytes from 172.27.0.3: icmp_seq=1 ttl=63 time=25.8 ms
64 bytes from 172.27.0.3: icmp_seq=2 ttl=63 time=25.6 ms
64 bytes from 172.27.0.3: icmp_seq=3 ttl=63 time=25.5 ms
^C
--- 172.27.0.3 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 25.493/25.610/25.751/0.106 ms
```

## Next Steps

[Wireguard Gateway (WGW) Guide](https://developers.telnyx.com/docs/network/gateways/wireguard-gateway) outlines many use cases that may be valuable to you.


## Related Pages

- [Wireguard Peer Config on Windows](../runbooks/wireguard-peer-config-on-windows.md)
- [Wireguard Peer Config on MacOS](../runbooks/wireguard-peer-config-on-macos.md)
