# DELETE /settings/layouts/{id}/actions/activate
**Operation:** `layoutDeactivate` — Deactivate Layout
> Deactivates an active layout and transfers its configuration (profile associations, permissions, field mappings) to another active layout within the same module. At least one active layout must remain in the module. This operation is idempotent - attempting to deactivate an already deactivated layout returns an error (ALREADY_DEACTIVATED).

**Parameters:**
- `id` (path, string/int64, required): Specify the unique identifier of the layout to activate or deactivate. Refer to the [Get Layouts](layouts.yaml#$.paths./settings/layouts.get) resource for valid values.
- `module` (query, string, required) [maxLen=100, minLen=1, pattern=^[A-Z][A-Za-z0-9_]*$]: Specify the API name of the module that contains the layout. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.
- `transfer_to` (query, string/int64, required): Specify the unique identifier of an active layout within the same module to which the deactivated layout's profile associations and configuration will be transferred. The target layout must be different from the layout being deactivated. Refer to the [Get Layouts](layouts.yaml#$.paths./settings/layouts.get) resource for valid values.

**Responses:**

- **200**: Returns the deactivation confirmation for the layout, including the result code and the deactivated layout ID. [application/json]
    > Represents the success response returned when a layout is successfully deactivated.
    - `layouts` (array of object) [minItems=1, maxItems=1] **REQ** — Array containing the result of the layout deactivation operation. Always returned in the response.
      - `code` (string) **REQ** [enum=['SUCCESS']] — Represents the operation result code. Possible values: **SUCCESS** - Indicates the layout was deactivated successfully. Always returned in the response.
      - `details` (object) **REQ** — Contains the details of the deactivated layout. Always returned in the response.
        - `id` (string/int64) **REQ** — Represents the unique identifier of the deactivated layout. Always returned in the response.
      - `message` (string) **REQ** [maxLen=200] — Represents the confirmation message for the deactivation operation. Always returned in the response.
      - `status` (string) **REQ** [enum=['success']] — Represents the overall operation status. Possible values: **success** - Indicates the deactivation completed without errors. Always returned in the response.

- **400**: The request could not be processed due to invalid parameters, missing required parameters, layout state violations, or association constraints. Resolution: Inspect the **code** field in the response body to identify the specific cause, and verify the layout ID, module name, and the **transfer_to** parameter value. [application/json]
    > Represents the error response for bad request scenarios during layout deactivation, covering invalid module names, invalid layout IDs, missing parameters, association constraints, and layout state violations.
    oneOf:
        - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the request did not complete successfully. Always returned in the response.
        - `code` (string) **REQ** [enum=['INVALID_MODULE']] — Represents the error code for the request failure. Possible values: **INVALID_MODULE** - Indicates the module name provided in the request is invalid. Always returned in the response.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message indicating the module name is invalid. Always returned in the response.
        - `details` (object) **REQ** — Contains additional context about the invalid module error. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the request did not complete successfully. Always returned in the response.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code for the request failure. Possible values: **INVALID_DATA** - Indicates the provided layout ID or parameter value is invalid. Always returned in the response.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the invalid data. Always returned in the response.
        - `details` (object) **REQ** — Contains additional context about the invalid data error. Always returned in the response.
          oneOf:
              - `param_name` (string) **REQ** [maxLen=100] — Represents the name of the parameter that contains the invalid value. Always returned in the response.
              - `resource_path_index` (integer/int32) — Represents the index in the resource path where the error occurred.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the request did not complete successfully. Always returned in the response.
        - `code` (string) **REQ** [enum=['REQUIRED_PARAM_MISSING']] — Represents the error code for the request failure. Possible values: **REQUIRED_PARAM_MISSING** - Indicates a required parameter is missing from the request. Always returned in the response.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message indicating the missing required parameter. Always returned in the response.
        - `details` (object) **REQ** — Contains the name of the missing required parameter. Always returned in the response.
          - `param_name` (string) **REQ** [maxLen=100] — Represents the name of the missing required parameter. Always returned in the response.
        - `layouts` (array of object) [minItems=1, maxItems=10] **REQ** — Array of error details for each layout that cannot be deactivated due to existing associations. Always returned in the response.
          - `code` (string) **REQ** [enum=['ASSOCIATIONS_EXIST']] — Represents the error code for the layout deactivation failure. Possible values: **ASSOCIATIONS_EXIST** - Indicates the layout has existing dependencies that must be resolved before deactivation. Always returned in the response.
          - `details` (object) **REQ** — Contains the identifier of the layout that has existing associations. Always returned in the response.
            - `id` (string) **REQ** [maxLen=20, minLen=1, pattern=^[0-9]+$] — Represents the unique identifier of the layout that has existing associations preventing deactivation. Always returned in the response.
          - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the association constraint that prevents deactivation. Always returned in the response.
          - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the layout deactivation did not complete successfully. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the request did not complete successfully. Always returned in the response.
        - `code` (string) **REQ** [enum=['NOT_ALLOWED']] — Represents the error code for the request failure. Possible values: **NOT_ALLOWED** - Indicates the transfer target layout is the same as the layout being deactivated. Always returned in the response.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message explaining why the operation is not allowed. Always returned in the response.
        - `details` (object) **REQ** — Contains the name of the parameter that caused the restriction. Always returned in the response.
          - `param_name` (string) **REQ** [maxLen=100] — Represents the name of the parameter that caused the NOT_ALLOWED error. Always returned in the response.
        - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the request did not complete successfully. Always returned in the response.
        - `code` (string) **REQ** [enum=['ALREADY_DEACTIVATED', 'NOT_ALLOWED']] — Represents the error code for the request failure. Possible values: **ALREADY_DEACTIVATED** - Indicates the specified layout is already in an inactive state. **NOT_ALLOWED** - Indicates the operation is not allowed. Always returned in the response.
        - `message` (string) **REQ** [maxLen=500] — Represents the error message indicating the layout is already in inactive state. Always returned in the response.
        - `details` (object) **REQ** — Contains additional context about the already-deactivated layout error. Always returned in the response.
          - `resource_path_index` (integer/int32) — Represents the index in the resource path where the error occurred.
        - `code` (string) **REQ** [enum=['ASSOCIATIONS_EXIST']] — Error code indicating the layout has existing associations preventing deactivation
        - `details` (object) **REQ** — Details about the layout with existing associations
          - `id` (string) **REQ** [maxLen=20, minLen=1, pattern=^[0-9]+$] — The unique identifier of the layout that has existing associations
        - `message` (string) **REQ** [maxLen=500] — Human-readable error message explaining why deactivation is blocked
        - `status` (string) **REQ** [enum=['error']] — Error status indicator

- **403**: The authenticated user does not have the CRM customization permission required to deactivate the layout. **Resolution:** The CRM administrator must grant the layout customization permission (**Customize Zoho CRM**) to the user's profile before retrying. [application/json]
    > Represents the error response returned when the user lacks the CRM customization permission required to deactivate a layout.
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code indicating that the user does not have the permission required to deactivate the layout. Possible values: **NO_PERMISSION** - The user's CRM profile is missing the layout customization permission.
    - `details` (object) **REQ** — Represents additional context about the permissions the user's profile is missing.
      - `permissions` (array of string) [maxItems=10] **REQ** — Represents the list of permissions the user's profile must be granted to deactivate the layout.
        items: [maxLen=100]
    - `message` (string) **REQ** [maxLen=200] — Represents the human-readable error message describing the missing permission.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the response. Possible values: **error** - The request encountered an error and did not complete.

- **500**: An unexpected error occurred while processing the layout deactivation request. Resolution: Retry the request. If the issue persists, contact Zoho CRM support. [application/json]
    > Represents the error response returned when an unexpected internal server error occurs during layout deactivation.
    - `code` (string) **REQ** [enum=['INTERNAL_ERROR']] — Represents the error code for the internal server error. Possible values: **INTERNAL_ERROR** - Indicates an unexpected error occurred while processing the request. Always returned in the response.
    - `message` (string) **REQ** [maxLen=500] — Represents the error message describing the internal server error. Always returned in the response.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status indicator. Possible values: **error** - Indicates the request failed due to an internal server error. Always returned in the response.

**Scopes:** ZohoCRM.settings.layouts.DELETE
