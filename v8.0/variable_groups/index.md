# Variable Groups

- [OpenAPI specification](variable_groups.yaml)
- [Variable Groups](mds/getVariableGroups.md)
  - To retrieve a list of all variable groups in your Zoho CRM organization.
  - [Examples](mds/examples/getVariableGroups.md)
- [Variable Groups](mds/updateVariableGroups.md)
  - To update the details of one or more variable groups in your Zoho CRM organization. The request accepts a maximum of 10 variable group items. When individual items succeed or fail independently, the API returns a 207 multi-status response with per-item results.
  - [Examples](mds/examples/updateVariableGroups.md)
- [Get variable group by ID](mds/getVariableGroupById.md)
  - To retrieve the details of a specific variable group by its ID in your Zoho CRM organization.
  - [Examples](mds/examples/getVariableGroupById.md)
- [Update variable group by ID](mds/updateVariableGroupById.md)
  - To update the details of a specific variable group by its ID in your Zoho CRM organization.
  - [Examples](mds/examples/updateVariableGroupById.md)
- [Generate API Name](mds/generateAPIName.md)
  - To generate an available API name for a new variable group in your Zoho CRM organization. Submit the proposed display name in the request, and the API returns a suggested `api_name` that complies with the naming requirements.
  - [Examples](mds/examples/generateAPIName.md)
