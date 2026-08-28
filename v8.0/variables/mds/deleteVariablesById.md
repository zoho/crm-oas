# DELETE /settings/variables/{id}
**Operation:** `deleteVariablesById` — Specific variable
> Deletes a specific CRM variable identified by its ID. A variable that is associated with other features such as email templates, webhooks, or functions cannot be deleted until the association is removed. Requires the ZohoCRM.settings.variables.DELETE scope.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: The unique ID of the variable. Mandatory.

**Responses:**

- **200**: OK - Successful response — Schema: `VariablesScopedRemovalResponse` [application/json]
    > Success response summarizing outcomes of variable removal within a scoped context, with per-item results.
    schema: `VariablesScopedRemovalResponse`
    - `variables` (array of object `VariableOperationResult`) [maxItems=1] — Array of operation results for each deleted variable.
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
      - `InvalidResourceIdError` — Indicates an invalid identifier in the request URL. Includes code INVALID_DATA and contextual details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) — The index of the invalid resource in the URL path.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
        - `variables` (array of object `VariablesRemovalFailedError`) [maxItems=25] **REQ** — Array of error objects
          schema: `VariablesRemovalFailedError`
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
          - `details` (object) **REQ** — Error details with validation information
            - `id` (string/int64) — Detail field: id
          - `message` (string) **REQ** [enum=['variable not deleted', 'the id given seems to be invalid']] — Represents the error message.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
      - `InvalidRequestMethodError` — Returned when an unsupported HTTP request method is used. Includes code INVALID_REQUEST_METHOD.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['The http request method type is not a valid one']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.

- **403**: Forbidden - The client does not have access rights to the content. — Schema: `VariablesPermissionDeniedError` [application/json]
    > Returned when the caller lacks permission to access variables. Includes code NO_PERMISSION and validation details.
    schema: `VariablesPermissionDeniedError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code.
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] — The list of required permissions.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message.
    - `status` (string) **REQ** [enum=['error']] — Error status

**Scopes:** ZohoCRM.settings.variables.DELETE
