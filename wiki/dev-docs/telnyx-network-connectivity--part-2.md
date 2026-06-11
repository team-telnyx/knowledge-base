---
title: Telnyx Network Connectivity
summary: Telnyx provides private network connectivity through Virtual Cross Connects
  (VXC) to AWS, GCP, and Azure, enabling direct BGP-peered links between your cloud
  environment and the Telnyx network, as well as Wireguard-based VPN peer configuration
  for Linux, macOS, and Windows clients.
sources:
- url: https://developers.telnyx.com/docs/network/vxc/azure
- url: https://developers.telnyx.com/docs/network/vxc/cost
- url: https://developers.telnyx.com/docs/network/vxc/coverage
- url: https://developers.telnyx.com/docs/network/vxc/gcp
- url: https://developers.telnyx.com/docs/network/vxc/intro/index
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/linux
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/macos
- url: https://developers.telnyx.com/docs/network/wireguard-peer-config/windows
updated_at: 2026-06-11T10:38:58Z
---

# Telnyx Network Connectivity

*Part 2 of 2 — see also: [Part 1](telnyx-network-connectivity--part-1.md)*

Telnyx provides private network connectivity through Virtual Cross Connects (VXC) to AWS, GCP, and Azure, enabling direct BGP-peered links between your cloud environment and the Telnyx network, as well as Wireguard-based VPN peer configuration for Linux, macOS, and Windows clients.

## Wireguard Peer Configuration

After setting up a [Wireguard Gateway (WGW)](wireguard-gateway.md), you will have a `.conf` file for each peer. The steps to configure a peer depend on the operating system.

### Linux

1. **Install Wireguard:**

   ```
   sudo apt install wireguard
   ```

2. **Bring up the interface:** Place the `.conf` file (e.g., `peer1.conf`) in `/etc/wireguard/` and run:

   ```
   sudo wg-quick up peer1
   ```

3. **Validate and test:**

   ```
   sudo wg show
   ```

   Verify a handshake has occurred, then ping another connected peer (e.g., `ping 172.27.0.3`).

### macOS

1. **Install the Wireguard client** from [wireguard.com/install](https://www.wireguard.com/install/).
2. **Import and activate the tunnel:** Choose **Import Tunnel(s) from File…**, select your `.conf` file, then click **Activate**. The status should change to **Active**.
3. **Validate and test:** Ping another connected peer (e.g., `ping 172.27.0.3`).

### Windows

1. **Install the Wireguard client** from [wireguard.com/install](https://www.wireguard.com/install/) (choose the Windows installer).
2. **Import and activate the tunnel:** Choose **Import Tunnel(s) from File…**, select your `.conf` file, then click **Activate**. The status should show **Active**.
3. **Validate and test:** Ping a connected peer, or set up a simple HTTP server on one peer and reach it from the other. For example, run a basic Python server on one peer:

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

   Then from the other peer:

   ```
   curl --location 'http://172.27.0.4:8000/'
   ```

   A successful response confirms end-to-end connectivity.
