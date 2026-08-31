# Map Dependency API

- [OpenAPI specification](map_dependency.yaml)
- [Get field dependencies for a layout](operations/getMapDependency/operation.md)
  - To retrieve the list of field dependencies configured for a specific layout in your Zoho CRM organization.
  - [Examples](operations/getMapDependency/examples/)
- [Create a field dependency for a layout](operations/createMapDependency/operation.md)
  - To create a field dependency between a parent picklist field and a child picklist field for a specific layout in your Zoho CRM organization. **Prerequisites** - The selected layout must contain at least two option-based fields. - Supported field types are Picklist, Radio Button, and Multi-select Picklist. - Multi-select Picklist fields can be used only as child fields. - Parent and child fields must belong to the selected layout. - When using subform fields, the parent and child fields must belong to the same subform. To create a field dependency between a parent picklist field and a child picklist field for a specific layout in your Zoho CRM organization.
  - [Examples](operations/createMapDependency/examples/)
- [Get a field dependency by ID](operations/getMapDependencyById/operation.md)
  - To retrieve the complete details of a specific field dependency from a layout in your Zoho CRM organization, including all picklist value mappings.
  - [Examples](operations/getMapDependencyById/examples/)
- [Update an existing field dependency](operations/updateMapDependency/operation.md)
  - Updates the picklist value mappings for an existing field dependency. Use \"_delete\": null to remove specific mappings.
  - [Examples](operations/updateMapDependency/examples/)
- [Delete a field dependency](operations/deleteMapDependency/operation.md)
  - To delete a specific field dependency from a layout in your Zoho CRM organization.
  - [Examples](operations/deleteMapDependency/examples/)
