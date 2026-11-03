# GET /settings/automation/functions/actions/associated_modules
**Operation:** `getAssociatedModules` — Get Associated Modules for Automation Functions
> To retrieve the list of modules associated with automation functions in your Zoho CRM organization.

**Responses:**

- **200**: Returns the list of modules associated with automation functions. — Schema: `AssociatedModulesListResponse` [application/json]
    > Represents the response containing the list of modules associated with automation functions.
    schema: `AssociatedModulesListResponse`
    - `associated_modules` (array of object `AssociatedModuleReference`) [maxItems=12] **REQ** — Represents the list of CRM modules associated with the automation functions.
      schema: `AssociatedModuleReference`
      - `api_name` (string) **REQ** [maxLen=255] — Represents the API name of the associated CRM module.
      - `id` (string/int64) **REQ** — Represents the unique ID of the associated CRM module.
  Headers:
    - `X-API-CREDITS-REMAINING` (string)

**Scopes:** ZohoCRM.settings.automation_actions.READ
