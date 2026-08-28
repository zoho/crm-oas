# Find And Merge

- [OpenAPI specification](find_and_merge.yaml)
- [Get Merge Job Status](mds/getMergeJobStatus.md)
  - To retrieve the status of a scheduled merge job in your Zoho CRM organization. Use the optional job_id query parameter to filter results to a specific job.
  - [Examples](mds/examples/getMergeJobStatus.md)
- [Merge Records](mds/mergeRecords.md)
  - To merge duplicate records in your Zoho CRM organization into a single master record. Supports field-level value selection from child records and file attachment management. If a child record has more than 1000 related records, the merge processes asynchronously and returns a job_id for status tracking.
  - [Examples](mds/examples/mergeRecords.md)
