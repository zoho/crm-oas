# GET /settings/variables
**Operation:** `getVariables` — Retrieve all variables
> Retrieves all available CRM variables. Returns the API name, display name, description, type, value, and variable group for each variable. Requires the ZohoCRM.settings.variables.READ scope.

**Responses:**

- **200**: OK - Successful response — Schema: `VariablesListResponse` [application/json]
    > Response wrapper containing an array of variables returned by the list operation.
    schema: `VariablesListResponse`
    - `variables` (array of object `VariableListItem`) [maxItems=200] **REQ** — Array of variable objects, each containing the variable details such as name, API name, type, value, and variable group.
      schema: `VariableListItem`
      - `read_only` (boolean) — Indicates whether the variable is read-only.
      - `api_name` (string) **REQ** [maxLen=100] — The API name of the CRM variable.
      - `name` (string) **REQ** [maxLen=50] — The display name of the variable.
      - `description` (string) **REQ** [maxLen=3000, nullable] — The description of the variable, if any.
      - `id` (string/int64) **REQ** [maxLen=19] — The unique ID of the variable.
      - `source` (string) **REQ** [maxLen=255] — The source of the variable (for example, crm).
      - `type` (string) **REQ** [maxLen=255] — The data type of the variable (for example, text, integer, percent, decimal, currency, date, datetime, email, phone, url, checkbox, textarea, long).
      - `variable_group` (object `VariableGroupSchema`) **REQ** — Base schema for variable_group
        schema: `VariableGroupSchema`
        - `api_name` (string) [maxLen=100] — The API name of the variable group.
        - `name` (string) [maxLen=50] — The display name of the variable group.
        - `id` (string) [maxLen=19] — The unique ID of the variable group.
        additionalProperties: any
      - `value` (string) [maxLen=3000] — The current value of the variable, if any.

- **403**: Forbidden - The client does not have access rights to the content. — Schema: `VariablesPermissionDeniedError` [application/json]
    > Returned when the caller lacks permission to access variables. Includes code NO_PERMISSION and validation details.
    schema: `VariablesPermissionDeniedError`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — Represents the error code.
    - `details` (object) **REQ** — Error details with validation information
      - `permissions` (array of string) [maxItems=25] — The list of required permissions.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message.
    - `status` (string) **REQ** [enum=['error']] — Error status

**Scopes:** ZohoCRM.settings.variables.READ
