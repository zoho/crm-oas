# Layouts API

- [OpenAPI specification](layouts.yaml)
- [Get layouts metadata](mds/getLayouts.md)
  - To retrieve the layout configurations for a specified module in your Zoho CRM organization. **Note:** - The **profiles** array is **null** if the user does not have the Module Customization permission in their profile. - For the Deals module, when the pipeline feature is enabled, multiple layouts exist per pipeline, each with its own set of layouts. - Score and Visit Summary sections are system-generated and read-only. - The API returns all layouts for the module in a single response; pagination is not supported.
  - [Examples](mds/examples/getLayouts.md)
- [Get layout by ID](mds/getLayoutById.md)
  - To retrieve the details of a specific layout by its layout ID for a specified module in your Zoho CRM account. **Important Notes:** - The `profiles` array is `null` when the user does not have "Module Customization" permission in their profile. - For Deals module: When the pipeline feature is enabled, multiple layouts exist per pipeline. Each pipeline can have its own set of layouts. - The `mode` parameter filters the layout by mode. Possible values: **all**, **business_card**, **quick_create**. - Score and Visit Summary sections are system-generated and read-only. **Prerequisite:** The layout ID can be obtained from the Get All Layouts API.
  - [Examples](mds/examples/getLayoutById.md)
- [Update a custom layout](mds/updateLayout.md)
  - To update a custom layout in your Zoho CRM organization, including renaming it, modifying profile permissions, enabling or disabling the business card display, and creating, updating, or deleting sections and fields within sections.
  - [Examples](mds/examples/updateLayout.md)
- [Delete a custom layout](mds/deleteLayout.md)
  - To delete a custom layout from a module in your Zoho CRM organization. When the layout being deleted has associated records, a target layout must be specified to receive the transferred records and profile associations. If the layout has an associated pipeline, the target pipeline and stage must also be provided. Specifying a transfer target is optional only when the layout is deactivated and has no associated records. Only one custom layout can be deleted per API call, and the standard layout cannot be deleted.
  - [Examples](mds/examples/deleteLayout.md)
