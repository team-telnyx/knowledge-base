---
title: WireGuard Peer Configuration
summary: Step-by-step instructions for configuring a WireGuard peer on Linux, macOS,
  and Windows after obtaining a `.conf` file from the Telnyx WireGuard Gateway.
sources:
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/linux
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/macos
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/windows
updated_at: 2026-08-05T13:59:20Z
---

# WireGuard Peer Configuration

Step-by-step instructions for configuring a WireGuard peer on Linux, macOS, and Windows after obtaining a `.conf` file from the Telnyx WireGuard Gateway.

## Prerequisite

You should already have a `.conf` file ready from the [WireGuard Gateway](wireguard-gateway.md) setup.

## Linux

### Install WireGuard

```
ubuntu@ip-10-10-11-10:~$ sudo apt install wireguard
```

### Bring up the Interface

Assuming the correct config file is located at `/etc/wireguard/peer1.conf`:

```
ubuntu@ip-10-10-11-10:~$ sudo wg-quick up peer1
[#] ip link add peer1 type wireguard
[#] wg setconf peer1 /dev/fd/63
[#] ip -4 address add 172.27.0.2/32 dev peer1
[#] ip link set mtu 8921 up dev peer1
[#] ip -4 route add 172.27.0.0/24 dev peer1
```

### Validate and Test

Verify the interface is up with `sudo wg show`:

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

If another peer is connected to the network, it should be pingable:

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

## macOS

### Install the WireGuard Client

Download and install the macOS client from the [WireGuard install page](https://www.wireguard.com/install/).

### Create a Tunnel

1. Open the WireGuard app and choose **Import Tunnel(s) from File…**
   ![Import Tunnel(s) from File...](https://mintcdn.com/telnyx/d2AUJO5qdne_WnZI/img/create-tunnel.png?fit=max&auto=format&n=d2AUJO5qdne_WnZI&q=85&s=01f8c04453399af1e7671b9aabd5d706)
2. Click **Activate**.
   !["Activate"](https://mintcdn.com/telnyx/qRGzozfyAtvPtPCw/img/activate.png?fit=max&auto=format&n=qRGzozfyAtvPtPCw&q=85&s=507ad61da1c474f140310b026133a524)
3. The tunnel should now show **Status: Active**.
   !["Active"](https://mintcdn.com/telnyx/qRGzozfyAtvPtPCw/img/activate-success.png?fit=max&auto=format&n=qRGzozfyAtvPtPCw&q=85&s=3b82c9d8d4dafe5af12ad0ec85baefb4)

### Validate and Test

A connected peer should be pingable:

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

## Windows

### Install the WireGuard Client

Download and install the Windows installer from the [WireGuard install page](https://www.wireguard.com/install/).

### Create a Tunnel

1. Open the WireGuard app and choose **Import Tunnel(s) from File…**
   ![Import Tunnel(s)](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/windows-import-tunnel.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=9dcf26ca565041ad8b62e2ca80d79c8b)
2. Click **Activate**.
   ![Activate Tunnel](https://mintcdn.com/telnyx/2URMJX3zP3rZ0vDO/img/windows-activate-tunnel.png?fit=max&auto=format&n=2URMJX3zP3rZ0vDO&q=85&s=a89bf5e4ff38593662c06093f2a0348a)
3. The tunnel should now show **Status: Active**.

### Validate and Test

Try pinging to or from a connected peer. If that does not work, you can also set up a barebones HTTP server and reach it from the connected peer (or vice versa). An example barebones server in Python:

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

Run the server on one peer (`python3 server.py`, assuming the example above is saved as `server.py`) and reach it with a client or browser from the other peer:

```
$ curl --location 'http://172.27.0.4:8000/'
It works!
```

## Next Steps

The [WireGuard Gateway](wireguard-gateway.md) guide outlines many use cases that may be valuable to you.
