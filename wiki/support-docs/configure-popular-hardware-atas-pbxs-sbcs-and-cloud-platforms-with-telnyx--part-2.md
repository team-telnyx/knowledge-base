---
title: Configure popular hardware, ATAs, PBXs, SBCs, and cloud platforms with Telnyx
summary: A consolidated, field-proven setup guide that distills Telnyx best practices
  and device-specific steps for Cisco/Linksys SPA ATAs, Poly OBi300, Dinstar C60 phones,
  Mediatrix C7/4100 gateways, Synway UC‑200 PBX, UniFi Talk (credentials and IP auth),
  SBCs from Oracle, AudioCodes, Ribbon EdgeMarc, Sansay, and BYOC with Genesys Cloud.
sources:
- url: https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata
- url: https://support.telnyx.com/en/articles/5733572-mediatrix-c7-4100-telnyx-setup
- url: https://support.telnyx.com/en/articles/5800399-synway-uc-200-telnyx-setup
- url: https://support.telnyx.com/en/articles/5820183-plantronics-polycom-obi300-setup
- url: https://support.telnyx.com/en/articles/6128321-dinstar-c60-setup-config
- url: https://support.telnyx.com/en/articles/6122586-ubiquiti-trunk-unifi-talk-auth
- url: https://support.telnyx.com/en/articles/6303467-ubiquiti-trunk-unifi-talk-ip-auth
- url: https://support.telnyx.com/en/articles/4194697-oracle-acme-packet-sbc-setup
- url: https://support.telnyx.com/en/articles/4194841-audiocodes-sbc-setup
- url: https://support.telnyx.com/en/articles/4215031-ribbon-edgemarc-6000-setup
- url: https://support.telnyx.com/en/articles/4301888-sansay-sbc-vsxi-setup
- url: https://support.telnyx.com/en/articles/1130641-telnyx-recommended-hardware-configurations
- url: https://support.telnyx.com/en/articles/8268122-byoc-telnyx-genesys
updated_at: 2026-05-20T15:17:31Z
---

# Configure popular hardware, ATAs, PBXs, SBCs, and cloud platforms with Telnyx

*Part 2 of 2 — see also: [Part 1](configure-popular-hardware-atas-pbxs-sbcs-and-cloud-platforms-with-telnyx--part-1.md)*

A consolidated, field-proven setup guide that distills Telnyx best practices and device-specific steps for Cisco/Linksys SPA ATAs, Poly OBi300, Dinstar C60 phones, Mediatrix C7/4100 gateways, Synway UC‑200 PBX, UniFi Talk (credentials and IP auth), SBCs from Oracle, AudioCodes, Ribbon EdgeMarc, Sansay, and BYOC with Genesys Cloud.

## UniFi Talk with Telnyx (credentials‑based auth)

- System Settings > Third Party SIP Setup > Add Provider (e.g., Telnyx). Add custom fields: proxy, realm, username, password, register, sip_cid_type, retry_seconds, expire-seconds.
- Values:
  - proxy: sip.telnyx.com
  - realm: sip.telnyx.com
  - username/password: Telnyx SIP credentials
  - register: true
  - sip_cid_type: rpd
  - retry_seconds: 30; expire-seconds: 120
- Optional: authorize international countries; DID Numbers: import in E.164 with leading +; IP Address Range: add Telnyx signaling IP (example US: 192.76.120.10/32; use the regional IPs for your deployment per https://sip.telnyx.com/#signaling-addresses); assign DIDs to users.

## UniFi Talk with Telnyx (IP authentication)

- Third Party SIP Setup > Add Provider. Add fields: proxy, realm, context, password, register, username, extension, from-user, from-domain, retry_seconds, expire-seconds.
- Values:
  - proxy: 192.76.120.10 (use regional signaling IP if outside US)
  - realm: sip.telnyx.com (regional as applicable)
  - context: public; register: false
  - password: any placeholder (Talk UI requires a value)
  - username/from-user: your Telnyx username (for header consistency)
  - from-domain: 192.76.120.10 (or your UniFi Talk’s static IP if required)
  - retry_seconds: 30; expire-seconds: 120
- Countries/DIDs/IP Range/assignment: same as credentials flow.

## Genesys Cloud BYOC with Telnyx

- In Telnyx Mission Control:
  - Voice > SIP Trunking: Add SIP Connection; choose FQDN type; set SIP URI to your Genesys Cloud org domain (matching region); enable “have FQDN.”
  - Outbound tab: Credentials auth (set username/password); Save & Finish Editing.
  - Create an Outbound Voice Profile (select allowed countries) and assign it to the SIP Connection.
  - Assign purchased numbers to this SIP Connection (Numbers > My Numbers).
- In Genesys Cloud:
  - Admin > Trunks: create BYOC Carrier trunk (Generic BYOC subtype); set Inbound SIP Termination Identifier to match the FQDN configured at Telnyx.
  - SIP Servers/Proxies: use the regional Telnyx SIP interface (e.g., sip.telnyx.com or sip.telnyx.eu). Enable Digest Authentication; Realm = the same SIP domain; set Username/Password to match Telnyx.
  - Caller ID: set a number purchased on Telnyx.
  - SIP Access Control: add Telnyx signaling IPs (see https://sip.telnyx.com/#signaling-addresses).
  - External Trunk > Protocol > Outbound: add custom SIP header X-Telnyx-Username with the same value used for Digest auth.
  - Route inbound DIDs to your flows (e.g., Architect) and test.
- Troubleshoot: Mission Control > Reporting > Debugging > SIP Call Flow Tool: search CDRs, view call flows/Session Info, export PCAP if needed.

## Troubleshooting and validation checklist

- Registration stable? Check timers (120–300s), NAT keepalives, STUN reachability, DNS resolution.
- TLS/SRTP: confirm CA trust (where applicable), correct port (5061), and SRTP policy alignment.
- Numbering: outbound caller ID in +E.164; DID imports (UniFi) must include leading +.
- ATA inbound routing: ensure Telnyx inbound DNIS is set to SIP Username for devices that require username‑based routing.
- Dial plans/DTMF: confirm digitmaps for star codes; normalize local dialing (strip 9; prepend area/country codes) where appropriate.
- Codecs/ptime: align sides (NA: µ‑law; disable a‑law if advised; 20–30 ms ptime); adjust if you see one‑way audio or 488/415 responses.
- Firmware: update endpoints/SBCs; note Cisco SPA112/122 are EOL (basic support slated to end in 2025).

## Useful links

- Telnyx codecs overview: https://telnyx.com/resources/codecs-affect-voip-sound-quality
- What is DTMF?: https://support.telnyx.com/en/articles/1130710-what-is-dtmf
- Telnyx signaling addresses: https://sip.telnyx.com/#signaling-addresses
- Telnyx media IPs/subnets: https://sip.telnyx.com/#media
- Cisco SPA112/122 EOL notice: https://www.cisco.com/c/en/us/products/collateral/unified-communications/small-business-voice-gateways-ata/eos-eol-notice-c51-743206.html
- Vendor docs: Mediatrix C7 https://documentation.media5corp.com/pages/viewpage.action?pageId=16547905 | Poly/HP support https://support.hp.com/us-en/poly | Synway docs https://wiki.synway.net/index.php/User_Manual | Dinstar docs https://www.dinstar.com/download/ | UniFi Talk https://help.ui.com/hc/en-us | Oracle ESBC https://docs.oracle.com/cd/E95619_01/html/esbc_ecz810_configuration/ | AudioCodes SBC https://www.audiocodes.com/library/technical-documents?productFamilyGroup=1637 | Ribbon/EdgeMarc https://ribboncommunications.com/services/ribbon-support-portal | Sansay VSXi https://www.sansay.com/products/vsxi/ | Genesys Resource Center https://help.mypurecloud.com/
