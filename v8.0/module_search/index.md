# Search Records

- [OpenAPI specification](module_search.yaml)
- [Bulk Search Records by Criteria, Word, Email, or Phone](operations/bulkSearchRecords/operation.md)
  - Searches for records in the specified module that match the given search criteria. This API accepts the same search parameters as the GET /{module}/search API, but they are provided in the request body instead of query parameters. Use this API when the search criteria are too long to be passed as query parameters. You must specify at least one of the following search parameters: criteria, email, phone, or word. A maximum of 2,000 records can be retrieved per search, with up to 15 criteria conditions. Newly created or updated records may not appear immediately in the search results due to indexing delays.
  - [Examples](operations/bulkSearchRecords/examples/)
- [Search Records by Criteria, Word, Email, or Phone](operations/searchRecords/operation.md)
  - To search for records within a specified module in your Zoho CRM organization using criteria-based conditions, full-text word search, or lookup by email or phone number.
  - [Examples](operations/searchRecords/examples/)
