# POST /settings/functions/{fxIdentifier}/actions/publish
**Operation:** `publishFunction` — Publish a function
> This API is applicable only to **Java**, **Node.js**, and **Python** functions. The function must have an unpublished **draft** version before it can be published. **Deluge** functions are **automatically published** when they are created or updated and cannot be published using this API.

Publish an existing draft of a **Java**, **Node.js**, or **Python** function in your Zoho CRM account. You can optionally specify a changelog message for revision tracking. To identify functions with unpublished drafts, use the [Functions API](functions.yaml#$.paths./settings/functions.get) and check whether the **has_draft** field is **true** ("has_draft": true).


**Parameters:**
- `fxIdentifier` (path, string, required) [maxLen=255]: Specify the unique ID or API name of the function. You can obtain the function ID or API name using the [Functions API](functions.yaml#$.paths./settings/functions.get).

**Schemas:**
`InvalidDataPublishError`:
  > Represents an error response returned when a field value in a publish request contains an invalid data type.
  - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code for the invalid data failure. Possible values: **INVALID_DATA** - Indicates that the field value provided in the request does not match the expected data type.
  - `details` (object) **REQ** — The details of the validation error, including the expected data type, maximum length, field API name, and JSON path of the field that failed validation.
    - `expected_data_type` (string) [maxLen=255] — The data type expected for the field that caused the validation error.
    - `maximum_length` (integer/int32) — The maximum character length allowed for the field that caused the validation error.
    - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the invalid data error.
    - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the invalid data error.
  - `message` (string) **REQ** [enum=['invalid data']] — The error message describing the invalid data condition. Possible values: **invalid data** - Indicates the request payload contains one or more fields with invalid data.
  - `status` (string) **REQ** [enum=['error']] — The status of the API response for this error condition. Possible values: **error** - Indicates the request resulted in an error due to invalid data.

**Request Body** — application/json `PostpublishRequest`
> The request body must contain a **publish** object with the changelog details.
  > The request body for publishing a post, containing the publish configuration.
  - `publish` (object `PublishNested`) — This object will be used for publish info
    schema: `PublishNested`
    - `changelog` (string) [maxLen=250, nullable] — Changelog message for revision tracking. For Deluge functions, recorded as part of the auto-publish. For non-Deluge functions, recorded when the publish step succeeds.

**Responses:**

- **200**: Returns a confirmation that the function was published successfully. — Schema: `PostpublishResponse200` [application/json]
    > Represents the successful response returned after a publish operation, containing the results of the publish action.
    schema: `PostpublishResponse200`
    - `publish` (array of object `PublishNested1`) [maxItems=1] **REQ** — Represents the list of results returned for the publish operation.
      schema: `PublishNested1`
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the result code for the operation. Possible values: **SUCCESS** - The operation completed successfully.
      - `details` (object `DetailsNested`) **REQ** — Details object returned in success responses, containing the unique identifier of the affected resource.
        schema: `DetailsNested`
        - `id` (string/int64) — Represents the unique identifier of the function that was created, updated, or deleted.
      - `message` (string) **REQ** [maxLen=255] — Represents the success message describing the completed operation.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall status of the operation. Possible values: **success** - The operation completed without errors.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    oneOf:
      - `ErrorResponseNoClientPortalSupport` — The error response returned when the requested API is not supported for client portal users.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — The error code identifying the cause of the failure. Possible values: **API_NOT_SUPPORTED** - The requested API is not supported for the current user type.
        - `details` (object) **REQ** — Additional error details associated with the failure, including information about the unsupported login user type.
          - `unsupported_login_user_type` (string) **REQ** [maxLen=255] — The type of login user that is not supported for this API.
        - `message` (string) **REQ** [enum=['api not supported for client portal user']] — The error message returned when the requested API is not supported for client portal users. Possible values: **api not supported for client portal user** - The API cannot be used by client portal users.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
      - `FunctionAlreadyPublished` — Represents the error response returned when the requested action cannot be performed because the function is already published.
        - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — Represents the error code for this response. Possible values: **CANNOT_PERFORM_ACTION** - Indicates the requested action cannot be performed.
        - `details` (object) **REQ** — Represents additional details about the error encountered when a function is already published.
        - `message` (string) **REQ** [enum=['function is already published']] — Represents the error message returned when the function has already been published. Possible values: **function is already published** - Indicates that the targeted function was previously published and cannot be published again.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error condition. Possible values: **error** - Indicates that the request failed because the function is already published.
      - `APINotSupportedInThisVersion` — The error response returned when the requested API is not supported in the accessed version.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — The error code for this response. Possible values: **API_NOT_SUPPORTED** - The requested API is not supported in the current version.
        - `details` (object) **REQ** — Additional details about the version incompatibility, including the **supported_version** of the API that supports this endpoint.
          - `supported_version` (integer/int32) **REQ** — The earliest API version that supports this endpoint.
        - `message` (string) **REQ** [enum=['api not supported in this version']] — The error message describing the version incompatibility. Possible values: **api not supported in this version** - Indicates that the requested API is not available in the current API version.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request was not processed successfully.
      - `ErrorResponseResourcePathIndex` — Represents the error response returned when invalid data is detected in the request URL path.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of invalid data error. Possible values: **INVALID_DATA** - Indicates that the data provided in the request URL path is invalid.
        - `details` (object) **REQ** — The error details for the failed request, including the **resource_path_index** that identifies the position in the URL path where the invalid value was found.
          - `resource_path_index` (integer/int32) **REQ** — Index position in the URL resource path where the invalid value was found.
        - `message` (string) **REQ** [enum=['invalid data']] — The error message returned for the failed request. Possible values: **invalid data** - The value supplied in the URL resource path is not valid.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request failed due to an invalid value in the URL resource path.
      - `ErrorResponseFeatureNotSupported` — The error response returned when a requested feature is not supported for the current edition.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — The error code for this response. Possible values: **FEATURE_NOT_SUPPORTED** - Indicates that the requested feature is not supported for the current edition.
        - `details` (object) **REQ** — Additional details about the error.
        - `message` (string) **REQ** [enum=['Your License does not support this feature']] — The error message returned when the feature is not supported. Possible values: **Your License does not support this feature** - Indicates that the current license does not include the requested feature.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
      - `CodeFileNonDelugeCompilationErrors` — Represents the error response returned when a non-Deluge function's code fails to compile during a publish attempt. Contains the error code **COMPILATION_ERROR**, along with details that include the file, line, and message for each compilation error.
        - `code` (string) **REQ** [enum=['COMPILATION_ERROR']] — Represents the error code for the response. Possible values: **COMPILATION_ERROR** - Indicates the function's code failed to compile.
        - `details` (object) **REQ** — Represents the error details for the compilation failure, including the list of individual errors found in the code.
          - `errors` (array of object) [maxItems=5000] **REQ** — The list of compilation errors found in the function code.
            - `file` (string) [maxLen=5000] — Relative file path within the code package where the error occurred.
            - `line` (integer/int32) — Line number in the source file where the error occurred.
            - `message` (string) **REQ** [maxLen=5000] — The description of the compilation error.
        - `message` (string) **REQ** [enum=['function publish failed due to compilation errors']] — The error message returned when a function publish operation fails due to compilation errors. Possible values: **function publish failed due to compilation errors** - Indicates that the function could not be published because the code contains compilation errors.
        - `status` (string) **REQ** [enum=['error']] — The status of the response when a compilation error occurs. Possible values: **error** - Indicates that the operation failed due to a compilation error.
      - `InvalidDataMetaDataError` — Represents an error response returned when a request field contains an invalid data type, including the error code, status, message, and validation details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of validation failure. Possible values: **INVALID_DATA** - Indicates that a request field contains an invalid data type.
        - `details` (object) **REQ** — Represents the validation details for the failed field, including the expected data type and the parameter name that caused the error.
          - `expected_data_type` (string) **REQ** [maxLen=255] — Represents the data type that the field requires for a valid request.
          - `param_name` (string) **REQ** [maxLen=255] — Name of the parameter that caused the error.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message describing the invalid data issue. Possible values: **invalid data** - Indicates that the submitted data failed validation.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the API response for this error. Possible values: **error** - Indicates that the request resulted in an error.
      - `InvalidDataPublishError` — Represents an error response returned when a field value in a publish request contains an invalid data type.
        - `publish` (array of object `InvalidDataPublishError`) [maxItems=25] **REQ** — Array of error objects
        - `metadata` (object) **REQ**
          oneOf:
            - `InvalidDataExpDataTypeError` — The error response returned when a field value fails data type validation, identified by the **INVALID_DATA** error code.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of validation failure. Possible values: **INVALID_DATA** - The field value does not match the expected data type or format.
              - `details` (object) **REQ** — The details of the validation error, including the expected data type, maximum length, API name, and JSON path of the field that caused the error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — The data type that the field expects, as determined by the field's schema definition.
                - `maximum_length` (integer/int32) **REQ** — The maximum number of characters or digits permitted for the field that failed validation.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the field that caused the data type error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the data type error.
              - `message` (string) **REQ** [enum=['Invalid data type']] — The error message describing the issue. Possible values: **Invalid data type** - The value provided for the field does not match the expected data type.
              - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
            - `InvalidDataMaxLenError` — An error response returned when submitted data exceeds the maximum allowed length, including the error code, status, message, and validation details.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code identifying the type of validation failure. Possible values: **INVALID_DATA** - Indicates that the submitted data is invalid.
              - `details` (object) **REQ** — The validation details associated with the error, including the maximum allowed length, the API name of the field, and the JSON path to the invalid value.
                - `maximum_length` (integer/int32) **REQ** — The maximum number of characters allowed for the field that caused the error.
                - `api_name` (string) **REQ** [maxLen=255] — API name of the field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data']] — The error message returned when the submitted data exceeds the maximum allowed length for a field. Possible values: Invalid data - The submitted value exceeds the maximum character length defined for the field.
              - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: error - Indicates that the request failed due to invalid data.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to publish the function. **Resolution:** The CRM administrator must grant the required permission to the user's profile. [application/json]
    > Represents the error response returned when the publish function request is denied due to insufficient permissions.
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

**Scopes:** ZohoCRM.settings.functions.CREATE
