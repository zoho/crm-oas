# PUT /settings/portals/{portal}/user_type/{userTypeId}
**Operation:** `updatePortalUserType` — Portal User Type
> Updates the configuration of an existing portal user type. You can modify module-level access settings, including shared type, allowed layouts, filter fields, and field-level permissions.

**Parameters:**
- `portal` (path, string, required) [maxLen=255]: Specify the API name of the portal whose user types are being managed. This is the unique identifier for the portal in Zoho CRM.
- `userTypeId` (path, string/int64, required) [maxLen=255]: Provide the unique numeric identifier of the portal user type to retrieve, update, or delete.
- `userTypeId` (path, string/int64, required) [maxLen=255]: Provide the unique numeric identifier of the portal user type to retrieve, update, or delete.

**Request Body** — application/json `PutusertypeRequest`
> The request body containing the portal user type fields to update. Include only the fields you want to change.
  > The request body schema for the update portal user type operation. Contains the `user_type` array with the fields to be updated.
  - `user_type` (array of object `UserTypeNestedV2`) [maxItems=1] **REQ** — An array containing the portal user type configuration to update. Must contain exactly one user type object with the fields to be modified.
    schema: `UserTypeNestedV2`
    - `personality_module` (object `PersonalityModuleNested`) — The updated personality module for the portal user type. Cannot be changed for the default user type.
      schema: `PersonalityModuleNested`
      - `api_name` (string) [maxLen=25, pattern=^[A-Za-z0-9_]{1,25}$] — Represents the API Name of the Personality Module.
      - `id` (string/int64) [maxLen=18] — The unique numeric identifier of the personality module in Zoho CRM.
    - `name` (string) [maxLen=50, nullable] — The updated display name for the portal user type. Must be alphanumeric with spaces only, maximum 50 characters.
    - `active` (boolean) [nullable] — Set to `true` to activate the portal user type or `false` to deactivate it.
    - `modules` (array of object `ModulesNestedV2`) [maxItems=1, nullable] — Represents the list of modules whose properties you want to update within the portal user type.
      schema: `ModulesNestedV2`
      - `shared_type` (string) [maxLen=7, minLen=6, enum=['public', 'private'], nullable] — The updated sharing mode for this module. Possible values: `public` (all records are shared with the portal user, and can be restricted using secondary conditions) or `private` (only records matching configured filter or secondary conditions are shared with the portal user).
      - `permissions` (object `PermissionsNestedV2`) — The updated CRUD permissions for portal users on this module.
        schema: `PermissionsNestedV2`
        - `edit_shared_records` (boolean) — Represents the updated permission for portal users to edit records shared from CRM into this module.
        - `create` (boolean) — Represents the updated create permission for portal users on this module. Set to `true` to allow portal users to create records.
        - `view` (boolean) — Represents the updated view permission for portal users on this module.
        - `edit` (boolean) — Represents the updated edit permission for portal users on records they created in this module.
        - `delete` (boolean) — Represents the updated delete permission for portal users on this module. Set to `true` to allow portal users to delete records.
      - `id` (string) [maxLen=25, pattern=^[0-9]+$] — Represents the unique numeric identifier of the CRM module to be updated within the portal user type.
      - `filters` (array of object `FiltersNested`) [maxItems=1, nullable] — Represents the updated filter-by field configuration for the module. Specifies the CRM field by which portal users can filter records.
        schema: `FiltersNested`
        - `display_label` (string) [maxLen=255] — Represents the display label of the filter field.
        - `id` (string) [maxLen=25, pattern=^[0-9]+$] — Represents the unique identifier of the filter field.
        - `api_name` (string) [maxLen=256] — Represents the API name of the resource
      - `layouts` (array of object `LayoutsNested`) [maxItems=1, nullable] — Represents the updated list of CRM layouts accessible to portal users for this module.
        schema: `LayoutsNested`
        - `display_label` (string) [maxLen=255] — Represents the display label of the CRM layout.
        - `name` (string) [maxLen=255] — Represents the internal name of the CRM layout.
        - `id` (string) [maxLen=25, pattern=^[0-9]+$] — Specifies the unique identifier of the CRM layout.
        - `_default_view` (object `DefaultViewNested`) — Nested schema for _default_view representing the default view configuration associated with the portal user type, including the view's unique identifier, name, display label, and type.
          oneOf:
            - `DefaultViewLayoutNested` — Nested schema for _default_view when type is layout
              - `display_label` (string) [maxLen=255] — Represents the display label of the default layout view.
              - `name` (string) [maxLen=255] — Represents the internal name of the default view.
              - `id` (string) [maxLen=25, pattern=^[0-9]+$] — Represents the unique numeric identifier of the default view.
              - `type` (string) [maxLen=255, enum=['layout']] — The type of the default view.
            - `DefaultViewWizardNested` — Nested schema for _default_view when type is wizard
              - `display_label` (string) [maxLen=255] — The display label of the resource
              - `name` (string) [maxLen=255] — The name of the resource
              - `id` (string/int64) [maxLen=19] — The unique identifier of the resource
              - `type` (string) [maxLen=255, enum=['wizard']] — The type of the resource
      - `views` (object `ViewsNested`) — The updated list view (canvas view or custom view) accessible to portal users for this module.
        schema: `ViewsNested`
        - `display_label` (string) [maxLen=255] — Represents the display label of the list view shown to portal users.
        - `name` (string) [maxLen=255] — Represents the name of the resource.
        - `id` (string) [maxLen=25, pattern=^[0-9]+$] — Represents the unique identifier of the resource.
        - `type` (string) [maxLen=255, enum=['canvas_view', 'custom_view']] — The type of the list view. Possible values: `canvas_view` (Canvas View), `custom_view` (Custom List View).

**Responses:**

- **200**: Zoho CRM updated the portal user type successfully. The response contains the identifier and name of the updated user type. — Schema: `PutusertypeResponse200` [application/json]
    > Returned on successful update of a portal user type. Contains the identifier and name of the updated user type.
    schema: `PutusertypeResponse200`
    - `user_type` (array of object `UserTypeNested2`) [maxItems=1] **REQ** — An array containing the result of the update operation, including the updated user type identifier.
      schema: `UserTypeNested2`
      - `code` (string) [maxLen=255] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
      - `details` (object `DetailsNested`) — A nested object containing additional detail fields returned with error responses, such as the field API name and JSON path that identify where the validation failure occurred.
        schema: `DetailsNested`
        - `id` (string/int64) [maxLen=255] — Represents the unique numeric identifier of the resource referenced in the error detail.
      - `message` (string) [maxLen=255] — Represents the error message that Zoho CRM returned, describing what went wrong.
      - `status` (string) [maxLen=255] — Represents the result status of the API call. The value is `error` for all error responses.

- **400**: The update request failed because the request body contains invalid data, missing required fields, or a field value that does not satisfy the configured constraints. [application/json]
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
      - `InvalidDataUserTypeBodyError` — Returned when the `user_type` field in the request body contains a value of the wrong data type.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
        - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
          - `expected_data_type` (string) **REQ** [maxLen=255] — The data type that the field value must conform to.
        - `message` (string) **REQ** [enum=['body']] — The error message that Zoho CRM returned, describing what went wrong.
        - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
        - `user_type` (array of object) [maxItems=25] **REQ** — Array of error objects
          oneOf:
            - `SamlInvitationFieldNotAllowedError` — Returned when a create or update request specifies a phone field as the invitation field while SAML authentication is active. SAML-based portals require an email field as the invitation field.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
              - `message` (string) **REQ** [enum=['SAML configured for portal so phone field was not allowed for user types']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `PersonalityModuleChangeNotAllowedError` — Returned when a request attempts to change the personality module of the default portal user type, which is not permitted.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
              - `message` (string) **REQ** [enum=['Change of personality module of default user type is not allowed.']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `InvalidDataTypeError` — Returned when a request body field value is provided in the wrong data type. The `details` object identifies the field and specifies the expected data type.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `expected_data_type` (string) **REQ** [maxLen=255] — The data type that the field value must conform to.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data type']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `InvalidDataMaximumLengthError` — Returned when a request body field value exceeds the maximum allowed character length. The `details` object identifies the field by API name and JSON path, and includes the configured maximum length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `maximum_length` (integer/int32) **REQ** — The maximum character length allowed for the field.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid data']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `InvalidDataMinimumLengthError` — Returned when a request body field value is shorter than the minimum required character length. The `details` object identifies the field and includes the configured minimum length.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
                - `minimum_length` (integer/int32) **REQ** — The minimum character length required for the field.
              - `message` (string) **REQ** [enum=['Invalid data']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `InvalidDataSupportedValuesError` — Returned when a request body field value is not among the allowed values. The `details` object identifies the field and lists the supported values.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
                - `supported_values` (array of string) [maxItems=25] **REQ** — Represents the list of values that are accepted for the field.
                  items: [maxLen=255]
              - `message` (string) **REQ** [enum=['Invalid data']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `ErrorInvalidPersonalityModule` — Returned when the personality module specified in the request body is invalid. The `details` object identifies the field by API name and JSON path.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
              - `message` (string) **REQ** [enum=['Invalid personality module.']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.

- **403**: The authenticated user does not have permission to update portal user types. [application/json]
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

**Scopes:** ZohoCRM.settings.clientportal.ALL, ZohoCRM.settings.clientportal.UPDATE
