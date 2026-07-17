---
title: Telnyx SIP, Fax, and PBX Configuration
summary: This page consolidates Telnyx support documentation covering fax service
  setup and error handling (T.38 and G.711), Programmable Fax API webhook and CDR
  error codes, FreeSWITCH and FusionPBX trunk configuration, SIP Trunking FIPS support,
  and the meaning of SIP 603+ carrier rejections.
sources:
- url: https://support.telnyx.com/en/articles/1130672-fax-service-with-telnyx-via-t-38-or-g711
- url: https://support.telnyx.com/en/articles/15374685-telnyx-sip-trunking-fips-support
- url: https://support.telnyx.com/en/articles/15395095-understanding-sip-603-carrier-rejections
- url: https://support.telnyx.com/en/articles/1616935-freeswitch-ip-trunk-setup
- url: https://support.telnyx.com/en/articles/1618801-freeswitch-credentials-trunk
- url: https://support.telnyx.com/en/articles/3220393-fusionpbx-telnyx-credentials
- url: https://support.telnyx.com/en/articles/4967498-fax-api-error-list
- url: https://support.telnyx.com/en/collections/3968239-telnyx-fax-configuration-errors
updated_at: 2026-07-17T09:05:45Z
---

# Telnyx SIP, Fax, and PBX Configuration

*Part 2 of 5 — see also: [Part 1](telnyx-sip-fax-and-pbx-configuration--part-1.md), [Part 3](telnyx-sip-fax-and-pbx-configuration--part-3.md), [Part 4](telnyx-sip-fax-and-pbx-configuration--part-4.md), [Part 5](telnyx-sip-fax-and-pbx-configuration--part-5.md)*

This page consolidates Telnyx support documentation covering fax service setup and error handling (T.38 and G.711), Programmable Fax API webhook and CDR error codes, FreeSWITCH and FusionPBX trunk configuration, SIP Trunking FIPS support, and the meaning of SIP 603+ carrier rejections.

## FreeSWITCH IP Trunk Setup

[FreeSWITCH](https://signalwire.com/freeswitch) is a scalable, open source, cross-platform telephony suite that routes and interconnects popular communication protocols using audio, video, text, or other media. It runs from a Raspberry Pi to a multi-core server.

FreeSWITCH v1.8 has reached End of Life and must be upgraded.

### Prerequisites

- Download and install FreeSWITCH.
- Configure the Telnyx Mission Control Portal.
- Create an IP connection in Mission Control, and assign it to a DID and outbound profile so calls can be made and received.

### Configure the Telnyx Mission Control Panel

Follow the [Get started with a Mission Control account](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) guide to configure the account.

### Update Default Credentials

The default credentials on a new FreeSWITCH instance must be changed to prevent unauthorized registration and toll fraud.

1. Open `vars.xml`:
   ```
   root@ip-172-31-54-222:/# cd /usr/local/freeswitch/conf
   root@ip-172-31-54-222:/usr/local/freeswitch/conf# vi vars.xml
   ```
2. Find the line beginning with `<X-PRE-PROCESS cmd="set" data="default_password="`.
3. Change the default password.

### Update the External SIP Profile

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

### Create the SIP Trunk

The easiest approach is to build a gateway under the external SIP profile.

1. Navigate to `sip_profiles/external/telnyx.xml`:
   ```
   .../sip_profiles# cd external
   .../sip_profiles/external# vi telnyx.xml
   ```
2. Configure the gateway:
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

### Create a Dialplan

This is a sample dialplan; each dialplan is typically unique. See FreeSWITCH's documentation for more detail.

1. Navigate to `/usr/local/freeswitch/conf/dialplan/public`.
2. Remove the files there and create a new inbound dialplan XML. Example:
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

### Network Configuration

To use the same profile for both internal and external communication, FreeSWITCH must know when to use the local IP versus the external IP. The `autonat:` prefix toggles the use of `local-network-acl`, enabling dynamic selection between `ext-rtp-ip` and `rtp-ip` based on ACL match:

```
<param name="ext-sip-ip" value="autonat:$${external_sip_ip}"/>
```

If FreeSWITCH fails to recognize the public IP, force a static public IP in `sip_profiles/external.xml`:

```
<param name="ext-rtp-ip" value="8.8.8.8"/>
<param name="ext-sip-ip" value="8.8.8.8"/>
<!-- Replace 8.8.8.8 with your public IP -->
```

## FreeSWITCH Credentials Trunk

A credentials-based trunk registers FreeSWITCH with Telnyx using a username and password rather than an IP allowlist.

### Prerequisites

- Download and install FreeSWITCH.
- Configure the Telnyx Mission Control Portal.
- Create a credentials-based connection in Mission Control, and assign it to a DID and outbound profile so calls can be made and received.

### Extension Configuration

Register to one of the existing extensions, but it is recommended to change the default password in `directory/default/1000.xml`:

```
<param name="password" value="abcd1234"/>
<!-- Replace abcd1234 with a strong password -->
```

### Create the SIP Trunk

Create a file at `sip_profiles/external/telnyx.xml`:

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

Linksys SPA2102 and SPA5xx devices reject calls if `ptime` is not set to 20. Set the RTP packet size to 0.020 (from 0.030) in the phone's configuration.

### Create a Dialplan

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

### Create an Inbound Trunk (DID)

Create a file at `dialplan/public/3125489677.xml` (replace `3125489677` with the DID purchased in Mission Control):

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

### Network Configuration

Use the same `autonat:` prefix and static-IP fallback described in the IP trunk setup above.
