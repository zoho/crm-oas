# POST /{module}
**Operation:** `createRecords` — Create records in a specified module
> Creates one or more records in the specified module in your Zoho CRM organization. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module API name. Use the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to retrieve the available field API names and data types. You can create up to 100 records in a single API call. Specify the required field API names and their corresponding values in the request body.

**Tags:** Records

**Parameters:**
- `module` (path, string, required) [maxLen=25]: Specify the API name of the module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module ID and API name.

**Schemas:**
`AuthorizationFailedError`:
  > Represents the error response returned when the operation fails due to a authorization failed error.
  - `code` (string) **REQ** [enum=['AUTHORIZATION_FAILED']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
    - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`DependentFieldMissingError`:
  > Represents the error response returned when the operation fails due to a dependent field missing error.
  - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
    - `dependee` (object) **REQ** — Contains additional context about the error.
      - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
      - `json_path` (string) **REQ** — Contains additional context about the error.
    - `api_name` (string) **REQ** [maxLen=255] — Contains additional context about the error.
    - `json_path` (string) **REQ** — Contains additional context about the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`DependentMismatchError`:
  > Represents the error response returned when the operation fails due to a dependent mismatch error.
  - `code` (string) **REQ** [enum=['DEPENDENT_MISMATCH']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
    - `resource_path_index` (integer/int32) — Contains additional context about the error.
    - `dependee` (object) **REQ** — Contains additional context about the error.
      - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
      - `json_path` (string) **REQ** — Contains additional context about the error.
    - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
    - `json_path` (string) **REQ** — Contains additional context about the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`DependentServiceError`:
  > Represents the error response returned when the operation fails due to a dependent service error.
  - `code` (string) **REQ** [enum=['DEPENDENT_SERVICE_ERROR']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
    - `dependency_error` (string) **REQ** [enum=['NO_PERMISSION', 'LIMIT_EXCEEDED', 'PROCESSING_ERROR', 'CANNOT_PROCESS']] — Contains additional context about the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`DuplicateDataError`:
  > Represents the error response returned when the operation fails due to a duplicate data error.
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
`InvalidDataFieldValueDetails`:
  > Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
  - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the field or module.
  - `json_path` (string) **REQ** — Represents the JSONPath location pointing to the field that caused the error.
`InvalidDataMaxLengthDetails`:
  > Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
  - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed value or length for the field that failed validation.
  - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the field or module.
  - `json_path` (string) **REQ** — Represents the JSONPath location pointing to the field that caused the error.
`InvalidDataMaxLengthError`:
  > Represents the error response returned when the operation fails due to invalid data exceeding the maximum length.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
    - `maximum_length` (integer/int32) **REQ** — Represents the maximum length that was exceeded.
    - `api_name` (string) **REQ** [maxLen=50] — Represents the API name for which the data exceeded the maximum length.
    - `expected_data_type` (string) **REQ** [maxLen=50] — Represents the expected data type for the field.
    - `json_path` (string) **REQ** — Represents the JSON path for the field that exceeded the maximum length.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`InvalidDataSupportedValuesDetails`:
  > Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
  - `api_name` (string) **REQ** — Represents the API name of the field or module.
  - `json_path` (string) **REQ** — Represents the JSONPath location pointing to the field that caused the error.
  - `supported_values` (array of string) **REQ** — Contains the list of valid values accepted for this field.
    items: [maxLen=255]
`InvalidDataTypeError`:
  > Represents the error response returned when the operation fails due to a invalid data type error.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object `InvalidDataTypeMismatchDetails`) **REQ** — Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`InvalidDataTypeMismatchDetails`:
  > Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
  - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type expected for the field.
  - `api_name` (string) **REQ** — Represents the API name of the field or module.
  - `json_path` (string) **REQ** — Represents the JSONPath location pointing to the field that caused the error.
`InvalidDataValueError`:
  > Represents the error response returned when the operation fails due to a invalid data value error.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object `InvalidDataFieldValueDetails`) **REQ** — Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`InvalidMaxLengthError`:
  > Represents the error response returned when the operation fails due to a invalid max length error.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object `InvalidDataMaxLengthDetails`) **REQ** — Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`InvalidModuleError`:
  > Represents the error response returned when the operation fails due to a invalid module error.
  - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
    - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`InvalidRequestMethodError`:
  > Represents the error response returned when the operation fails due to a invalid request method error.
  - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
    - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`InvalidSupportedValuesError`:
  > Represents the error response returned when the operation fails due to a invalid supported values error.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object `InvalidDataSupportedValuesDetails`) **REQ** — Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`MandatoryNotFoundError`:
  > Represents the error response returned when the operation fails due to a mandatory not found error.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
    - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
    - `json_path` (string) **REQ** — Contains additional context about the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`MandatoryNotFoundLayoutRuleWriteError`:
  > Represents the error response returned when the operation fails due to a mandatory not found layout rule write error.
  - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
    - `layout_rule` (object) **REQ** — Contains additional context about the error.
      - `name` (string) **REQ** [maxLen=255] — Contains additional context about the error.
      - `id` (string/int64) **REQ** — Contains additional context about the error.
    - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
    - `json_path` (string) **REQ** — Contains additional context about the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`MultipleOrMultiErrorsError`:
  > Represents the error response returned when the operation fails due to a multiple or multi errors error.
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
`NotAllowedDataValueError`:
  > This error occurs when the data provided in the request doesn't meet the expected requirements. The details structure varies based on the cause  not allowed value
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — A unique identifier for this type of error.
  - `message` (string) **REQ** — A clear explanation of what went wrong and why the operation could not complete.
  - `details` (object `InvalidDataFieldValueDetails`) **REQ** — Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates whether the operation succeeded or failed.
`RecordPostErrorDataItem`:
  oneOf:
    - `InvalidDataTypeError` — Represents the error response returned when the operation fails due to a invalid data type error.
    - `InvalidSupportedValuesError` — Represents the error response returned when the operation fails due to a invalid supported values error.
    - `InvalidMaxLengthError` — Represents the error response returned when the operation fails due to a invalid max length error.
    - `InvalidDataMaxLengthError` — Represents the error response returned when the operation fails due to invalid data exceeding the maximum length.
    - `InvalidDataValueError` — Represents the error response returned when the operation fails due to a invalid data value error.
    - `NotAllowedDataValueError` — This error occurs when the data provided in the request doesn't meet the expected requirements. The details structure varies based on the cause  not allowed value
    - `InvalidModuleError` — Represents the error response returned when the operation fails due to a invalid module error.
    - `MultipleOrMultiErrorsError` — Represents the error response returned when the operation fails due to a multiple or multi errors error.
    - `DependentFieldMissingError` — Represents the error response returned when the operation fails due to a dependent field missing error.
    - `DependentServiceError` — Represents the error response returned when the operation fails due to a dependent service error.
    - `MandatoryNotFoundError` — Represents the error response returned when the operation fails due to a mandatory not found error.
    - `MandatoryNotFoundLayoutRuleWriteError` — Represents the error response returned when the operation fails due to a mandatory not found layout rule write error.
    - `DependentMismatchError` — Represents the error response returned when the operation fails due to a dependent mismatch error.
    - `InvalidRequestMethodError` — Represents the error response returned when the operation fails due to a invalid request method error.
    - `AuthorizationFailedError` — Represents the error response returned when the operation fails due to a authorization failed error.
    - `DuplicateDataError` — Represents the error response returned when the operation fails due to a duplicate data error.
`RecordPostSuccessDataItem`:
  > Represents a single record post success data result item.
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

**Request Body** (required) — application/json `RecordsInputSchema`
> To insert a single record, send only one JSON object in the input with the necessary keys and values. Duplicates are checked for every insert record API call based on unique fields. A maximum of 100 records can be inserted per API call. You must use only Field API names in the input. You can obtain the field API names from the [Fields metadata API](fields.yaml#$.paths./settings/fields.get) Choose "Fields" from the "Filter By" drop-down. In the Calls module, the call duration for an Inbound or Outbound call cannot be zero. For any module, specify all the mandatory fields while creating a record. When inserting multiple records, the Response JSON array maintains the same order as the input records, allowing each response to be mapped to its respective input record. In case of partial success or failure, the API returns an HTTP status 207 (Multi-Status), where individual record-level success or error details are provided within the response array in the same order. You must provide the layout ID field if you want to, include the layout specific mandatory fields in the API-level mandatory check. Include only the fields that are defined in your layout for API-level processing and ignore the rest.
  > The request body for Records Post
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

- **201**: Returns the details of each successfully created record, including the record ID and audit metadata. — Schema: `RecordSuccessResponse` [application/json]
    > Represents the response schema for the recordsuccess operation.
    schema: `RecordSuccessResponse`
    - `data` (array of object `RecordPostSuccessDataItem`) [minItems=1, maxItems=100] **REQ** — Represents the data value.

- **207**: Returns a multi-status response when some record create operations succeed and others fail. Each item in the data array independently reports the outcome for the corresponding record. [application/json]
    > Represents the response returned when a bulk record create operation results in mixed success and failure outcomes.
    - `data` (array of object) [minItems=2, maxItems=100] **REQ** — Contains the list of per-record results. Each item represents either a successfully created record or an error identified by its **code** value.
      oneOf:
        - `RecordPostSuccessDataItem` — Represents a single record post success data result item.
        - `RecordPostErrorDataItem` — Represents the error response returned when the operation fails due to a record post data item error.

- **400**: The request could not be processed because one or more records contain invalid data or missing required fields.  **Resolution:** Each error in the data array identifies the specific record and field that caused the failure. The request must be corrected and resubmitted. — Schema: `RecordsPostErrorResponse` [application/json]
    > Standard error response schema returned when record operations fail.
    oneOf:
      - `NotApprovedError` — Represents the error response returned when the operation fails due to a not approved error.
        - `code` (string) **REQ** [enum=['NOT_APPROVED']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `InvalidDataValueError` — Represents the error response returned when the operation fails due to a invalid data value error.
      - `InvalidDataTypeError` — Represents the error response returned when the operation fails due to a invalid data type error.
      - `InvalidDataTypeSupportedValuesError` — This error occurs when the data provided in the request doesn't meet the expected requirements. The details structure varies based on the cause -  data type mismatch and unsupported values.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — A unique identifier for this type of error.
        - `message` (string) **REQ** — A clear explanation of what went wrong and why the operation could not complete.
        - `details` (object `InvalidDataTypeSupportedValuesDetails`) **REQ** — Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
          schema: `InvalidDataTypeSupportedValuesDetails`
          - `expected_data_type` (string) **REQ** [maxLen=255] — The type of data that the field expects to receive, such as text, number, true/false value, list, or structured object.
          - `api_name` (string) **REQ** — The API name of the field that received an unsupported value.
          - `json_path` (string) **REQ** — Represents the JSONPath location pointing to the field that caused the error.
          - `supported_values` (array of string) **REQ** — Contains the list of valid values accepted for this field.
            items: [maxLen=255]
        - `status` (string) **REQ** [enum=['error']] — Indicates whether the operation succeeded or failed.
      - `MandatoryNotFoundError` — Represents the error response returned when the operation fails due to a mandatory not found error.
      - `RecordsDataPostErrorResponse` — Standard error response schema returned when one or more record operations fail.
        - `data` (array of object `RecordPostErrorDataItem`) [minItems=1, maxItems=100] **REQ** — List of error objects describing failures encountered while processing record operation requests.
      - `InvalidSupportedValuesError` — Represents the error response returned when the operation fails due to a invalid supported values error.
      - `DependentFieldMissingError` — Represents the error response returned when the operation fails due to a dependent field missing error.
      - `InvalidMaxLengthError` — Represents the error response returned when the operation fails due to a invalid max length error.

- **401**: Authentication failed because the OAuth token is missing, expired, or does not have the required scope. **Resolution:** Generate a new access token with the required scope for this operation. — Schema: `RecordUnauthorizedResponse` [application/json]
    > Represents the response schema for the record unauthorized operation.
    schema: `RecordUnauthorizedResponse`
    - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **403**: Permission denied to create records in the specified module.  **Resolution:** The CRM administrator must grant the required create permission to the user's profile. — Schema: `RecordPermissionResponse` [application/json]
    > Represents the response schema for the record permission operation.
    schema: `RecordPermissionResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.
      - `permissions` (array of string) [minItems=1, maxItems=100] **REQ** — Contains additional context about the error.
        items: [maxLen=255]

- **404**: The request URL does not match any valid API endpoint pattern.  **Resolution:** The API endpoint URL must be verified for correct format and path parameters. — Schema: `RecordInvalidURLResponse` [application/json]
    > Represents the response schema for the record invalid URL operation.
    schema: `RecordInvalidURLResponse`
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **500**: An unexpected server error occurred while processing the request.  **Resolution:** The request can be retried after some time. If the error persists, Zoho CRM support must be contacted. — Schema: `RecordInternalErrorResponse` [application/json]
    > Represents the error response returned when the operation fails due to a record internal response error.
    schema: `RecordInternalErrorResponse`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

**Scopes:** ZohoCRM.modules.CREATE
