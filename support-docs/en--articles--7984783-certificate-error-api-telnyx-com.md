---
source_url: https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com
scraped: 2026-07-08
content_hash: b8a0fe4f7ba0cc06092c1f03d8a8abf75fb1478976ea88d3b0f4a47d99208fe5
---

Certificate Error: api.telnyx.com | Telnyx Help Center

[Skip to main content](#main-content)

# Certificate Error: api.telnyx.com

In this article, you will get to know how you can install the TLS certificate for Telnyx

Written by Alex Conroy

June 6, 2024

Table of contents

# What to do if you get a security certificate error:

TLDR:

Telnyx uses TLS (Transport Layer Security) certificate provided by Cloudflare and produces a secure connection between the users and the endpoint. Click [here](https://docs.google.com/document/d/1QPqyVEpMlbYe4iBMQB4drqHAtqrMM5HRHuJLdwROgdM/edit#heading=h.7nod16s9fpu7) to get a certificate. Users need to [install](https://docs.google.com/document/d/1QPqyVEpMlbYe4iBMQB4drqHAtqrMM5HRHuJLdwROgdM/edit#heading=h.7nod16s9fpu7) the TLS certificate then you can configure the [Java](https://docs.google.com/document/d/1QPqyVEpMlbYe4iBMQB4drqHAtqrMM5HRHuJLdwROgdM/edit#heading=h.6y7amvc7tpv6) settings via the terminal. For example, Telnyx API TLS certificates via Java click [here](https://docs.google.com/document/d/1QPqyVEpMlbYe4iBMQB4drqHAtqrMM5HRHuJLdwROgdM/edit#heading=h.fl7wifu6k9e7).

You should be able to solve the issue with the above steps but if the issue persists please read the remainder of the article.

## Quick Overview for TLS Certificates

SSL/TLS certificates create trust in the users' websites. Businesses install SSL/TLS certificates on web servers to create SSL/TLS-secured websites.

The characteristics of an SSL/TLS-secured webpage are as follows:

* A secure icon and green address bar on the web browser
* An https prefix on the website address on the browser
* A valid SSL/TLS certificate. You can check if the SSL/TLS certificate is valid by clicking and expanding the secure icon on the URL address bar
* Once the encrypted connection has been established only the client & the webserver can see the data that is sent.

An SSL/TLS certificate contains the following information:

* Domain name
* Certificate authority
* Certificate authority's digital signature
* Issuance date
* Expiration date
* Public key
* SSL/TLS version

TLS Public certificates are required to launch a website publicly, for example, the landing page of any website, or microsite webpages, and those websites keep away the browser warnings. A trusted certification authority must issue the public TLS certificate.

## Obtaining an SSL/TLS Certificate:

For an SSL certificate to be valid, domains need to obtain it from a certificate authority (CA). A CA is an outside organization, a trusted third party, that generates and gives out SSL certificates.

The CA will also digitally sign the certificate with their own private key, allowing client devices to verify it. Most, but not all, CAs will charge a fee for issuing an SSL certificate.

Once the certificate is issued, it needs to be installed and activated on the website's origin server. Web hosting services can usually handle this for website operators.

Once it's activated on the origin server, the website can load over HTTPS, and all traffic to and from the website will be encrypted and secure.

## Install the SSL/TLS Certificates:

Telnyx uses Cloudflare's [Universal TLS certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/), by default, Cloudflare issues and renews free, unshared, publicly trusted SSL certificates to all domains added to and activated on Cloudflare.

Universal certificates are [Domain Validated (DV)](https://developers.cloudflare.com/ssl/concepts/#validation-level). For setup details, refer to [Enable Universal](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/enable-universal-ssl/) SSL.

Cloudflare maintains the [trust store certificates](https://developers.cloudflare.com/ssl/concepts/#trust-store). A trust store is the list of certificate authority (CA) and intermediate certificates that are trusted by operating systems, web browsers, or other software that interacts with SSL/TLS certificates.

Cloudflare maintains its trust store on a public [GitHub repository](https://github.com/cloudflare/cfssl_trust).

More specifically the certificate that can be included in the trust store is [here](https://github.com/cloudflare/cfssl_trust/blob/master/ca-bundle.crt).

### Java Default Setting Via Terminal:

```
${JAVA_HOME}/lib/security/cacerts
```

If you (as a customer) are using Java defaults, then you do not need to take action to correctly validate the connection into [https://api.telnyx.com](https://portal.telnyx.com/#/login/sign-in).

If you are not using Java default ca certs store, you can import all trusted CA certificates used by Cloudflare using Java's key tool with the following steps:

1. Fetch CAs bundle published by Cloudflare: [https://github.com/cloudflare/cfssl\_trust/blob/master/ca-bundle.crt  
   ​](https://github.com/cloudflare/cfssl_trust/blob/master/ca-bundle.crt)
2. Add those certificates to the Java truststore you use.  
   ​

   ```
   # Fetch CA bundle from Cloudflare repo  
   $ curl -o cf-ca-bundle.crt -L https://raw.githubusercontent.com/cloudflare/cfssl_trust/master/ca-bundle.crt  
     
   # Split bundle in individual certs  
   $ csplit -f cf-ca-cert -z ca-bundle.crt '/-----BEGIN CERTIFICATE-----/' '{*}'  
     
   # Import the CA certs into an existing truststore file (eg: myTrustStoreFile). Adjust -storepass apropiately   
   $ for ca in ls cf-ca-cert*; do keytool -import -storepass changeit -keystore myTrustStoreFile -alias $ca -file $ca -noprompt; done
   ```

   ## Telnyx API Example of SSL/TLS Certificate Via Java

   We will use as an example, the [List notification channels](https://developers.telnyx.com/api/notifications/list-notification-channels) Telnyx API Java example:

   ```
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
   ```

   ```
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
   ```

   ### When we run it with the default Java JRE/JDK CA store, we will get the expected response:

   ```
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

   ### To see how the error would look like when the truststore doesn't contain the needed CA cert, we can perform the following quick test:

   ```
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
   ```

   ```
   # Run App again and it will fail  
   $ java -Djavax.net.ssl.trustStore=cacerts -Djavax.net.ssl.trustStorePassword=changeit App  
   Exception in thread "main" javax.net.ssl.SSLHandshakeException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target  
        at java.net.http/jdk.internal.net.http.HttpClientImpl.send(HttpClientImpl.java:560)  
        at java.net.http/jdk.internal.net.http.HttpClientFacade.send(HttpClientFacade.java:119)  
        at App.main(App.java:28)  
   Caused by: javax.net.ssl.SSLHandshakeException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target  
        at java.base/sun.security.ssl.Alert.createSSLException(Alert.java:131)  
   ...  
        at java.base/java.lang.Thread.run(Thread.java:831)  
   Caused by: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target  
        at java.base/sun.security.validator.PKIXValidator.doBuild(PKIXValidator.java:439)  
   ...  
       atjava.base/sun.security.ssl.CertificateMessage$T13CertificateConsumer.checkServerCerts(CertificateMessage.java:1335)  
   ... 21 more
   ```

   ```
   Caused by: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target  
        at java.base/sun.security.provider.certpath.SunCertPathBuilder.build(SunCertPathBuilder.java:141)  
   ...  
        at java.base/sun.security.validator.PKIXValidator.doBuild(PKIXValidator.java:434)  
   ...26more
   ```

   ### Configuring More SSL Certificates:

   If a customer wants to configure more SSL certificates for the [https://api.telnyx.com](https://portal.telnyx.com/#/login/sign-in) domain then you can configure more than one different type of public SSL certificate.

   Currently, Cloudflare can make a decision on which Certificate Authority (CA) uses that certificate for the customer.

   For [Universal SSL certificates](https://developers.cloudflare.com/ssl/edge-certificates/universal-ssl/limitations/#certificate-authority), Cloudflare chooses the certificate authority used for your certificate. Cloudflare can change the issuer for [https://api.telnyx.com](https://portal.telnyx.com/#/login/sign-in) certificates, but it will be listed in the links above.

   The following are the different types of certificates that can be included in the Trust Store.

   Cloudflare is using `[O = Baltimore, OU = CyberTrust](https://cacerts.digicert.com/BaltimoreCyberTrustRoot.crt.pem), [CN = Baltimore CyberTrust Root CA](https://cacerts.digicert.com/BaltimoreCyberTrustRoot.crt.pem) to sign [https://api.telnyx.com](https://portal.telnyx.com/#/login/sign-in). Including this certificate only in your truststore should be enough to validate connections to [https://api.telnyx.com](https://portal.telnyx.com/), but Cloudflare may change it at any time for other of its [supported CAs](https://developers.cloudflare.com/ssl/reference/certificate-authorities/).

   **For more help with this process please contact [support@telnyx.com](mailto:support@telnyx.com).**

---

Related Articles

[Understanding Telnyx SOC Compliance and Certifications](https://support.telnyx.com/en/articles/12397834-understanding-telnyx-soc-compliance-and-certifications)

Did this answer your question?

😞😐😃

Table of contents
