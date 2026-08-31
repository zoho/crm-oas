# GET /settings/variable_groups
**Operation:** `getVariableGroups` — Variable Groups
> To retrieve a list of all variable groups in your Zoho CRM organization.

**Responses:**

- **200**: Returns a list of all variable groups in the CRM organization. — Schema: `VariableGroupListResponse` [application/json]
    > Represents the response body for the list variable groups operation.
    schema: `VariableGroupListResponse`
    - `variable_groups` (array of object `VariableGroupSummary`) [maxItems=100] **REQ** — Represents an array of variable group summary objects returned in the list response.
      schema: `VariableGroupSummary`
      - `display_label` (string) **REQ** [maxLen=100] — Represents the display label of the variable group shown in the CRM interface.
      - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the variable group, used to reference the group in API calls.
      - `name` (string) **REQ** [maxLen=50] — Represents the internal name of the variable group.
      - `description` (string) **REQ** [maxLen=3000, nullable] — Represents the description of the variable group. This field is nullable.
      - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the variable group.
      - `source` (string) **REQ** [maxLen=255] — Represents the source of the variable group, indicating whether it is system-defined or user-defined.

- **403**: Returns an error response when the client does not have the required permissions.
**Resolution:** Ensure the OAuth token includes the `ZohoCRM.settings.variable_groups.READ` scope. — Schema: `PermissionDeniedError` [application/json]
    > Represents an error response returned when the client does not have the required permissions to access the variable group settings.
    schema: `PermissionDeniedError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code **NO_PERMISSION**.
    - `details` (object) **REQ** — Represents the validation details containing the list of permissions required to access this resource.
      - `permissions` (array of string) [maxItems=25] — Represents an array of permission names required to perform this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message indicating that access to the resource is denied.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

**Scopes:** ZohoCRM.settings.variable_groups.READ
