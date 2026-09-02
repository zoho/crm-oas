# POST /{module}/upsert
**Operation:** `upsertRecords` — Create or update records in a specified module
> The Upsert API inserts a new record or updates an existing record based on duplicate check field values. If a matching record is found, it is updated; otherwise, a new record is inserted.
When using the Upsert API, the system checks for duplicate records based on the duplicate check fields. There are two types of duplicate check fields: system-defined duplicate check fields and user-defined unique fields.
System-defined duplicate check fields are predefined unique fields for each module. The system automatically checks these fields to prevent duplicate records. Refer to the System-defined Duplicate Check Fields section for module-specific details.
User-defined unique fields are fields for which the "Do not allow duplicate values" option is enabled. These fields allow users to define custom fields for duplicate checking. For more information, refer to [Mark a Field as Unique](https://help.zoho.com/portal/en/kb/crm/customize-crm-account/customizing-fields/articles/use-custom-fields#Mark_a_Field_as_Unique). When a record is upserted, the system first checks for duplicates in these fields. If a matching record exists, it gets updated; otherwise, a new record is inserted.
You can specify the order in which the system checks for duplicate records using the "duplicate_check_fields" array in the API request. The array can contain system-defined duplicate check fields, such as "Email" for the Leads module, and user-defined unique fields, such as "Phone" and "Fax".
For example, in the Leads module, you can specify: "duplicate_check_fields": ["Email", "Phone", "Fax"].
If "duplicate_check_fields" is not specified, the system checks duplicate records in the following order: 1. System-defined duplicate check fields. 2. User-defined unique fields.

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

**Request Body** (required) — application/json `RecordsUpsertSchema`
> The request body must contain a **data** array. You can include a maximum of 100 objects per request. You must use only Field API names in the input; obtain them from the [Get Fields Metadata API](fields.yaml#$.paths./settings/fields.get). The "INVALID_DATA" error is returned if a field value exceeds the maximum length defined for that field. For example, if a Text field has a maximum length of 10 characters, the API cannot accept a value such as "12345678901", since it contains 11 characters. Records with subform details can also be inserted or updated through this API. Provide the layout ID to include layout-specific mandatory fields in the API-level mandatory field check; only the fields defined in that layout are considered for processing, and the rest are ignored.
  > Request body schema for upsert operations, allowing creation or update of records based on duplicate fields.
  - `data` (array of object `RecordSinglePutWriteDataItem`) [minItems=1, maxItems=100] **REQ** — List of records to be created or updated using the upsert operation.
    schema: `RecordSinglePutWriteDataItem`
    - `$append_values` (string) [maxLen=10] — Represents the $append values value.
    - `Layout` (object) — Represents the layout value. Use the [Get Layouts Metadata API](layouts.yaml#$.paths./settings/layouts.get) to retrieve the Layout ID.
      - `id` (string/int64) **REQ** [maxLen=19, minLen=1, pattern=^[0-9]{1,19}$] — Represents the layout value.
    additionalProperties: any
  - `trigger` (array of string) — Specifies the CRM features to execute for the API request. Supported values are "workflow", "approval", and "blueprint". If the "trigger" parameter is not specified, workflows, approvals, and blueprints related to the API are executed. Specify an empty array [] to prevent these features from executing.
    items: [enum=['approval', 'workflow', 'blueprint', 'pathfinder', 'orchestration']]
  - `duplicate_check_fields` (array of string) — Specifies the fields used to check for duplicate records during an Upsert operation. Duplicate check fields can be system-defined unique fields or user-defined unique fields.  
The following are the system-defined duplicate check fields for the respective modules: Leads - "Email"; Accounts - "Account_Name"; Contacts - "Email"; Deals - "Deal_Name"; Campaigns - "Campaign_Name"; Cases - "Subject"; Solutions - "Solution_Title"; Products - "Product_Name"; Vendors - "Vendor_Name"; PriceBooks - "Price_Book_Name"; Quotes - "Subject"; SalesOrders - "Subject"; PurchaseOrders - "Subject"; Invoices - "Subject"; Custom Modules - "Name".
If a matching record is found based on these fields, the record is updated; otherwise, a new record is inserted.
    items: [maxLen=100]
  - `wf_trigger` (string) [maxLen=50, nullable] — Workflow trigger identifier to be executed as part of the upsert operation.
  - `lar_id` (string) [maxLen=19, minLen=1, pattern=^[1-9][0-9]{0,18}$] — The unique ID of the assignment rule to trigger while inserting a record. Use the Get Assignment Rules API to retrieve valid values. This key must be provided parallel to the data key. Supported for all modules where assignment rules are applicable, such as Leads, Contacts, Deals, Accounts, Tasks, Cases, and Custom.

**Responses:**

- **200**: Returns the details of each successfully processed records, including the record ID and audit metadata. — Schema: `RecordUpsertSuccessResponse` [application/json]
    > Represents the response schema for the record upsert success operation.
    schema: `RecordUpsertSuccessResponse`
    - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the data value.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the data value.
      - `duplicate_field` (string) **REQ** [maxLen=255, nullable] — Represents the data value.
      - `action` (string) **REQ** [enum=['insert', 'update']] — Represents the data value.
      - `message` (string) **REQ** — Represents the data value.
      - `status` (string) **REQ** [enum=['success']] — Represents the data value.
      - `details` (object) **REQ** — Represents the data value.
        - `id` (string/int64) **REQ** — Represents the data value.
        - `Modified_Time` (string/date-time) — Represents the data value.
        - `Created_Time` (string/date-time) — Represents the data value.
        - `Created_By` (object) — Represents the data value.
          - `name` (string) **REQ** [maxLen=101] — Represents the data value.
          - `id` (string/int64) **REQ** — Represents the data value.
        - `Modified_By` (object) — Represents the data value.
          - `name` (string) **REQ** [maxLen=101] — Represents the data value.
          - `id` (string/int64) **REQ** — Represents the data value.
        - `$approval_state` (string) [maxLen=255] — Represents the data value.

- **207**: Returns a multi-status response when some record upsert operations succeed and others fail. Each item in the data array independently reports the outcome for the corresponding record. [application/json]
    > Represents the multi-status response returned when a bulk operation results in mixed success and failure outcomes.
    - `data` (array of object) [minItems=2, maxItems=100] **REQ** — Contains the list of per-record results for the operation.
      oneOf:
        - `RecordUpsertSuccessDataItem` — Represents a single record upsert success data result item.
          - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the error code identifying the type of failure.
          - `duplicate_field` (string) **REQ** [maxLen=255, nullable] — Represents the duplicate field value.
          - `action` (string) **REQ** [enum=['insert', 'update']] — Represents the action that triggered the record lock.
          - `message` (string) **REQ** — Represents the error message describing why the operation failed.
          - `status` (string) **REQ** [enum=['success']] — Indicates the overall result status of the request.
          - `details` (object) **REQ** — Contains additional context about the error.
            - `id` (string/int64) **REQ** — Contains additional context about the error.
            - `Modified_Time` (string/date-time) — Contains additional context about the error.
            - `Created_Time` (string/date-time) — Contains additional context about the error.
            - `Created_By` (object) — Contains additional context about the error.
              - `name` (string) **REQ** [maxLen=101] — Contains additional context about the error.
              - `id` (string/int64) **REQ** — Contains additional context about the error.
            - `Modified_By` (object) — Contains additional context about the error.
              - `name` (string) **REQ** [maxLen=101] — Contains additional context about the error.
              - `id` (string/int64) **REQ** — Contains additional context about the error.
            - `$approval_state` (string) [maxLen=255] — Contains additional context about the error.
        - `RecordUpsertErrorDataItem` — Represents the error response returned when the operation fails due to a record upsert data item error.
          oneOf:
            - `InvalidDataTypeError` — Represents the error response returned when the operation fails due to a invalid data type error.
            - `InvalidSupportedValuesError` — Represents the error response returned when the operation fails due to a invalid supported values error.
            - `InvalidMaxLengthError` — Represents the error response returned when the operation fails due to a invalid max length error.
            - `InvalidDataValueError` — Represents the error response returned when the operation fails due to a invalid data value error.
            - `InvalidModuleError` — Represents the error response returned when the operation fails due to a invalid module error.
            - `MultipleOrMultiErrorsError` — Represents the error response returned when the operation fails due to a multiple or multi errors error.
            - `DependentFieldMissingError` — Represents the error response returned when the operation fails due to a dependent field missing error.
            - `MandatoryNotFoundError` — Represents the error response returned when the operation fails due to a mandatory not found error.
            - `DependentMismatchError` — Represents the error response returned when the operation fails due to a dependent mismatch error.
            - `InvalidRequestMethodError` — Represents the error response returned when the operation fails due to a invalid request method error.
            - `AuthorizationFailedError` — Represents the error response returned when the operation fails due to a authorization failed error.
            - `DuplicateDataError` — Represents the error response returned when the operation fails due to a duplicate data error.

- **400**: The request could not be processed because one or more records contain invalid data or missing required fields.
**Resolution:** Each error in the data array identifies the specific record and field that caused the failure. The request must be corrected and resubmitted. — Schema: `RecordsUpsertErrorResponse` [application/json]
    oneOf:
      - `InvalidMaxLengthError` — Represents the error response returned when the operation fails due to a invalid max length error.
      - `NotApprovedError` — Represents the error response returned when the operation fails due to a not approved error.
        - `code` (string) **REQ** [enum=['NOT_APPROVED']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `InvalidDataTypeError` — Represents the error response returned when the operation fails due to a invalid data type error.
      - `MandatoryNotFoundError` — Represents the error response returned when the operation fails due to a mandatory not found error.
      - `InvalidSupportedValuesError` — Represents the error response returned when the operation fails due to a invalid supported values error.
      - `RecordsDataUpsertErrorResponse` — Standard error response schema returned when one or more record operations fail.
        - `data` (array of object) [minItems=1, maxItems=100] **REQ** — List of error objects describing failures encountered while processing record operation requests.
          oneOf:
            - `InvalidDataTypeError` — Represents the error response returned when the operation fails due to a invalid data type error.
            - `InvalidSupportedValuesError` — Represents the error response returned when the operation fails due to a invalid supported values error.
            - `InvalidMaxLengthError` — Represents the error response returned when the operation fails due to a invalid max length error.
            - `InvalidDataValueError` — Represents the error response returned when the operation fails due to a invalid data value error.
            - `InvalidModuleError` — Represents the error response returned when the operation fails due to a invalid module error.
            - `MultipleOrMultiErrorsError` — Represents the error response returned when the operation fails due to a multiple or multi errors error.
            - `DependentFieldMissingError` — Represents the error response returned when the operation fails due to a dependent field missing error.
            - `DependentServiceError` — Represents the error response returned when the operation fails due to a dependent service error.
              - `code` (string) **REQ** [enum=['DEPENDENT_SERVICE_ERROR']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `dependency_error` (string) **REQ** [enum=['NO_PERMISSION', 'LIMIT_EXCEEDED', 'PROCESSING_ERROR', 'CANNOT_PROCESS']] — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
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
            - `MandatoryNotFoundLayoutRuleError` — Represents the error response returned when the operation fails due to a mandatory not found layout rule error.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `layout_rule` (object) **REQ** — Contains additional context about the error.
                  - `name` (string) **REQ** [maxLen=255] — Contains additional context about the error.
                  - `id` (string/int64) **REQ** — Contains additional context about the error.
                - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
                - `json_path` (string) **REQ** — Contains additional context about the error.
                - `id` (string/int64) **REQ** — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `MandatoryNotFoundRecordIdError` — Represents the error response returned when the operation fails due to a mandatory not found record ID error.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code identifying the type of failure.
              - `message` (string) **REQ** — Represents the error message describing why the operation failed.
              - `details` (object) **REQ** — Contains additional context about the error.
                - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
                - `json_path` (string) **REQ** — Contains additional context about the error.
                - `id` (string/int64) **REQ** — Contains additional context about the error.
              - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `DependentMismatchError` — Represents the error response returned when the operation fails due to a dependent mismatch error.
            - `InvalidRequestMethodError` — Represents the error response returned when the operation fails due to a invalid request method error.
            - `AuthorizationFailedError` — Represents the error response returned when the operation fails due to a authorization failed error.
            - `DuplicateDataError` — Represents the error response returned when the operation fails due to a duplicate data error.
      - `DependentFieldMissingError` — Represents the error response returned when the operation fails due to a dependent field missing error.

- **401**: Authentication failed because the OAuth token is missing, expired, or does not include the required scope.
**Resolution:** A new access token must be generated with the required scope for this operation. — Schema: `RecordUnauthorizedResponse` [application/json]
    > Represents the response schema for the record unauthorized operation.
    schema: `RecordUnauthorizedResponse`
    - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **403**: Permission denied to upsert records in the specified module.
**Resolution:** The CRM administrator must grant the required upsert permission to the user's profile. — Schema: `RecordPermissionResponse` [application/json]
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
      - `message` (string) **REQ** [maxLen=255] — Contains the list of per-record results for the operation.
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

**Scopes:** ZohoCRM.modules.CREATE
