---
title: PBX SIP Trunk Configuration with Telnyx
summary: Comprehensive guide for configuring FreePBX (V13–V15) and Elastix (V4–V5)
  PBX systems with Telnyx SIP trunks, covering IP-based and credentials-based authentication,
  ChanSIP and PJSIP drivers, trunk settings, dial patterns, and call routing.
sources:
- url: https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx
- url: https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk
- url: https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk
- url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
- url: https://support.telnyx.com/en/articles/1277754-freepbx-v13-pjsip-credentials
- url: https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup
- url: https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk
- url: https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip
- url: https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip
- url: https://support.telnyx.com/en/articles/5464056-setting-up-freepbx-v15-with-telnyx-api
- url: https://support.telnyx.com/en/articles/5467232-freepbx-v15-ip-trunk-chansip-tutorial
- url: https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip
- url: https://support.telnyx.com/en/articles/5619597-freepbx-v15-credentials-pjsip
updated_at: 2026-06-11T11:25:15Z
---

# PBX SIP Trunk Configuration with Telnyx

*Part 3 of 3 — see also: [Part 1](pbx-sip-trunk-configuration-with-telnyx--part-1.md), [Part 2](pbx-sip-trunk-configuration-with-telnyx--part-2.md)*

Comprehensive guide for configuring FreePBX (V13–V15) and Elastix (V4–V5) PBX systems with Telnyx SIP trunks, covering IP-based and credentials-based authentication, ChanSIP and PJSIP drivers, trunk settings, dial patterns, and call routing.

## Number Format Considerations

By default, when creating a SIP Connection in the Telnyx Mission Control Portal, the number formats for ANI and DNIS are set to **E.164**. This means Telnyx sends the dialled number in the SIP INVITE with 11 digits. Ensure your DID numbers in inbound routes are in 11-digit format so calls are accepted and routed correctly. You can control number formats as desired — see [SIP Connection Number Formats](sip-connection-number-formats.md).

---

## Supported Codecs

Telnyx supports the following audio codecs:

- ulaw (G.711u)
- alaw (G.711a)
- gsm
- g722
- g729
- Opus

For video communication, Telnyx supports the **H264** video codec.

When configuring codecs, set `disallow: all` first, then `allow` only the codecs you need (typically `ulaw` or `ulaw&alaw`).

---

## TLS Encryption

To use TLS-encrypted SIP signalling:
- Set the SIP Server Port to **5061** (instead of 5060).
- Set the transport to **TLS/TCP** (instead of UDP or TCP).
- Ensure TLS is enabled on your Telnyx SIP connection.

---

## Additional Resources

- [FreePBX documentation](https://wiki.freepbx.org/#all-updates)
- [FreePBX community](https://community.freepbx.org/)
- [FreePBX support](https://www.freepbx.org/support/)
- [Elastix/3CX admin guide](https://www.3cx.com/docs/manual/)
- [Elastix/3CX support](https://www.3cx.com/support/)
