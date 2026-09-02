# DELETE /{module}
**Operation:** `deleteRecords` — Delete records from a specified module
> To permanently delete more records from the specified module in your Zoho CRM organization, use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs. A maximum of 100 records can be deleted per API call. By default, all workflows related to this API are executed. All subforms related to the deleted records are also deleted.

**Tags:** Records

**Parameters:**
- `module` (path, string, required) [maxLen=25]: Specify the API name of the module. Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve the module ID and API name.
- `ids` (query, array, optional) [minItems=1, uniqueItems] {style=form, explode=False}: Specify a comma-separated list of record IDs. Use the [Get Records API](record.yaml#$.paths./module.get) to retrieve the record IDs.

**Responses:**

- **200**: Returns the deletion status for each records successfully deleted. — Schema: `RecordDeleteSuccessResponse` [application/json]
    > Represents the response schema for the record delete success operation.
    schema: `RecordDeleteSuccessResponse`
    - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the data value.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the data value.
      - `details` (object) **REQ** — Represents the data value.
        - `id` (string/int64) **REQ** — Represents the data value.
      - `message` (string) **REQ** [enum=['record deleted']] — Represents the data value.
      - `status` (string) **REQ** [enum=['success']] — Represents the data value.

- **207**: Returns a multi-status response when some record deletion operations succeed and others fail. Each item in the data array independently reports the outcome for the corresponding record. — Schema: `RecordDeleteMultiStatusResponse` [application/json]
    > Represents the response schema for the record delete multi status operation.
    schema: `RecordDeleteMultiStatusResponse`
    - `data` (array of object) [minItems=2, maxItems=100] **REQ** — Represents the data value.
      oneOf:
          - `status` (string) **REQ** [enum=['success']] — Represents the data value.
          - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the data value.
          - `message` (string) **REQ** — Represents the data value.
          - `details` (object) **REQ** — Represents the data value.
            - `id` (string/int64) **REQ** — Represents the data value.
        - `RecordDeleteInvalidDataItem` — Represents a single record delete invalid data result item.
          - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of failure.
          - `message` (string) **REQ** — Represents the error message describing why the operation failed.
          - `details` (object) **REQ** — Contains additional context about the error.
            - `id` (string/int64) **REQ** [maxLen=20] — Contains additional context about the error.
        - `RecordDeleteRequiredParamMissingItem` — Represents a single record delete required parameter missing result item.
          - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
          - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code identifying the type of failure.
          - `message` (string) **REQ** — Represents the error message describing why the operation failed.
          - `details` (object) **REQ** — Contains additional context about the error.
            - `param_name` (string) **REQ** [maxLen=255] — Contains additional context about the error.

- **400**: The request could not be processed because of an invalid module, missing parameters, or invalid record IDs.
**Resolution:** The request must include valid module API name and record IDs. — Schema: `RecordDeleteBadRequestResponse` [application/json]
    > Represents the response schema for the record delete bad request operation.
    oneOf:
      - `RecordDeleteFlatError` — Represents the error response returned when the operation fails due to a record delete flat error.
        oneOf:
          - `RecordDeleteRequiredParamMissingError` — Represents the error response returned when the operation fails due to a record delete required parameter missing error.
            - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code identifying the type of failure.
            - `message` (string) **REQ** — Represents the error message describing why the operation failed.
            - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `details` (object `RecordDeleteRequiredParamDetails`) **REQ** — Contains the contextual details for the record delete required parameter error.
              schema: `RecordDeleteRequiredParamDetails`
              - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the parameter that caused the error.
          - `InvalidModuleError` — Represents the error response returned when the operation fails due to a invalid module error.
            - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code identifying the type of failure.
            - `message` (string) **REQ** — Represents the error message describing why the operation failed.
            - `details` (object) **REQ** — Contains additional context about the error.
              - `resource_path_index` (integer/int32) **REQ** — Contains additional context about the error.
            - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
          - `RecordDeleteInvalidRequestMethodError` — Represents the error response returned when the operation fails due to a record delete invalid request method error.
            - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Represents the error code identifying the type of failure.
            - `message` (string) **REQ** — Represents the error message describing why the operation failed.
            - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `details` (object) **REQ** [maxProperties=0] — Contains the contextual details for the record delete empty error.
          - `RecordDeleteAuthorizationFailedError` — Represents the error response returned when the operation fails due to a record delete authorization failed error.
            - `code` (string) **REQ** [enum=['AUTHORIZATION_FAILED']] — Represents the error code identifying the type of failure.
            - `message` (string) **REQ** — Represents the error message describing why the operation failed.
            - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `details` (object) **REQ** [maxProperties=0] — Contains the contextual details for the record delete empty error.
          - `RecordDeleteUnableToParseDataTypeError` — Error returned when the DELETE request contains data that cannot be parsed.
            - `code` (string) **REQ** [enum=['UNABLE_TO_PARSE_DATA_TYPE']] — Error code indicating unable to parse data type.
            - `message` (string) **REQ** — Represents the error message describing why the operation failed.
            - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
            - `details` (object) **REQ** [maxProperties=0] — Contains the contextual details for the record delete empty error.
      - `RecordDeleteLockedError` — Represents the error response returned when the operation fails due to a record delete locked error.
        - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the data value.
          - `code` (string) **REQ** [enum=['RECORD_LOCKED']] — Represents the data value.
          - `message` (string) **REQ** — Represents the data value.
          - `status` (string) **REQ** [enum=['error']] — Represents the data value.
          - `details` (object) **REQ** — Represents the data value.
            - `action` (string) **REQ** [maxLen=100] — Represents the data value.
            - `id` (string/int64) **REQ** — Represents the data value.
      - `RecordDeleteNotApprovedError` — Represents the error response returned when the operation fails due to a record delete not approved error.
        - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the data value.
          - `code` (string) **REQ** [enum=['NOT_APPROVED']] — Represents the data value.
          - `message` (string) **REQ** — Represents the data value.
          - `status` (string) **REQ** [enum=['error']] — Represents the data value.
          - `details` (object) **REQ** [maxProperties=0] — Represents the data value.
      - `RecordDeleteInvalidDataError` — Represents the error response returned when the operation fails due to a record delete invalid data error.
        - `data` (array of object) [minItems=1, maxItems=100] **REQ** — Represents the data value.
          - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the data value.
          - `message` (string) **REQ** — Represents the data value.
          - `status` (string) **REQ** [enum=['error']] — Represents the data value.
          - `details` (object) **REQ** — Represents the data value.
            - `id` (string/int64) **REQ** — Represents the data value.

- **401**: Authentication failed because the OAuth token is missing, expired, or does not include the required scope.
**Resolution:** A new access token must be generated with the required scope for this operation. — Schema: `RecordDeleteUnauthorizedResponse` [application/json]
    > Represents the response schema for the record delete unauthorized operation.
    schema: `RecordDeleteUnauthorizedResponse`
    - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **403**: Permission denied to delete records in the specified module.
**Resolution:** The CRM administrator must grant the required deletion permission to the user's profile. — Schema: `RecordDeletePermissionResponse` [application/json]
    > Represents the response schema for the record delete permission operation.
    schema: `RecordDeletePermissionResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.
      - `permissions` (array of string) [minItems=1, maxItems=100] **REQ** — Contains additional context about the error.
        items: [maxLen=255]

- **404**: The request URL does not match any valid API endpoint pattern.
**Resolution:** The API endpoint URL must be verified for correct format and path parameters. — Schema: `RecordDeleteInvalidURLResponse` [application/json]
    > Represents the response schema for the record delete invalid URL operation.
    schema: `RecordDeleteInvalidURLResponse`
    - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

- **500**: An unexpected server error occurred while processing the request.
**Resolution:** The request can be retried after some time. If the error persists, Zoho CRM support must be contacted. — Schema: `RecordDeleteInternalErrorResponse` [application/json]
    > Represents the error response returned when the operation fails due to a record delete internal response error.
    schema: `RecordDeleteInternalErrorResponse`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Represents the error code identifying the type of failure.
    - `message` (string) **REQ** — Represents the error message describing why the operation failed.
    - `status` (string) **REQ** [enum=['error']] — Indicates the overall result status of the request.
    - `details` (object) **REQ** — Contains additional context about the error.

**Scopes:** ZohoCRM.modules.DELETE
