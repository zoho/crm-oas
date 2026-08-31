# DELETE /settings/portals/{portal}/user_type/{userTypeId}
**Operation:** `deletePortalUserType` — Delete user type
> Deletes the specified portal user type from the portal. If portal users are assigned to this user type, provide `transfer_To` with the ID of another user type to transfer them before deletion.

**Parameters:**
- `portal` (path, string, required) [maxLen=255]: Specify the API name of the portal whose user types are being managed. This is the unique identifier for the portal in Zoho CRM.
- `userTypeId` (path, string/int64, required) [maxLen=255]: Provide the unique numeric identifier of the portal user type to retrieve, update, or delete.
- `userTypeId` (path, string/int64, required) [maxLen=255]: Provide the unique numeric identifier of the portal user type to retrieve, update, or delete.
- `transfer_To` (query, string/int64, optional) [maxLen=255, pattern=^[0-9]+$]: The ID of the portal user type to transfer existing users to before deleting. Required when the user type being deleted has active users assigned to it.

**Responses:**

- **200**: Zoho CRM deleted the portal user type successfully. The response contains the name of the deleted user type. — Schema: `DeleteusertypeResponse200` [application/json]
    > Returned on successful deletion of a portal user type. Contains the name of the deleted user type.
    schema: `DeleteusertypeResponse200`
    - `user_type` (array of object `UserTypeNested2`) [maxItems=1] **REQ** — An array containing the result of the delete operation, including the identifier of the deleted user type.
      schema: `UserTypeNested2`
      - `code` (string) [maxLen=255] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
      - `details` (object `DetailsNested`) — A nested object containing additional detail fields returned with error responses, such as the field API name and JSON path that identify where the validation failure occurred.
        schema: `DetailsNested`
        - `id` (string/int64) [maxLen=255] — Represents the unique numeric identifier of the resource referenced in the error detail.
      - `message` (string) [maxLen=255] — Represents the error message that Zoho CRM returned, describing what went wrong.
      - `status` (string) [maxLen=255] — Represents the result status of the API call. The value is `error` for all error responses.

- **400**: The request failed. This may occur if the user type still has active portal users assigned to it, or if the request body contains invalid data. [application/json]
    > One or more error conditions occurred. See the `oneOf` variants for specific error schemas.
    oneOf:
      - `ApiNotSupportedForClientPortalUserError` — Returned when the API operation is not supported for portal users. This error applies when the request is made in a context that is incompatible with client portal user access.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — Represents the error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
        - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
          - `unsupported_login_user_type` (string) **REQ** [maxLen=255] — Represents the login user type that should not be supported.
        - `message` (string) **REQ** [enum=['api not supported for client portal user']] — Represents the error message that Zoho CRM returned, describing what went wrong.
        - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
      - `ApiNotSupportedInSandboxError` — Returned when the Portal User Types API is called in a Zoho CRM sandbox environment, where this API is not available.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
        - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
          - `unsupported_environment` (string) **REQ** [maxLen=255] — Represents the environment that should not be supported.
        - `message` (string) **REQ** [enum=['api not supported in sandbox']] — The error message that Zoho CRM returned, describing what went wrong.
        - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
      - `ApiNotSupportedForDomainError` — Returned when the Portal User Types API is not supported for the specified domain configuration.
        - `code` (string) **REQ** [enum=['API_NOT_SUPPORTED']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
        - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
          - `supported_domains` (array of string) [maxItems=25] **REQ** — The list of domain configurations that are supported for this operation.
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=['api not supported']] — The error message that Zoho CRM returned, describing what went wrong.
        - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
      - `InvalidPortalNameError` — Returned when the `{portal}` path parameter does not match any portal configured in the organization's Zoho CRM account.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
        - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
        - `message` (string) **REQ** [enum=['No portal exists with the given portal name.']] — The error message that Zoho CRM returned, describing what went wrong.
        - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
      - `DeleteUserTypeUsersPresentError` — Returned when the portal user type cannot be deleted because it still has active portal users assigned to it. Remove or reassign users before deleting the user type.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
        - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
          - `param_name` (string) **REQ** [maxLen=255] — Represents the parameter name.
        - `message` (string) **REQ** [enum=[1 values]] — The error message that Zoho CRM returned, describing what went wrong.
        - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.

- **403**: The authenticated user does not have permission to delete portal user types. [application/json]
    > The request was rejected due to insufficient permissions. See the `oneOf` variants for specific permission error schemas.
    oneOf:
      - `NoPermissionError` — Returned when the authenticated user does not have permission to manage portal user types in the target organization.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
        - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
          - `permissions` (array of string) [maxItems=25] **REQ** — The list of permission entries associated with the error condition.
            items: [maxLen=255]
        - `message` (string) **REQ** [enum=['No permission']] — The error message that Zoho CRM returned, describing what went wrong.
        - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
      - `NoPermissionManagePortalsDisabledError` — Returned when the 'Manage Portals' permission has been disabled for the authenticated user's profile, preventing access to portal configuration APIs.
        - `code` (string) **REQ** [enum=['NO_PERMISSION']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
        - `details` (object) **REQ** — An empty object included for consistency with other error response shapes. No additional details are provided for this error condition.
        - `message` (string) **REQ** [enum=['NO_PERMISSION']] — The error message that Zoho CRM returned, describing what went wrong.
        - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.

**Scopes:** ZohoCRM.settings.clientportal.ALL, ZohoCRM.settings.clientportal.DELETE
