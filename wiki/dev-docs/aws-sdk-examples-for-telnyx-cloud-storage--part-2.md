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

*Part 2 of 4 — see also: [Part 1](aws-sdk-examples-for-telnyx-cloud-storage--part-1.md), [Part 3](aws-sdk-examples-for-telnyx-cloud-storage--part-3.md), [Part 4](aws-sdk-examples-for-telnyx-cloud-storage--part-4.md)*

Telnyx Cloud Storage is S3-compatible, so the official AWS SDKs can be used in any language to create buckets, upload and download objects, list contents, and generate presigned URLs. This page collects working examples for .NET, Elixir, Go, Java, Node.js, PHP, Python, and Ruby, including the client configuration quirks (endpoint, credentials, checksum settings) each SDK requires.

## Go (AWS SDK for Go v2)

The Go SDK uses `aws.CredentialsProviderFunc` to inject the Telnyx API key as both the access key ID and secret access key, and sets `BaseEndpoint` to the regional Telnyx URL. The example creates a uniquely named bucket, uploads two random 32 KiB objects, lists them, downloads one, and then exercises the presigned URL flow.

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

	ts := time.Now()
	bucketName := fmt.Sprintf("%v-%s.%v-%v.%v", "test-bucket", region, ts.Hour(), ts.Minute(), randSeq)

	objs := make(map[string]*bytes.Reader)
	for i := 0; i < 2; i++ {
		ct := make([]byte, 1024*32)
		crand.Read(ct)
		objs[fmt.Sprintf("%v.txt", i)] = bytes.NewReader(ct)
	}

	_, err = s3Client.CreateBucket(ctx, &s3.CreateBucketInput{Bucket: aws.String(bucketName)})
	if err != nil {
		log.Fatalf("unable to create bucket: %v", err)
	}

	for objName, body := range objs {
		_, err = s3Client.PutObject(ctx, &s3.PutObjectInput{
			Bucket: aws.String(bucketName),
			Key:    aws.String(objName),
			Body:   body,
		})
		if err != nil {
			log.Fatalf("unable to upload file (%v): %v", objName, err)
		}
	}

	listObj, err := s3Client.ListObjectsV2(ctx, &s3.ListObjectsV2Input{Bucket: aws.String(bucketName)})
	if err != nil {
		log.Fatalf("unable to list objects: %v", err)
	}
	for _, item := range listObj.Contents {
		log.Printf("Listed object: %v", *item.Key)
	}

	out, err := s3Client.GetObject(ctx, &s3.GetObjectInput{
		Bucket: aws.String(bucketName),
		Key:    aws.String("1.txt"),
	})
	if err != nil {
		log.Fatalf("unable to download object: %v", err)
	}
	defer out.Body.Close()

	dl, err := io.ReadAll(out.Body)
	if err != nil {
		log.Fatalf("unable to read object data: %v", err)
	}
	log.Printf("downloaded file size: %d", len(dl))

	url := fmt.Sprintf("https://api.telnyx.com/v2/storage/buckets/%v/%v/presigned_url", bucketName, "1.txt")
	req, err := http.NewRequest(http.MethodPost, url, bytes.NewReader([]byte(`{"ttl": 30}`)))
	if err != nil {
		log.Fatalf("unable to create presigned request: %v", err)
	}
	req.Header.Set("Authorization", "Bearer "+telnyxAPIKey)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		log.Fatalf("unable to send presigned request: %v", err)
	}
	defer resp.Body.Close()

	type presignedURL struct {
		Data struct {
			Token        string    `json:"token"`
			ExpiresAt    time.Time `json:"expires_at"`
			PresignedURL string    `json:"presigned_url"`
		} `json:"data"`
	}

	var purl presignedURL
	if err := json.NewDecoder(resp.Body).Decode(&purl); err != nil {
		log.Fatalf("unable to decode presigned URL: %v", err)
	}
	log.Printf("Generated presigned URL: %v", purl.Data.PresignedURL)

	res, err := http.Get(purl.Data.PresignedURL)
	if err != nil {
		log.Fatalf("unable to download presigned URL: %v", err)
	}
	defer res.Body.Close()
	log.Printf("Downloaded presigned URL status code: %v", res.StatusCode)
}
```

Run with `TELNYX_API_KEY=_YOUR_API_KEY go run main.go`.
