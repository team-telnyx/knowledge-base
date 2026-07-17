---
title: 'Telnyx Voice: DTMF, TwiML Conferences, and TLS Certificates'
summary: 'This page covers three Telnyx support topics: configuring DTMF (Dual-Tone
  Multi-Frequency) signalling on SIP connections, building Twilio TwiML conference
  calls on Telnyx using the Voice API across multiple programming languages, and resolving
  TLS certificate errors when connecting to api.telnyx.com.'
sources:
- url: https://support.telnyx.com/en/articles/1130710-what-is-dtmf-and-how-to-configure-it-on-telnyx
- url: https://support.telnyx.com/en/articles/13389311-twilio-twiml-conference-on-telnyx
- url: https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com
updated_at: 2026-07-17T09:06:59Z
---

# Telnyx Voice: DTMF, TwiML Conferences, and TLS Certificates

*Part 3 of 4 — see also: [Part 1](telnyx-voice-dtmf-twiml-conferences-and-tls-certificates--part-1.md), [Part 2](telnyx-voice-dtmf-twiml-conferences-and-tls-certificates--part-2.md), [Part 4](telnyx-voice-dtmf-twiml-conferences-and-tls-certificates--part-4.md)*

This page covers three Telnyx support topics: configuring DTMF (Dual-Tone Multi-Frequency) signalling on SIP connections, building Twilio TwiML conference calls on Telnyx using the Voice API across multiple programming languages, and resolving TLS certificate errors when connecting to api.telnyx.com.

## Certificate Error: api.telnyx.com

Telnyx uses a TLS (Transport Layer Security) certificate provided by Cloudflare to produce a secure connection between users and the endpoint. If you encounter a security certificate error when connecting to `https://api.telnyx.com`, you may need to install the TLS certificate.

### Quick overview of TLS certificates

SSL/TLS certificates create trust in users' websites. Businesses install SSL/TLS certificates on web servers to create SSL/TLS-secured websites. The characteristics of an SSL/TLS-secured webpage are:

- A secure icon and green address bar on the web browser
- An `https` prefix on the website address on the browser
- A valid SSL/TLS certificate (verifiable by clicking and expanding the secure icon on the URL address bar)
- Once the encrypted connection has been established, only the client and the webserver can see the data that is sent

An SSL/TLS certificate contains the following information:

- Domain name
- Certificate authority
- Certificate authority's digital signature
- Issuance date
- Expiration date
- Public key
- SSL/TLS version

TLS public certificates are required to launch a website publicly, and a trusted certification authority must issue the public TLS certificate.

### Obtaining an SSL/TLS certificate

For an SSL certificate to be valid, domains need to obtain it from a certificate authority (CA). A CA is an outside organization, a trusted third party, that generates and gives out SSL certificates. The CA will also digitally sign the certificate with their own private key, allowing client devices to verify it. Most, but not all, CAs will charge a fee for issuing an SSL certificate.

Once the certificate is issued, it needs to be installed and activated on the website's origin server. Web hosting services can usually handle this for website operators. Once it's activated on the origin server, the website can load over HTTPS, and all traffic to and from the website will be encrypted and secure.

### Installing the SSL/TLS certificates

Telnyx uses Cloudflare's [Universal TLS certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/). By default, Cloudflare issues and renews free, unshared, publicly trusted SSL certificates to all domains added to and activated on Cloudflare. Universal certificates are [Domain Validated (DV)](https://developers.cloudflare.com/ssl/concepts/#validation-level). For setup details, refer to [Enable Universal SSL](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/).

Cloudflare maintains the [trust store certificates](https://developers.cloudflare.com/ssl/concepts/#trust-store). A trust store is the list of certificate authority (CA) and intermediate certificates that are trusted by operating systems, web browsers, or other software that interacts with SSL/TLS certificates. Cloudflare maintains its trust store on a public [GitHub repository](https://github.com/cloudflare/cfssl_trust). The certificate bundle that can be included in the trust store is available at [ca-bundle.crt](https://github.com/cloudflare/cfssl_trust/blob/master/ca-bundle.crt).

### Java default setting via terminal

The default Java truststore is located at:

```
${JAVA_HOME}/lib/security/cacerts
```

If you are using Java defaults, you do not need to take action to correctly validate the connection into [https://api.telnyx.com](https://portal.telnyx.com/#/login/sign-in).

If you are not using the Java default CA certs store, you can import all trusted CA certificates used by Cloudflare using Java's keytool with the following steps:

1. Fetch the CAs bundle published by Cloudflare: [https://github.com/cloudflare/cfssl_trust/blob/master/ca-bundle.crt](https://github.com/cloudflare/cfssl_trust/blob/master/ca-bundle.crt)
2. Add those certificates to the Java truststore you use:

```bash
# Fetch CA bundle from Cloudflare repo
$ curl -o cf-ca-bundle.crt -L https://raw.githubusercontent.com/cloudflare/cfssl_trust/master/ca-bundle.crt

# Split bundle in individual certs
$ csplit -f cf-ca-cert -z ca-bundle.crt '/-----BEGIN CERTIFICATE-----/' '{*}'

# Import the CA certs into an existing truststore file (eg: myTrustStoreFile). Adjust -storepass appropriately
$ for ca in ls cf-ca-cert*; do keytool -import -storepass changeit -keystore myTrustStoreFile -alias $ca -file $ca -noprompt; done
```

### Telnyx API example of SSL/TLS certificate via Java

Using the [List notification channels](https://developers.telnyx.com/api/notifications/list-notification-channels) Telnyx API as an example:

```java
// App.java
import java.net.*;
import java.net.http.*;
import java.util.*;
import java.nio.charset.StandardCharsets;
import java.util.stream.Collectors;

public class App {
  public static void main(String[] args) throws Exception {
    var httpClient = HttpClient.newBuilder().build();
    HashMap<String, String> params = new HashMap<>();
    params.put("page[number]", "1");
    params.put("page[size]", "20");
    params.put("filter[channel_type_id][eq]", "webhook");

    var query = params.keySet().stream()
      .map(key -> key + "=" + URLEncoder.encode(params.get(key), StandardCharsets.UTF_8))
      .collect(Collectors.joining("&"));

    var host = "https://api.telnyx.com";
    var pathname = "/v2/notification_channels";
    var request = HttpRequest.newBuilder()
      .GET()
      .uri(URI.create(host + pathname + '?' + query))
      .header("Authorization", "Bearer ".concat(System.getenv("TELNYX_TOKEN")))
      .build();

    var response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
    System.out.println(response.body());
  }
}
```

When run with the default Java JRE/JDK CA store, the expected response is returned:

```bash
# Compile App.java
$ javac App.java

# Run App without creds
$ java App
{
  "errors": [
    {
      "code": "10009",
      "title": "Authentication failed",
      "detail": "Could not understand the provided credentials.",
      "meta": {
        "url": "https://developers.telnyx.com/docs/overview/errors/10009"
      }
    }
  ]
}

# Run App with creds
$ export TELNYX_TOKEN="<YOUR_TELNYX_API_TOKEN>"
$ java App
{"data": [], "meta": {"total_pages": 0, "total_results": 0, "page_number": 1, "page_size": 20}}
```

To see how the error looks when the truststore doesn't contain the needed CA cert, perform the following quick test:

```bash
# Fetch the default cacerts truststore
## When using JDK
$ cp ${JAVA_HOME}/lib/security/cacerts ./
## When using JRE
$ cp ${JAVA_HOME}/jre/lib/security/cacerts ./

# Confirm test App works as expected
$ java -Djavax.net.ssl.trustStore=cacerts -Djavax.net.ssl.trustStorePassword=changeit App
{"data": [], "meta": {"total_pages": 0, "total_results": 0, "page_number": 1, "page_size": 20}}

# Delete relevant certificate from the truststore
$ keytool -delete -alias debian:baltimore_cybertrust_root.pem -storepass changeit -keystore cacerts

# Run App again and it will fail
$ java -Djavax.net.ssl.trustStore=cacerts -Djavax.net.ssl.trustStorePassword=changeit App
Exception in thread "main" javax.net.ssl.SSLHandshakeException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target
```

### Configuring more SSL certificates

If a customer wants to configure more SSL certificates for the [https://api.telnyx.com](https://portal.telnyx.com/#/login/sign-in) domain, more than one different type of public SSL certificate can be configured. Currently, Cloudflare can make a decision on which Certificate Authority (CA) uses that certificate for the customer.

For [Universal SSL certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/limitations/#certificate-authority), Cloudflare chooses the certificate authority used for your certificate. Cloudflare can change the issuer for [https://api.telnyx.com](https://portal.telnyx.com/#/login/sign-in) certificates, but it will be listed in the links above.

Cloudflare is using `[O = Baltimore, OU = CyberTrust](https://cacerts.digicert.com/BaltimoreCyberTrustRoot.crt.pem), [CN = Baltimore CyberTrust Root CA](https://cacerts.digicert.com/BaltimoreCyberTrustRoot.crt.pem) to sign [https://api.telnyx.com](https://portal.telnyx.com/#/login/sign-in). Including this certificate only in your truststore should be enough to validate connections to [https://api.telnyx.com](https://portal.telnyx.com/), but Cloudflare may change it at any time for other of its [supported CAs](https://developers.cloudflare.com/ssl/reference/certificate-authorities/).

For more help with this process, contact [support@telnyx.com](mailto:support@telnyx.com).
