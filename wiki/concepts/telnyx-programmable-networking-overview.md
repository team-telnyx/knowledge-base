---
title: Telnyx Programmable Networking Overview
summary: Telnyx programmable networking allows users and their application to access Telnyx SIP and API endpoints ***without traversing the public internet***, therefore offering a path with better latency and throughput.
sources:
  - url: https://developers.telnyx.com/docs/network/overview/index
    content_hash: b17a9e8c09620ab1a1ae8ec94d1e1d56a1467722cb1fbdfd689612d1c8b1552c
updated_at: 2026-04-10T00:00:00Z
---

# Telnyx Programmable Networking Overview

## Introduction

Telnyx programmable networking allows users and their application to access Telnyx SIP and API endpoints ***without traversing the public internet***, therefore offering a path with better latency and throughput.

The SIP and API endpoints are:

* `api.telnyx.com`
* `sip.telnyx.com` and their regional counterparts
* `*.telnyxcloudstorage.com` where `*` is all available storage regions, e.g. `us-central-1`

The users' applications can reside in any one of the major hyperscalers, i.e. AWS, GCP, and Azure, or the users' own data centers (as long as the user has a presence in Equinix.)

This model is analogous to certain AWS concepts — From the “outside” world, a user can use a Direct Connect to connect to private resources (e.g. your EC2 instances) or public resources (e.g. S3). Though to AWS, the “outside” world is largely limited to their users’ on premise data centers.

## API Concepts

### Coverage

Coverage API enumerates all the supported products at each of Telnyx's PoP.

Before creating any resources, please ensure that

1. There is a PoP in the vicinity from where you want to connect, and
2. The desired resources are available at that PoP.

Equally important, depending on the resource, there are product specific coverage endpoints you must consult.

Refer to the [coverage guide](https://developers.telnyx.com/docs/network/coverage) for more detail.

### Networks

It is a logically isolated virtual network. It is a pre-requisite for the creation of other elements.

Refer to the [network guide](https://developers.telnyx.com/docs/network/networks) for more detail.

### Gateways

It is a virtual node that facilitates traffic routing between your Telnyx network and an outside network.

There are three types of gateways.

* Wireguard Gateways (WGW); in the API, it's named `interface`
* Internet Gateways (IGW)
* Private Wireless Gateways (PWG)

#### Wireguard Gateways

It is a virtual VPN concentrator implemented with the open source wireguard protocol.

It is similar to

* Virtual Private Gateway in AWS
* VPN Gateway in GCP
* Virtual Network Gateway in Azure

Refer to the [wireguard gateway guide](https://developers.telnyx.com/docs/network/gateways/wireguard-gateway) for more detail.

#### Internet Gateways

It is an element that routes traffic to and from the internet, similar to Internet Gateway or NAT Gateway in AWS

Refer to the [Internet Gateways Guide](https://developers.telnyx.com/docs/network/gateways/internet-gateway)

#### Private Wireless Gateways

It is a private packet gateway that concentrates, routes, and segments traffic for a group of SIMs.

Refer to [private wireless gateway guide](https://developers.telnyx.com/docs/iot-sim/private-wireless-gateways) for more detail.

### Virtual Cross Connects

It is a virtual direct connection between a supported cloud provider and Telnyx.

Refer to [VXC guide](https://developers.telnyx.com/docs/network/vxc/intro) for more detail.
