---
title: AWS Golang SDK Example
summary: The following example shows how AWS Golang SDK can be used to interact with Telnyx Cloud Storage.
sources:
  - url: https://developers.telnyx.com/docs/cloud-storage/sdk/golang/index
    content_hash: 01cc75b680c8de0e4dc010796eec83bb8d4da021c12fe943b77a978fbc637557
updated_at: 2026-04-10T00:00:00Z
---

# AWS Golang SDK Example

The following example shows how AWS Golang SDK can be used to interact with Telnyx Cloud Storage.

```
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

	// 1. Initializing the AWS client with specific options
	cfg, err := config.LoadDefaultConfig(ctx,
    	config.WithRegion(region),
    	config.WithCredentialsProvider(aws.CredentialsProviderFunc(
        	func(context.Context) (aws.Credentials, error) {
            	return aws.Credentials{
                	AccessKeyID: 	telnyxAPIKey, // Use your Telnyx API key
                	SecretAccessKey: telnyxAPIKey, // Optional, can be left blank
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
	log.Printf("Created S3 client for region (%v) and endpoint (%v)", cfg.Region, *cfg.BaseEndpoint)

	// test-bucket-us-central-1.23-34.randomNumber
	ts := time.Now()
	bucketName := fmt.Sprintf("%v-%s.%v-%v.%v", "test-bucket", region, ts.Hour(), ts.Minute(), randSeq)
	log.Printf("Generated bucket name: %q", bucketName)

	// Create two objects in memory
	objs := make(map[string]*bytes.Reader)
	noFiles := 2
	for i := 0; i < noFiles; i++ {
    	ct := make([]byte, 1024*32)
    	// fill with random data
    	if _, err := crand.Read(ct); err != nil {
        	log.Fatalf("failed to read random data: %v", err)
    	}

    	objName := fmt.Sprintf("%v.txt", i)
    	objs[objName] = bytes.NewReader(ct)
	}

	// 2. Create a bucket
	_, err = s3Client.CreateBucket(ctx, &s3.CreateBucketInput{
    	Bucket: aws.String(bucketName),
	})
	if err != nil {
    	log.Fatalf("unable to create bucket: %v", err)
	}
	log.Printf("Created bucket: %v", bucketName)

	// 3. Upload the two objects into the newly created bucket
	for objName, body := range objs {
    	if _, err = s3Client.PutObject(ctx, &s3.PutObjectInput{
        	Bucket: aws.String(bucketName),
        	Key:	aws.String(objName),
        	Body:   body,
    	}); err != nil {
        	log.Fatalf("unable to upload file (%v): %v", objName, err)
    	}

    	log.Printf("Uploaded file (%v) to bucket: %v", objName, bucketName)
	}

	// 4. List objects in the bucket
	listObj, err := s3Client.ListObjectsV2(ctx, &s3.ListObjectsV2Input{
    	Bucket: aws.String(bucketName),
	})
	if err != nil {
    	log.Fatalf("unable to list objects: %v", err)
	}

	for _, item := range listObj.Contents {
    	log.Printf("Listed object: %v", *item.Key)
	}

	// 5. Download the object first
	out, err := s3Client.GetObject(ctx, &s3.GetObjectInput{
    	Bucket: aws.String(bucketName),
    	Key:	aws.String("1.txt"),
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

	// 6. Create a presigned URL for the first file
	url := fmt.Sprintf("https://api.telnyx.com/v2/storage/buckets/%v/%v/presigned_url", bucketName, "1.txt")

	req, err := http.NewRequest(http.MethodPost, url, bytes.NewReader([]byte(`{"TTL": 30}`)))
	if err != nil {
    	log.Fatalf("unable to create presigned request: %v", err)
	}
	req.Header.Set("Authorization", "Bearer "+telnyxAPIKey)

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
    	log.Fatalf("unable to send presigned request: %v", err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
    	b, _ := io.ReadAll(resp.Body)
    	log.Fatalf("unexpected status code: %v | response: %s", resp.StatusCode, b)
	}

	type presignedURL struct {
    	Data struct {
        	Token    	string	`json:"token"`
        	ExpiresAt	time.Time `json:"expires_at"`
        	PresignedURL string	`json:"presigned_url"`
    	} `json:"data"`
	}

	var purl presignedURL
	if err := json.NewDecoder(resp.Body).Decode(&purl); err != nil {
    	log.Fatalf("unable to decode presigned URL: %v", err)
	}

	log.Printf("Generated presigned URL: %v", purl.Data.PresignedURL)

	// 7. Download the file again using the presigned URL
	res, err := http.Get(purl.Data.PresignedURL)
	if err != nil {
    	log.Fatalf("unable to download presigned URL: %v", err)
	}
	defer res.Body.Close()

	log.Printf("Downloaded presigned URL status code: %v", res.StatusCode)
}

```

Run the program.

```bash theme={null}
TELNYX_API_KEY=_YOUR_API_KEY go run main.go

2024/08/15 13:14:29 Created S3 client for region (us-central-1) and endpoint (https://us-central-1.telnyxcloudstorage.com)
2024/08/15 13:14:29 Generated bucket name: "test-bucket-us-central-1.13-14.536341"
2024/08/15 13:14:30 Created bucket: test-bucket-us-central-1.13-14.536341
2024/08/15 13:14:31 Uploaded file (0.txt) to bucket: test-bucket-us-central-1.13-14.536341
2024/08/15 13:14:31 Uploaded file (1.txt) to bucket: test-bucket-us-central-1.13-14.536341
2024/08/15 13:14:31 Listed object: 0.txt
2024/08/15 13:14:31 Listed object: 1.txt
2024/08/15 13:14:32 downloaded file size: 32768
2024/08/15 13:14:32 Generated presigned URL: https://us-central-1.telnyxcloudstorage.com/test-bucket-us-central-1.13-14.536341/1.txt?X-AMZ-Security-Token=sometoken
2024/08/15 13:14:33 Downloaded presigned URL status code: 200

```


## Related Pages

- [AWS .Net SDK Example](../runbooks/aws-net-sdk-example.md)
- [AWS Java SDK Example](../runbooks/aws-java-sdk-example.md)
- [AWS PHP SDK Example](../runbooks/aws-php-sdk-example.md)
- [AWS Elixir SDK Example](../runbooks/aws-elixir-sdk-example.md)
- [AWS Node.js SDK Example](../runbooks/aws-node-js-sdk-example.md)
