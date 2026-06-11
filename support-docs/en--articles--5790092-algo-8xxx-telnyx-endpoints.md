---
source_url: https://support.telnyx.com/en/articles/5790092-algo-8xxx-telnyx-endpoints
scraped: 2026-06-11
---

Algo 8xxx: Telnyx Endpoints | Telnyx Help Center

[Skip to main content](#main-content)

# Algo 8xxx: Telnyx Endpoints

Learn how to configure your Algo device and register Algo SIP endpoints with Telnyx.

C

Written by Customer Success

January 10, 2024

Table of contents

[Jump to Instructions](#h_6d2d1486d1)

[Algo](https://www.algotechnologies.co.za/about/) is a telecommunications manufacturer of SIP endpoints, as well as various other technologies including IP speakers, paging adapters, specialty handsets (PTT, PTM) and even strobe lights, clocks, push buttons, doorphones / intercoms, and specialty handsets (PTT, PTM).

This document supports configuration of the Algo 8xxx series.

Additional documentation:

* [Algo user guides](https://www.algosolutions.com/resources/guides/)
* [Device firmware](https://www.algosolutions.com/?s=firmware&v=7516fd43adaa)

---

# Instructions for configuring Algo SIP endpoints with Telnyx

In this activity you will:

1. [Associate the SIP credentials to your endpoint](#h_f5a05735de)
2. OPTIONAL: [Enable the SIP-TLS SRTP encryption](#h_4d671fb570)
3. [Confirm registration success](#h_0b38c284f5)
4. OPTIONAL: [Enable support for G-722 codec](#h_3f5139d98d)

If you experience any issues, visit our [Troubleshooting](#h_bbb3c1d05d) section.

**Pre-requisites**

* [Properly configured Telnyx Mission Control Portal](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account)
* At least one Telnyx SIP account/sub-account with the following features:

  + A valid caller ID must be indicated (if you want Algo to make outgoing call to a specific destination - Anonymous outgoing calls aren't possible)
  + IF you want SIP traffic to be encrypted (and it's your choice), you will need to enable SIP-TLS for SRTP encryption.
* Ensure you are on the [most current Algo device firmware](https://www.algosolutions.com/?s=firmware&v=7516fd43adaa)

**Video walkthrough**

Setting up your Telnyx SIP portal account so you can make and receive calls:

|  |
| --- |
| ***Note:*** *Video walkthrough for Algo/Telnyx configuration coming soon. Check back as we update our docs.* |

## 1. Associate the SIP credentials to your endpoint

In this step, you will associate the credentials for your Telnyx SIP account/sub-account (see [pre-requisites](#h_1ff6c0a181)) to your Algo SIP endpoint.

1. Your Algo device should have an IP address assigned to it. To register your Algo SIP endpoint, open a web browser and enter this IP address.

   [![SIP Horn Control Panel. ](https://downloads.intercomcdn.com/i/o/429861117/b7850b76ca6637cedb97dffb/landingPage.jpeg?expires=1781168400&signature=eca9bd694d6babf0fed3797e3ed4dfa3a1e90a052638b8b4d90a60f53b75ca21&req=cCIuHs9%2FnIBYFb4f3HP0gDVr%2BJ4jD4op%2FFfY5GekE0zi3rDX79SfTOSKLa4h%0ANd0%3D%0A)](https://downloads.intercomcdn.com/i/o/429861117/b7850b76ca6637cedb97dffb/landingPage.jpeg?expires=1781168400&signature=eca9bd694d6babf0fed3797e3ed4dfa3a1e90a052638b8b4d90a60f53b75ca21&req=cCIuHs9%2FnIBYFb4f3HP0gDVr%2BJ4jD4op%2FFfY5GekE0zi3rDX79SfTOSKLa4h%0ANd0%3D%0A)
2. Select the **Basic Settings** tab and then the **SIP** sub-tab and enter the following information:

   1. **SIP Domain (Proxy Server):** *sip.telnyx.com*
   2. **Base/Page Extension:** Your account/sub-account username
   3. **Authentication ID:** Your account/sub-account username
   4. **Authentication Password:** Your account/sub-account password
   5. **Display Name:** Your outbound caller ID. (Devices set to make outgoing calls require a caller ID to be configured on your Telnyx SIP account, as mentioned in the [pre-requisites](#h_1ff6c0a181).)  
      ​

   ***Note that*** *if you want to register additional extensions for ringing, paging and emergency alerting, you will need to use unique credential for the respective extension in the same way. You can use any combination of page, ring, and/or emergency alerts is fine, so long as their credentials are unique!*

   [![SIP Basic Settings tab. ](https://downloads.intercomcdn.com/i/o/429870762/eb9e7b40b2803929c51683ce/sipConfig.png?expires=1781168400&signature=44112f273d79e2d16c737a2384212b999435043811f198d6d3568374014c45b7&req=cCIuHs5%2BmoddFb4f3HP0gN8J15rSh1NcmN5XgVG8nD5lURQ3oK6fia8pOAly%0Amk4%3D%0A)](https://downloads.intercomcdn.com/i/o/429870762/eb9e7b40b2803929c51683ce/sipConfig.png?expires=1781168400&signature=44112f273d79e2d16c737a2384212b999435043811f198d6d3568374014c45b7&req=cCIuHs5%2BmoddFb4f3HP0gN8J15rSh1NcmN5XgVG8nD5lURQ3oK6fia8pOAly%0Amk4%3D%0A)

[Back to Top](#h_6d2d1486d1)

## 2. OPTIONAL: Enable the SIP-TLS/SRTP encryption

In this step, you will enable and activate TLS for SIP transportation and SRTP encryption if you want to encrypt SIP traffic.

1. Select the **Advanced Settings** tab, followed by the **Advanced SIP** tab and enter the following information:

   1. **SIP Transportation:** *TLS*
   2. **SDP SRTP Offer:** *Standard* which ensures mandatory audio encryption for all calls.   
      ​  
      ​***Note that*** *if the other party does not support audio encryption, any call attempt to that party will be rejected. If you don't want this to happen, set SDP SRTP Offer to Optional. All calls will be encrypted unless the other party does not support encryption. In that case, the call will not be encrypted.*

   [![Advanced SIP Settings. ](https://downloads.intercomcdn.com/i/o/429895531/de09bd2e5b355b92be816ed5/encryption.jpeg?expires=1781168400&signature=973264673f3d48b66f6cc808423ac110c2613d32122cc79c748a80831bc164cc&req=cCIuHsB7mIJeFb4f3HP0gJtcvyUZocEqm6QOqTlQQ9tKbiaBpFsQ6C%2BvmQOy%0A%2FlA%3D%0A)](https://downloads.intercomcdn.com/i/o/429895531/de09bd2e5b355b92be816ed5/encryption.jpeg?expires=1781168400&signature=973264673f3d48b66f6cc808423ac110c2613d32122cc79c748a80831bc164cc&req=cCIuHsB7mIJeFb4f3HP0gJtcvyUZocEqm6QOqTlQQ9tKbiaBpFsQ6C%2BvmQOy%0A%2FlA%3D%0A)

|  |
| --- |
| ***IMPORTANT 8301 Users:*** *In order for a SIP server to validate the Algo device, an additional certificate has to be manually installed on the 8301. To add this user certificate file use a ‘.pem’ filetype extension and have the file named ‘sipclient’. This is done by manually adding a file named ‘sipclient.pem’, which contains a device certificate and private key, to the ‘certs’ folder (under the **Advanced Settings** tab File Manager). In future releases, ‘.crt’, ‘.cer’, and ‘.der’ certificate extensions are also be supported and you will not be restricted to naming the file ‘sipclient.pem’.* |

[Back to Top](#h_6d2d1486d1)

## 3. Confirm registration success

1. Now select the **Status** tab. You will be on the **Device** **Status** tab.
2. Find the **Status** section and ensure that the each extension's SIP registration shows as *Successful*.

   [![Device status screenshot. ](https://downloads.intercomcdn.com/i/o/429897539/cbd738e99dd83483a33ee43c/registrationstatus.jpeg?expires=1781168400&signature=57902f21366c8f32ed248c7e9e114bbe1536b42d5418f863cc3cba7d175b829a&req=cCIuHsB5mIJWFb4f3HP0gLa0b3Fz%2Ftu%2FRS%2Fr5iZl%2B8WDu9g%2BcryDK0wI%2BvbF%0AhBc%3D%0A)](https://downloads.intercomcdn.com/i/o/429897539/cbd738e99dd83483a33ee43c/registrationstatus.jpeg?expires=1781168400&signature=57902f21366c8f32ed248c7e9e114bbe1536b42d5418f863cc3cba7d175b829a&req=cCIuHsB5mIJWFb4f3HP0gLa0b3Fz%2Ftu%2FRS%2Fr5iZl%2B8WDu9g%2BcryDK0wI%2BvbF%0AhBc%3D%0A)

That's it! Your Algo is now set up and ready to go with Telnyx!

[Back to Top](#h_6d2d1486d1)

## 4. OPTIONAL: Enable support for G-722 codec

In this step, you will enable the Telnyx-supported G-722 codec if you want to use it. This applies to the codec used during SIP negotiation only. Multicast codecs are configured separately.

1. Select the **Basic Settings** tab and then the **Features** sub-tab.
2. Find the **G-722 Support** field in the **Inbound Page Settings** section and use the radio buttons to enable this feature.

   [![Test tone settings page. ](https://downloads.intercomcdn.com/i/o/429944969/1801e27aed46686a9b35f94a/codec.png?expires=1781168400&signature=325bacd06e4f48efbf5e791dcf14575ba14e06d49c4bd75e533c1923f73623cd&req=cCIuH816lIdWFb4f3HP0gMrNGMm5OAfE%2B7bo33Aas4kVG2eRIboj6Y5HErAw%0AC2A%3D%0A)](https://downloads.intercomcdn.com/i/o/429944969/1801e27aed46686a9b35f94a/codec.png?expires=1781168400&signature=325bacd06e4f48efbf5e791dcf14575ba14e06d49c4bd75e533c1923f73623cd&req=cCIuH816lIdWFb4f3HP0gMrNGMm5OAfE%2B7bo33Aas4kVG2eRIboj6Y5HErAw%0AC2A%3D%0A)

|  |
| --- |
| ***Note:*** *Algo supports the following [audio codecs](https://telnyx.com/resources/codecs-affect-voip-sound-quality): G.711 u-law, G.711 A-law, G.722 Wideband.* |

---

## Troubleshooting

There are some common issues that you may run into. The following sections will provide the most likely reasons, and potential solutions.

## 1. SIP Registration status = "Rejected by Server"

If you see this error, it means that the Telnyx server got the connection request from your endpoint, but it didn't authorize the connection.

**Credentials**

In a case like this, the first thing to always check, and the most common issue, are incorrectly entered credentials.

1. Double-check your SIP account credentials (extension, authentication ID, and password) and make sure they're correct (including case)
2. If your credentials are correct, select the **Basic Settings** tab and then the **SIP** sub-tab.

   1. If the password doesn't appear correct, it's possible that your browser is auto-filling the password field. Make sure no auto-fill is occurring because of your browser settings.

**Transportation method**

If you're authenticating correctly, it could be possible that you didn't configure the SIP transportation correctly (i.e.: You enabled encryption on the Algo side, but not the Telnyx side, or vice versa)

1. Select the **Advanced Settings** tab and then the **Advanced SIP** tab and ensure that your transportation you set here matches the configuration in your Telnyx Mission Control Portal.

**Address/port**

It is possible that you entered the incorrect address or port for the SIP server. In this case, the server doesn't know it should reject the request and will simply deny the connection. You will find this in the system log. To view the system log:

1. Select the **System** tab and then the **System Log** sub-tab.
2. If you see a *500 Internal Server error*, double-check that you provided the correct address/port for the SIP server.

[Back to Top](#h_6d2d1486d1)

## 2. SIP Registration Status = "No reply from server"

If you see this error, it means that the Algo device isn't able to communicate with the phone server.

**No Internet?**

This is a really common issue. Make sure your internet connection is up and stable and try again.

**SIP Domain (Proxy Server)**

Ensure that the server is entered correctly.

1. Select the **Basic Settings** tab and then the **SIP** tab.
2. Double-check that the **SIP Domain (Proxy Server)** field is entered correctly.

**Firewall being extra careful**

If you have a firewall present, it could be blocking incoming packets from the server.

[Back to Top](#h_6d2d1486d1)

---

## Additional Resources

Review our [getting started with guide](https://support.telnyx.com/en/articles/1176636-get-started-with-a-mission-control-account) to make sure your Telnyx Mission Control Portal account is setup correctly!

Additionally, check out:

* [Algo user guides](https://www.algosolutions.com/resources/guides/)
* [Algo device firmware updates](https://www.algosolutions.com/?s=firmware&v=7516fd43adaa)

---

Related Articles

[Panasonic KX-HDV: Telnyx setup](https://support.telnyx.com/en/articles/5814406-panasonic-kx-hdv-telnyx-setup)[Fanvil A32i: Telnyx Setup](https://support.telnyx.com/en/articles/6056428-fanvil-a32i-telnyx-setup)[MicroSIP: Setup with Telnyx](https://support.telnyx.com/en/articles/6133145-microsip-setup-with-telnyx)[Grandstream GXV3370](https://support.telnyx.com/en/articles/6187576-grandstream-gxv3370)[Fanvil XU Series: IP Phone](https://support.telnyx.com/en/articles/6210147-fanvil-xu-series-ip-phone)

Did this answer your question?

😞😐😃

Table of contents
