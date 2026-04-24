---
title: Using SIPREC client for Voice API and TeXML calls
summary: SIPREC client (SRC) is a component within the SIPREC framework.
sources:
  - url: https://developers.telnyx.com/docs/voice/programmable-voice/siprec-client/index
    content_hash: 1890bdbe9a0f3866a4918d3b872a52fb105a62c541ca1659bdd2a3ae34eb8b9a
updated_at: 2026-04-10T00:00:00Z
---

# Using SIPREC client for Voice API and TeXML calls

## What is a SIPREC client?

SIPREC client (SRC) is a component within the SIPREC framework. The SRC is responsible for initiating and managing the recording session, which communicates to the Session Recording Server (SRS) to send the media streams and metadata for recording.

## Creating a SIPREC server connector

To create an SIPREC recording session, you need to define an SIPREC server connector that will be used to establish a connection. It can be done using an API request as follows:

```bash theme={null}
curl --request POST \
  --url https://api.telnyx.com/v2/siprec_connectors \
  --header 'Authorization: Bearer XXX' \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "siprec-server-connector",
	"host": "siprec.telnyx.com",
	"port": 5060
}'
```

## Creating a SIPREC recording session for Voice API calls

To start a SIPREC recording session you can use the following request:

```bash theme={null}
curl --request POST \
  --url https://api.telnyx.com/v2/{call_control_id}/actions/siprec_start \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer XXX' \
  --header 'Content-Type: application/json' \
  --data '{
        "connector_name": "siprec-server-connector",
        "direction": "both_tracks"
   }'

```

The session can be stopped at any point using the `siprec_stop` endpoint:

```bash theme={null}
curl --request POST \
  --url https://api.telnyx.com/v2/{call_control_id}/actions/siprec_stop \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer XXX' \
  --header 'Content-Type: application/json'
```

## Creating a SIPREC recording session for TeXML calls

To initialize the SIPREC recording session the following TeXML instruction can be used:

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

    <Siprec track="both_tracks" connectorName="siprec-server-connector" statusCallback="https://example.com/siprec_callback" />

```

It can be stopped in the following way:

```xml theme={null}
<?xml version="1.0" encoding="UTF-8"?>

```


## Related Pages

- [Speech-to-Text with Voice API and TeXML](../runbooks/speech-to-text-with-voice-api-and-texml.md)
