# POST /settings/variables
**Operation:** `createVariables` — Create variables
> Creates one or more CRM variables. The name, api_name, and variable_group keys are mandatory. The type key specifies the data type of the variable. Possible types: integer, text, percent, decimal, currency, date, datetime, email, phone, url, checkbox, textarea, long. Requires the ZohoCRM.settings.variables.CREATE scope.

**Schemas:**
`VariableOperationResult`:
  > Per-item outcome for a variable operation, including code, message, status, and details such as the resulting variable id.
  - `code` (string) [maxLen=255] — The result code of the operation (for example, SUCCESS, INVALID_DATA).
  - `details` (object `VariableResultDetails`) — Details of an individual variable operation result, including the id of the affected variable.
  - `message` (string) [maxLen=255] — A human-readable message describing the result of the operation.
  - `status` (string) [maxLen=255] — The status of the operation (for example, success or error).
`VariableResultDetails`:
  > Details of an individual variable operation result, including the id of the affected variable.
  - `id` (string/int64) — The unique ID of the affected variable.
  - `api_name` (string) [maxLen=100] — The API name of the affected variable.
  - `json_path` (string) [maxLen=255] — The JSON path to the field that caused the error.

**Request Body** — application/json `VariablesBatchInput`
> The request body containing the variable definitions to create.
  > Request body wrapper that carries an array of variable definitions to be processed in a single batch.
  - `variables` (array of object `VariableCreationItem`) [maxItems=2] **REQ** — Array of variable definitions to create. Maximum: 25 items.
    schema: `VariableCreationItem`
    - `api_name` (string) **REQ** [maxLen=100, pattern=^[a-zA-Z]+\w*[a-zA-Z0-9]*$] — Specify the API name of the variables.
    - `name` (string) **REQ** [maxLen=50] — Specify the name of the variables.
    - `description` (string) [maxLen=250, nullable] — Specify the description of the variables.
    - `type` (string) **REQ** [maxLen=7, enum=['text', 'integer', 'boolean', 'date', 'float']] — Specify the type of the variables
    - `variable_group` (object `VariableGroupIdentifierInput`) **REQ** — Variable Groups json object (Required)
      schema: `VariableGroupIdentifierInput`
      - `id` (string/int64) **REQ** — The unique ID of the variable group. Mandatory.
    - `value` (integer/int32) [nullable] — Initial value of variable

**Responses:**

- **201**: Created - Resource created successfully — Schema: `VariablesBatchOperationCreated` [application/json]
    > Summary response for a batch variables operation where all items are created successfully. Includes an array of per-item results.
    schema: `VariablesBatchOperationCreated`
    - `variables` (array of object `VariableOperationResult`) [maxItems=5] — Array of operation results for each created variable.

- **207**: Multi-Status - Response contains mixed status results — Schema: `VariablesBatchOperationMultiStatus` [application/json]
    > Batch response indicating mixed successes and failures. Contains a variables array with per-item outcomes and related details.
    schema: `VariablesBatchOperationMultiStatus`
    - `variables` (array of object `VariableOperationResult`) [maxItems=2] — Array of per-item operation results indicating success or failure for each variable.

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    > Error response for invalid request
    oneOf:
        - `variables` (array of object) [maxItems=25] **REQ** — Array of error objects
          oneOf:
            - `VariablesRequestBodyMissingError` — Error returned when the request body is missing. Includes code INVALID_DATA, validation details, message, and error status.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) **REQ** [maxLen=255] — The expected data type for the field.
              - `message` (string) **REQ** [enum=['body']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `VariablesRequiredFieldMissingError` — Error returned when the required variables field is not provided. Includes code MANDATORY_NOT_FOUND and validation details.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — The API name of the field that caused the error.
              - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
            - `VariablesDuplicateDataError` — Indicates that submitted data duplicates existing records. Includes code DUPLICATE_DATA, details, message, and status.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — The API name of the field that caused the error.
              - `message` (string) **REQ** [enum=['duplicate data']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
            - `VariablesDuplicateDataExtendedError` — Duplicate data error with extended validation details. Includes code DUPLICATE_DATA, detailed context, message, and status.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['duplicate data']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `VariablesMandatoryFieldMissingError` — Error for a missing required field in the payload. Includes code MANDATORY_NOT_FOUND and validation details.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `VariablesInvalidDataTypeError` — General invalid data type error with validation details. Includes code INVALID_DATA and a descriptive message.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) **REQ** [maxLen=255] — The expected data type for the field.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
            - `VariablesInvalidDataError` — Generic invalid data error for the submitted payload. Includes code INVALID_DATA, details, message, and status.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `maximum_length` (integer/int32) **REQ** — The maximum allowed length for the field.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data', 'invalid data']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `VariablesInvalidDataGenericError` — Generic invalid data response with standard error structure. Includes code INVALID_DATA and validation details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `regex` (string) **REQ** [maxLen=255] — The regular expression pattern that the field value must match.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
            - `VariablesInvalidDataGeneralError` — Another form of invalid data error with validation details. Includes code INVALID_DATA and message.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
                - `supported_values` (array of string) [maxItems=25] — Detail field: supported_values
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
            - `VariableGroupInvalidReferenceError` — Error payload returned when the supplied variable group identifier (id) is invalid during variable processing.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
            - `VariableGroupAmbiguityError` — Error payload indicating ambiguity while processing variable group identifiers, such as conflicting id and api_name references.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Detail field: ambiguity_due_to
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `VariableValueInvalidDataError` — Indicates invalid data supplied for a variable's value during update. Includes code INVALID_DATA and validation details.
              - `code` (string) **REQ** [enum=['INVALID_DATA', 'PATTERN_NOT_MATCHED']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) [maxLen=255] — The expected data type for the field.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['invalid data', 'Please check whether the input values are correct']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
      - `VariablesInvalidTypeError` — Indicates an invalid data type for the variables field. Includes code INVALID_DATA and validation details.
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'PATTERN_NOT_MATCHED']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `maximum_length` (integer/int32) — The maximum allowed length for the field.
          - `api_name` (string) [maxLen=255] — The API name of the field that caused the error.
          - `json_path` (string) [maxLen=1000] — The JSON path to the field that caused the error.
        - `message` (string) **REQ** [enum=[3 values]] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
        - `variables` (array of object) [maxItems=1] **REQ** — Array of error details
          - `status` (string) **REQ** [enum=['error']] — Status of the operation
          - `code` (string) **REQ** [enum=['LIMIT_EXCEEDED']] — Represents the error code.
          - `message` (string) **REQ** [maxLen=500] — A human-readable error message.
          - `details` (object) **REQ** — Additional error details
        - `variables` (array of object) [maxItems=1] **REQ** — Array of error details
          - `status` (string) **REQ** [enum=['error']] — Status of the operation
          - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code.
          - `message` (string) **REQ** [maxLen=500] — A human-readable error message.
          - `details` (object) **REQ** — Additional error details
            - `api_name` (string) **REQ** [maxLen=100] — The API name of the field that is not allowed.
            - `json_path` (string) **REQ** [maxLen=500] — The JSON path to the field that is not allowed.
        - `variables` (array of object) [maxItems=1] **REQ** — Array of error details
          - `status` (string) **REQ** [enum=['error']] — Status of the operation
          - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Represents the error code.
          - `message` (string) **REQ** [maxLen=500] — A human-readable error message.
          - `details` (object) **REQ** — Additional error details
            - `api_name` (string) **REQ** [maxLen=100] — The API name of the field that is not allowed.
            - `json_path` (string) **REQ** [maxLen=500] — The JSON path to the field that is not allowed.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code.
        - `details` (object) **REQ** — Additional error details
          - `api_name` (string) **REQ** [maxLen=100] — The API name of the missing required parameter.
        - `message` (string) **REQ** [maxLen=500] — A human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.

**Scopes:** ZohoCRM.settings.variables.CREATE
