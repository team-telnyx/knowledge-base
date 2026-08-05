---
title: AWS SDK Examples for Telnyx Cloud Storage
summary: Telnyx Cloud Storage is S3-compatible, so the official AWS SDKs can be used
  in any language to create buckets, upload and download objects, list contents, and
  generate presigned URLs. This page collects working examples for .NET, Elixir, Go,
  Java, Node.js, PHP, Python, and Ruby, including the client configuration quirks
  (endpoint, credentials, checksum settings) each SDK requires.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/node/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/php
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/python
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/ruby
updated_at: 2026-08-05T13:40:27Z
---

# AWS SDK Examples for Telnyx Cloud Storage

*Part 1 of 4 — see also: [Part 2](aws-sdk-examples-for-telnyx-cloud-storage--part-2.md), [Part 3](aws-sdk-examples-for-telnyx-cloud-storage--part-3.md), [Part 4](aws-sdk-examples-for-telnyx-cloud-storage--part-4.md)*

Telnyx Cloud Storage is S3-compatible, so the official AWS SDKs can be used in any language to create buckets, upload and download objects, list contents, and generate presigned URLs. This page collects working examples for .NET, Elixir, Go, Java, Node.js, PHP, Python, and Ruby, including the client configuration quirks (endpoint, credentials, checksum settings) each SDK requires.

## Overview

Telnyx Cloud Storage exposes an S3-compatible API, which means the official AWS SDKs can be used directly from any language. In every example below the client is pointed at a regional Telnyx endpoint of the form `https://<region>.telnyxcloudstorage.com` (commonly `us-central-1`) and authenticated with a Telnyx API key. The same key is supplied as both the access key ID and the secret access key — the secret value is ignored by Telnyx, so any non-empty string (or the API key itself) is acceptable.

All examples walk through the same end-to-end flow:

1. Initialize the AWS client against the Telnyx endpoint.
2. Create a bucket.
3. Upload one or more objects.
4. List the objects in the bucket.
5. Download an object.
6. Request a presigned URL from the Telnyx REST API.
7. Use the presigned URL to download (or, in some examples, upload) the object.

The presigned URL endpoint is always `POST https://api.telnyx.com/v2/storage/buckets/{bucket}/{object}/presigned_url` with a JSON body of `{"ttl": <seconds>}` and an `Authorization: Bearer <TELNYX_API_KEY>` header. The response contains a `data.presigned_url` field that can be used directly with any HTTP client.

## .NET (AWS SDK for .NET)

The .NET SDK requires `ForcePathStyle = true`, `SignatureVersion = "4"`, and — critically — chunk encoding must be disabled on every `PutObjectRequest` because the Cloud Storage API does not support it.

```csharp
using System.Text;
using System.Text.Json;
using Amazon.Runtime;
using Amazon.S3;
using Amazon.S3.Model;

var apiKeyTelnyx = "API-KEY-HERE";
var bucketName = "BUCKET-NAME-HERE";
var objectName = "OBJECT-NAME-HERE";
var region = "us-central-1";

var s3Config = new AmazonS3Config
{
   ServiceURL = $"https://{region}.telnyxcloudstorage.com",
   ForcePathStyle = true,
   LogResponse = true,
   DisableLogging = false,
   SignatureVersion = "4",
};

var telnyxClient = new AmazonS3Client(
   new BasicAWSCredentials(apiKeyTelnyx, apiKeyTelnyx),
   s3Config
);

// Create bucket
await telnyxClient.PutBucketAsync(new PutBucketRequest { BucketName = bucketName });

// Upload object (chunk encoding MUST be disabled)
var putObjectRequest = new PutObjectRequest
{
   BucketName = bucketName,
   Key = "objectName",
   FilePath = "/Users/yiuming/test.txt"
};
putObjectRequest.UseChunkEncoding = false;
await telnyxClient.PutObjectAsync(putObjectRequest);

// List objects
await telnyxClient.ListObjectsAsync(new ListObjectsRequest { BucketName = bucketName });

// List buckets
await telnyxClient.ListBucketsAsync(new ListBucketsRequest { });

// Download object
await telnyxClient.GetObjectAsync(new GetObjectRequest { BucketName = bucketName, Key = objectName });

// Presigned URL via the Telnyx REST API
using (HttpClient client = new HttpClient())
{
   client.BaseAddress = new Uri("https://api.telnyx.com");
   var presignedUrlRequestJson = JsonSerializer.Serialize(new Dictionary<string, object> { { "ttl", 200 } });
   var presignedUrlRequestContent = new StringContent(presignedUrlRequestJson, Encoding.UTF8, "application/json");
   client.DefaultRequestHeaders.Authorization =
       new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", apiKeyTelnyx);
   var presignedUrlResponse =
       await client.PostAsync($"/v2/storage/buckets/{bucketName}/{objectName}/presigned_url", presignedUrlRequestContent);
   Console.WriteLine(await presignedUrlResponse.Content.ReadAsStringAsync());
}
```

## Elixir (AWS Elixir SDK)

Add the following dependencies to `mix.exs`:

```elixir
{:aws, "~> 1.0.0"},
{:hackney, "~> 1.18"}
```

The client is created with the Telnyx API key as the access key, a blank secret, and a custom endpoint resolver that rewrites the host to `<region>.telnyxcloudstorage.com`.

```elixir
telnyx_storage_client =
  AWS.Client.create(
    System.fetch_env!("TELNYX_V2_API_KEY"),
    "",
    System.get_env("TELNYX_STORAGE_REGION", "us-east-1")
  )
  |> AWS.Client.put_endpoint(fn options -> "#{options.region}.telnyxcloudstorage.com" end)

bucket_name = System.get_env("TELNYX_STORAGE_BUCKET_NAME", "my-test-bucket-#{Enum.random(1..1_000_000)}")

{:ok, _, _} = AWS.S3.create_bucket(telnyx_storage_client, bucket_name, %{})

for i <- 1..2 do
  object_key = "object-#{i}.bin"
  upload_request = %{
    "Body" => :rand.bytes(42),
    "ContentType" => "application/octet-stream"
  }
  {:ok, _, _} = AWS.S3.put_object(telnyx_storage_client, bucket_name, object_key, upload_request)
end

{:ok, %{"ListBucketResult" => bucket_details}, _} = AWS.S3.list_objects(telnyx_storage_client, bucket_name)

Enum.each(bucket_details["Contents"], fn content ->
  IO.puts("Object key: #{content["Key"]}")
end)

object_key = List.first(bucket_details["Contents"])["Key"]
{:ok, %{"Body" => object_data}, _} = AWS.S3.get_object(telnyx_storage_client, bucket_name, object_key)
IO.puts("Downloaded object data: #{inspect(object_data)}")
```

For presigned URLs, add `{:req, "~> 0.5"}` and `{:jason, "~> 1.4"}` to `mix.exs`:

```elixir
url = "https://api.telnyx.com/v2/storage/buckets/#{bucket_name}/#{object_key}/presigned_url"
api_key = System.fetch_env!("TELNYX_V2_API_KEY")

headers = %{
  "authorization" => "Bearer #{api_key}",
  "content_type" => "application/json",
  "accept" => "application/json"
}

body = %{"ttl" => 30}

{:ok, %{body: %{"data" => %{"presigned_url" => presigned_url}}}} = Req.post(url, headers: headers, json: body)

{:ok, %{body: object_data}} = Req.get(presigned_url)
IO.puts("Downloaded object data using presigned URL: #{inspect(object_data)}")
```
