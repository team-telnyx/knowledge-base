---
title: Telnyx Programmable Networking Overview
summary: Telnyx Programmable Networking enables applications to reach Telnyx SIP and
  API endpoints without traversing the public internet, offering lower latency and
  higher throughput. It supports connections from major hyperscalers (AWS, GCP, Azure)
  and user data centers with Equinix presence, and is built around core concepts such
  as coverage, networks, gateways, and virtual cross connects.
sources:
- url: https://developers.telnyx.com/docs/network/overview
updated_at: 2026-08-05T13:58:47Z
---

# Telnyx Programmable Networking Overview

Telnyx Programmable Networking enables applications to reach Telnyx SIP and API endpoints without traversing the public internet, offering lower latency and higher throughput. It supports connections from major hyperscalers (AWS, GCP, Azure) and user data centers with Equinix presence, and is built around core concepts such as coverage, networks, gateways, and virtual cross connects.

## Introduction

Telnyx Programmable Networking allows users and their applications to access Telnyx SIP and API endpoints **without traversing the public internet**, providing a path with better latency and throughput. The SIP and API endpoints include:

- `api.telnyx.com`
- `sip.telnyx.com` and their regional counterparts
- `*.telnyxcloudstorage.com` where `*` represents all available storage regions (e.g. `us-central-1`)

Applications can reside in any of the major hyperscalers — AWS, GCP, and Azure — or in the user's own data centers, provided the user has a presence in Equinix. This model is analogous to certain AWS concepts: from the outside world, a user can use a Direct Connect to reach private resources (such as EC2 instances) or public resources (such as S3). For AWS, however, the "outside" world is largely limited to the user's on-premise data centers.

## API Concepts

### Coverage

The Coverage API enumerates all the supported products at each of Telnyx's Points of Presence (PoPs). Before creating any resources, ensure that:

1. There is a PoP in the vicinity from where you want to connect.
2. The desired resources are available at that PoP.

Depending on the resource, there are also product-specific coverage endpoints that must be consulted. See the [Coverage](coverage.md) guide for more detail.

### Networks

A Network is a logically isolated virtual network. It is a prerequisite for the creation of other networking elements. See the [Networks](networks.md) guide for more detail.

### Gateways

A Gateway is a virtual node that facilitates traffic routing between your Telnyx network and an outside network. There are three types of gateways:

- **WireGuard Gateways (WGW)** — represented as `interface` in the API
- **Internet Gateways (IGW)**
- **Private Wireless Gateways (PWG)**

#### WireGuard Gateways

A WireGuard Gateway is a virtual VPN concentrator implemented with the open source WireGuard protocol. It is similar to:

- Virtual Private Gateway in AWS
- VPN Gateway in GCP
- Virtual Network Gateway in Azure

See the [WireGuard Gateway](wireguard-gateway.md) guide for more detail.

#### Internet Gateways

An Internet Gateway routes traffic to and from the internet, similar to an Internet Gateway or NAT Gateway in AWS. See the [Internet Gateways Guide](https://developers.telnyx.com/docs/network/gateways/internet-gateway) for more detail.

#### Private Wireless Gateways

A Private Wireless Gateway is a private packet gateway that concentrates, routes, and segments traffic for a group of SIMs. See the [Private Wireless Gateway guide](https://developers.telnyx.com/docs/iot-sim/private-wireless-gateways) for more detail.

### Virtual Cross Connects

A Virtual Cross Connect (VXC) is a virtual direct connection between a supported cloud provider and Telnyx. See the [VXC guide](https://developers.telnyx.com/docs/network/vxc/intro) for more detail.
