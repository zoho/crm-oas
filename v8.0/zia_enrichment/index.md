# Zia Enrichment Configuration API

- [OpenAPI specification](zia_enrichment.yaml)
- [Zia Data Enrichment Configuration](mds/createZiaEnrichmentConfigurations.md)
  - Creates Zia Enrichment Configurations for a specific module. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to get CRM field IDs and API names, and the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module IDs and API names.
  - [Examples](mds/examples/createZiaEnrichmentConfigurations.md)
- [Data Enrichment](mds/getZiaEnrichmentConfiguration.md)
  - Use this API to get the details of configuration for data enrichment. This API gives you the mapping of the enrich fields with their corresponding CRM fields for enriching data. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module IDs and API names for filtering or reference.
  - [Examples](mds/examples/getZiaEnrichmentConfiguration.md)
- [Update Zia Enrichment Configurations for a specific module](mds/updateZiaEnrichmentConfigurations.md)
  - Updates Zia Enrichment Configurations for a specific module by ID. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to get CRM field IDs and API names, and the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module IDs and API names.
  - [Examples](mds/examples/updateZiaEnrichmentConfigurations.md)
- [Delete Zia Enrichment Configuration for a specific module](mds/deleteZiaEnrichmentConfiguration.md)
  - Deletes a Zia Enrichment Configuration for a specific module by ID. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module ID.
  - [Examples](mds/examples/deleteZiaEnrichmentConfiguration.md)
- [Get Zia Enrichment Configuration for a specific module](mds/getSpecificZiaEnrichmentConfiguration.md)
  - Retrieves a specific Zia Enrichment Configuration by ID. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to get CRM field IDs and API names, and the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module IDs and API names for reference.
  - [Examples](mds/examples/getSpecificZiaEnrichmentConfiguration.md)
