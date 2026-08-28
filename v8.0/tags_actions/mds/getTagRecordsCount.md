# GET /settings/tags/{id}/actions/records_count
**Operation:** `getTagRecordsCount` — Get Tag Records Count
> Retrieves the number of records associated with a specific tag, including workflow, blueprint, and orchestration usage details.

**Parameters:**
- `id` (query, string, optional) [maxLen=19]: Tag ID to retrieve the records count for. Use the [Get Tags API](tags.yaml#$.paths./settings/tags.get) to retrieve tag IDs.

- `module` (query, string, required) [maxLen=100]: The API name of the module to retrieve the tag records count for. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module API names.

- `id` (path, string, required) [maxLen=19]: Unique identifier of the record or tag. Use the [Get Tags API](tags.yaml#$.paths./settings/tags.get) to retrieve tag IDs.


**Schemas:**
`ErrorResponseTagIdNotFound`:
  > Error indicating that the specified tag ID was not found.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
  - `details` (object) **REQ** — Error details with validation information
    - `api_name` (string) [maxLen=100] — The field name that caused the error
  - `message` (string) **REQ** [enum=['tags not found']] — Error message
  - `status` (string) **REQ** [enum=['error']] — Error status
`GETRulesNested`:
  > Nested schema for rules with detailed properties.
  - `subtype_name` (string) **REQ** [maxLen=255] — Name of the rule subtype
  - `subtype` (string) **REQ** [maxLen=255] — Rule subtype identifier
  - `module` (string) **REQ** [maxLen=255] — Module associated with the rule
  - `name` (string) **REQ** [maxLen=255] — Name of the rule
  - `execution_type` (string) **REQ** [maxLen=255] — Execution type of the rule
  - `id` (string) **REQ** [maxLen=255] — Unique identifier of the rule
  - `source` (integer/int32) **REQ** — Source identifier for the rule
  - `subtype_id` (string) **REQ** [maxLen=255] — Unique identifier of the rule subtype
  - `status` (string) **REQ** [maxLen=255] — Status of the rule (e.g., Active)
`GETRulesNested1`:
  > Nested schema for rules within workflow, blueprint, or orchestration configurations.
  - `subtype_name` (string) **REQ** [maxLen=255] — Name of the rule subtype
  - `subtype` (string) **REQ** [maxLen=255] — Rule subtype identifier
  - `module` (string) **REQ** [maxLen=255] — Module associated with the rule
  - `name` (string) **REQ** [maxLen=255] — Name of the rule
  - `execution_type` (string) **REQ** [maxLen=255] — Execution type of the rule (e.g., instant, schedule)
  - `id` (string) **REQ** [maxLen=255] — Unique identifier of the rule
  - `source` (integer/int32) **REQ** — Source identifier for the rule
  - `subtype_id` (string) **REQ** [maxLen=255] — Unique identifier of the rule subtype
`GETRulesNested2`:
  > Nested schema for rules with simplified structure.
  - `subtype` (string) **REQ** [maxLen=255] — Rule subtype identifier
  - `module` (string) **REQ** [maxLen=255] — Module associated with the rule
  - `name` (string) **REQ** [maxLen=255] — Name of the rule
  - `execution_type` (string) **REQ** [maxLen=255] — Execution type of the rule
  - `id` (string) **REQ** [maxLen=255] — Unique identifier of the rule
  - `source` (integer/int32) **REQ** — Source identifier for the rule
  - `subtype_id` (string) **REQ** [maxLen=255] — Unique identifier of the rule subtype

**Responses:**

- **200**: OK - Successfully retrieved the tag records count with configured areas. — Schema: `GetrecordscountResponse200` [application/json]
    > Success response for tag records count API.
    schema: `GetrecordscountResponse200`
    - `configured_areas` (object `GETConfiguredAreasNested`) — Nested schema for configured_areas in records count response.
      schema: `GETConfiguredAreasNested`
      - `workflow_tagActionRecords` (object `GETWorkflowTagactionrecordsNested`) **REQ** — Nested schema for workflow tag action records.
        schema: `GETWorkflowTagactionrecordsNested`
        - `Orchestration` (object `GETOrchestrationNested`) **REQ** — Nested schema for Orchestration configurations.
          schema: `GETOrchestrationNested`
          - `3060320000000666022` (object `GET3060320000000666022Nested`) **REQ** — Nested schema for tag ID 3060320000000666022 configurations.
            schema: `GET3060320000000666022Nested`
            - `RemoveTags` (array of object `GETRemovetagsNested`) [maxItems=1] **REQ** — RemoveTags configurations
              schema: `GETRemovetagsNested`
              - `name` (string) **REQ** [maxLen=255] — Name of the RemoveTags configuration
              - `rules` (array of object `GETRulesNested`) [maxItems=1] **REQ** — Rules associated with the RemoveTags configuration
              - `id` (string) **REQ** [maxLen=255] — Unique identifier of the RemoveTags configuration
            - `AddTags` (array of object `GETAddtagsNested`) [maxItems=1] **REQ** — AddTags configurations
              schema: `GETAddtagsNested`
              - `name` (string) **REQ** [maxLen=255] — Name of the AddTags configuration
              - `rules` (array of object `GETRulesNested`) [maxItems=1] **REQ** — Rules associated with the AddTags configuration
              - `id` (string) **REQ** [maxLen=255] — Unique identifier of the AddTags configuration
        - `Blueprint` (object `GETBlueprintNested`) **REQ** — Nested schema for Blueprint configurations.
          schema: `GETBlueprintNested`
          - `3060320000000666022` (object `GET3060320000000666022Nested1`) **REQ** — Nested schema for tag ID 3060320000000666022 configurations.
            schema: `GET3060320000000666022Nested1`
            - `RemoveTags` (array of object `GETRemovetagsNested1`) [maxItems=1] **REQ** — RemoveTags configurations
              schema: `GETRemovetagsNested1`
              - `name` (string) **REQ** [maxLen=255] — Name of the RemoveTags configuration
              - `rules` (array of object `GETRulesNested1`) [maxItems=1] **REQ** — Rules associated with the RemoveTags configuration
              - `id` (string) **REQ** [maxLen=255] — Unique identifier of the RemoveTags configuration
            - `AddTags` (array of object `GETAddtagsNested1`) [maxItems=1] **REQ** — AddTags configurations
              schema: `GETAddtagsNested1`
              - `name` (string) **REQ** [maxLen=255] — Name of the AddTags configuration
              - `rules` (array of object `GETRulesNested1`) [maxItems=1] **REQ** — Rules associated with the AddTags configuration
              - `id` (string) **REQ** [maxLen=255] — Unique identifier of the AddTags configuration
        - `Workflow` (object `GETWorkflowNested`) **REQ** — Nested schema for Workflow configurations.
          schema: `GETWorkflowNested`
          - `3060320000000666022` (object `GET3060320000000666022Nested2`) **REQ** — Nested schema for tag ID 3060320000000666022 configurations.
            schema: `GET3060320000000666022Nested2`
            - `RemoveTags` (array of object `GETRemovetagsNested2`) [maxItems=2] **REQ** — RemoveTags configurations
              schema: `GETRemovetagsNested2`
              - `name` (string) **REQ** [maxLen=255] — Name of the RemoveTags configuration
              - `rules` (array of object `GETRulesNested2`) [maxItems=1] **REQ** — Rules associated with the RemoveTags configuration
              - `id` (string) **REQ** [maxLen=255] — Unique identifier of the RemoveTags configuration
            - `AddTags` (array of object `GETAddtagsNested2`) [maxItems=3] **REQ** — AddTags configurations
              schema: `GETAddtagsNested2`
              - `name` (string) **REQ** [maxLen=255] — Name of the AddTags configuration
              - `rules` (array of object `GETRulesNested2`) [maxItems=1] **REQ** — Rules associated with the AddTags configuration
              - `id` (string) **REQ** [maxLen=255] — Unique identifier of the AddTags configuration
      - `custom_view` (object `GETCustomViewNested`) **REQ** — Nested schema for custom_view configurations.
        schema: `GETCustomViewNested`
        - `cvnames` (array of object) [maxItems=0] **REQ** — List of custom view names
        - `inaccessible_custom_view_present` (boolean) **REQ** — Indicates whether inaccessible custom views exist
        - `cvmodules` (array of object) [maxItems=0] **REQ** — List of modules with custom views
        - `cvids` (array of object) [maxItems=0] **REQ** — List of custom view IDs
    - `count` (string) **REQ** [maxLen=255] — Total count of records associated with the tag

- **400**: Bad Request - The request cannot be processed due to invalid syntax or missing required parameters. [application/json]
    > Error response for status 400
    oneOf:
      - `RequiredParamMissingError` — Error indicating that a required parameter is missing.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) **REQ** [maxLen=255] — Name of the missing parameter
        - `message` (string) **REQ** [enum=['One of the expected param is missing']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidModuleNameError` — Error indicating that the specified module name is invalid.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `ModuleTagsNotSupportedError` — Error indicating that the specified module does not support tags.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['the given module is not supported for this api']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidRequestMethodError` — Error indicating that the HTTP request method is invalid.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `ErrorResponseTagIdNotFound` — Error indicating that the specified tag ID was not found.

- **403**: Forbidden - The client does not have access rights to perform the operation. — Schema: `NoPermissionError` [application/json]
    > Error response for status 403
    schema: `NoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] **REQ** — List of required permissions
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status

- **404**: Not Found - The specified tag ID does not exist. — Schema: `ErrorResponseTagIdNotFound` [application/json]
    > Error response when the given tag ID is invalid or not found

**Scopes:** ZohoCRM.settings.tags.all
