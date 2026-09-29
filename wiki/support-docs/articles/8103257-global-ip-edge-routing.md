---
title: "Global IP & Edge Routing"
summary: "Step by step process on how to get started with Telnyx Networking via procurement of Global IPs and setting up Global… See Telnyx guidance and requirements."
sources:
- url: "https://support.telnyx.com/en/articles/8103257-global-ip-edge-routing"
updated_at: 2026-07-08T00:00:00Z
tags: [support-docs]
source_path: "support-docs/en--articles--8103257-global-ip-edge-routing.md"
generated_by: incremental-support-docs-wiki
---
<!-- generated_from=support-docs/en--articles--8103257-global-ip-edge-routing.md -->

# Global IP & Edge Routing

Step by step process on how to get started with Telnyx Networking via procurement of Global IPs and setting up Global… See Telnyx guidance and requirements.




## Setting up Networking for Global Edge Routing

## **NOTE:** Please note that Global IP for customers is currently disabled. At present there are no plans to re-enable it in the near future. **Step 1. Create a Network**

![Network creation settings section. ](_images/c2cf5e5e636b0b8f.png)

## **Step 2. Create a WireGuard Interface**

![Wireguard interface section. ](_images/4d7ecc9d207690e4.png)

## **Step 3: Wait for WireGuard Interface to finish provisioning**

![Wireguard interface section. ](_images/67511a22e5111892.png)

## **Step 4: Create a WireGuard Peer**

![Wireguard interface section. ](_images/0d50fc133cd8e3fa.png)

## **Step 5: Make note of the Private Key returned**

![Wireguard interface section for private key. ](_images/d02b7939067e65cc.png)

## **Step 6: Acquire Global IP**

![Wireguard interface section for global IP. ](_images/9957e09047ea1a5c.png)

## **Step 7: Assign WireGuard Peer to Global IP**

![Wireguard interface section for Wireguard Peer. ](_images/e34e9fb24ede170c.png)

## **Step 8: Copy and paste WireGuard config to service VM, using the Private Key in Step 5**

![Wireguard interface for service VM. ](_images/70383a83726099b2.png)
