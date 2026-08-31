# GET /settings/zia/data_enrichment
**Operation:** `getZiaEnrichmentConfiguration` — Data Enrichment
> Use this API to get the details of configuration for data enrichment. This API gives you the mapping of the enrich fields with their corresponding CRM fields for enriching data. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module IDs and API names for filtering or reference.

**Responses:**

- **200**: Enrichment configurations fetched successfully. [application/json]
    > Data enrichment configurations fetched successfully.
    - `data_enrichment` (array of object) [maxItems=50] **REQ** — Array of data enrichment configurations.
      - `id` (string) **REQ** [maxLen=19] — Unique identifier of the enrichment configuration.
      - `type` (string) **REQ** [maxLen=255] — Type of enrichment — 'personal' or 'organization'.
      - `module` (object `Module`) **REQ** — CRM module metadata with ID and API name.
        schema: `Module`
        - `id` (string) **REQ** [maxLen=19] — Unique identifier of the CRM module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module IDs.
        - `api_name` (string) **REQ** [maxLen=255] — API name of the CRM module (e.g., Leads, Contacts, Accounts). Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module API names.
      - `status` (boolean) **REQ** — Whether the enrichment configuration is active.
      - `input_data_field_mapping` (array of object) [maxItems=50] **REQ** — Array of field mappings for read operations.
        - `enrich_field` (object) **REQ** — Zia enrichment field metadata with display label.
          - `name` (string) **REQ** [maxLen=255] — Name of the Zia enrichment field.
          - `display_label` (string) **REQ** [maxLen=255] — Display label of the Zia enrichment field.
        - `crm_field` (object) **REQ** — CRM field object with additional display name.
          oneOf:
              - `id` (string) **REQ** [maxLen=19] — Unique identifier of the CRM field.
              - `api_name` (string) **REQ** [maxLen=255] — API name of the CRM field.
              - `name` (string) [maxLen=255] — Display name of the CRM field.
              type: null — Null value for CRM field (no mapping).
      - `created_time` (string) **REQ** [maxLen=255] — Timestamp when the configuration was created.
      - `created_by` (object) **REQ** — User who created the enrichment configuration.
        - `id` (string) **REQ** [maxLen=19] — Unique identifier of the user who created the configuration.
        - `name` (string) **REQ** [maxLen=255] — Name of the user who created the configuration.
      - `modified_time` (string) **REQ** [maxLen=255] — Timestamp when the configuration was last modified.
      - `modified_by` (object) **REQ** — User who last modified the enrichment configuration.
        - `id` (string) **REQ** [maxLen=19] — Unique identifier of the user who last modified the configuration.
        - `name` (string) **REQ** [maxLen=255] — Name of the user who last modified the configuration.

- **204**: No Content — No enrichment configurations found.

- **400**: Bad Request. Returned when the feature is not enabled or not supported. [application/json]
    > Error response when the feature is not enabled or not supported.
    - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED', 'FEATURE_NOT_SUPPORTED']] — Error code indicating the feature is not enabled or not supported.
    - `details` (object) **REQ** — Additional details — empty for this error type.
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `status` (string) **REQ** [maxLen=255] — Error status — always 'error'.

- **403**: Permission error. Returned when the user lacks the necessary permissions to view enrichment configurations. [application/json]
    > Error response when the user lacks permission to access this feature.
    - `code` (string) **REQ** [maxLen=255] — Error code — 'NO_PERMISSION'.
    - `details` (object) **REQ** — Details about the missing permissions.
      - `permissions` (array of string) [maxItems=50] **REQ** — List of required permissions.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `status` (string) **REQ** [maxLen=255] — Error status — always 'error'.

**Scopes:** ZohoCRM.zia.enrichment.READ
