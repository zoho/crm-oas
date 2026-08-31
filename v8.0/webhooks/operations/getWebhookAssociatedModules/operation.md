# GET /settings/automation/webhooks/actions/associated_modules
**Operation:** `getWebhookAssociatedModules` — Get webhook-associated modules
> To retrieve the list of CRM modules that have at least one webhook currently associated in your Zoho CRM organization.

Results are filtered based on the requesting user's module access permissions. Use these module API names as valid values for the module filter when querying webhook failures.

**Responses:**

- **200**: Returns the list of CRM modules that have at least one webhook associated. Results are filtered based on the requesting user's module access permissions. — Schema: `AssociatedModulesResponse` [application/json]
    > Represents the response listing CRM modules that have at least one webhook associated.
    schema: `AssociatedModulesResponse`
    - `associated_modules` (array of object `AssociatedModuleReference`) [maxItems=2] — Represents the list of module references that have at least one webhook associated.
      schema: `AssociatedModuleReference`
      - `api_name` (string) [maxLen=255] — Represents the API name of the CRM module.
      - `id` (string) [maxLen=255] — Represents the unique module identifier. Refer to the [Get Modules](modules.yaml#$.paths./settings/modules.get) resource for valid values.

- **403**: Permission denied to retrieve webhook-associated modules in this Zoho CRM organization.

**Resolution:** The CRM administrator must grant the Manage Workflow permission to the user's profile. — Schema: `NoPermissionErrorResponse` [application/json]
    > Represents the error returned when the requesting user does not have the required CRM profile permission to perform the operation.
    schema: `NoPermissionErrorResponse`
    - `code` (string) **REQ** [enum=['NO_PERMISSION']] — The requesting user does not have the required CRM profile permission.
    - `details` (object) **REQ** — Represents the error details containing the list of permissions required for this operation.
      - `permissions` (array of string) [maxItems=25] — Represents the list of CRM profile permissions required to perform this operation.
        items: [maxLen=255]
    - `message` (string) **REQ** [enum=['permission denied']] — Represents the error message describing the failure.

Possible values:
**permission denied** - The requesting user lacks the required CRM profile permission for this operation.
    - `status` (string) **REQ** [enum=['error']] — Represents the error status.
Possible values:
**error** - Indicates the request did not complete successfully.

**Scopes:** ZohoCRM.settings.automation_actions.READ
