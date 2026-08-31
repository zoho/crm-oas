# PUT /settings/variables
**Operation:** `updateVariables` — Update variables
> Updates one or more CRM variables in a single request. The id key is mandatory in the request body to identify each variable. You cannot update the type or variable group of a variable. Requires the ZohoCRM.settings.variables.UPDATE scope.

**Request Body** — application/json `VariablesBatchUpdateRequestAlt1`
> The request body containing the variable data to update.
  > Alternate instance of the batch update request wrapper holding an array of variable update items.
  - `variables` (array of object `ScopedVariableUpdateItem`) [maxItems=25] **REQ** — Array of variable update items to process. Mandatory.
    schema: `ScopedVariableUpdateItem`
    - `id` (string/int64) **REQ** [maxLen=19] — Id of variables
    - `value` (string) **REQ** [maxLen=3000, nullable] — describes value for the variables

**Responses:**

- **200**: OK - Successful response — Schema: `VariablesBatchUpdateResponse` [application/json]
    > Success response summarizing the outcome of a batch update, with an array of per-item operation results.
    schema: `VariablesBatchUpdateResponse`
    - `variables` (array of object `VariableOperationResult`) [maxItems=1] — Array of operation results for each updated variable.
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
            - `VariableGroupAmbiguityError` — Error payload indicating ambiguity while processing variable group identifiers, such as conflicting id and api_name references.
              - `code` (string) **REQ** [enum=['AMBIGUITY_DURING_PROCESSING']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `ambiguity_due_to` (array of object) [maxItems=25] **REQ** — Detail field: ambiguity_due_to
                  - `api_name` (string) **REQ** [maxLen=255] — Nested detail field: api_name
                  - `json_path` (string) **REQ** [maxLen=1000] — Nested detail field: json_path
              - `message` (string) **REQ** [enum=['Ambiguity while processing the request']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `VariablesDuplicateDataExtendedError` — Duplicate data error with extended validation details. Includes code DUPLICATE_DATA, detailed context, message, and status.
              - `code` (string) **REQ** [enum=['DUPLICATE_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['duplicate data']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Error status
            - `VariableGroupInvalidReferenceError` — Error payload returned when the supplied variable group identifier (id) is invalid during variable processing.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
              - `details` (object) **REQ** — Error details with validation information
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['the id given seems to be invalid']] — Represents the error message.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.

**Scopes:** ZohoCRM.settings.variables.UPDATE
