# Map Dependency API

- [OpenAPI specification](map_dependency.yaml)
- [Get field dependencies for a layout](mds/getMapDependency.md)
  - To retrieve the list of field dependencies configured for a specific layout in your Zoho CRM organization.
  - [Examples](mds/examples/getMapDependency.md)
- [Create a field dependency for a layout](mds/createMapDependency.md)
  - To create a field dependency between a parent picklist field and a child picklist field for a specific layout in your Zoho CRM organization. **Prerequisites** - The selected layout must contain at least two option-based fields. - Supported field types are Picklist, Radio Button, and Multi-select Picklist. - Multi-select Picklist fields can be used only as child fields. - Parent and child fields must belong to the selected layout. - When using subform fields, the parent and child fields must belong to the same subform. To create a field dependency between a parent picklist field and a child picklist field for a specific layout in your Zoho CRM organization.
  - [Examples](mds/examples/createMapDependency.md)
- [Get a field dependency by ID](mds/getMapDependencyById.md)
  - To retrieve the complete details of a specific field dependency from a layout in your Zoho CRM organization, including all picklist value mappings.
  - [Examples](mds/examples/getMapDependencyById.md)
- [Update an existing field dependency](mds/updateMapDependency.md)
  - Updates the picklist value mappings for an existing field dependency. Use \"_delete\": null to remove specific mappings.
  - [Examples](mds/examples/updateMapDependency.md)
- [Delete a field dependency](mds/deleteMapDependency.md)
  - To delete a specific field dependency from a layout in your Zoho CRM organization.
  - [Examples](mds/examples/deleteMapDependency.md)
