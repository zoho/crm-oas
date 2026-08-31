# PUT /settings/variables/{id}
**Operation:** `updateVariableById` — Specific variable
> Updates a specific CRM variable identified by its ID or API name. You cannot update the type or variable group of the variable. For the list of updatable input keys, refer to the Create Variables operation. Requires the ZohoCRM.settings.variables.UPDATE scope.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: The unique ID of the variable. Mandatory.

**Request Body** — application/json `VariablesScopedBatchUpdateRequestAlt1`
> The request body containing the variable data to update.
  > Alternate instance of the scoped batch update request wrapper for variable updates.
  - `variables` (array of object `ScopedVariableUpdateItem`) [maxItems=1] **REQ** — Array of variable update items to process. Mandatory.
    schema: `ScopedVariableUpdateItem`
    - `id` (string/int64) **REQ** [maxLen=19] — Id of variables
    - `value` (string) **REQ** [maxLen=3000, nullable] — describes value for the variables

**Responses:**

- **200**: OK - Successful response — Schema: `VariablesScopedBatchUpdateResponse` [application/json]
    > Success response summarizing scoped batch updates with an array of per-item operation results.
    schema: `VariablesScopedBatchUpdateResponse`
    - `variables` (array of object `VariableOperationResult`) [maxItems=1] — Array of variable update items to process.
      schema: `VariableOperationResult`
      - `code` (string) [maxLen=255] — The result code of the operation (for example, SUCCESS, INVALID_DATA).
      - `details` (object `VariableResultDetails`) — Details of an individual variable operation result, including the id of the affected variable.
        schema: `VariableResultDetails`
        - `id` (string/int64) — The unique ID of the affected variable.
        - `api_name` (string) [maxLen=100] — The API name of the affected variable.
        - `json_path` (string) [maxLen=255] — The JSON path to the field that caused the error.
      - `message` (string) [maxLen=255] — A human-readable message describing the result of the operation.
      - `status` (string) [maxLen=255] — The status of the operation (for example, success or error).

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    > Error response for invalid request
    oneOf:
      - `VariablesDomainNotSupportedError` — Returned when the operation is not supported for the selected domain. Includes code INVALID_DATA and validation details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) — The index of the invalid resource in the URL path.
        - `message` (string) **REQ** [enum=['invalid data', 'the id given seems to be invalid or already deleted']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `VariablesInvalidTypeError` — Indicates an invalid data type for the variables field. Includes code INVALID_DATA and validation details.
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'PATTERN_NOT_MATCHED']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `maximum_length` (integer/int32) — The maximum allowed length for the field.
          - `api_name` (string) [maxLen=255] — The API name of the field that caused the error.
          - `json_path` (string) [maxLen=1000] — The JSON path to the field that caused the error.
        - `message` (string) **REQ** [enum=[3 values]] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
        - `variables` (array of object) [maxItems=25] **REQ** — Array of error objects
          oneOf:
            - `VariablesDuplicateDataExtendedError` — Duplicate data error with extended validation details. Includes code DUPLICATE_DATA, detailed context, message, and status.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['duplicate data']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `VariableValueInvalidDataError` — Indicates invalid data supplied for a variable's value during update. Includes code INVALID_DATA and validation details.
              - `code` (string) **REQ** [enum=['INVALID_DATA', 'PATTERN_NOT_MATCHED']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `expected_data_type` (string) [maxLen=255] — The expected data type for the field.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['invalid data', 'Please check whether the input values are correct']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
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

**Scopes:** ZohoCRM.settings.variables.UPDATE
