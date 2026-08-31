# POST /settings/layouts/{id}/actions/activate
**Operation:** `activateLayout` — Activate Layout
> Activates a single deactivated layout, making it available for use within the specified module. Optionally allows adding or removing profile associations during activation. Only one layout can be activated per request. This operation is idempotent - attempting to activate an already active layout returns an error (ALREADY_ACTIVATED).  The status key in the response from the [Get Layouts API](layouts.yaml#$.paths./settings/layouts.get) indicates whether the layout is active or inactive.

**Parameters:**
- `id` (path, string/int64, required): Specify the unique identifier of the layout to activate or deactivate. Refer to the [Get Layouts](layouts.yaml#$.paths./settings/layouts.get) resource for valid values.
- `module` (query, string, required) [maxLen=100, minLen=1, pattern=^[A-Z][A-Za-z0-9_]*$]: Specify the API name of the module that contains the layout. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.

**Request Body** (required) — application/json `LayoutActivateRequest`
> Request body for activating a single layout with optional profile association modifications. The layout can specify profile associations to add (default) or remove (using _delete flag). Profile modifications are optional - layout can be activated without any profile changes. At least one profile must remain associated with the layout after all operations are applied.
  > Represents the request payload for activating a layout, including the layout identifier and optional profile associations.
  - `layouts` (array of object) [minItems=1, maxItems=1] **REQ** — Specify the array containing exactly one layout object to activate. The layout includes its unique identifier and optionally the profiles to associate or disassociate. Profile associations can be added (default) or removed (using _delete flag). The array must contain exactly one item.
    - `id` (string/int64) **REQ** [maxLen=20, minLen=1, pattern=^[0-9]+$] — Specify the unique identifier of the deactivated layout to activate. Must reference an existing deactivated layout within the specified module. The ID is represented as a string containing a 64-bit integer value. Layout IDs are data center-specific. The status key in the response from the [Get Layouts Metadata API](layouts.yaml#$.paths./settings/layouts.get) indicates whether the layout is **active** or **inactive**.
    - `profiles` (array of object) [maxItems=100] — Specify the profile associations to add to or remove from the layout during activation. Omitting this field or providing an empty array preserves existing profile associations. Refer to the [Get Profiles](profiles.yaml#$.paths./settings/profiles.get) resource for valid values. Use the _delete flag to remove existing associations. Empty array or omitting this field entirely preserves existing profile associations. At least one profile must remain associated with the layout after all operations are applied. While duplicate profile IDs are technically allowed, they cause unnecessary processing and should be avoided.
      - `id` (string/int64) **REQ** [maxLen=20, minLen=1, pattern=^[0-9]+$] — Specify the unique identifier of the profile to associate with or disassociate from the layout. Must be a profile that exists in the CRM organization and is associated with the specified module. The ID is represented as a string containing a 64-bit integer value. Refer to the [Get Profiles](profiles.yaml#$.paths./settings/profiles.get) resource for valid values.
      - `_delete` (boolean) [default=False] — Specify whether to remove this profile's association from the layout. Possible values: **true** - Removes the profile association from the layout. **false** - Adds or retains the profile association on the layout.

**Responses:**

- **200**: Returns the activation confirmation for the layout, including the result code and the activated layout ID. [application/json]
    > Represents the success response returned when a layout is successfully activated.
    - `layouts` (array of object) [minItems=1, maxItems=1] **REQ** — Array containing the result of the layout activation operation. Always returned in the response.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the operation result code. Possible values: **SUCCESS** - Indicates the layout was activated successfully. Always returned in the response.
      - `details` (object) **REQ** — Contains the details of the activated layout. Always returned in the response.
        - `id` (string) **REQ** [maxLen=20, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the activated layout. Always returned in the response.
      - `message` (string) **REQ** [maxLen=200] — Represents the confirmation message for the activation operation. Always returned in the response.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall operation status. Possible values: **success** - Indicates the activation completed without errors. Always returned in the response.

- **400**: The request could not be processed due to invalid parameters, layout constraints, or business rule violations. Resolution: Inspect the **code** field in the response body to identify the specific cause, and verify the layout ID, module name, and profile IDs in the request. [application/json]
    > Represents the error response for bad request scenarios during layout activation, covering invalid layout IDs, layout state violations, and profile association errors.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the request did not complete successfully. Always returned in the response.
        - `code` (string) **REQ** [enum=['INVALID_DATA', 'INVALID_MODULE']] — Represents the error code for the request failure. Possible values: **INVALID_DATA** - Indicates the layout ID provided in the request is invalid. **INVALID_MODULE** - Indicates the specified module is invalid. Always returned in the response.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the invalid data. Always returned in the response.
        - `details` (object) **REQ** — Contains additional context about the invalid data error. Always returned in the response.
          - `resource_path_index` (integer/int32) — Represents the index in the resource path where the error occurred.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the request did not complete successfully. Always returned in the response.
        - `code` (string) **REQ** [enum=['ALREADY_ACTIVATED']] — Represents the error code for the request failure. Possible values: **ALREADY_ACTIVATED** - Indicates the layout is already in active state. Always returned in the response.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message indicating the layout is already in active state. Always returned in the response.
        - `details` (object) **REQ** — Contains additional context about the already-activated layout error. Always returned in the response.
          - `resource_path_index` (integer/int32) — Represents the index in the resource path where the error occurred.
        - `layouts` (array of object) [minItems=1, maxItems=10] **REQ** — Array of error details for each layout that encountered a profile association or permission error. Always returned in the response.
          - `code` (string) **REQ** [enum=['NOT_ALLOWED', 'INVALID_DATA', 'MANDATORY_NOT_FOUND']] — Error code indicating operation is not permitted
          - `details` (object) **REQ** — Additional context about the error
            oneOf:
                - `action` (string) **REQ** [enum=['set_layout_permissions']] — Represents the action that is not permitted on the layout. Possible values: **set_layout_permissions** - Indicates that profile permission modification is not allowed on this layout. Always returned in the response.
                - `id` (string) **REQ** [maxLen=20, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the layout on which the action is restricted. Always returned in the response.
                - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that caused the profile association validation error. Always returned in the response.
                - `json_path` (string) **REQ** [maxLen=200] — Represents the JSONPath location in the request body where the profile association validation error occurred. Always returned in the response.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message explaining the profile association or permission violation. Always returned in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the layout operation did not complete successfully. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the request did not complete successfully. Always returned in the response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request failure. Possible values: **INVALID_DATA** - Indicates the request body contains invalid data, such as an array that exceeds the maximum length. Always returned in the response.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the validation failure. Always returned in the response.
        - `details` (object) **REQ** — Contains validation error details, including the field name and its constraint violation. Always returned in the response.
          - `maximum_length` (integer/int32) **REQ** — Represents the maximum allowed length for the array field that was exceeded. Always returned in the response.
          - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the field that violated the constraint. Always returned in the response.
          - `json_path` (string) **REQ** [maxLen=200] — Represents the JSONPath location of the invalid data in the request body. Always returned in the response.
        - `layouts` (array of object) [minItems=1, maxItems=10] **REQ** — Array of layout-specific error details
          - `code` (string) **REQ** [enum=['CANNOT_PROCESS']] — Error code indicating the operation cannot be processed
          - `details` (object) **REQ** — Additional context about the error (may be empty)
          - `message` (string) **REQ** [maxLen=500] — Human-readable error message explaining why the layout cannot be activated
          - `status` (string) **REQ** [enum=['error']] — Error status indicator

- **403**: User does not have permission to perform this operation [application/json]
    > Error response when the user lacks required permissions to activate layouts
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Error code indicating insufficient permissions
    - `details` (object) **REQ** — Details about the required permissions
      - `permissions` (array of string) [maxItems=10] **REQ** — List of permissions required to perform this operation
        items: [maxLen=100]
    - `message` (string) **REQ** [maxLen=200] — Human-readable error message
    - `status` (string) **REQ** [enum=['error']] — Error status indicator

- **500**: An unexpected error occurred while processing the layout activation request. Resolution: Retry the request. If the issue persists, contact Zoho CRM support. [application/json]
    > Represents the error response returned when an unexpected internal server error occurs during layout activation.
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Represents the error code for the internal server error. Possible values: **INTERNAL_ERROR** - Indicates an unexpected error occurred while processing the request. Always returned in the response.
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the internal server error. Always returned in the response.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the request failed due to an internal server error. Always returned in the response.

**Scopes:** ZohoCRM.settings.layouts.CREATE
