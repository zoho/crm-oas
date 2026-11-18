# POST /settings/blueprints/{blueprintId}/actions/clone
**Operation:** `cloneBlueprint` — Clone Blueprint
> To clone a Blueprint in your Zoho CRM organization.

**Parameters:**
- `blueprintId` (path, string/bigint, required) [pattern=^[0-9]+]: Specify the ID of the Blueprint you want to clone. Refer to the [Blueprints](blueprints.yaml#$.paths./settings/blueprints.get) resource for valid values.
- `X-ZOHO-SERVICE` (header, string, required) [enum=['automation']] {style=simple, explode=False}: Specify the service to which the request is routed.
Possible values:
automation - Routes the request through the automation service.

**Request Body** — application/json `BlueprintCloneBatchRequest`
> The request body must contain a blueprints array with a single object.
  > Represents a batch request that contains the clone settings for a single Blueprint in the blueprints array.
  - `blueprints` (array of object `BlueprintCloneSettings`) [maxItems=1] **REQ** — Represents the list of clone settings for the Blueprint to clone. The object specifies the clone settings for one Blueprint, including the module, name, clone type, and state mappings.
    schema: `BlueprintCloneSettings`
    - `layout` (object `BlueprintLayoutSelector`) **REQ** — Specify the layout data of the cloned blueprint (Required)
      schema: `BlueprintLayoutSelector`
      - `name` (string) [maxLen=100, nullable] — Represents the name of the layout associated with the cloned Blueprint.
      - `id` (string) [maxLen=50, nullable] — Represents the ID of the layout associated with the cloned Blueprint.
    - `pipeline` (object `BlueprintPipelineSelector`) — Specify the pipeline data of the cloned blueprint
      schema: `BlueprintPipelineSelector`
      - `name` (string) [maxLen=100, nullable] — Represents the name of the pipeline associated with the cloned Blueprint.
      - `id` (string) [maxLen=50, pattern=[0-9]+, nullable] — Represents the ID of the pipeline associated with the cloned Blueprint.
    - `map_states` (array of object `StateValueMappingPair`) [maxItems=100, nullable] — Specify the mapping of states from the existing Blueprint to the cloned Blueprint.
      schema: `StateValueMappingPair`
      - `clone_state` (object `TargetStateToken`) — Map states data of new value to cloned blueprint
        schema: `TargetStateToken`
        - `actual_value` (string) [maxLen=100, nullable] — Represents the actual value of the new picklist state in the cloned Blueprint, to which an existing state is remapped through map_states.
      - `existing_state` (object `SourceStateToken`) — Map states data of existing  blueprint
        schema: `SourceStateToken`
        - `actual_value` (string) [maxLen=100, nullable] — Represents the actual value of an existing picklist state in the source Blueprint, which is remapped to a new state in the cloned Blueprint through map_states.
    - `field` (object `BlueprintFieldSelector`) **REQ** — Specify the field data of the cloned blueprint (Required)
      schema: `BlueprintFieldSelector`
      - `api_name` (string) [maxLen=100, nullable] — Represents the API name of the field in the cloned Blueprint.
      - `id` (string) [maxLen=50, nullable] — Represents the ID of the field in the cloned Blueprint.
    - `module` (string) **REQ** [maxLen=100] — Represents the API name of the module to which the cloned Blueprint belongs.
    - `name` (string) **REQ** [maxLen=14] — Represents the name of the cloned Blueprint.
    - `type` (string) **REQ** [maxLen=10] — Represents the type of clone to create for the Blueprint, such as a standalone or dependent clone.

**Responses:**

- **201**: Returns the clone result for the requested Blueprint, including its status, message, and the ID of the newly created Blueprint. — Schema: `BlueprintCloneResponse` [application/json]
    > Represents the response of a Blueprint clone request, containing the clone result for each requested Blueprint.
    schema: `BlueprintCloneResponse`
    - `blueprints` (array of object `BlueprintCloneResultEntry`) [maxItems=1] — Represents the list of clone results. Each object reports the outcome of the clone request for one Blueprint.
      schema: `BlueprintCloneResultEntry`
      - `code` (string) [maxLen=255] — Represents the code that indicates the outcome of the clone request for the Blueprint.
      - `details` (object `BlueprintCloneResultDetails`) — Represents additional details about the clone outcome, including the ID of the cloned Blueprint and the fields that were not copied in the entry criteria, before-transition criteria, or during-transition criteria.
        schema: `BlueprintCloneResultDetails`
        - `uncopied_before_criteria_fields` (null) — Represents the fields in the before-transition criteria that were not copied to the cloned Blueprint.
        - `id` (string) [maxLen=255] — Represents the ID of the cloned Blueprint.
        - `uncopied_entry_criteria_fields` (null) — Represents the fields in the Blueprint entry criteria that were not copied to the cloned Blueprint.
        - `uncopied_during_transition_fields` (null) — Represents the fields in the during-transition criteria that were not copied to the cloned Blueprint.
      - `message` (string) [maxLen=255] — Represents the message that describes the outcome of the clone request for the Blueprint.
      - `status` (string) [maxLen=255] — Indicates whether the clone request for the Blueprint was successful.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request cannot be processed due to invalid syntax.
**Resolution:** The request body and the Blueprint ID must be valid. [application/json]
    > Represents the error response returned when the Blueprint clone request cannot be processed, with the error entries for the requested clone carried in the **blueprints** array.
    oneOf:
        - `blueprints` (array of object) [maxItems=25] **REQ** — Represents the list of error entries for the requested Blueprint clone. Each entry reports one validation or processing error, including its code, message, status, and details.
          oneOf:
            - `ErrorResponseCore24` — Represents the error returned when the maximum number of Blueprints allowed in the Zoho CRM organization has already been reached.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code for the failed operation.
Possible values:
LIMIT_EXCEEDED - The number of Blueprints in the Zoho CRM organization has exceeded the allowed limit.
              - `details` (object) **REQ** — Represents additional details about the error, including the Blueprint limit that was exceeded.
                - `limit` (integer/int32) **REQ** — Represents the maximum number of Blueprints allowed in the Zoho CRM organization, which the request exceeded.
              - `message` (string) **REQ** [enum=['Blueprint limit exceed']] — Represents the error message describing the failure.
Possible values:
Blueprint limit exceed - The number of Blueprints in the Zoho CRM organization has exceeded the allowed limit.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
error - The request failed.
            - `BlueprintNameConflictError` — Represents the error returned when the Blueprint name in the clone request already exists.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code for the Blueprint name conflict.
Possible values:
DUPLICATE_DATA - A Blueprint with the same name already exists.
              - `details` (object) **REQ** — Represents the details of the name conflict error, including validation information.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the Blueprint involved in the name conflict.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation error.
              - `message` (string) **REQ** [enum=['There is already a blueprint with this name']] — Represents the error message that describes the name conflict.
Possible values:
There is already a blueprint with this name - A Blueprint with the specified name already exists in the Zoho CRM organization.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Blueprint clone request.
Possible values:
error - The request failed.
            - `InvalidLayoutReuseError` — Represents the error returned when the layout provided in the request is the same as the layout of the source Blueprint.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code that identifies the type of failure.
Possible values:
INVALID_DATA - The given layout is the same as the source Blueprint layout.
              - `details` (object) **REQ** — Represents the details of the error, including the API name and JSON path of the field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the error.
              - `message` (string) **REQ** [enum=['The given layout should be different from source blueprint layout']] — Represents the error message.
Possible values:
The given layout should be different from source blueprint layout - Returned when the layout given for the clone is the same as the source Blueprint layout.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
error - The request failed.
            - `CloneRequestAmbiguityError` — Represents the error returned when the clone request is ambiguous, such as when the clone type is dependent while map_states is also provided.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code that identifies the cause of the failure.
Possible values:
AMBIGUITY_DURING_PROCESSING - Returned when the clone request cannot be processed because of ambiguous input.
              - `details` (object) **REQ** — Represents the validation details that identify the ambiguous fields in the clone request.
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Represents the list of request fields that caused ambiguity while processing the clone request.
                  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the request field that caused ambiguity in the clone request.
                  - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the request field that caused ambiguity in the clone request.
              - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Represents the error message that describes the failure.
Possible values:
Ambiguity while processing the request - Returned when the clone request contains ambiguous input that prevents processing.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Blueprint clone request.
Possible values:
error - The request failed.
            - `ErrorResponseCore4` — Represents the error returned when a required field is missing from the request.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for the failed operation.
Possible values:
MANDATORY_NOT_FOUND - A required field is missing in the request.
              - `details` (object) **REQ** — Represents additional details about the error, including the API name and JSON path of the missing required field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the required field that is missing in the request.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the required field that is missing in the request.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message that describes the cause of the failure.
Possible values:
Required field is missing - A required field is missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed.
            - `ErrorResponseCore2` — Represents the error returned when the request data is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
Possible values:
INVALID_DATA - The request data has an invalid data type.
              - `details` (object) **REQ** — Represents the details of the error, including the API name of the field, the expected data type, and the JSON path of the invalid value.
                - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the field in the request.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field for which the data type is invalid.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field for which the data type is invalid.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message.
Possible values:
Invalid data type - The data type of a value in the request does not match the expected data type.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
error - The request failed.
            - `ErrorResponseCore6` — Represents the error returned when the request data is invalid.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code that identifies the type of failure.
Possible values:
INVALID_DATA - The request data is invalid, such as when a value exceeds the maximum allowed length.
              - `details` (object) **REQ** — Represents the validation details of the error, including the API name of the invalid field, its JSON path, and the maximum allowed length.
                - `maximum_length` (integer/int32) **REQ** — Represents the maximum length allowed for the field that failed validation.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that failed validation.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that failed validation.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message that describes the cause of the failure.
Possible values:
Invalid data - The request data is invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the failed request.
Possible values:
error - The request failed.
            - `RequiredFieldNotFoundError` — Represents the error returned when a required field is missing from the request. The response identifies the missing field through its api_name and json_path.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the code that identifies the error.
Possible values:
MANDATORY_NOT_FOUND - A required field is missing from the request.
              - `details` (object) **REQ** — Represents the details of the validation error, including the API name and JSON path of the required field that is missing from the request.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the required field that is missing from the request.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the required field that is missing from the request.
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message returned when a required field is missing from the request.
Possible values:
required field not found - A required field is missing from the request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
error - The request failed.
            - `CannotProcessMapStatesError` — Represents the error returned when map_states is required but not provided because the clone layout uses a different field from the source Blueprint field.
              - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Represents the error code returned when the state mappings for the Blueprint clone cannot be processed.
Possible values:
CANNOT_PROCESS - The state mappings cannot be processed.
              - `details` (object) **REQ** — Represents the details of the error, including validation information for the state mappings.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field for which the state-mappings validation failed.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field for which the state-mappings validation failed.
              - `message` (string) **REQ** [enum=[1 values]] — Represents the error message that describes why the state mappings could not be processed for the Blueprint clone.
Possible values:
The mapping states is mandatory for clone blueprint as given layout field different from source blueprint field - Returned when the state mappings are mandatory for the clone because the given layout field differs from the source Blueprint field.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Blueprint clone request.
Possible values:
error - The request failed.
            - `BlueprintNameSpecialCharError` — Represents the error returned when the Blueprint name contains special characters that are not allowed.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the validation failure.
Possible values:
INVALID_DATA - The request data failed validation.
              - `details` (object) **REQ** — Represents the validation details of the error, including the API name and JSON path of the invalid field.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that failed validation.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that caused the validation error.
              - `message` (string) **REQ** [enum=['Blueprint name should not allow special characters']] — Represents the error message that describes the validation failure.
Possible values:
Blueprint name should not allow special characters - The Blueprint name in the request contains special characters, which are not allowed.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Blueprint clone request.
Possible values:
error - The request failed.
            - `InvalidValueError` — Represents the error returned when a value provided for a field is not among the accepted values, such as an unrecognized clone type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
Possible values:
INVALID_DATA - Indicates that a field value in the request is not among the accepted values.
              - `details` (object) **REQ** — Represents the details of the error, including the API name and JSON path of the field with the invalid value and the list of accepted values.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that contains the invalid value.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that contains the invalid value.
                - `supported_values` (array of string) [maxItems=25] — Represents the values accepted for the field.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['the value given is invalid']] — Represents the message that describes the validation error.
Possible values:
the value given is invalid - The value supplied for the field is not among its accepted values.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the request.
Possible values:
error - The request failed.
            - `PipelineNotProvidedError` — Represents the error returned when the request does not include the pipeline.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the code that identifies the error.
Possible values:
INVALID_DATA - The request contains invalid data.
              - `details` (object) **REQ** — Represents additional details about the error, including the API name and JSON path of the field that was not provided.
                - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that was not provided in the request.
                - `json_path` (string) **REQ** [maxLen=1000] — Represents the JSON path of the field that was not provided in the request.
              - `message` (string) **REQ** [enum=['Pipeline is not provided']] — Represents the message that describes the validation error.
Possible values:
Pipeline is not provided - The request does not include the pipeline.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the request.
Possible values:
error - The request failed.
            - `CannotCloneBlueprintError` — Represents the error returned when the Blueprint cannot be cloned, with error code CANNOT_PROCESS.
              - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Represents the error code returned when the Blueprint cannot be cloned.
Possible values:
CANNOT_PROCESS - The Blueprint cannot be cloned.
              - `details` (object) **REQ** — Represents the details of the error, including the ID of the Blueprint that cannot be cloned.
                - `id` (string) **REQ** [maxLen=18] — Represents the ID of the Blueprint that cannot be cloned.
              - `message` (string) **REQ** [enum=['Cannot allow to clone this blueprint']] — Represents the error message returned when the Blueprint cannot be cloned.
Possible values:
Cannot allow to clone this blueprint - The Blueprint cannot be cloned.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the Blueprint clone request.
Possible values:
error - The request failed.
      - `ErrorResponseCore19` — Represents the error returned when the Blueprint ID in the request is invalid.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code that identifies the reason for the failure.
Possible values:
INVALID_DATA - The data in the request is invalid.
        - `details` (object) **REQ** — Represents the validation details of the error, including the index of the invalid entry in the resource path.
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the invalid entry in the resource path.
        - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message.
Possible values:
the id given seems to be invalid - The Blueprint ID in the request path is invalid.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
error - The request failed.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.blueprint.CREATE
