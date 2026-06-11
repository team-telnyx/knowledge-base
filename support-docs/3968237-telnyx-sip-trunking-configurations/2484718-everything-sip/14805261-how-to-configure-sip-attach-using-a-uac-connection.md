---
source_url: https://support.telnyx.com/en/articles/14805261-how-to-configure-sip-attach-using-a-uac-connection
scraped: 2026-06-11
---

How to Configure SIP Attach using a UAC Connection | Telnyx Help Center

[Skip to main content](#main-content)

# How to Configure SIP Attach using a UAC Connection

Written by Telnyx Engineering

Updated today

Table of contents

SIP Attach lets Telnyx register as a SIP endpoint on your existing PBX or voice system. This gives your Telnyx resource, such as an AI Assistant, Call Control Application, or SIP-enabled application, native PBX presence.  
​  
Under the hood, SIP Attach is configured using a UAC (User Agent Client) Connection. With a UAC Connection, Telnyx registers to your PBX as an extension, so internal callers can reach the Telnyx resource without routing through the PSTN.  
​  
This helps reduce latency and cost while making it easier to connect employee-facing voice agents, internal support flows, and other SIP-enabled Telnyx applications to your existing voice infrastructure.

---

## **How UAC differs from FQDN connections**

If you are setting up SIP Attach, the key concept to understand is that the SIP registration direction is reversed compared with traditional FQDN or IP-authenticated SIP connections.

Before you begin, it helps to understand the directional difference:

* **FQDN / IP connections:** Your PBX registers to Telnyx, or Telnyx accepts calls from your PBX based on IP Authentication. Telnyx is the server (UAS) and the PBX the client (UAC).
* **UAC connections:** Telnyx registers to your PBX as an extension. Your PBX is the server (UAS) and Telnyx the client (UAC).

This affects how inbound calls are routed (covered in Step 2) and what you need to configure on the PBX side.

---

# Before You Start

### What you need from your PBX (customer side)

Before creating a UAC Connection, collect the following from your PBX administrator or PBX management console:

|  |  |
| --- | --- |
| **Item** | **Notes** |
| **SIP username and password** | Credentials for the extension Telnyx will register as |
| **SIP proxy address** | Where Telnyx sends SIP REGISTER requests (e.g., pbx.example.com:5060) |
| **Transport protocol** | UDP, TCP, or TLS — must match your PBX |
| **Auth username** *(if different)* | Some PBX systems use a separate username for SIP digest auth |
| **Outbound proxy** *(if applicable)* | If your network routes SIP through an intermediary |
| **From User** *(if applicable)* | If your PBX requires a specific caller identity in the SIP From header |

### What you need to configure on your PBX (customer side)

On your PBX, you must:

1. Create a SIP extension that Telnyx will register as (e.g., extension 1001)
2. Allowlist Telnyx signaling IPs — your PBX must accept SIP REGISTER and INVITE requests from Telnyx's IP ranges.

   1. For SIP UAC registrations, Telnyx currently sends REGISTER requests from 192.76.120.14. Allowlist this IP on your PBX/firewall for SIP signaling.

### What you need on the Telnyx side

* A Telnyx account
* Telnyx resource (such as a Call Control Application, AI Assistant, or SIP-enabled application) that will handle calls on this connection.
* UAC Connections follow the same per-account connection limits as other SIP Connection types in the Mission Control Portal.

---

## Step 1 — Select Connection Type

1. Navigate to Voice → SIP Trunking → Create SIP Connection in the Mission Control Portal.
2. Select the UAC (User Agent Client) tile (marked BETA).
4. Enter a Name for your connection (e.g., PBX-uac).
5. Click Next.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2328640891/74b392bc2bbb25355ea7967a998d/e5d9d9ae-85cb-4ab8-884b-7d57de05262c?expires=1781222400&signature=90bdbcd084fb2c9df0b9834273a789baf0f1b16b285085433a709492d06c65e8&req=diMlHs96nYlWWPMW3nq%2BgWh1Wc28VG7X5gpz31btBplHF4vL0okCasLI6OGr%0AOmkQTAAPje0zm73O7PzC69qOovQ%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2328640891/74b392bc2bbb25355ea7967a998d/e5d9d9ae-85cb-4ab8-884b-7d57de05262c?expires=1781222400&signature=90bdbcd084fb2c9df0b9834273a789baf0f1b16b285085433a709492d06c65e8&req=diMlHs96nYlWWPMW3nq%2BgWh1Wc28VG7X5gpz31btBplHF4vL0okCasLI6OGr%0AOmkQTAAPje0zm73O7PzC69qOovQ%3D%0A)

## Step 2 — Authentication and Routing

Step 2 has two sections: Internal UAC settings (Telnyx side) and External UAC settings (your PBX side).

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2328919501/846b97fb9a0681f5d1b8c833b632/11f8e5d1-42d1-4f70-9d86-97f05276fd46?expires=1781222400&signature=59dd56109e377cc728a3ddd77d792a32d3f293ac8bcbdfc3780129370a0a04ed&req=diMlHsB%2FlIRfWPMW3nq%2BgSktGSu2zt%2B6%2FnpvNqsaMAFSFaiTlCSqrGTIq9pp%0Aof6IoBn0ix25aMaOFXs0GA4Ys9E%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2328919501/846b97fb9a0681f5d1b8c833b632/11f8e5d1-42d1-4f70-9d86-97f05276fd46?expires=1781222400&signature=59dd56109e377cc728a3ddd77d792a32d3f293ac8bcbdfc3780129370a0a04ed&req=diMlHsB%2FlIRfWPMW3nq%2BgSktGSu2zt%2B6%2FnpvNqsaMAFSFaiTlCSqrGTIq9pp%0Aof6IoBn0ix25aMaOFXs0GA4Ys9E%3D%0A)

**Understanding the directional model**

A UAC connection handles calls in two directions, and two different fields govern each direction:

* **Telnyx → PBX (outbound):** uses the auto-generated **SIP Subdomain**
* **PBX → Telnyx (inbound):** uses the **Internal SIP URI** you configure

Keep this in mind as you fill out the Internal UAC settings below, the two fields aren't redundant, they handle opposite directions of traffic.

## Internal UAC settings (Telnyx side)

These fields define how Telnyx identifies this connection and how it handles inbound calls from the external peer.

|  |  |  |
| --- | --- | --- |
| **Field** | **Required** | **Description** |
| **SIP Subdomain** | Read-only | Auto-generated by Telnyx (`e.g., qqffqgf1rbok.sip.telnyx.com`). This is the address used for **outbound calls from Telnyx to your PBX**. You don't configure it, but it's the domain your PBX will see calls originate from. |
| **Receive SIP Subdomain calls** | Yes | Controls who can place calls to the subdomain. Defaults to **From Anyone**. When enabled, Telnyx accepts inbound SIP calls addressed to this subdomain and routes them to the Internal SIP URI below. |
| **Username** | Yes | Internal SIP username (Telnyx-side identity). |
| **Password** | Yes | Internal SIP password. |
| **Internal SIP URI** | Yes | The Telnyx SIP URI that receives **inbound calls from your PBX**. Can be any valid SIP URI in your Telnyx account — typically the URI of the AI Assistant or Call Control Application that should answer these calls. See the portal tooltip for format requirements. |

**Why the Internal SIP URI matters** Because Telnyx registers *to* your PBX (rather than the other way around), inbound calls arrive via the SIP subdomain.

The Internal SIP URI tells Telnyx where to deliver them, typically your AI Assistant or Call Control Application. If this is wrong, registration will succeed but calls won't route.

## External UAC settings (PBX side)

These fields configure how Telnyx registers with your external PBX.

|  |  |  |
| --- | --- | --- |
| **Username** | Yes | SIP username for authenticating with your PBX. |
| **Password** | Yes | SIP password for digest authentication. |
| **Proxy** | Yes | SIP proxy address of your PBX (e.g., pbx.example.com:5060). Where Telnyx sends SIP REGISTER requests. |
| **Auth Username** | No | Separate username for digest auth, if your PBX uses one. Defaults to **Username**. |
| **From User** | No | User portion of the SIP From header in outbound requests. Defaults to **Username**. |
| **Outbound proxy** | No | SIP proxy for routing outbound requests through an intermediary, if required. |
| **Expiration (sec)** | No | Registration refresh interval. Telnyx re-registers at this interval. |
| **Transport** | No | UDP, TCP, or TLS. **Must match your PBX configuration.** |

Click Next.

## Steps 3–6 — Configuration, Inbound, Outbound, Numbers

Configure these steps the same way you would for an [FQDN connection](https://developers.telnyx.com/docs/v2/voice/sip-trunking/fqdn-connections):

* Step 3 — Configuration: Codec preferences, SRTP, and other SIP settings.
* Step 4 — Inbound: Inbound call routing and handling rules.
* Step 5 — Outbound: Outbound call routing rules.
* Step 6 — Numbers: Assign phone numbers to this connection. (Optional)

**UAC inbound routing is different** For IP-based and FQDN connections, inbound calls are routed based on source IP or resolved hostname.

For a UAC connection, Telnyx is a registered endpoint on the PBX, calls arrive via the **SIP subdomain** and are routed according to the **Internal SIP URI** you set in Step 2.

Make sure that URI points to the correct Telnyx resource.

To edit your configuration later, navigate to **Voice → SIP Trunking**, select your UAC connection, and go to the **UAC Settings (Beta)** tab.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2330839800/1232549d9bcf5d3aa3cb69a5cff2/3fbb4b18-b648-47d2-be28-f3fec261b5fc?expires=1781222400&signature=46a2cc12e75ae0005f8a7842d0714cb97bc196641cc936fea3fe56c6afbd8d7f&req=diMkFsF9lIlfWfMW3nq%2BgZTCaBEhRrj4vFf4A9l2iaLWRomaLtW%2Bcs6YoQZn%0AjAs5a1CKRUEgr4pcYPntDA7e6zs%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2330839800/1232549d9bcf5d3aa3cb69a5cff2/3fbb4b18-b648-47d2-be28-f3fec261b5fc?expires=1781222400&signature=46a2cc12e75ae0005f8a7842d0714cb97bc196641cc936fea3fe56c6afbd8d7f&req=diMkFsF9lIlfWfMW3nq%2BgZTCaBEhRrj4vFf4A9l2iaLWRomaLtW%2Bcs6YoQZn%0AjAs5a1CKRUEgr4pcYPntDA7e6zs%3D%0A)

## Check Registration status

After creating or editing a UAC Connection, review the **Registration status** section to confirm whether Telnyx is registered to your external SIP registrar or PBX.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/2468446991/04a2e1a4987a7ac0befd76ba38cf/image.png?expires=1781222400&signature=fe7de7089b00095aca8eebb934b4b12e0f431a96daff587cc476a7a6c5725fdc&req=diQhHs16m4hWWPMW3nq%2BgZc4Rd%2F9uczwyNv7rGYrqpK9uRBz%2FZPu8w9r8OoA%0AcegJ73bW7kQ28heCu4U50I0Wgds%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/2468446991/04a2e1a4987a7ac0befd76ba38cf/image.png?expires=1781222400&signature=fe7de7089b00095aca8eebb934b4b12e0f431a96daff587cc476a7a6c5725fdc&req=diQhHs16m4hWWPMW3nq%2BgZc4Rd%2F9uczwyNv7rGYrqpK9uRBz%2FZPu8w9r8OoA%0AcegJ73bW7kQ28heCu4U50I0Wgds%3D%0A)

The main field to check is **SIP registration status**:

|  |  |
| --- | --- |
| **SIP Registration Status** | **Meaning** |
| registered | Telnyx is currently registered to the external SIP registrar/PBX. |
| trying | Telnyx is attempting or retrying SIP registration. Wait for the registration attempt to complete, then refresh the status. |
| failed | The latest registration attempt failed. Check **Last registration response** for more information. |
| unregistering | Telnyx is removing or unregistering the SIP registration. |
| connection\_disabled | The UAC Connection is disabled or suspended, so registration is not active. |
| unknown | The registration state is unavailable or not classified. |

The Registration status section also includes:

|  |  |
| --- | --- |
| **Field** | **Description** |
| Registered | Shows whether the UAC connection is currently registered. This shows **Yes** only when **SIP registration status** is *registered*. |
| Last registration response | Shows the most recent SIP response Telnyx received from the external SIP registrar/PBX, such as *200 OK*. |
| Refresh | Fetches the latest registration state. Use this after saving changes or updating PBX settings. |
| Show registration details | Expands additional technical registration details, such as retry/failure counters, expiration timing, next scheduled action, uptime, and SIP URI/contact information. |

After creating or updating a UAC Connection, registration status may take a few minutes to update while Telnyx picks up the configuration and attempts SIP registration.

---

## Edit or Delete a UAC Connection

## Edit credentials or proxy settings

1. Navigate to Voice Suite → SIP Trunking → SIP Connections in the Mission Control Portal.
2. Select your UAC connection.
3. Click Edit to update any field in Step 2 — for example, changing the Password after a PBX credential rotation, updating the Proxy address after a network change, or adjusting the Expiration (sec) value.

#### Disable a connection to force a fresh registration

If you need to force a fresh, clean SIP registration without deleting the connection, temporarily disable the UAC Connection and then re-enable it.  
​  
Disabling the connection unregisters the SIP UAC from your PBX. When you re-enable the connection, Telnyx starts a new registration attempt using the current External UAC settings.

## Delete a connection

1. Navigate to Voice Suite → SIP Trunking → SIP Connections in the Mission Control Portal.
2. Select your UAC connection.
3. Click Delete and confirm.

Deleting a connection immediately deregisters from the PBX. Any phone numbers assigned to the connection will be unlinked — reassign them to another connection before deleting if you want to preserve inbound service.

---

## Troubleshooting

Before troubleshooting call routing, check the **Registration status** section on the UAC Connection.

* If **SIP registration status** is *registered*, Telnyx is registered to the external SIP registrar/PBX. If calls still do not route, check the PBX dial plan and the Internal SIP URI configured in Telnyx.
* If the status is *trying*, Telnyx is attempting or retrying registration. Wait for the registration attempt to complete, then click **Refresh** to check the latest status. If the status remains *trying* for several minutes or changes to *failed*, review **Last registration response** and continue troubleshooting.
* If the status is `*ailed*, review **Last registration response** and check the SIP username, password, auth username, proxy, transport, and PBX registrar settings.
* If the status is `connection\_disabled`, confirm the UAC Connection is enabled in UAC Connection details.
* After making changes, click **Refresh** to confirm the latest registration state.

## **Connection stuck in "Registering"**

* Verify your PBX is reachable at the Proxy address from the public internet.
* Check that the port is correct (5060 for UDP/TCP, 5061 for TLS).
* Confirm no firewall is blocking SIP traffic from Telnyx UAC IP (192.76.120.14).
* Verify the Transport setting in Step 2 matches what your PBX expects (UDP, TCP, or TLS).

## **Registration succeeds but calls don't route**

* On the PBX side: Verify your PBX dial plan routes calls to the registered extension correctly. Confirm the extension is assigned to the right user or hunt group.
* On the Telnyx Mission Control Portal: Confirm Receive SIP Subdomain calls is set correctly in Step 2 — this controls whether Telnyx accepts inbound calls addressed to the SIP subdomain. Verify your telephony resource (AI Assistant, Call Control Application) is correctly linked to this connection and the Internal SIP URI points to it.

## **Registration expires frequently**

If your PBX rate-limits registrations or you see frequent re-registration cycles:

1. Edit the connection in the Mission Control Portal.
2. Increase the Expiration (sec) value in Step 2 (e.g., from 3600 to 7200).
3. Check your PBX's minimum and maximum registration interval settings — some PBX systems override the requested expiry.

---

## **Need Help?**

If you're still having trouble, contact Telnyx support at [support@telnyx.com](mailto:support@telnyx.com) or open a ticket in the Mission Control Portal. Include your Connection ID and any SIP logs from your PBX for faster resolution.

---

Related Articles

[SIP URI Calling](https://support.telnyx.com/en/articles/2925713-sip-uri-calling)[SIP Registration](https://support.telnyx.com/en/articles/4363904-sip-registration)[Yeastar S-Series: Telnyx SIP](https://support.telnyx.com/en/articles/5748952-yeastar-s-series-telnyx-sip)[How to Configure a SIP Trunk](https://support.telnyx.com/en/articles/8096455-how-to-configure-a-sip-trunk)[How to configure Yeastar P-series](https://support.telnyx.com/en/articles/13375115-how-to-configure-yeastar-p-series)

Did this answer your question?

😞😐😃

Table of contents
