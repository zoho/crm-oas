# Bulk Write

- [OpenAPI specification](bulk_write.yaml)
- [Create a bulk write job](mds/createBulkWriteJob.md)
  - To create a bulk write job in your Zoho CRM organization that creates, updates, or upserts records in a target module from a previously uploaded file. The job is processed asynchronously; the response returns the job identifier that the get job details operation uses to poll job status, and an optional callback URL is notified on completion or failure.
  - [Examples](mds/examples/createBulkWriteJob.md)
- [Get bulk write job details](mds/getBulkWriteJobDetails.md)
  - To retrieve the details of a previously created bulk write job in your Zoho CRM organization, including its current status, per-resource and per-file processing counts, the creator, and the download URL of the result archive once the job completes. The download URL remains accessible for up to seven days after the job completes.
  - [Examples](mds/examples/getBulkWriteJobDetails.md)
