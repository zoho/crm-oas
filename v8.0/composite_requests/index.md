# Composite Request

- [OpenAPI specification](composite_requests.yaml)
- [Process multiple API requests in a single call](mds/createCompositeRequest.md)
  - To bundle multiple Zoho CRM API requests into a single HTTP call, reducing network round-trips and enabling request chaining. You can reference the output of one sub-request in another using the format **@{sub_request_id:JSONPath}** to build dependent workflows. When **rollback_on_fail** is enabled, all successful sub-requests are rolled back if any subsequent sub-request fails.
  - [Examples](mds/examples/createCompositeRequest.md)
