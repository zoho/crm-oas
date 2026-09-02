# GET /settings/automation/workflow_rules/actions/module_specific_count
**Operation:** `getModuleSpecificActionsCount` — Get Active and Total Workflow Rule Counts by Module

> To retrieve the count of active and total workflow rules configured for each module in your Zoho CRM organization.


**Parameters:**
- `module` (query, string/string, optional): Specifies the CRM module API name to filter workflow rules by, such as Leads, Contacts, or Deals.

**Responses:**

- **200**: Success for specific module — Schema: `ModuleSpecificCountsResponseAllSchema` [application/json]
    > Represents an alternate response model containing the workflow rule counts aggregated by CRM module.
    schema: `ModuleSpecificCountsResponseAllSchema`
    - `module_specific_count` (array of object `ModuleSpecificActionsCountSchema`) [maxItems=500] **REQ** — Represents action counts broken down by CRM module.
      schema: `ModuleSpecificActionsCountSchema`
      - `active_rules_configured` (integer/int32) **REQ** — Represents number of currently active workflow rules configured.
      - `module` (object `ModuleOrFieldNestedSchema`) **REQ** — Represents a CRM module or field reference using its API name and unique numeric ID.
        schema: `ModuleOrFieldNestedSchema`
        - `api_name` (string) **REQ** [maxLen=100] — Represents the API name of the module or field, such as **Leads**, **Contacts**, or a custom field API name.
        - `id` (string) **REQ** [maxLen=20] — Represents the unique numeric ID of the module or field.
      - `total_rules_configured` (integer/int32) **REQ** — Represents total number of workflow rules configured (active + inactive).

- **400**: The response returned when the deletion request is invalid, such as a malformed or missing rule ID. Resolution: verify the rule IDs in the request and resubmit. — Schema: `InvalidDataNoApiNameAndPathSchema` [application/json]
    > Represents the error response returned when a required parameter such as the module API name or field path is missing from the request.
    schema: `InvalidDataNoApiNameAndPathSchema`
    - `code` (string) **REQ** [enum=[9 values]] — Represents the error code that identifies the specific error condition.
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the response status for the error, typically **error**.
    - `details` (object) **REQ** — Represents the error details containing additional context about the failed request.
      - `param_name` (string) [enum=[7 values]] — Represents the **param_name** value from the error detail object.
      - `maximum_length` (integer/int32) — Represents the **maximum_length** value from the error detail object.
      - `id` (string) [maxLen=20] — Represents the **ID** value from the error detail object.
      - `expected_data_type` (string) [maxLen=255] — Represents the **expected_data_type** value from the error detail object.
      - `api_name` (string) [maxLen=255] — Represents the API name of the field or parameter that caused the validation error.

- **403**: Forbidden. The authenticated user does not have permission to perform this operation, or the workflow rules feature is not available in the current CRM edition. Resolution: verify the user's permissions and the organization's edition capabilities.
 — Schema: `NoPermissionSchema` [application/json]
    > Represents the error response returned when the authenticated user does not have permission to access the requested feature or module.
    schema: `NoPermissionSchema`
    - `code` (string) **REQ** [enum=['NO_PERMISSION', 'FEATURE_NOT_SUPPORTED']] — Represents the error code that identifies the specific error condition.
    - `message` (string) **REQ** [maxLen=1000] — Represents the error message describing the issue.
    - `status` (string) **REQ** [enum=['error']] — Represents the response status for the error, typically **error**.
    - `details` (object) **REQ** — Represents error details. For NO_PERMISSION, contains the list of permissions needed. For FEATURE_NOT_SUPPORTED, empty object.
      - `permissions` (array of string) [maxItems=10] — Represents the list of CRM profile permissions required to perform the requested action.
        items: [maxLen=255]

**Scopes:** ZohoCRM.settings.workflow_rules.READ
