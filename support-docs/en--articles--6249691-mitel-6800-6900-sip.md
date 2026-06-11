---
source_url: https://support.telnyx.com/en/articles/6249691-mitel-6800-6900-sip
scraped: 2026-06-11
---

Mitel: 6800/6900 SIP | Telnyx Help Center

[Skip to main content](#main-content)

# Mitel: 6800/6900 SIP

Learn how to set up and configure a Telnyx SIP trunk on any Mitel 6800/6900 series SIP phone.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_b563f95000)

|  |
| --- |
| ***Note:*** *The Mitel 6800/6900 families of SIP/IP phones contain a large number of products, including executive and desk phones to meet a wide variety of enterprise needs. Instead of outlining each product here, we've provided links below so you can explore these rich product lines for yourself.*  * [Mitel 6800 family of SIP phones](https://www.mitel.com/products/devices-accessories/sip-phones-peripherals) * [Mitel 6900 family of IP phones](https://www.mitel.com/products/devices-accessories/ip-phones-peripherals/6900-ip-series) |

**Additional Resources:**

* [6800/6900 series admin manual](https://www.mitel.com/document-center/devices-and-accessories/ip-phones/6800-series/6800-sip-phones/62sp1/en/mitel-6800-6900-series-sip-phones-administrator-guide)
* [Mitel Learning Center](https://www.mitel.com/support/learning-center)
* [Mitel live training webinars](https://www.mitel.com/support/learning-center/live-webinars)
* [Mitel user group](https://www.mitel.com/partners/mitel-user-group)

---

# Instructions for setting up and configuring a SIP trunk on the Mitel 6800/6900 SIP Phone

**In this activity you will:**

1. [Log into the Mitel Web Configuration Tool](#h_a607132d16)
2. [Configure your SIP trunk: Configuration options](#h_93f5a0591f)
3. [Configure your SIP trunk: Global parameters](#h_a4e2b19dc1)
4. [Configure your SIP trunk: Per-line parameters](#h_a8e407414a)
5. (Optional) [Configure TLS transportation](#h_7a4d4c9ca7)

**Pre-requisites**

* Ensure that your [Telnyx Mission Command Portal is configured properly](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* RECOMMENDED: [Enable TLS to encrypt your traffic](https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication)

  + If you choose to enable TLS/Persistent TLS, you can find your certificate(s) and keys [here](https://support.telnyx.com/en/articles/4404575-tls-and-srtp). See [section 5](#h_7a4d4c9ca7) to find out exactly what you'll need.
* Make sure your phone is running the latest firmware. See page 795 of the [Administrator Manual](https://www.mitel.com/document-center/devices-and-accessories/ip-phones/6800-series/6800-sip-phones/62sp1/en/mitel-6800-6900-series-sip-phones-administrator-guide) for details.

**Video Walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *There is currently no video walkthrough for configuring a SIP trunk on this device series. Check back as we update our docs.* |

## 1. Log into the Mitel Web Configuration Tool

Mitel phone configuration, including [SIP trunking](https://telnyx.com/products/sip-trunks), is done through the Mitel Web Configuration Tool, so you'll need to log into the portal first. To do this, you'll need your phone's IP address.

1. From your IP phone's UI, navigate to **Phone Status**.
2. From here, depending on your device, you can find the IP address by going to:

   1. **IP&MAC Addresses** option (6863i, 6865i, 6905, and 6910 IP Phones)
   2. **Network > IP Address** (6867i, 6869i, 6873i, 6920, 6930, 6940, and 6970 IP Phones)
3. Take note of the IP address, as you'll need it in a second.
4. From your computer on the same network, open a browser and enter the phone's IP address into the address bar. This will take you to the Web Configuration Tool's login screen. First time logins will use the default credentials. ***Note that the default admin credentials and the default user credentials are different.***   
   ​  
   ​**Admin default credentials:**

   1. **Username:** *admin*
   2. **Password**: *22222*

   ​**User default credentials:**

   1. **Username:** *user*
   2. **Password:** Leave this field blank.

[Back to Top](#h_b563f95000)

## 2. Configure your SIP trunk: Configuration Options

In this section, you'll use the Web Configuration Tool to set up and configure a Telnyx SIP trunk.

|  |
| --- |
| ***Note:*** *You have the option to configure these settings in the Mitel Web UI, the IP Phone UI, or the configuration files. This document covers configuration using the Mitel Web UI and the configuration files. Because each of the 6xxx series phones have slightly different UIs, please find your specific UI on page 78 of the [Administrator Guide](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291).* |

**From the Mitel Web UI:** From the lefthand navigation, go to **Advanced Settings > Global SIP** to configure global SIP parameters, or **Advanced Settings > <Line>** to configure individual line parameters for that line.

**From the configuration files (Administrators only):** Use a text editor to open the configuration file you're modifying. You can enter parameters in one of the following configuration files:

* startup.cfg
* <model>.cfg
* <mac>.cfg

You can learn more about how to configure Mitel parameters on page 95 of the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291).

|  |
| --- |
| ***Note:*** *Use the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291) to find information about configuration file precedence (page 66). For detailed information about each configuration parameter, see Appendix A, "About this Appendix" (page 843)* |

[Back to Top](#h_b563f95000)

## 3. Configure your SIP trunk: Global Parameters.

From here, you can configure your global SIP parameters.

|  |
| --- |
| ***Note:*** *SIP parameters are configurable on both a global and per-line basis. This section identifies the parameters for global authentication. If you're setting this up as a per-line authentication, see [this section](#h_a8e407414a).* |

**Global Authentication Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **IP PHONE UI PARAMETERS** | **MITEL WEB UI PARAMETERS** | **CONFIGURATION FILE PARAMETERS** | **VALUE** |
| **Screen Name** | **Screen Name** | **sip screen name** | Your Telnyx username |
| N/A | **Screen Name 2** | **sip screen name 2** | A custom text message that displays on the idle screen. (Up to 20 alphanumeric characters) |
| **User Name** | **Phone Number** | **sip user name** | Your Telnyx username |
| **Display Name** | **Caller ID** | **sip display name** | You can choose whatever you like, but keep in mind the following naming conventions:  1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices. 2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed. 3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID. |
| **Auth Name** | **Authentication Name** | **sip auth name** | Your Telnyx username |
| **Password** | **Password** | **sip password** | Your Telnyx password |
| N/A | **BLA Number** | **sip bla number** | The phone number that you assign to BLA lines that will be shared across all phones. (See page 538 of the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291).) |
| N/A | **Line Mode** | **sip mode** | The mode-type that you assign to the IP phone. Valid values are Generic (0), BroadSoft SCA (1), Reserved for (2), or BLA (3). Default is Generic (0). |
| N/A | **Call Waiting** (For more information, see page 312 of the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291)) | **call waiting** (For more information, see page 312 of the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291)) | Enables/disables call waiting on the IP phone. (See page 397 of the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291).) |
| N/A |  | **sip vmail** | The voicemail number for the phone system (i.e.: *sip vmail: \*97*) |

**Global Network Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **IP PHONE UI PARAMETERS** | **MITEL WEB UI PARAMETERS** | **CONFIGURATION FILE PARAMETERS** | **VALUE** |
| **Proxy Server** | **Proxy Server** | **sip proxy ip** | **FQDN:** *sip.telnyx.com* or **IP:***192.761.120.10*  (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).) |
| **Proxy Port** | **Proxy Port** | **sip proxy port** | If you are using TCP or UDP transport, use port *5060*. If you are using TLS transport, use port *5061.* (See [section 5](#h_7a4d4c9ca7) of this document for more information about configuring TLS) |
| N/A | **Backup Proxy Server** | **sip backup proxy ip** | *64.16.250.10* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).) |
| N/A | **Outbound Proxy Server** | **sip outbound proxy** | **FQDN:** *sip.telnyx.com* or **IP:***192.761.120.10*  (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).) |
| **Registrar Server** | **Backup Outbound Proxy** | **sip backup outbound proxy** | *sip.telnyx.com*  (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).) |

[Back to Top](#h_b563f95000)

## 4. Configure your SIP trunk: Per-Line Parameters.

From here, you can configure your per-line SIP parameters.

|  |
| --- |
| ***Note:*** *SIP parameters are configurable on both a global and per-line basis. This section identifies the parameters for per-line authentication. If you're setting this up as a global authentication, see [this section](#h_a4e2b19dc1).* |

**Per-Line Authentication Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **IP PHONE UI PARAMETERS** | **MITEL WEB UI PARAMETERS** | **CONFIGURATION FILE PARAMETERS** | **VALUE** |
| **Screen Name** | **Screen Name** | **sip lineN screen name** | Your Telnyx username |
| N/A | **Screen Name 2** | **sip lineN screen name 2** | A custom text message that displays on the idle screen. (Up to 20 alphanumeric characters) |
| **User Name** | **Phone Number** | **sip lineN user name** | Your Telnyx username |
| **Display Name** | **Caller ID** | **sip lineN display name** | You can choose whatever you like, but keep in mind the following naming conventions:  1. Caller ID Name should be in capital letters. This will appears more clearly/visible on some devices. 2. You must NOT use any special characters, as they will not be displayed. Spaces are allowed. 3. Some of regular Canadian providers will not show more than 15 characters. We suggest shrinking or adapt your caller ID. |
| **Auth Name** | **Authentication Name** | **sip lineN auth name** | Your Telnyx username |
| **Password** | **Password** | **sip lineN password** | Your Telnyx password |
| N/A | **BLA Number** | **sip lineN bla number** | The phone number that you assign to BLA lines that will be shared across all phones. (See page 538 of the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291).) |
| N/A | **Line Mode** | **sip lineN mode** | The mode-type that you assign to the IP phone. Valid values are Generic (0), BroadSoft SCA (1), Reserved for (2), or BLA (3). Default is Generic (0). |
| N/A | **Call Waiting** (For more information, see page 312 of the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291)) | **sip lineN call waiting** (For more information, see page 312 of the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291)) | Enables/disables call waiting on the IP phone. (See page 397 of the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291).) |
| N/A | N/A | **sip lineN vmail** | The voicemail number for each line (i.e.: *sip vmail: \*97*) |

**Global Network Parameters**

|  |  |  |  |
| --- | --- | --- | --- |
| **IP PHONE UI PARAMETERS** | **MITEL WEB UI PARAMETERS** | **CONFIGURATION FILE PARAMETERS** | **VALUE** |
| **Proxy Server** | **Proxy Server** | **sip lineN proxy ip** | **FQDN:** *sip.telnyx.com* or **IP:***192.761.120.10*  (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).) |
| **Proxy Port** | **Proxy Port** | **sip lineN proxy port** | If you are using TCP or UDP transport, use port *5060*. If you are using TLS transport, use port *5061.* (See [section 5](#h_7a4d4c9ca7) of this document for more information about configuring TLS) |
| N/A | **Backup Proxy Server** | **sip lineN backup proxy ip** | *64.16.250.10* (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).) |
| N/A | **Outbound Proxy Server** | **sip lineN outbound proxy** | **FQDN:** *sip.telnyx.com* or **IP:***192.761.120.10*  (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).) |
| **Registrar Server** | **Backup Outbound Proxy** | **sip lineN backup outbound proxy** | *sip.telnyx.com*  (For international, see [this document](https://sip.telnyx.com/#signaling-addresses).) |

[Back to Top](#h_b563f95000)

## 5. (Optional) Configure TLS transportation

Your phone supports both TLS (Transport Layer Security) and Persistent TLS, ensuring communication privacy between SIP phones and the internet without eavesdropping or tamper with your calls/messages. In this section, you can specify your SIP Root and Intermediate Certificate files, local certificate files, private key filename, and/or trusted certificate filename to use when your phone is using TLS as its transport protocol.

|  |
| --- |
| ***IMPORTANT:*** *This must be set up by an administrator. Additionally, note that you can only create one Persistent TLS connection per phone.*  * *If you choose to configure Persistent TLS, you must also specify the Trusted Certificate file to use. Root and Intermediate Certificates, Local Certificate, and Private Key files are OPTIONAL.*  *[This document](https://support.telnyx.com/en/articles/4404575-tls-and-srtp) will provide you with the values you'll need, and it is linked multiple times in this section.*    *For more information about Mitel's requirements, see page 692 of the [Administrator Manual](https://productdocuments.mitel.com/legacypdf/Devices%20and%20Accessories/IP%20Phones/6900%20Series/6900%20SIP%20Phones/6.2SP1/en/Mitel_6800_6900_Admin_Guide_R6.2.0_SP1.pdf?_gl=1*ob6l82*_ga*MTAzODA4NzQxNi4xNjUzNDA2Mjkx*_ga_GJ2SLN9QSE*MTY1NDUyMjk4NC44LjAuMTY1NDUyMjk4NC4w&_ga=2.223570075.1245405445.1654522984-1038087416.1653406291).*    *For more information about the TLS settings in the config files, see page 964 of the Administrator Manual.* |

|  |  |  |  |
| --- | --- | --- | --- |
| **IP PHONE UI PARAMETERS** | **MITEL WEB UI PARAMETERS** | **CONFIGURATION FILE PARAMETERS** | **VALUE** |
| N/A | **Transport Protocol** | **sip transport protocol** | This is the protocol the phone will use when sending SIP data. The default is *UDP*.    If you use TLS: the phone will check to see if **sips persistent tls** is enabled. If it is enabled, the phone uses Persistent TLS on the connection.    If **sips persistent tls** is disabled, then the phone uses TLS on the connection.    If TLS is used, you must specify the [Root and Intermediate Certificates, the Local Certificate, the Private Key, and the Trusted Certificates](https://support.telnyx.com/en/articles/4404575-tls-and-srtp). |
| N/A | N/A | **sips persistent tls** | Enables/disables the use of Persistent Transport Layer Security (TLS).    Persistent TLS sets up the connection to the server once and re-uses that connection for all calls from the phone. The setup connection for Persistent TLS is established during the registration of the phone. If the phones are set to use Persistent TLS, and a call is made from the phone, this call and all subsequent calls use the same authenticated connection. This significantly reduces the delay time when placing a call.    If the phone uses Persistent TLS, you MUST specify the [Trusted Certificates](https://support.telnyx.com/en/articles/4404575-tls-and-srtp); the Root and Intermediate Certificates, the Local Certificate, and the Private Key are *optional*. |
| N/A | N/A | **sip persistent tls keep alive** | Allows you to configure the keep-alive feature for persistent TLS connections only. When this feature is configured, the phone will send keep-alive pings to the proxy server at configured intervals.    **Note:** The real time interval will vary between 80% and 100% of the configured value. |
| N/A | N/A | **sip send sips over tls** | Allows administrators the ability to manually configure the IP phones to use either the SIP or SIPS URI scheme when TLS or persistent TLS is enabled. |
| N/A | **Root and Intermediate Certificates Filename** | **sips root and intermediate certificates** | Allows you to specify the SIP [Root and Intermediate Certificate files](https://support.telnyx.com/en/articles/4404575-tls-and-srtp) to use when the phone uses the TLS transport protocol to setup a call.    This parameter is required when configuring TLS (optional for Persistent TLS.) |
| N/A | **Local Certificate Filename** | **sips local certificate** | Allows you to specify the [Local Certificate file](https://support.telnyx.com/en/articles/4404575-tls-and-srtp) to use when the phone uses the TLS transport protocol to setup a call.    This parameter is required when configuring TLS (optional for Persistent TLS.) |
| N/A | **Private Key Filename** | **sips private key** | Allows you to specify a [Private Key file](https://support.telnyx.com/en/articles/4404575-tls-and-srtp) to use when the phone uses the TLS transport protocol to setup a call.    This parameter is required when configuring TLS (optional for Persistent TLS.) |
| N/A | **Trusted Certificate Filename** | **sips trusted certificate** | Allows you to specify the [Trusted Certificate files](https://support.telnyx.com/en/articles/4404575-tls-and-srtp) to use when the phone uses the TLS transport protocol to setup a call.    The Trusted Certificate files define a list of trusted certificates. The phone’s trusted list must contain the CA root certificates for all the servers it is connecting to. For example, if the phone is connecting to server A which has a certificate signed by CA1, and server B that has a certificate signed by CA2, the phone must have CA1 root certificate and CA2 root certificate in its Trusted Certificate file.    This parameter is required when configuring TLS or Persistent TLS. |

That's it, you've now completed the configuration of your Mitel SIP phone with your Telnyx account.

[Back to Top](#h_b563f95000)

---

## Additional Resources

Review our [getting started guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is set up correctly.

Additionally you can check out:

* [6800/6900 series admin manual](https://www.mitel.com/document-center/devices-and-accessories/ip-phones/6800-series/6800-sip-phones/62sp1/en/mitel-6800-6900-series-sip-phones-administrator-guide)
* [Mitel Learning Center](https://www.mitel.com/support/learning-center)
* [Mitel live training webinars](https://www.mitel.com/support/learning-center/live-webinars)
* [Mitel user group](https://www.mitel.com/partners/mitel-user-group)

---

Related Articles

[Grandstream GRP260x: SIP Trunk](https://support.telnyx.com/en/articles/6169513-grandstream-grp260x-sip-trunk)[Grandstream GRP2612: SIP Trunk](https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)[Fanvil X-Series: IP Phone](https://support.telnyx.com/en/articles/6209971-fanvil-x-series-ip-phone)[Mitel: 5320E/5330E/5340E SIP](https://support.telnyx.com/en/articles/6244551-mitel-5320e-5330e-5340e-sip)

Did this answer your question?

😞😐😃

Table of contents
