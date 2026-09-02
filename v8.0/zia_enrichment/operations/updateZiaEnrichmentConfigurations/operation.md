# PUT /settings/zia/data_enrichment/{id}
**Operation:** `updateZiaEnrichmentConfigurations` — Update Zia Enrichment Configurations for a specific module
> Updates Zia Enrichment Configurations for a specific module by ID. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to get CRM field IDs and API names, and the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to get module IDs and API names.

**Parameters:**
- `id` (path, string, required) [maxLen=19]: Data Enrichment configuration ID

**Schemas:**
`FieldMappingForWrite`:
  type: array of object [maxItems=50]
    - `enrich_field` (object) **REQ** — Zia enrichment field metadata.
      - `name` (string) **REQ** [maxLen=255] — Name of the Zia enrichment field.
    - `crm_field` (object) **REQ** — CRM field object. Provide both ID and API name. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to get CRM field IDs and API names.
      oneOf:
          - `id` (string) **REQ** [maxLen=19] — Unique identifier of the CRM field.
          - `api_name` (string) **REQ** [maxLen=255] — API name of the CRM field.
          type: null — Null value for CRM field (no mapping).

**Request Body** (required) — application/json
  > Request body schema for updating Zia Enrichment configurations.
  - `data_enrichment` (array of object) [maxItems=50] **REQ** — Array of updated data enrichment configurations.
    - `status` (boolean) — Whether the enrichment configuration should be active.
    - `output_data_field_mapping` (array of object) [maxItems=50] **REQ** — Array of field mappings for write operations.
      - `enrich_field` (object) **REQ** — Zia enrichment field metadata.
        - `name` (string) **REQ** [maxLen=255] — Name of the Zia enrichment field.
      - `crm_field` (object) **REQ** — CRM field object. Provide both ID and API name. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to get CRM field IDs and API names.
        oneOf:
            - `id` (string) **REQ** [maxLen=19] — Unique identifier of the CRM field.
            - `api_name` (string) **REQ** [maxLen=255] — API name of the CRM field.
            type: null — Null value for CRM field (no mapping).
    - `input_data_field_mapping` (array of object) [maxItems=50] **REQ** — Array of field mappings for write operations.
      - `enrich_field` (object) **REQ** — Zia enrichment field metadata.
        - `name` (string) **REQ** [maxLen=255] — Name of the Zia enrichment field.
      - `crm_field` (object) **REQ** — CRM field object. Provide both ID and API name. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to get CRM field IDs and API names.
        oneOf:
            - `id` (string) **REQ** [maxLen=19] — Unique identifier of the CRM field.
            - `api_name` (string) **REQ** [maxLen=255] — API name of the CRM field.
            type: null — Null value for CRM field (no mapping).

**Responses:**

- **200**: Enrichment configuration updated successfully. [application/json]
    > Enrichment updated successfully.
    - `data_enrichment` (array of object) [maxItems=50] **REQ** — Array of update results for each configuration.
      - `code` (string) **REQ** [maxLen=255] — Result code — 'SUCCESS' for successful update.
      - `message` (string) **REQ** [maxLen=255] — Human-readable message describing the operation result.
      - `details` (object) **REQ** — Details of the updated enrichment configuration.
        - `id` (string) **REQ** [maxLen=19] — Unique identifier of the updated enrichment configuration.
        - `modified_time` (string) **REQ** [maxLen=255] — Timestamp when the configuration was last modified.
        - `modified_by` (object) **REQ** — User who last modified the enrichment configuration.
          - `id` (string) **REQ** [maxLen=255] — Unique identifier of the user who modified the configuration.
          - `name` (string) **REQ** [maxLen=255] — Name of the user who modified the configuration.
      - `status` (string) **REQ** [maxLen=255] — Overall status of the operation — 'success' or 'error'.

- **400**: Validation error. Returned when the request contains invalid data, missing mandatory fields, or unsupported values. [application/json]
    > 400 responses
    oneOf:
        - `data_enrichment` (array of object) [maxItems=50] **REQ** — Array of error items.
          - `code` (string) **REQ** [enum=[5 values]] — Error code identifying the type of validation failure.
          - `details` (object) **REQ** — Details about the validation failure.
            - `expected_data_type` (string) [maxLen=255] — Expected data type for the field.
            - `api_name` (string) **REQ** [maxLen=255] — API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=255] — JSON path to the invalid field in the request body.
          - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
          - `status` (string) **REQ** [maxLen=255] — Error status — always 'error'.
        - `data_enrichment` (array of object) [maxItems=50] **REQ** — Array of error items.
          - `code` (string) **REQ** [maxLen=255] — Error code — 'INVALID_DATA'.
          - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
          - `details` (object) **REQ** — Details about the unsupported value.
            - `api_name` (string) **REQ** [maxLen=255] — API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=255] — JSON path to the invalid field in the request body.
            - `supported_values` (array of string) [maxItems=50] **REQ** — List of supported values for the field.
              items: [enum=['organization', 'personal']]
          - `status` (string) **REQ** [maxLen=255] — Error status — always 'error'.
        - `data_enrichment` (array of object) [maxItems=50] **REQ** — Array of error items.
          - `code` (string) **REQ** [maxLen=255] — Error code — 'EXPECTED_FIELD_MISSING'.
          - `details` (object) **REQ** — Details about the missing expected fields.
            - `expected_fields` (array of object) [maxItems=50] **REQ** — List of expected fields that are missing.
              - `api_name` (string) **REQ** [maxLen=255] — API name of the expected field.
              - `json_path` (string) **REQ** [maxLen=255] — JSON path to the expected field.
          - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
          - `status` (string) **REQ** [maxLen=255] — Error status — always 'error'.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_ENABLED', 'FEATURE_NOT_SUPPORTED']] — Error code indicating the feature is not enabled or not supported.
        - `details` (object) **REQ** — Additional details — empty for this error type.
        - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
        - `status` (string) **REQ** [maxLen=255] — Error status — always 'error'.

- **403**: Permission error. Returned when the user lacks the necessary permissions to update enrichment configurations. [application/json]
    > Error response when the user lacks permission to access this feature.
    - `code` (string) **REQ** [maxLen=255] — Error code — 'NO_PERMISSION'.
    - `details` (object) **REQ** — Details about the missing permissions.
      - `permissions` (array of string) [maxItems=50] **REQ** — List of required permissions.
        items: [maxLen=255]
    - `message` (string) **REQ** [maxLen=255] — Human-readable error message.
    - `status` (string) **REQ** [maxLen=255] — Error status — always 'error'.

**Scopes:** ZohoCRM.zia.enrichment.UPDATE
