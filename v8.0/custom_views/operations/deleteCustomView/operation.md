# DELETE /settings/custom_views
**Operation:** `deleteCustomView` — Delete Custom Views
> To delete one or more Custom Views from a specified module in your Zoho CRM organization.

**Tags:** Custom Views

**Parameters:**
- `ids` (query, array, required) [minItems=1, maxItems=100, uniqueItems] {style=form, explode=False}: Specify the comma-separated list of unique IDs of the Custom Views to delete. Accepts up to 100 IDs. Use the [Get Custom Views API](custom_views.yaml#$.paths./settings/custom_views.get) to retrieve the custom view IDs.
- `module` (query, string, required) [maxLen=25]: Specify the API name of the module for which to manage Custom Views. Refer to the Use the [Get Modules API](modules.yaml#$.paths./settings/modules.get) to retrieve module IDs.resource for valid values.

**Schemas:**
`CustomViewDeleteFailure`:
  oneOf:
    - `InvalidDataDelete` — Represents the error details returned when the Custom View ID provided for deletion is invalid or the view has already been deleted.
    - `NotAllowedDetailsDelete` — Represents the error details returned when a Custom View cannot be deleted due to active associations.
`CustomViewDeleteSuccess`:
  > Represents the successful deletion response for a Custom View, including the status, code, and confirmation message.
  - `status` (string) **REQ** [enum=['success']] — Represents the status of the deletion response.
Possible values:
**success** - The operation was successful.
  - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the success code for the deletion operation.
Possible values:
**SUCCESS** - The Custom View deletion completed successfully.
  - `details` (object `IdDetail`) **REQ** — Represents the ID details for a created or affected resource.
  - `message` (string) **REQ** [maxLen=255] — Represents the success message for the deletion operation.
`IdDetail`:
  > Represents the ID details for a created or affected resource.
  - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique ID of the created or affected resource.
`InvalidDataDelete`:
  > Represents the error details returned when the Custom View ID provided for deletion is invalid or the view has already been deleted.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
  - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the invalid data issue.
  - `details` (object) **REQ** — Represents the additional details about the invalid Custom View ID.
    - `id` (string/int64) **REQ** [maxLen=25] — Represents the ID of the invalid or already-deleted Custom View.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the invalid data error.
Possible values:
**INVALID_DATA** - The Custom View ID in the request is invalid or already deleted.
`NotAllowedDetails`:
  > Represents the details of associations that prevent the deletion of a Custom View, including the association type and the list of associated resources.
  - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique ID of the Custom View that cannot be deleted.
  - `associations` (array of object) [maxItems=50] **REQ** — Represents the list of associations that prevent the deletion of the Custom View.
    - `type` (string) **REQ** [maxLen=50] — Represents the association type, indicating the feature or module the resource belongs to.
    - `resources` (array of object) [maxItems=100] **REQ** — Represents the list of resources associated with this association type.
      - `id` (string/int64) **REQ** [maxLen=25] — Represents the unique identifier of the associated resource.
      - `name` (string) **REQ** [maxLen=255] — Represents the display name of the associated resource.
`NotAllowedDetailsDelete`:
  > Represents the error details returned when a Custom View cannot be deleted due to active associations.
  - `message` (string) **REQ** [maxLen=255] — Represents the error message describing why the deletion is not allowed.
  - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered an error.
  - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the not allowed deletion.
Possible values:
**NOT_ALLOWED** - The Custom View cannot be deleted because it has active associations.
  - `details` (object `NotAllowedDetails`) **REQ** — Represents the details of associations that prevent the deletion of a Custom View, including the association type and the list of associated resources.

**Responses:**

- **200**: Returns a success response indicating that all specified Custom Views were deleted. [application/json]
    > Represents the response schema for a successful Custom View deletion.
    - `custom_views` (array of object `CustomViewDeleteSuccess`) [maxItems=200] **REQ** — Represents the list of Custom Views deleted successfully.

- **207**: Returns a multi-status response when the deletion partially succeeded. Each item indicates whether the deletion succeeded or failed for that Custom View. [application/json]
    > Represents the multi-status response for the delete operation, containing a mix of success and failure items.
    - `custom_views` (array of object) [minItems=2, maxItems=200] **REQ** — Represents the list of Custom View deletion results, including both successful and failed items.
      oneOf:
        - `CustomViewDeleteSuccess` — Represents the successful deletion response for a Custom View, including the status, code, and confirmation message.
        - `CustomViewDeleteFailure` — Represents the deletion failure details for a Custom View, containing the error code, status, message, and additional context.

- **400**: The Custom View ID in the request is invalid or the view has already been deleted. Resolution: Verify that the Custom View IDs in the request are valid and the views have not already been deleted. [application/json]
    > Represents the error response for an invalid delete Custom View request.
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
      - `CustomViewDeleteItem` — Wrapped error: per-item delete failures inside custom_views array
        - `custom_views` (array of object `CustomViewDeleteFailure`) [maxItems=200] **REQ** — Represents the list of Custom View deletion result items, each containing success or failure details.

- **401**: Authentication failed or the OAuth access token does not include the required scope. Resolution: A new access token must be generated with the ZohoCRM.settings.custom_views.DELETE scope. [application/json]
    > Represents the error response for an unauthorized delete Custom View request.
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
      - `CvProfilePermissionError` — Represents the error response returned when the user does not have the required profile permission to perform the operation.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response.
Possible values:
**error** - The request encountered a permission error.
        - `message` (string) **REQ** [maxLen=255] — Represents the error message describing the permission denial.
        - `details` (object) **REQ** — Represents the additional details about the permission error.
          - `permissions` (array of string) [maxItems=25] — List of CRM permission keys that are missing for the operation
            items: [maxLen=255]
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for the permission denial.
Possible values:
**NO_PERMISSION** - The user does not have the required profile permission to perform the operation.

- **403**: Permission denied to delete Custom Views for this module. Resolution: The CRM administrator must grant the required permission to the user's profile. — Schema: `ModuleForbiddenErrorResponse` [application/json]
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

**Scopes:** ZohoCRM.settings.custom_views.DELETE
