---
title: AWS Elixir SDK Example
summary: The following example shows how AWS Elixir SDK can be used to interact with Telnyx Cloud Storage.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir/index
    content_hash: b15866baa4fc8e6952a795808edd9f64045f5d05a84494eddaa925c0244caadb
updated_at: 2026-04-10T00:00:00Z
---

# AWS Elixir SDK Example

The following example shows how AWS Elixir SDK can be used to interact with Telnyx Cloud Storage.

This example requires the following dependencies be added to your mix.exs file

```elixir theme={null}
  {:aws, "~> 1.0.0"},
  {:hackney, "~> 1.18"}
```

```elixir theme={null}
telnyx_storage_client =
	AWS.Client.create(
  	System.fetch_env!("TELNYX_V2_API_KEY"),
  	# secret access key can be left blank for Telnyx Storage
  	"",
  	System.get_env("TELNYX_STORAGE_REGION", "us-east-1")
	)
	|> AWS.Client.put_endpoint(fn options -> "#{options.region}.telnyxcloudstorage.com" end)


## Related Pages

- [AWS .Net SDK Example](../runbooks/aws-net-sdk-example.md)
- [AWS PHP SDK Example](../runbooks/aws-php-sdk-example.md)
- [AWS Golang SDK Example](../runbooks/aws-golang-sdk-example.md)
- [AWS Java SDK Example](../runbooks/aws-java-sdk-example.md)
- [AWS Node.js SDK Example](../runbooks/aws-node-js-sdk-example.md)
