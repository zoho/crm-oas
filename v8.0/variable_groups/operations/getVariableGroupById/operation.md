# GET /settings/variable_groups/{id}
**Operation:** `getVariableGroupById` — Get variable group by ID
> To retrieve the details of a specific variable group by its ID in your Zoho CRM organization.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: Specifies the unique ID of the variable group to retrieve or update.

**Responses:**

- **200**: Returns the details of the variable group matching the specified ID. — Schema: `VariableGroupQueryResponse` [application/json]
    > Represents the response body for the get variable group by ID operation.
    schema: `VariableGroupQueryResponse`
    - `variable_groups` (array of object `VariableGroupSummary`) [maxItems=1] **REQ** — Represents an array containing the variable group matching the specified ID.
      schema: `VariableGroupSummary`
      - `display_label` (string) **REQ** [maxLen=100] — Represents the display label of the variable group shown in the CRM interface.
      - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the variable group, used to reference the group in API calls.
      - `name` (string) **REQ** [maxLen=50] — Represents the internal name of the variable group.
      - `description` (string) **REQ** [maxLen=3000, nullable] — Represents the description of the variable group. This field is nullable.
      - `id` (string) **REQ** [maxLen=19] — Represents the unique ID of the variable group.
      - `source` (string) **REQ** [maxLen=255] — Represents the source of the variable group, indicating whether it is system-defined or user-defined.

- **204**: Returns no content when no variable group is found for the specified ID.

- **400**: Returns an error response when the provided ID in the request path is invalid.
**Resolution:** Verify that the ID is a valid variable group ID before retrying. — Schema: `InvalidIdentifierError` [application/json]
    > Represents an error response returned when the provided ID in the request path is invalid.
    schema: `InvalidIdentifierError`
    - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code **INVALID_DATA**.
    - `details` (object) **REQ** — Represents the validation details indicating the path segment that contains the invalid identifier.
      - `resource_path_index` (integer/int32) — Represents the index of the resource path element that contains the invalid ID.
    - `message` (string) **REQ** [enum=['Invalid ID']] — Represents the error message indicating that the provided ID is invalid.
    - `status` (string) **REQ** [enum=['error']] — Represents the status of the error response. The value is always **error**.

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
