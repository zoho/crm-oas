# GET /settings/portals/{portal}/user_type
**Operation:** `getPortalUserTypes` — Portal User Types
> Retrieves a list of all portal user types configured for the specified portal, with their summary configuration including name, status, user counts, and last modification time.

**Parameters:**
- `portal` (path, string, required) [maxLen=255]: Specify the API name of the portal whose user types are being managed. This is the unique identifier for the portal in Zoho CRM.
- `include` (query, string, optional) [enum=['modules']]: When set to `modules`, the response includes the full list of CRM modules and their access configurations for each portal user type.
- `include_inner_details` (query, string, optional) [enum=['field.field_label']]: When set to `fields` or another resource key, the response includes the detailed fields or sub-resource properties for the included modules.

**Responses:**

- **200**: The list of portal user types for the specified portal was retrieved successfully. — Schema: `GetusertypeResponse200` [application/json]
    > Returned on a successful request to list all portal user types. Contains an array of user type summary objects.
    schema: `GetusertypeResponse200`
    - `user_type` (array of object `GETUserTypeNested`) [maxItems=5] **REQ** — An array of portal user type summary objects, one per user type configured in the portal.
      schema: `GETUserTypeNested`
      - `created_time` (string) **REQ** [maxLen=255] — Represents the creation timestamp of the user type.
      - `default` (boolean) **REQ** — Indicates whether this is the default portal user type in the organization. The default user type is automatically assigned when no explicit user type is specified.
      - `modified_time` (string) **REQ** [maxLen=255] — Represents the ISO 8601 timestamp of when the portal user type was last modified.
      - `active_user_count` (integer/int32) **REQ** — Represents the number of portal users currently assigned to and active under this user type.
      - `personality_module` (object `GETPersonalityModuleNested`) **REQ** — Represents the nested object identifying the personality module configured for the portal user type. The personality module is the CRM module (for example, Contacts) whose records serve as portal user identities.
        schema: `GETPersonalityModuleNested`
        - `plural_label` (string) **REQ** [maxLen=255] — Represents the plural label of the module.
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM module configured as the personality module for this portal user type.
        - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique numeric identifier of the personality module in Zoho CRM.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the portal user type.
      - `modified_by` (object `GETModifiedByNested`) **REQ** — Represents the nested object identifying the Zoho CRM user who last modified the portal user type, containing the user's unique identifier and display name.
        schema: `GETModifiedByNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the Zoho CRM user who last modified the portal user type.
        - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique numeric identifier of the Zoho CRM user who last modified the portal user type.
      - `active` (boolean) **REQ** — Indicates whether the portal user type is currently active.
      - `invitation_field` (object `GETInvitationFieldNested`) **REQ** — The invitation field configured for the portal user type. This is the CRM field used to store the portal user's email address, to which portal invitations are sent.
        schema: `GETInvitationFieldNested`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM field designated as the invitation field for sending portal invitations.
        - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique numeric identifier of the invitation field in Zoho CRM.
      - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique numeric identifier of the portal user type.
      - `deactive_user_count` (integer/int32) **REQ** — Represents the number of portal users assigned to this user type who have been deactivated.
      - `created_by` (object `GETCreatedByNested`) **REQ** — Represents nested object identifying the Zoho CRM user who created the portal user type, containing the user's unique identifier and display name.
        schema: `GETCreatedByNested`
        - `name` (string) **REQ** [maxLen=255] — Represents the display name of the Zoho CRM user who created the portal user type.
        - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique numeric identifier of the Zoho CRM user who created the portal user type.

- **400**: The list request failed because the `{portal}` path parameter is invalid or the request is otherwise malformed. [application/json]
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

- **403**: The authenticated user does not have permission to list portal user types. [application/json]
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

**Scopes:** ZohoCRM.settings.clientportal.ALL, ZohoCRM.settings.clientportal.READ
