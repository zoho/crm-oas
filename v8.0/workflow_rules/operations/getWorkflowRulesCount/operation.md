# GET /settings/automation/workflow_rules/actions/rules_count
**Operation:** `getWorkflowRulesCount` — Get Workflow Rule Quota and Usage Counts

> To retrieve the organization-level quota and current usage counts for workflow rules and actions in your Zoho CRM organization. The response includes the total and active rule limits (both organization-wide and per module), the number of rules currently configured, and the per-rule limits for actions and scheduled action groups.


**Responses:**

- **200**: Returns the organization-level workflow rule quota and current usage counts.
 — Schema: `WorkflowRulesCountResponseSchema` [application/json]
    > Represents the response body containing the organization-level workflow rule quota and current usage counts.
    schema: `WorkflowRulesCountResponseSchema`
    - `rules_count` (object) **REQ** — Represents the workflow rule count and limit details for the organization.
      - `scheduled_actions_per_rule_limit` (integer/int32) **REQ** — Represents the maximum number of scheduled action groups allowed per workflow rule.
      - `total_rules_limit` (integer/int32) **REQ** — Represents the maximum total number of workflow rules allowed in the organization.
      - `active_rules_configured` (integer/int32) **REQ** — Represents the number of currently active workflow rules configured in the organization.
      - `rules_per_process_limit` (integer/int32) **REQ** — Represents the maximum number of workflow rules allowed per business process.
      - `total_actions_per_rule_limit` (integer/int32) **REQ** — Represents the maximum total number of actions (instant and scheduled combined) allowed per workflow rule.
      - `total_rules_limit_per_module` (integer/int32) **REQ** — Represents the maximum number of workflow rules allowed per CRM module.
      - `active_rules_limit` (integer/int32) **REQ** — Represents the maximum number of active workflow rules allowed in the organization.
      - `total_rules_configured` (integer/int32) **REQ** — Represents the total number of workflow rules configured in the organization, including both active and inactive rules.
      - `active_rules_limit_per_module` (integer/int32) **REQ** — Represents the maximum number of active workflow rules allowed per CRM module.

- **403**: The caller does not have permission to retrieve workflow rule counts, or the feature is not available in the current Zoho CRM edition.
**Resolution:** The CRM administrator must grant the `Crm_Implied_Manage_Workflow` permission to the user's profile in Zoho CRM.
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
