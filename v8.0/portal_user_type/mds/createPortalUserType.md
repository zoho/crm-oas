# POST /settings/portals/{portal}/user_type
**Operation:** `createPortalUserType` — Portal User Type
> Creates a new portal user type for the specified portal. A portal user type defines the personality module, invitation field, and per-module access permissions for portal users. The portal must already exist in the organization's Zoho CRM account.

**Parameters:**
- `portal` (path, string, required) [maxLen=255]: Specify the API name of the portal whose user types are being managed. This is the unique identifier for the portal in Zoho CRM.

**Schemas:**
`DefaultViewLayoutNested`:
  > Nested schema for _default_view when type is layout
  - `display_label` (string) [maxLen=255] — Represents the display label of the default layout view.
  - `name` (string) [maxLen=255] — Represents the internal name of the default view.
  - `id` (string) [maxLen=25, pattern=^[0-9]+$] — Represents the unique numeric identifier of the default view.
  - `type` (string) [maxLen=255, enum=['layout']] — The type of the default view.
`DefaultViewNested`:
  oneOf:
    - `DefaultViewLayoutNested` — Nested schema for _default_view when type is layout
    - `DefaultViewWizardNested` — Nested schema for _default_view when type is wizard
`DefaultViewWizardNested`:
  > Nested schema for _default_view when type is wizard
  - `display_label` (string) [maxLen=255] — The display label of the resource
  - `name` (string) [maxLen=255] — The name of the resource
  - `id` (string/int64) [maxLen=19] — The unique identifier of the resource
  - `type` (string) [maxLen=255, enum=['wizard']] — The type of the resource
`FieldsNested`:
  > Represents a field that is accessible to portal users for the configured module. Includes the field's unique identifier, API name, read-only flag, and the list of per-field CRUD permissions.
  - `read_only` (boolean) [nullable] — Denotes whether the field is read-only for portal users. When `true`, portal users can view the field value but cannot modify it.
  - `api_name` (string) [maxLen=50, pattern=^[A-Za-z][A-Za-z0-9_]*$] — The API name of the CRM field accessible to portal users within this module.
  - `id` (string/int64) — The unique numeric identifier of the CRM field.
  - `permissions` (array of object) [maxItems=25] — Represents the list of CRUD permission entries that control what portal users can do with this field.
    - `iscustomizable` (boolean) **REQ** — Whether the field permission for this action can be customized per portal user type.
    - `view` (boolean) — Whether portal users can view the value of this field.
    - `edit` (boolean) — Whether portal users can edit the value of this field on existing records.
    - `create` (boolean) — Whether portal users can set a value for this field when creating a record.
    - `delete` (boolean) — Whether portal users can delete records that have this field.
`FilterFieldNested`:
  > A nested object representing a filter field available for a module in the portal user type, identified by its unique ID, API name, and display label.
  - `display_label` (string) [maxLen=50] — Represents the display label shown to portal users for the filter field.
  - `api_name` (string) [maxLen=256] — Represents the API name that uniquely identifies the filter field within the CRM module.
  - `id` (string) [maxLen=25, pattern=^[0-9]+$] — Represents the unique numeric identifier of the filter field in Zoho CRM.
`InvitationFieldNested`:
  > The CRM field used as the invitation field for this portal user type. Portal invitations are sent to the contact value stored in this field. Required when creating a user type.
  - `api_name` (string) [maxLen=255, nullable] — Represents the API name of the CRM field to use as the invitation field for this portal user type.
  - `id` (string/int64) — Represents the unique numeric identifier of the CRM field to use as the invitation field.
`LayoutsNested`:
  > Represents the nested object representing a CRM layout that portal users can access for a given module. Identified by a unique numeric ID, name, and display label.
  - `display_label` (string) [maxLen=255] — Represents the display label of the CRM layout.
  - `name` (string) [maxLen=255] — Represents the internal name of the CRM layout.
  - `id` (string) [maxLen=25, pattern=^[0-9]+$] — Specifies the unique identifier of the CRM layout.
  - `_default_view` (object `DefaultViewNested`) — Nested schema for _default_view representing the default view configuration associated with the portal user type, including the view's unique identifier, name, display label, and type.
`ModulesNested`:
  > Represents a CRM module to which the portal user type grants access. Includes the module's unique identifier, API name, shared type, plural label, and the lists of allowed layouts, filter fields, and field-level permissions.
  - `plural_label` (string) [maxLen=255, nullable] — Represents the plural display label of the CRM module.
  - `shared_type` (string) **REQ** [maxLen=255, minLen=6, enum=['private', 'public']] — Specifies how records in this module are shared with portal users. This field is required. Possible values: `all_records`, `selected_records`, `related_records`.
  - `api_name` (string) [maxLen=25, pattern=^[A-Za-z0-9_]{1,25}$] — Represents the API name that uniquely identifies the CRM module being granted portal access.
  - `permissions` (object `PermissionsNested`) **REQ** — The access permissions granted to portal users for this module. The `view` permission is required; all other permissions are optional and module-dependent.
  - `id` (string) **REQ** [maxLen=25, pattern=^[0-9]+$] — Represents the unique identifier of the CRM module. This field is required when specifying module access in a portal user type.
  - `filters` (array of object `FilterFieldNested`) [maxItems=1, nullable] — Represents the list of filter field configurations that portal users can use to filter records in this module.
  - `fields` (array of object `FieldsNested`) [maxItems=500, nullable] — Represents the list of CRM fields within this module that portal users are permitted to access. Each entry specifies the field identifier, API name, read-only flag, and per-field CRUD permissions.
  - `layouts` (array of object `LayoutsNested`) [maxItems=7, nullable] — The list of CRM layouts that portal users can access within this module.
  - `views` (object `ViewsNested`) — The list view (canvas view or custom view) visible to portal users when browsing records in this module.
`PermissionsNested`:
  > The access permissions granted to portal users for this module. The `view` permission is required; all other permissions are optional and module-dependent.
  - `view` (boolean) **REQ** — Denotes whether portal users can view records in this module. View permission must be `true` for any other permission to take effect.
  - `delete_attachment` (boolean) [nullable] — Denotes whether portal users can delete attachments from notes associated with records in this module.
  - `edit` (boolean) [nullable] — Denotes whether portal users can edit records in this module that they created. Set to `true` to enable edit access for portal-user-created records.
  - `edit_shared_records` (boolean) [nullable] — Denotes whether portal users can edit records in this module that were shared with them from CRM, but not created by them.
  - `create` (boolean) [nullable] — Denotes whether portal users can create new records in this module. Set to `true` to enable create access.
  - `create_attachment` (boolean) [nullable] — Denotes whether portal users can add attachments to notes associated with records in this module.
  - `delete` (boolean) [nullable] — Denotes whether portal users can delete records in this module. Set to `true` to enable delete access.
`ViewsNested`:
  > The list view (canvas view or custom view) visible to portal users when browsing records in this module.
  - `display_label` (string) [maxLen=255] — Represents the display label of the list view shown to portal users.
  - `name` (string) [maxLen=255] — Represents the name of the resource.
  - `id` (string) [maxLen=25, pattern=^[0-9]+$] — Represents the unique identifier of the resource.
  - `type` (string) [maxLen=255, enum=['canvas_view', 'custom_view']] — The type of the list view. Possible values: `canvas_view` (Canvas View), `custom_view` (Custom List View).

**Request Body** — application/json `PostusertypeRequest`
> The request body containing the portal user type configuration to create. Must include the personality module, invitation field, active status, and the list of CRM modules with their access permissions.
  > The request body schema for the create portal user type operation. Contains the `user_type` array with the configuration of the user type to be created.
  - `user_type` (array of object `UserTypeNested`) [maxItems=1] **REQ** — An array containing the portal user type configuration to create. Must contain exactly one user type object.
    schema: `UserTypeNested`
    - `personality_module` (object `PersonalityModuleNested`) **REQ** — The personality module for this portal user type. Records in this module serve as portal user identities, and portal invitations are sent to records in this module. Required when creating a user type.
      schema: `PersonalityModuleNested`
      - `api_name` (string) [maxLen=25, pattern=^[A-Za-z0-9_]{1,25}$] — Represents the API Name of the Personality Module.
      - `id` (string/int64) [maxLen=18] — The unique numeric identifier of the personality module in Zoho CRM.
    - `name` (string) **REQ** [maxLen=50, minLen=1, pattern=^[A-Za-z0-9 ]+$] — The display name of the portal user type. For example, "Client Portal", "Vendor Portal", or "Partner Portal". Must be alphanumeric with spaces only, maximum 50 characters.
    - `active` (boolean) [nullable] — Indicates whether the portal user type is active. Set to `true` to allow portal users to access the portal via this user type, or `false` to deactivate it.
    - `invitation_field` (object `InvitationFieldNested`) **REQ** — The CRM field used as the invitation field for this portal user type. Portal invitations are sent to the contact value stored in this field. Required when creating a user type.
    - `id` (string/int64) [maxLen=18, readOnly] — Denotes the unique numeric identifier of the portal user type.
    - `deactive_user_count` (integer/int32) [nullable] — The number of portal users assigned to this user type who are currently deactivated.
    - `modules` (array of object `ModulesNested`) [maxItems=500] **REQ** — The list of CRM modules with their access configurations for this portal user type. Required when creating a user type.

**Responses:**

- **201**: Zoho CRM created the portal user type successfully. The response contains the identifier and name of the newly created user type. — Schema: `PostusertypeResponse201` [application/json]
    > Returned on successful creation of a new portal user type. Contains the identifier and name of the newly created user type.
    schema: `PostusertypeResponse201`
    - `user_type` (array of object `UserTypeNested1`) [maxItems=1] **REQ** — An array containing the full configuration of the newly created portal user type, including its generated identifier.
      schema: `UserTypeNested1`
      - `default` (boolean) — Indicates whether this is the default portal user type in the organization. The default user type is created automatically when the portal is set up, using Contacts as the personality module.
      - `personality_module` (object `PersonalityModuleNested1`) — Represents the nested object representing the personality module as returned in response bodies, containing the module's unique identifier, API name, and display label.
        schema: `PersonalityModuleNested1`
        - `plural_label` (string) [maxLen=255] — Represents the plural label of the module.
        - `api_name` (string) [maxLen=255] — Represents the API name of the resource.
        - `id` (string/int64) [maxLen=255] — Represents the unique identifier of the resource.
      - `name` (string) [maxLen=255] — Represents the name of the resource.
      - `active` (boolean) — Indicates whether the portal user type is currently active and available to portal users.
      - `invitation_field` (object `InvitationFieldNested`) — Represents the nested object used in create and update requests to specify the invitation field for the portal user type. The invitation field determines which CRM field stores the portal user's email address for sending invitations.
      - `id` (string/int64) [maxLen=255] — Indicates the unique identifier of the resource.
      - `modules` (array of object `ModulesNested`) [maxItems=4] — Represents the array of modules associated with the user type.

- **400**: The create request failed because the request body contains invalid data, missing required fields, or a field value that does not satisfy the configured constraints. [application/json]
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
            - `LayoutMissingSelectedFilterError` — Returned when the selected filter-by field is not included in the specified layout. The filter field must be part of the chosen layout.
              - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
              - `message` (string) **REQ** [enum=['Layout does not have selected filter in it.']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `LayoutFieldMissingError` — Returned when a layout's required field is absent from the request body. The `details` object identifies the missing field by API name and JSON path, and includes the dependent field reference.
              - `code` (string) **REQ** [enum=['DEPENDENT_FIELD_MISSING']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `dependee` (object) **REQ** — The dependent field object that is required but missing from the request body.
                  - `api_name` (string) **REQ** [maxLen=255] — The API name of the dependent field.
                  - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the dependent field in the request body.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
              - `message` (string) **REQ** [enum=['layouts are missing.']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `PrivateModulePermissionsRequiredError` — Returned when the request attempts to configure a private CRM module without providing the required permissions. Private modules require explicit permission assignments.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
              - `message` (string) **REQ** [enum=['required field not found']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `LicenseLimitExceededError` — Returned when the organization has reached the maximum number of portal user types allowed under its current Zoho CRM license plan.
              - `code` (string) **REQ** [enum=['LICENSE_LIMIT_EXCEEDED']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
              - `message` (string) **REQ** [enum=['License limit exceeded.']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `FieldNotAllowedInPortalsError` — Returned when the request includes a field that is not supported in client portals. The `details` object specifies the field that caused the error.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
              - `message` (string) **REQ** [enum=['Field is not allowed in portals.']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `MandatoryPersonalityAndNotesModulesError` — Returned when the request body does not include both the personality module and the Notes module, which are mandatory when configuring module access for a portal user type.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
              - `message` (string) **REQ** [enum=['Personality module and Notes module are mandatory modules.']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `InvalidUserTypeNameSpecialCharsError` — Returned when the portal user type name contains special characters that are not permitted. Only alphanumeric characters and underscores are allowed in user type names.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `regex` (string) **REQ** [maxLen=255] — The regular expression pattern that the field value must match.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
              - `message` (string) **REQ** [enum=['invalid data']] — The error message that Zoho CRM returned, describing what went wrong.
              - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.
            - `MandatoryFieldMissingError` — Returned when a required field is absent from the request body. The `details` object identifies the missing field by API name and JSON path.
              - `code` (string) **REQ** [enum=['MANDATORY_NOT_FOUND']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
              - `message` (string) **REQ** [enum=['Required field is missing']] — The error message that Zoho CRM returned, describing what went wrong.
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
            - `InvalidDataRegexError` — Returned when a request body field value does not match the required regular expression pattern. The `details` object identifies the field and specifies the expected regex pattern.
              - `code` (string) **REQ** [enum=['INVALID_DATA']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
              - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
                - `regex` (string) **REQ** [maxLen=255] — The regular expression pattern that the field value must match.
                - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
                - `json_path` (string) **REQ** [maxLen=1000] — The JSON path to the request body field that caused the error.
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
      - `RequiredParamMissingError` — Returned when the request body is missing the `read_only` field, which is required when specifying field-level permissions for a portal user type module.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — The error code that identifies the type of error. For example, `INVALID_DATA` or `MANDATORY_NOT_FOUND`.
        - `details` (object) **REQ** — An object containing additional detail fields that identify the specific request body field responsible for the error.
          - `api_name` (string) **REQ** [maxLen=255] — The API name of the request body field that caused the error.
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — The error message that Zoho CRM returned, describing what went wrong.
        - `status` (string) **REQ** [enum=['error']] — The result status of the API call. The value is `error` for all error responses.

- **403**: The authenticated user does not have permission to create portal user types, or the portal configuration prevents this operation. [application/json]
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

**Scopes:** ZohoCRM.settings.clientportal.ALL, ZohoCRM.settings.clientportal.CREATE
