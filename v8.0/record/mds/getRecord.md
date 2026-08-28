# GET /{module}/{recordId}
**Operation:** `getRecord` — Get a record by ID from a specified module
> To retrieve the details of a specific record by its unique ID from the specified module in your Zoho CRM organization. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module ID and API name. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.

**Tags:** Records

**Parameters:**
- `recordId` (path, string/int64, required): Specify the unique ID of the record. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.
- `module` (path, string, required) [maxLen=25]: Specify the API name of the module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module ID and API name.

**Responses:**

- **200**: Returns the details of the requested record from the specified module. — Schema: `RecordIDGETSuccessResponse` [application/json]
    > Represents the response schema for the record ID GET success operation.
    schema: `RecordIDGETSuccessResponse`
    - `data` (array of object `RecordGETDataItem`) [minItems=1, maxItems=1] **REQ** — Represents the data value.
      schema: `RecordGETDataItem`
      - `id` (string/int64) — Represents the unique identifier of the RecordGETDataItem record.
      - `Owner` (object) — Represents the owner value.
        - `name` (string) **REQ** [maxLen=101] — Represents the owner value.
        - `id` (string/int64) **REQ** — Represents the owner value.
        - `email` (string) [maxLen=256] — Represents the owner value.
      - `Created_Time` (string/date-time) — Represents the timestamp when the record was originally created.
      - `Modified_Time` (string/date-time) — Represents the timestamp when the record was last modified.
      - `Created_By` (object) — Contains information about the user who originally created the record.
        - `name` (string) **REQ** [maxLen=101] — Contains information about the user who originally created the record.
        - `id` (string/int64) **REQ** — Contains information about the user who originally created the record.
        - `email` (string) [maxLen=255] — Contains information about the user who originally created the record.
      - `Modified_By` (object) — Contains information about the user who last modified the record.
        - `name` (string) **REQ** [maxLen=101] — Contains information about the user who last modified the record.
        - `id` (string/int64) **REQ** — Contains information about the user who last modified the record.
        - `email` (string) [maxLen=255] — Contains information about the user who last modified the record.
      - `Wizard` (object) — Represents the wizard value.
        - `id` (string/int64) **REQ** [maxLen=19] — Represents the wizard value.
      - `$state` (string) [maxLen=255] — This will be as Save or Draft. 'save' indicates the record is not in any active Blueprint
      - `$wizard_connection_path` (string) [maxLen=2000, nullable] — $wizard_connection_path information denoted by comma separated connection ids between wizard screens.
      additionalProperties: any

- **204**: Returns an empty response when the request is successful but no record match the specified criteria.

- **400**: The request could not be processed because one or more records contain invalid data or missing required fields.
**Resolution:** Each error in the data array identifies the specific record and field that caused the failure. The request must be corrected and resubmitted. [application/json]
    > Represents the error response returned when one or more record operations fail.
    oneOf:
      - `TokenBoundDataMismatchGETError` — Represents the error response returned when the operation fails due to a token bound data mismatch GET error.
        - `code` (string) **REQ** [enum=['TOKEN_BOUND_DATA_MISMATCH']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `param_name` (string) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `InvalidModuleGETError` — Represents the error response returned when the operation fails due to a invalid module GET error.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
      - `ExpiredValueGETError` — Represents the error response returned when the operation fails due to a expired value GET error.
        - `code` (string) **REQ** [enum=['EXPIRED_VALUE']] — Represents the error code identifying the type of failure.
        - `message` (string) **REQ** — Represents the error message describing why the operation failed.
        - `details` (object) **REQ** — Contains additional context about the error.
          - `api_name` (string) **REQ** [maxLen=50] — Contains additional context about the error.
          - `json_path` (string) **REQ** — Contains additional context about the error.
        - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.

- **401**: Authentication failed because the OAuth token is missing, expired, or does not include the required scope.
**Resolution:** A new access token must be generated with the required scope for this operation. — Schema: `RecordUnauthorizedResponse` [application/json]
    > Represents the response schema for the record unauthorized operation.
    schema: `RecordUnauthorizedResponse`
    - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **403**: Permission denied to retrieve record in the specified module.
**Resolution:** The CRM administrator must grant the required retrieval permission to the user's profile. — Schema: `RecordPermissionResponse` [application/json]
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

**Scopes:** ZohoCRM.modules.READ
