# PUT /settings/custom_views/{id}/actions/change_sort
**Operation:** `changeSortById` — Sort Order by ID
> To change the sort field and sort order for a specific Custom View in the specified module of your Zoho CRM organization. Use the [Get Custom Views Metadata API](custom_views.yaml#$.paths./settings/custom_views.get) to retrieve the custom view IDs."

**Tags:** Custom Views

**Parameters:**
- `module` (query, string, required) [maxLen=25]: Specify the API name of the module for which to manage Custom Views. Refer to the Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module IDs.resource for valid values.
- `id` (path, string/int64, required) [maxLen=25]: Specify the unique ID of the Custom View. Use the [Get Custom View API](custom_views.yaml#$.paths./settings/custom_views.get) to retrieve the custom view IDs.

**Schemas:**
`SimpleFieldError`:
  > Represents the error details for an invalid or missing field, including the API name and JSON path.
  - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the field that caused the error.
  - `json_path` (string) **REQ** [maxLen=255] — Represents the JSON path pointing to the invalid field in the request.

**Request Body** (required) — application/json
> The request body must contain a custom_views array with one object specifying the new sort order for the Custom View.
  > Represents the request body for changing the sort order of a specific Custom View.
  - `custom_views` (array of object) [maxItems=1] **REQ** — Specify the sort order configuration to apply to the Custom View.
    - `sort_by` (object `FieldReference`) **REQ** — Represents a reference to a field in the Custom View, identified by its API name and unique ID.
      schema: `FieldReference`
      - `api_name` (string) [maxLen=255, nullable] — Represents the API name of the field. A null value indicates no field is selected.
      - `id` (string/int64) [maxLen=25, nullable] — Represents the unique ID of the field. A null value indicates no field is selected.
    - `sort_order` (string) **REQ** [enum=['asc', 'desc']] — Specify the sort order for the Custom View.
Possible values:
**asc** - Ascending order.
**desc** - Descending order.

**Responses:**

- **200**: Returns a success response indicating that the sort order update completed for the specified Custom View. — Schema: `CustomViewUpdateSuccessResponse` [application/json]
    > Represents the bulk update success response containing a list of updated Custom View items.
    schema: `CustomViewUpdateSuccessResponse`
    - `custom_views` (array of object `CustomViewUpdateSuccess`) [maxItems=200] **REQ** — Represents the list of Custom View update success items.
      schema: `CustomViewUpdateSuccess`
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the update response.
Possible values:
**success** - The operation was successful.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the success code for the update operation.
Possible values:
**SUCCESS** - The Custom View update completed successfully.
      - `message` (string) **REQ** [maxLen=255] — Represents the success message for the update operation.
      - `details` (object) **REQ** — Represents the additional details for the successful update operation.
        - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique ID of the updated Custom View.

- **400**: The sort field or sort order value in the request is invalid. Resolution: The sort order must be either **asc** or **desc**. [application/json]
    > Represents the error response for an invalid sort by ID request.
    oneOf:
      - `UrlErrorResponseForCustomView` — Flat error: URL/module validation failures
        oneOf:
          - `UnableToParseDataTypeError` — Data type could not be parsed from the request
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
            - `code` (string) **REQ** [enum=['UNABLE_TO_PARSE_DATA_TYPE']] — Represents the error code for the data type parse failure.
Possible values:
**UNABLE_TO_PARSE_DATA_TYPE** - The server could not parse the data type from the request.
            - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the data type parse failure.
            - `details` (object) **REQ** — Represents the additional details about the data type parse failure.
          - `InvalidUrlPatternError` — Request URL does not match any known pattern
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
            - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code for the invalid URL pattern.
Possible values:
**INVALID_URL_PATTERN** - The request URL does not match any known pattern.
            - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the URL pattern issue.
            - `details` (object) **REQ** — Represents the additional details about the URL pattern error.
          - `InvalidModuleError` — The specified module is invalid or does not exist
            - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
            - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for the invalid module error.
Possible values:
**INVALID_MODULE** - The specified module does not exist or is invalid.
            - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid module.
            - `details` (object) **REQ** — Represents the additional details about the invalid module error.
              - `param_name` (string) [maxLen=255] — Name of the invalid parameter
      - `RequiredParameterMissingResponse` — Flat error: required query parameter missing
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for the missing required parameter.
Possible values:
**REQUIRED_PARAM_MISSING** - A required query parameter is absent from the request.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing parameter.
        - `details` (object) **REQ** — Represents the details of the missing parameter.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the name of the missing required parameter.
      - `CustomViewSortByIdFailureDetails` — Wrapped error: per-item sort-by-ID failures inside custom_views array
        - `custom_views` (array of object `CustomViewSortByIdFailureItem`) [maxItems=200] **REQ** — Represents the list of Custom View sort failure items for the sort by ID operation.
          oneOf:
            - `InvalidDataSortById` — Represents the error details returned when the sort field or sort order value in the sort by ID request is invalid.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
              - `details` (object `SimpleFieldError`) **REQ** — Represents the error details for an invalid or missing field, including the API name and JSON path.
              - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid sort data.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid data error.
Possible values:
**INVALID_DATA** - The sort field or sort order value in the request is invalid.
            - `MandatoryNotFoundForSort` — Represents the error details returned when a required field is missing from a sort request.
              - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
              - `details` (object) **REQ** — Represents the additional details about the missing required field.
              - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the missing required field.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — Represents the error code for the missing required field.
Possible values:
**MANDATORY_NOT_FOUND** - A required field is missing from the sort request.
      - `ResourcePathIndexErrorResponse` — Flat error: invalid resource path segment
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid resource path.
Possible values:
**INVALID_DATA** - A segment in the resource path is invalid.
        - `details` (object `ResourcePathIndexError`) **REQ** — Represents the error details indicating which segment of the resource path or URL is invalid.
          schema: `ResourcePathIndexError`
          - `resource_path_index` (integer/int32) **REQ** — Represents the index of the invalid segment in the resource path.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid resource path segment.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.

- **401**: Authentication failed or the OAuth access token does not include the required scope. Resolution: A new access token must be generated with the ZohoCRM.settings.custom_views.UPDATE scope. [application/json]
    > Represents the error response for an unauthorized sort by ID request.
    oneOf:
      - `AuthenticationError` — Represents the error response returned when the authentication ticket is invalid or missing.
        - `code` (string) **REQ** [enum=['AUTHENTICATION_FAILURE']] — Represents the error code for the authentication failure.
Possible values:
**AUTHENTICATION_FAILURE** - The authentication ticket is invalid or missing.
        - `details` (object) **REQ** — Represents the error details containing validation information about the authentication failure.
        - `message` (string) **REQ** [enum=['Authentication failed']] — Represents the error message for the authentication failure.
Possible values:
**Authentication failed** - The provided authentication credentials are invalid or missing.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an authentication error.
      - `UnauthorizedResponse` — Represents the error response returned when the request is unauthorized due to an OAuth scope mismatch.
        - `code` (string) **REQ** [enum=['OAUTH_SCOPE_MISMATCH']] — Represents the error code for the OAuth scope mismatch.
Possible values:
**OAUTH_SCOPE_MISMATCH** - The access token does not include the required scope for this operation.
        - `message` (string) **REQ** [maxLen=1024] — Represents the error message indicating the request is unauthorized due to an OAuth scope mismatch.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an authorization error.
        - `details` (object) **REQ** [maxProperties=0] — Represents the additional details for this error. An empty object indicates no additional details are available.

- **403**: Permission denied to change the sort order of the specified Custom View. Resolution: The CRM administrator must grant the required permission to the user's profile. — Schema: `ModuleForbiddenErrorResponse` [application/json]
    > Represents the error response returned when the user does not have the required permissions for the specified module.
    schema: `ModuleForbiddenErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the permission error.
Possible values:
**NO_PERMISSION** - The user does not have the required permission for this module.
    - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the permission denial.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered a permission error.
    - `details` (object) **REQ** — Represents the additional details about the permission error, including the required permissions.
      - `permissions` (array of string) [maxItems=50] **REQ** — Represents the list of permissions required to perform the action on this module.
        items: [maxLen=255]

**Scopes:** ZohoCRM.settings.custom_views.UPDATE
