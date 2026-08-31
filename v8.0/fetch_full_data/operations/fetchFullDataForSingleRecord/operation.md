# GET /{moduleApiName}/{id}/actions/fetch_full_data
**Operation:** `fetchFullDataForSingleRecord` — Rich text field content for a specific record
> Retrieves the full content of rich text multi-line fields for a specific record identified by its record ID in the path. The 'fields' query parameter is optional for this endpoint - if omitted, all rich text fields of the record are returned. When specified, only the listed rich text fields are fetched. This API exclusively fetches rich text fields - other field types are not supported. Only data from rich text multi-line fields can be retrieved; multi-line fields of other types (small, large) are not supported.

**Parameters:**
- `moduleApiName` (path, string, required) [maxLen=50]: The API name of the CRM module containing the record(s) whose rich text fields you want to retrieve (e.g., Leads, Contacts, Deals, Accounts). This is a mandatory path parameter.
- `fields` (query, string, optional) [maxLen=1000]: A comma-separated list of rich text field API names whose values you want to retrieve. Mandatory when retrieving rich text fields for multiple records (maximum 8 field API names). Optional when retrieving rich text fields for a specific record - if omitted, all rich text fields of the record are returned.
- `id` (path, string, required) [maxLen=20, minLen=1, pattern=^[0-9]+$]: The unique identifier of the record whose rich text field content you want to retrieve. Must be a valid numeric record ID. If the ID is invalid, an INVALID_DATA error (HTTP 400) is returned.

**Responses:**

- **200**: Successful response containing the full HTML-formatted content of the rich text fields for the specified record. If the 'fields' parameter was omitted, all rich text fields of the record are included. [application/json]
    > Wrapper object for the response. Contains a 'data' array with a single record object holding the record ID and its rich text field values.
    - `data` (array of object) [maxItems=1] **REQ** — An array containing a single record object with the record ID and the values of the requested rich text fields.
      - `id` (string/int64) **REQ** — The unique identifier of the record whose rich text field data is being returned.
      additionalProperties: (string)

- **204**: No content. Returned when no record is found for the specified record ID, or when the specified fields contain no data.

- **400**: Bad Request. Returned when the module API name is invalid or the request cannot be processed due to incorrect method name, parameter, or parameter values. [application/json]
    > Error response for the single-record fetch full data operation. Includes INVALID_MODULE and INVALID_REQUEST error variants.
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code indicating that the module API name specified in the request path is not recognized as a valid CRM module.
        - `details` (object) **REQ** — Error details with resource path index
          - `resource_path_index` (integer/int32) **REQ** — Index of the resource path that caused the error.
        - `message` (string) **REQ** [maxLen=500] — Human-readable error message
        - `status` (string) **REQ** [enum=['error']] — Status of the response
        - `code` (string) **REQ** [enum=['INVALID_REQUEST']] — Error code indicating the request is invalid due to incorrect method name, parameter, or parameter values.
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
