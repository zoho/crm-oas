# GET /settings/variables/{id}
**Operation:** `getVariableById` — specific variable
> Retrieves the details of a specific CRM variable by its ID. The group query parameter, specifying the variable group ID or API name, is mandatory when retrieving a specific variable. Requires the ZohoCRM.settings.variables.READ scope.

**Parameters:**
- `id` (path, string, required) [maxLen=255]: The unique ID of the variable. Mandatory.
- `group` (query, string/int64, optional) {style=form, explode=True}: The unique ID or API name of the variable group to which the variable belongs. Mandatory when retrieving a specific variable by ID.

**Responses:**

- **200**: OK - Successful response — Schema: `VariablesbyGroupResponse` [application/json]
    > Collection wrapper returning variables associated with the specified group identifier.
    schema: `VariablesbyGroupResponse`
    - `variables` (array of object `VariableListItem`) [maxItems=25] **REQ** — Array of variable operation results.
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

- **400**: Bad Request - The request cannot be processed due to invalid syntax. [application/json]
    > Error response for invalid request
    oneOf:
      - `VariableGroupInvalidIDError` — Indicates an invalid variable group identifier in the request path. Includes code INVALID_DATA and validation details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `param_name` (string) [maxLen=255] — The name of the parameter that caused the error.
        - `message` (string) **REQ** [enum=['Invalid data']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
      - `InvalidUrlPatternError` — Returned when the requested URL does not match a supported pattern. Includes code INVALID_URL_PATTERN.
        - `code` (string) **REQ** [enum=['INVALID_URL_PATTERN']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
        - `message` (string) **REQ** [enum=['Please check if the URL trying to access is a correct one']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.
      - `InvalidResourceIdError` — Indicates an invalid identifier in the request URL. Includes code INVALID_DATA and contextual details.
        - `code` (string) **REQ** [enum=['INVALID_DATA']] — Represents the error code.
        - `details` (object) **REQ** — Error details with validation information
          - `resource_path_index` (integer/int32) — The index of the invalid resource in the URL path.
        - `message` (string) **REQ** [enum=['invalid data']] — Represents the error message.
        - `status` (string) **REQ** [enum=['error']] — Represents the status of the error.

**Scopes:** ZohoCRM.settings.variables.READ
