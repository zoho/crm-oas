# POST /settings/variables/actions/generate_api_name
**Operation:** `postGenerateApiName` — Generate API Name
> generates api name

**Request Body** — application/json `ApiNameGenerationRequestBody`
> The request body containing the variable definitions to create.
  > Alternate request payload wrapper containing items used to generate API names.
  - `variables` (array of object `ApiNameGenerationRequestBodyItem`) [maxItems=1] **REQ** — Array of variable definitions. Mandatory.
    schema: `ApiNameGenerationRequestBodyItem`
    - `name` (string) **REQ** [maxLen=50] — The display name for the variable. Mandatory.
    - `variable_group` (object `VariableGroupSchema`) **REQ** — The variable group to which this variable belongs. Mandatory.
      schema: `VariableGroupSchema`
      - `api_name` (string) [maxLen=100] — The API name of the variable group.
      - `name` (string) [maxLen=50] — The display name of the variable group.
      - `id` (string) [maxLen=19] — The unique ID of the variable group.
      additionalProperties: any

**Responses:**

- **200**: OK - Successful response — Schema: `ApiNameGenerationResponse` [application/json]
    > 200 response providing generated API names for the submitted variables.
    schema: `ApiNameGenerationResponse`
    - `variables` (array of object `VariableActionResult`) [maxItems=1] — Array of results for the API name generation operation.
      schema: `VariableActionResult`
      - `code` (string) [maxLen=255] — The result code of the operation (for example, SUCCESS).
      - `details` (object `VariableOperationDetail`) — Minimal details about a variable operation, including the server-assigned variable identifier.
        schema: `VariableOperationDetail`
        - `id` (string/int64) — The unique ID of the variable.
        - `api_name` (string) [maxLen=255] — The API name of the variable.
      - `message` (string) [maxLen=255] — A human-readable message describing the result of the operation.
      - `status` (string) [maxLen=255] — The status of the operation (for example, success or error).

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    > Wrapped error response with variables
    - `variables` (array of object) [maxItems=25] **REQ** — Array of error objects
      oneOf:
        - `ErrorApiNameGenerationMandatoryMissingResponse` — 400 error returned when required fields for API name generation are not provided.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code.
          - `details` (object) **REQ** — Error details with validation information
            - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=['required field not found']] — Represents the error message.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
        - `ErrorMandatoryFieldMissingResponse` — 400 error indicating a required field was not provided in the request.
          - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code.
          - `details` (object) **REQ** — Error details with validation information
            - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=['Required field is missing']] — Represents the error message.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
        - `ErrorInvalidDataTypeResponse` — 400 error indicating a field has an incorrect data type.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
          - `details` (object) **REQ** — Error details with validation information
            - `expected_data_type` (string) **REQ** [maxLen=255] — The expected data type for the field.
            - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=['Invalid data type']] — Represents the error message.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
        - `ErrorInvalidDataResponse` — 400 error for general invalid data submitted in the request.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
          - `details` (object) **REQ** — Error details with validation information
            - `maximum_length` (integer/int32) **REQ** — The maximum allowed length for the field.
            - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the error.
            - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
          - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message.
          - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.

**Scopes:** ZohoCRM.settings.variables.CREATE
