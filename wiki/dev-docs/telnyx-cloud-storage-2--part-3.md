---
title: Telnyx Cloud Storage
summary: Telnyx Cloud Storage is an S3-compatible object storage service with regional
  endpoints in the US and EU, supporting standard S3 operations via AWS CLI, SDKs,
  and third-party tools. It offers features such as multipart uploads, server-side
  encryption with customer keys (SSE-C), presigned URLs, public bucket policies, and
  a migration API for moving data from AWS S3 without incurring egress charges.
sources:
- url: https://developers.telnyx.com/docs/cloud-storage/limits
- url: https://developers.telnyx.com/docs/cloud-storage/migrating-from-aws
- url: https://developers.telnyx.com/docs/cloud-storage/multipart-upload/index
- url: https://developers.telnyx.com/docs/cloud-storage/object-encryption
- url: https://developers.telnyx.com/docs/cloud-storage/performance-benchmarks
- url: https://developers.telnyx.com/docs/cloud-storage/presigned-urls
- url: https://developers.telnyx.com/docs/cloud-storage/public-buckets
- url: https://developers.telnyx.com/docs/cloud-storage/quick-start/index
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/dotnet
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/elixir
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang
- url: https://developers.telnyx.com/docs/cloud-storage/sdk/java
updated_at: 2026-06-11T10:25:05Z
---

# Telnyx Cloud Storage

*Part 3 of 3 — see also: [Part 1](telnyx-cloud-storage-2--part-1.md), [Part 2](telnyx-cloud-storage-2--part-2.md)*

Telnyx Cloud Storage is an S3-compatible object storage service with regional endpoints in the US and EU, supporting standard S3 operations via AWS CLI, SDKs, and third-party tools. It offers features such as multipart uploads, server-side encryption with customer keys (SSE-C), presigned URLs, public bucket policies, and a migration API for moving data from AWS S3 without incurring egress charges.

## SDK Examples

### Common Configuration Notes

- Use your Telnyx API key as both the access key ID and secret access key when configuring AWS SDK credentials.
- Set the endpoint to `https://{region}.telnyxcloudstorage.com`.
- **Chunk encoding is not supported** by the Cloud Storage API. In the .NET SDK, set `putObjectRequest.UseChunkEncoding = false`.
- **For AWS Java SDK v2.30+**, disable checksum calculation and verification by setting `requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)` and `responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)`.
- Presigned URLs must be generated via the Telnyx API, not via the SDK's built-in presigned URL methods.

### Go (AWS SDK for Go v2)

```go
package main

import (
    "bytes"
    "context"
    crand "crypto/rand"
    "encoding/json"
    "fmt"
    "io"
    "log"
    "math/rand"
    "net/http"
    "os"
    "time"

    "github.com/aws/aws-sdk-go-v2/aws"
    "github.com/aws/aws-sdk-go-v2/config"
    "github.com/aws/aws-sdk-go-v2/service/s3"
)

func main() {
    ctx := context.Background()
    randSeq := rand.Intn(1_000_000)

    telnyxAPIKey := os.Getenv("TELNYX_API_KEY")
    if telnyxAPIKey == "" {
        log.Fatal("TELNYX_API_KEY environment variable not set")
    }

    region := "us-central-1"
    endpoint := fmt.Sprintf("https://%s.telnyxcloudstorage.com", region)

    cfg, err := config.LoadDefaultConfig(ctx,
        config.WithRegion(region),
        config.WithCredentialsProvider(aws.CredentialsProviderFunc(
            func(context.Context) (aws.Credentials, error) {
                return aws.Credentials{
                    AccessKeyID:     telnyxAPIKey,
                    SecretAccessKey: telnyxAPIKey,
                }, nil
            })),
        config.WithS3UseARNRegion(true),
        config.WithS3DisableExpressAuth(true),
        config.WithS3DisableMultiRegionAccessPoints(true),
    )
    if err != nil {
        log.Fatalf("s3 configuration error: %v", err)
    }
    cfg.BaseEndpoint = aws.String(endpoint)

    s3Client := s3.NewFromConfig(cfg)

    // Create bucket, upload objects, list objects, download objects, and
    // generate presigned URLs via the Telnyx API as shown in the full example.
    _ = s3Client
    _ = randSeq
}
```

Run with `TELNYX_API_KEY=_YOUR_API_KEY go run main.go`.

### Java (AWS SDK for Java v2)

Add the dependency:

```xml
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>s3</artifactId>
    <version>2.20.0</version>
</dependency>
```

Create an S3 client:

```java
S3Client s3 = S3Client.builder()
    .region(Region.US_EAST_1)
    .endpointOverride(URI.create("https://us-central-1.telnyxcloudstorage.com"))
    .requestChecksumCalculation(RequestChecksumCalculation.WHEN_REQUIRED)
    .responseChecksumValidation(ResponseChecksumValidation.WHEN_REQUIRED)
    .credentialsProvider(
        StaticCredentialsProvider.create(
            AwsBasicCredentials.create(telnyxApiKey, "does not matter")))
    .build();
```

For presigned URLs, call the Telnyx API directly using an HTTP client (e.g., OkHttp) with a JSON body `{"TTL": 30}` to `POST /v2/storage/buckets/{bucket}/{key}/presigned_url`.

### .NET (AWS SDK for .NET)

```csharp
var s3Config = new AmazonS3Config
{
    ServiceURL = $"https://{region}.telnyxcloudstorage.com",
    ForcePathStyle = true,
    SignatureVersion = "4",
};

var telnyxClient = new AmazonS3Client(
    new BasicAWSCredentials(apiKeyTelnyx, apiKeyTelnyx),
    s3Config
);
```

**Important**: Set `putObjectRequest.UseChunkEncoding = false` since chunk encoding is not supported.

For presigned URLs, use `HttpClient` to call `POST /v2/storage/buckets/{bucket}/{key}/presigned_url` with a JSON body `{"ttl": 200}` and a Bearer authorization header.

### Elixir (AWS Elixir SDK)

Add dependencies to `mix.exs`:

```elixir
{:aws, "~> 1.0.0"},
{:hackney, "~> 1.18"}
```

Create the client:

```elixir
telnyx_storage_client =
  AWS.Client.create(
    System.fetch_env!("TELNYX_V2_API_KEY"),
    "",  # secret access key can be left blank
    System.get_env("TELNYX_STORAGE_REGION", "us-east-1")
  )
  |> AWS.Client.put_endpoint(fn options -> "#{options.region}.telnyxcloudstorage.com" end)
```

For presigned URLs, use the `Req` library with `Jason` to call the Telnyx API:

```elixir
{:ok, %{body: %{"data" => %{"presigned_url" => presigned_url}}}} =
  Req.post("https://api.telnyx.com/v2/storage/buckets/#{bucket_name}/#{object_key}/presigned_url",
    headers: %{"authorization" => "Bearer #{api_key}"},
    json: %{"ttl" => 30}
  )
```
