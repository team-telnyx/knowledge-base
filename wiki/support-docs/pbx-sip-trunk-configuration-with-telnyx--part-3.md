---
title: PBX SIP Trunk Configuration with Telnyx
summary: Comprehensive guide for configuring FreePBX (V13–V15) and Elastix (V4–V5)
  PBX systems with Telnyx SIP trunks, covering IP-based and credentials-based authentication,
  ChanSIP and PJSIP drivers, trunk settings, dial patterns, and call routing.
sources:
- url: https://support.telnyx.com/en/articles/1130620-freepbx-trunk-settings-with-telnyx
  content_hash: d05ae939bac98cd660ab00f58760eaefb83a95abc85f43855b6b886814a3d42c
- url: https://support.telnyx.com/en/articles/1130622-configuring-an-elastix-4-pbx-ip-trunk
  content_hash: ad092ba4bc22ac53effad563b3946c8a4a7e2ddd8ca37297b5851363fc6ef05a
- url: https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk
  content_hash: 4a974423f69e2e328abd9bba5d548cf03d44c6ca0a93cd6930ec37c2e5cb793e
- url: https://support.telnyx.com/en/articles/1130654-configuring-an-elastix-4-pbx-trunk
  content_hash: 28b430d0c2f291395e77f38540343d7f72163f9a5470a026864404be6f6425ff
- url: https://support.telnyx.com/en/articles/1277754-freepbx-v13-pjsip-credentials
  content_hash: d6b82b3b26113648aba80d412932763b0688d0d5fef4f6111b643e7b81934cba
- url: https://support.telnyx.com/en/articles/3284033-elastix-5-fqdn-trunk-setup
  content_hash: 1e12535102d44c5a74872c1b760b80a8ab79427a6da2fc4cf94c3d7ba32a0e57
- url: https://support.telnyx.com/en/articles/3284164-elastix-5-credentials-trunk
  content_hash: 1c955a0cbcda6901892717a3feda78787cf8252182aa2550494141091b6992fb
- url: https://support.telnyx.com/en/articles/3284736-freepbx-v14-ip-trunk-chansip
  content_hash: abb0a2a3d845c440534538acb07afaf3afd806cb3f0106f589c371bc8f4f62d8
- url: https://support.telnyx.com/en/articles/3284752-freepbx-v14-credentials-chansip
  content_hash: ea0381ca75d15af69d9eb3fbb979fa6c049988e8d3d245fa1cfbc629397630ca
- url: https://support.telnyx.com/en/articles/5464056-setting-up-freepbx-v15-with-telnyx-api
  content_hash: 0abcba9e57b50ae65f4cdd8406ea4200a34267053564c8f80b31b6f96626a76c
- url: https://support.telnyx.com/en/articles/5467232-freepbx-v15-ip-trunk-chansip-tutorial
  content_hash: 2b74396965cfb1e0032b9ee1c046f7f349888d53fc2584f460ae0596f38217bf
- url: https://support.telnyx.com/en/articles/5619595-freepbx-v15-ip-trunk-pjsip
  content_hash: 97b84e426a7723c6dfdebed50c1dab66c1472af46eb3a3fe7980873d27fc3fa7
- url: https://support.telnyx.com/en/articles/5619597-freepbx-v15-credentials-pjsip
  content_hash: aad8fbb7d6b97e9fb886e76ae600137003847f5647255021a87404ed6b59df5c
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
