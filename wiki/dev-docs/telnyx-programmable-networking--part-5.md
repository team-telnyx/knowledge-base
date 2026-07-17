---
title: Telnyx Programmable Networking
summary: Telnyx Programmable Networking provides private connectivity to Telnyx SIP,
  API, and storage endpoints via logically isolated networks, three types of gateways
  (WireGuard, Internet, and Private Wireless), and Virtual Cross Connects to AWS,
  GCP, and Azure. This page consolidates the coverage APIs, network creation, gateway
  setup and use cases, WireGuard peer configuration for Linux/macOS/Windows, and cloud-provider-specific
  VXC setup procedures and pricing.
sources:
- url: https://developers.telnyx.com/docs/network/coverage
- url: https://developers.telnyx.com/docs/network/gateways/internet-gateway
- url: https://developers.telnyx.com/docs/network/gateways/private-wireless-gateway
- url: https://developers.telnyx.com/docs/network/gateways/wireguard-gateway/index
- url: https://developers.telnyx.com/docs/network/networks
- url: https://developers.telnyx.com/docs/network/overview/index
- url: https://developers.telnyx.com/docs/network/vxc/api
- url: https://developers.telnyx.com/docs/network/vxc/aws/index
- url: https://developers.telnyx.com/docs/network/vxc/azure
- url: https://developers.telnyx.com/docs/network/vxc/cost
- url: https://developers.telnyx.com/docs/network/vxc/coverage
- url: https://developers.telnyx.com/docs/network/vxc/gcp
- url: https://developers.telnyx.com/docs/network/vxc/intro/index
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/linux
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/macos
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/windows
updated_at: 2026-07-17T09:20:17Z
---

# Telnyx Programmable Networking

*Part 5 of 7 — see also: [Part 1](telnyx-programmable-networking--part-1.md), [Part 2](telnyx-programmable-networking--part-2.md), [Part 3](telnyx-programmable-networking--part-3.md), [Part 4](telnyx-programmable-networking--part-4.md), [Part 6](telnyx-programmable-networking--part-6.md), [Part 7](telnyx-programmable-networking--part-7.md)*

Telnyx Programmable Networking provides private connectivity to Telnyx SIP, API, and storage endpoints via logically isolated networks, three types of gateways (WireGuard, Internet, and Private Wireless), and Virtual Cross Connects to AWS, GCP, and Azure. This page consolidates the coverage APIs, network creation, gateway setup and use cases, WireGuard peer configuration for Linux/macOS/Windows, and cloud-provider-specific VXC setup procedures and pricing.

## WireGuard Peer Configuration

### Linux

**Prerequisite** — you come from the [WireGuard Gateway (WGW)](wireguard-gateway-wgw.md) guide and have a `.conf` file ready.

**Step 1: Install WireGuard**

```
ubuntu@ip-10-10-11-10:~$ sudo apt install wireguard
```

**Step 2: Bring up the Interface** — assuming the correct config file is located at `/etc/wireguard/peer1.conf`:

```
ubuntu@ip-10-10-11-10:~$ sudo wg-quick up peer1
[#] ip link add peer1 type wireguard
[#] wg setconf peer1 /dev/fd/63
[#] ip -4 address add 172.27.0.2/32 dev peer1
[#] ip link set mtu 8921 up dev peer1
[#] ip -4 route add 172.27.0.0/24 dev peer1
```

**Step 3: Validating and Testing**

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

### macOS

**Prerequisite** — you come from the [WireGuard Gateway (WGW)](wireguard-gateway-wgw.md) guide and have a `.conf` file ready.

**Step 1: Install WireGuard Client** — from [the WireGuard install page](https://www.wireguard.com/install/), choose and install the macOS client.

**Step 2: Create a Tunnel** — "Import Tunnel(s) from File…"

![Import Tunnel(s) from File...](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/create-tunnel.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=01f8c04453399af1e7671b9aabd5d706)

"Activate"

!["Activate"](https://mintcdn.com/telnyx/qRGzozfyAtvPtPCw/img/activate.png?fit=max&auto=format&n=qRGzozfyAtvPtPCw&q=85&s=507ad61da1c474f140310b026133a524)

At this point, it should show "Status: Active"

!["Active"](https://mintcdn.com/telnyx/qRGzozfyAtvPtPCw/img/activate-success.png?fit=max&auto=format&n=qRGzozfyAtvPtPCw&q=85&s=3b82c9d8d4dafe5af12ad0ec85baefb4)

**Step 3: Validating and Testing** — a connected peer should be pingable.

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

### Windows

**Prerequisite** — you come from the [WireGuard Gateway (WGW)](wireguard-gateway-wgw.md) guide and have a `.conf` file ready.

**Step 1: Install WireGuard Client** — from [the WireGuard install page](https://www.wireguard.com/install/), choose and install the Windows Installer.

**Step 2: Create a Tunnel** — "Import Tunnel(s) from File…"

![Import Tunnel(s)](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/windows-import-tunnel.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=9dcf26ca565041ad8b62e2ca80d79c8b)

"Activate"

![Activate Tunnel](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/windows-activate-tunnel.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=a89bf5e4ff38593662c06093f2a0348a)

At this point, it should show "Status: Active".

**Step 3: Validating and Testing** — you can try pinging to/from a connected peer. If that does not work you can also try to set up a barebones http server and hit it from the connected peer (or vice versa).

An example barebones server in python:

```python
import socket

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

while True:
    client_connection, client_address = server_socket.accept()
    request = client_connection.recv(1024).decode()
    response = 'HTTP/1.0 200 OK\n\nIt works!'
    client_connection.sendall(response.encode())
    client_connection.close()
```

Run the server in one peer (`python3 server.py` - assuming you saved the above example in a file named `server.py`) and reach it with a client / browser from the other peer:

```
$ curl --location 'http://172.27.0.4:8000/'
It works!
```
