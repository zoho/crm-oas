# GET /{parentRecordModule}/{parentRecord}/{relatedList}
**Operation:** `getRelatedRecords` — Related Records
> To retrieve the list of records associated with a parent record from a specified related list in your Zoho CRM organization.

**Parameters:**
- `parentRecordModule` (path, string, required) [maxLen=100, pattern=^[A-Za-z_][A-Za-z0-9_]*$]: Specify the API name of the module the parent record belongs to. Refer to the [Get Modules](https://www.zoho.com/crm/developer/docs/api/v8/modules-api.html) resource for valid values.
- `parentRecord` (path, string, required) [maxLen=20, pattern=^[0-9]+$]: Specify the unique numeric identifier of the parent record.
- `relatedList` (path, string, required) [maxLen=100, pattern=^[A-Za-z_][A-Za-z0-9_]*$]: Specify the API name of the related list containing the records to retrieve or modify. Refer to the [Get Related Lists](https://www.zoho.com/crm/developer/docs/api/v8/related-list-meta.html) resource for valid values.
- `fields` (query, string, required) [maxLen=1000, pattern=^[A-Za-z_][A-Za-z0-9_]*(,[A-Za-z_][A-Za-z0-9_]*)*$]: Specify the API names of the fields to include in the response as a comma-separated list.
- `page` (query, integer/int32, optional) [min=1, max=10000, default=1]: Specify the page number for paginating results.
- `perPage` (query, integer/int32, optional) [min=1, max=200, default=200]: Specify the number of records to return per page.

The page and per_page parameter is used to fetch records according to their position in the CRM. Let us assume that the user has to fetch 400 records. The maximum number of records that one can get for an API call is 200. So, for records above the 200th position, they cannot be fetched. By using the page (1 and 2) and per_page (200) parameter, the user can fetch all 400 records using 2 API calls.
If the requested related list is not present or hidden in a layout, the system will return an INVALID_DATA response.
- `If-Modified-Since` (header, string/date-time, optional): Specify the date and time in RFC 2822 format. The response includes only records modified after this timestamp.
- `page_token` (query, string, optional) [maxLen=500]: Specify the token to retrieve the next set of records beyond the first 2,000 results. Use the **next_page_token** value from the previous response.
- `ids` (query, string, optional) [maxLen=2000, pattern=^[0-9]+(,[0-9]+)*$]: Specify the unique identifiers of the records to retrieve as a comma-separated list.
- `sort_order` (query, string, optional) [enum=['asc', 'desc'], default=desc]: Specify the sort direction for the related records. Possible values: **asc**, **desc**.
- `sort_by` (query, string, optional) [enum=['id', 'Created_Time', 'Modified_Time'], default=id]: Specify the field to sort the related records by. Possible values: **ID**, **Created_Time**, **Modified_Time**.
- `converted` (query, string, optional) [enum=['true', 'false', 'both'], default=false]: Specify whether to filter records by conversion status. Possible values: **true**, **false**, **both**.
- `approved` (query, string, optional) [enum=['true', 'false', 'both'], default=true]: Filter records by approval status. When set to true, returns only approved records; when false, returns only unapproved records.
- `approval_state` (query, string, optional) [enum=[16 values]]: Filter records by their current approval state.
- `filters` (query, object, optional): Filter for fetching specific related records based on criteria

**Responses:**

- **200**: Returns the list of related records for the specified parent record, along with pagination metadata. [application/json]
    > Represents the response for a list of related records, including the record fields and pagination metadata.
    - `data` (array of object) [maxItems=200] **REQ** — Array of related record objects with requested fields.
      - `id` (string) [maxLen=20, pattern=^[0-9]+$] — Unique identifier of the related record.
      - `Created_Time` (string/date-time) — Represents the creation date and time of the related record.
      - `Modified_Time` (string/date-time) — Timestamp when the record was last modified.
      - `Moved_To__s` (string) [maxLen=255] — Stage value to which the record was moved (stage history / picklist movement).
      additionalProperties: any
    - `info` (object) **REQ** — Pagination and response metadata.
      - `page` (integer/int32) **REQ** [min=1] — Current page number.
      - `per_page` (integer/int32) **REQ** [min=1, max=200] — Number of records per page.
      - `count` (integer/int32) **REQ** [min=0] — Number of records in current response.
      - `more_records` (boolean) **REQ** — Indicates if more pages are available.
      - `next_page_token` (string) [maxLen=500, nullable] — Token to retrieve the next page of results.
      - `page_token_expiry` (string/date-time) [nullable] — Expiration timestamp for the page token.
      - `previous_page_token` (string) [maxLen=500, nullable] — Token to retrieve the previous page of results.

- **204**: No related records were found for the specified parent record in the given related list.

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

- **404**: The specified parent record or related list does not exist.
**Resolution:** The **parentRecord** and **relatedList** path parameter values must refer to existing resources. [application/json]
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
