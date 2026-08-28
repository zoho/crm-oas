# GET /{parentRecordModule}/{parentRecord}/{relatedList}/{record}
**Operation:** `getRelatedRecord` — Get a related record
> To retrieve the details of a specific related record from a specified related list of a parent record in your Zoho CRM organization.

**Parameters:**
- `parentRecordModule` (path, string, required) [maxLen=100, pattern=^[A-Za-z_][A-Za-z0-9_]*$]: Specify the API name of the module the parent record belongs to. Refer to the [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) resource for valid values.
- `parentRecord` (path, string, required) [maxLen=20, pattern=^[0-9]+$]: Specify the unique numeric identifier of the parent record.
- `relatedList` (path, string, required) [maxLen=100, pattern=^[A-Za-z_][A-Za-z0-9_]*$]: Specify the API name of the related list containing the records to retrieve or modify. Refer to the [Get Related Lists](https://www.zoho.com/crm/developer/docs/api/v8/related-list-meta.html) resource for valid values.
- `record` (path, string, required) [maxLen=20, pattern=^[0-9]+$]: Specify the unique numeric identifier of the specific related record.
- `fields` (query, string, required) [maxLen=1000, pattern=^[A-Za-z_][A-Za-z0-9_]*(,[A-Za-z_][A-Za-z0-9_]*)*$]: Specify the API names of the fields to include in the response as a comma-separated list.

**Responses:**

- **200**: Returns the details of the specified related record. [application/json]
    > Represents the response for a single related record, including the record fields and metadata.
    - `data` (array of object) [maxItems=1] **REQ** — Array containing the single related record.
      - `id` (string) [maxLen=20, pattern=^[0-9]+$] — Unique identifier of the related record.
      - `Created_Time` (string/date-time) — Represents the creation date and time of the related record.
      - `Modified_Time` (string/date-time) — Timestamp when the record was last modified.
      - `Moved_To__s` (string) [maxLen=255] — Stage value to which the record was moved (stage history / picklist movement).
      additionalProperties: any

- **204**: The specified related record was not found for the given parent record.

- **400**: The request contains invalid input, an unsupported module, or an invalid request method.
**Resolution:** Review the error code and message in the response to identify the specific issue. [application/json]
    > Contains one of the possible client error responses for invalid module name, unsupported module, invalid data, invalid request method, or authorization failure. May also indicate a missing required parameter.
    oneOf:
      - `InvalidModuleError` — Represents an error response returned when the module name in the request is not a valid Zoho CRM module API name.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code indicating the type of error.
        - `message` (string) **REQ** [maxLen=500] — Detailed error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error.
        - `details` (object) — Additional error details.
          - `resource_path_index` (integer/int32) — Index of the path parameter that caused the error (0-based).
          additionalProperties: any
      - `NotSupportedError` — Represents an error response returned when the specified module is not supported by this API.
        - `code` (string) **REQ** [enum=['NOT_SUPPORTED']] — Error code indicating the type of error.
        - `message` (string) **REQ** [maxLen=500] — Detailed error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error.
        - `details` (object) — Additional error details.
          - `resource_path_index` (integer/int32) — Index of the path parameter that caused the error (0-based).
          additionalProperties: any
      - `InvalidDataError` — Represents an error response returned when the request contains invalid data, such as an invalid record ID, invalid related list name, or invalid input format.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code.
        - `message` (string) **REQ** [maxLen=500] — Error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error.
        - `details` (object) **REQ** — Additional error details. Can be empty depending on the error.
          - `id` (string) [maxLen=20, pattern=^[0-9]+$] — Record/related record ID involved in the error (if applicable).
          - `api_name` (string) [maxLen=100] — API name of the field/module/related list involved (if applicable).
          - `resource_path_index` (integer/int32) — Index/position in the request resource path or payload where the error occurred (if applicable).
          additionalProperties: any
      - `InvalidRequestMethodError` — Represents an error response returned when the HTTP request method is not valid for this endpoint.
        - `code` (string) **REQ** [enum=['INVALID_REQUEST_METHOD']] — Error code.
        - `message` (string) **REQ** [maxLen=500] — Error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error.
        - `details` (object) — Additional error details.
      - `AuthorizationFailedError` — Represents an error response returned when the access token does not have sufficient privileges for the requested operation.
        - `code` (string) **REQ** [enum=['AUTHORIZATION_FAILED']] — Error code.
        - `message` (string) **REQ** [maxLen=500] — Error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error.
        - `details` (object) — Additional error details.
      - `RequiredParamMissingError` — Represents an error response returned when a required request parameter is missing.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code.
        - `message` (string) **REQ** [maxLen=500] — Error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error.
        - `details` (object) — Additional error details.
          - `param_name` (string) [maxLen=100] — Name of the missing required parameter.
          additionalProperties: any

- **401**: Authentication failed due to an invalid or expired token.
**Resolution:** A valid access token must be provided in the Authorization header. [application/json]
    > Contains one of the possible unauthorized access error responses for invalid token or OAuth scope mismatch.
    oneOf:
      - `InvalidTokenError` — Represents an error response returned when the access token in the request is invalid or expired.
        - `code` (string) **REQ** [enum=['INVALID_TOKEN']] — Error code.
        - `message` (string) **REQ** [maxLen=500] — Error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error.
        - `details` (object) — Additional error details.
      - `OAuthScopeMismatchError` — Represents an error response returned when the access token does not include the required OAuth scope for the requested operation.
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Error code.
        - `message` (string) **REQ** [maxLen=500] — Error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error.
        - `details` (object) — Additional error details.

- **403**: The access token does not have permission to read related records in this module.
**Resolution:** The CRM administrator must grant the required read permission to the user's profile. — Schema: `NoPermissionError` [application/json]
    > Represents an error response returned when the authenticated user does not have the required module-level permission for the requested operation.
    schema: `NoPermissionError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code.
    - `message` (string) **REQ** [maxLen=500] — Error message.
    - `status` (string) **REQ** [enum=['error']] — Status of the error.
    - `details` (object) — Additional error details.
      - `permissions` (array of string) [maxItems=100] — Missing/required permissions for the requested operation.
        items: [maxLen=200]
      additionalProperties: any

- **404**: The specified related record does not exist.
**Resolution:** The **parentRecord**, **relatedList**, and **record** path parameter values must refer to existing resources. [application/json]
    > Contains one of the possible not-found error responses for record not found or invalid URL pattern.
    oneOf:
      - `RecordNotFoundError` — Represents an error response returned when the specified record does not exist or cannot be found.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code.
        - `message` (string) **REQ** [maxLen=500] — Error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error.
        - `details` (object) — Additional error details.
      - `InvalidUrlPatternError` — Represents an error response returned when the request URL does not match a valid API endpoint pattern.
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Error code.
        - `message` (string) **REQ** [maxLen=500] — Error message.
        - `status` (string) **REQ** [enum=['error']] — Status of the error.
        - `details` (object) — Additional error details.

- **500**: An internal server error occurred.
**Resolution:** Retry the request after a brief delay. If the issue persists, contact Zoho CRM support. — Schema: `InternalError` [application/json]
    > Represents an error response returned when an unexpected internal server error occurs.
    schema: `InternalError`
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Error code.
    - `message` (string) **REQ** [maxLen=500] — Error message.
    - `status` (string) **REQ** [enum=['error']] — Status of the error.
    - `details` (object) — Additional error details.

**Scopes:** ZohoCRM.modules.READ
