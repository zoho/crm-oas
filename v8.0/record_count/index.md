# Module Record Count

- [OpenAPI specification](record_count.yaml)
- [Module Record Count](mds/getRecordCount.md)
  - To retrieve the total number of records in a specified Zoho CRM module, optionally filtered by a Custom View or search criteria. The count can be filtered using `cvid` (Custom View ID) or search parameters (`criteria`, `email`, `phone`, or `word`). These two filter groups are mutually exclusive - they cannot be combined in the same request. The `converted` and `approved` parameters apply only to the Leads module. The `type` parameter applies only to the Users module. Note: The record count may take 1-10 minutes to reflect the latest changes in Zoho CRM. The count can be filtered using `cvid` (Custom View ID) or one of the search parameters (`criteria`, `phone`, `email`, `word`). **Important Constraint (Zoho Documentation):** You can only include **either** `cvid` **or** one of the search parameters (`criteria`, `phone`, `email`, `word`) in a single request. Combining `cvid` with any search parameter will result in an `AMBIGUITY_DURING_PROCESSING` error (HTTP 400).
  - [Examples](mds/examples/getRecordCount.md)
