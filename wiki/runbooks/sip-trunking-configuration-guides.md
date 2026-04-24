---
title: SIP Trunking Configuration Guides
summary: Telnyx's SIP trunking guide will help you configure your sip devices for use with our service.
sources:
  - url: https://developers.telnyx.com/docs/voice/sip-trunking/configuration-guides/index
    content_hash: 79ae2e3f100f60ca2287a5dd90421b9622e53ca0a9892e867fd31427f245209e
updated_at: 2026-04-10T00:00:00Z
---

# SIP Trunking Configuration Guides

Telnyx's SIP trunking guide will help you configure your sip devices for use with our service.

The following Configuration Guides are intended to help you connect your SIP Infrastructure (IP-PBX, SBC, etc) to a Telnyx Elastic SIP Trunk.

Be aware, due to the large number of versions, variations, add-ons, and options for many of these systems, the settings you see may differ from those shown in our Configuration Guides. As such, these documents are intended as general guidelines, rather than configuration templates. There is an assumption of familiarity with your network and SIP infrastructure, and how they work.

## Guide Listing

Telnyx cannot provide direct support for third-party products; you should contact the manufacturer for your PBX/SBC for assistance in configuring such products.

<table>
  <tbody>
    <tr>
      <td>Vendor</td>
      <td>Version</td>
      <td>Type</td>
      <td>Qualified for Secure Trunking</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx-generic-provider-via-xml">3CX</a></td>
      <td>V18 with IP trunk</td>
      <td>IP-PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx">3CX</a></td>
      <td>V18 with credentials trunk</td>
      <td>IP-PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx">3CX</a></td>
      <td>V16 with IP trunk</td>
      <td>IP-PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx">3CX</a></td>
      <td>V16 with credentials trunk</td>
      <td>IP-PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility">3CX</a></td>
      <td>V15 with IP trunk</td>
      <td>IP-PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/7829412-3cx-and-telnyx-compatibility">3CX</a></td>
      <td>V15 with credentials trunk</td>
      <td>IP-PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6161111-3cx-configuring-a-3cx-v18-pbx">3CX</a></td>
      <td>V14 with IP trunk</td>
      <td>IP-PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1189026-3cx-configuring-a-3cx-v14-pbx-credentials-trunk">3CX</a></td>
      <td>V14 with credentials trunk</td>
      <td>IP-PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/4194697-oracle-how-to-configure-an-oracle-acme-packet-sbc-with-telnyx">Oracle</a></td>
      <td>Acme Packet</td>
      <td>E-SBC</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5761112-acrobits-configuring-acrobits-softphone-or-acrobits-groundwire-to-use-telnyx">Acrobits</a></td>
      <td>Groundwire, Softphone</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6281943-alcatel-configuring-a-telnyx-sip-trunk-with-the-alcatel-sd601-and-sd602-sip-door-phones">Alcatel</a></td>
      <td>SD601</td>
      <td>SIP door phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5790092-algo-technologies-configuring-algo-8xxx-sip-endpoints-with-telnyx">Algo</a></td>
      <td>8xxx Series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1371411-aws-setting-up-a-virtual-cross-connect-between-aws-and-telnyx">Amazon AWS</a></td>
      <td>n/a</td>
      <td>VXC</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130676-asterisk-configure-an-asterisk-credentials-trunk">Asterisk</a></td>
      <td>n/a: Credentials trunk</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130628-asterisk-configure-an-asterisk-ip-trunk">Asterisk</a></td>
      <td>n/a: IP trunk</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5819923-audiocodes-setup-and-configuration-of-the-audiocodes-400hd-ip-phone-with-telnyx">Audiocodes</a></td>
      <td>400HD</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/4194841-audiocodes-how-to-configure-an-audiocodes-sbc">Audiocodes</a></td>

      <td />

      <td>E-SBC</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5355953-auth0-setting-up-auth0-saml-identity-provider-with-telnyx-s-sso-feature">Auth0</a></td>
      <td>SAML identity proivder</td>
      <td>SaaS solution</td>
      <td>n/a</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130627-avaya-how-to-configure-an-avaya-ip-trunk-to-work-with-telnyx">Avaya</a></td>

      <td />

      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5138185-bicom-configuring-bicom-pbxware-to-work-with-telnyx">Bicom</a></td>
      <td>PBXware</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5808185-buddytalk-configure-buddytalk-bt110-bt120-to-work-with-telnyx">BuddyTalk</a></td>
      <td>BT110/120</td>
      <td>Smart speaker/speakerphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5820309-cisco-setup-and-configuration-of-the-cisco-68xx-88xx-series-with-telnyx">Cisco</a></td>
      <td>68xx/88xx</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130612-cisco-configure-a-cisco-cme-ip-trunk">Cisco</a></td>
      <td>CME with IP trunk</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130668-cisco-configure-a-cisco-cme-credentials-trunk">Cisco</a></td>
      <td>CME with credentials trunk</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130606-configuring-a-cisco-cube-cucm-ip-trunk">Cisco</a></td>
      <td>CUBE/CUCM with IP trunk</td>
      <td>SBC</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130673-cisco-configuring-a-cisco-cube-cucm-sip-trunk">Cisco</a></td>
      <td>CUBE/CUCM with credentials trunk</td>
      <td>SBC</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130665-configuring-your-cisco-spa112-122-ata">Cisco</a></td>
      <td>SPA112/122</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5772825-counterpath-configuring-bria-teams-to-work-with-telnyx">CounterPath</a></td>
      <td>Bria Teams</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130645-counterpath-configuring-bria-solo-a-k-a-x-lite-to-work-with-telnyx">CounterPath</a></td>
      <td>Bria Solo</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6128321-dinstar-setup-and-configuration-of-the-dinstar-c60-series-with-telnyx">Dinstar</a></td>
      <td>C60</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/3284164-elastix-by-3cx-configuring-a-3cx-elastix-5-credentials-trunk-with-telnyx">Elastix by 3CX</a></td>
      <td>Elastix 5 with credentials trunk</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/3284033-elastix-by-3cx-configuring-an-elastix-5-pbx-ip-fqdn-trunk-with-telnyx">Elastix by 3CX</a></td>
      <td>Elastix 5 with IP trunk</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130654-elastix-by-3cx-configure-an-elastix-4-pbx-credentials-trunk-with-telnyx">Elastix by 3CX</a></td>
      <td>Elastix 4 with credentials trunk</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130622-elastix-by-3cx-configuring-an-elastix-4-pbx-ip-trunk-with-telnyx">Elastix by 3CX</a></td>
      <td>Elastix 4 with IP trunk</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5728748-epygi-configuring-epygi-ip-pbx-qx-series-to-work-with-telnyx">Epygi</a></td>
      <td>QX series</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6203401-fanvil-configuring-a-telnyx-sip-trunk-on-the-fanvil-h5-hotel-ip-phone">Fanvil</a></td>
      <td>H5</td>
      <td>Hotel IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5811487-fanvil-setup-and-configuration-of-a-fanvil-x4g-ip-phone-with-telnyx">Fanvil</a></td>
      <td>X4G</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6206756-fanvil-configuring-a-telnyx-sip-trunk-on-the-fanvil-x2cp-x2c-x2p-call-center-ip-phone">Fanvil</a></td>
      <td>X2CP/X2C/X2P</td>
      <td>Call center IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6206533-fanvil-configuring-a-telnyx-sip-trunk-on-the-fanvil-x1-x1p-ip-phone">Fanvil</a></td>
      <td>X1/X1P</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6209862-fanvil-configuring-a-telnyx-sip-trunk-on-the-fanvil-v-series-ip-phones">Fanvil</a></td>
      <td>V-Series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6202965-fanvil-configuring-a-telnyx-sip-trunk-on-the-fanvil-h3-hotel-ip-phone">Fanvil</a></td>
      <td>H3</td>
      <td>Hotel IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6210147-fanvil-configuring-a-telnyx-sip-trunk-on-the-fanvil-xu-series-ip-phone">Fanvil</a></td>
      <td>XU Series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6202755-fanvil-configuring-a-telnyx-sip-trunk-on-the-fanvil-h2u-compact-ip-phone">Fanvil</a></td>
      <td>H2U</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6209971-fanvil-configuring-a-telnyx-sip-trunk-on-the-fanvil-x-series-ip-phone">Fanvil</a></td>
      <td>X Series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6209215-fanvil-configuring-a-telnyx-sip-trunk-on-the-fanvil-x7-series-ip-phones">Fanvil</a></td>
      <td>X7 Series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6203347-fanvil-configuring-a-telnyx-sip-trunk-on-the-fanvil-h3w-h5w-wifi-ip-phone">Fanvil</a></td>
      <td>H3W/H5W</td>
      <td>WiFi IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6056428-fanvil-setup-and-configuration-of-the-fanvil-a32i-android-console-ip-phone-with-telnyx">Fanvil</a></td>
      <td>A32i</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5810663-flyingvoice-how-to-configure-a-flyingvoice-ip-phone-to-work-with-telnyx">Flyingvoice</a></td>
      <td>All</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5811545-fortinet-setup-and-configuration-of-an-fortifone-fon-375-175-h25-ip-phone-with-telnyx">Fortinet</a></td>
      <td>FortiFone FON-375/175/H25</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5810226-fortinet-configuring-the-fortifone-fon-570-to-work-with-telnyx">Fortinet</a></td>
      <td>FortiFone FON-570</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5619597-freepbx-configuring-a-freepbx-v15-credentials-trunk-pjsip">FreePBX</a></td>
      <td>v15 with credentials trunk: PJSIP</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5619595-how-to-configure-a-freepbx-v15-ip-trunk-pjsip">FreePBX</a></td>
      <td>v15 with IP trunk: PJSIP</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5464056-freepbx-configuring-a-freepbx-v15-credentials-trunk-chansip">FreePBX</a></td>
      <td>v15 with credentials trunk: ChanSIP</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/3284736-freepbx-configuring-a-freepbx-v14-ip-trunk-chansip">FreePBX</a></td>
      <td>v14 with IP trunk: ChanSIP</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/3284752-freepbx-configuring-a-freepbx-v14-credentials-trunk-chansip">FreePBX</a></td>
      <td>v14 with credentials trunk: ChanSIP</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130620-freepbx-configuring-a-freepbx-v13-ip-trunk-chansip">FreePBX</a></td>
      <td>v13 with IP trunk: ChanSIP</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130648-configuring-a-freepbx-v13-credentials-trunk-chansip">FreePBX</a></td>
      <td>v13 with credentials trunk: ChanSIP</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1277754-configure-a-freepbx-v13-credentials-trunk-pjsip">FreePBX</a></td>
      <td>v13 with credentials trunk: PJSIP</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1618801-freeswitch-configuring-a-freeswitch-credentials-trunk">FreeSWITCH</a></td>
      <td>Credentials trunk</td>
      <td>Device</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1616935-freeswitch-configuring-a-freeswitch-ip-trunk">FreeSWITCH</a></td>
      <td>IP trunk</td>
      <td>Device</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/3220393-fusionpbx-configuring-a-fusionpbx-telnyx-credentials-trunk">FusionPBX</a></td>
      <td>n/a: Credentials trunk</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5815209-gigaset-setup-and-configuration-of-the-gigaset-a510-ip-phone-to-work-with-telnyx">Gigaset</a></td>
      <td>A510</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6167480-gigaset-configuring-the-gigaset-dx800a">Gigaset</a></td>
      <td>DX800a</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6060646-gigaset-configuring-the-gigaset-a690-as690-ip-phone-with-telnyx">Gigaset</a></td>
      <td>A690/AS690</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130694-goautodial-configure-a-goautodial-pbx-credentials-trunk-with-telnyx-as-the-carrier">GOautodial</a></td>
      <td>n/a: Credentials trunk</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130649-goautodial-configure-a-goautodial-pbx-ip-trunk-with-telnyx-as-the-carrier">GOautodial</a></td>
      <td>n/a: IP trunk</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/2239449-google-integrating-telnyx-with-a-google-vpc-through-a-virtual-cross-connect">Google VPC</a></td>
      <td>n/a</td>
      <td>VXC</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6187273-grandstream-connecting-the-grandstream-gds3710-with-wave-lite-android">Grandstream</a></td>
      <td>GDS3710</td>
      <td>Video door system</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6184748-grandstream-configuring-a-telnyx-sip-trunk-on-the-grandstream-wave-lite-softphone-app-iphone">Grandstream</a></td>
      <td>Wave Lite</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6187576-grandstream-configuring-the-grandstream-gxv3370-video-phone-with-a-telnyx-trunk">Grandstream</a></td>
      <td>GXV3370</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6184520-grandstream-configuring-a-telnyx-sip-trunk-on-the-grandstream-gxp1700-series">Grandstream</a></td>
      <td>GXP1700 Series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5819218-grandstream-setup-and-configuration-of-the-grandstream-gxp21xx-ip-phone-with-telnyx">Grandstream</a></td>
      <td>GXP21XX Series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6187411-grandstream-connecting-the-grandstream-gds3710-with-wave-lite-ios">Grandstream</a></td>
      <td>GDS3710 Series</td>
      <td>Video door system</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6184147-grandstream-configuring-a-telnyx-sip-trunk-on-the-grandstream-grp2612-grp2612p-grp2612w-series">Grandstream</a></td>
      <td>GRP2612/GRP2612P/GRP2612W Series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5815720-grandstream-setup-and-configuration-of-the-grandstream-gxp-ip-phone-with-telnyx">Grandstream</a></td>
      <td>GXP</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6169513-grandstream-configuring-a-telnyx-sip-trunk-on-the-grandstream-grp260x-series">Grandstream</a></td>
      <td>GRP260x Series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5808368-grandstream-configure-a-grandstream-dp752-ip-phone-to-work-with-telnyx">Grandstream</a></td>
      <td>DP752</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/2950523-grandstream-setup-and-configure-the-grandstream-umc6202-for-ip-authentication-with-telnyx">Grandstream</a></td>
      <td>UMC6202 with IP trunk</td>
      <td>IP-PBX appliance</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1295514-grandstream-setup-and-configuration-of-granstream-umc6202-for-credential-authentication-with-telnyx">Grandstream</a></td>
      <td>UMC6202 with credentials trunk</td>
      <td>IP-PBX appliance</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130660-configuring-grandstream-gxp16xx-with-telnyx">Grandstream</a></td>
      <td>GXP16XX Series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5748258-grandstream-configuring-sip-trunks-on-your-grandstream-ucm6xxx-series">Grandstream</a></td>
      <td>UCM6xxx Series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5725071-grandstream-configuring-grandstream-ht802-to-work-with-telnyx">Grandstream</a></td>
      <td>HT802</td>
      <td>ATA</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5361846-gsuite-by-google-setting-up-gsuite-saml-identity-provider-with-telnyx">GSuite by Google</a></td>
      <td>GSuite SAML Identity Provider</td>
      <td>SAML identity provider</td>
      <td>n/a</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5822579-konftel-setup-and-configuration-of-the-konftel-300ipx-to-work-with-telnyx">Konftel</a></td>
      <td>300IPx</td>
      <td>Conference IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5807979-konftel-configuring-the-konftel-300wx-conference-phone-to-work-with-telnyx">Konftel</a></td>
      <td>300Wx</td>
      <td>Conference IP phone (wireless)</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5341506-lastpass-setting-up-lastpass-saml-identity-provider-with-telnyx">LastPass</a></td>
      <td>n/a</td>
      <td>SAML identity provider</td>
      <td>n/a</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130674-linphone-how-to-configure-linphone-with-telnyx">Linphone</a></td>
      <td>n/a</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5733572-mediatrix-configuring-the-mediatrix-c7-4100-to-work-with-telnyx">Mediatrix</a></td>
      <td>C7/4100</td>
      <td>Analog adapter/media gateway</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/2964210-megaport-configuration-with-telnyx">Megaport</a></td>
      <td>n/a</td>
      <td>Cloud netoworking solution</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6133145-microsip-setup-and-configuration-of-the-microsip-softphone-using-telnyx-as-provider">MicroSIP</a></td>
      <td>n/a</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5355800-microsoft-azure-setting-up-microsoft-azure-ad-saml-identity-provider-with-telnyx">Microsoft</a></td>
      <td>Azure AD SAML Identity Provider</td>
      <td>SAML identity provider</td>
      <td>n/a</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/2239446-microsoft-azure-setting-up-a-virtual-cross-connect-between-azure-and-telnyx">Microsoft Azure</a></td>
      <td>n/a</td>
      <td>VXC</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/6133589-microsoft-teams-using-call2teams-to-connect-your-teams-account-to-a-telnyx-sip-trunk">Microsoft Teams</a></p></td>
      <td>Call2Teams</td>
      <td>Office 365 add-on</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5253876-microsoft-using-telnyx-as-a-pstn-provider-for-microsoft-teams-direct-routing">Microsoft</a></p></td>
      <td>Microsoft Teams</td>
      <td>E-SBC</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/6244551-mitel-configuring-a-telnyx-sip-trunk-on-the-mitel-5320e-5330e-5340e-sip-phone">Mitel</a></p></td>
      <td>5320E/5330E/5340E</td>
      <td>SIP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/6249691-mitel-configuring-a-telnyx-sip-trunk-on-the-mitel-6800-6900-sip-phone">Mitel</a></p></td>
      <td>6800/6900</td>
      <td>SIP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5807457-nch-software-configuring-an-express-talk-voip-softphone-to-work-with-telnyx">NCH Software</a></p></td>
      <td>ExpressTalk</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5335562-okta-setting-up-okta-saml-identity-provider-with-telnyx">Okta</a></p></td>
      <td>Okta SAML Identity Provider</td>
      <td>SAML identity provider</td>
      <td>n/a</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5316578-onelogin-setting-up-onelogin-saml-identity-provider-with-telnyx">OneLogin</a></p></td>
      <td>OneLogin SAML Identity Provider</td>
      <td>SAML identity provider</td>
      <td>n/a</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/1130636-osdial-configuring-an-ip-trunk-between-osdial-and-telnyx">OSDial</a></p></td>
      <td>n/a</td>
      <td>Predictive dialer</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5814406-panasonic-setup-and-configuration-of-the-panasonic-kx-hdv-series-ip-phone-with-telnyx">Panasonic</a></p></td>
      <td>KX-HDV</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5807663-panasonic-configuring-the-panasonic-kx-tgp-550-to-work-with-telnyx">Panasonic</a></p></td>
      <td>TGP 550</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5798240-pbxes-connecting-a-pbxes-trunk-to-telnyx">PBXes</a></p></td>
      <td>n/a</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5800936-phonesuite-configuring-phonesuite-voiceware-to-work-with-telnyx">PhoneSuite</a></p></td>
      <td>Voiceware, Voiceware Express/Express +, Voiceware Series 2</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5820183-plantronics-polycom-setup-and-configuration-of-the-poly-obi300-voip-adapter-with-telnyx">Plantronics/Polycom</a></p></td>
      <td>Poly OBi300</td>
      <td>VoIP adapter</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5619617-polycom-configuring-the-polycom-vvx-300-series-to-work-with-telnyx">Plantronics/Polycom</a></p></td>
      <td>VVX 300-series</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5811761-positron-setup-and-configuration-of-a-positron-ip-phone-with-telnyx">Positron</a></p></td>
      <td>IP304/IP304C, IP408/IP408C, IP410C/IP410G</td>
      <td>SIP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5790910-positron-configuring-positron-ip-pbx-to-work-with-telnyx">Positron</a></p></td>
      <td>G-Series</td>
      <td>PBX device</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/4215031-ribbon-configuring-an-edgemarc-6000-sbc-device-with-telnyx">Ribbon</a></p></td>
      <td>EdgeMarc 6000</td>
      <td>E-SBC</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/4301888-sansay-configuring-a-sansay-sbc-vsxi-session-controller">Sansay</a></p></td>
      <td>VSXi</td>
      <td>E-SBC</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5803103-scopserv-international-configuring-scoptel-ip-pbx-to-work-with-telnyx">ScopServ</a></p></td>
      <td>ScopTEL</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/6128008-sipfoundry-setup-and-configuration-of-the-sipxecs-pbx">SIPfoundry</a></p></td>
      <td>sipXecs</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/1130698-skype-configure-a-skype-for-business-sip-trunk-with-telnyx">Skype</a></p></td>
      <td>Skype for Business (Office 365)</td>
      <td>E-SBC</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><p><a href="https://support.telnyx.com/en/articles/5822823-snom-setup-and-configuration-of-the-snom-m100-kle-base-station-to-work-with-telnyx">SNOM</a></p></td>
      <td>M100 KLE</td>
      <td>IP phone base station</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5822706-snom-setup-and-configuration-of-the-snom-professinoal-d7xx-desk-phone-with-telnyx">SNOM</a></td>
      <td>Professinoal D7xx Series</td>
      <td>Desk phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5815678-snom-setup-and-configuration-of-the-snom-c520-conference-phone-to-work-with-telnyx">SNOM</a></td>
      <td>C520</td>
      <td>Conference phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5800399-synway-configuring-a-synway-uc-200-pbx-to-work-with-telnyx">Synway</a></td>
      <td>UC-200</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx">Thirdlane</a></td>
      <td>n/a</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6122586-ubiquiti-configure-a-telnyx-trunk-with-ubiquiti-unifi-talk-pbx-credentials">Ubiquiti</a></td>
      <td>Unifi Talk with credentials trunk</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6303467-ubiquiti-configure-a-telnyx-trunk-with-ubiquiti-unifi-talk-pbx-ip-auth">Ubiquiti</a></td>
      <td>Unifi Talk with IP trunk</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1130632-vicidial-how-to-configure-a-vicidial-ip-trunk-to-work-with-telnyx">Vicidial</a></td>
      <td>n/a: IP trunk</td>
      <td>Contact center suite</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/1176353-vicidial-how-to-configure-a-vicidial-credentials-trunk-to-work-with-telnyx">Vicidial</a></td>
      <td>n/a: Credentials trunk</td>
      <td>Contact center suite</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5754445-vitalpbx-configuring-your-vitalpbx">VitalPBX</a></td>
      <td>n/a</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/3185933-vodia-configuring-the-vodia-multi-tenant-pbx-for-telnyx">Vodia</a></td>
      <td>n/a</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6145484-voice-elements-configuring-voice-elements-to-use-telnyx-as-a-sip-provider">Voice Elements by Microsoft .NET</a></td>
      <td>n/a</td>
      <td>Development environment</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5822901-vtech-setup-and-configuration-of-the-vtech-vcs754-erisstation-with-telnyx">Vtech</a></td>
      <td>VCS754 ErisStation</td>
      <td>Conference phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5799830-wildix-establishing-a-sip-trunk-between-wildix-and-telnyx">Wildix</a></td>
      <td>n/a</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5754127-xorcom-configuring-a-xorcom-complete-pbx-sip-trunk-to-work-with-telnyx">Xorcom</a></td>
      <td>Complete PBX</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/3074710-yealink-configuring-a-yealink-ip-phone-to-work-with-telnyx">Yealink</a></td>
      <td>n/a</td>
      <td>IP phone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5748952-yeastar-configuring-a-yeastar-s-series-sip-trunk-to-work-with-telnyx">Yealink</a></td>
      <td>Yeastar S-Series</td>
      <td>PBX</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/6133517-zoiper-setup-and-configuration-of-zoiper-communicator-using-telnyx-as-provider">Zoiper</a></td>
      <td>Zoiper Communicator</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5717957-zoiper-configuring-zoiper-5-pro-to-work-with-telnyx">Zoiper</a></td>
      <td>5 Pro</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5721766-zoiper-configuring-zoiper-3-to-work-with-telnyx-linux">Zoiper</a></td>
      <td>3 with Linux</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>

    <tr>
      <td><a href="https://support.telnyx.com/en/articles/5720999-zoiper-configuring-zoiper-3-to-work-with-telnyx-mac-os">Zoiper</a></td>
      <td>3 with MacOS</td>
      <td>Softphone</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>


## Related Pages

- [Telnyx SIPREC server (SRS) Configuration Guide](../runbooks/telnyx-siprec-server-srs-configuration-guide.md)
- [Telnyx & LiveKit: SIP Trunk Configuration](../runbooks/telnyx-livekit-sip-trunk-configuration.md)
