---
source_url: https://support.telnyx.com/en/articles/4194697-oracle-acme-packet-sbc-setup
title: "Oracle: Acme Packet SBC Setup"
description: "Master Oracle's Acme Packet SBC configuration with Telnyx - Dive In Now! See Telnyx guidance and requirements."
scraped: 2026-07-08
content_hash: 0422e5bf45abeed5643ca0700571e1703339ea4558f8033cb8dcde1441d6db65
---







# Oracle: Acme Packet SBC Setup

Master Oracle's Acme Packet SBC configuration with Telnyx - Dive In Now! See Telnyx guidance and requirements.

C




[Jump to Instructions](#h_32f70a98cb)

The wide range of [Acme Packet platforms](https://www.oracle.com/industries/communications/acme-packet-platforms/) is designed to help customers deliver trusted, real-time communications across internet protocol (IP) network borders based on their different needs for performance and capacity.

Additional resources:

* [Acme SBC user guide](https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/GUID-3D090BC0-31D0-419D-A1F9-E7B1E5D3D55D.htm)

---

## Instructions for Configuring an Edge SBC with Telnyx

In this activity you will:

1. [Configure your SIP trunk](#h_49fe8134c7)
2. [Configure your session agent towards Telnyx](#h_08e76d29ca)
3. [Configure number translation](#h_4921a64206)
4. [Configure codecs](#h_7e08b4a28a)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* [Purchase a DID](https://portal.telnyx.com/#/app/numbers/search-numbers)
* [Set up your Telnyx SIP connection](https://portal.telnyx.com/#/app/connections)
* [Provision your number](https://portal.telnyx.com/#/app/numbers/my-numbers) (Assign it to a SIP connection)
* [Create an outbound voice profile](https://portal.telnyx.com/#/app/outbound)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)
* Have the SBC set up with your IP-PBX, with one or more clients configured and running calls between them

**Video Walk-through**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Acme Packet SBC/Telnyx configuration coming soon. Check back as we update our docs.* |

## **1. Configure your SIP trunk**

In this section, you'll configure your [SIP trunk](https://telnyx.com/products/sip-trunks) interface. A parameter reference is available below the code snippets. To view all sip-interface parameters, enter a **?** at the system prompt.
​

### **Configure Terminal Steps:**

1. In superuser mode, type *configure terminal* and press "**Enter"**.

   ```
   ORACLE# configure terminal
   ```
2. Type *session-router* and press "**Enter"** to access the system-level configuration elements.

   ```
   ORACLE(configure)# session-router
   ```
3. Type *sip-interface* and press "**Enter"**. The system prompt changes to let you know that you can begin configuring individual parameters.

   ```
   ORACLE(session-router)# sip-interface
   ORACLE(sip-interface)#
   ```
4. Use the following configuration parameters as a guide:

   ```
   sip-interface
   state                enabled
   realm-id             OUTSIDE
   description
   sip-port
   address              X.X.X.X
   port                 5060
   transport-protocol   UDP
   tls-profile
   allow-anonymous      agents-only
   ims-aka-profile
   carriers
   trans-expire         0
   ...
   ```

   * #### **state:**

     Enable or disable the SIP interface. The default is "**enabled"**. The valid values are:

     + enabled | disabled
   * #### **realm-id**:

     Enter the name of the realm to which the SIP interface is connected.
   * #### **sip-ports**:

     Access the "**sip-ports"** subelement.
   * #### **address**:

     Enter the IP address of the host associated with the sip-port entry on which to listen. For example:

     ```
     192.168.11.101
     ```
   * #### **port**:

     Enter the port number you want to use for this sip-port. The default is **"5060"**. The valid range is:

     + Minimum—1025
     + Maximum—65535
   * #### **transport-protocol**:

     Indicate the transport protocol you want to associate with the SIP port. The default is "**UDP"**. The valid values are:

     + **TCP**—Provides a reliable stream delivery and virtual connection service to applications through the use of sequenced acknowledgment with the retransmission of packets when necessary.
     + **UDP**—Provides a simple message service for transaction-oriented services. Each UDP header carries both a source port identifier and destination port identifier, allowing high-level protocols to target specific applications and services among hosts.
     + **TLS**—See the Security chapter for more information about configuring TLS.
   * #### **allow-anonymous**:

     Define the allow anonymous criteria for accepting and processing a SIP request from another SIP element.

     The anonymous connection mode criteria includes admission control based on whether an endpoint has successfully registered. Requests from an existing SIP dialog are always accepted and processed. The default is **all**.

     The following table lists the available options.

     + **all**—All requests from any SIP element are allowed.
     + **agents-only**—Only requests from configured session agents are allowed. The session agent must fit one of the following criteria:

       - Have a global realm.
       - Have the same realm as the SIP interface
       - Be a sub-realm of the SIP interface’s realm.

         When an agent that is not configured on the system sends an INVITE to a SIP interface, the Oracle® Enterprise Session Border Controller:
       - Refuses the connection in the case of TCP.
       - Responds with a 403 Forbidden in the case of UDP.
     + **realm-prefix**—The source IP address of the request must fall within the realm’s address prefix or a SIP interface sub-realm. A sub-realm is a realm that falls within a realm-group tree. The sub-realm is a child (or grandchild, and so on) of the SIP interface realm.

       Only realms with non-zero address prefixes are considered. Requests from session agents (as described in the **agents-only** option) are also allowed.
     + **registered**—Only requests from user agents that have an entry in the registration cache (regular or HNT) are allowed; with the exception of a REGISTER request. A REGISTER request is allowed from any user agent.

       The registration cache entry is only added if the REGISTER is successful. Requests from configured session agents (as described in the **agents-only** option) are also allowed.
     + **register-prefix**—Only requests from user agents that have an entry in the Registration Cache (regular or HNT) are allowed; with the exception of a REGISTER request. A REGISTER request is allowed only when the source IP address of the request falls within the realm address-prefix or a SIP interface sub-realm. Only realms with non-zero address prefixes are considered.

       The Registration Cache entry is only added if the REGISTER is successful. Requests from configured session agents (as described in the **agents-only** option) are also allowed.
   * #### **carriers**:

     Enter the list of carriers related to the SIP interface.

     Entries in this field can be from 1 to 24 characters in length and can consist of any alphabetical character (Aa-Zz), numerical character (0-9), or punctuation mark (! ”$ % ^ & \* ( ) + - = < > ? ‘ | { } [ ] @ / \ ‘ ~ , . \_ : ; ) or any combination of alphabetical characters, numerical characters, or punctuation marks. For example, both 1-0288 and acme\_carrier are valid carrier field formats
   * #### **trans-expire**:

     Set the TTL expiration timer in seconds for SIP transactions. This timer controls the following timers specified in RFC 3261:

     + Timer B—SIP INVITE transaction timeout
     + Timer F—non-INVITE transaction timeout
     + Timer H—Wait time for ACK receipt
     + Timer TEE—Used to transmit final responses before receiving an ACK

       The default is **0**. If you leave this parameter set to the default, then the Oracle® Enterprise Session Border Controller uses the timer value from the global SIP configuration. The valid range is:
     + Minimum—0
     + Maximum—999999999

[Back to Top](#h_32f70a98cb)

## 2. Configure your Session Agent towards Telnyx:

### **Configure Terminal Steps**

1. In superuser mode, type *configure terminal* and press "**Enter"**.

   ```
   ORACLE# configure terminal
   ```
2. Type *session-router* and press "**Enter"** to access the system-level configuration elements.

   ```
   ORACLE(configure)# session-router
   ```
3. Type *sip-interface* and press "**Enter"**. The system prompt changes to let you know that you can begin configuring individual parameters.

   ```
   ORACLE(session-router)# session-agent
   ORACLE(sip-interface)#
   ```
4. Use the following configuration parameters as a guide:

   ```
   session-agent
   hostname              sip.telnyx.com
   ip-address
   port                  5060
   state enabled
   app-protocol          SIP
   app-type
   transport-method      UDP
   realm-id              OUTSIDE
   egress-realm-id
   description           Telnyx
   carriers
   allow-next-hop-lp     enabled
   constraints           disabled
   ...
   ```

   * #### **hostname**:

     Enter the name of the host associated with the session agent in either hostname or FQDN format, or as an IP address.
     ​
     If you enter the host name as an IP address, you do not have to enter an IP address in the optional IP address parameter. If you enter the host name in FQDN format, and you want to specify an IP address, enter it in the optional IP address parameter. Otherwise you can leave the IP address parameter blank to allow a DNS query to resolve the host name.
     ​
     If the initial DNS query for the session agent fails to get back any addresses, the session agent is put out-of-service. When session agent is pinged, the DNS query is repeated. The ping message is not sent until the DNS query gets back one or more IP addresses. After the query receives some addresses, the ping message is sent. The session agent remains out of service until one of the addresses responds.
     ​
     ​***Note:*** *The value you enter here must be unique to this session agent. No two session agents can have the same hostname.*
     ​
     The hostnames established in the session agent populate the corresponding fields in other elements.
   * #### **ip-address**:

     Optional. Enter the IP address for the hostname you entered in FQDN format if you want to specify the IP address. Otherwise, you can leave this parameter blank to allow a DNS query to resolve the host name.
   * #### **port**:

     Enter the number of the port associated with this session agent. Available values include:

     + zero (0)—If you enter zero (0), the Oracle® Enterprise Session Border Controller will not initiate communication with this session agent (although it will accept calls).
     + 1025 through 65535

       The default value is **5060**.

       Note:

       If the transport method value is TCP, the Oracle® Enterprise Session Border Controller will initiate communication on that port of the session agent.
   * #### **state**:

     Enable or disable the session agent by configuring the state. By default, the session agent is **enabled**.

     + enabled | disabled
   * #### **app-protocol**:

     Enter the protocol on which you want to send the message. The default value is **SIP**. Available values are:

     + SIP | H.323
   * #### **app-type**:

     If configuring H.323, indicate whether the application type is a gateway or a gatekeeper. Available values include:

     + **H.323-GW**—gateway
     + **H.323-GK**—gatekeeper
   * #### **transport-method**:

     Indicate the IP protocol to use (transport method) to communicate with the session agent. **UDP** is the default value. The following protocols are supported:

     + **UDP**—Each UDP header carries both a source port identifier and destination port identifier, allowing high-level protocols to target specific applications and services among hosts.
     + **UDP+TCP**—Allows an initial transport method of UDP, followed by a subsequent transport method of TCP if and when a failure or timeout occurs in response to a UDP INVITE. If this transport method is selected, INVITEs are always sent through UDP as long as a response is received.
     + **DynamicTCP**—dTCP indicates that dynamic TCP connections are the transport method for this session agent. A new connection must be established for each session originating from the session agent. This connection is torn down at the end of a session.
     + **StaticTCP**—sTCP indicates that static TCP connections are the transport method for this session agent. Once a connection is established, it remains and is not torn down.
     + **DynamicTLS**—dTLS indicates that Dynamic TLS connections are the transport method for this session agent. A new connection must be established for each session originating from the session agent. This connection is torn down at the end of a session.
     + **StaticTLS**—sTLS indicates that Static TLS connections are the transport method for this session agent. Once a connection is established, it will remain and not be torn down.
   * #### **realm-id**:

     Optional. Indicate the ID of the realm in which the session agent resides.

     The realm ID identifies the realm for sessions coming from or going to this session agent. For requests coming from this session agent, the realm ID identifies the ingress realm. For requests being sent to this session agent, the realm ID identifies the egress realm. In a Oracle® Enterprise Session Border Controller, when the ingress and egress realms are different, the media flows must be steered between the realms.

     + no value: the egress realm is used unless the local policy dictates otherwise
     + asterisk (\*): keep the egress realm based on the Request URI

       Note:

       The realm ID you enter here must match the valid identifier value entered when you configured the realm.
   * #### **description**:

     Optional. Enter a descriptive name for this session agent.
   * #### **carriers**:

     Optional. Add the carriers list to restrict the set of carriers used for sessions originating from this session agent.

     Carrier names are arbitrary names that can represent specific service providers or traditional PSTN telephone service providers (for sessions delivered to gateways). They are global in scope, especially if they are exchanged in TRIP. Therefore, the definition of these carriers is beyond the scope of this documentation.

     You could create a list using carrier codes already defined in the North American Numbering Plan (NANP); or those defined by the local telephone number or carrier naming authority in another country.

     Note:

     If this list is empty, any carrier is allowed. If it is not empty, only local policies that reference one or more of the carriers in this list will be applied to requests coming from this session agent.
   * #### **allow-next-hop-lp**:

     Indicate whether this session agent can be used as a next hop in the local policy.

     If you retain the default value of **enabled**, the session agent can be used as the next hop for the local policy. Valid values are:

     + enabled | disabled
   * #### **constraints**:

     Enable this parameter to indicate that the individual constraints you configure in the next step are applied to the sessions sent to the session agent. Retain the default value of **disabled** if you do not want to apply the individual constraints. Valid values are:

     + enabled | disabled

       Note:

       In general, session control constraints are used for SAGs or SIP proxies outside or at the edge of a network.

[Back to Top](#h_32f70a98cb)

## 3. Configure number translation

In this section, you will configure number translation. E.164 Number Mapping, or ENUM, is a way to translate the standard format for telephone numbers to something more Internet friendly. To learn more about the mechanics of number translation, see [Oracle's documentation on the subject](https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/GUID-439344DD-1B25-47E2-974D-56B59A06CB27.htm).

The example we provide helps append a **+1** for US calling numbers. This is the session translation rule on the calling number.

|  |
| --- |
| ***Note:*** *Telnyx accepts the called number on outbound calls in 10 digit, 11 digit and +11 digit format, so there is no need to modify rules for the called number. However, we have a [caller ID policy](https://support.telnyx.com/en/articles/3546251-caller-id-number-policy) and require the calling number to be in +E.164 number format.* |

### **Terminal Steps:**

1. In superuser mode, Type *session-router* and press "**Enter"** to access the system-level configuration elements.

```
ORACLE(configure)# session-router
```

2. Now type *session-translation* and press "**Enter"**.

```
ORACLE(session-router)# session-translation
ORACLE(session-translation)#
```

3. Use the following configuration parameters as a guide. To view all session translation parameters, enter a **?** at the system prompt.

```
session-translation
id                    includeCallingPlus
rules-calling         includePlus
rules-called
```

* **ID**: Choose a descriptive name for this session translation.
* **rules-calling**: Enter the rules calling in the order in which they should be applied. Multiple rules should be put in quotes and separated by spaces.
* **rules-called**: Enter the rules called in the order in which they should be applied. Multiple rules should be included in quotes and separated by spaces.

4. In superuser mode, from *session-router,* type *translation-rules* and press "**Enter"**.

```
ORACLE(session-router)# translation-rules
ORACLE(session-translation)#
```

5. Use the following configuration parameters as a guide. To view all session translation parameters, enter a "**?"** at the system prompt. Then define the rule to append "**+1"** to the calling number:

```
translation-rules
id                    includePlus
type                  add
add-string            +1
add-index             0
delete-string
delete-index          0
```

#### Properties Description:

* **ID**:Set a descriptive ID name for this translation rule.
* **type**:Set the type of translation rule you want to configure. The default value is **none**. The valid values are:

  + **add**—Adds a character or string of characters to the address
  + **delete**—Deletes a character or string of characters from the address
  + **replace**—Replaces a character or string of characters within the address
  + **none**—Translation rule is disabled
* **add-string**: Enter the string to be added during address translation to the original address. The value in this field should always be a real value; i.e., this field should not be populated with at-signs (@) or dollar-signs ($). The default value is a blank string.
* **add-index**: Enter the position, 0 being the left most position, where you want to add the string defined in the **add-string** parameter. The default value is zero (**0**). The valid range is:

  + Minimum—0
  + Maximum—999999999
* **delete-string**: Enter the string to be deleted from the original address during address translation. Unspecified characters are denoted by the at-sign symbol (@).

  The @ character only works if the type parameter is set to delete. This parameter supports wildcard characters or digits only. For example, valid entries are: delete-string=@@@@@, or delete-string=123456. An invalid entry is delete-string=123@@@. When the type is set to replace, this value is used in conjunction with the add-string value. The value specified in the delete-string field is deleted and the value specified in the add-string field is inserted. If no value is specified in the delete-string parameter and the type field is set to replace, then nothing will be inserted into the address. The default value is a blank string.
* **delete-index**: Enter the position, 0 being the left most spot, where you want to delete the string defined in the **delete-string** parameter. This parameter is only used if the **delete-string** parameter is set to one or more at-signs. The default value is zero (**0**). The valid range is:

  + Minimum—0
  + Maximum—999999999

6. Then apply the translation rule to take effect on the outside realm:

```
realm-config
identifier            OUTSIDE
...
in-translationid
out-translationid     includeCallingPlus
...
```

[Back to Top](#h_32f70a98cb)

## 4. Configure codecs

In the ACME SBC, you can set your [codec policy](https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/GUID-49ECD7A3-8663-44ED-ADD4-EB01B76CC527.htm#GUID-9CEACADB-5A28-4367-9B7B-813C75F11289) as you wish. Please see a list of supported codecs on our [website](https://sip.telnyx.com/#codecs).
​

In the example below, the SBC will change the codec list for all **clients** that make outbound calls through the SBC's realm, such that PCMU will be preferred codec offered.

```
realm-config
identifier             clients
...
options                preferred-codec=PCMU
...
```

[Back to Top](#h_32f70a98cb)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Acme SBC user guide](https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/GUID-3D090BC0-31D0-419D-A1F9-E7B1E5D3D55D.htm)

---

Related Articles

[Configuring a Cisco CUBE/CUCM SIP Trunk](https://support.telnyx.com/en/articles/1130673-configuring-a-cisco-cube-cucm-sip-trunk)[Audiocodes SBC: Setup](https://support.telnyx.com/en/articles/4194841-audiocodes-sbc-setup)[Ribbon: EdgeMarc 6000 Setup](https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup)[Sansay: SBC VSXi Setup](https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup)[Fanvil A32i: Telnyx Setup](https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup)

Did this answer your question?

😞😐😃
