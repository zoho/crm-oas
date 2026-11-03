# DELETE /settings/functions/{fxIdentifier}
**Operation:** `deleteFunction` — Function
> To delete a function identified by its unique ID or API name from your Zoho CRM organization. The function can't be deleted if it has active references or associations, such as workflow rules, buttons, or schedules, references from other functions, or REST API exposure. Remove the references and associations, or disable the REST API exposure, before attempting deletion.

You can obtain the function ID or API name using the [Functions API](functions.yaml#$.paths./settings/functions.get).


**Parameters:**
- `fxIdentifier` (path, string, required) [maxLen=255]: Specify the unique ID or API name of the function. You can obtain the function ID or API name using the [Functions API](functions.yaml#$.paths./settings/functions.get).

**Responses:**

- **200**: Returns a confirmation that the specified function was deleted successfully. — Schema: `DeletefunctionsResponse200` [application/json]
    > Represents the response returned after a successful function deletion, containing the details of the deleted functions.
    schema: `DeletefunctionsResponse200`
    - `functions` (array of object `FunctionsNested1`) [maxItems=1] **REQ** — The list of function deletion result items returned in the response.
      schema: `FunctionsNested1`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the operation result code. Possible values: **SUCCESS** - The operation completed successfully.
      - `details` (object `DetailsNested`) **REQ** — Details object returned in success responses, containing the unique identifier of the affected resource.
        schema: `DetailsNested`
        - `id` (string/int64) — Represents the unique identifier of the function that was created, updated, or deleted.
      - `message` (string) **REQ** [maxLen=255] — Represents the message describing the outcome of the operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the status of the operation. Possible values: **success** - The operation completed without errors.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request can't be processed due to invalid syntax. **Resolution:** The request syntax must be corrected before resubmitting. [application/json]
    > Represents the error response returned when the delete function request cannot be completed.
    oneOf:
      - `ErrorResponseNoClientPortalSupport` — The error response returned when the requested API is not supported for client portal users.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — The error code identifying the cause of the failure. Possible values: **API_NOT_SUPPORTED** - The requested API is not supported for the current user type.
        - `details` (object) **REQ** — Additional error details associated with the failure, including information about the unsupported login user type.
          - `unsupported_login_user_type` (string) **REQ** [maxLen=255] — The type of login user that is not supported for this API.
        - `message` (string) **REQ** [enum=['api not supported for client portal user']] — The error message returned when the requested API is not supported for client portal users. Possible values: **api not supported for client portal user** - The API cannot be used by client portal users.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
      - `ErrorResponseFeatureNotSupported` — The error response returned when a requested feature is not supported for the current edition.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — The error code for this response. Possible values: **FEATURE_NOT_SUPPORTED** - Indicates that the requested feature is not supported for the current edition.
        - `details` (object) **REQ** — Additional details about the error.
        - `message` (string) **REQ** [enum=['Your License does not support this feature']] — The error message returned when the feature is not supported. Possible values: **Your License does not support this feature** - Indicates that the current license does not include the requested feature.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
      - `ErrorResponseResourcePathIndex` — Represents the error response returned when invalid data is detected in the request URL path.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of invalid data error. Possible values: **INVALID_DATA** - Indicates that the data provided in the request URL path is invalid.
        - `details` (object) **REQ** — The error details for the failed request, including the **resource_path_index** that identifies the position in the URL path where the invalid value was found.
          - `resource_path_index` (integer/int32) **REQ** — Index position in the URL resource path where the invalid value was found.
        - `message` (string) **REQ** [enum=['invalid data']] — The error message returned for the failed request. Possible values: **invalid data** - The value supplied in the URL resource path is not valid.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request failed due to an invalid value in the URL resource path.
      - `FxReferenceError` — The error returned when attempting to delete a function that is referenced as an inline function by other functions. All inline function references must be removed before deletion can proceed.
        - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — The error code identifying the type of failure. Possible values: **CANNOT_PERFORM_ACTION** - Indicates that the requested action cannot be performed because the function is referenced by other functions.
        - `details` (object) **REQ** — Additional details about the error, providing context on the conditions that caused the failure.
        - `message` (string) **REQ** [enum=['function has references']] — Represents the error message describing why the function could not be deleted. Possible values: **function has references** - The function has existing references and cannot be removed.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates the request resulted in an error.
      - `FxAssociationError` — Represents an error response returned when a function cannot be deleted because it is still associated with a Button, Workflow rule, or another CRM component.
        - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['function has associations']] — Represents the error message describing the association conflict. Possible values: function has associations - Indicates that the function cannot be deleted because it has one or more active associations.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: error - Indicates that the request resulted in an error.
      - `FxRestApiExposedError` — Error returned when attempting to delete a function that is currently exposed as a REST API. Remove the REST API exposure before deletion.
        - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — Represents the error code returned when the action cannot be performed. Possible values: **CANNOT_PERFORM_ACTION** - The requested action could not be completed.
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['function exposed as a REST API']] — Represents the error message describing why the action failed for the function exposed as a REST API.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response. Possible values: **error** - The request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to delete the specified function. **Resolution:** The CRM administrator must grant the required permission to the user's profile. [application/json]
    > Represents the error response returned when the request is denied due to insufficient permissions.
    oneOf:
      - `NoDevPermissionError` — An error response returned when the requesting user lacks the required permission to perform the operation.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — The error code for the permission denial response. Possible values: **NO_PERMISSION** - The requesting user does not have permission to perform the operation.
        - `details` (object) **REQ** — Additional details about the permission denial error, including the permissions required to perform the operation.
          - `permissions` (array of string) [maxItems=25] **REQ** — The list of permissions required to perform the operation that was denied.
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=['permission denied']] — The error message describing the permission denial. Possible values: **permission denied** - Indicates that the requesting user lacks the required permission to perform the operation.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
      - `UserEmailNotConfirmedError` — Represents the error response returned when the requesting user's email address has not been confirmed.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code for this response. Possible values: **NO_PERMISSION** - Indicates the operation was not permitted.
        - `details` (object) **REQ** — Represents additional details about the error. This object is empty for this error type.
        - `message` (string) **REQ** [enum=['User email not confirmed']] — Represents the error message for this response. Possible values: **User email not confirmed** - Indicates the user's email address has not been confirmed.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. Possible values: **error** - Indicates the request resulted in an error.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.functions.DELETE
