# DELETE /settings/variables
**Operation:** `deleteVariables` — Delete variables
> Deletes one or more CRM variables by their IDs. Pass variable IDs as a comma-separated list in the ids query parameter, or pass rids in the rids query parameter. A variable that is associated with other features such as email templates, webhooks, or functions cannot be deleted until the association is removed. Requires the ZohoCRM.settings.variables.DELETE scope.

**Parameters:**
- `ids` (query, array, optional) [minItems=1, maxItems=100, uniqueItems] {style=form, explode=False}: Comma-separated list of variable IDs to delete. Mandatory when deleting multiple variables. Maximum: 100 IDs.

**Responses:**

- **207**: Multi-Status - Response contains mixed status results — Schema: `VariablesBatchRemovalMultiStatusResponse` [application/json]
    > Batch removal response indicating mixed outcomes for multiple variables, with per-item result details.
    schema: `VariablesBatchRemovalMultiStatusResponse`
    - `variables` (array of object `VariableOperationResult`) [maxItems=6] — Array of operation results for each deleted variable.
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
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING', 'EXPECTED_PARAM_MISSING']] — Represents the error code.
        - `details` (object) **REQ** — Additional error details
          - `param_name` (string) **REQ** [maxLen=255] — The name of the parameter that caused the error.
        - `message` (string) **REQ** [maxLen=500] — A human-readable error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
        - `variables` (array of object) [maxItems=1] **REQ** — Array of error details
          - `status` (string) **REQ** [enum=['error']] — Status of the operation
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
          - `message` (string) **REQ** [maxLen=500] — A human-readable error message.
          - `details` (object) **REQ** — Additional error details
            - `id` (string/int64) **REQ** — The ID of the variable that could not be deleted.

**Scopes:** ZohoCRM.settings.variables.DELETE
