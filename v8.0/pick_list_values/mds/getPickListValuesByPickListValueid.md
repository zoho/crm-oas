# GET /settings/fields/{fieldId}/pick_list_values/{pickListValueId}
**Operation:** `getPickListValuesByPickListValueid` — get a picklist field option
> Picklist field option GET

**Parameters:**
- `module` (query, string, required) [maxLen=50, minLen=1] {style=form, explode=True}: Specify the API name of the CRM module that contains the field. Refer to the [Get Modules](modules.json#$.paths./settings/modules.get) resource for valid values.
- `fieldId` (path, string/int64, required) [minLen=1] {style=simple, explode=False}: Specify the unique numeric identifier of the field. Refer to the [Get Fields Metadata](fields.json#$.paths./settings/fields/{fieldId}.get) resource for valid values.
- `pickListValueId` (path, string/int64, required) [maxLen=255]: Path parameter: pickListValueId

**Responses:**

- **200**: OK - Successful response — Schema: `PicklistOptionLookupResponse` [application/json]
    > Successful response containing the list of picklist options that match the specified pick list value ID for the given field.
    schema: `PicklistOptionLookupResponse`
    - `pick_list_values` (array of object `PicklistOptionDetail`) [minItems=1, maxItems=1] **REQ** — PickList option of the mention picklist unique Id
      schema: `PicklistOptionDetail`
      - `sequence_number` (integer/int32) **REQ** — sort order of the option respective to field
      - `display_value` (string) **REQ** [maxLen=120] — Display value of the picklist option which are localised or translated
      - `reference_value` (string) **REQ** [maxLen=120] — Reference value of the picklist option which are localised or updated
      - `colour_code` (string) **REQ** [maxLen=9, nullable] — Color code of the picklist option when the picklist field in color code enabled
      - `actual_value` (string) **REQ** [maxLen=120] — Actual value of the picklist option.
      - `id` (string/int64) **REQ** — Unique Id of the picklist option
      - `type` (string) **REQ** [enum=['used', 'unused']] — Presence of the option in layouts and in the module
      - `layout_associations` (array of object `PicklistLayoutAssociation`) [minItems=0, maxItems=6, nullable] **REQ** — Layout Association of the picklist option
        schema: `PicklistLayoutAssociation`
        - `api_name` (string) **REQ** [maxLen=255] — Api Name of the layout
        - `name` (string) **REQ** [maxLen=255] — Name of the layout
        - `id` (string/int64) **REQ** — Unique Id of the picklist option

- **204**: No Content - Successful response with no body

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    oneOf:
      - `InvalidFieldIdForPicklistValuesErrorResponse` — Returned when the provided field ID is invalid for retrieving picklist values. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) **REQ** — Detail field: resource_path_index
        - `message` (string) **REQ** [enum=['The Field Id is Invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `InvalidModuleErrorResponse` — Returned when the specified module name is invalid. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) **REQ** [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['the module name given seems to be invalid']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `RequiredModuleParameterMissingErrorResponse` — Returned when the required module parameter is missing. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Error code
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) **REQ** [maxLen=255] — Detail field: param_name
        - `message` (string) **REQ** [enum=['One of the expected parameter is missing']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status
      - `FeatureNotSupportedErrorResponse` — Returned when the requested feature is not supported by the current license. Includes error code, message, status, and details.
        - `code` (string) **REQ** [enum=['FEATURE_NOT_SUPPORTED']] — Error code
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['Your License does not support this feature']] — Error message
        - `status` (string) **REQ** [enum=['error']] — Error status

- **403**: Forbidden - The client does not have access rights to the content. — Schema: `PermissionDeniedErrorResponse` [application/json]
    > Returned when the user lacks permission to access the requested picklist resource. Includes error code, message, status, and details.
    schema: `PermissionDeniedErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code.
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] **REQ** — Detail field: permissions
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Error message
    - `status` (string) **REQ** [enum=['error']] — Error status

**Scopes:** ZohoCRM.settings.fields.READ
