# GET /{module}/deleted
**Operation:** `getDeletedRecords` — Get deleted records from a specified module
> To retrieve the list of deleted records from the specified module in your Zoho CRM organization, including records in the recycle bin and permanently deleted records. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module ID and API name.

**Tags:** Deleted Records

**Parameters:**
- `module` (path, string, required) [maxLen=25]: Specify the API name of the module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module ID and API name.
- `type` (query, string, optional) [maxLen=20, enum=['all', 'recycle', 'permanent'], default=all]: Specify the category of deleted records to retrieve.  Possible values:  **all** - Returns both recycled and permanently deleted records.  **recycle** - Returns only records in the Recycle Bin.  **permanent** - Returns only permanently deleted records.
- `page` (query, integer/int32, optional) [min=1]: Specify the page number to retrieve. Starts at 1.
- `per_page` (query, integer/int32, optional) [min=1, max=200]: Specify the number of records to return per page. Maximum is 200.
- `If-Modified-Since` (header, string/date-time, optional) [maxLen=100]: Use this header to get the list of records modified after the specified timestamp. The timestamp must be in ISO 8601 format.

**Responses:**

- **200**: Returns the deletion status for each records successfully deleted. — Schema: `DeletedRecordsSuccessResponse` [application/json]
    > Represents the response schema for the deleted records success operation.
    schema: `DeletedRecordsSuccessResponse`
    - `data` (array of object) [minItems=1, maxItems=200] **REQ** — Represents the data value.
      - `id` (string/int64) **REQ** — Represents the data value.
      - `display_name` (string) **REQ** [maxLen=255, nullable] — Represents the data value.
      - `type` (string) **REQ** [enum=['recycle', 'permanent']] — Represents the data value.
      - `deleted_time` (string/date-time) **REQ** — Represents the data value.
      - `deleted_by` (object) **REQ** — Represents the data value.
        - `name` (string) **REQ** [maxLen=255] — Represents the data value.
        - `id` (string/int64) **REQ** — Represents the data value.
      - `created_by` (object) **REQ** — Represents the data value.
        - `name` (string) **REQ** [maxLen=101] — Represents the data value.
        - `id` (string/int64) **REQ** — Represents the data value.
    - `info` (object) **REQ** — Represents the info value.
      - `per_page` (integer/int32) **REQ** — Represents the info value.
      - `count` (integer/int32) **REQ** — Represents the info value.
      - `page` (integer/int32) **REQ** — Represents the info value.
      - `more_records` (boolean) **REQ** — Represents the info value.

- **204**: Returns an empty response when the request is successful but no records match the specified criteria.

- **400**: The request could not be processed because of an invalid module, missing parameters, or invalid record IDs.
**Resolution:** The request must include valid module API name and record IDs. — Schema: `DeletedRecordsErrorResponse` [application/json]
    > Represents the error response returned when the operation fails due to a deleted records response error.
    schema: `DeletedRecordsErrorResponse`
    - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the data value.
      oneOf:
        - `InvalidModuleGetDeletedError` — Represents the error response returned when the operation fails due to a invalid module error.
          - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code identifying the type of failure.
          - `message` (string) **REQ** — Represents the error message describing why the operation failed.
          - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
          - `details` (object) **REQ** — Contains additional context about the error.
            - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
        - `PatternNotMatchedGetDeletedError` — Represents the error response returned when the operation fails due to a pattern not matched error.
          - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Error code indicating pattern not matched.
          - `message` (string) **REQ** — Human-readable explanation of the error.
          - `status` (string) **REQ** [enum=['error']] — Indicates the request resulted in an error.
          - `details` (object) **REQ** — Additional contextual information about the error.
            - `param_name` (string) **REQ** [maxLen=255] — Name of the query parameter that failed pattern matching.

- **401**: Authentication failed because the OAuth token is missing, expired, or does not include the required scope.
**Resolution:** A new access token must be generated with the required scope for this operation. — Schema: `RecordUnauthorizedResponse` [application/json]
    > Represents the response schema for the record unauthorized operation.
    schema: `RecordUnauthorizedResponse`
    - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **403**: Permission denied to delete records in the specified module.
**Resolution:** The CRM administrator must grant the required deletion permission to the user's profile. — Schema: `RecordPermissionResponse` [application/json]
    > Represents the response schema for the record permission operation.
    schema: `RecordPermissionResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.
      - `permissions` (array of string) [minItems=1, maxItems=100] **REQ** — Contains additional context about the error.
        items: [maxLen=255]

- **500**: An unexpected server error occurred while processing the request.
**Resolution:** The request can be retried after some time. If the error persists, Zoho CRM support must be contacted. — Schema: `RecordInternalErrorResponse` [application/json]
    > Represents the error response returned when the operation fails due to a record internal response error.
    schema: `RecordInternalErrorResponse`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

**Scopes:** ZohoCRM.modules.READ
