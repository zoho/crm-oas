# Mass Update API

- [OpenAPI specification](mass_update.yaml)
- [Mass update records](mds/massUpdateRecords.md)
  - To update a specific field value across multiple records of a module in your Zoho CRM organization in a single API call. The operation supports two modes. In the non-scheduler mode, the caller supplies a list of record IDs in the `ids` array and the system updates those records synchronously, with a maximum of 500 records per request. In the scheduler mode, the caller supplies a Custom View ID in `cvid` and the request schedules an asynchronous background job that processes up to 50,000 records matching the view; the response returns a `job_id` that can be passed to the corresponding GET endpoint to track the job's progress. The Deals module accepts up to three fields per request; all other supported modules accept only one field per request. Email, lookup, multi-line, layout, and line item fields cannot be mass updated.
  - [Examples](mds/examples/massUpdateRecords.md)
- [Get mass update job status](mds/getMassUpdateStatus.md)
  - To retrieve the current status and record-processing counts of an asynchronous mass update job that was previously scheduled in your Zoho CRM organization. The job is identified by the `job_id` returned in the response of the scheduler-type mass update request. The response reports the job state along with the total, updated, not-updated, and failed record counts so that the caller can track progress until the job completes.
  - [Examples](mds/examples/getMassUpdateStatus.md)
