---
title: Configuring Cisco Devices with Telnyx
summary: Learn how to configure Cisco SPA112/122 ATA adapters and Cisco 68xx/88xx
  series IP phones to work with Telnyx, including SIP registration, NAT traversal,
  codec selection, and optional TLS encryption.
sources:
- url: https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata
  content_hash: 695acd9be6b1d1d8805f7c0a5f4bd3991a090c8a8461266c29eea2a11dccaec8
- url: https://support.telnyx.com/en/articles/5820309-cisco-68xx-88xx-setup
  content_hash: 332e265c25d974898756d8eeb8cb1cc186371e5a5bbf8f8972c7a506aca0ccc6
updated_at: 2026-06-11T11:26:53Z
---

# Configuring Cisco Devices with Telnyx

*Part 2 of 2 — see also: [Part 1](configuring-cisco-devices-with-telnyx--part-1.md)*

Learn how to configure Cisco SPA112/122 ATA adapters and Cisco 68xx/88xx series IP phones to work with Telnyx, including SIP registration, NAT traversal, codec selection, and optional TLS encryption.

## Optional: TLS Encryption

Both device families support TLS to encrypt SIP traffic.

### Enable Secure Calling

1. On the **Voice** tab, navigate to the **Supplementary Service Settings** section (SPA112/122: under **Supplementary Service Settings**; 68xx/88xx: under the **User** sub-tab → **Supplementary Services**).
2. Set **Secure Call Setting:** Yes

### Configure SIP Transport for TLS

On the relevant line/extension, under **SIP Settings**:

- **SIP Transport:** TLS
- **SIP Port:** 5061

### Import the CA Certificate

Cisco devices require a CA certificate for TLS. Obtain it from [https://crt.sh/?id=1199354](https://crt.sh/?id=1199354).

- **SPA112/122:** Go to the **Provisions** link in the left menu. Under **CA Settings**, set **Custom CA URL:** `https://crt.sh/?id=1199354`. Click **Submit**; the device will reboot.
- **68xx/88xx:** Go to **Voice** → **Provisioning** sub-tab. Paste the certificate link in the **Custom CA Rule** field.

Click **Submit All Changes** (68xx/88xx) or **Submit** (SPA112/122). Do not unplug the device during the update.

### TLS Encryption Method (68xx/88xx)

On the 68xx/88xx, when using TLS, verify under **Audio Configuration** that **Encryption Method** is set to **AES128**.

### Secure Call Indication Tone (SPA112/122)

During secure calls on the SPA112/122, you may hear periodic beeps. To disable this notification, go to **Voice** → **Regional** → **Call Progress Tones** and clear the **Secure Call Indication Tone** field. To re-enable it, repopulate the field with: `397@-19,507@-19;15(0/2/0,.2/.1/1,.1/2.1/2)`.

## Caller ID Override (SPA112/122)

If you removed the Display Name on the SPA112/122 to resolve registration issues, configure a Caller ID override on the outbound settings of your connection in the Telnyx portal to ensure a valid Caller ID is sent. See [Caller ID Outbound vs CNAM](caller-id-outbound-vs-cnam.md) for details.

## Additional Resources

- [Cisco SPA112/122 product documentation](https://www.cisco.com/c/en/us/support/unified-communications/spa122-ata-router/model.html)
- [Cisco SPA112/122 end-of-life documentation](https://www.cisco.com/c/en/us/products/collateral/unified-communications/small-business-voice-gateways-ata/eos-eol-notice-c51-743206.html)
- [Cisco 68xx product support](https://www.cisco.com/c/en/us/support/collaboration-endpoints/ip-phone-6800-series-multiplatform-firmware/series.html)
- [Cisco 88xx product support](https://www.cisco.com/c/en/us/products/collaboration-endpoints/unified-ip-phone-8800-series/index.html?dtid=osscdc000283)
- [Cisco Community](https://community.cisco.com/t5/technology-and-support/ct-p/technology-support)
- [Cisco documentation downloads](https://software.cisco.com/portal/pub/download/portal/select.html?&i=!m&mdfid=284729655)
