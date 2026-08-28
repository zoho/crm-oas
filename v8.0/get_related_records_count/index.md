# Related Records Count

- [OpenAPI specification](get_related_records_count.yaml)
- [Get related records count](mds/getRelatedRecordsCount.md)
  - To retrieve the count of related records for a specified parent record in your Zoho CRM organization. Supports optional filtering by approval status, conversion status, category type, and field-level equality criteria. A single request can include up to 20 related list count specifications. You can use this API to get the count of records in the following types of related lists: - **System-defined related lists**, such as: - Survey - Desk - Projects - Visits - Expense - Invoice - Subscription - **Custom related lists** created via Lookup fields. - **Custom related lists** created via Multi-select Lookup fields. - **Custom related lists** created via Multi-module Lookup fields. - **Related lists** created when history tracking is enabled for a picklist field.
  - [Examples](mds/examples/getRelatedRecordsCount.md)
