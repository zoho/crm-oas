# GET /{moduleApiName}/actions/fetch_full_data
**Operation:** `fetchFullDataForMultipleRecords` — Rich text field content for multiple records
> Retrieves the full content of rich text multi-line fields for multiple records in a single request. Both the 'ids' and 'fields' query parameters are mandatory. You can specify up to 200 record IDs in the 'ids' parameter and up to 8 rich text field API names in the 'fields' parameter. This API exclusively fetches rich text fields - other field types are not supported. Only data from rich text multi-line fields can be retrieved; multi-line fields of other types (small, large) are not supported.

**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=50]: The API name of the CRM module containing the record(s) whose rich text fields you want to retrieve (e.g., Leads, Contacts, Deals, Accounts). This is a mandatory path parameter.
- `fields` (query, string, optional) [maxLen=1000]: A comma-separated list of rich text field API names whose values you want to retrieve. Mandatory when retrieving rich text fields for multiple records (maximum 8 field API names). Optional when retrieving rich text fields for a specific record - if omitted, all rich text fields of the record are returned.
- `ids` (query, string/int64, required): Mandatory when retrieving rich text fields for multiple records. A comma-separated list of unique record IDs whose rich text field values you want to retrieve. You can specify up to 200 record IDs. Exceeding this limit results in an INVALID_REQUEST error.

**Responses:**

- **200**: Successful response containing the full HTML-formatted content of the requested rich text fields for the specified records. Each record object includes the record ID and the values of the requested rich text fields. [application/json]
    > Wrapper object for the response. Contains a 'data' array of record objects, each holding the record ID and the rich text field values.
    - `data` (array of object) [maxItems=200] **REQ** — An array of record objects, each containing the record ID and the values of the requested rich text fields. Returns up to 200 records matching the specified IDs.
      - `id` (string/int64) **REQ** — The unique identifier of the record whose rich text field data is being returned.
      additionalProperties: (string)

- **204**: No content. Returned when no record is found for the specified record ID, or when the specified fields contain no data.

- **400**: Bad Request. Returned when a required parameter is missing, the module API name is invalid, or the request exceeds parameter limits (more than 200 record IDs or more than 8 field API names). [application/json]
    > Error response for the multiple-records fetch full data operation. Includes INVALID_MODULE, REQUIRED_PARAM_MISSING, and INVALID_REQUEST error variants.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code indicating that the module API name specified in the request path is not recognized as a valid CRM module.
        - `details` (object) **REQ** — Error details with resource path index
          - `resource_path_index` (integer/int32) **REQ** — Index of the resource path that caused the error.
        - `message` (string) **REQ** [maxLen=500] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Status of the response
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code indicating that a required query parameter ('fields' or 'ids') is missing from the request.
        - `details` (object) **REQ** — Error details with parameter name
          - `param_name` (string) **REQ** [maxLen=100] — The name of the missing parameter.
        - `message` (string) **REQ** [maxLen=500] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Status of the response
        - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Error code indicating the request is invalid. Triggered when the number of record IDs exceeds 200 or the number of field API names exceeds 8.
        - `details` (object) **REQ** — Additional details about the error.
        - `message` (string) **REQ** [maxLen=500] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Status of the response

- **401**: Unauthorized. Returned when the access token is missing or invalid (AUTHENTICATION_FAILURE), or when the OAuth token does not include the required scope ZohoCRM.modules.ALL or ZohoCRM.modules.{module_name}.READ (OAUTH_SCOPE_MISMATCH). Generate a new token with the correct scope to resolve. [application/json]
    > Unauthorized error response. Contains either an AUTHENTICATION_FAILURE error when no valid access token is provided, or an OAUTH_SCOPE_MISMATCH error when the token lacks the required scope (ZohoCRM.modules.ALL or ZohoCRM.modules.{module_name}.READ).
    oneOf:
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Error code indicating that the request failed authentication because no valid access token was provided in the Authorization header.
        - `details` (object) **REQ** — Additional details about the error.
        - `message` (string) **REQ** [maxLen=500] — A message describing the authentication failure.
        - `status` (string) **REQ** [enum=['error']] — The status of the response.
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Error code indicating that the OAuth token does not include the required scope (ZohoCRM.modules.ALL or ZohoCRM.modules.{module_name}.READ) to access this endpoint.
        - `details` (object) **REQ** — Additional details about the error.
        - `message` (string) **REQ** [maxLen=500] — A message describing the OAuth scope mismatch.
        - `status` (string) **REQ** [enum=['error']] — The status of the response.

- **500**: Internal Server Error. An unexpected and unhandled exception occurred on the server. Contact the support team if this error persists. [application/json]
    > Internal server error response. Indicates an unexpected and unhandled exception on the server. Contact the Zoho CRM support team if this error persists.
    - `code` (string) **REQ** [maxLen=500] — Error code indicating the type of error.
    - `message` (string) **REQ** [maxLen=500] — Human-readable error message.
    - `details` (object) **REQ** — Additional details about the error.
    - `status` (string) **REQ** [enum=['error']] — Status of the error response.

**Scopes:** ZohoCRM.modules.READ
