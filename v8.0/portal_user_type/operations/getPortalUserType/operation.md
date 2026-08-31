# GET /settings/portals/{portal}/user_type/{userTypeId}
**Operation:** `getPortalUserType` — Portal User Type
> Retrieves the full configuration of a single portal user type, including identity fields, active status, user counts, audit metadata, personality module, invitation field, and per-module access permissions.

**Parameters:**
- `portal` (path, string, required) [maxLen=255]: Specify the API name of the portal whose user types are being managed. This is the unique identifier for the portal in Zoho CRM.
- `userTypeId` (path, string/int64, required) [maxLen=255]: Provide the unique numeric identifier of the portal user type to retrieve, update, or delete.
- `include_inner_details` (query, string, optional) [enum=['field.field_label']]: When set to `fields` or another resource key, the response includes the detailed fields or sub-resource properties for the included modules.

**Responses:**

- **200**: Zoho CRM returned the full configuration of the requested portal user type successfully. — Schema: `GetusertypeByIdResponse200` [application/json]
    > Returned on a successful request to retrieve a single portal user type by ID. Contains the full configuration of the requested user type.
    schema: `GetusertypeByIdResponse200`
    - `user_type` (array of object `GETUserTypeByIdNested`) [maxItems=1] **REQ** — An array containing the full configuration of the requested portal user type. Always contains exactly one entry.
      schema: `GETUserTypeByIdNested`
      - `default` (boolean) **REQ** — Whether this is the default portal user type in the organization. The default user type is automatically assigned when no explicit user type is specified.
      - `active_user_count` (integer/int32) **REQ** — Represents the number of portal users currently assigned to and active under this user type.
      - `personality_module` (object `GETPersonalityModuleNested`) **REQ** — Represents the nested object identifying the personality module configured for the portal user type. The personality module is the CRM module (for example, Contacts) whose records serve as portal user identities.
        schema: `GETPersonalityModuleNested`
        - `plural_label` (string) **REQ** [maxLen=255] — Represents the plural label of the module.
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM module configured as the personality module for this portal user type.
        - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique numeric identifier of the personality module in Zoho CRM.
      - `name` (string) **REQ** [maxLen=255] — Represents the name of the portal user type.
      - `active` (boolean) **REQ** — Indicates whether the portal user type is currently active and available to portal users.
      - `invitation_field` (object `GETInvitationFieldNested`) **REQ** — The invitation field configured for the portal user type. This is the CRM field used to store the portal user's email address, to which portal invitations are sent.
        schema: `GETInvitationFieldNested`
        - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the CRM field designated as the invitation field for sending portal invitations.
        - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique numeric identifier of the invitation field in Zoho CRM.
      - `id` (string/int64) **REQ** [maxLen=255] — Represents the unique numeric identifier of the portal user type.
      - `deactive_user_count` (integer/int32) **REQ** — Represents the number of portal users assigned to this user type who have been deactivated.
      - `modules` (array of object `ModulesNested`) [maxItems=500] **REQ** — The list of CRM modules that portal users of this type are permitted to access, along with the permissions and layouts configured for each module.
        schema: `ModulesNested`
        - `plural_label` (string) [maxLen=255, nullable] — Represents the plural display label of the CRM module.
        - `shared_type` (string) **REQ** [maxLen=255, minLen=6, enum=['private', 'public']] — Specifies how records in this module are shared with portal users. This field is required. Possible values: `all_records`, `selected_records`, `related_records`.
        - `api_name` (string) [maxLen=25, pattern=^[A-Za-z0-9_]{1,25}$] — Represents the API name that uniquely identifies the CRM module being granted portal access.
        - `permissions` (object `PermissionsNested`) **REQ** — The access permissions granted to portal users for this module. The `view` permission is required; all other permissions are optional and module-dependent.
          schema: `PermissionsNested`
          - `view` (boolean) **REQ** — Denotes whether portal users can view records in this module. View permission must be `true` for any other permission to take effect.
          - `delete_attachment` (boolean) [nullable] — Denotes whether portal users can delete attachments from notes associated with records in this module.
          - `edit` (boolean) [nullable] — Denotes whether portal users can edit records in this module that they created. Set to `true` to enable edit access for portal-user-created records.
          - `edit_shared_records` (boolean) [nullable] — Denotes whether portal users can edit records in this module that were shared with them from CRM, but not created by them.
          - `create` (boolean) [nullable] — Denotes whether portal users can create new records in this module. Set to `true` to enable create access.
          - `create_attachment` (boolean) [nullable] — Denotes whether portal users can add attachments to notes associated with records in this module.
          - `delete` (boolean) [nullable] — Denotes whether portal users can delete records in this module. Set to `true` to enable delete access.
        - `id` (string) **REQ** [maxLen=25, pattern=^[0-9]+$] — Represents the unique identifier of the CRM module. This field is required when specifying module access in a portal user type.
        - `filters` (array of object `FilterFieldNested`) [maxItems=1, nullable] — Represents the list of filter field configurations that portal users can use to filter records in this module.
          schema: `FilterFieldNested`
          - `display_label` (string) [maxLen=50] — Represents the display label shown to portal users for the filter field.
          - `api_name` (string) [maxLen=256] — Represents the API name that uniquely identifies the filter field within the CRM module.
          - `id` (string) [maxLen=25, pattern=^[0-9]+$] — Represents the unique numeric identifier of the filter field in Zoho CRM.
        - `fields` (array of object `FieldsNested`) [maxItems=500, nullable] — Represents the list of CRM fields within this module that portal users are permitted to access. Each entry specifies the field identifier, API name, read-only flag, and per-field CRUD permissions.
          schema: `FieldsNested`
          - `read_only` (boolean) [nullable] — Denotes whether the field is read-only for portal users. When `true`, portal users can view the field value but cannot modify it.
          - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — The API name of the CRM field accessible to portal users within this module.
          - `id` (string/int64) — The unique numeric identifier of the CRM field.
          - `permissions` (array of object) [maxItems=25] — Represents the list of CRUD permission entries that control what portal users can do with this field.
            - `iscustomizable` (boolean) **REQ** — Whether the field permission for this action can be customized per portal user type.
            - `view` (boolean) — Whether portal users can view the value of this field.
            - `edit` (boolean) — Whether portal users can edit the value of this field on existing records.
            - `create` (boolean) — Whether portal users can set a value for this field when creating a record.
            - `delete` (boolean) — Whether portal users can delete records that have this field.
        - `layouts` (array of object `LayoutsNested`) [maxItems=7, nullable] — The list of CRM layouts that portal users can access within this module.
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
        - `views` (object `ViewsNested`) — The list view (canvas view or custom view) visible to portal users when browsing records in this module.
          schema: `ViewsNested`
          - `display_label` (string) [maxLen=255] — Represents the display label of the list view shown to portal users.
          - `name` (string) [maxLen=255] — Represents the name of the resource.
          - `id` (string) [maxLen=25, pattern=^[0-9]+$] — Represents the unique identifier of the resource.
          - `type` (string) [maxLen=255, enum=['canvas_view', 'custom_view']] — The type of the list view. Possible values: `canvas_view` (Canvas View), `custom_view` (Custom List View).

- **400**: The request failed because the `{userTypeId}` path parameter references a user type that does not exist, or the request is otherwise invalid. [application/json]
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

- **403**: The authenticated user does not have permission to view portal user type configuration. [application/json]
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
