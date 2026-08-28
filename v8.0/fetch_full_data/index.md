# Fetch Full Data

- [OpenAPI specification](fetch_full_data.yaml)
- [Rich text field content for multiple records](mds/fetchFullDataForMultipleRecords.md)
  - Retrieves the full content of rich text multi-line fields for multiple records in a single request. Both the 'ids' and 'fields' query parameters are mandatory. You can specify up to 200 record IDs in the 'ids' parameter and up to 8 rich text field API names in the 'fields' parameter. This API exclusively fetches rich text fields - other field types are not supported. Only data from rich text multi-line fields can be retrieved; multi-line fields of other types (small, large) are not supported.
  - [Examples](mds/examples/fetchFullDataForMultipleRecords.md)
- [Rich text field content for a specific record](mds/fetchFullDataForSingleRecord.md)
  - Retrieves the full content of rich text multi-line fields for a specific record identified by its record ID in the path. The 'fields' query parameter is optional for this endpoint - if omitted, all rich text fields of the record are returned. When specified, only the listed rich text fields are fetched. This API exclusively fetches rich text fields - other field types are not supported. Only data from rich text multi-line fields can be retrieved; multi-line fields of other types (small, large) are not supported.
  - [Examples](mds/examples/fetchFullDataForSingleRecord.md)
