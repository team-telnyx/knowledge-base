---
title: Telnyx SIP Connection Configuration Guide
summary: This page consolidates Telnyx guidance on configuring SIP connections, including
  IP and credentials-based authentication, failover and retry behavior, multi-device
  registration, tech prefixes, X-Telnyx-Token authentication, P-Charge-Info headers,
  and PBX-specific setup examples for FreePBX, FreeSWITCH, and FusionPBX.
sources:
- url: https://support.telnyx.com/en/articles/1130715-register-multiple-devices-on-one-connection
- url: https://support.telnyx.com/en/articles/1176364-sip-connection-failover-guide-ip-fqdn-based
- url: https://support.telnyx.com/en/articles/12580765-configure-p-charge-info-for-private-pbx-example-freepbx
- url: https://support.telnyx.com/en/articles/12580952-configure-token-authentication-header-x-telnyx-token-in-freepbx
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
- url: https://support.telnyx.com/en/articles/2602782-ip-authentication-with-tech-prefix
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
- url: https://support.telnyx.com/en/articles/4305158-api-keys-and-how-to-use-them
- url: https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries
- url: https://support.telnyx.com/en/articles/4860170-ip-authentication-with-x-telnyx-token
updated_at: 2026-08-05T13:32:19Z
---

# Telnyx SIP Connection Configuration Guide

*Part 3 of 5 — see also: [Part 1](telnyx-sip-connection-configuration-guide--part-1.md), [Part 2](telnyx-sip-connection-configuration-guide--part-2.md), [Part 4](telnyx-sip-connection-configuration-guide--part-4.md), [Part 5](telnyx-sip-connection-configuration-guide--part-5.md)*

This page consolidates Telnyx guidance on configuring SIP connections, including IP and credentials-based authentication, failover and retry behavior, multi-device registration, tech prefixes, X-Telnyx-Token authentication, P-Charge-Info headers, and PBX-specific setup examples for FreePBX, FreeSWITCH, and FusionPBX.

## FreeSWITCH IP Trunk Setup

[FreeSWITCH](https://signalwire.com/freeswitch) is a scalable open source cross-platform telephony suite designed to route and interconnect popular communication protocols using audio, video, text, or any other form of media. It runs on everything from a Raspberry Pi to a multi-core server.

> **IMPORTANT:** FreeSWITCH v1.8 has been tagged End of Life. If you are on this version, you must upgrade.

### Pre-requisites

- [Download](https://files.freeswitch.org/freeswitch-releases/) and [install](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Installation/) FreeSWITCH
- Configure the Telnyx Mission Control Portal following the [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- Create an [IP connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned to a DID and outbound profile

### Step 1: Configure the Telnyx Mission Control Panel

Follow the [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) for step-by-step instructions on each requirement.

### Step 2: Update Default Credentials

Your new FreeSWITCH instance is preconfigured with default credentials that must be changed to prevent unauthorized access.

1. Open `vars.xml`:
   ```
   root@ip-172-31-54-222:/# cd /usr/local/freeswitch/conf
   root@ip-172-31-54-222:/usr/local/freeswitch/conf# vi vars.xml
   ```
2. Find the line that begins with `<X-PRE-PROCESS cmd="set" data="default_password="`
3. Change the default password.

### Step 3: Update the External SIP Profile

1. Navigate to `sip_profiles/external.xml`:
   ```
   ...# cd sip_profiles
   .../sip_profiles# vi external.xml
   ```
2. Uncomment the following lines:
   ```
   <param name="ext-rtp-ip" value="$${external_rtp_ip}"/>
   <param name="ext-sip-ip" value="$${external_sip_ip}"/>
   ```

### Step 4: Create the SIP Trunk to Telnyx

Create a gateway under the external SIP profile at `sip_profiles/external/telnyx.xml`:

```
<include>
<gateway name="telnyx">
<param name="proxy" value="sip.telnyx.com"/>
<param name="register" value="false"/>
<param name="caller-id-in-from" value="true"/>
<param name="username" value="not-used"/>
<param name="password" value="not-used"/>
</gateway>
</include>
```

### Step 5: Create a Dialplan

Navigate to `/usr/local/freeswitch/conf/dialplan/public`, remove the files there, and create a new inbound dialplan XML. Example:

```
<include>
  <extension name="public_did">
    <condition field="destination_number" expression="^(1{0,1}\d{10})$">
      <action application="set" data="effective_caller_id_number=13125489677"/>
      <!-- Replace 3125489677 with the DID you want as CID -->
      <action application="bridge" data="sofia/gateway/telnyx/$1"/>
    </condition>
  </extension>

  <extension name="local.com">
    <condition field="destination_number" expression="^(\d{7})$">
      <action application="set" data="effective_caller_id_number=${outbound_caller_id_number}"/>
      <action application="set" data="effective_caller_id_name=${outbound_caller_id_name}"/>
      <action application="bridge" data="sofia/gateway/telnyx/+1${default_areacode}$1"/>
    </condition>
  </extension>

  <extension name="domestic.com">
    <condition field="destination_number" expression="^(\d{11})$">
      <action application="set" data="effective_caller_id_number=${outbound_caller_id_number}"/>
      <action application="set" data="effective_caller_id_name=${outbound_caller_id_name}"/>
      <action application="bridge" data="sofia/gateway/telnyx/+$1"/>
    </condition>
  </extension>

  <extension name="international.com">
    <condition field="destination_number" expression="^(011\d+)$">
      <action application="set" data="effective_caller_id_number=${outbound_caller_id_number}"/>
      <action application="set" data="effective_caller_id_name=${outbound_caller_id_name}"/>
      <action application="bridge" data="sofia/gateway/telnyx/+$1"/>
    </condition>
  </extension>
</include>
```

### Step 6: Network Configuration

To use the same profile for communication both inside and outside your network, tell FreeSWITCH when to use the local IP versus the external IP. The `autonat:` prefix toggles on the usage of the `local-network-acl`:

```
<param name="ext-sip-ip" value="autonat:$${external_sip_ip}"/>
```

If FreeSWITCH fails to recognize your public IP, force a static public IP in `sip_profiles/external.xml`:

```
<param name="ext-rtp-ip" value="8.8.8.8"/>
<param name="ext-sip-ip" value="8.8.8.8"/>
<!-- Replace 8.8.8.8 with your public IP -->
```

## FreeSWITCH Credentials Trunk

> **IMPORTANT:** FreeSWITCH v1.8 has been tagged End of Life. If you are on this version, you must upgrade.

### Pre-requisites

- [Download](https://files.freeswitch.org/freeswitch-releases/) and [install](https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Installation/) FreeSWITCH
- Configure the Telnyx Mission Control Portal following the [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
- Create a [credentials-based connection](https://portal.telnyx.com/#/app/connections) on your Telnyx Mission Control Portal account, assigned to a DID and outbound profile

### Step 1: Extension Configuration for Registering a SIP Phone

You may register to one of the existing extensions; however, it is recommended that you change the default password in the `directory/default/1000.xml` file:

```
<param name="password" value="abcd1234"/>
<!-- Replace abcd1234 with a strong password -->
```

### Step 2: Create the SIP Trunk

Create a file under `sip_profiles/external` (for example, `sip_profiles/external/telnyx.xml`):

> **Note:** If you have a Linksys device (SPA2102, SPA5xx series), it will reject calls if ptime is not set to 20. Make sure to change that in the phone's configuration (RTP packet size 0.020 [from 0.030]).

```
<include>
  <gateway name="telnyx">
    <param name="realm" value="sip.telnyx.com"/>
    <param name="username" value="freesuser"/>
    <!-- Replace freesuser with your Telnyx Portal username -->
    <param name="password" value="freespass"/>
    <!-- Replace freepass with your Telnyx Portal password -->
    <param name="register" value="true"/>
  </gateway>
</include>
```

### Step 3: Create a Dialplan

Edit `dialplan/default.xml` and add:

```
<extension name="dial">
  <condition field="destination_number" expression="^(1{0,1}\d{10})$">
    <action application="set" data="effective_caller_id_number=13125489677"/>
    <!-- Replace 3125489677 with the DID you want as CID -->
    <action application="bridge" data="sofia/gateway/telnyx/$1"/>
  </condition>
</extension>
```

### Step 4: Create an Inbound Trunk (DID)

Create a file under `dialplan/public/` (for example, `dialplan/public/3125489677.xml`, where 3125489677 is the DID you purchased):

```
<include>
  <extension name="public_did">
    <condition field="destination_number" expression="^(13125489677)$">
    <!-- Replace 13125489677 with the DID you purchased at the Telnyx Portal -->
      <action application="set" data="domain_name=$${domain}"/>
      <action application="transfer" data="1000 XML default"/>
    </condition>
  </extension>
</include>
```

### Step 5: Configure Your Network

Use the `autonat:` prefix to toggle the `local-network-acl`:

```
<param name="ext-sip-ip" value="autonat:$${external_sip_ip}"/>
```

If FreeSWITCH fails to recognize your public IP, force a static public IP in `sip_profiles/external.xml`:

```
<param name="ext-rtp-ip" value="8.8.8.8"/>
<param name="ext-sip-ip" value="8.8.8.8"/>
<!-- Replace 8.8.8.8 with your public IP -->
```
