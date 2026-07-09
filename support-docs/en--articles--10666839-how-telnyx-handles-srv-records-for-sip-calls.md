---
source_url: https://support.telnyx.com/en/articles/10666839-how-telnyx-handles-srv-records-for-sip-calls
scraped: 2026-07-08
content_hash: d2ae9b1cf77ffd7f28098cbfc0026cefa1f52577b088d7fcb213c7da10397d80
---

How Telnyx Handles SRV Records for SIP Calls | Telnyx Help Center

[Skip to main content](#main-content)

# How Telnyx Handles SRV Records for SIP Calls

SRV Records for SIP calls

Written by Cameron Fitzpatrick

April 7, 2026

This guide explains how Telnyx handles SRV records and provides insights into best practices for configuring SIP calls to ensure smooth operation.

---

### **What are SRV records?**

SRV (Service) records in DNS are used to specify the location of servers for specific services. For SIP traffic, SRV records enable the distribution of SIP requests across multiple hosts, providing load balancing and failover capabilities.

### **Where are SRV records used?**

SRV (Service) records in DNS are used in two different scenarios:

1. **SIP FQDN Connections**: the FQDN(s) of the Connection indicate Telnyx where to route Inbound calls.
2. **Voice API calls to external domains:** Customers can dial or transfer calls to external non Telnyx FQDNs.

Both of these FQDNs might have SRV records configured that Telnyx will honor.

---

### **How Telnyx Handles SRV Records**

When Telnyx receives a request to route a call to an external non Telnyx FQDN, it determines how to route the call based on the DNS records of the FQDN. This behavior depends on whether a port is specified in the RURI. **Telnyx will select the appropriate SRV record based on the transport protocol used in the SIP request**.

**RURI with a Port Number**

If the RURI contains a port number(e.g. `sip:+1234567890@sip.example.com:5060`):

1. **DNS Lookup:** Telnyx performs an A-record lookup, bypassing the SRV record.  
   ​
2. **Routing:** The call is routed to the IP address returned by the A-record lookup.

​

**RURI Without a Port Number**

If the RURI does not contain a port number (e.g. `sip:+1234567890@sip.example.com`):

1. **DNS Lookup:** Telnyx performs an SRV-record lookup.  
   ​
2. **Routing:** The SRV record dictates the server to which the call should be routed. If no SRV record exists, Telnyx will fall back to an A-record lookup and use the default SIP port (5060 for UDP/TCP or 5061 for TLS). If the first SRV target fails with a SIP 503 response, Telnyx will attempt the next highest priority target in the SRV list  
   ​

---

### **Key Considerations for Configuring SIP Calls**

1. **Remove Port Numbers for SRV Record Range**  
   To leverage SRV records, ensure the to header in your dial command does not include a port number. For example:  
   ​  
   - Incorrect: `"to" => "sip:+1234567890@sip.example.com:5060"`  
   ​  
   - Correct: `"to" => "sip:+1234567890@sip.example.com"`  
   ​
2. **Fallback Behaviour**  
   If an SRV record is not found:  
   ​  
   - Telnyx attempts an A-record lookup.  
   ​  
   - If no A-record exists, the call fails with a `SIP 478 (Unresolvable Destination) response`.  
   ​
3. **DNS Resolvability**  
   ​  
   - Ensure your DNS configuration is correct and resolvable globally.  
   ​  
   - Ensure SRV targets are properly configured with resolvable A records.   
   ​

---

### **Example Use Case**

A customer configures their to header with a domain and port, where the domain **sip.example.com** is an SRV record:

​`"to" => "sip:+1234567890@sip.example.com:5060"`

This results in an A-record lookup, which fails because there is no A-record for sip.example.com.

​**Solution:**

Remove the port number to allow SRV record processing

`"to":"sip:+1234567890@sip.example.com"`

This change enables Telnyx to perform an SRV lookup, correctly routing the call based on the SRV record.

---

### **Summary**

Customers should use SRV records for load balancing and failover by omitting the port number in the SIP "to" headers. You should ensure that DNS records (SRV and A records) are configured and resolvable, and if calls fail with a 478 response please verify that no port number is included in the RURI and that the SRV records are properly configured.

---

Related Articles

[SIP URI Calling](https://support.telnyx.com/en/articles/2925713-sip-uri-calling)[SIP Connection: Fail-over and Retries](https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries)[SIP Registration](https://support.telnyx.com/en/articles/4363904-sip-registration)[Grandstream GRP2612: SIP Trunk](https://support.telnyx.com/en/articles/6184147-grandstream-grp2612-sip-trunk)[Grandstream GXP1700: SIP Trunk](https://support.telnyx.com/en/articles/6184520-grandstream-gxp1700-sip-trunk)

Did this answer your question?

😞😐😃
