# GET /settings/functions/{fxIdentifier}/code
**Operation:** `getFunctionCode` — Download Function Code
> This API downloads the source code of the specified function.

- **Deluge Functions:** A Deluge function consists of a single source file containing the function logic. When downloaded, the API returns the function as a **.ds file** with a maximum file size of **2 MB**.
- **Multi-file runtime Functions:** **Java, Node.js, and Python** functions are packaged as projects that can contain multiple source files and folders, rather than a single source file. When downloaded, the API returns the function as a **ZIP (.zip)** package with a maximum file size of **25 MB**.

You can obtain the function ID or API name using the [Functions API](functions.yaml#$.paths./settings/functions.get).


**Note:** The above images show sample downloads for both Deluge functions and multi-file runtime functions (Java, Node.js, and Python).


**Parameters:**
- `version` (query, string, optional) [enum=['draft']]: Specify which version of the function code to retrieve. Possible values: **draft** - Retrieves the draft version of the function code. When omitted, the published version is returned.
- `fxIdentifier` (path, string, required) [maxLen=255]: Specify the unique ID or API name of the function. You can obtain the function ID or API name using the [Functions API](functions.yaml#$.paths./settings/functions.get).

**Responses:**

- **200**: Returns the source code file for the specified function. [application/octet-stream] (also: application/zip)
    > Represents the source code file returned for the specified function.
    type: string/binary — Represents the source code file returned for the specified function.
  *Alt schema for application/zip*:
      type: string/binary — Represents the ZIP package containing the source code for the specified function.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request is invalid. **Resolution:** The request syntax must be corrected before resubmitting. [application/json]
    > Represents the error response body returned when the request contains invalid data.
    oneOf:
      - `ErrorResponseNoClientPortalSupport` — The error response returned when the requested API is not supported for client portal users.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — The error code identifying the cause of the failure. Possible values: **API_NOT_SUPPORTED** - The requested API is not supported for the current user type.
        - `details` (object) **REQ** — Additional error details associated with the failure, including information about the unsupported login user type.
          - `unsupported_login_user_type` (string) **REQ** [maxLen=255] — The type of login user that is not supported for this API.
        - `message` (string) **REQ** [enum=['api not supported for client portal user']] — The error message returned when the requested API is not supported for client portal users. Possible values: **api not supported for client portal user** - The API cannot be used by client portal users.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request resulted in an error.
      - `DraftVersionsNotExist` — Represents the error response returned when no draft version exists for the requested function.
        - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — The error code identifying the type of failure. Possible values: **CANNOT_PERFORM_ACTION** - Indicates that the requested action cannot be performed because no draft version exists.
        - `details` (object) **REQ** — Additional details about the error, providing context on why the action could not be performed.
        - `message` (string) **REQ** [enum=['draft version not exist']] — The error message returned when a draft version does not exist. Possible values: **draft version not exist** - The specified draft version could not be found.
        - `status` (string) **REQ** [enum=['error']] — The status of the response for this error condition. Possible values: **error** - Indicates that the request resulted in an error.
      - `PublishedVersionsNotExist` — The error response returned when no published version exists for the function.
        - `code` (string) **REQ** [enum=['CANNOT_PERFORM_ACTION']] — The error code identifying the type of failure. Possible values: **CANNOT_PERFORM_ACTION** - Indicates the requested action cannot be performed.
        - `details` (object) **REQ** — Additional details about the error condition.
        - `message` (string) **REQ** [enum=['published version not exist']] — The error message describing the failure. Possible values: **published version not exist** - Indicates that no published version exists for the function.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - Indicates the request resulted in an error.
      - `APINotSupportedInThisVersion` — The error response returned when the requested API is not supported in the accessed version.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — The error code for this response. Possible values: **API_NOT_SUPPORTED** - The requested API is not supported in the current version.
        - `details` (object) **REQ** — Additional details about the version incompatibility, including the **supported_version** of the API that supports this endpoint.
          - `supported_version` (integer/int32) **REQ** — The earliest API version that supports this endpoint.
        - `message` (string) **REQ** [enum=['api not supported in this version']] — The error message describing the version incompatibility. Possible values: **api not supported in this version** - Indicates that the requested API is not available in the current API version.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request was not processed successfully.
      - `ParamPatternNotMatchedError` — Represents the error response returned when a query parameter value does not match the expected pattern.
        - `code` (string) **REQ** [enum=['PATTERN_NOT_MATCHED']] — Represents the error code identifying the type of pattern mismatch. Possible values: **PATTERN_NOT_MATCHED** - Indicates the query parameter value does not match the expected pattern.
        - `details` (object) **REQ** — The details of the parameter pattern mismatch error, including the name of the parameter for which the value did not match the expected pattern.
          - `param_name` (string) **REQ** [maxLen=50] — The name of the parameter for which the submitted value did not match the expected pattern.
        - `message` (string) **REQ** [enum=['Please check whether the input values are correct']] — The error message describing the parameter pattern mismatch.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response for this error. Possible values: **error** - Indicates that the request failed due to a parameter pattern mismatch.
      - `ErrorResponseResourcePathIndex` — Represents the error response returned when invalid data is detected in the request URL path.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code identifying the type of invalid data error. Possible values: **INVALID_DATA** - Indicates that the data provided in the request URL path is invalid.
        - `details` (object) **REQ** — The error details for the failed request, including the **resource_path_index** that identifies the position in the URL path where the invalid value was found.
          - `resource_path_index` (integer/int32) **REQ** — Index position in the URL resource path where the invalid value was found.
        - `message` (string) **REQ** [enum=['invalid data']] — The error message returned for the failed request. Possible values: **invalid data** - The value supplied in the URL resource path is not valid.
        - `status` (string) **REQ** [enum=['error']] — The status of the API response. Possible values: **error** - Indicates that the request failed due to an invalid value in the URL resource path.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to retrieve the function code. **Resolution:** The CRM administrator must grant the required permission to the user's profile. [application/json]
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

**Scopes:** ZohoCRM.settings.functions.READ
