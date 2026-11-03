# GET /settings/functions/__schemas/runtimes
**Operation:** `getRuntimes` — List Function Runtime
> To retrieve the list of all supported function runtimes available in your Zoho CRM organization, including the programming language, runtime version identifier, and deprecation status for each entry.

**Responses:**

- **200**: Returns the list of available function runtimes supported in the Zoho CRM organization. — Schema: `GetruntimesResponse200` [application/json]
    > The response returned when retrieving the list of supported runtime environments.
    schema: `GetruntimesResponse200`
    - `runtimes` (array of object `GETRuntimesNested`) [maxItems=100] **REQ** — Array of supported runtime environment entries.
      schema: `GETRuntimesNested`
      - `deprecated` (boolean) **REQ** — Indicates whether this runtime version is deprecated and should no longer be used for new functions. Possible values: **true** - The runtime version is deprecated. **false** - The runtime version is active and available for use.
      - `runtime` (string) **REQ** [enum=['Deluge 1.0', 'NodeJS 8', 'NodeJS 22', 'Java 8', 'Java 17', 'Python 3.12']] — The runtime version identifier for this function entry. Possible values: **Deluge 1.0** - Deluge scripting language, version 1.0. **NodeJS 8** - Node.js runtime, version 8. **NodeJS 22** - Node.js runtime, version 22. **Java 8** - Java runtime, version 8. **Java 17** - Java runtime, version 17. **Python 3.12** - Python runtime, version 3.12.
      - `language` (string) **REQ** [enum=['Deluge', 'Node JS', 'Java', 'Python']] — Represents the programming language of the runtime. Possible values: **Deluge** - Deluge scripting language. **Node JS** - Node.js runtime environment. **Java** - Java runtime environment. **Python** - Python runtime environment.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

- **400**: The request is not supported for the authenticated user type. **Resolution:** The API is available only for supported user types; client portal users must use a non-portal CRM user account to access this endpoint. [application/json]
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

- **403**: Permission denied to access the requested resource. **Resolution:** The CRM administrator must grant the required permission to the user's profile. [application/json]
    > Represents the error response returned when the request is forbidden due to insufficient permissions.
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
