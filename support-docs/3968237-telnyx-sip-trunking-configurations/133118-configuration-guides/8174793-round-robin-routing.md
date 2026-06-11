---
source_url: https://support.telnyx.com/en/articles/8174793-round-robin-routing
scraped: 2026-06-11
---

Round Robin Routing | Telnyx Help Center

[Skip to main content](#main-content)

# Round Robin Routing

Round Robin routing helps customers implement a basic Load Balancing functionality from the connection.

Written by David

January 28, 2026

Table of contents

Round Robin is a type of routing that distributes inbound calls evenly between all the IPs in a connection. This is helpful because all IPs would receive an equal amount of inbound calls therefore helping balance the load of incoming calls to all the different systems in the connection instead of sending all calls to a single system and the other systems only acting as backups for whenever the main system fails.

# Setting up Round Robin Routing

So with a connection setup with 3 IPs, once calls start coming in, the first call would be sent to IP 1 then the second call to IP 2 then the third call to IP 3 then the fourth call to IP 1 then the fifth call to IP 2 then the sixth call to IP 4 and so on.

It's important to note that we only take into account inbound calls and not active calls for the load balancing itself. So if for some reason one of the systems is keeping calls active that system will still keep receiving the same amount of calls as the other systems regardless of the amount of active calls it's currently managing.

It's also important to note that in Round Robin routing all systems would effectively be used as failovers depending on the specific call. So for instance if a call is sent to IP 1 but fails then it will be sent to IP 2 and if that one fails it will continue to go down the list of IPs until all are exhausted or one of them answers. However if a call is originally sent to IP 2 as a first attempt then the rest of the IPs will still be used as backups including IP 1.

In general Round Robin provides a novel configuration option that lets customers distribute load evenly between several systems while also providing failover scenario using the same systems.

You can select the Round Robin routing method from the drop down menu labeled Default Routing Method in the Basic Settings of your connection.

[![](https://downloads.intercomcdn.com/i/o/ltcafuzd/1997260295/7c255374072467c0af2ad7260c4a/image.png?expires=1781168400&signature=15735bad0edee6456b27f52f9258dc026e88ba167eb908b85e7eaff6aef455f6&req=dSkuEct4nYNWXPMW1HO4zfp8wr5I9xZL%2BhJPWE52fZiY5fY8jG8%2FRMz6qoa8%0Adudq0%2FfQMHGqpmeg4Zs%3D%0A)](https://downloads.intercomcdn.com/i/o/ltcafuzd/1997260295/7c255374072467c0af2ad7260c4a/image.png?expires=1781168400&signature=15735bad0edee6456b27f52f9258dc026e88ba167eb908b85e7eaff6aef455f6&req=dSkuEct4nYNWXPMW1HO4zfp8wr5I9xZL%2BhJPWE52fZiY5fY8jG8%2FRMz6qoa8%0Adudq0%2FfQMHGqpmeg4Zs%3D%0A)

If you have any questions regarding how to set this up or any further questions regarding how it works reach out to our support team.

---

Related Articles

[How to configure a Thirdlane PBX](https://support.telnyx.com/en/articles/1130631-how-to-configure-a-thirdlane-pbx)[SIP Connection: Fail-over and Retries](https://support.telnyx.com/en/articles/4320364-sip-connection-fail-over-and-retries)[SIP Connection: Settings](https://support.telnyx.com/en/articles/4351104-sip-connection-settings)[Telnyx SIP Response Codes](https://support.telnyx.com/en/articles/4409457-telnyx-sip-response-codes)[SIP - Record Route Headers](https://support.telnyx.com/en/articles/9133298-sip-record-route-headers)

Did this answer your question?

😞😐😃

Table of contents
