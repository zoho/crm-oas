# GET /settings/fields/{fieldId}/pick_list_values
**Operation:** `getPickListValues` — Picklist Values for a Field
> Returns the available pick list values for a specified field in a module, including display values (with translations if enabled), reference values, layout associations, and metadata. Returns 204 if the field exists but is not a pick list type. Does not support pagination.

**Parameters:**
- `fieldId` (path, string/int64, required) [minLen=1] {style=simple, explode=False}: Specify the unique numeric identifier of the field. Refer to the [Get Fields Metadata](fields.json#$.paths./settings/fields/{fieldId}.get) resource for valid values.
- `module` (query, string, required) [maxLen=50, minLen=1] {style=form, explode=True}: Specify the API name of the CRM module that contains the field. Refer to the [Get Modules](modules.json#$.paths./settings/modules.get) resource for valid values.

**Responses:**

- **200**: Returns the list of picklist values for the specified field, including display values, reference values, color codes, usage status, and associated layouts. [application/json]
    > Contains the picklist values with metadata for the specified field, including display names, reference values, color codes, usage status, and layout associations.
    - `pick_list_values` (array of object) [maxItems=2000] **REQ** — Represents the list of picklist value objects retrieved for the specified field.
      - `sequence_number` (integer/int32) **REQ** [min=1] — Represents the display order position of the picklist value in the list.
      - `display_value` (string) **REQ** [maxLen=120] — Represents the translated display value of the picklist option shown to users. When translation is not enabled, this value matches **reference_value**.
      - `reference_value` (string) **REQ** [maxLen=120] — Represents the untranslated reference value of the picklist option used in API operations.
      - `colour_code` (string) **REQ** [maxLen=9, pattern=^#[0-9a-fA-F]{6}$, nullable] — Hexadecimal color code for UI rendering. Null if no color assigned.
      - `actual_value` (string) **REQ** [maxLen=120] — Represents the actual internal value of the picklist option stored in the system.
      - `id` (string/int64) **REQ** — Represents the unique identifier of this pick list value
      - `type` (string) **REQ** [enum=['used', 'unused']] — Represents the usage status of the picklist value in the CRM field. Possible values: **used** - The picklist value is active and available for selection. **unused** - The picklist value is inactive and not available for selection. Always returned in the response.
      - `layout_associations` (array of object) [maxItems=10, nullable] **REQ** — Represents the layouts with which this picklist value is associated. Returns **null** if the value is unused or not associated with any layout. Always returned in the response. Refer to the [Get Layouts](layouts.json#$.paths./settings/layouts.get) endpoint for details. Layout IDs are unique within this array.
        - `api_name` (string) **REQ** [maxLen=50] — Represents the API name of the associated layout.
        - `name` (string) **REQ** [maxLen=40] — Display name of the associated layout
        - `id` (string/int64) **REQ** — Unique identifier of the associated layout

- **204**: The specified field exists in the module but is not a picklist type. The API returns an empty response body.

- **400**: The request failed due to an invalid field ID, an invalid module API name, or an unsupported API version. Resolution: Verify that the field ID in the request URL is valid, the module API name is correct, and the API version is supported. [application/json]
    oneOf:
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code returned when an invalid filed ID is provided in the request.
        - `details` (object) **REQ** — Contains additional context about the invalid field ID error, including the zero-based index of the invalid path parameter.
          - `resource_path_index` (integer/int32) **REQ** [min=0, max=10] — Represents the zero-based index of the invalid path parameter in the request URL, where 2 indicates the **fieldId** position. Always returned in the response.
        - `message` (string) **REQ** [maxLen=255, minLen=1] — Represents the error message describing why the request failed due to an invalid field ID.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. **Possible values:** **error** - The request was not processed successfully.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code returned when an invalid module API name is provided in the request. Possible values: **INVALID_MODULE** - The module API name in the request is invalid. Always returned in the response.
        - `message` (string) **REQ** [maxLen=255, minLen=1] — Represents the error message describing why the request failed due to an invalid module name.
        - `details` (object) **REQ** — Contains additional error context for this response. Returns an empty object for the **INVALID_MODULE** error. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - The request was not processed successfully. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - The request was not processed successfully. Always returned in the response.
        - `code` (string) **REQ** [enum=['VERSION_NOT_SUPPORTED']] — Represents the error code returned when the specified API version is not supported. Possible values: **VERSION_NOT_SUPPORTED** - The API version specified in the request URL is not supported. Always returned in the response.
        - `message` (string) **REQ** [maxLen=255, minLen=1] — Represents the error message describing why the request failed due to an unsupported API version.
        - `details` (object) **REQ** — Contains additional error context for this response. Returns an empty object for the **VERSION_NOT_SUPPORTED** error.

- **403**: Permission denied to access field metadata. Resolution: The CRM administrator must grant the required permission to the user's profile (Crm_Implied_Customize_Zoho_CRM permission). [application/json]
    > Represents the error response when the user does not have the required permissions to access picklist field metadata.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code returned when permission to access field metadata is denied. Possible values: **NO_PERMISSION** - The user does not have the required permission to access this resource. Always returned in the response.
    - `details` (object) **REQ** — Contains additional context about the permission error, including the list of required permissions that are missing.
      - `permissions` (array of string) [minItems=1, maxItems=10, uniqueItems] **REQ** — Represents the list of CRM permissions required to perform this action that are missing from the user's profile. Always returned in the response. Array contains unique permission identifiers; order is not significant.
        items: [maxLen=255, minLen=1]
    - `message` (string) **REQ** [maxLen=255, minLen=1] — Human-readable error message describing the permission denial
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - The request was not processed successfully. Always returned in the response.

**Scopes:** ZohoCRM.settings.fields.READ
