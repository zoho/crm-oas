# Zia Enrichment Configuration API

- [OpenAPI specification](zia_enrichment.yaml)
- [Zia Data Enrichment Configuration](operations/createZiaEnrichmentConfigurations/operation.md)
  - Creates Zia Enrichment Configurations for a specific module. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to get CRM field IDs and API names, and the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module IDs and API names.
  - [Examples](operations/createZiaEnrichmentConfigurations/examples/)
- [Data Enrichment](operations/getZiaEnrichmentConfiguration/operation.md)
  - Use this API to get the details of configuration for data enrichment. This API gives you the mapping of the enrich fields with their corresponding CRM fields for enriching data. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module IDs and API names for filtering or reference.
  - [Examples](operations/getZiaEnrichmentConfiguration/examples/)
- [Update Zia Enrichment Configurations for a specific module](operations/updateZiaEnrichmentConfigurations/operation.md)
  - Updates Zia Enrichment Configurations for a specific module by ID. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to get CRM field IDs and API names, and the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module IDs and API names.
  - [Examples](operations/updateZiaEnrichmentConfigurations/examples/)
- [Delete Zia Enrichment Configuration for a specific module](operations/deleteZiaEnrichmentConfiguration/operation.md)
  - Deletes a Zia Enrichment Configuration for a specific module by ID. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID.
  - [Examples](operations/deleteZiaEnrichmentConfiguration/examples/)
- [Get Zia Enrichment Configuration for a specific module](operations/getSpecificZiaEnrichmentConfiguration/operation.md)
  - Retrieves a specific Zia Enrichment Configuration by ID. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to get CRM field IDs and API names, and the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module IDs and API names for reference.
  - [Examples](operations/getSpecificZiaEnrichmentConfiguration/examples/)
