---
source_url: https://support.telnyx.com/en/articles/8268648-webhook-issue-ca-error
scraped: 2026-07-08
content_hash: 33f2a911f356445a83cfd50c5edc338ef9247777c8cbf29a8763ed2b29a74989
---

Webhook Issue: CA Error | Telnyx Help Center

[Skip to main content](#main-content)

# Webhook Issue: CA Error

Join Telnyx's Reseller Program. Earn commissions & leverage cutting-edge telecom tech!

K

Written by Klane Pedrie

October 30, 2023

Table of contents

# Primary Webhook Not Triggering because of Error: certificate authority (CA) isn’t recognized

If the error says the certificate authority (CA) isn’t recognized and your payload is being sent to the failover webhook url instead of the primary then that means the connection can’t be established over https.

We have two options here:

(a) make sure your server has a certificate that is signed by a known CA

or

(b) use http instead of https  
​  
​[More about Certificate Authority.](https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com)

---

Related Articles

[How to Leverage Webhooks](https://support.telnyx.com/en/articles/4334722-how-to-leverage-webhooks)[Certificate Error: api.telnyx.com](https://support.telnyx.com/en/articles/7984783-certificate-error-api-telnyx-com)

Did this answer your question?

😞😐😃

Table of contents
