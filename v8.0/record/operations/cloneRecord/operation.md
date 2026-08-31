# POST /{module}/{recordId}/actions/clone
**Operation:** `cloneRecord` — Record Clone
> Clones a record in the specified module.  Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module ID and API name. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to retrieve the field IDs and API names.
By default, the field values of the parent record are copied to the cloned record. To modify or add field values, specify the field API names and their corresponding values in the input body. If no field values need to be modified, the input body can be omitted.
Mandatory fields specified in the input must not be null. The Sample Inputs, Sample Responses, and Possible Errors documented for the [Insert Records API](record.yaml#$.paths./module.post) also apply to the [Record Clone API](record.yaml#$.paths./{module}/{recordId}/actions/clone.post).

**Tags:** Records

**Parameters:**
- `module` (path, string, required) [maxLen=25]: Specify the API name of the module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module ID and API name.
- `recordId` (path, string/int64, required): Specify the unique ID of the record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.

**Schemas:**
`RecordDeleteByIdInvalidDataError`:
  > Represents the error response returned when the operation fails due to a record delete by ID invalid data error.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
  - `details` (object `RecordDeleteByIdResourcePathDetails`) **REQ** — Contains the contextual details for the record delete by ID resource path error.
`RecordDeleteByIdResourcePathDetails`:
  > Contains the contextual details for the record delete by ID resource path error.
  - `resource_path_index` (integer/int32) **REQ** — Represents the zero-based index indicating which resource in the path caused the error.

**Request Body** (required) — application/json `RecordsInputSchema`
> The request body must contain a **data** array with one object containing the field values to override in the cloned record.
  > By default, when you clone a record, the field values of the parent record will also be copied to the cloned record. If you want to modify certain fields or to add value to some fields, specify their field API names and their corresponding values in the input body.
  - `data` (array of object `RecordWriteDataItem`) [minItems=1, maxItems=100] **REQ** — Represents the data value.
    schema: `RecordWriteDataItem`
    - `Layout` (object) — Represents the layout value. Use the [Get Layouts Metadata API](layouts.yaml#$.paths./settings/layouts.get) to retrieve the Layout ID.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents the layout value.
    - `Wizard` (object) — Represents the wizard value. Use the [Get Wizards API](wizards.yaml#$.paths./settings/wizards.get) to retrieve the Wizard ID.
      - `id` (string/int64) **REQ** [maxLen=19] — Represents the wizard value.
    additionalProperties: any
  - `apply_feature_execution` (array of object) — Use the "apply_feature_execution" array to trigger supported CRM features when creating or updating a record through the API. Specify "layout_rules" to apply layout rules or "criteria_validation_rule" to trigger validation rules. For "layout_rules", ensure the request includes all fields required by the layout rule criteria; otherwise, the API returns an error. For "criteria_validation_rule", all applicable validation rules are evaluated, and the API returns "MULTIPLE_OR_MULTI_ERRORS" if multiple rules fail.
    - `name` (string) **REQ** [enum=[7 values]] — Represents the apply feature execution value.
  - `skip_feature_execution` (array of object) — Use the "skip_feature_execution" array to skip Cadences execution when creating a record through the API. Specify "cadences" as the value of the "name" key and include this key alongside "data" in the request.
    - `name` (string) **REQ** [enum=['assignment_rules', 'cadences', 'connected_workflows']] — Represents the skip feature execution value.
  - `trigger` (array of string) — Specifies the CRM features to execute for the API request. Supported values are "workflow", "approval", and "blueprint". If the "trigger" parameter is not specified, workflows, approvals, and blueprints related to the API are executed. Specify an empty array [] to prevent these features from executing.
    items: [enum=['approval', 'workflow', 'blueprint', 'pathfinder', 'orchestration']]

**Responses:**

- **201**: Returns the details of each successfully cloned record, including the record ID and audit metadata. — Schema: `RecordSuccessResponse` [application/json]
    > Represents the response schema for the recordsuccess operation.
    schema: `RecordSuccessResponse`
    - `data` (array of object `RecordPostSuccessDataItem`) [minItems=1, maxItems=100] **REQ** — Represents the data value.
      schema: `RecordPostSuccessDataItem`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the error code identifying the type of failure.
      - `message` (string) **REQ** — Represents the error message describing why the operation failed.
      - `status` (string) **REQ** [enum=['success']] — Indicates the overall result status of the request.
      - `details` (object) **REQ** — Contains additional context about the error.
        - `id` (string/int64) **REQ** — Contains additional context about the error.
        - `Modified_Time` (string/date-time) **REQ** — Contains additional context about the error.
        - `Created_Time` (string/date-time) **REQ** — Contains additional context about the error.
        - `Created_By` (object) **REQ** — Contains additional context about the error.
          - `name` (string) **REQ** [maxLen=101] — Contains additional context about the error.
          - `id` (string/int64) **REQ** — Contains additional context about the error.
        - `Modified_By` (object) **REQ** — Contains additional context about the error.
          - `name` (string) **REQ** [maxLen=101] — Contains additional context about the error.
          - `id` (string/int64) **REQ** — Contains additional context about the error.
        - `$approval_state` (string) [maxLen=255] — Contains additional context about the error.
        - `$state` (string) [maxLen=255] — Contains additional context about the error.
        - `$wizard_connection_path` (string) [maxLen=2000, nullable] — $wizard_connection_path information denoted by comma separated connection ids between wizard screens.
        - `$process_flow` (boolean) — Contains additional context about the error.
        - `$locked_for_me` (boolean) — Contains additional context about the error.
        - `$approved` (boolean) — Contains additional context about the error.
        - `$status` (string) [maxLen=255] — Contains additional context about the error.
        - `$layout_id` (object) — Contains additional context about the error.
          - `id` (string/int64) **REQ** — Contains additional context about the error.
          - `name` (string) [maxLen=255] — Contains additional context about the error.
          - `display_label` (string) [maxLen=255] — Contains additional context about the error.
        - `$has_more` (object) — Contains additional context about the error.

- **400**: The request could not be processed because one or more records contain invalid data or missing required fields.
**Resolution:** Each error in the data array identifies the specific record and field that caused the failure. The request must be corrected and resubmitted. [application/json]
    oneOf:
      - `DependentFieldMissingError` — Represents the error response returned when the operation fails due to a dependent field missing error.
        - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `dependee` (object) **REQ** — Contains additional context about the error.
            - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
            - `json_path` (string) **REQ** — Contains additional context about the error.
          - `api_name` (string) **REQ** [maxLen=255] — Contains additional context about the error.
          - `json_path` (string) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `RecordDeleteByIdInvalidDataError` — Represents the error response returned when the operation fails due to a record delete by ID invalid data error.
      - `RecordsIdPostErrorResponse` — Standard error response schema returned when a single-record operation fails.
        - `data` (array of object) [minItems=1, maxItems=100] **REQ** — List of error objects describing failures encountered while processing record operation requests.
          oneOf:
            - `InvalidDataTypeError` — Represents the error response returned when the operation fails due to a invalid data type error.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object `InvalidDataTypeMismatchDetails`) **REQ** — Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
                schema: `InvalidDataTypeMismatchDetails`
                - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the field.
                - `api_name` (string) **REQ** — Represents the API name of the field or module.
                - `json_path` (string) **REQ** — Represents the JSONPath location pointing to the field that caused the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `InvalidSupportedValuesError` — Represents the error response returned when the operation fails due to a invalid supported values error.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object `InvalidDataSupportedValuesDetails`) **REQ** — Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
                schema: `InvalidDataSupportedValuesDetails`
                - `api_name` (string) **REQ** — Represents the API name of the field or module.
                - `json_path` (string) **REQ** — Represents the JSONPath location pointing to the field that caused the error.
                - `supported_values` (array of string) **REQ** — Contains the list of valid values accepted for this field.
                  items: [maxLen=255]
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `InvalidMaxLengthError` — Represents the error response returned when the operation fails due to a invalid max length error.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object `InvalidDataMaxLengthDetails`) **REQ** — Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
                schema: `InvalidDataMaxLengthDetails`
                - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed value or length for the field that failed validation.
                - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the field or module.
                - `json_path` (string) **REQ** — Represents the JSONPath location pointing to the field that caused the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `InvalidDataValueError` — Represents the error response returned when the operation fails due to a invalid data value error.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object `InvalidDataFieldValueDetails`) **REQ** — Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
                schema: `InvalidDataFieldValueDetails`
                - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the field or module.
                - `json_path` (string) **REQ** — Represents the JSONPath location pointing to the field that caused the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `RecordDeleteByIdInvalidDataError` — Represents the error response returned when the operation fails due to a record delete by ID invalid data error.
            - `InvalidModuleError` — Represents the error response returned when the operation fails due to a invalid module error.
              - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `MultipleOrMultiErrorsError` — Represents the error response returned when the operation fails due to a multiple or multi errors error.
              - `code` (string) **REQ** [enum=['MULTIPLE_OR_MULTI_ERRORS']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `errors` (array of object) [minItems=1, maxItems=100] **REQ** — Contains additional context about the error.
                  - `code` (string) **REQ** — Contains additional context about the error.
                  - `message` (string) **REQ** — Contains additional context about the error.
                  - `status` (string) **REQ** [enum=['error']] — Contains additional context about the error.
                  - `details` (object) — Contains additional context about the error.
                    - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
                    - `json_path` (string) — Contains additional context about the error.
                    - `duplicate_record` (object) — Contains additional context about the error.
                      - `id` (string/int64) **REQ** — Contains additional context about the error.
                      - `Owner` (object) — Contains additional context about the error.
                        - `name` (string) **REQ** [maxLen=101] — Contains additional context about the error.
                        - `id` (string/int64) **REQ** — Contains additional context about the error.
                        - `zuid` (string) [maxLen=100] — Contains additional context about the error.
                      - `module` (object) — Contains additional context about the error.
                        - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
                        - `id` (string/int64) **REQ** — Contains additional context about the error.
                    - `more_records` (boolean) — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `MandatoryNotFoundError` — Represents the error response returned when the operation fails due to a mandatory not found error.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
                - `json_path` (string) **REQ** — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `MandatoryNotFoundLayoutRuleWriteError` — Represents the error response returned when the operation fails due to a mandatory not found layout rule write error.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `layout_rule` (object) **REQ** — Contains additional context about the error.
                  - `name` (string) **REQ** [maxLen=255] — Contains additional context about the error.
                  - `id` (string/int64) **REQ** — Contains additional context about the error.
                - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
                - `json_path` (string) **REQ** — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `InvalidRequestMethodError` — Represents the error response returned when the operation fails due to a invalid request method error.
              - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `AuthorizationFailedError` — Represents the error response returned when the operation fails due to a authorization failed error.
              - `code` (string) **REQ** [enum=['AUTHORIZATION_FAILED']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `DuplicateDataError` — Represents the error response returned when the operation fails due to a duplicate data error.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
                - `json_path` (string) **REQ** — Contains additional context about the error.
                - `id` (string/int64) [maxLen=255] — Contains additional context about the error.
                - `duplicate_record` (object) **REQ** — Information about the existing record that has the duplicate value, containing field values from the duplicate record.
                  - `id` (string/int64) **REQ** — Contains additional context about the error.
                  - `Owner` (object) — Contains additional context about the error.
                    - `name` (string) **REQ** [maxLen=101] — Contains additional context about the error.
                    - `id` (string/int64) **REQ** — Contains additional context about the error.
                    - `zuid` (string) [maxLen=255] — Contains additional context about the error.
                  - `module` (object) — Contains additional context about the error.
                    - `api_name` (string) **REQ** [maxLen=255] — Contains additional context about the error.
                    - `id` (string/int64) **REQ** — Contains additional context about the error.
                  additionalProperties: any
                - `more_records` (boolean) **REQ** — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `DependentServiceError` — Represents the error response returned when the operation fails due to a dependent service error.
              - `code` (string) **REQ** [enum=['DEPENDENT_SERVICE_ERROR']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `dependency_error` (string) **REQ** [enum=['NO_PERMISSION', 'LIMIT_EXCEEDED', 'PROCESSING_ERROR', 'CANNOT_PROCESS']] — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `InvalidModuleGETError` — Represents the error response returned when the operation fails due to a invalid module GET error.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.

- **401**: Authentication failed because the OAuth token is missing, expired, or does not include the required scope.
**Resolution:** A new access token must be generated with the required scope for this operation. [application/json]
    > Represents the response schema for the cloneRecord operation.
    oneOf:
      - `RecordUnauthorizedResponse` — Represents the response schema for the record unauthorized operation.
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
        - `details` (object) **REQ** — Contains additional context about the error.
      - `RecordAuthenticationFailureResponse` — Represents the response schema for the record authentication failure operation.
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
        - `details` (object) **REQ** — Contains additional context about the error.

- **403**: Permission denied to clone record in the specified module.
**Resolution:** The CRM administrator must grant the required clone permission to the user's profile. — Schema: `RecordPermissionResponse` [application/json]
    > Represents the response schema for the record permission operation.
    schema: `RecordPermissionResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.
      - `permissions` (array of string) [minItems=1, maxItems=100] **REQ** — Contains additional context about the error.
        items: [maxLen=255]

- **404**: The request URL does not match any valid API endpoint pattern.
**Resolution:** The API endpoint URL must be verified for correct format and path parameters. — Schema: `RecordInvalidURLResponse` [application/json]
    > Represents the response schema for the record invalid URL operation.
    schema: `RecordInvalidURLResponse`
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **500**: An unexpected server error occurred while processing the request.
**Resolution:** The request can be retried after some time. If the error persists, Zoho CRM support must be contacted. — Schema: `RecordInternalErrorResponse` [application/json]
    > Represents the error response returned when the operation fails due to a record internal response error.
    schema: `RecordInternalErrorResponse`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

**Scopes:** ZohoCRM.modules.CREATE
