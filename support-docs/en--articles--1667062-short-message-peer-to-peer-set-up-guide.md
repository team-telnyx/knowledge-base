---
source_url: https://support.telnyx.com/en/articles/1667062-short-message-peer-to-peer-set-up-guide
title: "Short Message Peer-to-Peer Set-up Guide"
description: "SMPP is great for customers that require a high throughput. See Telnyx guidance and requirements Learn more about Short Message Peer-to-Peer Set-up Guide with."
scraped: 2026-07-08
content_hash: 0cbac626016d0e25a6fae97c1a37f85c01eff273aaad2fa3d0aa8d229754e781
---







# Short Message Peer-to-Peer Set-up Guide

SMPP is great for customers that require a high throughput. See Telnyx guidance and requirements Learn more about Short Message Peer-to-Peer Set-up Guide with.




## SMPP Overview

The Short Message Peer-to-Peer Protocol is a widely used protocol for SMS delivery and receipt. SMPP is best utilized by customers that require high throughput. The following guide is designed to help you establish an SMPP bind and initiate your SMS campaigns.

This feature is reserved for contracted Telnyx customers only who can commit to $5000 minimum spend per month for a period of 12 months. Please liaise with your account manager or sales rep for assistance on getting set up.
​

## SMPP Hosts

Telnyx provides users a primary SMPP server, which must be connected with over TLS.

![SMPP Hosts value table. ](_images/f8f40892abfebc24.png)

In the future, Telnyx will offer both a primary and secondary server. Once available, Telnyx will only guarantee that one of the servers is up at anytime, and it will be highly recommended that customers connect to both in order to avoid service outages.
​

## Username and password

Your username and password will be provided by your Telnyx account manager. You can request one by providing the ID of the Messaging Profile you intend to utilize for SMPP messaging. You can find your Messaging Profile ID by navigating to [Messaging](https://portal.telnyx.com/#/app/messaging), open settings for the messaging profile to be used (Basic, Inbound or Outbound), and the Messaging Profile ID will be at the bottom of the pop-up screen.
​

## Throughput per number

Throughput per number varies by number type.  Messages over Long Code numbers can be delivered at 10 messages per number per minute, while messages over toll-free can be delivered at 1200 message per number per minute.
​

## **Binding - Supported PDUs**

Telnyx supports the following PDUs

* bind\_transmitter
* bind\_transceiver
* bind\_receiver
* unbind
* submit\_sm
* deliver\_sm
* enquire\_link

## **Binding - Required Parameters**

* system\_id = Telnyx provided
* password = Telnyx provided
* Host = smpp.telnyx.com
* Port = 2775
* SSL = yes
* addr\_ton = 1  (International)
* addr\_npi = 1 (ISDN/telephone numbering plan (E163/E164)

---

Related Articles

[Rate Limits for Messaging](https://support.telnyx.com/en/articles/96934-rate-limits-for-messaging)[Setting Up a Messaging Profile](https://support.telnyx.com/en/articles/3562059-setting-up-a-messaging-profile)[Textable Setup Guide](https://support.telnyx.com/en/articles/3685327-textable-setup-guide)[Telnyx Messaging Error Codes](https://support.telnyx.com/en/articles/6505121-telnyx-messaging-error-codes)[Messaging in Mission Control](https://support.telnyx.com/en/articles/8219294-messaging-in-mission-control)

Did this answer your question?

😞😐😃
