# PUT /{module}
**Operation:** `updateRecords` — Update records in a specified module
> Updates one or more existing records in the specified module in your Zoho CRM organization. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module API name and the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to retrieve the field API names.
A maximum of 100 records can be updated per API call. Use only Field API names in the input. You can update all fields supported by the Insert Records API operation.
When updating multiple records, the response array maintains the same order as the input records, allowing each response to be mapped to its corresponding input record. 
To update multiple subform records, specify the subform API name as a key within the record and provide the subform records as a JSON array. Use the subform field API names as keys within each subform record. For detailed information on subforms, refer to the [Manipulating Subform using Zoho CRM APIs](https://help.zoho.com/portal/en/community/topic/kaizen-124-accessing-subform-using-zoho-crm-apis).
Use the [Modules API](modules.yaml#$.paths./settings/modules.get) and [Fields Metadata API](fields.yaml#$.paths./settings/fields.get) to retrieve the API names of the subform and its fields. To update an existing subform record, include its record ID in the subform JSON array. Use the [Get Records API](record.yaml#$.paths./module.get) with the subform API name to retrieve subform record IDs.
When adding a new subform record, it is appended to the existing records. Passing an empty JSON array for a subform deletes all its records. To delete a specific subform record, specify its record ID and set "_delete" to "null". Deleting the parent record also deletes all its subform records.
  

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
`NotApprovedError`:
  > Represents the error response returned when the operation fails due to a not approved error.
  - `code` (string) **REQ** [enum=['NOT_APPROVED']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
    - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`NotReviewedError`:
  > Represents the error response returned when the operation fails due to a not reviewed error.
  - `code` (string) **REQ** [enum=['NOT_REVIEWED']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
`RecordLockedError`:
  > Represents the error response returned when the operation fails due to a record locked error.
  - `code` (string) **REQ** [enum=['RECORD_LOCKED']] — Represents the error code identifying the type of failure.
  - `message` (string) **REQ** — Represents the error message describing why the operation failed.
  - `details` (object) **REQ** — Contains additional context about the error.
    - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
    - `action` (string) **REQ** [maxLen=50] — The specific action that was attempted on the locked record, such as record_locking.
    - `json_path` (string) **REQ** — Contains additional context about the error.
  - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
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

**Request Body** (required) — application/json `RecordsPutInputSchema`
> The request body must contain a **data** array. You can include a maximum of 100 objects per request. Each object must include an **id** field to identify the record to update.
  > Request body containing the updated resource data to modify the existing record.
  - `data` (array of object `RecordPutWriteDataItem`) [minItems=1, maxItems=100] **REQ** — Represents the data value.
    schema: `RecordPutWriteDataItem`
    - `id` (string/int64) **REQ** — Represents the unique identifier of the RecordPutWriteDataItem record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.
    - `$append_values` (string) [maxLen=10] — Represents the $append values value.
    - `Layout` (object) — Represents the layout value. Use the [Get Layouts Metadata API](layouts.yaml#$.paths./settings/layouts.get) to retrieve the Layout ID.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents the layout value.
    additionalProperties: any
  - `apply_feature_execution` (array of object) — Represents the apply feature execution value.
    - `name` (string) **REQ** [enum=[7 values]] — Represents the apply feature execution value.
  - `skip_feature_execution` (array of object) — Represents the skip feature execution value.
    - `name` (string) **REQ** [enum=['assignment_rules', 'cadences', 'connected_workflows']] — Represents the skip feature execution value.
  - `trigger` (array of string) — Represents the trigger value.
    items: [enum=['approval', 'workflow', 'blueprint', 'pathfinder', 'orchestration']]

**Responses:**

- **200**: Returns the details of each successfully updated records, including the record ID and audit metadata. — Schema: `RecordSuccessResponse` [application/json]
    > Represents the response schema for the recordsuccess operation.
    schema: `RecordSuccessResponse`
    - `data` (array of object `RecordPostSuccessDataItem`) [minItems=1, maxItems=100] **REQ** — Represents the data value.

- **207**: Returns a multi-status response when some record update operations succeed and others fail. Each item in the data array independently reports the outcome for the corresponding record. [application/json]
    > Represents the multi-status response returned when a bulk operation results in mixed success and failure outcomes.
    - `data` (array of object) [minItems=2, maxItems=100] **REQ** — Contains the list of per-record results for the operation.
      oneOf:
        - `RecordPostSuccessDataItem` — Represents a single record post success data result item.
        - `RecordPutErrorDataItem` — Represents the error response returned when the operation fails due to a record put data item error.
          oneOf:
            - `InvalidDataTypeError` — Represents the error response returned when the operation fails due to a invalid data type error.
            - `InvalidSupportedValuesError` — Represents the error response returned when the operation fails due to a invalid supported values error.
            - `InvalidMaxLengthError` — Represents the error response returned when the operation fails due to a invalid max length error.
            - `InvalidDataValueError` — Represents the error response returned when the operation fails due to a invalid data value error.
            - `InvalidModuleError` — Represents the error response returned when the operation fails due to a invalid module error.
            - `MultipleOrMultiErrorsError` — Represents the error response returned when the operation fails due to a multiple or multi errors error.
            - `DependentFieldMissingError` — Represents the error response returned when the operation fails due to a dependent field missing error.
            - `DependentServiceError` — Represents the error response returned when the operation fails due to a dependent service error.
            - `MandatoryNotFoundError` — Represents the error response returned when the operation fails due to a mandatory not found error.
            - `DependentMismatchError` — Represents the error response returned when the operation fails due to a dependent mismatch error.
            - `InvalidRequestMethodError` — Represents the error response returned when the operation fails due to a invalid request method error.
            - `AuthorizationFailedError` — Represents the error response returned when the operation fails due to a authorization failed error.
            - `DuplicateDataError` — Represents the error response returned when the operation fails due to a duplicate data error.
            - `RecordLockedError` — Represents the error response returned when the operation fails due to a record locked error.
            - `NotApprovedError` — Represents the error response returned when the operation fails due to a not approved error.
            - `NotReviewedError` — Represents the error response returned when the operation fails due to a not reviewed error.

- **400**: The request could not be processed because one or more records contain invalid data or missing required fields.
**Resolution:** Each error in the data array identifies the specific record and field that caused the failure. The request must be corrected and resubmitted. — Schema: `RecordsPutErrorResponse` [application/json]
    > Standard error response schema returned when record operations fail.
    oneOf:
      - `MandatoryNotFoundError` — Represents the error response returned when the operation fails due to a mandatory not found error.
      - `InvalidDataValueError` — Represents the error response returned when the operation fails due to a invalid data value error.
      - `RecordsDataPutErrorResponse` — Standard error response schema returned when one or more record operations fail.
        - `data` (array of object) [minItems=1, maxItems=100] **REQ** — List of error objects describing failures encountered while processing record operation requests.
          oneOf:
            - `InvalidDataTypeError` — Represents the error response returned when the operation fails due to a invalid data type error.
            - `InvalidSupportedValuesError` — Represents the error response returned when the operation fails due to a invalid supported values error.
            - `InvalidMaxLengthError` — Represents the error response returned when the operation fails due to a invalid max length error.
            - `InvalidDataValueError` — Represents the error response returned when the operation fails due to a invalid data value error.
            - `InvalidModuleError` — Represents the error response returned when the operation fails due to a invalid module error.
            - `MultipleOrMultiErrorsError` — Represents the error response returned when the operation fails due to a multiple or multi errors error.
            - `DependentFieldMissingError` — Represents the error response returned when the operation fails due to a dependent field missing error.
            - `MandatoryNotFoundError` — Represents the error response returned when the operation fails due to a mandatory not found error.
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
            - `DependentMismatchError` — Represents the error response returned when the operation fails due to a dependent mismatch error.
            - `InvalidRequestMethodError` — Represents the error response returned when the operation fails due to a invalid request method error.
            - `AuthorizationFailedError` — Represents the error response returned when the operation fails due to a authorization failed error.
            - `DuplicateDataError` — Represents the error response returned when the operation fails due to a duplicate data error.
            - `RecordLockedError` — Represents the error response returned when the operation fails due to a record locked error.
            - `NotApprovedError` — Represents the error response returned when the operation fails due to a not approved error.
            - `NotReviewedError` — Represents the error response returned when the operation fails due to a not reviewed error.
            - `LimitExceededError` — Represents the error response returned when the operation fails due to a limit exceeded error.
              - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `maximum_length` (integer/int32) **REQ** — Contains additional context about the error.
                - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `DuplicateLinkingDataError` — Represents the error response returned when the operation fails due to a duplicate linking data error.
              - `code` (string) **REQ** [enum=['DUPLICATE_LINKING_DATA']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `linking_fields` (array of string) [minItems=1] **REQ** — Contains additional context about the error.
                  items: [maxLen=50]
                - `id` (string/int64) **REQ** [maxLen=19] — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `DependentServiceError` — Represents the error response returned when the operation fails due to a dependent service error.
            - `NotAllowedDataValueError` — This error occurs when the data provided in the request doesn't meet the expected requirements. The details structure varies based on the cause  not allowed value
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — A unique identifier for this type of error.
              - `message` (string) **REQ** — A clear explanation of what went wrong and why the operation could not complete.
              - `details` (object `InvalidDataFieldValueDetails`) **REQ** — Additional information pinpointing exactly what was invalid. The structure varies based on the cause of the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates whether the operation succeeded or failed.
      - `InvalidDataTypeError` — Represents the error response returned when the operation fails due to a invalid data type error.
      - `DependentFieldMissingError` — Represents the error response returned when the operation fails due to a dependent field missing error.
      - `InvalidSupportedValuesError` — Represents the error response returned when the operation fails due to a invalid supported values error.
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

- **401**: Authentication failed because the OAuth token is missing, expired, or does not include the required scope.
**Resolution:** A new access token must be generated with the required scope for this operation. — Schema: `RecordUnauthorizedResponse` [application/json]
    > Represents the response schema for the record unauthorized operation.
    schema: `RecordUnauthorizedResponse`
    - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **403**: Permission denied to update records in the specified module.
**Resolution:** The CRM administrator must grant the required update permission to the user's profile. — Schema: `RecordPermissionResponse` [application/json]
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

- **412**: The record has been modified after the timestamp specified in the If-Unmodified-Since header.
**Resolution:** The latest version of the record must be retrieved and the update must be resubmitted with the current modification timestamp. [application/json]
    > Represents the error response returned when the record has been modified after the If-Unmodified-Since timestamp.
    - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Contains the list of per-record results for the operation.
      - `code` (string) **REQ** [enum=['ALREADY_MODIFIED']] — Contains the list of per-record results for the operation.
      - `message` (string) **REQ** — Contains the list of per-record results for the operation.
      - `status` (string) **REQ** [enum=['error']] — Contains the list of per-record results for the operation.
      - `details` (object) — Contains the list of per-record results for the operation.
        - `Modified_Time` (string/date-time) — Contains the list of per-record results for the operation.
        - `Created_Time` (string/date-time) — Contains the list of per-record results for the operation.
        - `id` (string/int64) **REQ** — Contains the list of per-record results for the operation.
        - `Modified_By` (object) — Contains the list of per-record results for the operation.
          - `name` (string) **REQ** [maxLen=101] — Contains the list of per-record results for the operation.
          - `id` (string/int64) **REQ** — Contains the list of per-record results for the operation.
        - `Created_By` (object) — Contains the list of per-record results for the operation.
          - `name` (string) **REQ** [maxLen=101] — Contains the list of per-record results for the operation.
          - `id` (string/int64) **REQ** — Contains the list of per-record results for the operation.

- **500**: An unexpected server error occurred while processing the request.
**Resolution:** The request can be retried after some time. If the error persists, Zoho CRM support must be contacted. — Schema: `RecordInternalErrorResponse` [application/json]
    > Represents the error response returned when the operation fails due to a record internal response error.
    schema: `RecordInternalErrorResponse`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

**Scopes:** ZohoCRM.modules.UPDATE
