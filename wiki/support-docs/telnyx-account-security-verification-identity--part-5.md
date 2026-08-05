---
title: Telnyx Account Security, Verification & Identity
summary: This page consolidates Telnyx guidance on account verification (legacy Level
  1/Level 2 and the newer Trial-Paid-Verified-Enterprise framework), Mission Control
  Portal two-factor authentication, the Telnyx Verify API for embedding 2FA in your
  own applications, fraud prevention and account compromise recovery, blocked account
  guidelines, refunds, TLS/SSL certificate handling, and webhook certificate authority
  errors.
sources:
- url: https://support.telnyx.com/en/articles/1130595-account-verification
- url: https://support.telnyx.com/en/articles/1130639-what-is-your-refund-policy
- url: https://support.telnyx.com/en/articles/1130711-does-telnyx-encrypt-communication
- url: https://support.telnyx.com/en/articles/3610162-prevent-telnyx-account-fraud
- url: https://support.telnyx.com/en/articles/3739748-2fa-totp-setup
- url: https://support.telnyx.com/en/articles/5367966-introducing-the-verify-api
- url: https://support.telnyx.com/en/articles/5701653-telnyx-verify-2fa-made-easy
- url: https://support.telnyx.com/en/articles/7020727-account-compromise-what-to-do
- url: https://support.telnyx.com/en/articles/7915224-blocked-account-guidelines
- url: https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com
- url: https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error
- url: https://support.telnyx.com/en/articles/8269305-appeal-level-2-verification-status
- url: https://support.telnyx.com/en/collections/3968260-telnyx-identity-verification-tools
updated_at: 2026-08-05T13:26:47Z
---

# Telnyx Account Security, Verification & Identity

*Part 5 of 5 — see also: [Part 1](telnyx-account-security-verification-identity--part-1.md), [Part 2](telnyx-account-security-verification-identity--part-2.md), [Part 3](telnyx-account-security-verification-identity--part-3.md), [Part 4](telnyx-account-security-verification-identity--part-4.md)*

This page consolidates Telnyx guidance on account verification (legacy Level 1/Level 2 and the newer Trial-Paid-Verified-Enterprise framework), Mission Control Portal two-factor authentication, the Telnyx Verify API for embedding 2FA in your own applications, fraud prevention and account compromise recovery, blocked account guidelines, refunds, TLS/SSL certificate handling, and webhook certificate authority errors.

## TLS, Encryption, and Certificate Errors

### Does Telnyx Encrypt Communication?

By default, Telnyx does not encrypt calls. If your device supports TLS (Transport Layer Security) to encrypt signaling and SRTP to encrypt media, you can turn on these settings on your connection for end-to-end encryption.

Telnyx leverages its private network to pull traffic off the public web and carry media across its own fiber, ensuring packets are exposed to as few public hops as possible.

- For outbound calls, configure your device to use TLS and SRTP; no further configuration is needed on the Telnyx portal.
- For inbound calls, enable TLS and SRTP in the [Connections page](https://portal.telnyx.com/#/voice/connections).

To encrypt inbound signaling in the Telnyx portal, on the Real-Time Communications tab, navigate to **Voice > SIP Trunking** and to the Connection settings. If using IP/FQDN, you can encrypt the inbound signaling there. Media encryption is configured in the same section.

### Certificate Error: api.telnyx.com

Telnyx uses TLS certificates provided by Cloudflare to produce a secure connection between users and the endpoint. If you receive a security certificate error, you may need to install the TLS certificate and configure Java settings via the terminal.

SSL/TLS certificates create trust in users' websites. The characteristics of an SSL/TLS-secured webpage include:

- A secure icon and green address bar on the web browser
- An `https` prefix on the website address
- A valid SSL/TLS certificate (verifiable by clicking and expanding the secure icon on the URL address bar)
- Once the encrypted connection is established, only the client and the webserver can see the data sent

An SSL/TLS certificate contains the domain name, certificate authority, certificate authority's digital signature, issuance date, expiration date, public key, and SSL/TLS version.

Telnyx uses Cloudflare's [Universal TLS certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/). By default, Cloudflare issues and renews free, unshared, publicly trusted SSL certificates to all domains added to and activated on Cloudflare. Universal certificates are [Domain Validated (DV)](https://developers.cloudflare.com/ssl/concepts/#validation-level).

Cloudflare maintains the [trust store certificates](https://developers.cloudflare.com/ssl/concepts/#trust-store) on a public [GitHub repository](https://github.com/cloudflare/cfssl_trust). The certificate bundle that can be included in the trust store is at [ca-bundle.crt](https://github.com/cloudflare/cfssl_trust/blob/master/ca-bundle.crt).

#### Java Default Setting Via Terminal

```
${JAVA_HOME}/lib/security/cacerts
```

If you are using Java defaults, you do not need to take action to correctly validate the connection into [https://api.telnyx.com](https://portal.telnyx.com/#/login/sign-in). If you are not using the Java default CA certs store, you can import all trusted CA certificates used by Cloudflare using Java's keytool:

1. Fetch the CAs bundle published by Cloudflare: [ca-bundle.crt](https://github.com/cloudflare/cfssl_trust/blob/master/ca-bundle.crt)
2. Add those certificates to the Java truststore you use:

```
## Fetch CA bundle from Cloudflare repo
$ curl -o cf-ca-bundle.crt -L https://raw.githubusercontent.com/cloudflare/cfssl_trust/master/ca-bundle.crt

## Split bundle in individual certs
$ csplit -f cf-ca-cert -z ca-bundle.crt '/-----BEGIN CERTIFICATE-----/' '{*}'

## Import the CA certs into an existing truststore file (eg: myTrustStoreFile). Adjust -storepass appropriately
$ for ca in ls cf-ca-cert*; do keytool -import -storepass changeit -keystore myTrustStoreFile -alias $ca -file $ca -noprompt; done
```

Cloudflare is using `[O = Baltimore, OU = CyberTrust, CN = Baltimore CyberTrust Root CA](https://cacerts.digicert.com/BaltimoreCyberTrustRoot.crt.pem)` to sign `https://api.telnyx.com`. Including this certificate only in your truststore should be enough to validate connections to `https://api.telnyx.com`, but Cloudflare may change it at any time for other [supported CAs](https://developers.cloudflare.com/ssl/reference/certificate-authorities/).

For more help with this process, contact [support@telnyx.com](mailto:support@telnyx.com).

### Webhook Issue: CA Error

If the error says the certificate authority (CA) isn't recognized and your payload is being sent to the failover webhook URL instead of the primary, the connection cannot be established over HTTPS. There are two options:

- (a) Make sure your server has a certificate that is signed by a known CA
- (b) Use HTTP instead of HTTPS

## Appeal Level 2 Verification Status

New users will be enabled with the TPVE Account Levels framework and will not have access to the legacy L2 Verification section.

Level 2 Verification is one way that Telnyx helps to protect the integrity of the Telnyx platform and consumers from spam or fraudulent calls and messages by making sure users are legitimate. If you become L2 Verified, you will have more freedom to call certain international destinations, send messages from your account at a higher rate, order SIM cards, and use call forwarding.

### How to Submit Your L2 Verification

1. Log in to your [Mission Control Portal](https://portal.telnyx.com/).
2. Navigate to the **Account Settings** section of the portal by clicking on the Profile icon (top right) > Account Settings.
3. Within Account Settings, click on the **Profile** tab in the left navigation bar. Update your Company Name and Address in the **Account Information** section.
4. Add a Payment Method by navigating to the [Billing section](https://portal.telnyx.com/#/billing/payment) of the portal. Click on the Profile icon (top right) > Manage Billing. From there, click on the **Billing Overview** tab on the left navigation bar, then click **Make a Payment**. Fill out the form and hit **Continue**.
5. Navigate to the [Verifications section](https://portal.telnyx.com/#/account/my-account/verifications) of the portal to submit your Level 2 verification request. Click on the Profile icon (top right) > Account Settings > Verifications. Fill out your L2 verification request and hit submit.

### How to Check Status of L2 Verification

1. Log in to your Mission Control Portal > Profile (top right) > Account Settings > [Verifications](https://portal.telnyx.com/#/app/account/verifications).
2. If you have recently submitted your L2 Verification, allow at least 48 hours for review.
3. If approved, it will say "Verified" in green next to Level 2 Verification.
4. If it has been more than 72 hours and your account is still unverified for L2, and you feel you have been denied in error, follow the appeal instructions below.

### Appealing a Denied L2 Verification

If you have been denied L2 Verification and would like to appeal your verification status, answer the following questions:

- What are you planning to use the Telnyx services for?
- Are you going to use Telnyx services for your business?
- What is your business's website?
- Have you ensured your Telnyx account details match any payment methods used to make a payment? If you have not added a payment method, please do so now.

Send your appeal and responses to [kyc.verifications@telnyx.com](mailto:kyc.verifications@telnyx.com). In some circumstances, the review team may require scanned documentation in order to verify your account.
