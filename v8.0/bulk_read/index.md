# Bulk Read

- [OpenAPI specification](bulk_read.yaml)
- [Create a bulk read job](mds/createBulkReadJob.md)
  - To create a bulk read job in Zoho CRM. A bulk read job exports records from a specified CRM module to a CSV or ICS file. The job runs asynchronously; use the Get Bulk Read Job Details API to monitor the job status, and use the Download Bulk Read Result API to retrieve the exported file once the job is complete.
  - [Examples](mds/examples/createBulkReadJob.md)
- [Get bulk read job details](mds/getBulkReadJobDetails.md)
  - To retrieve the details of a bulk read job in Zoho CRM. Use this API to check the current state of a bulk read job and obtain the download URL once the job is complete. Specify the unique job ID that Zoho CRM returned when you created the job.
  - [Examples](mds/examples/getBulkReadJobDetails.md)
- [Download bulk read result](mds/downloadBulkReadResult.md)
  - To download the exported records from a completed bulk read job in Zoho CRM. This API returns a ZIP archive containing the CSV or ICS file with the exported records. The bulk read job must have a COMPLETED state before you can download the result.
  - [Examples](mds/examples/downloadBulkReadResult.md)
