# GET /settings/functions/{fxIdentifier}
**Operation:** `getFunction` — Function
> Use this API to retrieve the details of a specific [function](https://www.zoho.com/crm/developer/docs/functions/overview/introduction.html) in your Zoho CRM account by specifying its unique ID or API name. The response contains information such as the function's runtime, category, state, arguments, tags, REST API mode, and creation and modification details. To get the implementation code of the function, you must use the [Download Function Code API](functions.yaml#$.paths./settings/functions/{fxIdentifier}/code.get).

You can obtain the function ID or API name using the [Functions API](functions.yaml#$.paths./settings/functions.get).


**Note:** If the specified function ID or API name does not exist, the API returns an **HTTP 204 (No Content)** response with an empty response body.


**Parameters:**
- `fxIdentifier` (path, string, required) [maxLen=255]: Specify the unique ID or API name of the function. You can obtain the function ID or API name using the [Functions API](functions.yaml#$.paths./settings/functions.get).

**Responses:**

- **200**: Returns the details of the requested function configuration. — Schema: `GetfunctionResponse200` [application/json]
    > The successful response returned when retrieving one or more functions from the Zoho CRM organization.
    schema: `GetfunctionResponse200`
    - `functions` (array of object `GETFunctionsNested`) [maxItems=200] **REQ** — The list of function metadata objects returned by the operation.
      schema: `GETFunctionsNested`
      - `return_type` (string) **REQ** [enum=[10 values], nullable] — The data type the function returns when executed. Possible values: **bool** - Boolean return type. **collection** - Collection return type. **date** - Date return type. **float** - Floating-point number return type. **int** - Integer return type. **list** - List return type. **map** - Map return type. **string** - String return type. **void** - No return value. **null** - Return type is not explicitly set.
      - `created_time` (string/date-time) **REQ** — The timestamp when the function was created.
      - `has_draft` (boolean) **REQ** — Indicates whether the function has an unpublished draft version that differs from the currently published version. Possible values: **true** - The function has an unpublished draft version. **false** - The function does not have an unpublished draft version.
      - `description` (string) **REQ** [maxLen=3000, nullable] — The description of the function's purpose and behavior provided by the user. Null if no description has been set.
      - `runtime` (string) **REQ** [enum=['Deluge 1.0', 'NodeJS 8', 'NodeJS 22', 'Java 8', 'Java 17', 'Python 3.12']] — Represents the execution runtime environment used to run this function. Possible values: **Deluge 1.0** - Deluge scripting runtime version 1.0. **NodeJS 8** - Node.js runtime version 8. **NodeJS 22** - Node.js runtime version 22. **Java 8** - Java runtime version 8. **Java 17** - Java runtime version 17. **Python 3.12** - Python runtime version 3.12.
      - `language` (string) **REQ** [enum=['Deluge', 'Node JS', 'Java', 'Python']] — Represents the programming language in which this function is written. Possible values: **Deluge** - Zoho's proprietary Deluge scripting language. **Node JS** - JavaScript runtime environment (Node.js). **Java** - Java programming language. **Python** - Python programming language.
      - `source` (string) **REQ** [enum=['crm', 'extension', 'private_extension']] — Represents the origin of this function. Possible values: **crm** - The function was created within Zoho CRM. **extension** - The function originates from a Marketplace extension. **private_extension** - The function originates from a private extension.
      - `rest_api_mode` (array of string) [maxItems=3] **REQ** — Represents the REST API authentication modes enabled for this function.
        items: [enum=['Oauth', 'ZAPI', 'None']]
      - `created_by` (object `GETCreatedByNested`) **REQ** — Represents the user who created the resource, including the user's name and ID.
        schema: `GETCreatedByNested`
        - `name` (string) **REQ** [maxLen=100] — Display name of the user who created the function.
        - `id` (string/int64) **REQ** — The unique ID of the user who created the function.
      - `modified_time` (string/date-time) **REQ** — Represents the timestamp of the last modification made to the function.
      - `api_name` (string) **REQ** [maxLen=100, pattern=^[A-Za-z][A-Za-z0-9_-]*$] — Represents the unique programmatic identifier for the function, used in API calls and automation references.
      - `name` (string) **REQ** [maxLen=100] — Represents the display name of the function.
      - `modified_by` (object `GETModifiedByNested`) **REQ** — Represents the user who last modified the resource, including the user's display name and unique identifier.
        schema: `GETModifiedByNested`
        - `name` (string) **REQ** [maxLen=100] — Represents the display name of the user who last modified the resource.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the user who last modified the resource.
      - `arguments` (array of object `GETArgumentsNested`) [maxItems=50, nullable] **REQ** — List of input arguments accepted by the function. Null if the function takes no arguments.
        schema: `GETArgumentsNested`
        - `name` (string) **REQ** [maxLen=100] — The name of the function argument.
        - `type` (string) **REQ** [maxLen=100] — The data type of the function argument.
      - `state` (string) **REQ** [enum=['active', 'unpublished', 'deprecated', 'archived', 'inactive', 'hibernated']] — Represents the current lifecycle state of the function. Possible values: **active** - The function has a published version. **unpublished** - The function was created but has never been published. **deprecated** - The function is deprecated. **archived** - The function is archived. **inactive** - The function is inactive. **hibernated** - The function is hibernated.
      - `id` (string/int64) **REQ** — The numeric identifier of the function.
      - `Tag` (array of object `GETTagNested`) [maxItems=200] **REQ** — The list of tags associated with the function.
        schema: `GETTagNested`
        - `name` (string) **REQ** [maxLen=100] — The display name of the tag.
        - `id` (string/int64) **REQ** — Unique identifier of the tag.
        - `color_code` (string/color) **REQ** — The hex color code assigned to the tag for visual identification.
      - `category` (string) **REQ** [enum=[8 values]] — The trigger category that determines how and when the function executes. Possible values: **Related List** - The function is triggered from a related list context. **Validation Rule** - The function executes as part of a Validation Rule. **Schedule** - The function runs on a scheduled basis. **Automation** - The function is triggered by an automation event. **Standalone** - The function runs independently without a trigger context. **Signals** - The function is triggered by a Signals event. **Button** - The function executes when a button is clicked. **Dynamic** - The function operates in a dynamic context.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **204**: Indicates that the request was successful but no function data was found for the specified identifier.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request could not be processed due to invalid syntax or a malformed function identifier. **Resolution:** The request must be corrected to use a valid function identifier in the correct format before resubmitting. [application/json]
    > Represents the error response body returned for a 400 Bad Request, containing the error code, status, message, and details.
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
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **403**: Permission denied to retrieve the function configuration. **Resolution:** The CRM administrator must grant the required permission to the user's profile. [application/json]
    > Represents the error details returned when the request is denied due to insufficient permissions.
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
