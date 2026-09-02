# GET /settings/variables/{id}/actions/associations
**Operation:** `getVariableAssociations` — Variable Associations
> Get associated variables

**Parameters:**
- `id` (path, string, required) [maxLen=255]: The unique ID of the variable. Mandatory.

**Responses:**

- **200**: OK - Successful response — Schema: `VariableAssociationsResponse` [application/json]
    > Success response containing an array of variable association groups for the requested context.
    schema: `VariableAssociationsResponse`
    - `variables_associations` (array of object `VariableAssociationGroup`) [maxItems=1] **REQ** — Array of variable association groups, each containing the association type and related resources.
      schema: `VariableAssociationGroup`
      - `name` (string) **REQ** [maxLen=255] — The name of the association category (for example, email_templates).
      - `resources` (array of object `VariableAssociationResource`) [maxItems=1] **REQ** — Array of resources associated with this variable under this category.
        schema: `VariableAssociationResource`
        - `name` (string) **REQ** [maxLen=255] — The name of the associated resource.
        - `details` (object `VariableAssociationResourceDetails`) **REQ** — Details about a resource association, including the referenced module.
          schema: `VariableAssociationResourceDetails`
          - `module` (object `AssociationResourceModuleDetails`) **REQ** — Minimal reference to a module used in association details, containing id and apiName.
            schema: `AssociationResourceModuleDetails`
            - `api_name` (string) **REQ** [maxLen=255] — The API name of the CRM module.
            - `id` (string/int64) **REQ** — The unique ID of the CRM module.
        - `id` (string/int64) **REQ** [maxLen=19] — The unique ID of the associated resource.

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
